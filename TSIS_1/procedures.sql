CREATE OR REPLACE PROCEDURE add_phone(p_contact_name VARCHAR, p_phone VARCHAR, p_type VARCHAR)
AS $$
BEGIN
    INSERT INTO phones (contact_id, phone, type)
    SELECT id, p_phone, p_type FROM phonebook WHERE name = p_contact_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE move_to_group(p_contact_name VARCHAR, p_group_name VARCHAR)
AS $$
DECLARE
    v_id INT;
BEGIN
    INSERT INTO groups (name) VALUES (p_group_name)
    ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
    RETURNING id INTO v_id;
    UPDATE phonebook SET group_id = v_id WHERE name = p_contact_name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION search_contacts_advanced(p_query TEXT)
RETURNS TABLE(res_id INT, res_name VARCHAR, res_email VARCHAR, all_phones TEXT) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.email, string_agg(p.phone, ', ')
    FROM phonebook c
    LEFT JOIN phones p ON c.id = p.contact_id
    WHERE c.name ILIKE '%' || p_query || '%'
       OR c.email ILIKE '%' || p_query || '%'
       OR p.phone ILIKE '%' || p_query || '%'
    GROUP BY c.id;
END;
$$ LANGUAGE plpgsql;
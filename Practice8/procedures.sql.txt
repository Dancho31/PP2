-- Insert new contact or update phone if name already exists
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_name) THEN
        UPDATE phonebook SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO phonebook (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;

-- Insert multiple users with phone length validation
CREATE OR REPLACE PROCEDURE insert_many_users(names VARCHAR[], phones VARCHAR[], OUT errors TEXT[])
AS $$
DECLARE
    i INT;
BEGIN
    errors := '{}';
    FOR i IN 1..array_length(names, 1) LOOP
        -- If phone is shorter than 6 digits, it's considered invalid
        IF length(phones[i]) < 6 THEN
            errors := array_append(errors, names[i] || ':' || phones[i]);
        ELSE
            INSERT INTO phonebook (name, phone) VALUES (names[i], phones[i]);
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Delete a contact by name or phone number
CREATE OR REPLACE PROCEDURE delete_contact_by_data(target TEXT)
AS $$
BEGIN
    DELETE FROM phonebook WHERE name = target OR phone = target;
END;
$$ LANGUAGE plpgsql;
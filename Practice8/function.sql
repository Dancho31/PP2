-- Search contacts by name or phone pattern
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    WHERE phonebook.name ILIKE '%' || pattern || '%' 
       OR phonebook.phone ILIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

-- Get contacts with limit and offset (pagination)
CREATE OR REPLACE FUNCTION get_contacts_paged(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY 
    SELECT * FROM phonebook 
    ORDER BY contact_id 
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;
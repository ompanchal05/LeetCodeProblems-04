-- 175. Combine Two Tables 

SELECT 
    first_name,
    last_name,
    city,
    state
FROM Person
LEFT JOIN Address 
ON Person.personId = Address.personId;
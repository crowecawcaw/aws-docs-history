# Prefer the properties function over individual property lookup when

retrieving all property values

The `properties()` function is used to return a map containing all properties for an entity, and is much
more efficient than returning properties individually.

Assuming your `Person` nodes contain 5 properties, `firstName`, `lastName`,
`age`, `dept`, and `company`, the following query would be preferred:

```
MATCH (n:Person)
WHERE n.dept = 'AWS'
RETURN properties(n) as personDetails
```

Rather than using:

```
MATCH (n:Person)
WHERE n.dept = 'AWS'
RETURN n.firstName, n.lastName, n.age, n.dept, n.company

=== OR ===

MATCH (n:Person)
WHERE n.dept = 'AWS'
RETURN {firstName: n.firstName, lastName: n.lastName, age: n.age,
department: n.dept, company: n.company} as personDetails
```

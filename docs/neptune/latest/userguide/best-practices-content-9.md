# Explicitly check whether properties exist

Based on openCypher semantics, when a property is accessed it is equivalent to an optional join and must retain all
rows even if the property does not exist. If you know based on your graph schema that a particular property will always
exist for that entity, explicitly checking that property for existence allows the query engine to create optimal plans
and improve performance.

Consider a graph model where nodes of type `person` always have a property `name`. Instead of
doing this:

```
MATCH (n:person)
RETURN n.name
```

Explicitly verify the property existence in the query with an IS NOT NULL check:

```
MATCH (n:person)
WHERE n.name IS NOT NULL
RETURN n.name
```

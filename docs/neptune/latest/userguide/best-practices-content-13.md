# Perform static computations outside of the query

It is recommended to resolve static computations (simple mathematical/string operations) on the client-side.
Consider this example where you want to find all people one year older or less than the author:

```
MATCH (m:Message)-[:HAS_CREATOR]->(p:person)
WHERE p.age <= ($age + 1)
RETURN m
```

Here, `$age` is injected into the query via parameters, and is then added to a fixed value. This value is
then compared with `p.age`. Instead, a better approach would be doing the addition on the client-side
and passing the calculated value as a parameter $ageplusone. This helps the query engine to create optimized plans, and
avoids static computation for each incoming row. Following these guidelines, a more efficient verson of the query
would be:

```
MATCH (m:Message)-[:HAS_CREATOR]->(p:person)
WHERE p.age <= $ageplusone
RETURN m
```

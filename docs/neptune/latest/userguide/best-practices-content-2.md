# Use parameterized queries

It is recommended to always use parameterized queries when querying using openCypher. The query engine can leverage
repeated parameterized queries for features like query plan cache, where repeated invocation of the same parameterized
structure with different parameters can leverage the cached plans. The query plan generated for parameterized queries
is cached and reused only when it completes within 100ms and the parameter types are either NUMBER, BOOLEAN or STRING.

Use:

```
MATCH (n:foo) WHERE id(n) = $id RETURN n
```

With parameters:

```
parameters={"id": "first"}
parameters={"id": "second"}
parameters={"id": "third"}
```

Instead of:

```
MATCH (n:foo) WHERE id(n) = "first" RETURN n
MATCH (n:foo) WHERE id(n) = "second" RETURN n
MATCH (n:foo) WHERE id(n) = "third" RETURN n
```

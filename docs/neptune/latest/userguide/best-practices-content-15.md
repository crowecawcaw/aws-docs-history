# Prefer using custom IDs for node/relationship

Neptune allows users to explicitly assign IDs on nodes and relationships. The ID must be globally unique in the
dataset and deterministic to be useful. A deterministic ID can be used as a lookup or a filtering mechanism just like
properties; however, using an ID is much more optimized from query execution perspective than using properties. There
are several benefits to using custom IDs -

- Properties can be null for an existing entity, but the ID must exist. This allows the query engine to use an
  optimized join during execution.
- When concurrent mutation queries are executed, the chances of
  [concurrent modification exceptions](transactions-exceptions.md "transactions-exceptions.md") (CMEs) are reduced significantly when IDs are used to access
  nodes because fewer locks are taking on IDs than properties due to their enforced uniqueness.
- Using IDs avoids the chance of creating duplicate data as Neptune enforces uniqueness on IDs, unlike
  properties.

The following query example uses a custom ID:

###### Note

The property `~id` is used to specify the ID, whereas `id` is just stored as any other property.

```
CREATE (n:Person {`~id`: '1', name: 'alice'})
```

Without using a custom ID:

```
CREATE (n:Person {id: '1', name: 'alice'})
```

If using the latter mechanism, there is no uniqueness enforcement and you could later execute the query:

```
CREATE (n:Person {id: '1', name: 'john'})
```

This creates a second node with `id=1` named `john`. In this scenario, you would now have
two nodes with `id=1`, each having a different name - (alice and john).

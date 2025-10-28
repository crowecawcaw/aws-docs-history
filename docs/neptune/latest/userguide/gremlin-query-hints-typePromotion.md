# Gremlin typePromotion query hint

When you submit a Gremlin traversal that filters on a numerical value or range, the Neptune
query engine must normally use type promotion when it executes the query. This means that it
has to examine values of every type that could hold the value you are filtering on.

For example, if you are filtering for values equal to 55, the engine must look for
integers equal to 55, long integers equal to 55L, floats equal to 55.0,
and so forth. Each type promotion requires an additional lookup on storage,
which can cause an apparently simple query to take an unexpectedly long time to
complete.

Let's say you are searching for all vertexes with a customer-age property
greater than 5:

```
g.V().has('customerAge', gt(5))
```

To execute that traversal thoroughly, Neptune must expand the query to examine
every numeric type that the value you are querying for could be promoted to. In this
case, the `gt` filter has to be applied for any integer over 5, any long
over 5L, any float over 5.0, and any double over 5.0. Because each of these type
promotions requires an additional lookup on storage, you will see multiple filters per
numeric filter when you run the [Gremlin profile API](gremlin-profile-api.md "gremlin-profile-api.md") for this query, and it will take
significantly longer to complete than you might expect.

Often type promotion is unnecessary because you know in advance that you only
need to find values of one specific type. When this is the case, you can speed up your
queries dramatically by using the `typePromotion` query hint to turn off
type promotion.

## Syntax

The `typePromotion` query hint is specified by adding a
`withSideEffect` step to the query.

```
g.withSideEffect('Neptune#typePromotion', `true or false`).`gremlin-traversal`
```

###### Note

All Gremlin query hints side effects are prefixed with
`Neptune#`.

###### Available Values

- `true`
- `false`

To turn off type promotion for the query above, you would use:

```
g.withSideEffect('Neptune#typePromotion', false).V().has('customerAge', gt(5))
```

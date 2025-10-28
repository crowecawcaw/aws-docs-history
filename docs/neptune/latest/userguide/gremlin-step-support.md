# Native Gremlin step support in Amazon Neptune

The Amazon Neptune engine does not currently have full native support for all Gremlin steps,
as explained in [Tuning Gremlin queries](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md"). Current support falls into four
categories:

- [Gremlin steps that can always be converted to native
  Neptune engine operations](#gremlin-steps-always "#gremlin-steps-always")
- [Gremlin steps that can be converted to native
  Neptune engine operations in some cases](#gremlin-steps-sometimes "#gremlin-steps-sometimes")
- [Gremlin steps that are never converted to native
  Neptune engine operations](#gremlin-steps-never "#gremlin-steps-never")
- [Gremlin steps that are not supported
  in Neptune at all](#neptune-gremlin-steps-unsupported "#neptune-gremlin-steps-unsupported")

## Gremlin steps that can always be converted to native

Neptune engine operations

Many Gremlin steps can be converted to native Neptune engine operations as long
as they meet the following conditions:

- They are not preceded in the query by a step that cannot be converted.
- Their parent step, if any, can be converted,
- All their child traversals, if any, can be converted.

The following Gremlin steps are always converted to native Neptune engine operations
if they meet those conditions:

- [and( )](http://tinkerpop.apache.org/docs/current/reference/#and-step "http://tinkerpop.apache.org/docs/current/reference/#and-step")
- [as( )](http://tinkerpop.apache.org/docs/current/reference/#as-step "http://tinkerpop.apache.org/docs/current/reference/#as-step")
- [count( )](http://tinkerpop.apache.org/docs/current/reference/#count-step "http://tinkerpop.apache.org/docs/current/reference/#count-step")
- [E( )](http://tinkerpop.apache.org/docs/current/reference/#graph-step "http://tinkerpop.apache.org/docs/current/reference/#graph-step")
- [emit( )](http://tinkerpop.apache.org/docs/current/reference/#emit-step "http://tinkerpop.apache.org/docs/current/reference/#emit-step")
- [explain( )](http://tinkerpop.apache.org/docs/current/reference/#explain-step "http://tinkerpop.apache.org/docs/current/reference/#explain-step")
- [group( )](http://tinkerpop.apache.org/docs/current/reference/#group-step "http://tinkerpop.apache.org/docs/current/reference/#group-step")
- [groupCount( )](http://tinkerpop.apache.org/docs/current/reference/#groupcount-step "http://tinkerpop.apache.org/docs/current/reference/#groupcount-step")
- [identity( )](http://tinkerpop.apache.org/docs/current/reference/#identity-step "http://tinkerpop.apache.org/docs/current/reference/#identity-step")
- [is( )](http://tinkerpop.apache.org/docs/current/reference/#is-step "http://tinkerpop.apache.org/docs/current/reference/#is-step")
- [key( )](http://tinkerpop.apache.org/docs/current/reference/#key-step "http://tinkerpop.apache.org/docs/current/reference/#key-step")
- [label( )](http://tinkerpop.apache.org/docs/current/reference/#label-step "http://tinkerpop.apache.org/docs/current/reference/#label-step")
- [limit( )](http://tinkerpop.apache.org/docs/current/reference/#limit-step "http://tinkerpop.apache.org/docs/current/reference/#limit-step")
- [local( )](http://tinkerpop.apache.org/docs/current/reference/#local-step "http://tinkerpop.apache.org/docs/current/reference/#local-step")
- [loops( )](http://tinkerpop.apache.org/docs/current/reference/#loops-step "http://tinkerpop.apache.org/docs/current/reference/#loops-step")
- [not( )](http://tinkerpop.apache.org/docs/current/reference/#not-step "http://tinkerpop.apache.org/docs/current/reference/#not-step")
- [or( )](http://tinkerpop.apache.org/docs/current/reference/#or-step "http://tinkerpop.apache.org/docs/current/reference/#or-step")
- [profile( )](http://tinkerpop.apache.org/docs/current/reference/#profile-step "http://tinkerpop.apache.org/docs/current/reference/#profile-step")
- [properties( )](http://tinkerpop.apache.org/docs/current/reference/#properties-step "http://tinkerpop.apache.org/docs/current/reference/#properties-step")
- [subgraph( )](http://tinkerpop.apache.org/docs/current/reference/#subgraph-step "http://tinkerpop.apache.org/docs/current/reference/#subgraph-step")
- [until( )](http://tinkerpop.apache.org/docs/current/reference/#until-step "http://tinkerpop.apache.org/docs/current/reference/#until-step")
- [V( )](http://tinkerpop.apache.org/docs/current/reference/#graph-step "http://tinkerpop.apache.org/docs/current/reference/#graph-step")
- [value( )](http://tinkerpop.apache.org/docs/current/reference/#value-step "http://tinkerpop.apache.org/docs/current/reference/#value-step")
- [valueMap( )](http://tinkerpop.apache.org/docs/current/reference/#valuemap-step "http://tinkerpop.apache.org/docs/current/reference/#valuemap-step")
- [values( )](http://tinkerpop.apache.org/docs/current/reference/#values-step "http://tinkerpop.apache.org/docs/current/reference/#values-step")

## Gremlin steps that can be converted to native

Neptune engine operations in some cases

Some Gremlin steps can be converted to native Neptune engine operations in some
situations but not in others:

- [addE( )](http://tinkerpop.apache.org/docs/current/reference/#addedge-step "http://tinkerpop.apache.org/docs/current/reference/#addedge-step")
    –   The `addE()` step can generally be converted to a native Neptune engine
  operation, unless it is immediately followed by a `property()` step containing a traversal as
  a key.
- [addV( )](http://tinkerpop.apache.org/docs/current/reference/#addvertex-step "http://tinkerpop.apache.org/docs/current/reference/#addvertex-step")
    –   The `addV()` step can generally be converted to a native Neptune engine
  operation, unless it is immediately followed by a `property()` step containing a traversal as
  a key, or unless multiple labels are assigned.
- [aggregate( )](http://tinkerpop.apache.org/docs/current/reference/#store-step "http://tinkerpop.apache.org/docs/current/reference/#store-step")
    –   The `aggregate()` step can generally be converted to a native Neptune engine
  operation, unless the step is used in a child traversal or sub-traversal, or unless
  the value being stored is something other than a vertex, edge, id, label or property value.

In example below, `aggregate()` is not converted because it is being
used in a child traversal:

```
g.V().has('code','ANC').as('a')
     .project('flights').by(select('a')
     .outE().aggregate('x'))
```

In this example, aggregate() is not converted because what is stored is the
`min()` of a value:

```
g.V().has('code','ANC').outE().aggregate('x').by(values('dist').min())
```

- [barrier( )](http://tinkerpop.apache.org/docs/current/reference/#barrier-step "http://tinkerpop.apache.org/docs/current/reference/#barrier-step")
    –   The `barrier()` step can generally be converted to a native Neptune engine
  operation, unless the step following it is not converted.
- [cap( )](http://tinkerpop.apache.org/docs/current/reference/#cap-step "http://tinkerpop.apache.org/docs/current/reference/#cap-step")
    –   The only case in which the `cap()` step is converted is when
  it is combined with the `unfold()` step to return an unfolded version of an aggregate
  of vertex, edge, id, or poperty values. In this example, `cap()` will be converted
  because it is followed by `.unfold()`:

```
g.V().has('airport','country','IE').aggregate('airport').limit(2)
     .cap('airport').unfold()
```

However, if you remove the `.unfold()`, `cap()` will not be converted:

```
g.V().has('airport','country','IE').aggregate('airport').limit(2)
     .cap('airport')
```

- [coalesce( )](http://tinkerpop.apache.org/docs/current/reference/#coalesce-step "http://tinkerpop.apache.org/docs/current/reference/#coalesce-step")
    –   The only case where the `coalesce()` step is converted is when it
  follows the [Upsert pattern](http://tinkerpop.apache.org/docs/current/recipes/#element-existence "http://tinkerpop.apache.org/docs/current/recipes/#element-existence")
  recommended on the [TinkerPop recipes page](http://tinkerpop.apache.org/docs/current/recipes/ "http://tinkerpop.apache.org/docs/current/recipes/").
  Other coalesce() patterns are not allowed. Conversion is limited to the case where all child traversals
  can be converted, they all produce the same type as output (vertex, edge, id, value, key, or label),
  they all traverse to a new element, and they do not contain the `repeat()` step.
- [constant( )](http://tinkerpop.apache.org/docs/current/reference/#constant-step "http://tinkerpop.apache.org/docs/current/reference/#constant-step")
    –   The constant() step is currently only converted if it is used within a `sack().by()`
  part of a traversal to assign a constant value, like this:

```
g.V().has('code','ANC').sack(assign).by(constant(10)).out().limit(2)
```

- [cyclicPath( )](http://tinkerpop.apache.org/docs/current/reference/#cyclicpath-step "http://tinkerpop.apache.org/docs/current/reference/#cyclicpath-step")
    –   The `cyclicPath()` step can generally be converted to a native Neptune engine
  operation, unless the step is used with `by()`, `from()`, or `to()`
  modulators. In the following queries, for example, `cyclicPath()` is not converted:

```
g.V().has('code','ANC').as('a').out().out().cyclicPath().by('code')
g.V().has('code','ANC').as('a').out().out().cyclicPath().from('a')
g.V().has('code','ANC').as('a').out().out().cyclicPath().to('a')
```

- [drop( )](http://tinkerpop.apache.org/docs/current/reference/#drop-step "http://tinkerpop.apache.org/docs/current/reference/#drop-step")
    –   The `drop()` step can generally be converted to a native Neptune engine
  operation, unless the step is used inside a `sideEffect(`) or `optional()` step.
- [fold( )](http://tinkerpop.apache.org/docs/current/reference/#fold-step "http://tinkerpop.apache.org/docs/current/reference/#fold-step")
    –   There are only two situations where the fold() step can be converted, namely
  when it is used in the [Upsert pattern](http://tinkerpop.apache.org/docs/current/recipes/#element-existence "http://tinkerpop.apache.org/docs/current/recipes/#element-existence")
  recommended on the [TinkerPop recipes page](http://tinkerpop.apache.org/docs/current/recipes/ "http://tinkerpop.apache.org/docs/current/recipes/"),
  and when it is used in a `group().by()` context like this:

```
g.V().has('code','ANC').out().group().by().by(values('code', 'city').fold())
```

- [has( )](http://tinkerpop.apache.org/docs/current/reference/#has-step "http://tinkerpop.apache.org/docs/current/reference/#has-step")
    –   The `has()` step can generally be converted to a native Neptune engine operation provided
  queries with `T` use the predicate `P.eq`, `P.neq` or `P.contains`. Expect variations of `has()` that imply those
  instances of `P` to convert to native as well, such as `hasId('id1234')` which is equivalent to `has(eq, T.id, 'id1234')`.
- [id( )](http://tinkerpop.apache.org/docs/current/reference/#id-step "http://tinkerpop.apache.org/docs/current/reference/#id-step")
    –   The `id()` step is converted unless it is used on a property, like this:

```
g.V().has('code','ANC').properties('code').id()
```

- [mergeE()](https://tinkerpop.apache.org/docs/current/reference/#mergeedge-step "https://tinkerpop.apache.org/docs/current/reference/#mergeedge-step")   –  
  The `mergeE()` step can be converted to a native Neptune
  engine operation if the parameters (the merge condition, the `onCreate` and `onMatch`) are constant
  (either `null`, a constant `Map`, or `select()` of a `Map`). All examples in
  [upserting edges](gremlin-efficient-upserts.md#gremlin-upserts-edges "gremlin-efficient-upserts.md#gremlin-upserts-edges") can be converted.
- [mergeV()](https://tinkerpop.apache.org/docs/current/reference/#mergevertex-step "https://tinkerpop.apache.org/docs/current/reference/#mergevertex-step")   –  
  The mergeV() step can be converted to a native Neptune engine operation if the parameters
  (the merge condition, the `onCreate` and `onMatch`) are constant (either `null`,
  a constant `Map`, or `select()` of a `Map`). All examples in
  [upserting vertices](gremlin-efficient-upserts.md#gremlin-upserts-vertices "gremlin-efficient-upserts.md#gremlin-upserts-vertices") can be converted.
- [order( )](http://tinkerpop.apache.org/docs/current/reference/#order-step "http://tinkerpop.apache.org/docs/current/reference/#order-step")
    –   The `order()` step can generally be converted to a native Neptune engine
  operation, unless one of the following is true:
  - The `order()` step is within a nested child traversal, like this:

  ```
  g.V().has('code','ANC').where(V().out().order().by(id))
  ```

  - Local ordering is being used, as for example with `order(local)`.
  - A custom comparator is being used in the `by()` modulation to order by.
    An example is this use of `sack()`:

  ```
  g.withSack(0).
    V().has('code','ANC').
        repeat(outE().sack(sum).by('dist').inV()).times(2).limit(10).
        order().by(sack())
  ```

  - There are multiple orderings on the same element.

- [project( )](http://tinkerpop.apache.org/docs/current/reference/#project-step "http://tinkerpop.apache.org/docs/current/reference/#project-step")
    –   The `project()` step can generally be converted to a native Neptune engine
  operation, unless the number of `by()` statements following the `project()`
  does not match the number of labels specified, as here:

```
g.V().has('code','ANC').project('x', 'y').by(id)
```

- [range( )](http://tinkerpop.apache.org/docs/current/reference/#range-step "http://tinkerpop.apache.org/docs/current/reference/#range-step")
    –   The `range()` step is only converted when the lower end of the
  range in question is zero (for example, `range(0,3)`).
- [repeat( )](http://tinkerpop.apache.org/docs/current/reference/#repeat-step "http://tinkerpop.apache.org/docs/current/reference/#repeat-step")
    –   The `repeat()` step can generally be converted to a native Neptune engine
  operation, unless it is nested within another `repeat()` step, like this:

```
g.V().has('code','ANC').repeat(out().repeat(out()).times(2)).times(2)
```

- [sack( )](http://tinkerpop.apache.org/docs/current/reference/#sack-step "http://tinkerpop.apache.org/docs/current/reference/#sack-step")
    –   The `sack()` step can generally be converted to a native Neptune engine
  operation, except in the following cases:
  - If a non-numeric sack operator is being used.
  - If a numeric sack operator other than `+`, `-`,
    `mult`, `div`, `min` and `max` is being used.
  - If `sack()` is used inside a `where()` step to filter
    based on a sack value, as here:

  ```
  g.V().has('code','ANC').sack(assign).by(values('code')).where(sack().is('ANC'))
  ```

- [sum( )](http://tinkerpop.apache.org/docs/current/reference/#sum-step "http://tinkerpop.apache.org/docs/current/reference/#sum-step")
    –   The `sum()` step can generally be converted to a native Neptune engine
  operation, but not when used to calculate a global summation, like this:

```
g.V().has('code','ANC').outE('routes').values('dist').sum()
```

- [union( )](http://tinkerpop.apache.org/docs/current/reference/#union-step "http://tinkerpop.apache.org/docs/current/reference/#union-step")
    –   The `union()` step can be converted to a native Neptune engine operation
  as long as it is the last step in the query aside from the terminal step.
- [unfold( )](http://tinkerpop.apache.org/docs/current/reference/#unfold-step "http://tinkerpop.apache.org/docs/current/reference/#unfold-step")
    –   The `unfold()` step can only be converted to a native Neptune engine
  operation when it is used in the [Upsert
  pattern](http://tinkerpop.apache.org/docs/current/recipes/#element-existence "http://tinkerpop.apache.org/docs/current/recipes/#element-existence") recommended on the [TinkerPop
  recipes page](http://tinkerpop.apache.org/docs/current/recipes/ "http://tinkerpop.apache.org/docs/current/recipes/"), and when it is used together with `cap()` like this:

```
g.V().has('airport','country','IE').aggregate('airport').limit(2)
     .cap('airport').unfold()
```

- [where( )](http://tinkerpop.apache.org/docs/current/reference/#where-step "http://tinkerpop.apache.org/docs/current/reference/#where-step")
    –   The `where()` step can generally be converted to a native Neptune engine
  operation, except in the following cases:
  - When by() modulations are used, like this:

  ```
  g.V().hasLabel('airport').as('a')
       .where(gt('a')).by('runways')
  ```

  - When comparison operators other than `eq`, `neq`,
    `within`, and `without` are used.
  - When user-supplied aggregations are used.

## Gremlin steps that are never converted to native

Neptune engine operations

The following Gremlin steps are supported in Neptune but are never converted to
native Neptune engine operations. Instead, they are executed by the Gremlin server.

- [choose( )](http://tinkerpop.apache.org/docs/current/reference/#choose-step "http://tinkerpop.apache.org/docs/current/reference/#choose-step")
- [coin( )](http://tinkerpop.apache.org/docs/current/reference/#coin-step "http://tinkerpop.apache.org/docs/current/reference/#coin-step")
- [inject( )](http://tinkerpop.apache.org/docs/current/reference/#inject-step "http://tinkerpop.apache.org/docs/current/reference/#inject-step")
- [match( )](http://tinkerpop.apache.org/docs/current/reference/#match-step "http://tinkerpop.apache.org/docs/current/reference/#match-step")
- [math( )](http://tinkerpop.apache.org/docs/current/reference/#math-step "http://tinkerpop.apache.org/docs/current/reference/#math-step")
- [max( )](http://tinkerpop.apache.org/docs/current/reference/#max-step "http://tinkerpop.apache.org/docs/current/reference/#max-step")
- [mean( )](http://tinkerpop.apache.org/docs/current/reference/#mean-step "http://tinkerpop.apache.org/docs/current/reference/#mean-step")
- [min( )](http://tinkerpop.apache.org/docs/current/reference/#min-step "http://tinkerpop.apache.org/docs/current/reference/#min-step")
- [option( )](http://tinkerpop.apache.org/docs/current/reference/#option-step "http://tinkerpop.apache.org/docs/current/reference/#option-step")
- [optional( )](http://tinkerpop.apache.org/docs/current/reference/#optional-step "http://tinkerpop.apache.org/docs/current/reference/#optional-step")
- [path( )](http://tinkerpop.apache.org/docs/current/reference/#path-step "http://tinkerpop.apache.org/docs/current/reference/#path-step")
- [propertyMap( )](http://tinkerpop.apache.org/docs/current/reference/#propertymap-step "http://tinkerpop.apache.org/docs/current/reference/#propertymap-step")
- [sample( )](http://tinkerpop.apache.org/docs/current/reference/#sample-step "http://tinkerpop.apache.org/docs/current/reference/#sample-step")
- [skip( )](http://tinkerpop.apache.org/docs/current/reference/#skip-step "http://tinkerpop.apache.org/docs/current/reference/#skip-step")
- [tail( )](http://tinkerpop.apache.org/docs/current/reference/#tail-step "http://tinkerpop.apache.org/docs/current/reference/#tail-step")
- [timeLimit( )](http://tinkerpop.apache.org/docs/current/reference/#timelimit-step "http://tinkerpop.apache.org/docs/current/reference/#timelimit-step")
- [tree( )](http://tinkerpop.apache.org/docs/current/reference/#tree-step "http://tinkerpop.apache.org/docs/current/reference/#tree-step")

## Gremlin steps that are not supported

in Neptune at all

The following Gremlin steps are not supported at all in Neptune. In most cases
this is because they require a `GraphComputer`, which Neptune does not
currently support.

- [connectedComponent( )](http://tinkerpop.apache.org/docs/current/reference/#connectedcomponent-step "http://tinkerpop.apache.org/docs/current/reference/#connectedcomponent-step")
- [io( )](http://tinkerpop.apache.org/docs/current/reference/#io-step "http://tinkerpop.apache.org/docs/current/reference/#io-step")
- [shortestPath( )](http://tinkerpop.apache.org/docs/current/reference/#shortestpath-step "http://tinkerpop.apache.org/docs/current/reference/#shortestpath-step")
- [withComputer( )](http://tinkerpop.apache.org/docs/current/reference/#with-step "http://tinkerpop.apache.org/docs/current/reference/#with-step")
- [pageRank( )](http://tinkerpop.apache.org/docs/current/reference/#pagerank-step "http://tinkerpop.apache.org/docs/current/reference/#pagerank-step")
- [peerPressure( )](http://tinkerpop.apache.org/docs/current/reference/#peerpressure-step "http://tinkerpop.apache.org/docs/current/reference/#peerpressure-step")
- [program( )](http://tinkerpop.apache.org/docs/current/reference/#program-step "http://tinkerpop.apache.org/docs/current/reference/#program-step")

The `io()` step is actually partially supported, in that it can be
used to `read()` from a URL but not to `write()`.

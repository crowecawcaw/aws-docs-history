# Gremlin step coverage in DFE

Gremlin DFE is a labmode feature and can be used by either enabling the cluster parameter or
using the `Neptune#useDFE` query hint. For more information please refer to
[Using Gremlin with the Neptune DFE query engine](gremlin-with-dfe.md "gremlin-with-dfe.md").

The following steps are available to use in Gremlin DFE.

## Path and traversal steps:

[asDate()](https://tinkerpop.apache.org/docs/current/reference/#asDate-step "https://tinkerpop.apache.org/docs/current/reference/#asDate-step"),
[barrier()](https://tinkerpop.apache.org/docs/current/reference/#barrier-step "https://tinkerpop.apache.org/docs/current/reference/#barrier-step"),
[call()](https://tinkerpop.apache.org/docs/current/reference/#call-step "https://tinkerpop.apache.org/docs/current/reference/#call-step"),
[cap()](https://tinkerpop.apache.org/docs/current/reference/#cap-step "https://tinkerpop.apache.org/docs/current/reference/#cap-step"),
[dateAdd()](https://tinkerpop.apache.org/docs/current/reference/#dateadd-step "https://tinkerpop.apache.org/docs/current/reference/#dateadd-step"),
[dateDiff()](https://tinkerpop.apache.org/docs/current/reference/#datediff-step "https://tinkerpop.apache.org/docs/current/reference/#datediff-step"),
[disjunct()](https://tinkerpop.apache.org/docs/current/reference/#disjunct-step "https://tinkerpop.apache.org/docs/current/reference/#disjunct-step"),
[drop()](https://tinkerpop.apache.org/docs/current/reference/#drop-step "https://tinkerpop.apache.org/docs/current/reference/#drop-step"),
[fail()](https://tinkerpop.apache.org/docs/current/reference/#fail-step "https://tinkerpop.apache.org/docs/current/reference/#fail-step"),
[filter()](https://tinkerpop.apache.org/docs/current/reference/#filter-step "https://tinkerpop.apache.org/docs/current/reference/#filter-step"),
[flatMap()](https://tinkerpop.apache.org/docs/current/reference/#flatmap-step "https://tinkerpop.apache.org/docs/current/reference/#flatmap-step"),
[id()](https://tinkerpop.apache.org/docs/current/reference/#id-step "https://tinkerpop.apache.org/docs/current/reference/#id-step"),
[identity()](https://tinkerpop.apache.org/docs/current/reference/#identity-step "https://tinkerpop.apache.org/docs/current/reference/#identity-step"),
[index()](https://tinkerpop.apache.org/docs/current/reference/#index-step "https://tinkerpop.apache.org/docs/current/reference/#index-step"),
[intersect()](https://tinkerpop.apache.org/docs/current/reference/#intersect-step "https://tinkerpop.apache.org/docs/current/reference/#intersect-step"),
[inject()](https://tinkerpop.apache.org/docs/current/reference/#inject-step "https://tinkerpop.apache.org/docs/current/reference/#inject-step"),
[label()](https://tinkerpop.apache.org/docs/current/reference/#label-step "https://tinkerpop.apache.org/docs/current/reference/#label-step"),
[length()](https://tinkerpop.apache.org/docs/current/reference/#length-step "https://tinkerpop.apache.org/docs/current/reference/#length-step"),
[loops()](https://tinkerpop.apache.org/docs/current/reference/#loops-step "https://tinkerpop.apache.org/docs/current/reference/#loops-step"),
[map()](https://tinkerpop.apache.org/docs/current/reference/#map-step "https://tinkerpop.apache.org/docs/current/reference/#map-step"),
[order()](https://tinkerpop.apache.org/docs/current/reference/#order-step "https://tinkerpop.apache.org/docs/current/reference/#order-step"),
[path()](https://tinkerpop.apache.org/docs/current/reference/#path-step "https://tinkerpop.apache.org/docs/current/reference/#path-step"),
[project()](https://tinkerpop.apache.org/docs/current/reference/#project-step "https://tinkerpop.apache.org/docs/current/reference/#project-step"),
[range()](https://tinkerpop.apache.org/docs/current/reference/#range-step "https://tinkerpop.apache.org/docs/current/reference/#range-step"),
[repeat()](https://tinkerpop.apache.org/docs/current/reference/#repeat-step "https://tinkerpop.apache.org/docs/current/reference/#repeat-step"),
[reverse()](https://tinkerpop.apache.org/docs/current/reference/#reverse-step "https://tinkerpop.apache.org/docs/current/reference/#reverse-step"),
[sack()](https://tinkerpop.apache.org/docs/current/reference/#sack-step "https://tinkerpop.apache.org/docs/current/reference/#sack-step"),
[sample()](https://tinkerpop.apache.org/docs/current/reference/#sample-step "https://tinkerpop.apache.org/docs/current/reference/#sample-step"),
[select()](https://tinkerpop.apache.org/docs/current/reference/#select-step "https://tinkerpop.apache.org/docs/current/reference/#select-step"),
[sideEffect()](https://tinkerpop.apache.org/docs/current/reference/#sideeffect-step "https://tinkerpop.apache.org/docs/current/reference/#sideeffect-step"),
[split()](https://tinkerpop.apache.org/docs/current/reference/#split-step "https://tinkerpop.apache.org/docs/current/reference/#split-step"),
[unfold()](https://tinkerpop.apache.org/docs/current/reference/#unfold-step "https://tinkerpop.apache.org/docs/current/reference/#unfold-step"),
[union()](https://tinkerpop.apache.org/docs/current/reference/#union-step "https://tinkerpop.apache.org/docs/current/reference/#union-step")

## Aggregate and collection steps:

[aggregate(global)](https://tinkerpop.apache.org/docs/current/reference/#aggregate-step "https://tinkerpop.apache.org/docs/current/reference/#aggregate-step"),
[combine()](https://tinkerpop.apache.org/docs/current/reference/#combine-step "https://tinkerpop.apache.org/docs/current/reference/#combine-step"),
[count()](https://tinkerpop.apache.org/docs/current/reference/#count-step "https://tinkerpop.apache.org/docs/current/reference/#count-step"),
[dedup(global)](https://tinkerpop.apache.org/docs/current/reference/#dedup-step "https://tinkerpop.apache.org/docs/current/reference/#dedup-step"),
[fold()](https://tinkerpop.apache.org/docs/current/reference/#fold-step "https://tinkerpop.apache.org/docs/current/reference/#fold-step"),
[group()](https://tinkerpop.apache.org/docs/current/reference/#group-step "https://tinkerpop.apache.org/docs/current/reference/#group-step"),
[groupCount()](https://tinkerpop.apache.org/docs/current/reference/#groupcount-step "https://tinkerpop.apache.org/docs/current/reference/#groupcount-step"),

## Mathematical steps:

[max()](https://tinkerpop.apache.org/docs/current/reference/#max-step "https://tinkerpop.apache.org/docs/current/reference/#max-step"),
[mean()](https://tinkerpop.apache.org/docs/current/reference/#mean-step "https://tinkerpop.apache.org/docs/current/reference/#mean-step"),
[min()](https://tinkerpop.apache.org/docs/current/reference/#min-step "https://tinkerpop.apache.org/docs/current/reference/#min-step"),
[sum()](https://tinkerpop.apache.org/docs/current/reference/#sum-step "https://tinkerpop.apache.org/docs/current/reference/#sum-step")

## Element steps:

[otherV()](https://tinkerpop.apache.org/docs/current/reference/#otherv-step "https://tinkerpop.apache.org/docs/current/reference/#otherv-step"),
[elementMap()](https://tinkerpop.apache.org/docs/current/reference/#elementmap-step "https://tinkerpop.apache.org/docs/current/reference/#elementmap-step"),
[element()](https://tinkerpop.apache.org/docs/current/reference/#element-step "https://tinkerpop.apache.org/docs/current/reference/#element-step"),
[v()](https://tinkerpop.apache.org/docs/current/reference/#graph-step "https://tinkerpop.apache.org/docs/current/reference/#graph-step"),
[out(), in(), both(), outE(), inE(), bothE(), outV(), inV(), bothV(), otherV()](https://tinkerpop.apache.org/docs/current/reference/#vertex-step "https://tinkerpop.apache.org/docs/current/reference/#vertex-step")

## Property steps:

[properties()](https://tinkerpop.apache.org/docs/current/reference/#properties-step "https://tinkerpop.apache.org/docs/current/reference/#properties-step"),
[key()](https://tinkerpop.apache.org/docs/current/reference/#key-step "https://tinkerpop.apache.org/docs/current/reference/#key-step"),
[valueMap()](https://tinkerpop.apache.org/docs/current/reference/#propertymap-step "https://tinkerpop.apache.org/docs/current/reference/#propertymap-step"),
[value()](https://tinkerpop.apache.org/docs/current/reference/#value-step "https://tinkerpop.apache.org/docs/current/reference/#value-step")

## Filter steps:

[and()](https://tinkerpop.apache.org/docs/current/reference/#and-step "https://tinkerpop.apache.org/docs/current/reference/#and-step"),
[coalesce()](https://tinkerpop.apache.org/docs/current/reference/#coalesce-step "https://tinkerpop.apache.org/docs/current/reference/#coalesce-step"),
[coin()](https://tinkerpop.apache.org/docs/current/reference/#coin-step "https://tinkerpop.apache.org/docs/current/reference/#coin-step"),
[has()](https://tinkerpop.apache.org/docs/current/reference/#has-step "https://tinkerpop.apache.org/docs/current/reference/#has-step"),
[is()](https://tinkerpop.apache.org/docs/current/reference/#is-step "https://tinkerpop.apache.org/docs/current/reference/#is-step"),
[local()](https://tinkerpop.apache.org/docs/current/reference/#local-step "https://tinkerpop.apache.org/docs/current/reference/#local-step"),
[none()](https://tinkerpop.apache.org/docs/current/reference/#none-step "https://tinkerpop.apache.org/docs/current/reference/#none-step"),
[not()](https://tinkerpop.apache.org/docs/current/reference/#not-step "https://tinkerpop.apache.org/docs/current/reference/#not-step"),
[or()](https://tinkerpop.apache.org/docs/current/reference/#or-step "https://tinkerpop.apache.org/docs/current/reference/#or-step"),
[where()](https://tinkerpop.apache.org/docs/current/reference/#where-step "https://tinkerpop.apache.org/docs/current/reference/#where-step")

## String manipulation steps:

[concat()](https://tinkerpop.apache.org/docs/current/reference/#concat-step "https://tinkerpop.apache.org/docs/current/reference/#concat-step"),
[lTrim()](https://tinkerpop.apache.org/docs/current/reference/#lTrim-step "https://tinkerpop.apache.org/docs/current/reference/#lTrim-step"),
[rTrim()](https://tinkerpop.apache.org/docs/current/reference/#rtrim-step "https://tinkerpop.apache.org/docs/current/reference/#rtrim-step"),
[substring()](https://tinkerpop.apache.org/docs/current/reference/#substring-step "https://tinkerpop.apache.org/docs/current/reference/#substring-step"),
[toLower()](https://tinkerpop.apache.org/docs/current/reference/#toLower-step "https://tinkerpop.apache.org/docs/current/reference/#toLower-step"),
[toUpper()](https://tinkerpop.apache.org/docs/current/reference/#toUpper-step "https://tinkerpop.apache.org/docs/current/reference/#toUpper-step"),
[trim()](https://tinkerpop.apache.org/docs/current/reference/#trim-step "https://tinkerpop.apache.org/docs/current/reference/#trim-step")

## Predicates:

- [Compare: eq, neq, lt, lte, gt, gte](https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates "https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates")

- [Contains: within, without](https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates "https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates")

- [TextP: endingWith, containing, notStartingWith, notEndingWith, notContaining](https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates "https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates")

- [P: and, or, between, outside, inside](https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates "https://tinkerpop.apache.org/docs/current/reference/#a-note-on-predicates")

## Limitations

Repeat with Limit, Labels inside repeat traversal and dedup are not supported in DFE yet.

```
// With Limit inside the repeat traversal
  g.V().has('code','AGR').repeat(out().limit(5)).until(has('code','FRA'))

  // With Labels inside the repeat traversal
  g.V().has('code','AGR').repeat(out().as('a')).until(has('code','FRA'))

  // With Dedup inside the repeat traversal
  g.V().has('code','AGR').repeat(out().dedup()).until(has('code','FRA'))
```

Path with nested repeats, or branching steps are not supported yet.

```
// Path with branching steps
  g.V().has('code','AGR').union(identity, outE().inV()).path().by('code')


  // With nested repeat
  g.V().has('code','AGR').repeat(out().union(identity(), out())).path().by('code')
```

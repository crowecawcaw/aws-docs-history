# Neptune SPARQL `explain` operators

The following sections describe the operators and parameters for the SPARQL
`explain` feature currently available in Amazon Neptune.

###### Important

The SPARQL `explain` feature is still being refined. The operators and
parameters documented here might change in future versions.

###### Topics

- [Aggregation operator](#sparql-explain-operator-aggregation "#sparql-explain-operator-aggregation")
- [ConditionalRouting operator](#sparql-explain-operator-conditional-routing "#sparql-explain-operator-conditional-routing")
- [Copy operator](#sparql-explain-operator-copy "#sparql-explain-operator-copy")
- [DFENode operator](#sparql-explain-operator-dfenode "#sparql-explain-operator-dfenode")
- [Distinct operator](#sparql-explain-operator-distinct "#sparql-explain-operator-distinct")
- [Federation operator](#sparql-explain-operator-federation "#sparql-explain-operator-federation")
- [Filter operator](#sparql-explain-operator-filter "#sparql-explain-operator-filter")
- [HashIndexBuild operator](#sparql-explain-operator-hash-index-build "#sparql-explain-operator-hash-index-build")
- [HashIndexJoin operator](#sparql-explain-operator-hash-index-join "#sparql-explain-operator-hash-index-join")
- [MergeJoin operator](#sparql-explain-operator-merge-join "#sparql-explain-operator-merge-join")
- [NamedSubquery operator](#sparql-explain-operator-named-subquery "#sparql-explain-operator-named-subquery")
- [PipelineJoin operator](#sparql-explain-operator-pipeline-join "#sparql-explain-operator-pipeline-join")
- [PipelineCountJoin operator](#sparql-explain-operator-pipeline-count-join "#sparql-explain-operator-pipeline-count-join")
- [PipelinedHashIndexJoin operator](#sparql-explain-operator-pipeline-hash-index-join "#sparql-explain-operator-pipeline-hash-index-join")
- [Projection operator](#sparql-explain-operator-projection "#sparql-explain-operator-projection")
- [PropertyPath operator](#sparql-explain-operator-property-path "#sparql-explain-operator-property-path")
- [TermResolution operator](#sparql-explain-operator-term-resolution "#sparql-explain-operator-term-resolution")
- [Slice operator](#sparql-explain-operator-slice "#sparql-explain-operator-slice")
- [SolutionInjection operator](#sparql-explain-operator-solution-injection "#sparql-explain-operator-solution-injection")
- [Sort operator](#sparql-explain-operator-sort "#sparql-explain-operator-sort")
- [VariableAlignment operator](#sparql-explain-operator-variable-alignment "#sparql-explain-operator-variable-alignment")

## `Aggregation` operator

Performs one or more aggregations, implementing the semantics of SPARQL
aggregation operators such as `count`, `max`, `min`, `sum`,
and so on.

`Aggregation` comes with optional grouping using `groupBy`
clauses, and optional `having` constraints.

###### Arguments

- `groupBy` – (_Optional_) Provides a
  `groupBy` clause that specifies the sequence of expressions according to
  which the incoming solutions are grouped.
- `aggregates` – (_Required_) Specifies an ordered
  list of aggregation expressions.
- `having` – (_Optional_) Adds constraints to
  filter on groups, as implied by the `having` clause in the SPARQL query.

## `ConditionalRouting` operator

Routes incoming solutions based on a given condition. Solutions that satisfy the
condition are routed to the operator ID referenced by `Out #1`, whereas
solutions that do not are routed to the operator referenced by `Out #2`.

###### Arguments

- `condition` – (_Required_) The routing
  condition.

## `Copy` operator

Delegates the solution stream as specified by the specified mode.

###### Modes

- `forward` – Forwards the solutions to the downstream operator
  identified by `Out #1`.
- `duplicate` – Duplicates the solutions and forwards them to each of
  the two operators identified by `Out #1` and `Out #2`.

`Copy` has no arguments.

## `DFENode` operator

This operator is an abstraction of the plan that is run by the DFE alternative
query engine. The detailed DFE plan is outlined in the arguments for this operator.
The argument is currently overloaded to contain the detailed runtime statistics
of the DFE plan. It contains the time spent in the various steps of query
execution by DFE.

The logical optimized abstract syntax tree (AST) for the DFE query plan is printed
with information about the operator types that were considered while planning and the
associated best- and worst-case costs to run the operators. The AST consists of the
following type of nodes at the moment:

- `DFEJoinGroupNode` – 
  Represents a join of one or more `DFEPatternNodes`.
- `DFEPatternNode` – 
  Encapsulates an underlying pattern using which matching tuples are projected
  out of the underlying database.

The sub-section, `Statistics & Operator histogram`, contains
details about the execution time of the `DataflowOp` plan and the
breakdown of CPU time used by each operator. Below this there is a table which
prints detailed runtime statistics of the plan executed by DFE.

###### Note

Because the DFE is an experimental feature released in lab mode,
the exact format of its `explain` output may change.

## `Distinct` operator

Computes the distinct projection on a subset of the variables, eliminating
duplicates. As a result, the number of solutions flowing in is larger than or equal
to the number of solutions flowing out.

###### Arguments

- `vars` – (_Required_) The variables to which to
  apply the `Distinct` projection.

## `Federation` operator

Passes a specified query to a specified remote SPARQL endpoint.

###### Arguments

- `endpoint` – (_Required_)
  The endpoint URL in the SPARQL `SERVICE` statement. This can be a constant string, or
  if the query endpoint is determined based on a variable within the same query, it
  can be the variable name.
- `query` – (_Required_)
  The reconstructed query string to be sent to the remote endpoint. The engine adds
  default prefixes to this query even when the client doesn't specify any.
- `silent` – (_Required_)
  A Boolean that indicates whether the `SILENT` keyword appeared after the
  keyword. `SILENT` tells the engine not to fail the whole query even if
  the remote `SERVICE` portion fails.

## `Filter` operator

Filters the incoming solutions. Only those solutions that satisfy the filter
condition are forwarded to the upstream operator, and all others are dropped.

###### Arguments

- `condition` – (_Required_) The filter
  condition.

## `HashIndexBuild` operator

Takes a list of bindings and spools them into a hash index whose name is defined
by the `solutionSet` argument. Typically, subsequent operators perform joins
against this solution set, referring it by that name.

###### Arguments

- `solutionSet` – (_Required_) The name of the
  hash index solution set.
- `sourceType` – (_Required_) The type of
  the source from which the bindings to store in the hash index are obtained:
  - `pipeline` – Spools the incoming solutions from
    the downstream operator in the operator pipeline into the hash index.
  - `binding set` – Spools the fixed binding set
    specified by the `sourceBindingSet` argument into the hash index.

- `sourceBindingSet` – (_Optional_) If the
  `sourceType` argument value is `binding set`, this argument
  specifies the static binding set to be spooled into the hash index.

## `HashIndexJoin` operator

Joins the incoming solutions against the hash index solution set identified by
the `solutionSet` argument.

###### Arguments

- `solutionSet` – (_Required_) Name of the
  solution set to join against. This must be a hash index that has been constructed in a
  prior step using the `HashIndexBuild` operator.
- `joinType` – (_Required_) The type of
  join to be performed:
  - `join` – A normal join, requiring an exact match
    between all shared variables.
  - `optional` – An `optional` join that uses the
    SPARQL `OPTIONAL` operator semantics.
  - `minus` – A `minus` operation retains a mapping for which no join
    partner exists, using the SPARQL `MINUS` operator semantics.
  - `existence check` – Checks whether there is
    a join partner or not, and binds the `existenceCheckResultVar`
    variable to the result of this check.

- `constraints` – (_Optional_) Additional join
  constraints that are considered during the join. Joins that do not satisfy these
  constraints are discarded.
- `existenceCheckResultVar` – (_Optional_) Only
  used for joins where `joinType` equals `existence check` (see the
  `joinType` argument earlier).

## `MergeJoin` operator

A merge join over multiple solution sets, as identified by the
`solutionSets` argument.

###### Arguments

- `solutionSets` – (_Required_) The solution sets
  to join together.

## `NamedSubquery` operator

Triggers evaluation of the subquery identified by the `subQuery`
argument and spools the result into the solution set specified by the `solutionSet`
argument. The incoming solutions for the operator are forwarded to the subquery
and then to the next operator.

###### Arguments

- `subQuery` – (_Required_) Name of the subquery
  to evaluate. The subquery is rendered explicitly in the output.
- `solutionSet` – (_Required_) The name of the
  solution set in which to store the subquery result.

## `PipelineJoin` operator

Receives as input the output of the previous operator and joins it against the
tuple pattern defined by the `pattern` argument.

###### Arguments

- `pattern` – (_Required_) The pattern, which
  takes the form of a subject-predicate-object, and optionally -graph tuple that underlies
  the join. If `distinct` is specified for the pattern, the join only extracts
  distinct solutions from projection variables specified by the `projectionVars`
  argument, rather than all matching solutions.
- `inlineFilters` – (_Optional_) A set of filters
  to be applied to the variables in the pattern. The pattern is evaluated in conjunction
  with these filters.
- `joinType` – (_Required_) The type of
  join to be performed:
  - `join` – A normal join, requiring an exact match
    between all shared variables.
  - `optional` – An `optional` join that uses the
    SPARQL `OPTIONAL` operator semantics.
  - `minus` – A `minus` operation retains a mapping for which no join
    partner exists, using the SPARQL `MINUS` operator semantics.
  - `existence check` – Checks whether there is
    a join partner or not, and binds the `existenceCheckResultVar`
    variable to the result of this check.

- `constraints` – (_Optional_) Additional join
  constraints that are considered during the join. Joins that do not satisfy these
  constraints are discarded.
- `projectionVars` – (_Optional_) The projection
  variables. Used in combination with `distinct := true` to enforce the
  extraction of distinct projections over a specified set of variables.
- `cutoffLimit` – (_Optional_) A cutoff limit for
  the number of join partners extracted. Although there is no limit by default, you can set
  this to 1 when performing joins to implement `FILTER (NOT) EXISTS` clauses,
  where it is sufficient to prove or disprove that there is a join partner.

## `PipelineCountJoin` operator

Variant of the `PipelineJoin`. Instead of joining, it just counts the matching
join partners and binds the count to the variable specified by the `countVar`
argument.

###### Arguments

- `countVar` – (_Required_) The variable to which
  the count result, namely the number of join partners, should be bound.
- `pattern` – (_Required_) The pattern, which
  takes the form of a subject-predicate-object, and optionally -graph tuple that underlies
  the join. If `distinct` is specified for the pattern, the join only extracts
  distinct solutions from projection variables specified by the `projectionVars`
  argument, rather than all matching solutions.
- `inlineFilters` – (_Optional_) A set of filters
  to be applied to the variables in the pattern. The pattern is evaluated in conjunction
  with these filters.
- `joinType` – (_Required_) The type of
  join to be performed:
  - `join` – A normal join, requiring an exact match
    between all shared variables.
  - `optional` – An `optional` join that uses the
    SPARQL `OPTIONAL` operator semantics.
  - `minus` – A `minus` operation retains a mapping for which no join
    partner exists, using the SPARQL `MINUS` operator semantics.
  - `existence check` – Checks whether there is
    a join partner or not, and binds the `existenceCheckResultVar`
    variable to the result of this check.

- `constraints` – (_Optional_) Additional join
  constraints that are considered during the join. Joins that do not satisfy these
  constraints are discarded.
- `projectionVars` – (_Optional_) The projection
  variables. Used in combination with `distinct := true` to enforce the
  extraction of distinct projections over a specified set of variables.
- `cutoffLimit` – (_Optional_) A cutoff limit for
  the number of join partners extracted. Although there is no limit by default, you can set
  this to 1 when performing joins to implement `FILTER (NOT) EXISTS` clauses,
  where it is sufficient to prove or disprove that there is a join partner.

## `PipelinedHashIndexJoin` operator

This is an all-in-one build hash index and join operator. It takes a list of
bindings, spools them into a hash index, and then joins the incoming solutions
against the hash index.

###### Arguments

- `sourceType`  –   (_Required_)
  The type of the source from which the bindings to store in the hash index are obtained,
  one of:
  - `pipeline`  –   Causes `PipelinedHashIndexJoin`
    to spool the incoming solutions from the downstream operator in the operator pipeline
    into the hash index.
  - `binding set`  –   Causes `PipelinedHashIndexJoin`
    to spool the fixed binding set specified by the `sourceBindingSet` argument into
    the hash index.

- `sourceSubQuery`   –   (_Optional_)
  If the `sourceType` argument value is `pipeline`, this argument specifies
  the subquery that is evaluated and spooled into the hash index.
- `sourceBindingSet`   –   (_Optional_)
  If the `sourceType` argument value is `binding set`, this argument
  specifies the static binding set to be spooled into the hash index.
- `joinType`  –   (_Required_) The type of
  join to be performed:
  - `join` – A normal join, requiring an exact match
    between all shared variables.
  - `optional` – An `optional` join that uses the
    SPARQL `OPTIONAL` operator semantics.
  - `minus` – A `minus` operation retains a mapping for which no join
    partner exists, using the SPARQL `MINUS` operator semantics.
  - `existence check` – Checks whether there is
    a join partner or not, and binds the `existenceCheckResultVar`
    variable to the result of this check.

- `existenceCheckResultVar`  –   (_Optional_)
  Only used for joins where `joinType` equals `existence check` (see
  the joinType argument above).

## `Projection` operator

Projects over a subset of the variables. The number of solutions flowing in equals
the number of solutions flowing out, but the shape of the solution differs, depending
on the mode setting.

###### Modes

- `retain` – Retain in solutions only the variables that are
  specified by the `vars` argument.
- `drop` – Drop all the variables that are specified by the
  `vars` argument.

###### Arguments

- `vars` – (_Required_) The variables to retain or
  drop, depending on the mode setting.

## `PropertyPath` operator

Enables recursive property paths such as `+` or `*`.
Neptune implements a fixed-point iteration approach based on a template specified by
the `iterationTemplate` argument. Known left-side or right-side variables are
bound in the template for every fixed-point iteration, until no more new solutions can be
found.

###### Arguments

- `iterationTemplate` – (_Required_) Name of the
  subquery template used to implement the fixed-point iteration.
- `leftTerm` – (_Required_) The term (variable or
  constant) on the left side of the property path.
- `rightTerm` – (_Required_) The term (variable or
  constant) on the right side of the property path.
- `lowerBound` – (_Required_) The lower bound for
  fixed-point iteration (either `0` for `*` queries, or `1`
  for `+` queries).

## `TermResolution` operator

Translates internal string identifier values back to their corresponding external strings, or
translates external strings to internal string identifier values, depending on the mode.

###### Modes

- `value2id` – Maps terms such as literals and URIs to corresponding
  internal ID values (encoding to internal values).
- `id2value` – Maps internal ID values to the corresponding terms
  such as literals and URIs (decoding of internal values).

###### Arguments

- `vars` – (_Required_) Specifies the variables
  whose strings or internal string IDs should be mapped.

## `Slice` operator

Implements a slice over the incoming solution stream, using the semantics of
SPARQL’s `LIMIT` and `OFFSET` clauses.

###### Arguments

- `limit` – (_Optional_) A limit on the solutions
  to be forwarded.
- `offset` – (_Optional_) The offset at which
  solutions are evaluated for forwarding.

## `SolutionInjection` operator

Receives no input. Statically injects solutions into the query plan and
records them in the `solutions` argument.

Query plans always begin with this static injection. If static solutions to inject can be
derived from the query itself by combining various sources of static bindings (for example,
from `VALUES` or `BIND` clauses), then the
`SolutionInjection` operator injects these derived static solutions. In the
simplest case, these reflect bindings that are implied by an outer `VALUES`
clause.

If no static solutions can be derived from the query, `SolutionInjection`
injects the empty, so-called universal solution, which is expanded and multiplied throughout
the query-evaluation process.

###### Arguments

- `solutions` – (_Required_) The sequence of
  solutions injected by the operator.

## `Sort` operator

Sorts the solution set using specified sort conditions.

###### Arguments

- `sortOrder` – (_Required_) An ordered list of
  variables, each containing an `ASC` (ascending) or `DESC`
  (descending) identifier, used sequentially to sort the solution set.

## `VariableAlignment` operator

Inspects solutions one by one, performing alignment on each one over two variables: a
specified `sourceVar` and a specified `targetVar`.

If `sourceVar` and `targetVar` in a solution have the same value,
the variables are considered aligned and the solution is forwarded, with the
redundant `sourceVar` projected out.

If the variables bind to different values, the solution is filtered out entirely.

###### Arguments

- `sourceVar` – (_Required_) The source variable,
  to be compared to the target variable. If alignment succeeds in a solution, meaning that
  the two variables have the same value, the source variable is projected out.
- `targetVar` – (_Required_) The target variable,
  with which the source variable is compared. Is retained even when alignment
  succeeds.

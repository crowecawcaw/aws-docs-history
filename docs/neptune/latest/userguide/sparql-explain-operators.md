

# Neptune SPARQL `explain` operators
<a name="sparql-explain-operators"></a>

The following sections describe the operators and parameters for the SPARQL `explain` feature currently available in Amazon Neptune.

**Important**  
The SPARQL `explain` feature is still being refined. The operators and parameters documented here might change in future versions.

**Topics**
+ [`Aggregation` operator](#sparql-explain-operator-aggregation)
+ [`ConditionalRouting` operator](#sparql-explain-operator-conditional-routing)
+ [`Copy` operator](#sparql-explain-operator-copy)
+ [`DFENode` operator](#sparql-explain-operator-dfenode)
+ [`Distinct` operator](#sparql-explain-operator-distinct)
+ [`Federation` operator](#sparql-explain-operator-federation)
+ [`Filter` operator](#sparql-explain-operator-filter)
+ [`HashIndexBuild` operator](#sparql-explain-operator-hash-index-build)
+ [`HashIndexJoin` operator](#sparql-explain-operator-hash-index-join)
+ [`MergeJoin` operator](#sparql-explain-operator-merge-join)
+ [`NamedSubquery` operator](#sparql-explain-operator-named-subquery)
+ [`PipelineJoin` operator](#sparql-explain-operator-pipeline-join)
+ [`PipelineCountJoin` operator](#sparql-explain-operator-pipeline-count-join)
+ [`PipelinedHashIndexJoin` operator](#sparql-explain-operator-pipeline-hash-index-join)
+ [`Projection` operator](#sparql-explain-operator-projection)
+ [`PropertyPath` operator](#sparql-explain-operator-property-path)
+ [`TermResolution` operator](#sparql-explain-operator-term-resolution)
+ [`Slice` operator](#sparql-explain-operator-slice)
+ [`SolutionInjection` operator](#sparql-explain-operator-solution-injection)
+ [`Sort` operator](#sparql-explain-operator-sort)
+ [`VariableAlignment` operator](#sparql-explain-operator-variable-alignment)

## `Aggregation` operator
<a name="sparql-explain-operator-aggregation"></a>

Performs one or more aggregations, implementing the semantics of SPARQL aggregation operators such as `count`, `max`, `min`, `sum`, and so on.

`Aggregation` comes with optional grouping using `groupBy` clauses, and optional `having` constraints.

**Arguments**
+ `groupBy` – (*Optional*) Provides a `groupBy` clause that specifies the sequence of expressions according to which the incoming solutions are grouped.
+ `aggregates` – (*Required*) Specifies an ordered list of aggregation expressions.
+ `having` – (*Optional*) Adds constraints to filter on groups, as implied by the `having` clause in the SPARQL query.

## `ConditionalRouting` operator
<a name="sparql-explain-operator-conditional-routing"></a>

Routes incoming solutions based on a given condition. Solutions that satisfy the condition are routed to the operator ID referenced by `Out #1`, whereas solutions that do not are routed to the operator referenced by `Out #2`.

**Arguments**
+ `condition` – (*Required*) The routing condition.

## `Copy` operator
<a name="sparql-explain-operator-copy"></a>

Delegates the solution stream as specified by the specified mode.

**Modes**
+ `forward` – Forwards the solutions to the downstream operator identified by `Out #1`. 
+ `duplicate` – Duplicates the solutions and forwards them to each of the two operators identified by `Out #1` and `Out #2`.

`Copy` has no arguments.

## `DFENode` operator
<a name="sparql-explain-operator-dfenode"></a>

This operator is an abstraction of the plan that is run by the DFE alternative query engine. The detailed DFE plan is outlined in the arguments for this operator. The argument is currently overloaded to contain the detailed runtime statistics of the DFE plan. It contains the time spent in the various steps of query execution by DFE.

The logical optimized abstract syntax tree (AST) for the DFE query plan is printed with information about the operator types that were considered while planning and the associated best- and worst-case costs to run the operators. The AST consists of the following type of nodes at the moment:
+ `DFEJoinGroupNode` –  Represents a join of one or more `DFEPatternNodes`.
+ `DFEPatternNode` –  Encapsulates an underlying pattern using which matching tuples are projected out of the underlying database.

The sub-section, `Statistics & Operator histogram`, contains details about the execution time of the `DataflowOp` plan and the breakdown of CPU time used by each operator. Below this there is a table which prints detailed runtime statistics of the plan executed by DFE.

**Note**  
Because DFE support for SPARQL is an experimental feature, the exact format of its `explain` output may change.

## `Distinct` operator
<a name="sparql-explain-operator-distinct"></a>

Computes the distinct projection on a subset of the variables, eliminating duplicates. As a result, the number of solutions flowing in is larger than or equal to the number of solutions flowing out.

**Arguments**
+ `vars` – (*Required*) The variables to which to apply the `Distinct` projection.

## `Federation` operator
<a name="sparql-explain-operator-federation"></a>

Passes a specified query to a specified remote SPARQL endpoint.

**Arguments**
+ `endpoint` – (*Required*) The endpoint URL in the SPARQL `SERVICE` statement. This can be a constant string, or if the query endpoint is determined based on a variable within the same query, it can be the variable name.
+ `query` – (*Required*) The reconstructed query string to be sent to the remote endpoint. The engine adds default prefixes to this query even when the client doesn't specify any.
+ `silent` – (*Required*) A Boolean that indicates whether the `SILENT` keyword appeared after the keyword. `SILENT` tells the engine not to fail the whole query even if the remote `SERVICE` portion fails.

## `Filter` operator
<a name="sparql-explain-operator-filter"></a>

Filters the incoming solutions. Only those solutions that satisfy the filter condition are forwarded to the upstream operator, and all others are dropped.

**Arguments**
+ `condition` – (*Required*) The filter condition.

## `HashIndexBuild` operator
<a name="sparql-explain-operator-hash-index-build"></a>

Takes a list of bindings and spools them into a hash index whose name is defined by the `solutionSet` argument. Typically, subsequent operators perform joins against this solution set, referring it by that name.

**Arguments**
+ `solutionSet` – (*Required*) The name of the hash index solution set.
+ `sourceType` – (*Required*) The type of the source from which the bindings to store in the hash index are obtained:
  + `pipeline` – Spools the incoming solutions from the downstream operator in the operator pipeline into the hash index.
  + `binding set` – Spools the fixed binding set specified by the `sourceBindingSet` argument into the hash index.
+ `sourceBindingSet` – (*Optional*) If the `sourceType` argument value is `binding set`, this argument specifies the static binding set to be spooled into the hash index.

## `HashIndexJoin` operator
<a name="sparql-explain-operator-hash-index-join"></a>

Joins the incoming solutions against the hash index solution set identified by the `solutionSet` argument.

**Arguments**
+ `solutionSet` – (*Required*) Name of the solution set to join against. This must be a hash index that has been constructed in a prior step using the `HashIndexBuild` operator.
+ `joinType` – (*Required*) The type of join to be performed:
  + `join` – A normal join, requiring an exact match between all shared variables.
  + `optional` – An `optional` join that uses the SPARQL `OPTIONAL` operator semantics.
  + `minus` – A `minus` operation retains a mapping for which no join partner exists, using the SPARQL `MINUS` operator semantics.
  + `existence check` – Checks whether there is a join partner or not, and binds the `existenceCheckResultVar` variable to the result of this check.
+ `constraints` – (*Optional*) Additional join constraints that are considered during the join. Joins that do not satisfy these constraints are discarded.
+ `existenceCheckResultVar` – (*Optional*) Only used for joins where `joinType` equals `existence check` (see the `joinType` argument earlier).

## `MergeJoin` operator
<a name="sparql-explain-operator-merge-join"></a>

A merge join over multiple solution sets, as identified by the `solutionSets` argument.

**Arguments**
+ `solutionSets` – (*Required*) The solution sets to join together.

## `NamedSubquery` operator
<a name="sparql-explain-operator-named-subquery"></a>

Triggers evaluation of the subquery identified by the `subQuery` argument and spools the result into the solution set specified by the `solutionSet` argument. The incoming solutions for the operator are forwarded to the subquery and then to the next operator.

**Arguments**
+ `subQuery` – (*Required*) Name of the subquery to evaluate. The subquery is rendered explicitly in the output.
+ `solutionSet` – (*Required*) The name of the solution set in which to store the subquery result.

## `PipelineJoin` operator
<a name="sparql-explain-operator-pipeline-join"></a>

Receives as input the output of the previous operator and joins it against the tuple pattern defined by the `pattern` argument.

**Arguments**
+ `pattern` – (*Required*) The pattern, which takes the form of a subject-predicate-object, and optionally -graph tuple that underlies the join. If `distinct` is specified for the pattern, the join only extracts distinct solutions from projection variables specified by the `projectionVars` argument, rather than all matching solutions.
+ `inlineFilters` – (*Optional*) A set of filters to be applied to the variables in the pattern. The pattern is evaluated in conjunction with these filters.
+ `joinType` – (*Required*) The type of join to be performed:
  + `join` – A normal join, requiring an exact match between all shared variables.
  + `optional` – An `optional` join that uses the SPARQL `OPTIONAL` operator semantics.
  + `minus` – A `minus` operation retains a mapping for which no join partner exists, using the SPARQL `MINUS` operator semantics.
  + `existence check` – Checks whether there is a join partner or not, and binds the `existenceCheckResultVar` variable to the result of this check.
+ `constraints` – (*Optional*) Additional join constraints that are considered during the join. Joins that do not satisfy these constraints are discarded.
+ `projectionVars` – (*Optional*) The projection variables. Used in combination with `distinct := true` to enforce the extraction of distinct projections over a specified set of variables.
+ `cutoffLimit` – (*Optional*) A cutoff limit for the number of join partners extracted. Although there is no limit by default, you can set this to 1 when performing joins to implement `FILTER (NOT) EXISTS` clauses, where it is sufficient to prove or disprove that there is a join partner.

## `PipelineCountJoin` operator
<a name="sparql-explain-operator-pipeline-count-join"></a>

Variant of the `PipelineJoin`. Instead of joining, it just counts the matching join partners and binds the count to the variable specified by the `countVar` argument.

**Arguments**
+ `countVar` – (*Required*) The variable to which the count result, namely the number of join partners, should be bound.
+ `pattern` – (*Required*) The pattern, which takes the form of a subject-predicate-object, and optionally -graph tuple that underlies the join. If `distinct` is specified for the pattern, the join only extracts distinct solutions from projection variables specified by the `projectionVars` argument, rather than all matching solutions.
+ `inlineFilters` – (*Optional*) A set of filters to be applied to the variables in the pattern. The pattern is evaluated in conjunction with these filters.
+ `joinType` – (*Required*) The type of join to be performed:
  + `join` – A normal join, requiring an exact match between all shared variables.
  + `optional` – An `optional` join that uses the SPARQL `OPTIONAL` operator semantics.
  + `minus` – A `minus` operation retains a mapping for which no join partner exists, using the SPARQL `MINUS` operator semantics.
  + `existence check` – Checks whether there is a join partner or not, and binds the `existenceCheckResultVar` variable to the result of this check.
+ `constraints` – (*Optional*) Additional join constraints that are considered during the join. Joins that do not satisfy these constraints are discarded.
+ `projectionVars` – (*Optional*) The projection variables. Used in combination with `distinct := true` to enforce the extraction of distinct projections over a specified set of variables.
+ `cutoffLimit` – (*Optional*) A cutoff limit for the number of join partners extracted. Although there is no limit by default, you can set this to 1 when performing joins to implement `FILTER (NOT) EXISTS` clauses, where it is sufficient to prove or disprove that there is a join partner.

## `PipelinedHashIndexJoin` operator
<a name="sparql-explain-operator-pipeline-hash-index-join"></a>

This is an all-in-one build hash index and join operator. It takes a list of bindings, spools them into a hash index, and then joins the incoming solutions against the hash index.

**Arguments**
+ `sourceType`  –   (*Required*) The type of the source from which the bindings to store in the hash index are obtained, one of:
  + `pipeline`  –   Causes `PipelinedHashIndexJoin` to spool the incoming solutions from the downstream operator in the operator pipeline into the hash index.
  + `binding set`  –   Causes `PipelinedHashIndexJoin` to spool the fixed binding set specified by the `sourceBindingSet` argument into the hash index.
+ `sourceSubQuery `  –   (*Optional*) If the `sourceType` argument value is `pipeline`, this argument specifies the subquery that is evaluated and spooled into the hash index.
+ `sourceBindingSet `  –   (*Optional*) If the `sourceType` argument value is `binding set`, this argument specifies the static binding set to be spooled into the hash index.
+ `joinType`  –   (*Required*) The type of join to be performed:
  + `join` – A normal join, requiring an exact match between all shared variables.
  + `optional` – An `optional` join that uses the SPARQL `OPTIONAL` operator semantics.
  + `minus` – A `minus` operation retains a mapping for which no join partner exists, using the SPARQL `MINUS` operator semantics.
  + `existence check` – Checks whether there is a join partner or not, and binds the `existenceCheckResultVar` variable to the result of this check.
+ `existenceCheckResultVar`  –   (*Optional*) Only used for joins where `joinType` equals `existence check` (see the joinType argument above).

## `Projection` operator
<a name="sparql-explain-operator-projection"></a>

Projects over a subset of the variables. The number of solutions flowing in equals the number of solutions flowing out, but the shape of the solution differs, depending on the mode setting.

**Modes**
+ `retain` – Retain in solutions only the variables that are specified by the `vars` argument.
+ `drop` – Drop all the variables that are specified by the `vars` argument.

**Arguments**
+ `vars` – (*Required*) The variables to retain or drop, depending on the mode setting.

## `PropertyPath` operator
<a name="sparql-explain-operator-property-path"></a>

Enables recursive property paths such as `+` or `*`. Neptune implements a fixed-point iteration approach based on a template specified by the `iterationTemplate` argument. Known left-side or right-side variables are bound in the template for every fixed-point iteration, until no more new solutions can be found.

**Arguments**
+ `iterationTemplate` – (*Required*) Name of the subquery template used to implement the fixed-point iteration.
+ `leftTerm` – (*Required*) The term (variable or constant) on the left side of the property path.
+ `rightTerm` – (*Required*) The term (variable or constant) on the right side of the property path.
+ `lowerBound` – (*Required*) The lower bound for fixed-point iteration (either `0` for `*` queries, or `1` for `+` queries).

## `TermResolution` operator
<a name="sparql-explain-operator-term-resolution"></a>

Translates internal string identifier values back to their corresponding external strings, or translates external strings to internal string identifier values, depending on the mode.

**Modes**
+ `value2id` – Maps terms such as literals and URIs to corresponding internal ID values (encoding to internal values).
+ `id2value` – Maps internal ID values to the corresponding terms such as literals and URIs (decoding of internal values).

**Arguments**
+ `vars` – (*Required*) Specifies the variables whose strings or internal string IDs should be mapped.

## `Slice` operator
<a name="sparql-explain-operator-slice"></a>

Implements a slice over the incoming solution stream, using the semantics of SPARQL’s `LIMIT` and `OFFSET` clauses.

**Arguments**
+ `limit` – (*Optional*) A limit on the solutions to be forwarded.
+ `offset` – (*Optional*) The offset at which solutions are evaluated for forwarding.

## `SolutionInjection` operator
<a name="sparql-explain-operator-solution-injection"></a>

Receives no input. Statically injects solutions into the query plan and records them in the `solutions` argument.

Query plans always begin with this static injection. If static solutions to inject can be derived from the query itself by combining various sources of static bindings (for example, from `VALUES` or `BIND` clauses), then the `SolutionInjection` operator injects these derived static solutions. In the simplest case, these reflect bindings that are implied by an outer `VALUES` clause.

If no static solutions can be derived from the query, `SolutionInjection` injects the empty, so-called universal solution, which is expanded and multiplied throughout the query-evaluation process.

**Arguments**
+ `solutions` – (*Required*) The sequence of solutions injected by the operator.

## `Sort` operator
<a name="sparql-explain-operator-sort"></a>

Sorts the solution set using specified sort conditions.

**Arguments**
+ `sortOrder` – (*Required*) An ordered list of variables, each containing an `ASC` (ascending) or `DESC` (descending) identifier, used sequentially to sort the solution set.

## `VariableAlignment` operator
<a name="sparql-explain-operator-variable-alignment"></a>

Inspects solutions one by one, performing alignment on each one over two variables: a specified `sourceVar` and a specified `targetVar`.

If `sourceVar` and `targetVar` in a solution have the same value, the variables are considered aligned and the solution is forwarded, with the redundant `sourceVar` projected out.

If the variables bind to different values, the solution is filtered out entirely.

**Arguments**
+ `sourceVar` – (*Required*) The source variable, to be compared to the target variable. If alignment succeeds in a solution, meaning that the two variables have the same value, the source variable is projected out.
+ `targetVar` – (*Required*) The target variable, with which the source variable is compared. Is retained even when alignment succeeds.
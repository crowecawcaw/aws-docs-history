# The openCypher `explain` feature

The openCypher `explain` feature is a self-service tool in Amazon Neptune
that helps you understand the execution approach taken by the Neptune engine. To invoke
explain, you pass a parameter to an openCypher [HTTPS](access-graph-opencypher-queries.md "access-graph-opencypher-queries.md")
request with `explain=`mode``, where the
 `_mode_` value can be one of the following:

######

- **`static`**   –  
  In `static` mode, `explain` prints only the static structure
  of the query plan. It doesn't actually run the query.
- **`dynamic`**   –  
  In `dynamic` mode, `explain` also runs the query, and
  includes dynamic aspects of the query plan. These may include the number of
  intermediate bindings flowing through the operators, the ratio of incoming
  bindings to outgoing bindings, and the total time taken by each operator.
- **`details`**   –  
  In `details` mode, `explain` prints the information shown
  in dynamic mode plus additional details, such as the actual openCypher query string
  and the estimated range count for the pattern underlying a join operator.
  For example, using `POST`:

```
curl HTTPS://`server`:`port`/openCypher \
  -d "query=MATCH (n) RETURN n LIMIT 1;" \
  -d "explain=dynamic"
```

Or, using `GET`:

```
curl -X GET \
  "HTTPS://`server`:`port`/openCypher?query=MATCH%20(n)%20RETURN%20n%20LIMIT%201&explain=dynamic"
```

## Limitations for openCypher `explain` in Neptune

The current release of openCypher explain has the following limitations:

- Explain plans are currently only available for queries that perform
  read-only operations. Queries that perform any sort of mutation, such as `CREATE`,
  `DELETE`, `MERGE`, `SET` and so on, are not
  supported.
- Operators and output for a specific plan may change in future releases.

## DFE operators in openCypher `explain` output

To use the information that the openCypher `explain` feature provides,
you need to understand some details about how the [DFE query engine](neptune-dfe-engine.md "neptune-dfe-engine.md")
works (DFE being the engine that Neptune uses to process openCypher queries).

The DFE engine translates every query into a pipeline of operators. Starting from
the first operator, intermediate solutions flow from one operator to the next through
this operator pipeline. Each row in the explain table represents a result, up to the
point of evaluation.

The operators that can appear in a DFE query plan are as follows:

**DFEApply**   –  
Executes the function specified in the arguments section, on the value stored in the specified variable

**DFEBindRelation**   –  
Binds together variables with the specified names

**DFEChunkLocalSubQuery**   –  
This is a non-blocking operation that acts as a wrapper around subqueries being performed.

**DFEDistinctColumn**   –  
Returns the distinct subset of the input values based on the variable specified.

**DFEDistinctRelation**   –  
Returns the distinct subset of the input solutions based on the variable specified.

**DFEDrain**   –  
Appears at the end of a subquery to act as a termination step for that subquery.
The number of solutions is recorded as `Units In`. `Units Out` is always zero.

**DFEForwardValue**   –  
Copies all input chunks directly as output chunks to be passed to its downstream operator.

**DFEGroupByHashIndex**   –  
Performs a group-by operation over the input solutions based on a previously computed hash index (using the
`DFEHashIndexBuild` operation). As an output, the given input is extended by a column containing
a group key for every input solution.

**DFEHashIndexBuild**   –  
Builds a hash index over a set of variables as a side-effect. This hash index is typically
reused in later operations. See `DFEHashIndexJoin` or `DFEGroupByHashIndex`
for where this hash index might be used.

**DFEHashIndexJoin**   –  
Performs a join over the incoming solutions against a previously built hash index. See `DFEHashIndexBuild`
for where this hash index might be built.

**DFEJoinExists**   –  
Takes a left and right hand input relation, and retains values from the left relation that have a corresponding
value in the right relation as defined by the given join variables.

  –  
This is a non-blocking operation that acts as a wrapper for a subquery, allowing it to be
run repeatedly for use in loops.

**DFEMergeChunks**   –  
This is a blocking operation that combines chunks from its upstream operator into a single chunk of solutions
to pass to its downstream operator (inverse of `DFESplitChunks`).

**DFEMinus**   –  
Takes a left and right hand input relation, and retains values from the left relation that
do not have a corresponding value in the right relation as defined by the given join variables.
If there is no overlap in variables across both relations, then this operator simply returns
the left hand input relation.

**DFENotExists**   –  
Takes a left and right hand input relation, and retains values from the left relation
that do not have a corresponding value in the right relation as defined by the given
join variables. If there is no overlap in variables across both relations, then this
operator returns an empty relation.

**DFEOptionalJoin**   –  
Performs a left outer join (also called OPTIONAL join): solutions from the left hand
side that have at least one join partner in the right-hand side are joined, and solutions
from the left-hand side without join partner in the right-hand side are forwarded as is.
This is a blocking operation.

**DFEPipelineJoin**   –  
Joins the input against the tuple pattern defined by the `pattern` argument.

**DFEPipelineRangeCount**   –  
Counts the number of solutions matching a given pattern, and returns a single one-ary solution containing the count value.

**DFEPipelineScan**   –  
Scans the database for the given `pattern` argument, with or without a given filter on column(s).

**DFEProject**   –  
Takes multiple input columns and projects only the desired columns.

**DFEReduce**   –  
Performs the specified aggregation function on specified variables.

**DFERelationalJoin**   –  
Joins the input of the previous operator based on the specified pattern keys using a merge join.
This is a blocking operation.

**DFERouteChunks**   –  
Takes input chunks from its singular incoming edge and routes those chunks along its multiple outgoing edges.

**DFESelectRows**   –  
This operator selectively takes rows from its left input relation solutions to forward to its
downstream operator. The rows selected based on the row identifiers supplied in the operator's
right input relation.

**DFESerialize**   –  
Serializes a query’s final results into a JSON string serialization,
mapping each input solution to the appropriate variable name. For node and edge
results, these results are serialized into a map of entity properties and metadata.

**DFESort**   –  
Takes an input relation and produces a sorted relation based on the provided sort key.

**DFESplitByGroup**   –  
Splits each single input chunk from one incoming edge into smaller output chunks corresponding to row
groups identified by row IDs from the corresponding input chunk from the other incoming edge.

**DFESplitChunks**   –  
Splits each single input chunk into smaller output chunks (inverse of `DFEMergeChunks`).

**DFEStreamingHashIndexBuild**   –  
Streaming version of `DFEHashIndexBuild`.

**DFEStreamingGroupByHashIndex**   –  
Streaming version of `DFEGroupByHashIndex`.

**DFESubquery**   –  
This operator appears at the beginning of all plans and encapsulates the portions of the
plan that are run on the [DFE engine](neptune-dfe-engine.md "neptune-dfe-engine.md"), which is the
entire plan for openCypher.

**DFESymmetricHashJoin**   –  
Joins the input of the previous operator based on the specified pattern keys using a hash join. This is a non-blocking operation.

**DFESync**   –  
This operator is a synchronization operator supporting non-blocking plans. It takes solutions
from two incoming edges and forwards these solutions to the appropriate downstream edges.
For synchronization purposes, the inputs along one of these edges may be buffered internally.

**DFETee**   –  
This is a branching operator that sends the same set of solutions to multiple operators.

**DFETermResolution**   –  
Performs a localize or globalize operation on its inputs, resulting in columns of either
localized or globalized identifiers respectively.

  –  
Unfolds lists of values from an input column into the output column as individual elements.

**DFEUnion**   –  
Takes two or more input relations and produces a union of those relations using the desired output schema.

**SolutionInjection**   –  
Appears before everything else in the explain output, with a value of 1 in the Units Out column.
However, it serves as a no-op, and doesn't actually inject any solutions into the DFE engine.

**TermResolution**   –  
Appears at the end of plans and translates objects from the Neptune engine into openCypher objects.

## Columns in openCypher `explain` output

The query plan information that Neptune generates as openCypher explain output
contains tables with one operator per row. The table has the following columns:

**ID**   –  
The numeric ID of this operator in the plan.

**Out #1** (and **Out #2**)   –  
The ID(s) of operator(s) that are downstream from this operator. There can be at most
two downstream operators.

**Name**   –  
The name of this operator.

**Arguments**   –  
Any relevant details for the operator. This includes things like input schema,
output schema, pattern (for `PipelineScan` and `PipelineJoin`),
and so on.

**Mode**   –  
A label describing fundamental operator behavior. This column is mostly blank (`-`).
One exception is `TermResolution`, where mode can be `id2value_opencypher`,
indicating a resolution from ID to openCypher value.

**Units In**   –  
The number of solutions passed as input to this operator. Operators without upstream operators,
such as `DFEPipelineScan`, `SolutionInjections`, and a `DFESubquery`
with no static value injected, would have zero value.

**Units Out**   –  
The number of solutions produced as output of this operator. `DFEDrain` is a special case,
where the number of solutions being drained is recorded in `Units In` and `Units Out`
is always zero.

**Ratio**   –  
The ratio of `Units Out` to `Units In`.

**Time (ms)**   –  
The CPU time consumed by this operator, in milliseconds.

## A basic example of openCypher explain output

The following is a basic example of openCypher `explain` output.
The query is a single-node lookup in the air routes dataset for a node
with the airport code `ATL` that invokes `explain` using the
`details` mode in default ASCII output format:

```
curl -d "query=MATCH (n {code: 'ATL'}) RETURN n" -k https://localhost:8182/openCypher -d "explain=details"                                                                                                      ~
Query:
MATCH (n {code: 'ATL'}) RETURN n

╔════╤════════╤════════╤═══════════════════╤════════════════════╤═════════════════════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name              │ Arguments          │ Mode                │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════╪════════════════════╪═════════════════════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ SolutionInjection │ solutions=[{}]     │ -                   │ 0        │ 1         │ 0.00  │ 0         ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFESubquery       │ subQuery=subQuery1 │ -                   │ 0        │ 1         │ 0.00  │ 4.00      ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ TermResolution    │ vars=[?n]          │ id2value_opencypher │ 1        │ 1         │ 1.00  │ 2.00      ║
╚════╧════════╧════════╧═══════════════════╧════════════════════╧═════════════════════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery1
╔════╤════════╤════════╤═══════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments                                                                                                    │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan       │ pattern=Node(?n) with property 'code' as ?n_code2 and label 'ALL'                                            │ -    │ 0        │ 1         │ 0.00  │ 0.21      ║
║    │        │        │                       │ inlineFilters=[(?n_code2 IN ["ATL"^^xsd:string])]                                                            │      │          │           │       │           ║
║    │        │        │                       │ patternEstimate=1                                                                                            │      │          │           │       │           ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEChunkLocalSubQuery │ subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#9d84f97c-c3b0-459a-98d5-955a8726b159/graph_1 │ -    │ 1        │ 1         │ 1.00  │ 0.04      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 3      │ -      │ DFEProject            │ columns=[?n]                                                                                                 │ -    │ 1        │ 1         │ 1.00  │ 0.04      ║
╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ -      │ -      │ DFEDrain              │ -                                                                                                            │ -    │ 1        │ 0         │ 0.00  │ 0.03      ║
╚════╧════════╧════════╧═══════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#9d84f97c-c3b0-459a-98d5-955a8726b159/graph_1
╔════╤════════╤════════╤══════════════════════╤════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                 │ Arguments                                                  │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪══════════════════════╪════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFESolutionInjection │ outSchema=[?n, ?n_code2]                                   │ -    │ 0        │ 1         │ 0.00  │ 0.02      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ 3      │ DFETee               │ -                                                          │ -    │ 1        │ 2         │ 2.00  │ 0.02      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 4      │ -      │ DFEDistinctColumn    │ column=?n                                                  │ -    │ 1        │ 1         │ 1.00  │ 0.20      ║
║    │        │        │                      │ ordered=false                                              │      │          │           │       │           ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ 5      │ -      │ DFEHashIndexBuild    │ vars=[?n]                                                  │ -    │ 1        │ 1         │ 1.00  │ 0.04      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 4  │ 5      │ -      │ DFEPipelineJoin      │ pattern=Node(?n) with property 'ALL' and label '?n_label1' │ -    │ 1        │ 1         │ 1.00  │ 0.25      ║
║    │        │        │                      │ patternEstimate=3506                                       │      │          │           │       │           ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 5  │ 6      │ 7      │ DFESync              │ -                                                          │ -    │ 2        │ 2         │ 1.00  │ 0.02      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 6  │ 8      │ -      │ DFEForwardValue      │ -                                                          │ -    │ 1        │ 1         │ 1.00  │ 0.01      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 7  │ 8      │ -      │ DFEForwardValue      │ -                                                          │ -    │ 1        │ 1         │ 1.00  │ 0.01      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 8  │ 9      │ -      │ DFEHashIndexJoin     │ -                                                          │ -    │ 2        │ 1         │ 0.50  │ 0.35      ║
╟────┼────────┼────────┼──────────────────────┼────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 9  │ -      │ -      │ DFEDrain             │ -                                                          │ -    │ 1        │ 0         │ 0.00  │ 0.02      ║
╚════╧════════╧════════╧══════════════════════╧════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```

At the top-level, `SolutionInjection` appears before everything else,
with 1 unit out. Note that it doesn't actually inject any solutions. You can see that the next
operator, `DFESubquery`, has 0 units in.

After `SolutionInjection` at the top-level are `DFESubquery` and
`TermResolution` operators. `DFESubquery` encapsulates the parts of
the query execution plan that is being pushed to the [DFE
engine](neptune-dfe-engine.md "neptune-dfe-engine.md") (for openCypher queries, the entire query plan is executed by the DFE).
All the operators in the query plan are nested inside `subQuery1` that is
referenced by `DFESubquery`. The only exception is `TermResolution`,
which materializes internal IDs into fully serialized openCypher objects.

All the operators that are pushed down to the DFE engine have names that start with
a `DFE` prefix. As mentioned above, the whole openCypher query plan is
executed by the DFE, so as a result, all the operators except the final `TermResolution`
operator start with `DFE`.

Inside `subQuery1`, there can be zero or more `DFEChunkLocalSubQuery`
or `DFELoopSubQuery` operators that encapsulate a part of the pushed execution
plan that is executed in a memory-bounded mechanism. `DFEChunkLocalSubQuery` here
contains one `SolutionInjection` that is used as an input to the subquery.
To find the table for that subquery in the output, search for the
`subQuery=`graph URI``specified in the`Arguments` column for the`DFEChunkLocalSubQuery`or`DFELoopSubQuery` operator.

In `subQuery1`, `DFEPipelineScan` with `ID` 0 scans
the database for a specified `pattern`. The pattern scans for an entity with
property `code` saved as a variable `?n_code2` over all labels
(you could filter on a specific label by appending `airport` to `n:airport`).
The `inlineFilters` argument shows the filtering for the `code`
property equalling `ATL`.

Next, the `DFEChunkLocalSubQuery` operator joins the intermediate results
of a subquery that contains `DFEPipelineJoin`. This ensures that `?n`
is actually a node, since the previous `DFEPipelineScan` scans for any entity
with the `code` property.

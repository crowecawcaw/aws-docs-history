# Query explain

The openCypher `explain` feature is a feature that helps users to understand how the query is executed.
Usually this is used in the context of query performance analysis.

## Explain inputs

To invoke `explain`, you can pass the explain-mode parameter to an ExecuteQuery request specifying the desired
explain mode (i.e., level of detail), where this explain mode value can be one of the following:

- `static` - In static mode, `explain` doesn't run the query, but instead prints only the
  static structure of the query plan.
- `details` - In details mode, `explain` runs the query, and includes dynamic aspects of
  the query plan. These may include the number of intermediate bindings flowing through the operators, the ratio
  of incoming bindings to outgoing bindings, and the total time taken by each operator. Additional details, such
  as the actual openCypher query string and the estimated range count for the pattern underlying a join operator,
  are also shown.

The following code examples provide the `explain-mode` when using either the AWS CLI or AWSCURL.

AWS CLI

```
aws neptune-graph execute-query \
--region <region> \
--graph-identifier <graph-id> \
--query-string <query-string> \
--explain-mode <explain-mode> \
--language open_cypher /tmp/out.txt
```

AWSCURL

```
awscurl -X POST "https://<graph-id>.<endpoint>/queries" \
-H "Content-Type: application/x-www-form-urlencoded" \
--region <region> \
--service neptune-graph \
-d "query=<query>&explain=<mode>"
```

## Explain outputs

**DFE operators in openCypher explain output**

To use the information that the openCypher explain feature provides, you need to understand some details about how the
DFE query engine works (DFE being the engine that Neptune uses to process openCypher queries).

The DFE engine translates every query into a pipeline of operators. Starting from the first operator, intermediate
solutions flow from one operator to the next through this operator pipeline. Each row in the explain table represents
a result, up to the point of evaluation. The operators that can appear in a DFE query plan are as follows:

- DFEApply – Executes the function specified by functor in the arguments section, on the value stored in the
  specified variable
- DFEAlgoWriteProperty – Explain operator for the property-writing portion of mutate algorithm invocations.
- DFEBFSAlgo – Explain operator for invocations of the Breadth First Search algorithm, which searches for nodes
  from a starting vertex (or starting vertices, also called multi-source BFS) in a graph in breadth-first order.
- DFEBindRelation – Binds together variables with the specified names.
- DFEChunkLocalSubQuery – This is a non-blocking operation that acts as a wrapper around subqueries being
  performed.
- DFEClosenessCentralityAlgo – Explain operator for invocations of the Closeness Centrality algorithm, which
  computes a metric that can be used as a positive measure of how close a given node is to all other nodes or
  how central it is in the graph.
- DFECommonNeighborsAlgo – Explain operator for invocations of the Common Neighbors algorithm, which counts
  the number of common neighbors of two input nodes.
- DFECreateConstant – Extends the given input relation with new columns containing constant values.
- DFEDegreeAlgo – Explain operator for invocations of the Degree algorithm, which calculates the number of
  edges that are incident to a vertex.
- DFEDistinctColumn – Returns the distinct subset of the input values based on the variable specified.
- DFEDistinctRelation – Returns the distinct subset of the input solutions based on the variable specified.
- DFEDrain – Appears at the end of a subquery to act as a termination step for that subquery. The number of
  solutions is recorded as Units In. Units Out is always zero.
- DFEForwardValue – Copies all input chunks directly as output chunks to be passed to its downstream operator.
- DFEGroupByHashIndex – This is a blocking operation that organizes the rows of a relation according to a set
  of variables, outputting a single group identifier column that is one-to-one with the rows of the input
  relation. Groups here are defined by the join variables used to build the hash index (See DFEHashIndexBuild
  for where this hash index might be built.)
- DFEHashIndexBuild – Builds a hash index over a set of variables as a side-effect. This hash index is typically
  reused in later operations. (See DFEHashIndexJoin for where this hash index might be used.)
- DFEHashIndexJoin – Performs a join over the incoming solutions against a previously built hash index. (See
  DFEHashIndexBuild for where this hash index might be built.)
- DFEJaccardSimilarityAlgo – Explain operator for invocations of the Jaccard similarity algorithm, which measures
  the similarity between two sets of nodes.
- DFEJoinExists – Takes a left and right hand input relation, and retains values from the left relation that
  have a corresponding value in the right relation as defined by the given join variables.
- DFELabelPropagationAlgo – Explain operator for invocations of the Label Propagation algorithm, which is used
  for community detection.
- DFELoopSubQuery – This is a non-blocking operation that acts as a wrapper for a subquery, allowing it to be
  run repeatedly for use in loops.
- DFEMergeChunks – This is a blocking operation that combines chunks from its upstream operator into a single
  chunk of solutions to pass to its downstream operator (inverse of DFESplitChunks).
- DFEMinus – Takes a left and right hand input relation, and retains values from the left relation that do not
  have a corresponding value in the right relation as defined by the given join variables. If there is no overlap
  in join variables across both relations, then this operator simply returns the left hand input relation as is.
- DFENotExists – Takes a left and right hand input relation, and retains values from the left relation that
  do not have a corresponding value in the right relation as defined by the given join variables. If there is
  no overlap in join variables, then this operator will return an empty relation.
- DFEOptionalJoin – Performs the optional join A OPTIONAL B ≡ (A JOIN B) UNION (A MINUS_NE B). This is a
  blocking operation.
- DFEOverlapSimilarityAlgo – Explain operator for invocations of the Overlap Similarity algorithm, which
  measures the overlap between the neighbors of two nodes.
- DFEPageRankAlgo – Explain operator for invocations of the Page Rank algorithm, which calculates a score
  for a given node based on the number, quality, and importance of the edges pointing to that node.
- DFEPipelineJoin – Joins the input against the tuple pattern defined by the pattern argument.
- DFEPipelineRangeCount – Counts the number of solutions matching a given pattern, and returns a
  single solution containing the count value.
- DFEPipelineScan – Scans the database for the given pattern argument, with or without a given filter
  on column(s).
- DFEProject – Takes multiple input columns and projects only the desired columns.
- DFEReduce – Performs the specified aggregation function on specified variables.
- DFERelationalJoin – Joins the input of the previous operator based on the specified pattern keys
  using a merge join. This is a blocking operation.
- DFERouteChunks – Takes input chunks from its singular incoming edge and routes those chunks along its
  multiple outgoing edges.
- DFESCCAlgo – Explain operator for invocations of the Strongly Connected Components algorithm, which
  calculates the maximally connected subgraphs of a directed graph where every node is reachable from every
  other node.
- DFESelectRows – This operator selectively takes rows from its left input relation solutions to forward
  to its downstream operator. The rows selected based on the row identifiers supplied in the operator’s
  right input relation.
- DFESerialize – Serializes a query’s final results into a JSON string serialization, mapping each input
  solution to the appropriate variable name. For node and edge results, these results are serialized into a
  map of entity properties and metadata.
- DFESort – Takes an input relation and produces a sorted relation based on the provided sort key.
- DFESplitByGroup – Splits each single input chunk from one incoming edge into smaller output chunks
  corresponding to row groups identified by row ids from the corresponding input chunk from the other
  incoming edge.
- DFESplitChunks – Splits each single input chunk into smaller output chunks (inverse of DFEMergeChunks).
- DFESSSPAlgo – Explain operator for invocations of the single source shortest path (SSSP) algorithms
  (Delta-stepping and Bellman-ford).
- DFEStreamingHashIndexBuild – Streaming version of DFEHashIndexBuild.
- DFEStreamingGroupByHashIndex – Streaming version of DFEGroupByHashIndex.
- DFESubquery – This operator appears at the beginning of all plans and encapsulates the portions
  of the plan that are run on the DFE engine, which is the entire plan for openCypher.
- DFESymmetricHashJoin – Joins the input of the previous operator based on the specified pattern keys using
  a hash join. This is a non-blocking operation.
- DFESync – This operator is a synchronization operator supporting non-blocking plans. It takes solutions
  from two incoming edges and forwards these solutions to the appropriate downstream edges. For synchronization
  purposes, the inputs along one of these edges may be buffered internally.
- DFETee – This is a branching operator that sends the same set of solutions to multiple operators.
- DFETermResolution – Performs a localize or globalize operation on its inputs, resulting in columns of
  either localized or globalized identifiers respectively.
- DFETopKSSSPAlgo – Explain operator for invocations of the TopK hop-limited single source (weighted)
  shortest path algorithm algorithm, which finds the single-source weighted shortest paths from a source
  node to its neighbors out to the distance specified by maxDepth.
- DFETotalNeighborsAlgo – Explain operator for invocations of the Total Neighbors algorithm, which counts
  the total number of unique neighbors of two input vertices.
- DFEUnfold – Unfolds lists of values from an input column into the output column as individual elements.
- DFEUnion – Takes two or more input relations and produces a union of those relations using the desired
  output schema.
- DFEVSSAlgo – Explain operator for invocations of the Vector similarity search algorithms, which find
  similar vectors based on the distance to each other.
- DFEWCCAlgo – Explain operator for invocations of the Weakly Connected Components algorithm, which finds
  the weakly-connected components in a directed graph.
- SolutionInjection – Appears before everything else in the explain output, with a value of one in the
  `Units Out` column. However, it serves a no-op, and doesn't actually inject any solutions into
  the DFE engine.
- TermResolution – Appears at the end of plans and translates of objects from the Neptune engine into
  openCypher objects.

**Columns in openCypher `explain` output**

The query plan information generated as openCypher explain output contains tables with one operator per row.
The table has the following columns:

- ID – The numeric ID of this operator in the plan.
- Out #1 (and Out #2) – The ID(s) of operator(s) that are downstream from this operator. There can be
  at most two downstream operators.
- Name – The name of this operator.
- Arguments – Any relevant details for the operator. This includes things like input schema, output schema,
  pattern (for `PipelineScan` and `PipelineJoin`), and so on.
- Mode – A label describing fundamental operator behavior. This column is mostly blank (-). One exception
  is `TermResolution`, where mode can be `id2value_opencypher`, indicating a resolution
  from ID to openCypher value.
- Units In – The number of solutions passed as input to this operator. Operators without upstream operators,
  such as `DFEPipelineScan`, `SolutionInjections`, and a `DFESubquery` with no
  static value injected, would have zero value.
- Units Out – The number of solutions produced as output of this operator. `DFEDrain` is a special
  case, where the number of solutions being drained is recorded in `Units In` and
  `Units Out` is always zero.
- Ratio – The ratio of `Units Out` to `Units In`.
- Time (ms) – The CPU time consumed by this operator, in milliseconds.

###### Note

Depending on the level of detail selected via the explain mode parameter, some of these columns may not appear
in the output.

## Explain examples

The following is a basic example of openCypher `explain` output. The query is a single-node lookup
in the air routes dataset for a node with the airport code `ATL` that invokes `explain`
using the details mode:

```
## sample query
aws neptune-graph execute-query \
--region <region> \
--graph-identifier <graph-id> \
--query-string "MATCH (n {code: 'ATL'}) RETURN n" \
--explain-mode details \
--language open_cypher /tmp/out.txt

## output
Query:
MATCH (n {code: 'ATL'}) RETURN n

╔════╤════════╤════════╤═══════════════════════╤════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments          │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════════╪════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ SolutionInjection     │ solutions=[{}]     │ -    │ 0        │ 1         │ 0.00  │ 0         ║
╟────┼────────┼────────┼───────────────────────┼────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ -      │ -      │ DFESubquery           │ subQuery=subQuery1 │ -    │ 0        │ 0         │ 0.00  │ 8.00      ║
╟────┼────────┼────────┼───────────────────────┼────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║    │        │        │ Summed execution time │                    │      │          │           │       │ 8.00      ║
╚════╧════════╧════════╧═══════════════════════╧════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery1
╔════╤════════╤════════╤════════════════════════╤══════════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name                   │ Arguments                                                        │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪════════════════════════╪══════════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan (DFX)  │ pattern=project ?n ?n_code2 (?n,code,?n_code2) [VERTEX_PROPERTY] │ -    │ 0        │ 1         │ 0.00  │ 0.03      ║
║    │        │        │                        │ inlineFilters=[(?n_code2 IN ["ATL"^^xsd:string])]                │      │          │           │       │           ║
║    │        │        │                        │ patternEstimate=1                                                │      │          │           │       │           ║
╟────┼────────┼────────┼────────────────────────┼──────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEProject (DFX)       │ columns=[?n]                                                     │ -    │ 1        │ 1         │ 1.00  │ 0.03      ║
╟────┼────────┼────────┼────────────────────────┼──────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ 3      │ -      │ DFESerialize (DFX)     │ columnsToSerialize=[?n]                                          │ -    │ 1        │ 0         │ 0.00  │ 0.08      ║
╟────┼────────┼────────┼────────────────────────┼──────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 3  │ -      │ -      │ DFEDrain (DFX)         │ -                                                                │ -    │ 0        │ 0         │ 0.00  │ 0         ║
╟────┼────────┼────────┼────────────────────────┼──────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║    │        │        │ Summed execution time  │                                                                  │      │          │           │       │ 0.15      ║
╚════╧════════╧════════╧════════════════════════╧══════════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```

At the top-level, `SolutionInjection` appears before everything else, with 1 unit out. Note that it doesn't
actually inject any solutions. You can see that the next operator, `DFESubquery`, has 0 units in.

After `SolutionInjection` at the top-level is the `DFESubquery` operator. `DFESubquery`
encapsulates the parts of the query execution plan that are pushed to the DFE engine (for openCypher queries, the
entire query plan is executed by the DFE). All the operators in the query plan are nested inside `subQuery1`
that is referenced by `DFESubquery`.

All the operators that are pushed down to the DFE engine have names that start with a `DFE`
prefix. As mentioned above, the whole openCypher query plan is executed by the DFE, so as a result, all of the
operators start with `DFE`.

Inside `subQuery1`, there can be zero (as in this case) or more `DFEChunkLocalSubQuery` or
`DFELoopSubQuery` operators that encapsulate a part of the pushed execution plan that is executed in
a memory-bounded mechanism. A `DFEChunkLocalSubQuery` contains one `SolutionInjection` that
is used as an input to the subquery. To find the table for that subquery in the output, search for the
`subQuery=graph URI` specified in the `Arguments` column for the `DFEChunkLocalSubQuery`
or `DFELoopSubQuery` operator.

In `subQuery1`, `DFEPipelineScan` with `ID` 0 scans the database for a specified
`pattern`. The pattern scans for vertices `?n` with property `code` saved as a
variable `?n_code2`. The `inlineFilters` argument shows the filtering for the `code`
property equaling `ATL`.

Next, the `DFEProject` operator propagates forward only the `?n` variable we’re interested in.
Finally, the `DFESerialize` operator performs result serialization, transforming the input solutions
into a readable format.

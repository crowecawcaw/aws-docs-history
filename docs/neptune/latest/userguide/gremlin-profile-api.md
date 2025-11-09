# Gremlin `profile` API in Neptune

The Neptune Gremlin `profile` API runs a specified Gremlin traversal,
collects various metrics about the run, and produces a profile report as output.

###### Note

This feature is available starting with [Release 1.0.1.0.200463.0 (2019-10-15)](engine-releases-1.0.1.0.200463.md "engine-releases-1.0.1.0.200463.md").

It differs from the TinkerPop .profile() step so as to be able to report
information specific to the Neptune engine.

The profile report includes the following information about the query plan:

- The physical operator pipeline
- The index operations for query execution and serialization
- The size of the result
  The `profile` API uses an extended version of the HTTP API syntax for query,
  with `/gremlin/profile` as the endpoint instead of `/gremlin`.

## Parameters specific to Neptune Gremlin `profile`

- **profile.results**
  – `boolean`, allowed values: `TRUE` and `FALSE`,
  default value: `TRUE`.

If true, the query results are gathered and displayed as part of the `profile` report.
If false, only the result count is displayed.

- **profile.chop**
  – `int`, default value: 250.

If non-zero, causes the results string to be truncated at that number of characters.
This does not keep all results from being captured. It simply limits the size of the
string in the profile report. If set to zero, the string contains all the results.

- **profile.serializer**
  – `string`, default value: `<null>`.

If non-null, the gathered results are returned in a serialized response message in the
format specified by this parameter. The number of index operations necessary to produce
that response message is reported along with the size in bytes to be sent to the
client.

Allowed values are `<null>` or any of the valid MIME type or
TinkerPop driver "Serializers" enum values.

```

"application/json" or "GRAPHSON"
"application/vnd.gremlin-v1.0+json" or "GRAPHSON_V1"
"application/vnd.gremlin-v1.0+json;types=false" or "GRAPHSON_V1_UNTYPED"
"application/vnd.gremlin-v2.0+json" or "GRAPHSON_V2"
"application/vnd.gremlin-v2.0+json;types=false" or "GRAPHSON_V2_UNTYPED"
"application/vnd.gremlin-v3.0+json" or "GRAPHSON_V3"
"application/vnd.gremlin-v3.0+json;types=false" or "GRAPHSON_V3_UNTYPED"
"application/vnd.graphbinary-v1.0" or "GRAPHBINARY_V1"

```

- **profile.indexOps**
  – `boolean`, allowed values: `TRUE` and `FALSE`,
  default value: `FALSE`.

If true, shows a detailed report of all index operations that took place during query
execution and serialization. Warning: This report can be verbose.

## Sample output of Neptune Gremlin `profile`

The following is a sample `profile` query.

```
curl -X POST https://`your-neptune-endpoint`:`port`/gremlin/profile \
     -d '{"gremlin":"g.V().hasLabel(\"airport\")
                          .has(\"code\", \"AUS\")
                          .emit()
                          .repeat(in().simplePath())
                          .times(2)
                          .limit(100)",
          "profile.serializer":"application/vnd.gremlin-v3.0+gryo"}'
```

This query generates the following `profile` report when executed on the
air-routes sample graph from the blog post, [Let Me Graph That For You – Part 1 – Air Routes](https://aws.amazon.com/blogs/database/let-me-graph-that-for-you-part-1-air-routes/ "https://aws.amazon.com/blogs/database/let-me-graph-that-for-you-part-1-air-routes/").

```
*******************************************************
                Neptune Gremlin Profile
*******************************************************

Query String
==================
g.V().hasLabel("airport").has("code", "AUS").emit().repeat(in().simplePath()).times(2).limit(100)

Original Traversal
==================
[GraphStep(vertex,[]), HasStep([~label.eq(airport), code.eq(AUS)]), RepeatStep(emit(true),[VertexStep(IN,vertex), PathFilterStep(simple), RepeatEndStep],until(loops(2))), RangeGlobalStep(0,100)]

Optimized Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <code>, "AUS", ?) . project ?1 .], {estimatedCardinality=1, indexTime=84, hashJoin=true, joinTime=3, actualTotalOutput=1}
            PatternNode[(?1, <~label>, ?2=<airport>, <~>) . project ask .], {estimatedCardinality=3374, indexTime=29, hashJoin=true, joinTime=0, actualTotalOutput=61}
            RepeatNode {
                Repeat {
                    PatternNode[(?3, ?5, ?1, ?6) . project ?1,?3 . IsEdgeIdFilter(?6) . SimplePathFilter(?1, ?3)) .], {hashJoin=true, estimatedCardinality=50148, indexTime=0, joinTime=3}
                }
                Emit {
                    Filter(true)
                }
                LoopsCondition {
                    LoopsFilter([?1, ?3],eq(2))
                }
            }, annotations={repeatMode=BFS, emitFirst=true, untilFirst=false, leftVar=?1, rightVar=?3}
        }, finishers=[limit(100)], annotations={path=[Vertex(?1):GraphStep, Repeat[Vertex(?3):VertexStep]], joinStats=true, optimizationTime=495, maxVarId=7, executionTime=323}
    },
    NeptuneTraverserConverterStep
]

Physical Pipeline
=================
NeptuneGraphQueryStep
    |-- StartOp
    |-- JoinGroupOp
        |-- SpoolerOp(100)
        |-- DynamicJoinOp(PatternNode[(?1, <code>, "AUS", ?) . project ?1 .], {estimatedCardinality=1, indexTime=84, hashJoin=true})
        |-- SpoolerOp(100)
        |-- DynamicJoinOp(PatternNode[(?1, <~label>, ?2=<airport>, <~>) . project ask .], {estimatedCardinality=3374, indexTime=29, hashJoin=true})
        |-- RepeatOp
            |-- <upstream input> (Iteration 0) [visited=1, output=1 (until=0, emit=1), next=1]
            |-- BindingSetQueue (Iteration 1) [visited=61, output=61 (until=0, emit=61), next=61]
                |-- SpoolerOp(100)
                |-- DynamicJoinOp(PatternNode[(?3, ?5, ?1, ?6) . project ?1,?3 . IsEdgeIdFilter(?6) . SimplePathFilter(?1, ?3)) .], {hashJoin=true, estimatedCardinality=50148, indexTime=0})
            |-- BindingSetQueue (Iteration 2) [visited=38, output=38 (until=38, emit=0), next=0]
                |-- SpoolerOp(100)
                |-- DynamicJoinOp(PatternNode[(?3, ?5, ?1, ?6) . project ?1,?3 . IsEdgeIdFilter(?6) . SimplePathFilter(?1, ?3)) .], {hashJoin=true, estimatedCardinality=50148, indexTime=0})
        |-- LimitOp(100)

Runtime (ms)
============
Query Execution:  392.686
Serialization:   2636.380

Traversal Metrics
=================
Step                                                               Count  Traversers       Time (ms)    % Dur
-------------------------------------------------------------------------------------------------------------
NeptuneGraphQueryStep(Vertex)                                        100         100         314.162    82.78
NeptuneTraverserConverterStep                                        100         100          65.333    17.22
                                            >TOTAL                     -           -         379.495        -

Repeat Metrics
==============
Iteration  Visited   Output    Until     Emit     Next
------------------------------------------------------
        0        1        1        0        1        1
        1       61       61        0       61       61
        2       38       38       38        0        0
------------------------------------------------------
               100      100       38       62       62

Predicates
==========
# of predicates: 16

WARNING: reverse traversal with no edge label(s) - .in() / .both() may impact query performance

Results
=======
Count: 100
Output: [v[3], v[3600], v[3614], v[4], v[5], v[6], v[7], v[8], v[9], v[10], v[11], v[12], v[47], v[49], v[136], v[13], v[15], v[16], v[17], v[18], v[389], v[20], v[21], v[22], v[23], v[24], v[25], v[26], v[27], v[28], v[416], v[29], v[30], v[430], v[31], v[9...
Response serializer: GRYO_V3D0
Response size (bytes): 23566

Index Operations
================
Query execution:
    # of statement index ops: 3
    # of unique statement index ops: 3
    Duplication ratio: 1.0
    # of terms materialized: 0
Serialization:
    # of statement index ops: 200
    # of unique statement index ops: 140
    Duplication ratio: 1.43
    # of terms materialized: 393
```

In addition to the query plans returned by a call to Neptune `explain`,
the `profile` results include runtime statistics around query execution.
Each Join operation is tagged with the time it took to perform its join as well
as the actual number of solutions that passed through it.

The `profile` output includes the time taken during the core query execution
phase, as well as the serialization phase if the `profile.serializer` option
was specified.

The breakdown of the index operations performed during each phase is also
included at the bottom of the `profile` output.

Note that consecutive runs of the same query may show different results in
terms of run-time and index operations because of caching.

For queries using the `repeat()` step, a breakdown of the frontier
on each iteration is available if the `repeat()` step was pushed down
as part of a `NeptuneGraphQueryStep`.

## Differences in `profile` reports when DFE is enabled

When the Neptune DFE alternative query engine is enabled, `profile` output
is somewhat different:

**Optimized Traversal:**
This section is similar to the one in `explain` output, but contains
additional information. This includes the type of DFE operators that were considered
in planning, and the associated worst case and best case cost estimates.

**Physical Pipeline:**
This section captures the operators that are used to execute the query.
`DFESubQuery` elements abstract the physical plan that is used by DFE to
execute the portion of the plan it is responsible for. The `DFESubQuery`
elements are unfolded in the following section where DFE statistics are listed.

**DFEQueryEngine Statistics:**
This section shows up only when at least part of the query is executed by DFE.
It outlines various runtime statistics that are specific to DFE, and contains
a detailed breakdown of the time spent in the various parts of the query execution,
by `DFESubQuery`.

Nested subqueries in different `DFESubQuery` elements are flattened
in this section, and unique identifiers are marked with a header that starts with
`subQuery=`.

**Traversal metrics:**
This section shows step-level traversal metrics, and when the DFE engine runs all
or part of the query, displays metrics for `DFEStep` and/or
`NeptuneInterleavingStep`. See [Tuning Gremlin queries using explain and profile](gremlin-traversal-tuning.md "gremlin-traversal-tuning.md").

###### Note

DFE is an experimental feature released under lab mode, so the
exact format of the `profile` output is still subject to change.

## Sample `profile` output when the Neptune Dataflow engine (DFE) is enabled

When the DFE engine is being used to run Gremlin queries, output of the
[Gremlin profile API](gremlin-profile-api.md "gremlin-profile-api.md") is
formatted as shown in the example below.

Query:

```
curl https://localhost:8182/gremlin/profile \
  -d "{\"gremlin\": \"g.withSideEffect('Neptune#useDFE', true).V().has('code', 'ATL').out()\"}"
```

```
*******************************************************
                    Neptune Gremlin Profile
    *******************************************************

    Query String
    ==================
    g.withSideEffect('Neptune#useDFE', true).V().has('code', 'ATL').out()

    Original Traversal
    ==================
    [GraphStep(vertex,[]), HasStep([code.eq(ATL)]), VertexStep(OUT,vertex)]

    Optimized Traversal
    ===================
    Neptune steps:
    [
        DFEStep(Vertex) {
          DFENode {
            DFEJoinGroupNode[null](
              children=[
                DFEPatternNode((?1, vp://code[419430926], ?4, defaultGraph[526]) . project DISTINCT[?1] objectFilters=(in(ATL[452987149]) . ), {rangeCountEstimate=1},
                  opInfo=(type=PipelineJoin, cost=(exp=(in=1.00,out=1.00,io=0.00,comp=0.00,mem=0.00),wc=(in=1.00,out=1.00,io=0.00,comp=0.00,mem=0.00)),
                    disc=(type=PipelineScan, cost=(exp=(in=1.00,out=1.00,io=0.00,comp=0.00,mem=34.00),wc=(in=1.00,out=1.00,io=0.00,comp=0.00,mem=34.00))))),
                DFEPatternNode((?1, ?5, ?6, ?7) . project ALL[?1, ?6] graphFilters=(!= defaultGraph[526] . ), {rangeCountEstimate=9223372036854775807})],
              opInfo=[
                OperatorInfoWithAlternative[
                  rec=(type=PipelineJoin, cost=(exp=(in=1.00,out=27.76,io=0.00,comp=0.00,mem=0.00),wc=(in=1.00,out=27.76,io=0.00,comp=0.00,mem=0.00)),
                    disc=(type=PipelineScan, cost=(exp=(in=1.00,out=27.76,io=Infinity,comp=0.00,mem=295147905179352830000.00),wc=(in=1.00,out=27.76,io=Infinity,comp=0.00,mem=295147905179352830000.00)))),
                  alt=(type=PipelineScan, cost=(exp=(in=1.00,out=27.76,io=Infinity,comp=0.00,mem=295147905179352830000.00),wc=(in=1.00,out=27.76,io=Infinity,comp=0.00,mem=295147905179352830000.00)))]])
          } [Vertex(?1):GraphStep, Vertex(?6):VertexStep]
        } ,
        NeptuneTraverserConverterDFEStep,
        DFECleanupStep
    ]


    Physical Pipeline
    =================
    DFEStep
        |-- DFESubQuery1

    DFEQueryEngine Statistics
    =================
    DFESubQuery1
    ╔════╤════════╤════════╤═══════════════════════╤══════════════════════════════════════════════════════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤════════╤═══════════╗
    ║ ID │ Out #1 │ Out #2 │ Name                  │ Arguments                                                                                                    │ Mode │ Units In │ Units Out │ Ratio  │ Time (ms) ║
    ╠════╪════════╪════════╪═══════════════════════╪══════════════════════════════════════════════════════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪════════╪═══════════╣
    ║ 0  │ 1      │ -      │ DFESolutionInjection  │ solutions=[]                                                                                                 │ -    │ 0        │ 1         │ 0.00   │ 0.01      ║
    ║    │        │        │                       │ outSchema=[]                                                                                                 │      │          │           │        │           ║
    ╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 1  │ 2      │ -      │ DFEChunkLocalSubQuery │ subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#089f43e3-4d71-4259-8d19-254ff63cee04/graph_1 │ -    │ 1        │ 1         │ 1.00   │ 0.02      ║
    ╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 2  │ 3      │ -      │ DFEChunkLocalSubQuery │ subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#089f43e3-4d71-4259-8d19-254ff63cee04/graph_2 │ -    │ 1        │ 242       │ 242.00 │ 0.02      ║
    ╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 3  │ 4      │ -      │ DFEMergeChunks        │ -                                                                                                            │ -    │ 242      │ 242       │ 1.00   │ 0.01      ║
    ╟────┼────────┼────────┼───────────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 4  │ -      │ -      │ DFEDrain              │ -                                                                                                            │ -    │ 242      │ 0         │ 0.00   │ 0.01      ║
    ╚════╧════════╧════════╧═══════════════════════╧══════════════════════════════════════════════════════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧════════╧═══════════╝


    subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#089f43e3-4d71-4259-8d19-254ff63cee04/graph_1
    ╔════╤════════╤════════╤══════════════════════╤═════════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
    ║ ID │ Out #1 │ Out #2 │ Name                 │ Arguments                                                   │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
    ╠════╪════════╪════════╪══════════════════════╪═════════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
    ║ 0  │ 1      │ -      │ DFEPipelineScan      │ pattern=Node(?1) with property 'code' as ?4 and label 'ALL' │ -    │ 0        │ 1         │ 0.00  │ 0.22      ║
    ║    │        │        │                      │ inlineFilters=[(?4 IN ["ATL"])]                             │      │          │           │       │           ║
    ║    │        │        │                      │ patternEstimate=1                                           │      │          │           │       │           ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
    ║ 1  │ 2      │ -      │ DFEMergeChunks       │ -                                                           │ -    │ 1        │ 1         │ 1.00  │ 0.02      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
    ║ 2  │ 4      │ -      │ DFERelationalJoin    │ joinVars=[]                                                 │ -    │ 2        │ 1         │ 0.50  │ 0.09      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
    ║ 3  │ 2      │ -      │ DFESolutionInjection │ solutions=[]                                                │ -    │ 0        │ 1         │ 0.00  │ 0.01      ║
    ║    │        │        │                      │ outSchema=[]                                                │      │          │           │       │           ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
    ║ 4  │ -      │ -      │ DFEDrain             │ -                                                           │ -    │ 1        │ 0         │ 0.00  │ 0.01      ║
    ╚════╧════════╧════════╧══════════════════════╧═════════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝


    subQuery=http://aws.amazon.com/neptune/vocab/v01/dfe/past/graph#089f43e3-4d71-4259-8d19-254ff63cee04/graph_2
    ╔════╤════════╤════════╤══════════════════════╤═════════════════════════════════════╤══════╤══════════╤═══════════╤════════╤═══════════╗
    ║ ID │ Out #1 │ Out #2 │ Name                 │ Arguments                           │ Mode │ Units In │ Units Out │ Ratio  │ Time (ms) ║
    ╠════╪════════╪════════╪══════════════════════╪═════════════════════════════════════╪══════╪══════════╪═══════════╪════════╪═══════════╣
    ║ 0  │ 1      │ -      │ DFESolutionInjection │ solutions=[]                        │ -    │ 0        │ 1         │ 0.00   │ 0.01      ║
    ║    │        │        │                      │ outSchema=[?1]                      │      │          │           │        │           ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 1  │ 2      │ 3      │ DFETee               │ -                                   │ -    │ 1        │ 2         │ 2.00   │ 0.01      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 2  │ 4      │ -      │ DFEDistinctColumn    │ column=?1                           │ -    │ 1        │ 1         │ 1.00   │ 0.21      ║
    ║    │        │        │                      │ ordered=false                       │      │          │           │        │           ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 3  │ 5      │ -      │ DFEHashIndexBuild    │ vars=[?1]                           │ -    │ 1        │ 1         │ 1.00   │ 0.03      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 4  │ 5      │ -      │ DFEPipelineJoin      │ pattern=Edge((?1)-[?7:?5]->(?6))    │ -    │ 1        │ 242       │ 242.00 │ 0.51      ║
    ║    │        │        │                      │ constraints=[]                      │      │          │           │        │           ║
    ║    │        │        │                      │ patternEstimate=9223372036854775807 │      │          │           │        │           ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 5  │ 6      │ 7      │ DFESync              │ -                                   │ -    │ 243      │ 243       │ 1.00   │ 0.02      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 6  │ 8      │ -      │ DFEForwardValue      │ -                                   │ -    │ 1        │ 1         │ 1.00   │ 0.01      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 7  │ 8      │ -      │ DFEForwardValue      │ -                                   │ -    │ 242      │ 242       │ 1.00   │ 0.02      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 8  │ 9      │ -      │ DFEHashIndexJoin     │ -                                   │ -    │ 243      │ 242       │ 1.00   │ 0.31      ║
    ╟────┼────────┼────────┼──────────────────────┼─────────────────────────────────────┼──────┼──────────┼───────────┼────────┼───────────╢
    ║ 9  │ -      │ -      │ DFEDrain             │ -                                   │ -    │ 242      │ 0         │ 0.00   │ 0.01      ║
    ╚════╧════════╧════════╧══════════════════════╧═════════════════════════════════════╧══════╧══════════╧═══════════╧════════╧═══════════╝


    Runtime (ms)
    ============
    Query Execution: 11.744

    Traversal Metrics
    =================
    Step                                                               Count  Traversers       Time (ms)    % Dur
    -------------------------------------------------------------------------------------------------------------
    DFEStep(Vertex)                                                      242         242          10.849    95.48
    NeptuneTraverserConverterDFEStep                                     242         242           0.514     4.52
                                                >TOTAL                     -           -          11.363        -

    Predicates
    ==========
    # of predicates: 18

    Results
    =======
    Count: 242


    Index Operations
    ================
    Query execution:
        # of statement index ops: 0
        # of terms materialized: 0
```

###### Note

Because the DFE engine is an experimental feature released in lab mode,
the exact format of the `profile` output is subject to change.

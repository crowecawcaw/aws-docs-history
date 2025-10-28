# Using the Gremlin `explain` API in Neptune

The Amazon Neptune Gremlin `explain` API returns the query plan that would be
executed if a specified query were run. Because the API doesn't actually run the query, the
plan is returned almost instantaneously.

It differs from the TinkerPop .explain() step so as to be able to report
information specific to the Neptune engine.

## Information contained in a Gremlin `explain` report

An `explain` report contains the following information:

- The query string as requested.
- **The original traversal.**
  This is the TinkerPop Traversal object produced by parsing the query string
  into TinkerPop steps. It is equivalent to the original query produced
  by running `.explain()` on the query against the TinkerPop
  TinkerGraph.
- **The converted traversal.**
  This is the Neptune Traversal produced by converting the TinkerPop Traversal
  into the Neptune logical query plan representation. In many cases the entire
  TinkerPop traversal is converted into two Neptune steps: one that executes
  the entire query (`NeptuneGraphQueryStep`) and one that converts the
  Neptune query engine output back into TinkerPop Traversers
  (`NeptuneTraverserConverterStep`).
- **The optimized traversal.**
  This is the optimized version of the Neptune query plan after it has been run
  through a series of static work-reducing optimizers that rewrite the query
  based on static analysis and estimated cardinalities. These optimizers do
  things like reorder operators based on range counts, prune unnecessary or
  redundant operators, rearrange filters, push operators into different groups,
  and so on.
- **The predicate count.**
  Because of the Neptune indexing strategy described earlier, having a large
  number of different predicates can cause performance problems. This is
  especially true for queries that use reverse traversal operators with
  no edge label (`.in` or `.both`).
  If such operators are used and the predicate count is high enough, the
  `explain` report displays a warning message.
- **DFE information.**
  When the DFE alternative engine is enabled, the following traversal components
  may show up in the optimized traversal:

      + **`DFEStep`**   –  
       A Neptune optimized DFE step in the traversal that contains a child
       `DFENode`. `DFEStep` represents the part of the query plan
       that is executed in the DFE engine.
      + **`DFENode`**   –  
       Contains the intermediate representation as one or more child `DFEJoinGroupNodes`.
      + **`DFEJoinGroupNode`**   –  
       Represents a join of one or more `DFENode` or `DFEJoinGroupNode`
       elements.
      + **`NeptuneInterleavingStep`**   –  
       A Neptune optimized DFE step in the traversal that contains a child `DFEStep`.


      Also contains a `stepInfo` element that contains information
       about the traversal, such as the frontier element, the path elements used,
       and so on. This information is used to process the child `DFEStep`.

  An easy way to find out if your query is being evaluated by DFE is to check
  whether the `explain` output contains a `DFEStep`. Any part
  of the traversal that is not part of the `DFEStep` will not be executed
  by DFE and will be executed by the TinkerPop engine.

See [Example with DFE enabled](#gremlin-explain-dfe "#gremlin-explain-dfe")
for a sample report.

## Gremlin `explain` syntax

The syntax of the `explain` API is the same as that for the HTTP API for query,
except that it uses `/gremlin/explain` as the endpoint instead of
`/gremlin`, as in the following example.

```
curl -X POST https://`your-neptune-endpoint`:`port`/gremlin/explain -d '{"gremlin":"g.V().limit(1)"}'
```

The preceding query would produce the following output.

```
*******************************************************
                Neptune Gremlin Explain
*******************************************************

Query String
============
g.V().limit(1)

Original Traversal
==================
[GraphStep(vertex,[]), RangeGlobalStep(0,1)]

Converted Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <~label>, ?2, <~>) . project distinct ?1 .]
        }, finishers=[limit(1)], annotations={path=[Vertex(?1):GraphStep], maxVarId=3}
    },
    NeptuneTraverserConverterStep
]

Optimized Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <~label>, ?2, <~>) . project distinct ?1 .], {estimatedCardinality=INFINITY}
        }, finishers=[limit(1)], annotations={path=[Vertex(?1):GraphStep], maxVarId=3}
    },
    NeptuneTraverserConverterStep
]

Predicates
==========
# of predicates: 18
```

## Unconverted TinkerPop Steps

Ideally, all TinkerPop steps in a traversal have native Neptune operator coverage. When
this isn't the case, Neptune falls back on TinkerPop step execution for gaps in its
operator coverage. If a traversal uses a step for which Neptune does not yet have
native coverage, the `explain` report displays a warning showing where the
gap occurred.

When a step without a corresponding native Neptune operator is encountered, the entire
traversal from that point forward is run using TinkerPop steps, even if subsequent steps
do have native Neptune operators.

The exception to this is when Neptune full-text search is invoked. The
NeptuneSearchStep implements steps without native equivalents as full-text
search steps.

## Example of `explain` output where all steps in a query have native equivalents

The following is an example `explain` report for a query where
all steps have native equivalents:

```
*******************************************************
                Neptune Gremlin Explain
*******************************************************

Query String
============
g.V().out()

Original Traversal
==================
[GraphStep(vertex,[]), VertexStep(OUT,vertex)]

Converted Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <~label>, ?2, <~>) . project distinct ?1 .]
            PatternNode[(?1, ?5, ?3, ?6) . project ?1,?3 . IsEdgeIdFilter(?6) .]
            PatternNode[(?3, <~label>, ?4, <~>) . project ask .]
        }, annotations={path=[Vertex(?1):GraphStep, Vertex(?3):VertexStep], maxVarId=7}
    },
    NeptuneTraverserConverterStep
]

Optimized Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, ?5, ?3, ?6) . project ?1,?3 . IsEdgeIdFilter(?6) .], {estimatedCardinality=INFINITY}
        }, annotations={path=[Vertex(?1):GraphStep, Vertex(?3):VertexStep], maxVarId=7}
    },
    NeptuneTraverserConverterStep
]

Predicates
==========
# of predicates: 18
```

## Example where some steps in a query do not have native equivalents

Neptune handles both `GraphStep` and `VertexStep` natively, but if
you introduce a `FoldStep` and `UnfoldStep`, the resulting
`explain` output is different:

```
*******************************************************
                Neptune Gremlin Explain
*******************************************************

Query String
============
g.V().fold().unfold().out()

Original Traversal
==================
[GraphStep(vertex,[]), FoldStep, UnfoldStep, VertexStep(OUT,vertex)]

Converted Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <~label>, ?2, <~>) . project distinct ?1 .]
        }, annotations={path=[Vertex(?1):GraphStep], maxVarId=3}
    },
    NeptuneTraverserConverterStep
]
+ not converted into Neptune steps: [FoldStep, UnfoldStep, VertexStep(OUT,vertex)]

Optimized Traversal
===================
Neptune steps:
[
    NeptuneGraphQueryStep(Vertex) {
        JoinGroupNode {
            PatternNode[(?1, <~label>, ?2, <~>) . project distinct ?1 .], {estimatedCardinality=INFINITY}
        }, annotations={path=[Vertex(?1):GraphStep], maxVarId=3}
    },
    NeptuneTraverserConverterStep,
    NeptuneMemoryTrackerStep
]
+ not converted into Neptune steps: [FoldStep, UnfoldStep, VertexStep(OUT,vertex)]

WARNING: >> FoldStep << is not supported natively yet
```

In this case, the `FoldStep` breaks you out of native execution.
But even the subsequent `VertexStep` is no longer handled natively
because it appears downstream of the `Fold/Unfold` steps.

For performance and cost-savings, it's important that you try to formulate traversals so
that the maximum amount of work possible is done natively inside the Neptune query
engine, instead of by the TinkerPop step implementations.

## Example of a query that uses Neptune full-text-search

The following query uses Neptune full-text search:

```
g.withSideEffect("`Neptune#fts.endpoint`", "`some_endpoint`")
  .V()
  .tail(100)
  .has("Neptune#fts mark*")
  -------
  .has("name", "Neptune#fts mark*")
  .has("Person", "name", "Neptune#fts mark*")
```

The `.has("name", "Neptune#fts mark*")` part limits the search
to vertexes with `name`, while `.has("Person", "name", "Neptune#fts mark*")`
limits the search to vertexes with `name` and the label `Person`.
This results in the following traversal in the `explain` report:

```
Final Traversal
[NeptuneGraphQueryStep(Vertex) {
    JoinGroupNode {
        PatternNode[(?1, termid(1,URI), ?2, termid(0,URI)) . project distinct ?1 .], {estimatedCardinality=INFINITY}
    }, annotations={path=[Vertex(?1):GraphStep], maxVarId=4}
}, NeptuneTraverserConverterStep, NeptuneTailGlobalStep(10), NeptuneTinkerpopTraverserConverterStep, NeptuneSearchStep {
    JoinGroupNode {
        SearchNode[(idVar=?3, query=mark*, field=name) . project ask .], {endpoint=some_endpoint}
    }
    JoinGroupNode {
        SearchNode[(idVar=?3, query=mark*, field=name) . project ask .], {endpoint=some_endpoint}
    }
}]
```

## Example of using `explain` when the DFE is enabled

The following is an example of an `explain` report when the
DFE alternative query engine is enabled:

```
*******************************************************
                Neptune Gremlin Explain
*******************************************************

Query String
============

g.V().as("a").out().has("name", "josh").out().in().where(eq("a"))


Original Traversal
==================
[GraphStep(vertex,[])@[a], VertexStep(OUT,vertex), HasStep([name.eq(josh)]), VertexStep(OUT,vertex), VertexStep(IN,vertex), WherePredicateStep(eq(a))]

Converted Traversal
===================
Neptune steps:
[
    DFEStep(Vertex) {
      DFENode {
        DFEJoinGroupNode[ children={
          DFEPatternNode[(?1, <http://www.w3.org/1999/02/22-rdf-syntax-ns#type>, ?2, <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph>) . project DISTINCT[?1] {rangeCountEstimate=unknown}],
          DFEPatternNode[(?1, ?3, ?4, ?5) . project ALL[?1, ?4] graphFilters=(!= <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph> . ), {rangeCountEstimate=unknown}]
        }, {rangeCountEstimate=unknown}
        ]
      } [Vertex(?1):GraphStep@[a], Vertex(?4):VertexStep]
    } ,
    NeptuneTraverserConverterDFEStep
]
+ not converted into Neptune steps: HasStep([name.eq(josh)]),
Neptune steps:
[
    NeptuneInterleavingStep {
      StepInfo[joinVars=[?7, ?1], frontierElement=Vertex(?7):HasStep, pathElements={a=(last,Vertex(?1):GraphStep@[a])}, listPathElement={}, indexTime=0ms],
      DFEStep(Vertex) {
        DFENode {
          DFEJoinGroupNode[ children={
            DFEPatternNode[(?7, ?8, ?9, ?10) . project ALL[?7, ?9] graphFilters=(!= <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph> . ), {rangeCountEstimate=unknown}],
            DFEPatternNode[(?12, ?11, ?9, ?13) . project ALL[?9, ?12] graphFilters=(!= <http://aws.amazon.com/neptune/vocab/v01/DefaultNamedGraph> . ), {rangeCountEstimate=unknown}]
          }, {rangeCountEstimate=unknown}
          ]
        } [Vertex(?9):VertexStep, Vertex(?12):VertexStep]
      }
    }
]
+ not converted into Neptune steps: WherePredicateStep(eq(a)),
Neptune steps:
[
    DFECleanupStep
]


Optimized Traversal
===================
Neptune steps:
[
    DFEStep(Vertex) {
      DFENode {
        DFEJoinGroupNode[ children={
          DFEPatternNode[(?1, ?3, ?4, ?5) . project ALL[?1, ?4] graphFilters=(!= defaultGraph[526] . ), {rangeCountEstimate=9223372036854775807}]
        }, {rangeCountEstimate=unknown}
        ]
      } [Vertex(?1):GraphStep@[a], Vertex(?4):VertexStep]
    } ,
    NeptuneTraverserConverterDFEStep
]
+ not converted into Neptune steps: NeptuneHasStep([name.eq(josh)]),
Neptune steps:
[
    NeptuneMemoryTrackerStep,
    NeptuneInterleavingStep {
      StepInfo[joinVars=[?7, ?1], frontierElement=Vertex(?7):HasStep, pathElements={a=(last,Vertex(?1):GraphStep@[a])}, listPathElement={}, indexTime=0ms],
      DFEStep(Vertex) {
        DFENode {
          DFEJoinGroupNode[ children={
            DFEPatternNode[(?7, ?8, ?9, ?10) . project ALL[?7, ?9] graphFilters=(!= defaultGraph[526] . ), {rangeCountEstimate=9223372036854775807}],
            DFEPatternNode[(?12, ?11, ?9, ?13) . project ALL[?9, ?12] graphFilters=(!= defaultGraph[526] . ), {rangeCountEstimate=9223372036854775807}]
          }, {rangeCountEstimate=unknown}
          ]
        } [Vertex(?9):VertexStep, Vertex(?12):VertexStep]
      }
    }
]
+ not converted into Neptune steps: WherePredicateStep(eq(a)),
Neptune steps:
[
    DFECleanupStep
]


WARNING: >> [NeptuneHasStep([name.eq(josh)]), WherePredicateStep(eq(a))] << (or one of the children for each step) is not supported natively yet

Predicates
==========
# of predicates: 8
```

See [Information in explain](#gremlin-explain-api-results "#gremlin-explain-api-results") for a description
of the DFE-specific sections in the report.

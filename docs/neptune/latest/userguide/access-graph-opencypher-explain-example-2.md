# Example of `explain` output for a relationship lookup with a limit

This query looks for relationships between two anonymous nodes with type
`route`, and returns at most 10. Again, the `explain` mode is
`details` and the output format is the default ASCII format. Here is the
`explain` output:

Here, `DFEPipelineScan` scans for edges that start from anonymous node
`?anon_node7` and end at another anonymous node `?anon_node21`, with a
relationship type saved as `?p_type1`. There is a filter for `?p_type1`
being `el://route` (where `el` stands for edge label), which
corresponds to `[p:route]` in the query string.

`DFEDrain` collects the output solution with a limit of 10, as shown in
its `Arguments` column. `DFEDrain` terminates once the limit is
reached or the all solutions are produced, whichever happens first.

```
curl -d "query=MATCH ()-[p:route]->() RETURN p LIMIT 10" -k https://localhost:8182/openCypher -d "explain=details"                                                                                              ~
Query:
MATCH ()-[p:route]->() RETURN p LIMIT 10

╔════╤════════╤════════╤═══════════════════╤════════════════════╤═════════════════════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name              │ Arguments          │ Mode                │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═══════════════════╪════════════════════╪═════════════════════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ SolutionInjection │ solutions=[{}]     │ -                   │ 0        │ 1         │ 0.00  │ 0         ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFESubquery       │ subQuery=subQuery1 │ -                   │ 0        │ 10        │ 0.00  │ 5.00      ║
╟────┼────────┼────────┼───────────────────┼────────────────────┼─────────────────────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ TermResolution    │ vars=[?p]          │ id2value_opencypher │ 10       │ 10        │ 1.00  │ 1.00      ║
╚════╧════════╧════════╧═══════════════════╧════════════════════╧═════════════════════╧══════════╧═══════════╧═══════╧═══════════╝


subQuery1
╔════╤════════╤════════╤═════════════════╤═══════════════════════════════════════════════════════════╤══════╤══════════╤═══════════╤═══════╤═══════════╗
║ ID │ Out #1 │ Out #2 │ Name            │ Arguments                                                 │ Mode │ Units In │ Units Out │ Ratio │ Time (ms) ║
╠════╪════════╪════════╪═════════════════╪═══════════════════════════════════════════════════════════╪══════╪══════════╪═══════════╪═══════╪═══════════╣
║ 0  │ 1      │ -      │ DFEPipelineScan │ pattern=Edge((?anon_node7)-[?p:?p_type1]->(?anon_node21)) │ -    │ 0        │ 1000      │ 0.00  │ 0.66      ║
║    │        │        │                 │ inlineFilters=[(?p_type1 IN [<el://route>])]              │      │          │           │       │           ║
║    │        │        │                 │ patternEstimate=26219                                     │      │          │           │       │           ║
╟────┼────────┼────────┼─────────────────┼───────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 1  │ 2      │ -      │ DFEProject      │ columns=[?p]                                              │ -    │ 1000     │ 1000      │ 1.00  │ 0.14      ║
╟────┼────────┼────────┼─────────────────┼───────────────────────────────────────────────────────────┼──────┼──────────┼───────────┼───────┼───────────╢
║ 2  │ -      │ -      │ DFEDrain        │ limit=10                                                  │ -    │ 1000     │ 0         │ 0.00  │ 0.11      ║
╚════╧════════╧════════╧═════════════════╧═══════════════════════════════════════════════════════════╧══════╧══════════╧═══════════╧═══════╧═══════════╝
```



# Graph schema and metadata
<a name="graph-schema-metadata"></a>

Neptune provides several ways to discover and inspect the structure of your graph data without scanning the entire database. Use these features to understand your graph's topology, optimize query planning, and provide schema context to applications.
+ **[Getting a quick summary report about your graph](neptune-graph-summary.md)** – Returns high-level statistics about your graph, including node and edge counts and the list of distinct labels and predicates.
+ **[Property graph schema](access-graph-pg-schema.md)** – Retrieves the complete schema of your property graph, including node labels, edge labels, property data types, and label triples that describe how node types connect through edge types. Designed for LLM query generation, graph visualization, and schema discovery.
+ **[Managing statistics for the Neptune DFE to use](neptune-dfe-statistics.md)** – Provides statistics used by the DFE query optimizer for query plan selection, such as cardinality estimates and predicate selectivity.

**Topics**
+ [Getting a quick summary report about your graph](neptune-graph-summary.md)
+ [Property graph schema](access-graph-pg-schema.md)
+ [Managing statistics for the Neptune DFE to use](neptune-dfe-statistics.md)
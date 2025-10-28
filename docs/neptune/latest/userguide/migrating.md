# Migrating an existing graph to Amazon Neptune

There are a number of tools and techniques that can help you migrate
existing graph data into Amazon Neptune from another data store.

A simple migration workflow involves the following steps:

- Export the data from its existing store into Amazon Simple Storage Service (Amazon S3).
- Clean and format it for import.
- Load it into a Neptune DB cluster using [Neptune Bulk Loader](bulk-load.md "bulk-load.md").
- Configure your Gremlin or SPARQL application to use
  the corresponding endpoint that Neptune provides.

###### Note

Your Neptune cluster must be running in a VPC that your application
can access.

There are ways to simplify and automate some of these steps, depending on
where the data is stored:

###### Topics

- [Migrating from Neo4j to Amazon Neptune](migrating-from-neo4j.md "migrating-from-neo4j.md")
- [Migrating an existing graph from an Apache TinkerPop Gremlin server to Amazon Neptune](migrating-from-tinkerpop.md "migrating-from-tinkerpop.md")
- [Migrating an existing graph from an RDF triple store to Amazon Neptune](migrating-from-rdf.md "migrating-from-rdf.md")
- [Using AWS Database Migration Service (AWS DMS) to migrate from a
  relational or NoSQL database to Amazon Neptune](migrating-using-dms.md "migrating-using-dms.md")
- [Migrating from Blazegraph to Amazon Neptune](migrating-from-blazegraph.md "migrating-from-blazegraph.md")

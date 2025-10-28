# SPARQL HTTP API

SPARQL HTTP requests are accepted at the following endpoint:
`https://`your-neptune-endpoint`:`port`/sparql`

For more information about connecting to Amazon Neptune with SPARQL, see [Accessing the Neptune graph with SPARQL](access-graph-sparql.md "access-graph-sparql.md").

For more information about the SPARQL protocol and query language, see the [SPARQL 1.1 Protocol](https://www.w3.org/TR/sparql11-protocol/#protocol "https://www.w3.org/TR/sparql11-protocol/#protocol") and the
[SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/ "https://www.w3.org/TR/sparql11-query/")
specification.

The following topics provide information about SPARQL RDF serialization
formats and how to use the SPARQL HTTP API with Neptune.

###### Contents

- [Using the HTTP REST endpoint to connect to a
  Neptune DB instance](access-graph-sparql-http-rest.md "access-graph-sparql-http-rest.md")
- [Optional HTTP trailing headers for multi-part SPARQL responses](access-graph-sparql-http-trailing-headers.md "access-graph-sparql-http-trailing-headers.md")
- [RDF media types used by SPARQL in Neptune](sparql-media-type-support.md "sparql-media-type-support.md")
  - [RDF serialization formats used by Neptune SPARQL](sparql-media-type-support.md#sparql-serialization-formats "sparql-media-type-support.md#sparql-serialization-formats")
  - [SPARQL result serialization formats used by Neptune SPARQL](sparql-media-type-support.md#sparql-serialization-formats-neptune-output "sparql-media-type-support.md#sparql-serialization-formats-neptune-output")
  - [Media-Types that Neptune can use to import RDF data](sparql-media-type-support.md#sparql-serialization-formats-input "sparql-media-type-support.md#sparql-serialization-formats-input")
  - [Media-Types that Neptune can use to export query results](sparql-media-type-support.md#sparql-serialization-formats-output "sparql-media-type-support.md#sparql-serialization-formats-output")

- [Using SPARQL UPDATE LOAD
  to import data into Neptune](sparql-api-reference-update-load.md "sparql-api-reference-update-load.md")
- [Using SPARQL UPDATE UNLOAD to delete data from Neptune](sparql-api-reference-unload.md "sparql-api-reference-unload.md")

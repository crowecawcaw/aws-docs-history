# RDF media types used by SPARQL in Neptune

Resource Description Framework (RDF) data can be serialized in many
different ways, most of which SPARQL can consume or output:

## RDF serialization formats used by Neptune SPARQL

- **RDF/XML**  –  
  XML serialization of RDF, defined in [RDF 1.1 XML Syntax](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/").
  Media type: `application/rdf+xml`.
  Typical file extension: `.rdf`.
- **N-Triples**  –  
  A line-based, plain-text format for encoding an RDF graph, defined in [RDF 1.1 N-Triples](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/").
  Media type: `application/n-triples`, `text/turtle`,
  or `text/plain`. Typical file extension: `.nt`.
- **N-Quads**  –  
  A line-based, plain-text format for encoding an RDF graph, defined in [RDF 1.1 N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/"). It is an
  extension of N-Triples. Media type: `application/n-quads`, or
  `text/x-nquads` when encoded with 7-bit US-ASCII. Typical file
  extension: `.nq`.
- **Turtle**  –  
  A textual syntax for RDF defined in [RDF 1.1 Turtle](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/") that allows an RDF graph to be completely written
  in a compact and natural text form, with abbreviations for common usage
  patterns and datatypes. Turtle provides levels of compatibility with the
  N-Triples format as well as SPARQL's triple pattern syntax. Media type:
  `text/turtle`Typical file extension: `.ttl`.
- **TriG**  –  
  A textual syntax for RDF defined in [RDF 1.1 TriG](https://www.w3.org/TR/trig/ "https://www.w3.org/TR/trig/") that allows an RDF graph to be completely written
  in a compact and natural text form, with abbreviations for common usage
  patterns and datatypes. TriG is an extension of the Turtle format. Media type:
  `application/trig`. Typical file extension: `.trig`.
- **N3 (Notation3)**  –  
  An assertion and logic language defined in [Notation3 (N3): A readable RDF
  syntax](https://www.w3.org/TeamSubmission/n3/ "https://www.w3.org/TeamSubmission/n3/"). N3 extends the RDF data model by adding formulae (literals
  which are graphs themselves), variables, logical implication, and functional
  predicates, and provides a textual syntax alternative to RDF/XML. Media type:
  `text/n3`. Typical file extension: `.n3`.
- **JSON-LD**  –  
  A data serialization and messaging format defined in [JSON-LD 1.0](https://www.w3.org/TR/json-ld/ "https://www.w3.org/TR/json-ld/").Media type:
  `application/ld+json`. Typical file extension:
  `.jsonld`.
- **TriX**  –  
  A serialization of RDF in XML, defined in [TriX:
  RDF Triples in XML](https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html "https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html"). Media type:
  `application/trix`. Typical file extension:
  `.trix`.
- **SPARQL JSON Results**  –  
  A serialization of RDF using the [SPARQL
  1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json "https://www.w3.org/TR/sparql11-results-json"). Media type:
  `application/sparql-results+json`. Typical file extension:
  `.srj`.
- **RDF4J Binary Format**  –  
  A binary format for encoding RDF data, documented in [RDF4J Binary RDF Format](https://rdf4j.org/documentation/reference/rdf4j-binary "https://rdf4j.org/documentation/reference/rdf4j-binary").
  Media type: `application/x-binary-rdf`.

## SPARQL result serialization formats used by Neptune SPARQL

- **SPARQL XML Results**  –  
  An XML format for the variable binding and boolean results formats provided
  by the SPARQL query language, defined in [SPARQL Query Results
  XML Format (Second Edition)](https://www.w3.org/TR/rdf-sparql-XMLres/ "https://www.w3.org/TR/rdf-sparql-XMLres/"). Media type:
  `application/sparql-results+xml`. Typical file extension:
  `.srx`.
- **SPARQL CSV and TSV Results**  –  
  The use of comma-separated values and tab-separated values to express SPARQL
  query results from `SELECT` queries, defined in [SPARQL 1.1 Query
  Results CSV and TSV Formats](https://www.w3.org/TR/sparql11-results-csv-tsv/ "https://www.w3.org/TR/sparql11-results-csv-tsv/"). Media type: `text/csv` for
  comma-separated values, and `text/tab-separated-values` for tab-separated
  values. Typical file extensions: `.csv` for comma-separated values,
  and `.tsv` for tab-separated values.
- **Binary Results Table**  –  
  A binary format for encoding the output of SPARQL queries.
  Media type: `application/x-binary-rdf-results-table`.
- **SPARQL JSON Results**  –  
  A serialization of RDF using the [SPARQL 1.1 Query Results
  JSON Format](https://www.w3.org/TR/sparql11-results-json/ "https://www.w3.org/TR/sparql11-results-json/"). Media type: `application/sparql-results+json`.

## Media-Types that Neptune can use to import RDF data

###### Media-types supported by the [Neptune bulk-loader](bulk-load.md "bulk-load.md")

- [N-Triples](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/")
- [N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/")
- [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/")
- [Turtle](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/")

###### Media-types that SPARQL UPDATE LOAD can import

- [N-Triples](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/")
- [N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/")
- [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/")
- [Turtle](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/")
- [TriG](https://www.w3.org/TR/trig/ "https://www.w3.org/TR/trig/")
- [N3](https://www.w3.org/TeamSubmission/n3/ "https://www.w3.org/TeamSubmission/n3/")
- [JSON-LD](https://www.w3.org/TR/json-ld/ "https://www.w3.org/TR/json-ld/")

## Media-Types that Neptune can use to export query results

To specify the output format for a SPARQL query response, send an `"Accept:
 `media-type`"` header with the query request. For example:

```
curl -H "Accept: application/nquads" ...
```

###### RDF media-types that SPARQL SELECT can output from Neptune

- [SPARQL JSON Results](https://www.w3.org/TR/sparql11-results-json "https://www.w3.org/TR/sparql11-results-json")
  (This is the default)
- [SPARQL XML Results](https://www.w3.org/TR/rdf-sparql-XMLres/ "https://www.w3.org/TR/rdf-sparql-XMLres/")
- **Binary Results Table**
  (media type: `application/x-binary-rdf-results-table`)
- [Comma-Separated Values (CSV)](https://www.w3.org/TR/sparql11-results-csv-tsv/ "https://www.w3.org/TR/sparql11-results-csv-tsv/")
- [Tab-Separated Values (TSV)](https://www.w3.org/TR/sparql11-results-csv-tsv/ "https://www.w3.org/TR/sparql11-results-csv-tsv/")

###### RDF media-types that SPARQL ASK can output from Neptune

- [SPARQL JSON Results](https://www.w3.org/TR/sparql11-results-json "https://www.w3.org/TR/sparql11-results-json")
  (This is the default)
- [SPARQL XML Results](https://www.w3.org/TR/rdf-sparql-XMLres/ "https://www.w3.org/TR/rdf-sparql-XMLres/")
- **Boolean**
  (media type: `text/boolean`, meaning "true" or "false")

###### RDF media-types that SPARQL CONSTRUCT can output from Neptune

- [N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/") (This is the default)
- [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/")
- [JSON-LD](https://www.w3.org/TR/json-ld/ "https://www.w3.org/TR/json-ld/")
- [N-Triples](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/")
- [Turtle](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/")
- [N3](https://www.w3.org/TeamSubmission/n3/ "https://www.w3.org/TeamSubmission/n3/")
- [TriX](https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html "https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html")
- [TriG](https://www.w3.org/TR/trig/ "https://www.w3.org/TR/trig/")
- [SPARQL JSON Results](https://www.w3.org/TR/sparql11-results-json "https://www.w3.org/TR/sparql11-results-json")
- [RDF4J Binary RDF Format](https://rdf4j.org/documentation/reference/rdf4j-binary "https://rdf4j.org/documentation/reference/rdf4j-binary")

###### RDF media-types that SPARQL DESCRIBE can output from Neptune

- [N-Quads](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/") (This is the default)
- [RDF/XML](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/")
- [JSON-LD](https://www.w3.org/TR/json-ld/ "https://www.w3.org/TR/json-ld/")
- [N-Triples](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/")
- [Turtle](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/")
- [N3](https://www.w3.org/TeamSubmission/n3/ "https://www.w3.org/TeamSubmission/n3/")
- [TriX](https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html "https://www.hpl.hp.com/techreports/2004/HPL-2004-56.html")
- [TriG](https://www.w3.org/TR/trig/ "https://www.w3.org/TR/trig/")
- [SPARQL JSON Results](https://www.w3.org/TR/sparql11-results-json "https://www.w3.org/TR/sparql11-results-json")
- [RDF4J Binary RDF Format](https://rdf4j.org/documentation/reference/rdf4j-binary "https://rdf4j.org/documentation/reference/rdf4j-binary")

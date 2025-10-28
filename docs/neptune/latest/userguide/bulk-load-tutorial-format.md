# Load Data Formats

The Amazon Neptune `Load` API supports loading data in a variety
of formats.

**Property-graph load formats**

Data loaded in one of the following property-graph formats can
then be queried using both Gremlin and openCypher:

- [Gremlin load data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md") (`csv`): a
  comma-separated values (CSV) format.
- [openCypher
  data load format](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md") (`opencypher`): a comma-separated values
  (CSV) format.
  **RDF load formats**

To load Resource Description Framework (RDF) data that you query using SPARQL,
you can use one of the following standard formats as specified by the World Wide
Web Consortium (W3C):

- N-Triples (`ntriples`) from the specification at [https://www.w3.org/TR/n-triples/](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/").
- N-Quads (`nquads`) from the specification at [https://www.w3.org/TR/n-quads/](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/").
- RDF/XML (`rdfxml`) from the specification at [https://www.w3.org/TR/rdf-syntax-grammar/](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/").
- Turtle (`turtle`) from the specification at [https://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/").
  **Load data must use UTF-8 encoding**

###### Important

All load-data files must be encoded in UTF-8 form. If a file is
not UTF-8 encoded, Neptune tries to load it as UTF-8 anyway.

For N-Quads and N-triples data that includes Unicode characters,
`\u`xxxxx`` escape sequences are supported. However,
Neptune does not support normalization. If a value is present that requires
normalization, it will not match byte-to-byte during querying. For more information about
normalization, see the [Normalization](https://unicode.org/faq/normalization.html "https://unicode.org/faq/normalization.html")
page on [Unicode.org](https://unicode.org "https://unicode.org").

If your data is not in a supported format, you must convert it before
you load it.

A tool for converting GraphML to the Neptune CSV format is available in the [GraphML2CSV project](https://github.com/awslabs/amazon-neptune-tools/blob/master/graphml2csv/README.md "https://github.com/awslabs/amazon-neptune-tools/blob/master/graphml2csv/README.md") on [GitHub](https://github.com/ "https://github.com/").

## Compression support for load-data files

Neptune supports compression of individual files in `gzip`
or `bzip2` format.

The compressed file must have a `.gz` or `.bz2`
extension, and must be a single text file encoded in UTF-8 format. You can
load multiple files, but each one must be a separate `.gz`,
`.bz2`, or uncompressed text file. Archive files with extensions
such as `.tar`, `.tar.gz`, and `.tgz` are
not supported.

The following sections describe the formats in more detail.

###### Topics

- [Gremlin load data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md")
- [Load format for openCypher data](bulk-load-tutorial-format-opencypher.md "bulk-load-tutorial-format-opencypher.md")
- [RDF load data formats](bulk-load-tutorial-format-rdf.md "bulk-load-tutorial-format-rdf.md")

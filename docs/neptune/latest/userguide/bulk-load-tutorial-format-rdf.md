# RDF load data formats

To load Resource Description Framework (RDF) data, you can use one of the following
standard formats as specified by the World Wide Web Consortium (W3C):

- N-Triples (`ntriples`) from the specification at [https://www.w3.org/TR/n-triples/](https://www.w3.org/TR/n-triples/ "https://www.w3.org/TR/n-triples/")
- N-Quads (`nquads`) from the specification at [https://www.w3.org/TR/n-quads/](https://www.w3.org/TR/n-quads/ "https://www.w3.org/TR/n-quads/")
- RDF/XML (`rdfxml`) from the specification at [https://www.w3.org/TR/rdf-syntax-grammar/](https://www.w3.org/TR/rdf-syntax-grammar/ "https://www.w3.org/TR/rdf-syntax-grammar/")
- Turtle (`turtle`) from the specification at [https://www.w3.org/TR/turtle/](https://www.w3.org/TR/turtle/ "https://www.w3.org/TR/turtle/")

###### Important

All files must be encoded in UTF-8 format.

For N-Quads and N-triples data that includes Unicode characters,
`\u`xxxxx`` escape sequences are supported. However,
Neptune does not support normalization. If a value is present that requires
normalization, it will not match byte-to-byte during querying. For more information about
normalization, see the [Normalization](https://unicode.org/faq/normalization.html "https://unicode.org/faq/normalization.html")
page on [Unicode.org](https://unicode.org "https://unicode.org").

###### Next Steps

Now that you know more about the loading formats, see [Example: Loading Data into a Neptune DB Instance](bulk-load-data.md "bulk-load-data.md").

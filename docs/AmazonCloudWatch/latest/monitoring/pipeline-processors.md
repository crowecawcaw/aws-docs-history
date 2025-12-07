# CloudWatch pipelines processors

CloudWatch pipelines processors transform, parse, and enrich log data as it flows through the pipeline. A
pipeline can have up to 20 processors that are applied sequentially in the order they are
defined.

| Processor categories | Category                                                                                                                  | Description |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------- | ----------- |
| Parsers              | Convert raw log data into structured formats, such as Open Cybersecurity<br>Schema Framework (OCSF), CSV, JSON, and so on |
| Transformers         | Modify log data structure; add, copy, move, or delete fields                                                              |
| String Processors    | Manipulate string values; case conversion, trimming, substitution                                                         |

###### Topics

- [Parser processors](parser-processors.md "parser-processors.md")
- [Transformation processors](transformation-processors.md "transformation-processors.md")
- [String manipulation processors](string-processors.md "string-processors.md")
- [Common processor use cases](processor-examples.md "processor-examples.md")
- [Processor compatibility and restrictions](processor-compatibility.md "processor-compatibility.md")

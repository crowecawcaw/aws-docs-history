# CloudWatch pipelines processors

CloudWatch pipelines processors transform, parse, and enrich log data as it flows through the pipeline.
Log pipelines support up to 20 processors that are applied sequentially in the order they
are defined. Metrics pipelines support up to 20 processors, applied
sequentially in the order you define them. For metrics pipeline processors, see
[Metrics pipeline processors](metrics-pipeline-processors.md "metrics-pipeline-processors.md").

###### Transformation metadata

When a pipeline processes log events, CloudWatch pipelines automatically adds transformation metadata
to each processed log entry. This metadata indicates that the log has been transformed,
making it easy to distinguish between original and processed data. If you enable the
**Keep original log** option during pipeline creation, you can compare
the original log with the transformed version at any time.

The following table describes the processor categories.

| Category           | Description                                                                                                               |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------- |
| Parsers            | Convert raw log data into structured formats, such as Open Cybersecurity<br>Schema Framework (OCSF), CSV, JSON, and so on |
| Transformers       | Modify log data structure; add, copy, move, or delete fields                                                              |
| String Processors  | Manipulate string values; case conversion, trimming, substitution                                                         |
| Metrics processors | Add, delete, rename attributes and metrics on OTel metric<br>datapoints                                                   |

###### Topics

- [Parser processors](parser-processors.md "parser-processors.md")
- [Transformation processors](transformation-processors.md "transformation-processors.md")
- [String manipulation processors](string-processors.md "string-processors.md")
- [Filter processors](filter-processors.md "filter-processors.md")
- [Common processor use cases](processor-examples.md "processor-examples.md")
- [Processor compatibility and restrictions](processor-compatibility.md "processor-compatibility.md")
- [Metrics pipeline processors](metrics-pipeline-processors.md "metrics-pipeline-processors.md")

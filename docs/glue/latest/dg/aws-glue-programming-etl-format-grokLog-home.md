# Using the grokLog format in AWS Glue

AWS Glue retrieves data from sources and writes data to targets stored and transported in various data formats. If your data is
stored or transported in a loosely structured plaintext format, this document introduces you available features for using your
data in AWS Glue through Grok patterns.

AWS Glue supports using Grok patterns. Grok patterns are similar to regular expression capture groups. They
recognize patterns of character sequences in a plaintext file and give them a type and purpose. In AWS Glue, their primary purpose
is to read logs. For an introduction to the Grok by the authors, see [Logstash
Reference: Grok filter plugin](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html "https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html").

| Read      | Write          | Streaming read | Group small files | Job bookmarks |
| --------- | -------------- | -------------- | ----------------- | ------------- |
| Supported | Not Applicable | Supported      | Supported         | Unsupported   |

## grokLog configuration reference

You can use the following `format_options` values with
`format="grokLog"`:

- `logFormat` — Specifies the Grok pattern that matches the log's
  format.
- `customPatterns` — Specifies additional Grok patterns used here.
- `MISSING` — Specifies the signal to use in identifying missing values. The
  default is `'-'`.
- `LineCount` — Specifies the number of lines in each log record. The default
  is `'1'`, and currently only single-line records are supported.
- `StrictMode` — A Boolean value that specifies whether strict mode is
  turned on. In strict mode, the reader doesn't do automatic type conversion or recovery. The
  default value is `"false"`.

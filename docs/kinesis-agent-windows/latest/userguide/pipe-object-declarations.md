# Pipe Declarations

Use _pipe declarations_ to connect a source (see [Source Declarations](source-object-declarations.md "source-object-declarations.md")) to a sink (see
[Sink Declarations](sink-object-declarations.md "sink-object-declarations.md")) in
Amazon Kinesis Agent for Microsoft Windows. A pipe declaration is expressed as a JSON object. After Kinesis Agent for Windows starts, the logs, events,
or metrics are gathered from the source for a given pipe. They are then streamed to various AWS services using the sink that is associated with that pipe.

The following is an example pipe declaration:

```
{
   "Id": "MyAppLogToCloudWatchLogs",
   "SourceRef": "MyAppLog",
   "SinkRef": "MyCloudWatchLogsSink"
}
```

###### Topics

- [Configuring Pipes](#kinesis-agent-pipe-configuration "#kinesis-agent-pipe-configuration")
- [Configuring Kinesis Agent for Windows Metric Pipes](#kinesis-agent-metric-pipe-configuration "#kinesis-agent-metric-pipe-configuration")

## Configuring Pipes

All pipe declarations can contain the following key-value pairs:

`Id`

Specifies the name of the pipe (required). It must be unique within the configuration
file.

`Type`

Specifies the type of transformation (if any) that is applied by the pipe as log data is
transferred from the source to the sink. The only supported value is
`RegexFilterPipe`. This value enables regular expression filtering of the
underlying textual representation of the log record. Using filtering can reduce transmission
and storage costs by sending only relevant log records downstream to the data pipeline. This
key-value pair is optional. The default value is to provide no transformation.

`FilterPattern`

Specifies the regular expression for `RegexFilterPipe` pipelines that are used
to filter log records gathered by the source before being transferred to the sink. Log records
are transferred by `RegexFilterPipe` type pipes when the regular expression matches
the underlying textual representation of the record. Structured log records that are
generated, for example, when using the `ExtractionPattern` key-value pair in a
`DirectorySource` declaration, can still be filtered using the
`RegexFilterPipe` mechanism. This is because this mechanism operates against the
original textual representation before parsing. This key-value pair is optional, but it must
be provided if the pipe specifies the `RegexFilterPipe` type.

The following is an example `RegexFilterPipe` pipe declaration:

```
{
	"Id": "MyAppLog2ToFirehose",
	"Type": "RegexFilterPipe",
	"SourceRef": "MyAppLog2",
	"SinkRef": "MyFirehose",
	"FilterPattern": "^(10|11),.*",
	"IgnoreCase": false,
	"Negate": false
}
```

`SourceRef`

Specifies the name (the value of the `Id` key-value pair) of the source
declaration that defines the source that is collecting log, event, and metric data for the
pipe (required).

`SinkRef`

Specifies the name (the value of the `Id` key-value pair) of the sink
declaration that defines the sink that is receiving the log, event, and metric data for the
pipe (required).

`IgnoreCase`
Optional. Accepts values of `true` or `false`. When set to `true`, the Regex will match records in a case-insensitive manner.

`Negate`
Optional. Accepts values of `true` or `false`. When set to `true`, the pipe will forward the records that _do not_ match the regular expression.

For an example of a complete configuration file that uses the `RegexFilterPipe`
pipe type, see [Using Pipes](configuring-kaw-examples.md#configuring-kaw-examples-pipes "configuring-kaw-examples.md#configuring-kaw-examples-pipes").

## Configuring Kinesis Agent for Windows Metric Pipes

There is a built-in metric source named `_KinesisTapMetricsSource` that produces
metrics about Kinesis Agent for Windows. If there is a `CloudWatch` sink declaration with an
`Id` of `MyCloudWatchSink`, the following example pipeline declaration transfers
Kinesis Agent for Windows-generated metrics to that sink:

```
{
   "Id": "KinesisAgentMetricsToCloudWatch",
   "SourceRef": "_KinesisTapMetricsSource",
   "SinkRef": "MyCloudWatchSink"
}
```

For more information about the Kinesis Agent for Windows built-in metrics source, see [Kinesis Agent for Windows Built-In Metrics Source](source-object-declarations.md#kinesis-agent-builin-metrics-source "source-object-declarations.md#kinesis-agent-builin-metrics-source").

If the configuration file also streams Windows performance counter metrics, we recommend
that you use a separate pipe and sink rather than using the same sink for both Kinesis Agent for Windows metrics and
Windows performance counter metrics.

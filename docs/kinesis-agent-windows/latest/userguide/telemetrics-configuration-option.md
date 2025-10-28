# Configuring Telemetrics

To enable better support, by default, Amazon Kinesis Agent for Microsoft Windows collects statistics about the operation of
the agent and sends them to AWS. This information contains no personally identifiable
information. It doesn't include any data that you gather or stream to AWS services. We collect
approximately 1–2 KB of this metric data every 60 minutes.

You can opt out of the collection and transmission of these statistics. To do this, add the
following key-value pair to the `appsettings.json` configuration file at the
same level as sources, sinks, and pipes:

```

"Telemetrics":
    { "off": "true" }

```

For example, the following configuration file configures a source, sink, and pipe, and also
disables telemetrics:

```
{
  "Sources": [
    {
      "Id": "ApplicationLogSource",
      "SourceType": "DirectorySource",
      "Directory": "C:\\LogSource\\",
      "FileNameFilter": "*.log",
      "RecordParser": "SingleLine"
    }
  ],
  "Sinks": [
    {
       "Id": "ApplicationLogKinesisFirehoseSink",
       "SinkType": "KinesisFirehose",
       "StreamName": "ApplicationLogFirehoseDeliveryStream",
       "Region": "us-east-1"
    }
    ],
  "Pipes": [
    {
      "Id": "ApplicationLogSourceToApplicationLogKinesisFirehoseSink",
      "SourceRef": "ApplicationLogSource",
      "SinkRef": "ApplicationLogKinesisFirehoseSink"
    }
  ],
  "Telemetrics":
    {
      "off": "true"
    }
}
```

We collect the following metrics when telemetry is enabled:

`ClientId`
The automatically assigned unique ID when the software is installed.

`ClientTimestamp`
The date and time the telemetry is collected.

`OSDescription`
A description of the operating system.

`DotnetFramework`
The current dotnet framework version.

`MemoryUsage`
The amount of memory consumed by Kinesis Agent for Windows(MB).

`CPUUsage`
The amount of Kinesis Agent for Windows CPU usage percentage in decimal. For example, 0.01 means 1%.

`InstanceId`
The Amazon EC2 instance ID if Kinesis Agent for Windows is running on an Amazon EC2 instance.

`InstanceType (string)`
The Amazon EC2 instance type if Kinesis Agent for Windows is running on an Amazon EC2 instance.

In addition, we collect the metrics listed in [List of Kinesis Agent for Windows Metrics](source-object-declarations.md#kinesis-agent-metric-list "source-object-declarations.md#kinesis-agent-metric-list").

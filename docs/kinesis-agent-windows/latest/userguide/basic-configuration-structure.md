# Basic Configuration Structure

The basic structure of the Amazon Kinesis Agent for Microsoft Windows configuration file is a JSON document with the
following template:

```
{
     "Sources": [ ],
     "Sinks": [ ],
     "Pipes": [ ]
}
```

- The value of `Sources` is one or more [Source Declarations](source-object-declarations.md "source-object-declarations.md").
- The value of `Sinks` is one or more [Sink Declarations](sink-object-declarations.md "sink-object-declarations.md").
- The value of `Pipes` is one or more [Pipe Declarations](pipe-object-declarations.md "pipe-object-declarations.md").
  For more information about the Kinesis Agent for Windows source, pipe, and sink concepts, see [Amazon Kinesis Agent for Microsoft Windows Concepts](kinesis-agent-windows-concepts.md "kinesis-agent-windows-concepts.md").

The following example is a complete `appsettings.json` configuration
file that configures Kinesis Agent for Windows to stream Windows application log events to Firehose.

```
{
  "Sources": [
    {
      "LogName": "Application",
      "Id": "ApplicationLog",
      "SourceType": "WindowsEventLogSource"
    }
  ],
  "Sinks": [
    {
      "StreamName": "ApplicationLogFirehoseStream",
      "Region": "us-west-2",
      "Id": "MyKinesisFirehoseSink",
      "SinkType": "KinesisFirehose"
    }
  ],
  "Pipes": [
    {
      "Id": "ApplicationLogTotestKinesisFirehoseSink",
      "SourceRef": "ApplicationLog",
      "SinkRef": "MyKinesisFirehoseSink"
    }
  ]
}
```

For information about each kind of declaration, see the following sections:

- [Source Declarations](source-object-declarations.md "source-object-declarations.md")
- [Sink Declarations](sink-object-declarations.md "sink-object-declarations.md")
- [Pipe Declarations](pipe-object-declarations.md "pipe-object-declarations.md")

## Configuration Case Sensitivity

JSON-formatted files are typically case sensitive, and you should assume that all the
keys and values in Kinesis Agent for Windows configuration files are also case sensitive. Some keys and values
in the `appsettings.json` configuration file are not case sensitive; for
example:

- The value of the `Format` key-value pair for sinks. For more information,
  see [Sink Declarations](sink-object-declarations.md "sink-object-declarations.md").
- The value of the `SourceType` key-value pair for sources, the
  `SinkType` key-value pair for sinks, and the `Type` key-value
  pair for pipes and plugins.
- The value of `RecordParser` key-value pair for the
  `DirectorySource` source. For more information, see [DirectorySource Configuration](source-object-declarations.md#directory-source-configuration "source-object-declarations.md#directory-source-configuration").
- The value of the `InitialPosition` key-value pair for sources. For more
  information, see [Bookmark Configuration](source-object-declarations.md#advanced-source-configuration "source-object-declarations.md#advanced-source-configuration").
- Prefixes for variable substitutions. For more information, see [Configuring Sink Variable
  Substitutions](sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution "sink-object-declarations.md#configuring-kinesis-agent-windows-sink-variable-substitution").

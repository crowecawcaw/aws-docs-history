

# Use Apache Beam with Managed Service for Apache Flink applications
<a name="how-creating-apps-beam"></a>

You can use the [Apache Beam](https://beam.apache.org/) framework with your Managed Service for Apache Flink application to process streaming data. Managed Service for Apache Flink applications that use Apache Beam use [Apache Flink runner](https://beam.apache.org/documentation/runners/flink/) to execute Beam pipelines.

For a tutorial about how to use Apache Beam in a Managed Service for Apache Flink application, see [Use CloudFormation](examples-beam.md).

**Topics**
+ [Limitations of Apache Flink runner with Managed Service for Apache Flink](#how-creating-apps-beam-using)
+ [Apache Beam capabilities with Managed Service for Apache Flink](#how-creating-apps-beam-capabilities)
+ [Create an application using Apache Beam](examples-beam.md)

## Limitations of Apache Flink runner with Managed Service for Apache Flink
<a name="how-creating-apps-beam-using"></a>

Note the following about using the Apache Flink runner with Managed Service for Apache Flink:
+ Apache Beam metrics are not viewable in the Managed Service for Apache Flink console.
+ **Apache Beam is only supported with Managed Service for Apache Flink applications that use Apache Flink version 1.8 and above. Apache Beam is not supported with Managed Service for Apache Flink applications that use Apache Flink version 1.6.**

## Apache Beam capabilities with Managed Service for Apache Flink
<a name="how-creating-apps-beam-capabilities"></a>

Managed Service for Apache Flink supports the same Apache Beam capabilties as the Apache Flink runner. For information about what features are supported with the Apache Flink runner, see the [Beam Compatibility Matrix](https://beam.apache.org/documentation/runners/capability-matrix/). 

We recommend that you test your Apache Flink application in the Managed Service for Apache Flink service to verify that we support all the features that your application needs.
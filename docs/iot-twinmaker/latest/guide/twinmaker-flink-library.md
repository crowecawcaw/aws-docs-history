# Using the AWS IoT TwinMaker Flink library

AWS IoT TwinMaker provides a Flink library that you can use to read and write data to external data stores used in your digital twins.

You use the AWS IoT TwinMaker Flink library by installing it as a custom connector in Managed Service for Apache Flink and performing Flink SQL queries in a
Zeppelin notebook in Managed Service for Apache Flink. The notebook can be promoted to a continuously running stream processing application.
The library leverages AWS IoT TwinMaker components to retrieve data from your workspace.

The AWS IoT TwinMaker Flink library requires the following.

###### Prerequisites

1. A fully populated workspace with scenes and components. Use the built-in component types for
   data from AWS services (AWS IoT SiteWise and Kinesis Video Streams). Create custom component types for
   data from third-party sources. For more information, see [Using and creating component types](twinmaker-component-types.md "twinmaker-component-types.md").
2. An understanding of Studio notebooks with Managed Service for Apache Flink for Apache Flink. These notebooks are powered by
   [Apache Zeppelin](https://zeppelin.apache.org "https://zeppelin.apache.org") and use the [Apache Flink](https://flink.apache.org "https://flink.apache.org") framework.
   For more information, see [Using a Studio notebook with Managed Service for Apache Flink for Apache Flink](../../../kinesisanalytics/latest/java/how-notebook.md "../../../kinesisanalytics/latest/java/how-notebook.md").
   For instructions on using the library, see the [AWS IoT TwinMaker Flink library user guide](https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/insights/iot-twinmaker-flink-library-guide.md "https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/insights/iot-twinmaker-flink-library-guide.md").

For instructions on setting up AWS IoT TwinMaker with the quick start in [AWS IoT TwinMaker
samples](https://github.com/aws-samples/aws-iot-twinmaker-samples "https://github.com/aws-samples/aws-iot-twinmaker-samples"), see [README
file for the sample insights application](https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/insights/README.md "https://github.com/aws-samples/aws-iot-twinmaker-samples/blob/main/src/modules/insights/README.md").

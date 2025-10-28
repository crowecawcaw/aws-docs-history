# Schedule video recording and storage with Amazon Kinesis Video Streams Edge Agent

Amazon Kinesis Video Streams offers an efficient, cost-effective way to connect to IP cameras on customer
premises. With the Amazon Kinesis Video Streams Edge Agent, you can locally record and store video from the cameras
and stream videos to the cloud on a customer-defined schedule for long-term storage,
playback, and analytical processing.

###### Note

To access the Amazon Kinesis Video Streams Edge Agent, complete this [brief
form](https://pages.awscloud.com/GLOBAL-launch-DL-KVS-Edge-2023-learn.html "https://pages.awscloud.com/GLOBAL-launch-DL-KVS-Edge-2023-learn.html").

You can download the Amazon Kinesis Video Streams Edge Agent and deploy it at your on-premises edge compute
devices. You can also easily deploy them in Docker containers running on Amazon EC2 instances.
After deployment, you can use the Amazon Kinesis Video Streams API to update video recording and cloud
uploading configurations. The feature works with any IP camera that can stream over RTSP
protocol. It doesn't require any additional firmware deployment to the cameras.

We offer the following installations for the Amazon Kinesis Video Streams Edge Agent:

- **As an AWS IoT Greengrass V2 component:** You can install the
  Amazon Kinesis Video Streams Edge Agent as an AWS IoT Greengrass component on any AWS IoT Greengrass certified device. To learn more
  about AWS IoT Greengrass, see the [AWS IoT Greengrass Version 2 Developer Guide](../../../greengrass/v2/developerguide.md "../../../greengrass/v2/developerguide.md").
- **On AWS Snowball Edge:** You can run the
  Amazon Kinesis Video Streams Edge Agent on Snowball Edge devices. To learn more, see the [AWS Snowball Edge Edge Developer Guide](../../../snowball/latest/developer-guide.md "../../../snowball/latest/developer-guide.md").
- **On a native AWS IoT deployment:** You can install the
  Amazon Kinesis Video Streams Edge Agent natively on any compute instance. Edge SDK uses [AWS IoT Core](../../../iot/latest/developerguide/iot-gs.md "../../../iot/latest/developerguide/iot-gs.md") for managing edge through the [Amazon Kinesis Video Streams](API_Operations_Amazon_Kinesis_Video_Streams.md "API_Operations_Amazon_Kinesis_Video_Streams.md").
  To get started with Amazon Kinesis Video Streams Edge Agent, continue with the appropriate procedures
  below.

###### Topics

- [Amazon Kinesis Video Streams Edge Agent API operations](#edge-apis "#edge-apis")
- [Monitoring Amazon Kinesis Video Streams Edge Agent](#edge-monitoring "#edge-monitoring")
- [Deploy in non-AWS IoT Greengrass mode](gs-edge-outside.md "gs-edge-outside.md")
- [Deploy the Amazon Kinesis Video Streams Edge Agent to AWS IoT Greengrass](gs-edge-gg.md "gs-edge-gg.md")
- [Amazon Kinesis Video Streams Edge Agent FAQ](edge-faq.md "edge-faq.md")

## Amazon Kinesis Video Streams Edge Agent API operations

Use the following API operations to configure the Amazon Kinesis Video Streams Edge Agent:

- [StartEdgeConfigurationUpdate](API_StartEdgeConfigurationUpdate.md "API_StartEdgeConfigurationUpdate.md")
- [DescribeEdgeConfiguration](API_DescribeEdgeConfiguration.md "API_DescribeEdgeConfiguration.md")
- [DeleteEdgeConfiguration](API_DeleteEdgeConfiguration.md "API_DeleteEdgeConfiguration.md")
- [ListEdgeAgentConfigurations](API_ListEdgeAgentConfigurations.md "API_ListEdgeAgentConfigurations.md")

## Monitoring Amazon Kinesis Video Streams Edge Agent

To monitor your Amazon Kinesis Video Streams Edge Agent, see [Monitor the Amazon Kinesis Video Streams Edge Agent with
CloudWatch](monitoring-edge-cloudwatch.md "monitoring-edge-cloudwatch.md").

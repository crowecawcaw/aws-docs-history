# Create custom plugins

A plugin is an AWS resource that contains the code that defines your connector logic.
You upload a JAR file (or a ZIP file that contains one or more JAR files) to an S3 bucket,
and specify the location of the bucket when you create the plugin. When you create a
connector, you specify the plugin that you want MSK Connect to use for it. The relationship
of plugins to connectors is one-to-many: You can create one or more connectors from the same
plugin.

For information on how to develop the code for a connector, see the [Connector Development
Guide](https://kafka.apache.org/documentation/#connect_development "https://kafka.apache.org/documentation/#connect_development")in the Apache Kafka documentation.

###### Creating a custom plugin using the AWS Management Console

1. Open the Amazon MSK console at [https://console.aws.amazon.com/msk/](https://console.aws.amazon.com/msk/ "https://console.aws.amazon.com/msk/").
2. In the left pane, under **MSK Connect**, choose **Custom
   plugins**.
3. Choose **Create custom plugin**.
4. Choose **Browse S3**.
5. In the list of S3 buckets, choose the bucket that has the JAR or ZIP file for the
   plugin.
6. In the list of object, select the box to the left of the JAR or ZIP file for the
   plugin, then choose **Choose**.
7. Choose **Create custom plugin**.
   To use the MSK Connect API to create a custom plugin, see [CreateCustomPlugin](../../../MSKC/latest/mskc/API_CreateCustomPlugin.md "../../../MSKC/latest/mskc/API_CreateCustomPlugin.md").

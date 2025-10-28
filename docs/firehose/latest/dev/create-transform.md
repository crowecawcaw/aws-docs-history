# (Optional) Configure record transformation and format

conversion

Configure Amazon Data Firehose to transform and convert your record data.

###### In the **Transform source records with AWS Lambda** section,

provide values for the following field.

1. **Data transformation**

To create a Firehose stream that doesn't transform incoming data, do not
check the **Enable data transformation** checkbox.

To specify a Lambda function for Firehose to invoke and use to transform
incoming data before delivering it, check the **Enable data
transformation** checkbox. You can configure a new Lambda
function using one of the Lambda blueprints or choose an existing Lambda
function. Your Lambda function must contain the status model that is
required by Firehose. For more information, see [Transform source data in Amazon Data Firehose](data-transformation.md "data-transformation.md"). 2. In the **Convert record format** section, provide values for the
following field:

**Record format conversion**

To create a Firehose stream that doesn't convert the format of the incoming
data records, choose **Disabled**.

To convert the format of the incoming records, choose
**Enabled**, then specify the output format you
want. You need to specify an AWS Glue table that holds the schema that you
want Firehose to use to convert your record format. For more information,
see [Convert input data format in Amazon Data Firehose](record-format-conversion.md "record-format-conversion.md").

For an example of how to set up record format conversion with AWS CloudFormation,
see [AWS::KinesisFirehose::DeliveryStream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples").

###### In the **Source settings** section, provide the following

fields.

1. Under **Transform records**, choose one of the following:
   1. If your destination is Amazon S3 or Splunk, in the **Decompress source records Amazon CloudWatch Logs** section, choose **Turn on decompression**.
   2. In the **Transform source records with AWS Lambda** section,
      provide values for the following field:

   **Data transformation**

   To create a Firehose stream that doesn't transform incoming data, do not
   check the **Enable data transformation** checkbox.

   To specify a Lambda function for Amazon Data Firehose to invoke and use to transform
   incoming data before delivering it, check the **Enable data
   transformation** checkbox. You can configure a new Lambda
   function using one of the Lambda blueprints or choose an existing Lambda
   function. Your Lambda function must contain the status model that is
   required by Amazon Data Firehose. For more information, see [Transform source data in Amazon Data Firehose](data-transformation.md "data-transformation.md").

2. In the **Convert record format** section, provide values for the
   following field:

**Record format conversion**

To create a Firehose stream that doesn't convert the format of the incoming
data records, choose **Disabled**.

To convert the format of the incoming records, choose
**Enabled**, then specify the output format you
want. You need to specify an AWS Glue table that holds the schema that you
want Amazon Data Firehose to use to convert your record format. For more information,
see [Convert input data format in Amazon Data Firehose](record-format-conversion.md "record-format-conversion.md").

For an example of how to set up record format conversion with AWS CloudFormation,
see [AWS::KinesisFirehose::DeliveryStream](../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-kinesisfirehose-deliverystream.md#aws-resource-kinesisfirehose-deliverystream--examples").

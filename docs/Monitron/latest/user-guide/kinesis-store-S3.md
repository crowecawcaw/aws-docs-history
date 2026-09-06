

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Storing exported data in Amazon S3
<a name="kinesis-store-S3"></a>

**Topics**
+ [Using a predefined CloudFormation template](#kinesis-cloudfront-makestack)
+ [Configuring Kinesis manually in the console](#kinesis-configure-console)

## Using a predefined CloudFormation template
<a name="kinesis-cloudfront-makestack"></a>

Amazon Monitron provides a predefined AWS CloudFormation template to help quickly set up the Firehose to deliver data from a Kinesis data stream to the Amazon S3 bucket. This template enables dynamic partitioning and the Amazon S3 objects delivered will use the following key format recommended by Amazon Monitron: `/project={projectName}/site={siteName}/time={yyyy-mm-dd 00:00:00}/{filename}`

1. Sign into your AWS account.

1. Open a new browser tab with the following URL:

   ```
   https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3.us-east-1.amazonaws.com/monitron-cloudformation-templates-us-east-1/monitron_kinesis_data_export.yaml&stackName=monitron-kinesis-live-data-export
   ```

1. On the CloudFormation page that opens, in the upper right corner, select the region in which you are using Amazon Monitron.

1. By default, the template will create a new Kinesis data stream and S3 bucket along with other resources needed to deliver data to Amazon S3. You can change the parameters to use existing resources.

1. Check the box that says *I acknowledge that AWS CloudFormation might create IAM resources.*

1. Choose **Create stack**.

1. On the next page, choose the refresh icon as often as you like until the status of the stack is CREATE\_COMPLETE.

## Configuring Kinesis manually in the console
<a name="kinesis-configure-console"></a>

1. Sign in to the AWS Management Console and open the Kinesis console at https://console.aws.amazon.com/kinesis.

1. Choose **Delivery streams** in the navigation pane.

1. Choose **Create delivery stream**.

1. For Source, select **Amazon Kinesis Data Streams**.

1. For Destination, select **Amazon S3**.

1. Under **Source settings, Kinesis data stream**, enter the ARN of your Kinesis data stream.

1. Under **delivery stream name**, enter the name of your Kinesis data stream.

1. Under **Desination settings**, choose an Amazon S3 bucket or enter a bucket URI.

1. (optional) Enable dynamic partitioning using inline parsing for JSON. This option is appropriate if you want to partition streaming measurement data based on source information and timestamp. For example:
   + Choose **Enabled** for **Dynamic partitioning**.
   + Choose **Enabled** for **New line delimiter**.
   + Choose **Enabled** for **Inline parsing for JSON**.
   + Under **Dynamic partitioning keys**, add:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3.html)

1. Choose **Apply dynamic partitioning keys** and confirm the generated Amazon S3 bucket prefix is `!{partitionKeyFromQuery:project}/!{partitionKeyFromQuery:site}/!{partitionKeyFromQuery:time}/`.

1. In Amazon S3, objects will use the following key format: `/project={projectName}/site={siteName}/time={yyyy-mm-dd 00:00:00}/{filename}`.

1. Choose **Create delivery stream**.

1. (optional) Use a more granular path.

   If you chose a dynamic partition, use the preceeding Amazon S3 key format if you plan to use AWS Glue and Athena to query the data. You can also choose a finer key format, but the Amazon Athena query will not be efficient. Here is an example of setting up a finer Amazon S3 key path.

   Under **Dynamic partitioning keys**, add:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/Monitron/latest/user-guide/kinesis-store-S3.html)

   In Amazon S3, objects will use the following key format: ` /project={projectName}/site={siteName}/asset={assetName}/position={positionName}/sensor={sensorId}/date={yyyy-mm-dd}/time={HH:MM:SS}/{filename}`
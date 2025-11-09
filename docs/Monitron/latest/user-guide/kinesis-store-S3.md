Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Storing exported data in Amazon S3

###### Topics

- [Using a predefined CloudFormation
  template](#kinesis-cloudfront-makestack "#kinesis-cloudfront-makestack")
- [Configuring Kinesis manually in the
  console](#kinesis-configure-console "#kinesis-configure-console")

## Using a predefined CloudFormation

template

Amazon Monitron provides a predefined AWS CloudFormation template to help quickly set up the
Firehose to deliver data from a Kinesis data stream to the Amazon S3 bucket. This
template enables dynamic partitioning and the Amazon S3 objects delivered will
use the following key format recommended by Amazon Monitron:
`/project={projectName}/site={siteName}/time={yyyy-mm-dd
 00:00:00}/{filename}`

1. Sign into your AWS account.
2. Open a new browser tab with the following URL:

```
https://console.aws.amazon.com/cloudformation/home?region=us-east-1#/stacks/create/review?templateURL=https://s3.us-east-1.amazonaws.com/monitron-cloudformation-templates-us-east-1/monitron_kinesis_data_export.yaml&stackName=monitron-kinesis-live-data-export
```

3. On the AWS CloudFormation page that opens, in the upper right corner, select the
   region in which you are using Amazon Monitron.
4. By default, the template will create a new Kinesis data stream and S3
   bucket along with other resources needed to deliver data to Amazon S3. You
   can change the parameters to use existing resources.
5. Check the box that says _I acknowledge that AWS CloudFormation might
   create IAM resources._
6. Choose **Create stack**.
7. On the next page, choose the refresh icon as often as you like until
   the status of the stack is CREATE_COMPLETE.

## Configuring Kinesis manually in the

console

1. Sign in to the AWS Management Console and open the Kinesis console at
   https://console.aws.amazon.com/kinesis.
2. Choose **Delivery streams** in the navigation
   pane.
3. Choose **Create delivery stream**.
4. For Source, select **Amazon Kinesis Data Streams**.
5. For Destination, select **Amazon S3**.
6. Under **Source settings, Kinesis data stream**, enter
   the ARN of your Kinesis data stream.
7. Under **delivery stream name**, enter the name of
   your Kinesis data stream.
8. Under **Desination settings**, choose an Amazon S3 bucket
   or enter a bucket URI.
9. (optional) Enable dynamic partitioning using inline parsing for JSON.
   This option is appropriate if you want to partition streaming
   measurement data based on source information and timestamp. For
   example:
   - Choose **Enabled** for **Dynamic
     partitioning**.
   - Choose **Enabled** for **New line
     delimiter**.
   - Choose **Enabled** for **Inline
     parsing for JSON**.
   - Under **Dynamic partitioning keys**,
     add:

   | Key name | JQ expression       |
   | -------- | ------------------- | -------------------------------------------------------------- | ----------- |
   | project  | .projectDisplayName | "project=\(.)"                                                 |
   | site     | .siteDisplayName    | "site=\(.)"                                                    |
   | time     | .timestamp          | <br>sub("[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}$";<br>"00:00:00") | "time=\(.)" |

10. Choose **Apply dynamic partitioning keys** and
    confirm the generated Amazon S3 bucket prefix is
    `!{partitionKeyFromQuery:project}/!{partitionKeyFromQuery:site}/!{partitionKeyFromQuery:time}/`.
11. In Amazon S3, objects will use the following key format:
    `/project={projectName}/site={siteName}/time={yyyy-mm-dd
00:00:00}/{filename}`.
12. Choose **Create delivery stream**.
13. (optional) Use a more granular path.

If you chose a dynamic partition, use the preceeding Amazon S3 key format
if you plan to use AWS Glue and Athena to query the data. You can also
choose a finer key format, but the Amazon Athena query will not be
efficient. Here is an example of setting up a finer Amazon S3 key
path.

Under **Dynamic partitioning keys**, add:

| Key name | JQ expression              |
| -------- | -------------------------- | --------------------------------------------------- | --------------- |
| project  | .projectDisplayName        | "project=\(.)"                                      |
| site     | .siteDisplayName           | "site=\(.)"                                         |
| asset    | .assetDisplayName          | "asset=\(.)"                                        |
| position | .sensorPositionDisplayName | "position=\(.)"                                     |
| sensor   | .sensor.physicalId         | "sensor=\(.)"                                       |
| date     | .timestamp                 | sub("<br>[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}$"; "") | <br>"date=\(.)" |

In Amazon S3, objects will use the following key format: `/project={projectName}/site={siteName}/asset={assetName}/position={positionName}/sensor={sensorId}/date={yyyy-mm-dd}/time={HH:MM:SS}/{filename}`

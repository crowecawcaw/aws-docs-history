Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Storing exported data in Amazon S3

If you want to store your exported data in Amazon S3, use the following
procedure.

###### Topics

- [Configuring Kinesis manually in the
  console](#kinesis-configure-console-v2 "#kinesis-configure-console-v2")

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

| Key name | JQ expression          |
| -------- | ---------------------- | ------------------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| project  | .projectName           | "project=\(.)"                                          |
| site     | .eventPayload.siteName | "site=\(.)"                                             |
| time     | .timestamp             | sub("[0-9]{2}:[0-9]{2}:[0-9]{2}.[0-9]{3}$"; "00:00:00") | "time=\(.)" | 10. Choose **Apply dynamic partitioning keys** and confirm the generated Amazon S3 bucket prefix is `!{partitionKeyFromQuery:project}/!{partitionKeyFromQuery:site}/!{partitionKeyFromQuery:time}/`. 11. In Amazon S3, objects will use the following key format: `/project={projectName}/site={siteName}/time={yyyy-mm-dd 00:00:00}/{filename}`. 12. Choose **Create delivery stream**. |

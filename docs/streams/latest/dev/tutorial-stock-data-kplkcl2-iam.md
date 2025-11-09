# Create an IAM policy and

user

Security best practices for AWS dictate the use of fine-grained permissions to
control access to different resources. AWS Identity and Access Management (IAM) lets you to manage users and
user permissions in AWS. An [IAM
policy](../../../IAM/latest/UserGuide/PoliciesOverview.md "../../../IAM/latest/UserGuide/PoliciesOverview.md") explicitly lists actions that are allowed and the resources on which
the actions are applicable.

The following are the minimum permissions generally required for Kinesis Data Streams producers and
consumers.

| Producer                                                               | Actions             | Resource                                                                                                                                                    | Purpose |
| ---------------------------------------------------------------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `DescribeStream`, `DescribeStreamSummary`,<br>`DescribeStreamConsumer` | Kinesis data stream | Before attempting to read records, the consumer checks if the data<br>stream exists, if it's active, and if the shards are contained in the<br>data stream. |
| `SubscribeToShard`,<br>`RegisterStreamConsumer`                        | Kinesis data stream | Subscribes and registers consumers to a shard.                                                                                                              |
| `PutRecord`, `PutRecords`                                              | Kinesis data stream | Writes records to Kinesis Data Streams.                                                                                                                     |

| Consumer                                                                         | **Actions**           | **Resource**                                                                                                                                                                                      | **Purpose** |
| -------------------------------------------------------------------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `DescribeStream`                                                                 | Kinesis data stream   | Before attempting to read records, the consumer checks if the data<br>stream exists, if it's active, and if the shards are contained in the<br>data stream.                                       |
| `GetRecords`, `GetShardIterator`                                                 | Kinesis data stream   | Reads records from a shard.                                                                                                                                                                       |
| `CreateTable`, `DescribeTable`,<br>`GetItem`, `PutItem`, `Scan`,<br>`UpdateItem` | Amazon DynamoDB table | If the consumer is developed using the Kinesis Client Library (KCL)<br>(either version 1.x or 2.x), it needs permissions to a DynamoDB table to<br>track the processing state of the application. |
| `DeleteItem`                                                                     | Amazon DynamoDB table | For when the consumer performs split/merge operations on Kinesis Data Streams<br>shards.                                                                                                          |
| `PutMetricData`                                                                  | Amazon CloudWatch log | The KCL also uploads metrics to CloudWatch, which are useful for monitoring<br>the application.                                                                                                   |

For this tutorial, you will create a single IAM policy that grants all of the
preceding permissions. In production, you might want to create two policies, one for
producers and one for consumers.

###### To create an IAM policy

1. Locate the Amazon Resource Name (ARN) for the new data stream that you created
   in the previous step. You can find this ARN listed as **Stream
   ARN** at the top of the **Details** tab. The ARN
   format is as follows:

```
arn:aws:kinesis:`region`:`account`:stream/`name`
```

_region_

The AWS Region code; for example, `us-west-2`. For
more information, see [Region and Availability Zone Concepts](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-regions-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-regions-availability-zones").

_account_

The AWS account ID, as shown in [Account
Settings](https://console.aws.amazon.com/billing/home?#/account "https://console.aws.amazon.com/billing/home?#/account").

_name_

The name of the data stream that you created in the preceding
step, which is `StockTradeStream`. 2. Determine the ARN for the DynamoDB table to be used by the consumer (and to be
created by the first consumer instance). It must be in the following
format:

```
arn:aws:dynamodb:`region`:`account`:table/`name`
```

The Region and account ID are identical to the values in the ARN of the data
stream that you're using for this tutorial, but the _name_ is
the name of the DynamoDB table created and used by the consumer application. KCL
uses the application name as the table name. In this step, use
`StockTradesProcessor` for the DynamoDB table name, because that is
the application name used in later steps in this tutorial. 3. In the IAM console, in **Policies** ([https://console.aws.amazon.com/iam/home#policies](https://console.aws.amazon.com/iam/home#policies "https://console.aws.amazon.com/iam/home#policies")), choose **Create
policy**. If this is the first time that you have worked with IAM
policies, choose **Get Started**, **Create
Policy**. 4. Choose **Select** next to **Policy
Generator**. 5. Choose **Amazon Kinesis** as the AWS service. 6. Select `DescribeStream`, `GetShardIterator`,
`GetRecords`, `PutRecord`, and `PutRecords`
as the allowed actions. 7. Enter the ARN of the data stream that you're using in this tutorial. 8. Use **Add Statement** for each of the following:

| AWS Service       | Actions                                                                                           | ARN                                                                            |
| ----------------- | ------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Amazon DynamoDB   | `CreateTable`, `DeleteItem`,<br>`DescribeTable`, `GetItem`,<br>`PutItem`, `Scan`,<br>`UpdateItem` | The ARN of the DynamoDB table that you created in Step 2 of this<br>procedure. |
| Amazon CloudWatch | `PutMetricData`                                                                                   | `*`                                                                            |

The asterisk (`*`) that is used when specifying an ARN is not
required. In this case, it's because there is no specific resource in CloudWatch on
which the `PutMetricData` action is invoked. 9. Choose **Next Step**. 10. Change **Policy Name** to
`StockTradeStreamPolicy`, review the code, and choose
**Create Policy**.
The resulting policy document should look like this:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Stmt123",
 "Effect": "Allow",
 "Action": [
 "kinesis:DescribeStream",
 "kinesis:PutRecord",
 "kinesis:PutRecords",
 "kinesis:GetShardIterator",
 "kinesis:GetRecords",
 "kinesis:ListShards",
 "kinesis:DescribeStreamSummary",
 "kinesis:RegisterStreamConsumer"
 ],
 "Resource": [
 "arn:aws:kinesis:us-west-2:`111122223333`:stream/StockTradeStream"
 ]
 },
 {
 "Sid": "Stmt234",
 "Effect": "Allow",
 "Action": [
 "kinesis:SubscribeToShard",
 "kinesis:DescribeStreamConsumer"
 ],
 "Resource": [
 "arn:aws:kinesis:us-west-2:`111122223333`:stream/StockTradeStream/*"
 ]
 },
 {
 "Sid": "Stmt456",
 "Effect": "Allow",
 "Action": [
 "dynamodb:*"
 ],
 "Resource": [
 "arn:aws:dynamodb:us-west-2:`111122223333`:table/StockTradesProcessor"
 ]
 },
 {
 "Sid": "Stmt789",
 "Effect": "Allow",
 "Action": [
 "cloudwatch:PutMetricData"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

###### To create an IAM user

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. On the **Users** page, choose **Add
   user**.
3. For **User name**, type
   `StockTradeStreamUser`.
4. For **Access type**, choose **Programmatic
   access**, and then choose **Next:
   Permissions**.
5. Choose **Attach existing policies directly**.
6. Search by name for the policy that you created in the preceding procedure
   (`StockTradeStreamPolicy`. Select the box to the left of the
   policy name, and then choose **Next: Review**.
7. Review the details and summary, and then choose **Create
   user**.
8. Copy the **Access key ID**, and save it privately. Under
   **Secret access key**, choose **Show**,
   and save that key privately also.
9. Paste the access and secret keys to a local file in a safe place that only you
   can access. For this application, create a file named `~/.aws/credentials` (with strict permissions). The file should be
   in the following format:

```
[default]
aws_access_key_id=`access key`
aws_secret_access_key=`secret access key`
```

###### To attach an IAM policy to a user

1. In the IAM console, open [Policies](https://console.aws.amazon.com/iam/home?#policies "https://console.aws.amazon.com/iam/home?#policies") and choose **Policy Actions**.
2. Choose `StockTradeStreamPolicy` and
   **Attach**.
3. Choose `StockTradeStreamUser` and **Attach
   Policy**.

## Next steps

[Download and build the
code](tutorial-stock-data-kplkcl2-download.md "tutorial-stock-data-kplkcl2-download.md")

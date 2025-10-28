# Attach a resource-based policy to a

DynamoDB stream

You can attach a resource-based policy to an existing table's stream or modify an existing
policy by using the DynamoDB console, [PutResourcePolicy](../APIReference/API_PutResourcePolicy.md "../APIReference/API_PutResourcePolicy.md") API, the AWS CLI, AWS SDK, or an [AWS CloudFormation template](rbac-create-table.md#rbac-create-table-cfn "rbac-create-table.md#rbac-create-table-cfn").

###### Note

You can't attach a policy to a stream while creating it using the [CreateTable](../APIReference/API_CreateTable.md "../APIReference/API_CreateTable.md") or [UpdateTable](../APIReference/API_UpdateTable.md "../APIReference/API_UpdateTable.md") APIs.
However, you can modify or delete a policy after a table is deleted. You can also modify or
delete the policy of a disabled stream.

The following IAM policy example uses the `put-resource-policy` AWS CLI
command to attach a resource-based policy to the stream of a table named
`MusicCollection`. This example allows the user
`John` to perform the [GetRecords](../APIReference/API_streams_GetRecords.md "../APIReference/API_streams_GetRecords.md"),
[GetShardIterator](../APIReference/API_streams_GetShardIterator.md "../APIReference/API_streams_GetShardIterator.md"), and [DescribeStream](../APIReference/API_streams_DescribeStream.md "../APIReference/API_streams_DescribeStream.md") API actions on the stream.

Remember to replace the `italicized` text with your resource-specific information.

```
aws dynamodb put-resource-policy \
    --resource-arn arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`/stream/`2024-02-12T18:57:26.492` \
    --policy \
        "{
            \"Version\": \"2012-10-17\",
            \"Statement\": [
              {
                    \"Effect\": \"Allow\",
                    \"Principal\": {
                        \"AWS\": \"arn:aws:iam::`111122223333`:user/`John`\"
                    },
                    \"Action\": [
                        \"dynamodb:GetRecords\",
                        \"dynamodb:GetShardIterator\",
                        \"dynamodb:DescribeStream\"
                    ],
                    \"Resource\": \"arn:aws:dynamodb:us-west-2:`123456789012`:table/`MusicCollection`/stream/`2024-02-12T18:57:26.492`\"
                }
            ]
        }"
```

1. Sign in to the AWS Management Console and open the DynamoDB console at
   [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the DynamoDB console dashboard, choose **Tables** and then select
   an existing table.

Make sure the table you select has streams turned on. For information about
turning on streams for a table, see [Enabling a stream](Streams.md#Streams.Enabling "Streams.md#Streams.Enabling"). 3. Choose the **Permissions** tab. 4. In **Resource-based policy for active stream**, choose
**Create stream policy**. 5. In the **Resource-based policy** editor, add a policy to define
the access permissions for the stream. In this policy, you specify who has access to
the stream and the actions they are allowed to perform on the stream. To add a policy,
do one of the following:

    * Type or paste a JSON policy document. For details about the IAM policy
     language, see [Creating policies using the JSON editor](../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create-console.md#access_policies_create-json-editor") in the
     *IAM User Guide*.


    ###### Tip

    To see examples of resource-based policies in the Amazon DynamoDB Developer Guide, choose
     **Policy examples**.
    * Choose **Add new statement** to add a new statement and enter
     the information in the provided fields. Repeat this step for as many statements as
     you would like to add.

###### Important

Make sure that you resolve any security warnings, errors, or suggestions before
you save your policy. 6. (Optional) Choose **Preview external access** in the lower-right
corner to preview how your new policy affects public and cross-account access to your
resource. Before you save your policy, you can check whether it introduces new
IAM Access Analyzer findings or resolves existing findings. If you don’t see an active
analyzer, choose **Go to Access Analyzer** to [create an account analyzer](../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling "../../../IAM/latest/UserGuide/access-analyzer-getting-started.md#access-analyzer-enabling") in IAM Access Analyzer. For more information, see
[Preview
access](../../../IAM/latest/UserGuide/access-analyzer-access-preview.md "../../../IAM/latest/UserGuide/access-analyzer-access-preview.md"). 7. Choose **Create policy**.
The following IAM policy example attaches a resource-based policy to the stream of a
table named `MusicCollection`. This example allows the user
`John` to perform the [GetRecords](../APIReference/API_streams_GetRecords.md "../APIReference/API_streams_GetRecords.md"),
[GetShardIterator](../APIReference/API_streams_GetShardIterator.md "../APIReference/API_streams_GetShardIterator.md"), and [DescribeStream](../APIReference/API_streams_DescribeStream.md "../APIReference/API_streams_DescribeStream.md") API actions on the stream.

Remember to replace the `italicized` text with your resource-specific information.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:user/`username`"
 },
 "Action": [
 "dynamodb:GetRecords",
 "dynamodb:GetShardIterator",
 "dynamodb:DescribeStream"
 ],
 "Resource": [
 "arn:aws:dynamodb:`us-east-1`:`123456789012`:table/`MusicCollection`/stream/`2024-02-12T18:57:26.492`"
 ]
 }
 ]
}`

```

# Managing table policies

You can add, delete, update, and view table policies for tables by using the Amazon S3 console, Amazon S3 REST API, AWS SDK and the AWS CLI. For more information, see the following topics. For more information about supported AWS Identity and Access Management (IAM) actions and condition keys for Amazon S3 Tables, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md"). For example table policies, see [Resource-based policies for
S3 Tables](s3-tables-resource-based-policies.md "s3-tables-resource-based-policies.md").

## Adding a table policy

To add a table policy to a table, you can use the Amazon S3 REST API, AWS SDK and the AWS CLI.

This example shows how to view the policy attached to a table by using the AWS CLI. To use the
command replace the `user input placeholders` with your own
information.

```
aws s3tables get-table-policy \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`/table/`tableID` \
    --namespace `my-namespace` \
    --name `my-table`
```

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
   S3**.
3. Choose **Table buckets** and select the table
   bucket name that contains your table, then select your table from that bucket.
4. Choose the **Permissions** tab.
5. Under **Table policy**, Choose
   **Edit**.
6. In the policy editor, enter your policy JSON.
7. (Optional) Choose **Policy examples** to see sample
   policies that you can adapt to your needs.
8. After entering your policy, choose **Save
   changes**.

## Viewing a table policy

To view the bucket policy attached to a table, you can use the Amazon S3 REST API, AWS SDK and the AWS CLI.

This example shows how to view the policy attached to a table by using the AWS CLI. To use the
command replace the `user input placeholders` with your own
information.

```
aws s3tables get-table-policy \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket  \
    --namespace `my-namespace` \
    --name `my-table`
```

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
   S3**.
3. Choose **Table buckets** and select the table
   bucket name that contains your table, then select your table from that bucket.
4. Choose the **Permissions** tab.

## Deleting a table policy

To delete a policy attached to a table, you can use the Amazon S3 REST API, AWS SDK and the AWS CLI.

This example shows how to delete a table policy by using the AWS CLI. To use the
command replace the `user input placeholders` with your own
information.

```
aws s3tables delete-table-policy \
    --table-ARN arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/amzn-s3-demo-table-bucket \
    --namespace `your-namespace` \
    --name `your-table`
```

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
   S3**.
3. Choose **Table buckets** and select the table
   bucket name that contains your table, then select your table from that bucket.
4. Choose the **Permissions** tab.
5. Under **Table bucket policy**, choose
   **Delete**.

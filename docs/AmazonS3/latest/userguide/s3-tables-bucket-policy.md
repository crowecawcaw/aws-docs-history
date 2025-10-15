# Managing table bucket policies

You can add, delete, update, and view bucket policies for Amazon S3 table buckets by using
 the Amazon S3 REST API, AWS SDKs, and the AWS Command Line Interface (AWS CLI). For more information, see the
 following topics. 

For more information, see the following topics. For more information about supported
 AWS Identity and Access Management (IAM) actions and condition keys for Amazon S3 Tables, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md"). For example
 bucket policies for table buckets, see [Resource-based policies for
 S3 Tables](s3-tables-resource-based-policies.md "s3-tables-resource-based-policies.md").

###### Note

The table bucket policy provides access to the tables stored in the bucket. Table
 bucket policies don't apply to tables owned by other accounts.


## Adding a table bucket policy


To add a bucket policy to a table bucket, use the following AWS CLI example. 


This example shows how to create a table bucket policy by using the AWS CLI. To
 use the command, replace the ``user input
 placeholders`` with your own information.


```
aws s3tables put-table-bucket-policy \
    --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`  \
    --resource-policy `your-policy-JSON`
```

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
 S3**.
3. Choose **Table buckets** and select the table
 bucket name that you want to add a policy
 to.
4. Choose the **Permissions** tab.
5. Under **Table bucket policy**, Choose
 **Edit**.
6. In the policy editor, enter your policy JSON.
7. (Optional) Choose **Policy examples** to see sample
 policies that you can adapt to your needs.
8. After entering your policy, choose **Save
 changes**.

## Viewing a table bucket policy


To view the bucket policy that's attached to a table bucket, use the following AWS CLI
 example. 


This example shows how to view the policy that's attached to a table bucket
 by using the AWS CLI. To use the command, replace the ``user
 input placeholders`` with your own
 information.


```
aws s3tables get-table-bucket-policy --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`
```

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
 S3**.
3. Choose **Table buckets** and select the table bucket
 name that you want to view the policy for.
4. Choose the **Permissions** tab.

## Deleting a table bucket policy


To delete a bucket policy that's attached to a table bucket, use the following AWS CLI
 example. 


This example shows how to delete a table bucket policy by using the AWS CLI.
 To use the command, replace the ``user input
 placeholders`` with your own information.


```
aws s3tables delete-table-bucket-policy --table-bucket-arn arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`
```

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Amazon
 S3**.
3. Choose **Table buckets** and select the table bucket
 name that you want to delete a policy for.
4. Choose the **Permissions** tab.
5. Under **Table bucket policy**, choose
 **Delete**.

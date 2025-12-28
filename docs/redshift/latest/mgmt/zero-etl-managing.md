Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Modify a zero-ETL integration for

DynamoDB

In this step, you modify an DynamoDB zero-ETL integration with Amazon Redshift.

Amazon Redshift console

###### To modify an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the Amazon Redshift console

1. From the Amazon Redshift console, choose **Zero-ETL integrations**. On the
   pane with the list of zero-ETL integrations, then choose the DynamoDB integration that you want
   to modify.
2. Choose **Edit** and make modifications to the
   **Integration name** or **Description**.
3. Choose **Save changes** to save your changes.

AWS CLI
To modify an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the AWS CLI, use the
`modify-integration` command with the following options:

- `integration-arn` – Specify the ARN of the DynamoDB integration
  to modify.
- `integration-name` – Specify a new name for the
  integration.
- `description` – Specify a new description for the
  integration.

The follow example modifies an integration by providing the integration ARN, new
description, and new name.

```
`aws redshift modify-integration \
--integration-arn arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
--description "Test modify description and name together." \
--integration-name "updated-integration-name-2"`
      `{
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "IntegrationName": "updated-integration-name-2",
 "SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/ddb-temp-test-table-table",
 "SourceType": "dynamodb",
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "Status": "active",
 "Errors": [],
 "CreateTime": "2024-09-19T18:06:33.555Z",
 "Description": "Test modify description and name together.",
 "KMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "AdditionalEncryptionContext": {},
 "Tags": []
}`

```

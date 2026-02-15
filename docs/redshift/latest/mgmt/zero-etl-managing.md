Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Delete a zero-ETL integration for

DynamoDB

When you delete an integration, the target data warehouse retains any previously
replicated data. You can continue to share and query this data. However, new data in the
source will not replicate to the target.

In this step, you delete an DynamoDB zero-ETL integration with Amazon Redshift.

Amazon Redshift console

###### To delete an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the Amazon Redshift console

1. From the Amazon Redshift console, choose **Zero-ETL integrations**. On the
   pane with the list of zero-ETL integrations, then choose the DynamoDB integration that you want
   to delete.
2. Choose **Delete** and provide the requested information.
3. Choose **Delete** to delete the zero-ETL integration.

AWS CLI
To delete an Amazon DynamoDB zero-ETL integration with Amazon Redshift using the AWS CLI, use the
`delete-integration` command with the following options:

- `integration-arn` – Specify the ARN of the DynamoDB integration
  to delete.

The follow example deletes an integration by providing the integration ARN.

```
`aws redshift delete-integration \
--integration-arn arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`
    `{
 "IntegrationArn": "arn:aws:redshift:us-east-1:123456789012:integration:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
 "IntegrationName": "updated-integration-name-2",
 "SourceArn": "arn:aws:dynamodb:us-east-1:123456789012:table/tidal-ddb-ddb-temp-test-table-table",
 "SourceType": "dynamodb",
 "TargetArn": "arn:aws:redshift:us-east-1:123456789012:namespace:a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
 "Status": "deleting",
 "Errors": [],
 "CreateTime": "2024-09-19T18:06:33.555Z",
 "Description": "Test modify description and name together.",
 "KMSKeyId": "arn:aws:kms:us-east-1:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111:key/a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
 "AdditionalEncryptionContext": {},
 "Tags": []
}`
```

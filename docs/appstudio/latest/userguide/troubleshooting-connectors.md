# Troubleshooting connectors

This topic contains troubleshooting guidance for common connector issues. You must be a member of an admin group to view or edit connectors.

## Check that your IAM role has the correct custom trust policy and tag

While setting up the IAM role for your connector, ensure that the custom
trust policy is properly configured to provide access to App Studio. This custom trust policy is still needed if the AWS resources are in the same AWS account used to
set up App Studio.

- Ensure the AWS account number in the `Principal` section is the AWS account ID of the account used to set up App Studio. This
  account number is not always the account in which the resource is located.
- Ensure `"aws:PrincipalTag/IsAppStudioAccessRole": "true"` is properly added in the `sts:AssumeRole` section.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:PrincipalTag/IsAppStudioAccessRole": "true"
 }
 }
 }
 ]
}`

```

Also ensure that a tag with the following key and value have been added to the IAM role, for more information about adding tags, see
[Tag IAM roles](../../../IAM/latest/UserGuide/id_tags_roles.md "../../../IAM/latest/UserGuide/id_tags_roles.md"):

###### Note

Note that the value of the tag is `IsAppStudioDataAccessRole`, which is slightly different than the value in the
custom trust policy (`IsAppStudioAccessRole`).

- **Key:** `IsAppStudioDataAccessRole`
- **Value:** `true`

Check the configuration of the resources in the product or service that your connector is connecting to. Some resources, such as Amazon Redshift tables, require
additional configuration to use with App Studio.

Check your connector configuration. For AWS services, go to the connector in App Studio and ensure the correct Amazon Resource Name (ARN) is included and the AWS Region specified
is the one that contains your resources.

## Check that your IAM role has the correct permissions

To provide App Studio access to AWS resources, you must assign appropriate permissions to the IAM role used by your connector.
The required permissions are unique to the service, resource, and actions to be performed. For example, reading data from a Amazon Redshift table
requires different permissions than uploading an object to an Amazon S3 bucket. See the appropriate topic in
[Connect to AWS services](add-connector-services.md "add-connector-services.md") for more information.

## Troubleshooting Amazon Redshift connectors

This section includes troubleshooting guidance for common issues with Amazon Redshift connectors. For information about configuring
Amazon Redshift connectors and resources, see [Connect to Amazon Redshift](connectors-redshift.md "connectors-redshift.md").

1. Ensure that the `Isolated Session` toggle is set to `OFF` on the Amazon Redshift editor. This setting is
   required to allow visibility of data changes made by other users, such as an App Studio app.
2. Ensure the appropriate permissions are granted on the Amazon Redshift table.
3. In the connector configuration, ensure that the appropriate compute type
   (`Provisioned` or `Serverless`) is selected to match the Amazon Redshift table type.

## Troubleshooting Aurora connectors

This section includes troubleshooting guidance for common issues with Aurora connectors. For information about configuring
Aurora connectors and resources, see [Connect to Amazon Aurora](connectors-aurora.md "connectors-aurora.md").

1. Ensure that the appropriate and supported Aurora version is chosen when creating the table.
2. Verify that the Amazon RDS Data API is enabled, as this is a requirement to allow App Studio to perform operations on the Aurora tables. For
   more information, see [Enabling Amazon RDS Data API](../../../AmazonRDS/latest/AuroraUserGuide/data-api.md#data-api.enabling "../../../AmazonRDS/latest/AuroraUserGuide/data-api.md#data-api.enabling").
3. Verify that AWS Secrets Manager permissions are provided.

## Troubleshooting DynamoDB connectors

This section includes troubleshooting guidance for common issues with DynamoDB connectors. For information about configuring
DynamoDB connectors and resources, see [Connect to Amazon DynamoDB](connectors-dynamodb.md "connectors-dynamodb.md").

If your DynamoDB table schemas don't appear when creating the connector, it may be because your DynamoDB table is
encrypted with a customer-managed key (CMK) and the table data cannot be accessed without permissions to describe
the key and decrypt the table. In order to create a DynamoDB connector with a table encrypted with a CMK,
you must add the `kms:decrypt` and `kms:describeKey` permissions to your IAM role.

## Troubleshooting Amazon S3 connectors

This section includes troubleshooting guidance for common issues with Amazon S3 connectors. For information about configuring
Amazon S3 connectors and resources, see [Connect to Amazon Simple Storage Service (Amazon S3)](connectors-s3.md "connectors-s3.md").

General troubleshooting guidance includes checking the following:

1. Ensure the Amazon S3 connector is configured with the AWS Region that the Amazon S3 resources are in.
2. Ensure the IAM role is configured correctly.
3. In the Amazon S3 bucket, ensure the CORS configuration grants the appropriate permissions. For more information, see
   [Step 1: Create and configure Amazon S3 resources](connectors-s3.md#connectors-s3-create-resources "connectors-s3.md#connectors-s3-create-resources").

### Amazon S3 file upload error: Failed to calculate presigned URL

You may encounter the following error when trying to upload a file to an Amazon S3
bucket using the S3 Upload component:

```
Error while uploading file to S3: Failed to calculate presigned URL.
```

This error is typically caused by either an incorrect IAM role configuration, or incorrect CORS configuration
on the Amazon S3 bucket and can be resolved by fixing those configurations with the information
in [Connect to Amazon Simple Storage Service (Amazon S3)](connectors-s3.md "connectors-s3.md").

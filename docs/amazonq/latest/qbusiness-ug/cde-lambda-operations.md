# Using Lambda functions for

Amazon Q Business document enrichment

You can use Lambda functions to prepare your document attributes for
advanced data manipulation. For example, you could use Optical Character Recognition
(OCR), which interprets text from images and treats each image as a textual
document. Or, you could retrieve the current date-time in a specific time zone and
then insert the date-time where there's an empty value for a date field.

You can choose to apply a basic operation first and then use a Lambda
function to manipulate your data, and the reverse.

Amazon Q Business requires an Amazon S3 bucket when using Lambda functions for
custom document enrichment. This bucket serves as temporary storage during document
processing. Amazon Q Business carries out the following steps when interacting
with an Amazon S3 bucket:

1. Before invoking the Lambda function, Amazon Q Business uploads the
   document to your Amazon S3 bucket.
2. Your Lambda function code must get the document from the bucket and may
   then processes it.
3. Your Lambda code must put the processed document into the bucket for
   Amazon Q Business to retrieve.
4. You inform Amazon Q Business what updated document to retrieve
   using parameters in the return parameter.
5. Amazon Q Business retrieves the processed document and continues.

###### Note

Amazon Q Business can't create a target document attribute field if it
isn't already created as an index field.

###### Topics

- [Lambda functions using
  the Amazon Q Business API](#cde-lambda-operations-api "#cde-lambda-operations-api")
- [Lambda functions
  using the Amazon Q Business console](#cde-lambda-operations-console "#cde-lambda-operations-console")
- [IAM roles for
  Lambda functions](#cde-lambda-operations-iam-roles "#cde-lambda-operations-iam-roles")
- [Use cases for Lambda functions](#cde-lambda-operations-examples "#cde-lambda-operations-examples")
- [Code examples of Lambda functions](#cde-lambda-operations-code-samples "#cde-lambda-operations-code-samples")
- [Data contracts for
  Lambda functions](#cde-lambda-operations-data-contracts "#cde-lambda-operations-data-contracts")

## Lambda functions using

the Amazon Q Business API

To apply a Lambda function, you specify your advanced data
manipulation logic using the [DocumentEnrichmentConfiguration](../api-reference/API_DocumentEnrichmentConfiguration.md "../api-reference/API_DocumentEnrichmentConfiguration.md")
object when you use either the [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation or the [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation.

Your Lambda functions must follow the mandatory request and
response structures. For more information, see [Data contracts for Lambda
functions](cde-lambda-operations.md#cde-lambda-operations-data-contracts "cde-lambda-operations.md#cde-lambda-operations-data-contracts").

Use the following parameters to create your configuration:

- `InlineDocumentEnrichmentConfiguration` –
  Configuration information to alter document attributes during
  ingestion.
- `PostExtractionHookConfiguration` – Configuration
  information to invoke a Lambda function on structured
  documents with their metadata and text already extracted.
- `PreExtractionHookConfiguration` – Configuration
  information to invoke a Lambda function on raw documents
  before metadata and text has been extracted from them.
- `PreExtractionHookConfiguration` RoleArn – The
  Amazon Resource Name (ARN) of a role under
  `PreExtractionHookConfiguration` with permissions to run
  `PreExtractionHookConfiguration` and to access the Amazon S3
  bucket when you use `PreExtractionHookConfiguration`.
- `PostExtractionHookConfiguration` RoleArn – The
  Amazon Resource Name (ARN) of a role under
  `PostExtractionHookConfiguration` with permissions to run
  `PreExtractionHookConfiguration` and to access the Amazon S3
  bucket when you use `PostExtractionHookConfiguration`.

You can configure only one Lambda function for
`PreExtractionHookConfiguration` and only one Lambda
function for `PostExtractionHookConfiguration`. However, your Lambda function can invoke other functions that it requires.

You can configure both `PreExtractionHookConfiguration` and
`PostExtractionHookConfiguration` or either one. Your Lambda function for `PreExtractionHookConfiguration` must not
exceed a run time of 5 minutes. Your Lambda function for
`PostExtractionHookConfiguration` must not exceed a run time of 1
minute.

You can configure Amazon Q Business to invoke a Lambda
function only if a condition is met. For example, you can specify a condition
that, if there are empty date-time values, then Amazon Q Business invokes
a function that inserts the current date-time.

For more information, see the following topics in the _Amazon Q Business API Reference_:

- [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md")
- [CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md")
- [DocumentEnrichmentConfiguration](../api-reference/API_DocumentEnrichmentConfiguration.md "../api-reference/API_DocumentEnrichmentConfiguration.md")
- [DocumentAttributeCondition](../api-reference/API_DocumentAttributeCondition.md "../api-reference/API_DocumentAttributeCondition.md")

## Lambda functions

using the Amazon Q Business console

###### To configure a Lambda function using the console

1. Select your index, and then select
   **Document enrichments** from the navigation
   menu.
2. To configure Lambda functions, go to **Configure
   Lambda functions**.

## IAM roles for

Lambda functions

When you use the Lambda functions for CDE, you need an IAM role for the following:

- A role for `PreExtractionHookConfiguration` with
  permissions to run `PreExtractionHookConfiguration` and to
  access the Amazon S3 bucket when you use
  `PreExtractionHookConfiguration`.
- A role for `PostExtractionHookConfiguration` with
  permissions to run `PreExtractionHookConfiguration` and to
  access the Amazon S3 bucket when you use
  `PostExtractionHookConfiguration`.

###### Important

IAM roles for Custom Document Enrichmmnt (CDE) Lambda functions should
belong to the same account as the account using [BatchPutDocument](../api-reference/API_BatchPutDocument.md "../api-reference/API_BatchPutDocument.md") API operation or the
[CreateDataSource](../api-reference/API_CreateDataSource.md "../api-reference/API_CreateDataSource.md") operation
to configure CDE.

Both AWS Identity and Access Management (IAM) roles must have the permissions to:

- Run `PreExtractionHookConfiguration` and/or
  `PostExtractionHookConfiguration`. To apply advanced
  alterations of your document metadata and content during the ingestion
  process, configure a Lambda function for
  `PreExtractionHookConfiguration` and/or
  `PostExtractionHookConfiguration`.
- (Optional) If you choose to activate Server Side Encryption for your
  Amazon S3 bucket, you must provide permissions to use the
  AWS KMS key to encrypt and decrypt the objects stored in
  your Amazon S3 bucket.

**A role policy to allow Amazon Q Business to run
`PreExtractionHookConfiguration` with encryption for your
Amazon S3 bucket.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/`key-id`"
 ],
 "Effect": "Allow",
 "Sid": "KMSPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:`pre-extraction-lambda-function`",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**An role policy to allow Amazon Q Business to run
`PreExtractionHookConfiguration` without
encryption.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:`pre-extraction-lambda-function`",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**A role policy to allow Amazon Q Business to run
`PostExtractionHookConfiguration` with Default (server-side
encryption with S3-managed keys (SSE-S3) for your Amazon S3
bucket.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Sid": "KMSPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:`post-extraction-lambda-function`",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**A role policy to allow Amazon Q Business to run
`PostExtractionHookConfiguration` with encryption for your
Amazon S3 bucket.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:111122223333:key/key-id"
 ],
 "Effect": "Allow",
 "Sid": "KMSPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:post-extraction-lambda-function",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

**An role policy to allow Amazon Q Business to run
`PostExtractionHookConfiguration` without
encryption.**

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "s3:GetObject",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name",
 "arn:aws:s3:::bucket-name/*"
 ],
 "Effect": "Allow",
 "Sid": "S3GetObjectPermissions"
 },
 {
 "Action": [
 "s3:ListBucket"
 ],
 "Resource": [
 "arn:aws:s3:::bucket-name"
 ],
 "Effect": "Allow",
 "Sid": "S3ListBucketPermissions"
 },
 {
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Resource": "arn:aws:lambda:us-east-1:111122223333:function:post-extraction-lambda-function",
 "Effect": "Allow",
 "Sid": "LambdaPermissions"
 }
 ]
}`

```

We recommend that you include `aws:sourceAccount` and
`aws:sourceArn` in the trust policy. Their inclusion limits
permissions and securely checks if `aws:sourceAccount` and
`aws:sourceArn` are the same values as provided in the IAM role policy for the `sts:AssumeRole` action. This
approach prevents unauthorized entities from accessing your IAM
roles and their permissions. For more information, see [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _IAM User Guide_.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "sts:AssumeRole",
 "Sid": "QBusinessTrustPolicy",
 "Effect": "Allow",
 "Condition": {
 "StringLike": {
 "aws:SourceArn": "arn:aws:qbusiness:`your-region`:`your-account-id`:application/<`application-id`>/index/<`index-id`>"
 },
 "StringEquals": {
 "aws:SourceAccount": "your-account-id"
 }
 },
 "Principal": {
 "Service": [
 "qbusiness.amazonaws.com"
 ]
 }
 }
 ]
}`

```

## Use cases for Lambda functions

This section outlines two examples of using Lambda
functions.

**Example 1: Extracting text from images to create textual
documents**

The following is an example of using a Lambda function to run OCR to interpret
text from images and store this text in a field called
`document_image_text`.

The following table shows data before advanced manipulation is applied.

| **\_document_id** | **document_image**  |
| ----------------- | ------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1                 | image_1.png         |
| 2                 | image_2.png         |
| 3                 | image_3.png         | The following table shows data after advanced manipulation is applied. |
| **\_document_id** | **document_image**  | **document_image_text**                                                |
| ---               | ---                 | ---                                                                    |
| 1                 | image_1.png         | Mailed survey response                                                 |
| 2                 | image_2.png         | Mailed survey response                                                 |
| 3                 | image_3.png         | Mailed survey response                                                 | **Example 2: Replacing empty values in the Last_Updated field with the current date-time** The following is an example of using a Lambda function to insert the current date-time for empty date values. This example uses the condition that, if a date field value is `null`, then the value is replaced with the current date-time. The following table shows data before advanced manipulation is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **\_document_id** | **\_document_body** | **\_last_updated_at**                                                  |
| ---               | ---                 | ---                                                                    |
| 1                 | Example text        | January 1, 2020                                                        |
| 2                 | Example text        |                                                                        |
| 3                 | Example text        | July 1, 2020                                                           | The following table shows data after advanced manipulation is applied.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **\_document_id** | **\_document_body** | **\_last_updated_at**                                                  |
| ---               | ---                 | ---                                                                    |
| 1                 | Example text        | January 1, 2020                                                        |
| 2                 | Example text        | December 1, 2021                                                       |
| 3                 | Example text        | July 1, 2020                                                           | ## Code examples of Lambda functions The following code is an example of configuring a Lambda function for advanced data manipulation on the raw, original data. Console **To configure a Lambda function for advanced data manipulation on the raw, original data** 1. Sign in to the AWS Management Console and open the Amazon Q Business console. 2. From the left navigation menu, choose **Enhancements**, and then choose **Document enrichments**. 3. In **Document enrichments**, choose **Add document enrichment**. 4. In **Configure basic operations**, for **Document enrichment source**, choose a data source connected to your application environment. 5. (Optional) To apply basic manipulations to your document fields and content, go to **Configure basic operations** and choose **Next** to save your configuration. 6. On the **Configure Lambda functions** page, in the **Lambda for pre-extraction** section, select your Lambda function ARN and your Amazon S3 bucket using the dropdown menus. 7. To add your IAM access role, select the option to create a new role from the dropdown. This step creates the required Amazon Q Business permissions to create the document enrichment. 8. Select **Add basic operation**. AWS CLI **To configure a Lambda function for advanced data manipulation on the raw, original data** ``aws qbusiness create-data-source \ --display-name `data-source-name` \ --application-id `application-id` \ --index-id `index-id` \ --role-arn `arn:aws:iam::account-id:role/role-name` \ --configuration '{"connectionConfiguration":{"repositoryEndpointMetadata":{"BucketName":"`S3-bucket-name`"}}, "type":"`S3`", "syncMode": "`Sync-Mode-Type`", "repositoryConfigurations":{"document":{"fieldMappings":[{"dataSourceFieldName":"`s3_document_id`","indexFieldName":"`s3_document_id`","indexFieldType":"`STRING`"}]}}}' \ --document-enrichment-configuration '{"inlineConfigurations":[{"target":{"key":"`_file_type`","value":{"stringValue":"`file-type`"}}, "condition":{"key":"`_file_type`","operator":"`operator-type`","value":{"stringValue":"`file-type`"}}}]}'`` Python **To configure a Lambda function for advanced data manipulation on the raw, original data** ``import boto3 from botocore.exceptions import ClientError import pprint import time qbusiness = boto3.client("qbusiness") print("Create a data source with customizations") # Provide the name of the data source name = "data-source-name" # Provide the application ID for the data source application_id = "`application-id`" # Provide the index ID for the data source index_id = "index-id" # Provide the IAM role ARN required for data sources role_arn = "arn:aws:iam::${account-id}:role/${role-name}" # Provide the data source connection information data_source_type = "S3" S3_bucket_name = "S3-bucket-name" # Configure the data source with Document Enrichment configuration = {"S3Configuration": { "BucketName": S3_bucket_name } } document_enrichment_configuration = {"InlineDocumentEnrichmentConfiguration":[ { "Target":{"key":"Customer_ID", "attributeValueOperator": "DELETE"} }] } try: data_source_response = qbusiness.create_data_source( Name = name, ApplicationId = application_id, IndexId = index_id, RoleArn = role_arn, Type = data_source_type Configuration = configuration DocumentEnrichmentConfiguration = document_enrichment_configuration ) pprint.pprint(data_source_response) data_source_id = data_source_response["Id"] print("Wait for Amazon Q to create the data source with your customizations.") while True: # Get the details of the data source, such as the status data_source_description = qbusiness.get_data_source( DataSourceId = data_source_id, ApplicationId = application_id, IndexId = index_id ) status = data_source_description["Status"] print(" Creating data source. Status: "+status) time.sleep(60) if status != "CREATING": break print("Synchronize the data source.") sync_response = qbusiness.start_data_source_sync_job( DataSourceId = data_source_id, ApplicationId = application_id, IndexId = index_id ) pprint.pprint(sync_response) print("Wait for the data source to sync with the index.") while True: jobs = qbusiness.list_data_source_sync_jobs( DataSourceId = data_source_id, ApplicationId = application_id, IndexId = index_id ) # For this example, there should be one job status = jobs["History"][0]["Status"] print(" Syncing data source. Status: "+status) time.sleep(60) if status != "SYNCING": break except  ClientError as e: print("%s" % e) print("Program ends.")`` Java **To configure a Lambda function for advanced data manipulation on the raw, original data** ``package com.amazonaws.qbusiness; import java.util.concurrent.TimeUnit; import software.amazon.awssdk.services.qbusiness.QBusinessClient; import software.amazon.awssdk.services.qbusiness.model.AttributeValueOperator; import software.amazon.awssdk.services.qbusiness.model.CreateDataSourceRequest; import software.amazon.awssdk.services.qbusiness.model.CreateDataSourceResponse; import software.amazon.awssdk.services.qbusiness.model.CreateIndexRequest; import software.amazon.awssdk.services.qbusiness.model.CreateIndexResponse; import software.amazon.awssdk.services.qbusiness.model.DataSourceConfiguration; import software.amazon.awssdk.services.qbusiness.model.DataSourceStatus; import software.amazon.awssdk.services.qbusiness.model.DataSourceSyncJob; import software.amazon.awssdk.services.qbusiness.model.DataSourceSyncJobStatus; import software.amazon.awssdk.services.qbusiness.model.DataSourceType; import software.amazon.awssdk.services.qbusiness.model.GetDataSourceRequest; import software.amazon.awssdk.services.qbusiness.model.GetDataSourceResponse; import software.amazon.awssdk.services.qbusiness.model.IndexStatus; import software.amazon.awssdk.services.qbusiness.model.ListDataSourceSyncJobsRequest; import software.amazon.awssdk.services.qbusiness.model.ListDataSourceSyncJobsResponse; import software.amazon.awssdk.services.qbusiness.model.DataSourceConfiguration; import software.amazon.awssdk.services.qbusiness.model.StartDataSourceSyncJobRequest; import software.amazon.awssdk.services.qbusiness.model.StartDataSourceSyncJobResponse; public class CreateDataSourceWithCustomizationsExample { public static void main(String[] args) throws InterruptedException { System.out.println("Create a data source with customizations"); String dataSourceName = "`data-source-name`"; String applicationId = "`application-id`"; String indexId = "`index-id`"; String dataSourceRoleArn = "arn:aws:iam::`account-id`:role/`role-name`"; String s3BucketName = "`S3-bucket-name`" QBusinessClient qbusiness = QBusinessClient.builder().build(); CreateDataSourceRequest createDataSourceRequest = CreateDataSourceRequest .builder() .name(dataSourceName) .applicationId(applicationId) .indexId(indexId) .description(experienceDescription) .roleArn(experienceRoleArn) .type(DataSourceType.S3) .configuration( DataSourceConfiguration .builder() .s3Configuration( S3DataSourceConfiguration .builder() .bucketName(s3BucketName) .build() ).build() ) .documentEnrichmentConfiguration( DocumentEnrichmentConfiguration .builder() .inlineConfigurations(Arrays.asList( InlineDocumentEnrichmentConfiguration .builder() .target( DocumentAttributeTarget .builder() .key("Customer_ID") .attributeValueOperator(AttributeValueOperator.DELETE) .build()) .build() )).build(); CreateDataSourceResponse createDataSourceResponse = qbusiness.createDataSource(createDataSourceRequest); System.out.println(String.format("Response of creating data source: %s", createDataSourceResponse)); String dataSourceId = createDataSourceResponse.id(); System.out.println(String.format("Waiting for Amazon Q to create the data source %s", dataSourceId)); GetDataSourceRequest getDataSourceRequest = GetDataSourceRequest .builder() .applicationId(applicationId) .indexId(indexId) .datasourceId(dataSourceId) .build(); while (true) { GetDataSourceResponse getDataSourceResponse = qbusiness.getDataSource(getDataSourceRequest); DataSourceStatus status = getDataSourceResponse.status(); System.out.println(String.format("Creating data source. Status: %s", status)); TimeUnit.SECONDS.sleep(60); if (status != DataSourceStatus.CREATING) { break; } } System.out.println(String.format("Synchronize the data source %s", dataSourceId)); StartDataSourceSyncJobRequest startDataSourceSyncJobRequest = StartDataSourceSyncJobRequest .builder() .applicationId(applicationId) .indexId(indexId) .datasourceId(dataSourceId) .build(); StartDataSourceSyncJobResponse startDataSourceSyncJobResponse = qbusiness.startDataSourceSyncJob(startDataSourceSyncJobRequest); System.out.println(String.format("Waiting for the data source to sync with the application %s index %s for execution ID %s", applicationId, indexId, startDataSourceSyncJobResponse.executionId())); // For this example, there should be one job ListDataSourceSyncJobsRequest listDataSourceSyncJobsRequest = ListDataSourceSyncJobsRequest .builder() .applicationId(applicationId) .indexId(indexId) .datasourceId(dataSourceId) .build(); while (true) { ListDataSourceSyncJobsResponse listDataSourceSyncJobsResponse = qbusiness.listDataSourceSyncJobs(listDataSourceSyncJobsRequest); DataSourceSyncJob job = listDataSourceSyncJobsResponse.history().get(0); System.out.println(String.format("Syncing data source. Status: %s", job.status())); TimeUnit.SECONDS.sleep(60); if (job.status() != DataSourceSyncJobStatus.SYNCING) { break; } } System.out.println("Data source creation with customizations is complete"); } }`` ## Data contracts for Lambda functions Lambda functions for advanced data manipulation interact with Amazon Q Business data contracts. The contracts are the mandatory request and response structures of your Lambda functions. If your Lambda functions don't follow these structures, then Amazon Q Business produces an error. Your Lambda function for `PreExtractionHookConfiguration` should use the following request structure: `{ "version": <str>, "dataBlobStringEncodedInBase64": <str>, //In the case of a data blob "s3Bucket": <str>, //In the case of an S3 bucket "s3ObjectKey": <str>, //In the case of an S3 bucket "metadata": <Metadata> }` [Show moreShow less](# "#") The `metadata` structure, which includes the `DocumentAttribute` structure, is as follows: `{ "attributes": [<DocumentAttribute<] } DocumentAttribute { "name": <str>, "value": <DocumentAttributeValue> } DocumentAttributeValue { "stringValue": <str>, "integerValue": <int>, "longValue": <long>, "stringListValue": list<str>, "dateValue": <str> }` [Show moreShow less](# "#") Your Lambda function for `PreExtractionHookConfiguration` must adhere to the following response structure: `{ "version": <str>, "dataBlobStringEncodedInBase64": <str>, //In the case of a data blob "s3ObjectKey": <str>, //In the case of an S3 bucket "metadataUpdates": [<DocumentAttribute>] }` [Show moreShow less](# "#") Your Lambda function for `PostExtractionHookConfiguration` should expect the following request structure: `{ "version": <str>, "s3Bucket": <str>, "s3ObjectKey": <str>, "metadata": <Metadata> }` [Show moreShow less](# "#") Your Lambda function for `PostExtractionHookConfiguration` must adhere to the following response structure: `PostExtractionHookConfiguration Lambda Response { "version": <str>, "s3ObjectKey": <str>, "metadataUpdates": [<DocumentAttribute>] }` [Show moreShow less](# "#") Amazon Q Business uploads your structured document to the specified Amazon S3 bucket. The structured document follows this format: `QBusiness document { "textContent": <TextContent> } TextContent { "documentBodyText": <str> }` [Show moreShow less](# "#") ### Examples of Lambda functions that adhere to data contracts This section provides examples of how to structure your Lambda functions that adhere to Amazon Q Business data contracts. **Example 1: A Lambda function that applies advanced manipulation to raw documents** The following Python code is an example of a Lambda function that applies advanced manipulation of the metadata fields `_authors`, `_document_title`, and the body content on the raw or original documents. The following code example shows the case of the body content residing in an Amazon S3 bucket `import json import boto3 s3 = boto3.client("s3") # Lambda function for advanced data manipulation def lambda_handler(event, context): # Get the value of "S3Bucket" key name or item from the given event input s3_bucket = event.get("s3Bucket") # Get the value of "S3ObjectKey" key name or item from the given event input s3_object_key = event.get("s3ObjectKey") content_object_before_DE = s3.get_object(Bucket = s3_bucket, Key = s3_object_key) content_before_DE = content_object_before_DE["Body"].read().decode("utf-8"); content_after_DE = "DEInvolved " + content_before_DE # Get the value of "metadata" key name or item from the given event input metadata = event.get("metadata") # Get the document "attributes" from the metadata document_attributes = metadata.get("attributes") s3.put_object(Bucket = s3_bucket, Key = "dummy_updated_qbusiness_document", Body=json.dumps(content_after_DE)) return { "version": "v0", "s3ObjectKey": "dummy_updated_qbusiness_document", "metadataUpdates": [ {"name":"_document_title", "value":{"stringValue":"title_from_pre_extraction_lambda"}}, {"name":"_authors", "value":{"stringListValue":["author1", "author2"]}} ] }` [Show moreShow less](# "#") **Example 2: A Lambda function that applies advanced manipulation to structured or parsed documents** The following Python code is an example of a Lambda function that applies advanced manipulation of the metadata fields `_authors`, `_document_title`, and the body content on the structured or parsed documents. `import json import boto3 import time s3 = boto3.client("s3") # Lambda function for advanced data manipulation def lambda_handler(event, context): # Get the value of "S3Bucket" key name or item from the given event input s3_bucket = event.get("s3Bucket") # Get the value of "S3ObjectKey" key name or item from the given event input s3_key = event.get("s3ObjectKey") # Get the value of "metadata" key name or item from the given event input metadata = event.get("metadata") # Get the document "attributes" from the metadata document_attributes = metadata.get("attributes") qbusiness_document_object = s3.get_object(Bucket = s3_bucket, Key = s3_key) qbusiness_document_string = qbusiness_document_object['Body'].read().decode('utf-8') qbusiness_document = json.loads(qbusiness_document_string) qbusiness_document["textContent"]["documentBodyText"] = "Changing document body to a short sentence." s3.put_object(Bucket = s3_bucket, Key = "dummy_updated_qbusiness_document", Body=json.dumps(qbusiness_document)) return { "version" : "v0", "s3ObjectKey": "dummy_updated_qbusiness_document", "metadataUpdates": [ {"name": "_document_title", "value":{"stringValue": "title_from_post_extraction_lambda"}}, {"name": "_authors", "value":{"stringListValue":["author1", "author2"]}} ] }` [Show moreShow less](# "#") **Example 3: Body content residing in a data blob** `import json import boto3 import base64 # Lambda function for advanced data manipulation def lambda_handler(event, context): # Get the value of "dataBlobStringEncodedInBase64" key name or item from the given event input data_blob_string_encoded_in_base64 = event.get("dataBlobStringEncodedInBase64") # Decode the data blob string in UTF-8 data_blob_string = base64.b64decode(data_blob_string_encoded_in_base64).decode("utf-8") # Get the value of "metadata" key name or item from the given event input metadata = event.get("metadata") # Get the document "attributes" from the metadata document_attributes = metadata.get("attributes") new_data_blob = "This should be the modified data in the document by pre processing lambda ".encode("utf-8") return { "version": "v0", "dataBlobStringEncodedInBase64": base64.b64encode(new_data_blob).decode("utf-8"), "metadataUpdates": [ {"name":"_document_title", "value":{"stringValue":"title_from_pre_extraction_lambda"}}, {"name":"_authors", "value":{"stringListValue":["author1", "author2"]}} ] }` [Show moreShow less](# "#") |

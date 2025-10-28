# Set up bulk export for all of your unified customer

profile data

###### Note

To complete the steps in this topic, you need to have developer skills, and be
experienced with using AWS KMS and Amazon S3.

When Amazon Connect Customer Profiles creates a unified customer profile, it enhances, refines, and improves
raw data and information into a more accurate profile by combining data from first-party
and third-party sources. Customer Profiles also improves the quality of the datasets through the
addition of new data. You can use the improved datasets for additional use cases, such
as to formulate more informed and targeted marketing, sales, and customer service
strategies. For example, you may want to leverage the unified customer profile to:

- Audit the customer data you have in the entirety of a domain.
- Perform in-house analytics, for example, for sales and marketing
  reports.
- Export the data into your own tools or third-party products, to personalize
  ads and target customers.
  To leverage the unified customer profile data for additional use cases, you can bulk
  export it to Amazon S3. This topic explains how to do that.

###### Contents

- [Step 1: Set up a KMS key and S3
  bucket](#enable-cpbulk-export "#enable-cpbulk-export")
- [Step 2: Create a bulk export job](#create-bulk-export-job "#create-bulk-export-job")
- [Step 3: Check the status of a bulk
  export job](#check-status-bulk-cp-export "#check-status-bulk-cp-export")
- [Step 4: View the exported data in S3](#view-bulk-cp-export "#view-bulk-cp-export")
- [Update the bulk export job](#update-bulk-cp-export "#update-bulk-cp-export")
- [Delete or cancel the bulk export job - not
  supported](#delete-bulk-cp-export "#delete-bulk-cp-export")

## Step 1: Set up a KMS key and S3

bucket

To enable bulk export for your domain, you’ll need to setup the following
resources:

- [A KMS key with a specific resource
  policy](#cp-kms "#cp-kms")
- [A destination S3 bucket with a specific
  resource policy](#cp-s3-bulk "#cp-s3-bulk"). Do not configure [access control lists
  (ACLs)](../../../AmazonS3/latest/userguide/acls.md "../../../AmazonS3/latest/userguide/acls.md") on the bucket.

These steps are explained next.

### Create a new KMS key or reuse an existing KMS

key

To set up a KMS key for bulk export, you must create or reuse an existing KMS
key that is in the same AWS Region as the Amazon S3 bucket you plan on configuring
as your bulk export destination. You must allow the Amazon Connect AppIntegrations
service to perform KMS actions for the key.

Add the following statement to your **key
policy**.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`Enable AppIntegrations access to KMS key`",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "`arn:aws:iam::`111122223333`:root`"
 ],
 "Service": [
 "`app-integrations.amazonaws.com`"
 ]
 },
 "Action": [
 "kms:Encrypt*",
 "kms:Describe*",
 "kms:Decrypt*",
 "kms:GenerateDataKey*"
 ],
 "Resource": "*"
 }
 ]
}`

```

### Set up an S3 destination bucket

You must configure a new or existing bucket in the same AWS Region as the
KMS key, and configure a resource policy on the S3 bucket.

When configuring the bucket, ensure that you select **Encryption with
SSE-KMS** and use the same KMS key from the previous procedure. In
addition, do not enable ACLs on the S3 bucket.

Following is an example resource policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "`Allow AppIntegrations to write data to destination bucket`",
 "Effect": "Allow",
 "Principal": {
 "Service": [
 "app-integrations.amazonaws.com"
 ]
 },
 "Action": [
 "s3:GetObject",
 "s3:ListBucket",
 "s3:PutObject",
 "s3:PutObjectAcl"
 ],
 "Resource": [
 "arn:aws:s3:::{{`amzn-s3-demo-bucket1`}}",
 "arn:aws:s3:::{{`amzn-s3-demo-bucket2`}}/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "{{AwsAccountId}}"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:*-*:{{Region}}:{{AwsAccountId}}:data-integration/*"
 }
 }
 }
 ]
}`

```

## Step 2: Create a bulk export job

To create a bulk export job, you invoke the following Amazon Connect AppIntegrations
APIs:

1. [CreateDataIntegration](../APIReference/API_connect-app-integrations_CreateDataIntegration.md "../APIReference/API_connect-app-integrations_CreateDataIntegration.md"): This API creates an integration with the
   data source (for example, Customer Profiles).
2. [CreateDataIntegrationAssociation](../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md "../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md"): This API writes data to the
   destination (for example, an S3 bucket) by using the data source.

Following is more information about how to call these APIs.

### Create a data integration

A data integration represents the _data source_ of your
data. You can call the [CreateDataIntegration](../APIReference/API_connect-app-integrations_CreateDataIntegration.md "../APIReference/API_connect-app-integrations_CreateDataIntegration.md") API or run the [create-data-integration](../../../cli/latest/reference/appintegrations/create-data-integration.md "../../../cli/latest/reference/appintegrations/create-data-integration.md") CLI command to create a data integration.
You must provide a Customer Profiles _object type_ and
Customer Profiles _domain_.

If you want to export multiple object types, you need to create a separate
data integration for each one. For example, if you want to export both
`_profile` and `_asset` objects, you need to create
two separate data integrations.

###### Note

Any data that is ingested within the last 30 minutes may not be included
in the export.

The following code sample shows how to run the [create-data-integration](../../../cli/latest/reference/appintegrations/create-data-integration.md "../../../cli/latest/reference/appintegrations/create-data-integration.md") CLI command.

```
aws appintegrations create-data-integration \
--region "us-west-2" \
--name "`bulk-export-job-01`" \
--description "`Data integration for _profile objects`" \
--kms-key "`arn:aws:kms:us-west-2:123456789012:key/123456789012-1234-1234-123456789012`" \
--source-uri "`AmazonConnect://AppIntegrations`" \
--object-configuration '`{"CustomerProfiles":{"domainName":["my-domain-pdx"],"objectType":["_profile"]}}`'
```

The following code sample shows how to call the [CreateDataIntegration](../APIReference/API_connect-app-integrations_CreateDataIntegration.md "../APIReference/API_connect-app-integrations_CreateDataIntegration.md") API.

```
{
    "Description": "`Data integration for _profile objects`",
    "KmsKey": "`arn:aws:kms:us-west-2:123456789012:key/123456789012-1234-1234-123456789012`",
    "Name": "`unique-data-integration-name-01`",
    "SourceURI": "AmazonConnect://AppIntegrations",
    "ObjectConfiguration": {
        "CustomerProfiles": {
            "domainName": [
                "`my-domain-pdx`"
            ],
            "objectType": [
                "_profile"
            ]
        }
    }
}
```

### Create a data integration

association

A data integration association represents the destination for where you want
to export your data and a time range for choosing which data to export. You can
call the [CreateDataIntegrationAssociation](../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md "../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md") API or run the [create-data-integration-association](../../../cli/latest/reference/appintegrations/create-data-integration-association.md "../../../cli/latest/reference/appintegrations/create-data-integration-association.md") CLI command to create a data
integration. You configure the time range by using the `StartTime`
and `EndTime` properties. This time range corresponds to when objects
were last updated in Customer Profiles.

The destination S3 bucket that you specify can be just the bucket name, or it
can include an additional folder or S3 prefix where you want the data to be
exported.

###### Note

For the quota for **Concurrent bulk export jobs**, see
[Amazon Connect Customer Profiles service
quotas](amazon-connect-service-limits.md#customer-profiles-quotas "amazon-connect-service-limits.md#customer-profiles-quotas"). After a bulk export job
completes or fails, it no longer counts towards the concurrency
quota.

The following code sample shows how to run the [create-data-integration-association](../../../cli/latest/reference/appintegrations/create-data-integration-association.md "../../../cli/latest/reference/appintegrations/create-data-integration-association.md") CLI command.

```
aws appintegrations create-data-integration-association \
--region "us-west-2" \
--data-integration-identifier "`unique-data-integration-name-01`" \
--destination-uri "`s3://`amzn-s3-demo-bucket1``" \
--execution-configuration '`{"ExecutionMode": "ON_DEMAND", "OnDemandConfiguration": {"StartTime":"1715278292014", "EndTime":"1715364692014"}}`'
```

The following code sample shows how to call the [CreateDataIntegrationAssociation](../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md "../APIReference/API_connect-app-integrations_CreateDataIntegrationAssociation.md") API.

```
{
    "DataIntegrationIdentifier": "`arn:aws:app-integrations:us-west-2:123456789012:data-integration/123456789012-1234-1234-123456789012`",
    "DestinationURI": "s3://amzn-s3-demo-bucket1",
    "ExecutionConfiguration": {
        "ExecutionMode": "ON_DEMAND",
        "OnDemandConfiguration": {
            "StartTime": "1713565000004",
            "EndTime": "1713565000005"
        }
    }
}
```

## Step 3: Check the status of a bulk

export job

To view the status of your bulk export job, you can call the [ListDataIntegrationAssociations](../APIReference/API_connect-app-integrations_ListDataIntegrationAssociations.md "../APIReference/API_connect-app-integrations_ListDataIntegrationAssociations.md") API, or run the [list-data-integration-associations](../../../cli/latest/reference/appintegrations/list-data-integration-associations.md "../../../cli/latest/reference/appintegrations/list-data-integration-associations.md") CLI command.

The following code sample shows how to run the [list-data-integration-associations](../../../cli/latest/reference/appintegrations/list-data-integration-associations.md "../../../cli/latest/reference/appintegrations/list-data-integration-associations.md") CLI command.

```
aws appintegrations list-data-integration-associations \
--region "us-west-2" \
--data-integration-identifier "`unique-data-integration-name-01`"
```

## Step 4: View the exported data in S3

When the data integration association is in `IN_PROGRESS`, you will
begin to see data being copied over to your S3 bucket.

The exported data is written using the following path structure:

- {BucketNameAndFolderName}
  - {AwsAccountId}
    - {DomainName}
      - {RequestTimestamp}
        - {lStartTime}-{EndTime}
          - {ObjectTypeName}
            - <filename: uuid>

Following is an example path:

`amzn-s3-demo-bucket1/123456789012/my-domain-pdx/20240607T175023/20240101T235959-20240430T235959/_profile/123456789012-1234-1234-123456789012`

## Update the bulk export job

After the job finishes, you can update the data integration association with a
different data pull start time and data pull end time. This creates a new bulk
export job. You may want to do this if you performed a bulk export in the past and
want to export only data that was updated since the previous export. For example, if
your last bulk export job was three months ago, you can update your data integration
association with a time range of 3 months ago to today.

You can call the [UpdateDataIntegrationAssociation](../APIReference/API_connect-app-integrations_UpdateDataIntegrationAssociation.md "../APIReference/API_connect-app-integrations_UpdateDataIntegrationAssociation.md") API, or run the [update-data-integration-association](../../../cli/latest/reference/appintegrations/update-data-integration-association.md "../../../cli/latest/reference/appintegrations/update-data-integration-association.md") CLI command to update the export
job.

The following code sample shows how to run the [update-data-integration-association](../../../cli/latest/reference/appintegrations/update-data-integration-association.md "../../../cli/latest/reference/appintegrations/update-data-integration-association.md") CLI command.

```
aws appintegrations update-data-integration-association \
--region "us-west-2" \
--data-integration-identifier "`unique-data-integration-name-01`" \
--data-integration-association-identifier "`arn:aws:app-integrations:us-west-2:123456789012:data-integration-association/123456789012-1234-1234-123456789012/123456789012-1234-1234-123456789012`" \
--execution-configuration '`{"ExecutionMode": "ON_DEMAND", "OnDemandConfiguration": {"StartTime":"1715278292014", "EndTime":"1715364692014"}}`'
```

## Delete or cancel the bulk export job - not

supported

You cannot delete or cancel bulk export. After an export job finishes, it no
longer counts toward your export quota.

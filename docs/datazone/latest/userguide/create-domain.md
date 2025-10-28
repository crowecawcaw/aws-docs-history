# Create Amazon DataZone domains

###### Note

If you are using Amazon DataZone with AWS Identity Center to provide access to SSO
users and groups, then currently your Amazon DataZone domain must be in the same AWS
Region as your AWS Identity Center instance.

Amazon DataZone, a domain is an organizing entity for connecting together your assets,
users, and their projects. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

To create an Amazon DataZone domain, you must assume an IAM role in the account with
administrative permissions. [Configure the IAM permissions required to use the
Amazon DataZone management console](create-iam-roles.md "create-iam-roles.md") to obtain the minimum permissions necessary to
create a domain.

Additional IAM roles are needed by Amazon DataZone to perform actions on behalf of domain
users with a default configuration. You can create these IAM roles in advance, or have
Amazon DataZone create them for you. If you want Amazon DataZone to create these IAM roles for you
during the domain creation process, then for domain creation you must assume an IAM role
with role creation permissions. See [Create a custom policy for IAM
permissions to enable the Amazon DataZone service console simplified role creation](create-iam-roles.md#create-custom-to-manage-EZCRZ "create-iam-roles.md#create-custom-to-manage-EZCRZ") . Depending on your domain creation
choices, Amazon DataZone will create up to four new IAM roles for you:
**AmazonDataZoneDomainExecutionRole**,
**AmazonDataZoneGlueManageAccessRole**,
**AmazonDataZoneRedshiftManageAccessRole**, and
**AmazonDataZoneProvisioningRole**.

Complete the following procedure to create an Amazon DataZone domain.

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **Create domain** and provide values for the following
   fields:
   - **Name** - specify a friendly name for the domain.
     Once the domain is created this name cannot be changed.
   - **Description** - (optional) specify a domain
     description.
   - \***\*Data encryption\*\*** - your
     Amazon DataZone domain, metadata, and reporting data is encrypted by the
     AWS Key Management Service (KMS) using a key specific to your
     Amazon DataZone. Use this field to specify whether you want to use an AWS
     owned key or choose a different AWS KMS key.

   For more information about using customer managed keys, see [Data encryption at rest for Amazon DataZone](encryption-rest-datazone.md "encryption-rest-datazone.md"). If you use your own KMS
   key for data encryption, you must include the following statement in
   your default [AmazonDataZoneDomainExecutionRole](AmazonDataZoneDomainExecutionRole.md "AmazonDataZoneDomainExecutionRole.md").

   JSON

   ```
   `{
    "Version":"2012-10-17",
    "Statement": [
    {
    "Sid": "Statement1",
    "Effect": "Allow",
    "Action": [
    "kms:Decrypt",
    "kms:DescribeKey",
    "kms:GenerateDataKey"
    ],
    "Resource": [
    "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    ]
    }
    ]
   }`

   ```

   - **Service access** - choose whether to have
     Amazon DataZone create and use a new **DomainExecutionRole**
     for you, or choose an existing IAM role.
   - **Quick setup** - (optional) check this box to get
     started faster by having Amazon DataZone set-up your account for data
     consumption and publishing. Amazon DataZone will create three IAM roles for
     provisioning, ingesting, and managing access to AWS Glue and Amazon
     Redshift resources, create a new Amazon S3 bucket, create an
     administrative Amazon DataZone project, and create environment profiles for
     the data lake and data warehouse default blueprints.
   - Tags - (optional) specify AWS tags (key and value pairs)
     for the domain.
   - Once the domain is successfully created, your browser should be
     refreshed to display your new Amazon DataZone domain’s details page.

# DynamoDB zero-ETL integration with Amazon Redshift

Amazon DynamoDB zero-ETL integration with Amazon Redshift enables seamless analytics on
DynamoDB data without any coding. This fully-managed feature automatically replicates DynamoDB
tables into an Amazon Redshift database so users can run SQL queries and analytics on their DynamoDB
data without having to set up complex ETL processes. The integration works by
replicating data from the DynamoDB table to the Amazon Redshift database.

To set up the integration, simply specify a DynamoDB table as the source and an Amazon Redshift
database as the target. On activation, the integration exports the full DynamoDB table to
populate the Amazon Redshift database. The time it takes for this initial process to complete
depends on the DynamoDB table size. The zero-ETL integration then incrementally replicates
updates from DynamoDB to Amazon Redshift every 15-30 minutes using DynamoDB incremental exports. This
means the replicated DynamoDB data in Amazon Redshift is kept up-to-date automatically.

Once configured, users can analyze the DynamoDB data in Amazon Redshift using standard SQL clients
and tools, without impacting DynamoDB table performance. By eliminating cumbersome ETL,
this zero-ETL integration provides a fast, easy way to unlock insights from DynamoDB
through Amazon Redshift analytics and machine learning capabilities.

###### Topics

- [Prerequisites before creating a DynamoDB zero-ETL integration with Amazon Redshift](#RedshiftforDynamoDB-zero-etl-prereqs "#RedshiftforDynamoDB-zero-etl-prereqs")
- [Limitations when using DynamoDB zero-ETL integrations with Amazon Redshift](#RedshiftforDynamoDB-zero-etl-limitations "#RedshiftforDynamoDB-zero-etl-limitations")
- [Creating a DynamoDB zero-ETL integration with Amazon Redshift](RedshiftforDynamoDB-zero-etl-getting-started.md "RedshiftforDynamoDB-zero-etl-getting-started.md")
- [Viewing DynamoDB zero-ETL integrations with Amazon Redshift](RedshiftforDynamoDB-zero-etl-viewing.md "RedshiftforDynamoDB-zero-etl-viewing.md")
- [Deleting DynamoDB zero-ETL integrations with Amazon Redshift](RedshiftforDynamoDB-zero-etl-deleting.md "RedshiftforDynamoDB-zero-etl-deleting.md")

## Prerequisites before creating a DynamoDB zero-ETL integration with Amazon Redshift

1. You must have your source DynamoDB table and target Amazon Redshift cluster created
   before creating an integration. This information is covered in [Step 1: Configuring a source DynamoDB table](RedshiftforDynamoDB-zero-etl-getting-started.md#RedshiftforDynamoDB-zero-etl-getting-started-configuring "RedshiftforDynamoDB-zero-etl-getting-started.md#RedshiftforDynamoDB-zero-etl-getting-started-configuring") and [Step 2: Creating an Amazon Redshift data warehouse](RedshiftforDynamoDB-zero-etl-getting-started.md#RedshiftforDynamoDB-zero-etl-getting-started-creating "RedshiftforDynamoDB-zero-etl-getting-started.md#RedshiftforDynamoDB-zero-etl-getting-started-creating").
2. A zero-ETL integration between Amazon DynamoDB and Amazon Redshift requires your
   source DynamoDB table to have [Point-in-time recovery (PITR)](Point-in-time-recovery.md "Point-in-time-recovery.md") enabled.
3. For **resource-based policies**, if you
   create the integration where your DynamoDB table and Amazon Redshift data warehouse are in
   the same account, you can use the **Fix it for me** option
   during the create integration step to automatically apply the required
   resource policies to both DynamoDB and Amazon Redshift.

If you create an integration where your DynamoDB table and Amazon Redshift data
warehouse are in different AWS accounts, you will need to apply the
following resource policy on your DynamoDB table.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "StatementthatallowsAmazonRedshiftservicetoDescribeTableandExportTable",
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": [
 "dynamodb:ExportTableToPointInTime",
 "dynamodb:DescribeTable"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:redshift:us-east-1:111122223333:integration:*"
 }
 }
 },
 {
 "Sid": "StatementthatallowsAmazonRedshiftservicetoDescribeTableandExportTable",
 "Effect": "Allow",
 "Principal": {
 "Service": "redshift.amazonaws.com"
 },
 "Action": "dynamodb:DescribeExport",
 "Resource": "arn:aws:dynamodb:us-east-1:111122223333:table/table-name/export/*",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "111122223333"
 },
 "ArnEquals": {
 "aws:SourceArn": "arn:aws:redshift:us-east-1:111122223333:integration:*"
 }
 }
 }
 ]
}`

```

You may also need to
configure the resource policy on your Amazon Redshift data warehouse. For more
information, see [Configure authorization using the Amazon Redshift API](../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.resource-policies "../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.resource-policies"). 4. ###### For Identity-based policies:

    1. The user creating the integration requires an identity-based
     policy that authorizes the following actions:
     `GetResourcePolicy`, `PutResourcePolicy`,
     and `UpdateContinuousBackups`.


    ###### Note

     The following policy examples will show the resource as
     `arn:aws:redshift{-serverless}`. This is an
     example to show that the arn can be either
     `arn:aws:redshift` or
     `arn:aws:redshift-serverless` depending on if
     your namespace is an Amazon Redshift cluster or Amazon Redshift Serverless namespace.




    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "dynamodb:ListTables"
     ],
     "Resource": "*"
     },
     {
     "Effect": "Allow",
     "Action": [
     "dynamodb:GetResourcePolicy",
     "dynamodb:PutResourcePolicy",
     "dynamodb:UpdateContinuousBackups"
     ],
     "Resource": [
     "arn:aws:dynamodb:`us-east-1`:`111122223333`:table/`table-name`"
     ]
     },
     {
     "Sid": "AllowRedshiftDescribeIntegration",
     "Effect": "Allow",
     "Action": [
     "redshift:DescribeIntegrations"
     ],
     "Resource": "*"
     },
     {
     "Sid": "AllowRedshiftCreateIntegration",
     "Effect": "Allow",
     "Action": "redshift:CreateIntegration",
     "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:integration:*"
     },
     {
     "Sid": "AllowRedshiftModifyDeleteIntegration",
     "Effect": "Allow",
     "Action": [
     "redshift:ModifyIntegration",
     "redshift:DeleteIntegration"
     ],
     "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:integration:`uuid`"
     },
     {
     "Sid": "AllowRedshiftCreateInboundIntegration",
     "Effect": "Allow",
     "Action": "redshift:CreateInboundIntegration",
     "Resource": "arn:aws:redshift:`us-east-1`:`111122223333`:namespace:`uuid`"
     }
     ]
    }`

    ```
    2. The user responsible for configuring the destination Amazon Redshift
     namespace requires an identity-based policy that authorizes the
     following actions: `PutResourcePolicy`,
     `DeleteResourcePolicy`, and
     `GetResourcePolicy`.



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Action": [
     "redshift:PutResourcePolicy",
     "redshift:DeleteResourcePolicy",
     "redshift:GetResourcePolicy"
     ],
     "Resource": [
     "arn:aws:redshift:`us-east-1`:`111122223333`:cluster:`cluster-name`"
     ]
     },
     {
     "Effect": "Allow",
     "Action": [
     "redshift:DescribeInboundIntegrations"
     ],
     "Resource": [
     "arn:aws:redshift:`us-east-1`:`111122223333`:cluster:`cluster-name`"
     ]
     }
     ]
    }`

    ```

5. ###### Encryption key permissions

If the source DynamoDB table is encrypted using customer managed AWS KMS
key, you will need to add the following policy on your KMS key. This
policy allows Amazon Redshift to be able to export data from your encrypted table
using your KMS key.

```
{
    "Sid": "Statement to allow Amazon Redshift service to perform Decrypt operation on the source DynamoDB Table",
    "Effect": "Allow",
    "Principal": {
        "Service": [
            "redshift.amazonaws.com"
        ]
    },
    "Action": "kms:Decrypt",
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "aws:SourceAccount": "<account>"
        },
        "ArnEquals": {
            "aws:SourceArn": "arn:aws:redshift:<region>:<account>:integration:*"
        }
    }
}
```

You can also follow the steps on [Getting started with zero-ETL integrations](../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam "../../../redshift/latest/mgmt/zero-etl-using.md#zero-etl-using.redshift-iam") in the Amazon Redshift management
guide to configure the permissions of the Amazon Redshift namespace.

## Limitations when using DynamoDB zero-ETL integrations with Amazon Redshift

The following general limitations apply to the current release of this
integration. These limitations can change in subsequent releases.

###### Note

In addition to the limitations below, also review the general considerations
when using zero-ETL integrations see [Considerations when
using zero-ETL integrations with Amazon Redshift](../../../redshift/latest/mgmt/zero-etl.md "../../../redshift/latest/mgmt/zero-etl.md") in the
_Amazon Redshift Management Guide_.

- The DynamoDB table and Amazon Redshift cluster need to be in the same Region.
- The source DynamoDB table must be encrypted with either an Amazon-owned or
  Customer-managed AWS KMS key. Amazon managed encryption is not supported for
  the source DynamoDB table.

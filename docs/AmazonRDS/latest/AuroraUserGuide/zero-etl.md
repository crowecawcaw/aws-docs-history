# Creating Aurora zero-ETL integrations with an Amazon SageMaker lakehouse

When you create an Aurora zero-ETL integration with an Amazon SageMaker lakehouse, you specify the source Aurora DB cluster and the target AWS Glue managed catalog. You can also customize encryption settings and add tags. Aurora creates an
integration between the source DB cluster and its target. Once the integration is active, any data
that you insert into the source DB cluster will be replicated into the configured target.

## Prerequisites

Before you create a zero-ETL integration with an Amazon SageMaker lakehouse, you must create a source DB cluster and a target AWS Glue managed catalog. You also must allow replication
into the catalog by adding the DB cluster as an authorized
integration source.

For instructions to complete each of these steps, see [Getting started with Aurora zero-ETL integrations](zero-etl.md "zero-etl.md").

## Required permissions

Certain IAM permissions are required to create a zero-ETL integration with an Amazon SageMaker lakehouse. At minimum, you
need permissions to perform the following actions:

- Create zero-ETL integrations for the source Aurora DB cluster.
- View and delete all zero-ETL integrations.
- Create inbound integrations into the target AWS Glue managed catalog.
- Access Amazon S3 buckets used by the AWS Glue managed catalog.
- Use AWS KMS keys for encryption if custom encryption is configured.
- Register resources with Lake Formation.
- Put resource policy on the AWS Glue managed catalog to authorize inbound integrations.

The following sample policy demonstrates the [least privilege
permissions](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") required to create and manage integrations with an Amazon SageMaker lakehouse. You might not need
these exact permissions if your user or role has broader permissions, such as an
`AdministratorAccess` managed policy.

Additionally, you must configure a resource policy on the target AWS Glue managed catalog to authorize inbound integrations. Use the following AWS CLI command to apply the resource policy.

```
aws glue put-resource-policy \
      --policy-in-json  '{
    "Version": "2012-10-17",
    "Statement": [{
        "Effect": "Allow",
        "Principal": {
            "Service": "glue.amazonaws.com"
        },
        "Action": [
            "glue:AuthorizeInboundIntegration"
        ],
        "Resource": ["arn:aws:glue:`region`:`account_id`:catalog/`catalog_name`"],
        "Condition": {
            "StringEquals": {
                "aws:SourceArn": "arn:aws:rds:`region`:`account_id`:db:`source_name`"
            }
        }
    },
    {
        "Effect": "Allow",
        "Principal": {
            "AWS": "`account_id`"
        },
        "Action": ["glue:CreateInboundIntegration"],
        "Resource": ["arn:aws:glue:`region`:`account_id`:catalog/`catalog_name`"]
    }
    ]
}' \
      --region `region`
```

###### Note

Glue catalog Amazon Resource Names (ARNs) have the following format:

- Glue catalog – `arn:aws:**glue**:{region}:{account-id}:catalog**/**`catalog-name``

### Choosing a target AWS Glue managed catalog in a different account

If you plan to specify a target AWS Glue managed catalog that's in another AWS account,
you must create a role that allows users in the current account to access resources
in the target account. For more information, see [Providing access
to an IAM user in another AWS account that you own](../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md "../../../IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.md").

The role must have the following permissions, which allow the user to view
available AWS Glue catalogs in the target account.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "glue:GetCatalog"
 ],
 "Resource":[
 "*"
 ]
 }
 ]
}`

```

The role must have the following trust policy, which specifies the target account
ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Principal":{
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action":"sts:AssumeRole"
 }
 ]
}`

```

For instructions to create the role, see [Creating a role using custom trust policies](../../../IAM/latest/UserGuide/id_roles_create_for-custom.md "../../../IAM/latest/UserGuide/id_roles_create_for-custom.md").

## Creating zero-ETL integrations with an Amazon SageMaker lakehouse

You can create a zero-ETL integration with an Amazon SageMaker lakehouse using the AWS Management Console, the AWS CLI, or the RDS API.

###### Important

Zero-ETL integrations with an Amazon SageMaker lakehouse do not support refresh or resync operations. If you encounter issues with an integration after creation, you must delete the integration and create a new one.

###### To create a zero-ETL integration with an Amazon SageMaker lakehouse

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the left navigation pane, choose **Zero-ETL integrations**.
3. Choose **Create zero-ETL integration**.
4. For **Integration identifier**, enter a name for the
   integration. The name can have up to 63 alphanumeric characters and can
   include hyphens.
5. Choose **Next**.
6. For **Source**, select the Aurora DB cluster where
   the data will originate from.

###### Note

RDS notifies you if the DB cluster parameters aren't configured correctly. If you
receive this message, you can either choose **Fix it for
me**, or configure them manually. For instructions to
fix them manually, see [Step 1: Create a custom DB cluster parameter group](zero-etl.md#zero-etl.parameters "zero-etl.md#zero-etl.parameters").

Modifying DB cluster
parameters requires a reboot. Before you can create the integration,
the reboot must be complete and the new parameter values must be
successfully applied to the cluster. 7. (Optional) Select **Customize data filtering
options** and add data filters to your integration. You can
use data filters to define the scope of replication to the target Amazon SageMaker lakehouse. For more information, see [Data filtering for Aurora zero-ETL integrations](zero-etl.md "zero-etl.md"). 8. Once your source DB cluster is
successfully configured, choose **Next**. 9. For **Target**, do the following:

    1. (Optional) To use a different AWS account for the Amazon SageMaker lakehouse target, choose **Specify a
     different account**. Then, enter the ARN of an
     IAM role with permissions to display your AWS Glue catalogs. For
     instructions to create the IAM role, see [Choosing a target AWS Glue managed catalog in a different account](#zero-etl.create-permissions-cross-account-smlh "#zero-etl.create-permissions-cross-account-smlh").
    2. For **AWS Glue catalog**, select the target for replicated data from the
     source DB cluster. You can choose an existing
     AWS Glue managed catalog as the target.
    3. The target IAM role needs describe permissions on the target catalog and must have the following permissions:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "VisualEditor0",
     "Effect": "Allow",
     "Action": "glue:GetCatalog",
     "Resource": [
     "arn:aws:glue:`us-east-1`:`111122223333`:catalog/*",
     "arn:aws:glue:`us-east-1`:`111122223333`:catalog"
     ]
     }
     ]
    }`

    ```





    The target IAM role must have the following trust relationship:



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "Service": "glue.amazonaws.com"
     },
     "Action": "sts:AssumeRole"
     }
     ]
    }`

    ```
    4. You must grant the target IAM role describe permissions for the target AWS Glue managed catalog with the Lake Formation administrator role created in [Step 3b: Create an AWS Glue catalog for
     Amazon SageMaker AI zero-ETL integration](zero-etl.md#zero-etl-setting-up.sagemaker "zero-etl.md#zero-etl-setting-up.sagemaker").

###### Note

RDS notifies you if the resource policy or configuration settings
for the specified AWS Glue managed catalog aren't configured
correctly. If you receive this message, you can either choose
**Fix it for me**, or configure them manually.

If your selected source and target are in different
AWS accounts, then Amazon RDS cannot fix these settings for you. You
must navigate to the other account and fix them manually in
SageMaker Unified Studio. 10. Once your target AWS Glue managed catalog is configured correctly, choose
**Next**. 11. (Optional) For **Tags**, add one or more tags to the
integration. For more information, see [Tagging Amazon Aurora and Amazon RDS resources](USER_Tagging.md "USER_Tagging.md"). 12. For **Encryption**, specify how you want your
integration to be encrypted. By default, RDS encrypts all integrations with
an AWS owned key. To choose a customer managed key instead, enable
**Customize encryption settings** and choose a
KMS key to use for encryption. For more information, see [Encrypting Amazon Aurora
resources](Overview.md "Overview.md").

Optionally, add an encryption context. For more information, see
[Encryption
context](../../../kms/latest/developerguide/concepts.md#encrypt_context "../../../kms/latest/developerguide/concepts.md#encrypt_context") in the _AWS Key Management Service Developer
Guide_.

###### Note

Amazon RDS adds the following encryption context pairs in addition to
any that you add:

    * `aws:glue:integration:arn` -
     `IntegrationArn`
    * `aws:servicename:id` -
     `glue`This reduces the overall number of pairs that you can add from 8

to 6, and contributes to the overall character limit of the grant
constraint. For more information, see [Using grant constraints](../../../kms/latest/developerguide/create-grant-overview.md#grant-constraints "../../../kms/latest/developerguide/create-grant-overview.md#grant-constraints") in the _AWS Key Management Service Developer Guide_. 13. Choose **Next**. 14. Review your integration settings and choose **Create zero-ETL integration**.

If creation fails, see [Troubleshooting Aurora zero-ETL integrations](zero-etl.md "zero-etl.md") for
troubleshooting steps.
The integration has a status of `Creating` while it's being created, and the
target Amazon SageMaker lakehouse has a status of `Modifying`. During this time, you
can't query the catalog or make any configuration changes on it.

When the integration is successfully created, the status of the integration and the target
Amazon SageMaker lakehouse both change to `Active`.

To prepare a target AWS Glue managed catalog for zero-ETL integration using the AWS CLI, you must first use the [create-integration-resource-property](../../../cli/latest/reference/rds/create-integration.md "../../../cli/latest/reference/rds/create-integration.md")
command with the following options:

- `--resource-arn` – Specify the ARN of the AWS Glue managed catalog
  that will be the target for the integration.
- `--target-processing-properties` – Specify the
  ARN of the IAM role to access the target AWS Glue managed catalog

```
aws glue create-integration-resource-property --region us-east-1
 --resource-arn arn:aws:glue:`region`:`account_id`:catalog/`catalog_name` \
 --target-processing-properties '{"RoleArn" : "arn:aws:iam::`account_id`:role/TargetIamRole"}'
```

To create a zero-ETL integration with an Amazon SageMaker lakehouse using the AWS CLI, use the [create-integration](../../../cli/latest/reference/rds/create-integration.md "../../../cli/latest/reference/rds/create-integration.md")
command with the following options:

- `--integration-name` – Specify a name for the
  integration.
- `--source-arn` – Specify the ARN of the Aurora DB cluster that will be the source for the
  integration.
- `--target-arn` – Specify the ARN of the AWS Glue managed catalog that will be the target for the integration.
  For Linux, macOS, or Unix:

```
aws rds create-integration \
    --integration-name `my-sagemaker-integration` \
    --source-arn arn:aws:rds:`{region}`:`{account-id}`:`cluster:my-db` \
    --target-arn arn:aws:glue:`{region}`:`{account-id}`:catalog**/**`catalog-name`
```

For Windows:

```
aws rds create-integration ^
    --integration-name `my-sagemaker-integration` ^
    --source-arn arn:aws:rds:`{region}`:`{account-id}`:`cluster:my-db` ^
    --target-arn arn:aws:glue:`{region}`:`{account-id}`:catalog**/**`catalog-name`
```

To create a zero-ETL integration with Amazon SageMaker by using the Amazon RDS API, use the [`CreateIntegration`](../APIReference/API_CreateIntegration.md "../APIReference/API_CreateIntegration.md") operation with the following
parameters:

###### Note

Catalog names are limited to 19 characters. Ensure your IntegrationName parameter meets this requirement if it will be used as a catalog name.

- `IntegrationName` – Specify a name for the
  integration.
- `SourceArn` – Specify the ARN of the Aurora DB cluster that will be the source for the
  integration.
- `TargetArn` – Specify the ARN of the AWS Glue managed catalog that will be the target for the integration.

## Encrypting integrations with a

customer managed key

If you specify a custom KMS key rather than an AWS owned key when you create an
integration with Amazon SageMaker, the key policy must provide the SageMaker Unified Studio service principal access to the
`CreateGrant` action. In addition, it must allow the current user to
perform to the `DescribeKey` and `CreateGrant` actions.

The following sample policy demonstrates how to provide the required permissions in
the key policy. It includes context keys to further reduce the scope of
permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Id": "Key policy",
 "Statement": [
 {
 "Sid": "EnablesIAMUserPermissions",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:root"
 },
 "Action": "kms:*",
 "Resource": "*"
 },
 {
 "Sid": "GlueServicePrincipalAddGrant",
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:`{context-key}`":"`{context-value}`"
 },
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "GenerateDataKey",
 "CreateGrant"
 ]
 }
 }
 },
 {
 "Sid": "AllowsCurrentUserRoleAddGrantKMSKey",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`{role-name}`"
 },
 "Action": "kms:CreateGrant",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "kms:EncryptionContext:`{context-key}`":"`{context-value}`",
 "kms:ViaService": "rds.us-east-1.amazonaws.com"
 },
 "ForAllValues:StringEquals": {
 "kms:GrantOperations": [
 "Decrypt",
 "GenerateDataKey",
 "CreateGrant"
 ]
 }
 }
 },
 {
 "Sid": "AllowsCurrentUserRoleRetrieveKMSKeyInformation",
 "Effect": "Allow",
 "Principal": {
 "AWS": "arn:aws:iam::`111122223333`:role/`{role-name}`"
 },
 "Action": "kms:DescribeKey",
 "Resource": "*"
 }
 ]
}`

```

For more information, see [Creating a key policy](../../../kms/latest/developerguide/key-policy-overview.md "../../../kms/latest/developerguide/key-policy-overview.md") in the _AWS Key Management Service
Developer Guide_.

## Next steps

After you successfully create a zero-ETL integration with Amazon SageMaker, you can start adding data to the
source Aurora DB cluster and querying it in your Amazon SageMaker lakehouse. The data will be automatically
replicated and made available for analytics and machine learning workloads.

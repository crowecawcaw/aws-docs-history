

# Creating Aurora zero-ETL integrations with Amazon Redshift
<a name="zero-etl.creating"></a>

When you create an Aurora zero-ETL integration, you specify the source Aurora DB cluster and the target Amazon Redshift data warehouse. You can also customize encryption settings and add tags. Aurora creates an integration between the source DB cluster and its target. Once the integration is active, any data that you insert into the source DB cluster will be replicated into the configured Amazon Redshift target.

## Prerequisites
<a name="zero-etl.create-prereqs"></a>

Before you create a zero-ETL integration, you must create a source DB cluster and a target Amazon Redshift data warehouse. You also must allow replication into the data warehouse by adding the DB cluster as an authorized integration source.

For instructions to complete each of these steps, see [Getting started with Aurora zero-ETL integrations](zero-etl.setting-up.md).

## Required permissions
<a name="zero-etl.create-permissions"></a>

Certain IAM permissions are required to create a zero-ETL integration. At minimum, you need permissions to perform the following actions:
+ Create zero-ETL integrations for the source Aurora DB cluster.
+ View and delete all zero-ETL integrations.
+ Create inbound integrations into the target data warehouse.

The following sample policies demonstrate the [least privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) required to create and manage integrations. You might not need these exact permissions if your user or role has broader permissions, such as an `AdministratorAccess` managed policy.

**Note**  
Redshift Amazon Resource Names (ARNs) have the following format. Note the use of a forward slash `(/`) rather than a colon (`:`) before the serverless namespace UUID.  
Provisioned cluster – `arn:aws:redshift:{region}:{account-id}:namespace:{{namespace-uuid}}`
Serverless – `arn:aws:redshift-serverless:{region}:{account-id}:namespace/{{namespace-uuid}}`

### Sample policy for Redshift target
<a name="zero-etl.create-sample-policy"></a>

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "CreateIntegration",
      "Effect": "Allow",
      "Action": [
        "rds:CreateIntegration"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{123456789012}}:db:{{source-db}}",
        "arn:aws:rds:{{us-east-1}}:{{123456789012}}:integration:*"
      ]
    },
    {
      "Sid": "DescribeIntegrationDetails",
      "Effect": "Allow",
      "Action": [
        "rds:DescribeIntegrations"
      ],
      "Resource": [
      "arn:aws:rds:{{us-east-1}}:{{123456789012}}:integration:*"
  ]
    },
    {
      "Sid": "ChangeIntegrationDetails",
      "Effect": "Allow",
      "Action": [
        "rds:DeleteIntegration",
        "rds:ModifyIntegration"
      ],
      "Resource": [
        "arn:aws:rds:{{us-east-1}}:{{123456789012}}:integration:*"
      ]
    },
    {
      "Sid": "AllowRedShiftIntegration",
      "Effect": "Allow",
      "Action": [
        "redshift:CreateInboundIntegration"
      ],
      "Resource": [
        "arn:aws:redshift:{{us-east-1}}:{{123456789012}}:namespace:{{namespace-uuid}}"
      ]
    }
  ]
}
```

------

### Choosing a target data warehouse in a different account
<a name="zero-etl.create-permissions-cross-account"></a>

If you plan to specify a target Amazon Redshift data warehouse that's in another AWS account, you must create a role that allows users in the current account to access resources in the target account. For more information, see [Providing access to an IAM user in another AWS account that you own](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_common-scenarios_aws-accounts.html).

The role must have the following permissions, which allow the user to view available Amazon Redshift provisioned clusters and Redshift Serverless namespaces in the target account.

#### Required permissions and trust policy
<a name="zero-etl.cross-account-sample-policy"></a>

------
#### [ JSON ]

****  

```
{
   "Version":"2012-10-17",		 	 	 
   "Statement":[
      {
         "Effect":"Allow",
         "Action":[
            "redshift:DescribeClusters",
            "redshift-serverless:ListNamespaces"
         ],
         "Resource":[
            "*"
         ]
      }
   ]
}
```

------

The role must have the following trust policy, which specifies the target account ID.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

For instructions to create the role, see [Creating a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html).

## Creating zero-ETL integrations
<a name="zero-etl.create"></a>

You can create a zero-ETL integration using the AWS Management Console, the AWS CLI, or the RDS API.

**Important**  
zero-ETL integrations do not support refresh or resync operations. If you encounter issues with an integration after creation, you must delete the integration and create a new one.

### RDS console
<a name="zero-etl.create-console"></a>

**To create a zero-ETL integration**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the left navigation pane, choose **Zero-ETL integrations**.

1. Choose **Create zero-ETL integration**.

1. For **Integration identifier**, enter a name for the integration. The name can have up to 63 alphanumeric characters and can include hyphens.
**Important**  
Catalog names are limited to 19 characters in length. Ensure your integration identifier meets this requirement if it will be used as a catalog name.

1. Choose **Next**.

1. For **Source**, select the Aurora DB cluster where the data will originate from.
**Note**  
RDS notifies you if the DB cluster parameters aren't configured correctly. If you receive this message, you can either choose **Fix it for me**, or configure them manually. For instructions to fix them manually, see [Step 1: Create a custom DB cluster parameter group](zero-etl.setting-up.md#zero-etl.parameters).  
Modifying DB cluster parameters requires a reboot. Before you can create the integration, the reboot must be complete and the new parameter values must be successfully applied to the cluster.

1. (Optional) Select **Customize data filtering options** and add data filters to your integration. You can use data filters to define the scope of replication to the target data warehouse. For more information, see [Data filtering for Aurora zero-ETL integrations](zero-etl.filtering.md).

1. Once your source DB cluster is successfully configured, choose **Next**.

1. For **Target**, do the following:

   1. (Optional) To use a different AWS account for the Amazon Redshift target, choose **Specify a different account**. Then, enter the ARN of an IAM role with permissions to display your data warehouses. For instructions to create the IAM role, see [Choosing a target data warehouse in a different account](#zero-etl.create-permissions-cross-account).

   1. For **Amazon Redshift data warehouse**, select the target for replicated data from the source DB cluster. You can choose a provisioned Amazon Redshift *cluster* or a Redshift Serverless *namespace* as the target.
**Note**  
RDS notifies you if the resource policy or case sensitivity settings for the specified data warehouse aren't configured correctly. If you receive this message, you can either choose **Fix it for me**, or configure them manually. For instructions to fix them manually, see [Turn on case sensitivity for your data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html#zero-etl-setting-up.case-sensitivity) and [Configure authorization for your data warehouse](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.setting-up.html#zero-etl-using.redshift-iam) in the *Amazon Redshift Management Guide*.  
Modifying case sensitivity for a *provisioned* Redshift cluster requires a reboot. Before you can create the integration, the reboot must be complete and the new parameter value must be successfully applied to the cluster.  
If your selected source and target are in different AWS accounts, then Amazon RDS cannot fix these settings for you. You must navigate to the other account and fix them manually in Amazon Redshift.

1. Once your target data warehouse is configured correctly, choose **Next**.

1. (Optional) For **Tags**, add one or more tags to the integration. For more information, see [Tagging Amazon Aurora andAmazon RDS resources](USER_Tagging.md).

1. For **Encryption**, specify how you want your integration to be encrypted. By default, RDS encrypts all integrations with an AWS owned key. To choose a customer managed key instead, enable **Customize encryption settings** and choose a KMS key to use for encryption. For more information, see [Encrypting Amazon Aurora resources](Overview.Encryption.md).

   Optionally, add an encryption context. For more information, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the *AWS Key Management Service Developer Guide*.
**Note**  
Amazon RDS adds the following encryption context pairs in addition to any that you add:  
`aws:redshift:integration:arn` - `IntegrationArn`
`aws:servicename:id` - `Redshift`
This reduces the overall number of pairs that you can add from 8 to 6, and contributes to the overall character limit of the grant constraint. For more information, see [Using grant constraints](https://docs.aws.amazon.com/kms/latest/developerguide/create-grant-overview.html#grant-constraints) in the *AWS Key Management Service Developer Guide*.

1. Choose **Next**.

1. Review your integration settings and choose **Create zero-ETL integration**.

   If creation fails, see [I can't create a zero-ETL integration](zero-etl.troubleshooting.md#zero-etl.troubleshooting.creation) for troubleshooting steps.

The integration has a status of `Creating` while it's being created, and the target Amazon Redshift data warehouse has a status of `Modifying`. During this time, you can't query the data warehouse or make any configuration changes on it.

When the integration is successfully created, the status of the integration and the target Amazon Redshift data warehouse both change to `Active`.

### AWS CLI
<a name="zero-etl.create-cli"></a>

To create a zero-ETL integration using the AWS CLI, use the [create-integration](https://docs.aws.amazon.com/cli/latest/reference/rds/create-integration.html) command with the following options:

**Note**  
Remember that catalog names are limited to 19 characters. Choose your integration name accordingly if it will be used as a catalog name.
+ `--integration-name` – Specify a name for the integration.
+ `--source-arn` – Specify the ARN of the Aurora DB cluster that will be the source for the integration.
+ `--target-arn` – Specify the ARN of the Amazon Redshift data warehouse that will be the target for the integration.

**Example**  
For Linux, macOS, or Unix:  

```
aws rds create-integration \
    --integration-name {{my-integration}} \
    --source-arn arn:aws:rds:{{{region}}}:{{{account-id}}}:{{my-db}} \
    --target-arn arn:aws:redshift:{{{region}}}:{{{account-id}}}:namespace:{{namespace-uuid}}
```
For Windows:  

```
aws rds create-integration ^
    --integration-name {{my-integration}} ^
    --source-arn arn:aws:rds:{{{region}}}:{{{account-id}}}:{{my-db}} ^
    --target-arn arn:aws:redshift:{{{region}}}:{{{account-id}}}:namespace:{{namespace-uuid}}
```

### RDS API
<a name="zero-etl.create-api"></a>

To create a zero-ETL integration by using the Amazon RDS API, use the [`CreateIntegration`](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_CreateIntegration.html) operation with the following parameters:

**Note**  
Catalog names are limited to 19 characters. Ensure your IntegrationName parameter meets this requirement if it will be used as a catalog name.
+ `IntegrationName` – Specify a name for the integration.
+ `SourceArn` – Specify the ARN of the Aurora DB cluster that will be the source for the integration.
+ `TargetArn` – Specify the ARN of the Amazon Redshift data warehouse that will be the target for the integration.

## Encrypting integrations with a customer managed key
<a name="zero-etl.create-encrypt"></a>

If you specify a custom KMS key rather than an AWS owned key when you create an integration, the key policy must provide the Amazon Redshift service principal access to the `CreateGrant` action. In addition, it must allow the current user to perform to the `DescribeKey` and `CreateGrant` actions.

The following sample policy demonstrates how to provide the required permissions in the key policy. It includes context keys to further reduce the scope of permissions.

### Sample key policy
<a name="zero-etl.kms-sample-policy"></a>

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Id": "Key policy",
    "Statement": [
        {
            "Sid": "Enables IAM user permissions",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:root"
            },
            "Action": "kms:*",
            "Resource": "*"
        },
        {
            "Sid": "Allows the Redshift service principal to add a grant to a KMS key",
            "Effect": "Allow",
            "Principal": {
                "Service": "redshift.amazonaws.com"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:{{{context-key}}}": "{{{context-value}}}"
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
            "Sid": "Allows the current user or role to add a grant to a KMS key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{{role-name}}}"
            },
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:EncryptionContext:{{{context-key}}}": "{{{context-value}}}",
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
            "Sid": "Allows the current uer or role to retrieve information about a KMS key",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::{{111122223333}}:role/{{{role-name}}}"
            },
            "Action": "kms:DescribeKey",
            "Resource": "*"
        }
    ]
}
```

------

For more information, see [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) in the *AWS Key Management Service Developer Guide*.

## Next steps
<a name="zero-etl.create-next"></a>

After you successfully create a zero-ETL integration, you must create a destination database within your target Amazon Redshift cluster or workgroup. Then, you can start adding data to the source Aurora DB cluster and querying it in Amazon Redshift. For instructions, see [Creating destination databases in Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/zero-etl-using.creating-db.html).
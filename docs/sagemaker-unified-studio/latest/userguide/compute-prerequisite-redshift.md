# Gaining access to Amazon Redshift resources

To add Amazon SageMaker Unified Studio connections to existing compute resources,
you must get access information from the admin that owns the resources.
To do this, first get your project ID from the **Project overview** page of the project you want to add resources to.
Then, send the project ID to the owner of the Amazon Redshift resources. The Amazon Redshift admin uses the project ID to complete some steps so that you receive access details from them,
and then you can input the access information in Amazon SageMaker Unified Studio.

You and the admin must complete different steps depending on whether the resources are
in the same account as the account you are accessing Amazon SageMaker Unified Studio in.

###### Note

If you want to query the Amazon Redshift resources using JuypterLab within Amazon SageMaker Unified Studio, the Amazon Redshift resource
must use the same VPC as the Amazon SageMaker Unified Studio project. If the Amazon SageMaker Unified Studio project uses a different VPC than the Amazon Redshift resource you want to gain access to,
you and your admin must complete additional steps to connect the VPCs before you can use JupyterLab to query. You can still query using the Data page of your project if you are using different VPCs.
For more information, see [VPC to VPC connectivity](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.md")
and [Connect VPCs using VPC peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md").

## Gaining access to resources in the same account

In some cases, the Amazon Redshift resource you want to add to your Amazon SageMaker Unified Studio project might be in the same account as your project.

###### For compute resources in the same account as your Amazon SageMaker Unified Studio project, complete the following steps:

1. Send the Amazon Redshift admin the project ID. This can be found on the **Project overview** page of your Amazon SageMaker Unified Studio project.
2. The admin then adds 1 of the following tags to the Amazon Redshift cluster or workgroup and its namespace that you want to add to Amazon SageMaker Unified Studio.
   - Option 1: Add a tag to allow only a specific Amazon SageMaker Unified Studio project to access it: `AmazonDataZoneProject=`projectID``.
   - Option 2: Add a tag to allow all Amazon SageMaker Unified Studio projects in this account to access it: `for-use-with-all-datazone-projects=true`.

3. The admin then must send you a username and password for a database user that has access to the compute
   resources.

You can then use the username and password to add the compute connection in Amazon SageMaker Unified Studio. For
more information, see [Connecting to an existing Amazon Redshift resource](adding-a-existing-compute-connection.md "adding-a-existing-compute-connection.md").

## Gaining access to resources in a different account

In some cases, the Amazon Redshift resource you want to add to your Amazon SageMaker Unified Studio project might be in a different AWS account than your project.

###### For compute resources in a different account, complete the following steps:

1. Send the Amazon Redshift admin the following information from the **Project overview** page of your Amazon SageMaker Unified Studio project:
   - The Amazon SageMaker Unified Studio project role ARN.
   - The Amazon SageMaker Unified Studio project ID.
   - The Amazon SageMaker Unified Studio project domain ID.

2. The admin must create an access role for Amazon SageMaker Unified Studio that can be used to query Amazon Redshift.

An example Amazon Redshift access role for Amazon SageMaker Unified Studio is provided below:

```

# Sample permission policy of access role to query Redshift
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RedshiftQueryEditorConnectPermissions",
            "Effect": "Allow",
            "Action": [
                "redshift:GetClusterCredentialsWithIAM",
                "redshift:GetClusterCredentials",
                "redshift:DescribeClusters",
                "redshift:CreateClusterUser"
            ],
            "Resource": [
                "arn:aws:redshift:*:012345678912:cluster:*",
                "arn:aws:redshift:*:012345678912:dbname:*/*",
                "arn:aws:redshift:*:012345678912:dbuser:*/*"
            ]
        },
        {
            "Sid": "RedshiftServerlessQueryEditorConnectPermissions",
            "Effect": "Allow",
            "Action": [
                "redshift-serverless:GetCredentials",
                "redshift-serverless:GetWorkgroup",
                "redshift-serverless:ListTagsForResource"
            ],
            "Resource": [
                "arn:aws:redshift-serverless:*:012345678912:workgroup/*"
            ]
        },
        {
            "Sid": "SecretsManagerAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:DescribeSecret"
            ],
            "Resource": [
                "`secret_arn`"
            ]
        },
        {
            "Sid": "sqlworkbench",
            "Effect": "Allow",
            "Action": [
                "sqlworkbench:*"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

```

The trust policy is as follows:

```

# trust policy of access role
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": "sts:AssumeRole",
            "Condition": {
                "StringEquals": {
                    "sts:ExternalId": "`project-id`"
                }
            }
        },
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": [
                "sts:SetSourceIdentity"
            ],
            "Condition": {
                "StringLike": {
                    "sts:SourceIdentity": "${aws:PrincipalTag/datazone:userId}"
                }
            }
        },
       {
            "Effect": "Allow",
            "Principal": {
                "AWS": "`project-role-arn`"
            },
            "Action": "sts:TagSession",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/AmazonDataZoneProject": "`project-id`",
                    "aws:RequestTag/AmazonDataZoneDomain": "`domain-id`"
                }
            }
        }
    ]
}

```

3. (Optional) If you want to use IAM credentials to access the Amazon Redshift resource, rather than an AWS Secrets Manager secret,
   the admin must add the following tag to the access role:

```
RedshiftDbUser=`Username`
```

4. The admin then needs to provide JDBC connection info in one of two ways:
   - Use a Secrets Manager secret in the same account as the Redshift resource. The
     access role should have permission to read the secret value.
     For more information about the JSON format that should be used in the secret, see [JSON structure of a secret](../../../secretsmanager/latest/userguide/reference_secret_json_structure.md#reference_secret_json_structure_RS "../../../secretsmanager/latest/userguide/reference_secret_json_structure.md#reference_secret_json_structure_RS")
     in the AWS Secrets Manager User Guide.
   - Use a temporary username and password. This is generated from the IAM access role
     credentials.
     - The `RedshiftDbUser` tag on the access role is required. This determines the federated database user
       within the databases for the Amazon SageMaker Unified Studio users. For more information, see [Setting up principal tags to connect a cluster or workgroup from query editor
       v2](../../../redshift/latest/mgmt/query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam "../../../redshift/latest/mgmt/query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam") in the Amazon Redshift Management Guide.

5. The admin then sends you the following information:
   - Access role ARN.
   - JDBC URL. For example: _jdbc:redshift://default-workgroup.012345678912.us-west-2.redshift-serverless.amazonaws.com.
     For more information about JDBC connections, see_ [_Connecting to Amazon Redshift Serverless through JDBC
     drivers_](../../../redshift/latest/mgmt/serverless-connecting.md#serverless-connecting-driver "../../../redshift/latest/mgmt/serverless-connecting.md#serverless-connecting-driver") _and_ [_Getting the JDBC URL_](../../../redshift/latest/mgmt/jdbc20-obtain-url.md "../../../redshift/latest/mgmt/jdbc20-obtain-url.md") _in the in the Amazon Redshift Management Guide._.
   - _(Optional) AWS Secrets Manager secret ARN._
     For example:_arn:aws:secretsmanager:us-west-2:012345678912:secret:shared-rs-cluster-password-Ab1CDe._

You can then use the access credentials and JDBC URL to add the compute connection in Amazon SageMaker Unified Studio. For
more information, see [Connecting to an existing Amazon Redshift resource](adding-a-existing-compute-connection.md "adding-a-existing-compute-connection.md").

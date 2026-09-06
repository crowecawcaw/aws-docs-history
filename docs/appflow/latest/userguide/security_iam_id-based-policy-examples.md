

# Identity-based policy examples for Amazon AppFlow
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify Amazon AppFlow resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by Amazon AppFlow, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for Amazon AppFlow](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonappflow.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Example 1: Allow IAM users full administrator access to Amazon AppFlow](#example-full-admin)
+ [Example 2: Allow IAM users read-only access to Amazon AppFlow](#example-read-only)
+ [Example 3: Grant access to permission-only actions](#permission-only-actions)
+ [Example 4: Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Example 5: Allow Amazon AppFlow to access the AWS Glue Data Catalog](#security_iam_id-based-policy-examples-access-gdc)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete Amazon AppFlow resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Example 1: Allow IAM users full administrator access to Amazon AppFlow
<a name="example-full-admin"></a>

This policy example provides full access to Amazon AppFlow, to all AWS services that are available as flow sources or destinations, and to AWS Key Management Service (AWS KMS).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "appflow:*",
            "Resource": "*"
        },
        {
            "Sid": "ListRolesForRedshift",
            "Effect": "Allow",
            "Action": "iam:ListRoles",
            "Resource": "*"
        },
        {
            "Sid": "KMSListAccess",
            "Action": [
                "kms:ListKeys",
                "kms:DescribeKey",
                "kms:ListAliases"
            ],
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Sid": "KMSGrantAccess",
            "Effect": "Allow",
            "Action": [
                "kms:CreateGrant"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "appflow.*.amazonaws.com"
                },
                "Bool": {
                    "kms:GrantIsForAWSResource": "true"
                }
            }
        },
        {
            "Sid": "KMSListGrantAccess",
            "Effect": "Allow",
            "Action": [
                "kms:ListGrants"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "kms:ViaService": "appflow.*.amazonaws.com"
                }
            }
        },
        {
            "Sid": "S3ReadAccess",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:ListBucket",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicy"
            ],
            "Resource": "*"
        },
        {
            "Sid": "S3PutBucketPolicyAccess",
            "Effect": "Allow",
            "Action": [
                "s3:PutBucketPolicy"
            ],
            "Resource": "arn:aws:s3:::appflow-*"
        },
        {
            "Sid": "SecretsManagerCreateSecretAccess",
            "Effect": "Allow",
            "Action": "secretsmanager:CreateSecret",
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "secretsmanager:Name": "appflow!*"
                },
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "appflow.amazonaws.com"
                    ]
                }
            }
        },
        {
            "Sid": "SecretsManagerPutResourcePolicyAccess",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:PutResourcePolicy"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:CalledVia": [
                        "appflow.amazonaws.com"
                    ]
                },
                "StringEqualsIgnoreCase": {
                    "secretsmanager:ResourceTag/aws:secretsmanager:owningService": "appflow"
                }
            }
        }
    ]
}
```

------

## Example 2: Allow IAM users read-only access to Amazon AppFlow
<a name="example-read-only"></a>

This policy example provides read-only access to Amazon AppFlow.

For definitions of each action, see [Actions defined by Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/identity-access-management.html#actions-table).

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
            "appflow:DescribeConnectors",
            "appflow:DescribeConnectorProfiles",
            "appflow:DescribeFlows",
            "appflow:DescribeFlowExecution",
            "appflow:DescribeConnectorFields",
            "appflow:ListConnectorFields",
            "appflow:ListTagsForResource"
            ],
            "Resource": "*"
        }
    ]
}
```

------

## Example 3: Grant access to permission-only actions
<a name="permission-only-actions"></a>

If you use a custom policy to grant users permission to use Amazon AppFlow instead of the managed policies provided, you must include specific permissions for the user or role to perform specific actions. For example, if the user or role needs to add or update a flow, the policy attached to the user or role must include permission to use the `UseConnectorProfile` permission-only action so that the user has permission to use the connection specified for the flow. You can specify that the user is allowed to use all connector profiles, or only a specific connector profile. The following example policy statement demonstrates how to grant access only to a specific connector profile by specifying the ARN to the connector profile named *test-profile* in the account 123456789012. You can modify this policy statement and include it in a custom policy for your environment, but this statement grants permission only to use the connector profile. The user or role needs additional permissions to perform other Amazon AppFlow actions.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowConnectionProfile",
            "Effect": "Allow",
            "Action": "appflow:UseConnectorProfile",
            "Resource": "arn:aws:appflow:us-east-1:123456789012:connectorprofile/test-profile"
        }
    ]
}
```

------

## Example 4: Allow users to view their own permissions
<a name="security_iam_id-based-policy-examples-view-own-permissions"></a>

This example shows how you might create a policy that allows IAM users to view the inline and managed policies that are attached to their user identity. This policy includes permissions to complete this action on the console or programmatically using the AWS CLI or AWS API.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "ViewOwnUserInfo",
            "Effect": "Allow",
            "Action": [
                "iam:GetUserPolicy",
                "iam:ListGroupsForUser",
                "iam:ListAttachedUserPolicies",
                "iam:ListUserPolicies",
                "iam:GetUser"
            ],
            "Resource": ["arn:aws:iam::*:user/${aws:username}"]
        },
        {
            "Sid": "NavigateInConsole",
            "Effect": "Allow",
            "Action": [
                "iam:GetGroupPolicy",
                "iam:GetPolicyVersion",
                "iam:GetPolicy",
                "iam:ListAttachedGroupPolicies",
                "iam:ListGroupPolicies",
                "iam:ListPolicyVersions",
                "iam:ListPolicies",
                "iam:ListUsers"
            ],
            "Resource": "*"
        }
    ]
}
```

## Example 5: Allow Amazon AppFlow to access the AWS Glue Data Catalog
<a name="security_iam_id-based-policy-examples-access-gdc"></a>

Before you can create a flow that catalogs its output data in the AWS Glue Data Catalog, you must grant Amazon AppFlow the required permissions. Amazon AppFlow requires permissions to create Data Catalog tables, databases, and partitions. To grant those permissions, create an IAM role that contains the following permissions policy and trust policy. Provide this role to Amazon AppFlow in the settings for your flows.

**Example permissions policy**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "glue:BatchCreatePartition",
                "glue:CreatePartitionIndex",
                "glue:DeleteDatabase",
                "glue:GetTableVersions",
                "glue:GetPartitions",
                "glue:BatchDeletePartition",
                "glue:DeleteTableVersion",
                "glue:UpdateTable",
                "glue:DeleteTable",
                "glue:DeletePartitionIndex",
                "glue:GetTableVersion",
                "glue:CreatePartition",
                "glue:UntagResource",
                "glue:UpdatePartition",
                "glue:TagResource",
                "glue:UpdateDatabase",
                "glue:CreateTable",
                "glue:BatchUpdatePartition",
                "glue:GetTables",
                "glue:BatchGetPartition",
                "glue:GetDatabases",
                "glue:GetPartitionIndexes",
                "glue:GetTable",
                "glue:GetDatabase",
                "glue:GetPartition",
                "glue:CreateDatabase",
                "glue:BatchDeleteTableVersion",
                "glue:BatchDeleteTable",
                "glue:DeletePartition"
            ],
            "Resource": "*"
        }
    ]
}
```

**Example trust policy**    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "Service": "appflow.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```
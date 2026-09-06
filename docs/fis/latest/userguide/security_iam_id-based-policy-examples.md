

# AWS Fault Injection Service policy examples
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify AWS FIS resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by AWS FIS, including the format of the ARNs for each of the resource types, see [Actions, resources, and condition keys for AWS Fault Injection Service](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsfaultinjectionservice.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Example: Use the AWS FIS console](#security-iam-policy-examples-console)
+ [Example: List available AWS FIS actions](#security-iam-policy-examples-list-actions)
+ [Example: Create an experiment template for a specific action](#security-iam-policy-examples-create-template)
+ [Example: Start an experiment](#security-iam-policy-examples-start-experiment)
+ [Example: Use tags to control resource usage](#security-iam-policy-examples-tagging)
+ [Example: Delete an experiment template with a specific tag](#security-iam-policy-examples-delete-tagged-template)
+ [Example: Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Example: Use condition keys for `ec2:InjectApiError`](#security-iam-policy-examples-ec2)
+ [Example: Use condition keys for `aws:s3:bucket-pause-replication`](#security-iam-policy-examples-s3)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete AWS FIS resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Example: Use the AWS FIS console
<a name="security-iam-policy-examples-console"></a>

To access the AWS Fault Injection Service console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the AWS FIS resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

The following example policy grants permission to list and view all AWS FIS resources using AWS FIS console, but not to create, update, or delete them. It also grants permissions to view the available resources used by all AWS FIS actions that you could specify in an experiment template.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "FISReadOnlyActions",
            "Effect": "Allow",
            "Action": [
                "fis:List*",
                "fis:Get*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "AdditionalReadOnlyActions",
            "Effect": "Allow",
            "Action": [
                "ssm:Describe*",
                "ssm:Get*",
                "ssm:List*",
                "ec2:DescribeInstances",
                "rds:DescribeDBClusters",
                "ecs:DescribeClusters",
                "ecs:ListContainerInstances",
                "eks:DescribeNodegroup",
                "cloudwatch:DescribeAlarms",
                "iam:ListRoles"
            ],
            "Resource": "*"
        },
        {
            "Sid": "PermissionsToCreateServiceLinkedRole",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "fis.amazonaws.com"
                }
            }
        }
    ]
}
```

------

## Example: List available AWS FIS actions
<a name="security-iam-policy-examples-list-actions"></a>

The following policy grants permission to list the available AWS FIS actions.

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
                "fis:ListActions"
            ],
            "Resource": "arn:aws:fis:*:*:action/*"
        }
    ]
}
```

------

## Example: Create an experiment template for a specific action
<a name="security-iam-policy-examples-create-template"></a>

The following policy grants permission to create an experiment template for the action `aws:ec2:stop-instances`.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "PolicyExample",
            "Effect": "Allow",
            "Action": [
                "fis:CreateExperimentTemplate"
            ],
            "Resource": [
                "arn:aws:fis:*:*:action/aws:ec2:stop-instances",
                "arn:aws:fis:*:*:experiment-template/*"
            ]
        },
        {
            "Sid": "PolicyPassRoleExample",
            "Effect": "Allow",
            "Action": [
                "iam:PassRole"
            ],
            "Resource": [
                "arn:aws:iam::{{111122223333}}:role/{{role-name}}"
            ]
        }
    ]
}
```

------

## Example: Start an experiment
<a name="security-iam-policy-examples-start-experiment"></a>

The following policy grants permission to start an experiment using the specified IAM role and experiment template. It also allows AWS FIS to create a service-linked role on the user's behalf. For more information, see [Use service-linked roles for AWS Fault Injection Service](using-service-linked-roles.md).

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Sid": "PolicyExample",
      "Effect": "Allow",
      "Action": [
          "fis:StartExperiment"
      ],
      "Resource": [
        "arn:aws:fis:*:*:experiment-template/{{experiment-template-id}}",
        "arn:aws:fis:*:*:experiment/*"
      ]
    },
    {
        "Sid": "PolicyExampleforServiceLinkedRole",
        "Effect": "Allow",
        "Action": "iam:CreateServiceLinkedRole",
        "Resource": "*",
        "Condition": {
            "StringEquals": {
                "iam:AWSServiceName": "fis.amazonaws.com"
            }
        }
    }
  ]
}
```

------

## Example: Use tags to control resource usage
<a name="security-iam-policy-examples-tagging"></a>

The following policy grants permission to run experiments from experiment templates that have the tag `Purpose=Test`. It does not grant permission to create or modify experiment templates, or run experiments using templates that do not have the specified tag.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "fis:StartExperiment",
            "Resource": "arn:aws:fis:*:*:experiment-template/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/{{Purpose}}": "{{Test}}"
                }
            }
        }
    ]
}
```

------

## Example: Delete an experiment template with a specific tag
<a name="security-iam-policy-examples-delete-tagged-template"></a>

The following policy grants permission to delete an experiment template with tag `Purpose=Test`.

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
                "fis:DeleteExperimentTemplate"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/{{Purpose}}": "{{Test}}"
                }
            }
        }
    ]
}
```

------

## Example: Allow users to view their own permissions
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

## Example: Use condition keys for `ec2:InjectApiError`
<a name="security-iam-policy-examples-ec2"></a>

The following example policy uses the `ec2:FisTargetArns` condition key to scope target resources. This policy allows the AWS FIS actions `aws:ec2:api-insufficient-instance-capacity-error` and `aws:ec2:asg-insufficient-instance-capacity-error`. 

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:InjectApiError",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "ec2:FisActionId": [
            "aws:ec2:api-insufficient-instance-capacity-error",
            "aws:ec2:asg-insufficient-instance-capacity-error"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "ec2:InjectApiError",
      "Resource": "*",
      "Condition": {
        "ForAllValues:ArnLike": {
          "ec2:FisTargetArns": [
            "arn:aws:autoscaling:*:*:autoScalingGroup:uuid:{{autoScalingGroupName}}/{{asg-name}}"
          ]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": "autoscaling:DescribeAutoScalingGroups",
      "Resource": "*"
    }
  ]
}
```

------

## Example: Use condition keys for `aws:s3:bucket-pause-replication`
<a name="security-iam-policy-examples-s3"></a>

The following example policy uses the `S3:IsReplicationPauseRequest` condition key to allow `PutReplicationConfiguration` and `GetReplicationConfiguration` only when used by AWS FIS in the context of the AWS FIS action `aws:s3:bucket-pause-replication`.

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
                "S3:PauseReplication"
            ],
            "Resource": "arn:aws:s3:::mybucket",
            "Condition": {
                "StringEquals": {
                    "s3:DestinationRegion": "{{region}}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "S3:PutReplicationConfiguration",
                "S3:GetReplicationConfiguration"
            ],
            "Resource": "arn:aws:s3:::mybucket",
            "Condition": {
                "BoolIfExists": {
                    "s3:IsReplicationPauseRequest": "true"
                }
            } 
        },
        {
            "Effect": "Allow",
            "Action": [
                "S3:ListBucket"                   
            ],
            "Resource": "arn:aws:s3:::*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "tag:GetResources"                   
            ],
            "Resource": "*"
        }
    ]
    }
```

------
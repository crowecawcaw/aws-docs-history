

# Identity-based policy examples for RTB Fabric
<a name="security_iam_id-based-policy-examples"></a>

By default, users and roles don't have permission to create or modify RTB Fabric resources. To grant users permission to perform actions on the resources that they need, an IAM administrator can create IAM policies.

To learn how to create an IAM identity-based policy by using these example JSON policy documents, see [Create IAM policies (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html) in the *IAM User Guide*.

For details about actions and resource types defined by RTB Fabric, including the format of the ARNs for each of the resource types, see [Actions, Resources, and Condition Keys for AWS RTB Fabric](https://docs.aws.amazon.com/IAM/latest/UserGuide/list_rtbfabric.html) in the *Service Authorization Reference*.

**Topics**
+ [Policy best practices](#security_iam_service-with-iam-policy-best-practices)
+ [Using the RTB Fabric console](#security_iam_id-based-policy-examples-console)
+ [Allow users to view their own permissions](#security_iam_id-based-policy-examples-view-own-permissions)
+ [Basic RTB Fabric permissions](#security_iam_id-based-policy-examples-rtb-basic)
+ [RTB Fabric administrator permissions](#security_iam_id-based-policy-examples-rtb-admin)
+ [RTB Fabric read-only permissions](#security_iam_id-based-policy-examples-rtb-readonly)

## Policy best practices
<a name="security_iam_service-with-iam-policy-best-practices"></a>

Identity-based policies determine whether someone can create, access, or delete RTB Fabric resources in your account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and recommendations:
+ **Get started with AWS managed policies and move toward least-privilege permissions** – To get started granting permissions to your users and workloads, use the *AWS managed policies* that grant permissions for many common use cases. They are available in your AWS account. We recommend that you reduce permissions further by defining AWS customer managed policies that are specific to your use cases. For more information, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) or [AWS managed policies for job functions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_job-functions.html) in the *IAM User Guide*.
+ **Apply least-privilege permissions** – When you set permissions with IAM policies, grant only the permissions required to perform a task. You do this by defining the actions that can be taken on specific resources under specific conditions, also known as *least-privilege permissions*. For more information about using IAM to apply permissions, see [ Policies and permissions in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html) in the *IAM User Guide*.
+ **Use conditions in IAM policies to further restrict access** – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must be sent using SSL. You can also use conditions to grant access to service actions if they are used through a specific AWS service, such as CloudFormation. For more information, see [ IAM JSON policy elements: Condition](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_condition.html) in the *IAM User Guide*.
+ **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions** – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices. IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-validation.html) in the *IAM User Guide*.
+ **Require multi-factor authentication (MFA)** – If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require MFA when API operations are called, add MFA conditions to your policies. For more information, see [ Secure API access with MFA](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html) in the *IAM User Guide*.

For more information about best practices in IAM, see [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the *IAM User Guide*.

## Using the RTB Fabric console
<a name="security_iam_id-based-policy-examples-console"></a>

To access the AWS RTB Fabric console, you must have a minimum set of permissions. These permissions must allow you to list and view details about the RTB Fabric resources in your AWS account. If you create an identity-based policy that is more restrictive than the minimum required permissions, the console won't function as intended for entities (users or roles) with that policy.

You don't need to allow minimum console permissions for users that are making calls only to the AWS CLI or the AWS API. Instead, allow access to only the actions that match the API operation that they're trying to perform.

To ensure that users and roles can still use the RTB Fabric console, also attach the RTB Fabric `ReadOnly` permissions to the entities. For more information, see [Adding permissions to a user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

Users who need console access require the following permissions:

```
{
    "Version": "2012-10-17", 		 	 	 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:GetRequesterGateway",
                "rtbfabric:GetResponderGateway", 
                "rtbfabric:ListRequesterGateways",
                "rtbfabric:ListResponderGateways",
                "rtbfabric:GetLink",
                "rtbfabric:ListLinks",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*"
        }
    ]
}
```

## Allow users to view their own permissions
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

## Basic RTB Fabric permissions
<a name="security_iam_id-based-policy-examples-rtb-basic"></a>

This example shows a policy that allows basic RTB Fabric operations including creating, viewing, and managing RTB applications and links.

```
{
    "Version": "2012-10-17", 		 	 	 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:CreateRequesterGateway",
                "rtbfabric:CreateResponderGateway",
                "rtbfabric:DeleteRequesterGateway",
                "rtbfabric:DeleteResponderGateway",
                "rtbfabric:GetRequesterGateway",
                "rtbfabric:GetResponderGateway", 
                "rtbfabric:ListRequesterGateways",
                "rtbfabric:ListResponderGateways",
                "rtbfabric:CreateLink",
                "rtbfabric:DeleteLink",
                "rtbfabric:GetLink",
                "rtbfabric:ListLinks",
                "rtbfabric:AcceptLink",
                "rtbfabric:RejectLink"
            ],
            "Resource": [
                "arn:aws:rtbfabric:*:*:gateway/*",
                "arn:aws:rtbfabric:*:*:link/*"
            ]
        }
    ]
}
```

This policy grants permissions to perform common RTB Fabric operations on RTB applications and links in any region within your AWS account.

## RTB Fabric administrator permissions
<a name="security_iam_id-based-policy-examples-rtb-admin"></a>

This example shows a policy that allows full administrative access to RTB Fabric, including the ability to view network interfaces managed by the service. For additional security, consider scoping the CloudWatch Get actions to specific metric resources rather than using wildcard (\*) resources, depending on your monitoring requirements.

```
{
    "Version": "2012-10-17", 		 	 	 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": "${aws:PrincipalTag/RTBFabricRegion}"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "rtbfabric"
                }
            }
        }
    ]
}
```

This policy grants full RTB Fabric permissions and allows viewing of related AWS resources like network interfaces and CloudWatch metrics that RTB Fabric manages. The EC2 describe actions are scoped to regions specified in the principal's RTBFabricRegion tag for additional security.

## RTB Fabric read-only permissions
<a name="security_iam_id-based-policy-examples-rtb-readonly"></a>

This example shows a policy that allows read-only access to RTB Fabric resources and related AWS resources.

```
{
    "Version": "2012-10-17", 		 	 	 		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rtbfabric:GetRequesterGateway",
                "rtbfabric:GetResponderGateway", 
                "rtbfabric:ListRequesterGateways",
                "rtbfabric:ListResponderGateways",
                "rtbfabric:GetLink",
                "rtbfabric:ListLinks"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:ListMetrics"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": "rtbfabric"
                }
            }
        }
    ]
}
```

This policy grants read-only access to RTB Fabric resources and allows viewing CloudWatch metrics published by the service.
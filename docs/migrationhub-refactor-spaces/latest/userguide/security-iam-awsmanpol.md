AWS Migration Hub Refactor Spaces is no longer open to new customers as of November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# AWS managed policies for AWS Migration Hub Refactor Spaces

To add permissions to users, groups, and roles, it is easier to use AWS managed policies
than to write policies yourself. It takes time and expertise to [create IAM customer
managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the permissions they need. To
get started quickly, you can use our AWS managed policies. These policies cover common use
cases and are available in your AWS account. For more information about AWS managed
policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions to
an AWS managed policy to support new features. This type of update affects all identities
(users, groups, and roles) where the policy is attached. Services are most likely to update
an AWS managed policy when a new feature is launched or when new operations become
available. Services do not remove permissions from an AWS managed policy, so policy
updates won't break your existing permissions.

## AWS

managed policy: AWSMigrationHubRefactorSpacesFullAccess

You can attach the `AWSMigrationHubRefactorSpacesFullAccess` policy to a
role that users can assume.

The `AWSMigrationHubRefactorSpacesFullAccess` policy grants full access to
AWS Migration Hub Refactor Spaces, the Refactor Spaces console features and other related AWS services.

**Permissions details**

The `AWSMigrationHubRefactorSpacesFullAccess` policy includes the following
permissions.

- `refactor-spaces` – Allows the user full access to
  Refactor Spaces.
- `ec2` – Allows the user to perform Amazon Elastic Compute Cloud (Amazon EC2)
  operations used by Refactor Spaces.
- `elasticloadbalancing` – Allows the user to perform
  Elastic Load Balancing operations used by Refactor Spaces.
- `apigateway` – Allows the user to perform Amazon API Gateway
  operations used by Refactor Spaces.
- `organizations` – Allows the user to perform AWS Organizations
  operations used by Refactor Spaces.
- `cloudformation` – Allows the user to perform AWS CloudFormation
  operations to create a one-click sample environment from the console.
- `iam` – Allows a service-linked role to be created for the
  user, which is a requirement for using Refactor Spaces.

### Extra required

permissions for Refactor Spaces

Before you can use Refactor Spaces, in addition to the
`AWSMigrationHubRefactorSpacesFullAccess` managed policy provided by
Refactor Spaces, the following extra required permissions must be attached to a role that
users can assume.

- Grant permission to create a service-linked role for AWS Transit Gateway.
- Grant permission to attach a virtual private cloud (VPC) to a transit
  gateway for the calling account for all resources.
- Grant permission to modify the permissions for a VPC endpoint service for
  all resources.
- Grant permission to add or overwrite specified tags for Amazon EC2
  resources.
- Grant permission to return tagged or previously tagged resources for the
  calling account for all resources.
- Grant permission to perform all AWS Resource Access Manager (AWS RAM) actions for the calling
  account on all resources.
- Grant permission to perform all AWS Lambda actions for the calling account
  on all resources.

You can get these extra permissions by creating an IAM policy using the
following policy JSON, and attach it to a role.

The following policy grants the extra required permissions necessary to be able to
use Refactor Spaces.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "transitgateway.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTransitGatewayVpcAttachment"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:ModifyVpcEndpointServicePermissions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "tag:GetResources"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ram:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "*"
        }
    ]
 }
```

The following is the `AWSMigrationHubRefactorSpacesFullAccess`
policy.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RefactorSpaces",
            "Effect": "Allow",
            "Action": [
                "refactor-spaces:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2Describe",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcEndpointServiceConfigurations",
                "ec2:DescribeVpcs",
                "ec2:DescribeTransitGatewayVpcAttachments",
                "ec2:DescribeTransitGateways",
                "ec2:DescribeTags",
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeInternetGateways"
            ],
            "Resource": "*"
        },
        {
            "Sid": "RequestTagTransitGatewayCreate",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTransitGateway",
                "ec2:CreateSecurityGroup",
                "ec2:CreateTransitGatewayVpcAttachment"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:environment-id": "false"
                }
            }
        },
        {
            "Sid": "ResourceTagTransitGatewayCreate",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTransitGateway",
                "ec2:CreateSecurityGroup",
                "ec2:CreateTransitGatewayVpcAttachment"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:environment-id": "false"
                }
            }
        },
        {
            "Sid": "VpcEndpointServiceConfigurationCreate",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpcEndpointServiceConfiguration"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2NetworkingModify",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteTransitGateway",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteTransitGatewayVpcAttachment",
                "ec2:CreateRoute",
                "ec2:DeleteRoute",
                "ec2:DeleteTags"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:environment-id": "false"
                }
            }
        },
        {
            "Sid": "VpcEndpointServiceConfigurationDelete",
            "Effect": "Allow",
            "Action": "ec2:DeleteVpcEndpointServiceConfigurations",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "ELBLoadBalancerCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateLoadBalancer"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "ELBDescribe",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTags",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeListeners"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ELBModify",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:RegisterTargets",
                "elasticloadbalancing:CreateLoadBalancerListeners",
                "elasticloadbalancing:CreateListener",
                "elasticloadbalancing:DeleteListener",
                "elasticloadbalancing:DeleteTargetGroup"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/refactor-spaces:route-id": [
                        "*"
                    ]
                }
            }
        },
        {
            "Sid": "ELBLoadBalancerDelete",
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteLoadBalancer",
            "Resource": "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*"
        },
        {
            "Sid": "ELBListenerCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateListener"
            ],
            "Resource": [
                "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*",
                "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
            "Sid": "ELBListenerDelete",
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteListener",
            "Resource": "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"
        },
        {
            "Sid": "ELBTargetGroupModify",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DeleteTargetGroup",
                "elasticloadbalancing:RegisterTargets"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*"
        },
        {
            "Sid": "ELBTargetGroupCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateTargetGroup"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
            "Sid": "APIGatewayModify",
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "apigateway:DELETE",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "apigateway:UpdateRestApiPolicy"
            ],
            "Resource": [
                "arn:aws:apigateway:*::/restapis",
                "arn:aws:apigateway:*::/restapis/*",
                "arn:aws:apigateway:*::/vpclinks",
                "arn:aws:apigateway:*::/vpclinks/*",
                "arn:aws:apigateway:*::/tags",
                "arn:aws:apigateway:*::/tags/*"
            ],
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "APIGatewayVpcLinksGet",
            "Effect": "Allow",
            "Action": "apigateway:GET",
            "Resource": [
                "arn:aws:apigateway:*::/vpclinks",
                "arn:aws:apigateway:*::/vpclinks/*"
            ]
        },
        {
            "Sid": "OrganizationDescribe",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudformationStackCreate",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudformationStackTag",
            "Effect": "Allow",
            "Action": [
                "cloudformation:TagResource"
            ],
            "Resource": "arn:aws:cloudformation:*:*:stack/*"
        },
        {
            "Sid": "CreateRefactorSpacesSLR",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "refactor-spaces.amazonaws.com"
                }
            }
        },
        {
            "Sid": "CreateELBSLR",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
                }
            }
        }
    ]
}
```

## AWS managed policy:

AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess

This AWS managed policy has reduced permissions when compared to the
`AWSMigrationHubRefactorSpacesFullAccess` policy. You can attach the
`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`
policy to a role that users can assume.

You can use the
`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`
policy when you create environments without a network bridge. Since you are using your
own network infrastructure, the modified policy removes Transit Gateway permissions and Amazon EC2
security groups related to Transit Gateway actions.

**Permissions details**

The `AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`
policy includes the following permissions.

- `refactor-spaces` – Allows the user full access to
  Refactor Spaces.
- `ec2` – Allows the user to perform Amazon Elastic Compute Cloud (Amazon EC2)
  operations used by Refactor Spaces.
- `elasticloadbalancing` – Allows the user to perform
  Elastic Load Balancing operations used by Refactor Spaces.
- `apigateway` – Allows the user to perform Amazon API Gateway
  operations used by Refactor Spaces.
- `organizations` – Allows the user to perform AWS Organizations
  operations used by Refactor Spaces.
- `cloudformation` – Allows the user to perform AWS CloudFormation
  operations to create a one-click sample environment from the console.
- `iam` – Allows a service-linked role to be created for the
  user, which is a requirement for using Refactor Spaces.

###

Extra required permissions policy for environments without a network
bridge

The following policy is an example of a modified version of the extra required
permissions policy that you must use together with the
`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`
policy when creating environments without a Transit Gateway. To use this policy, create a
role and attach the policy to the role.

- Grant permission to modify the permissions for a virtual private cloud
  (VPC) endpoint for all resources.
- Grant permission to add or overwrite specified tags for Amazon EC2
  resources.
- Grant permission to return tagged or previously tagged resources for the
  calling account for all resources.
- Grant permission to perform all AWS Resource Access Manager (AWS RAM) actions for the calling
  account on all resources.
- Grant permission to perform all AWS Lambda actions for the calling account
  on all resources.

```
{
    "Version": "2012-10-17",
    "Statement": [{
            "Effect": "Allow",
            "Action": [
                "ec2:ModifyVpcEndpointServicePermissions"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "tag:GetResources"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ram:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "lambda:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "*"
        }
    ]
}
```

The following is the
`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`
managed policy that you can use when creating environments without a Transit Gateway. To use
this policy, create a role and attach the policy to the role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RefactorSpaces",
            "Effect": "Allow",
            "Action": [
                "refactor-spaces:*"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2Describe",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcEndpointServiceConfigurations",
                "ec2:DescribeVpcs",
                "ec2:DescribeTags",
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeInternetGateways"
            ],
            "Resource": "*"
        },
        {
            "Sid": "VpcEndpointServiceConfigurationCreate",
            "Effect": "Allow",
            "Action": [
                "ec2:CreateVpcEndpointServiceConfiguration"
            ],
            "Resource": "*"
        },
        {
            "Sid": "EC2TagsDelete",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteTags"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:environment-id": "false"
                }
            }
        },
        {
            "Sid": "VpcEndpointServiceConfigurationDelete",
            "Effect": "Allow",
            "Action": "ec2:DeleteVpcEndpointServiceConfigurations",
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "ELBLoadBalancerCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateLoadBalancer"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "ELBDescribe",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTags",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeTargetGroups",
                "elasticloadbalancing:DescribeListeners"
            ],
            "Resource": "*"
        },
        {
            "Sid": "ELBModify",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:RegisterTargets",
                "elasticloadbalancing:CreateLoadBalancerListeners",
                "elasticloadbalancing:CreateListener",
                "elasticloadbalancing:DeleteListener",
                "elasticloadbalancing:DeleteTargetGroup"
            ],
            "Resource": "*",
            "Condition": {
                "StringLike": {
                    "aws:ResourceTag/refactor-spaces:route-id": [
                        "*"
                    ]
                }
            }
        },
        {
            "Sid": "ELBLoadBalancerDelete",
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteLoadBalancer",
            "Resource": "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*"
        },
        {
            "Sid": "ELBListenerCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateListener"
            ],
            "Resource": [
                "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*",
                "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"
            ],
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
            "Sid": "ELBListenerDelete",
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteListener",
            "Resource": "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"
        },
        {
            "Sid": "ELBTargetGroupModify",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DeleteTargetGroup",
                "elasticloadbalancing:RegisterTargets"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*"
        },
        {
            "Sid": "ELBTargetGroupCreate",
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateTargetGroup"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*",
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
            "Sid": "APIGatewayModify",
            "Effect": "Allow",
            "Action": [
                "apigateway:GET",
                "apigateway:DELETE",
                "apigateway:PATCH",
                "apigateway:POST",
                "apigateway:PUT",
                "apigateway:UpdateRestApiPolicy"
            ],
            "Resource": [
                "arn:aws:apigateway:*::/restapis",
                "arn:aws:apigateway:*::/restapis/*",
                "arn:aws:apigateway:*::/vpclinks",
                "arn:aws:apigateway:*::/vpclinks/*",
                "arn:aws:apigateway:*::/tags",
                "arn:aws:apigateway:*::/tags/*"
            ],
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:application-id": "false"
                }
            }
        },
        {
            "Sid": "APIGatewayVpcLinksGet",
            "Effect": "Allow",
            "Action": "apigateway:GET",
            "Resource": [
                "arn:aws:apigateway:*::/vpclinks",
                "arn:aws:apigateway:*::/vpclinks/*"
            ]
        },
        {
            "Sid": "OrganizationDescribe",
            "Effect": "Allow",
            "Action": [
                "organizations:DescribeOrganization"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudformationStackCreate",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudformationStackTag",
            "Effect": "Allow",
            "Action": [
                "cloudformation:TagResource"
            ],
            "Resource": "arn:aws:cloudformation:*:*:stack/*"
        },
        {
            "Sid": "CreateRefactorSpacesSLR",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "refactor-spaces.amazonaws.com"
                }
            }
        },
        {
            "Sid": "CreateELBSLR",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "elasticloadbalancing.amazonaws.com"
                }
            }
        }
    ]
}
```

## AWS managed policy:

AWSMigrationHubRefactorSpaces-SSMAutomationPolicy

To grant the permissions that are required to run SSM Automation, use this AWS
managed policy in the IAM service role passed to the
`AWSRefactorSpaces-CreateResources` automation document. This policy
grants read and write access to tags to track the progress of the automation. When the
Refactor Spaces environment’s network bridge is enabled, the automation also adds the
environment’s security group to the Amazon EC2 instance to permit traffic from other
Refactor Spaces services in the environment. This policy also grants access to the SSM
parameters of the Application Migration Service post-launch action.

###### Important

When you use the `AWSMigrationHubRefactorSpaces-SSMAutomationPolicy`
managed policy, the role must also use either [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess") or [AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess"),
along with the extra required permissions that are described under these two
policies.

**Permissions details**

The `AWSMigrationHubRefactorSpaces-SSMAutomationPolicy` policy includes the
following permissions.

- `ec2:DescribeInstanceStatus` – required to validate that the
  Amazon EC2 instance exists.
- `ec2:CreateTags` and `ec2:DeleteTags` – required
  for tagging the Amazon EC2 instance. Tagging is needed for the automation to check if
  the script has already run against the Amazon EC2 instance. Deletion is needed for
  rollback in case of errors.
- `ec2:DescribeInstances` – required for the script to fetch
  all the security groups that are attached to an instance.
- `ec2:ModifyInstanceAttribute` – required when the Refactor Spaces
  environment’s network bridge is enabled. This permission allows the script to
  add the environment’s security group to the Amazon EC2 instance to permit traffic
  from other Refactor Spaces services in the environment.
- `ssm:GetParameters` – required to get the user-provided
  input values that are stored in the SSM parameter store.

The following is the `AWSMigrationHubRefactorSpaces-SSMAutomationPolicy`
that you need to use in the IAM role that you pass to the SSM automation document
`AWSRefactorSpaces-CreateResources` to grant the permissions that are
required to run the automation.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstanceStatus",
                "ec2:DescribeInstances"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:ModifyInstanceAttribute"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/refactor-spaces:ssm:optin": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:ModifyInstanceAttribute"
            ],
            "Resource": "arn:aws:ec2:*:*:security-group/*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags",
                "ec2:DeleteTags"
            ],
            "Resource": "arn:aws:ec2:*:*:instance/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/refactor-spaces:ssm:optin": "true"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": "refactor-spaces:ssm:environment-id"
                }
            }
        },
        {
            "Action": "ssm:GetParameters",
            "Resource": "arn:aws:ssm:*:*:parameter/ManagedByAWSApplicationMigrationService-*",
            "Effect": "Allow"
        }
    ]
}
```

## Refactor Spaces updates to AWS managed

policies

View details about updates to AWS managed policies for Refactor Spaces since this service
began tracking these changes. For automatic alerts about changes to this page, subscribe
to the RSS feed on the Refactor Spaces Document history page.

| Change                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | Description                                                                                                                                                                                                                                                                                                                       | Date              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- |
| Updated the [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess") and [AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess")<br>policies to allow the `cloudformation:TagResource`<br>action.                                                                                                                                                                                                                                                                                                         | To accommodate a change in CloudFormation, the two policies now allow the<br>`cloudformation:TagResource` action.                                                                                                                                                                                                                 | April 11, 2024    |
| [AWSMigrationHubRefactorSpaces-SSMAutomationPolicy](#SSMAutomationPolicy "#SSMAutomationPolicy")<br>– New policy                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | To grant the permissions that are required to run SSM Automation,<br>use this AWS managed policy in the IAM service role passed to the<br>`AWSRefactorSpaces-CreateResources` automation<br>document.                                                                                                                             | August 10, 2023   |
| Changed the resource element in statements that have the following<br>action element:<br>`<br>"Action": ["elasticloadbalancing:AddTags", "elasticloadbalancing:CreateListener"]<br>`<br>This change affects [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess"), [AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess"),<br>and [MigrationHubRefactorSpacesServiceRolePolicy](using-service-linked-roles.md#slr-permissions-iam-policy "using-service-linked-roles.md#slr-permissions-iam-policy"). | Updated NLB permissions to work with ELBv2 IAM changes.                                                                                                                                                                                                                                                                           | July 20, 2023     |
| [AWS managed policy:<br>AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess") – Added the<br>`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`<br>managed policy that you use when creating environments without a<br>Transit Gateway.                                                                                                                                                                                                                                                                                                                                                                    | Use the<br>`AWSMigrationHubRefactorSpaces-EnvironmentsWithoutBridgesFullAccess`<br>policy when you create environments without a network bridge. Since<br>you are using your own network infrastructure, the modified policy<br>Transit Gateway permissions and Amazon EC2 security groups related to Transit Gateway<br>actions. | April 3, 2023     |
| [MigrationHubRefactorSpacesServiceRolePolicy](using-service-linked-roles.md#slr-permissions-iam-policy "using-service-linked-roles.md#slr-permissions-iam-policy") – Added the<br>ELB `DeregisterTargets` permission to the policy.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `MigrationHubRefactorSpacesServiceRolePolicy` provides<br>access to AWS resources managed or used by AWS Migration Hub Refactor Spaces. The<br>`AWSServiceRoleForMigrationHubRefactorSpaces`<br>service-linked role uses this policy.                                                                                             | October 28, 2022  |
| [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess") – Added<br>ELB tagging permissions.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The `AWSMigrationHubRefactorSpacesFullAccess` policy<br>grants full access to Refactor Spaces, the Refactor Spaces console features and<br>other related AWS services.                                                                                                                                                            | October 6, 2022   |
| [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess") – Removed<br>the permission for creating tags for Amazon EC2 instances. This<br>permission was added to [Extra required<br>permissions for Refactor Spaces](#security-iam-awsmanpol-extra-permissions "#security-iam-awsmanpol-extra-permissions").                                                                                                                                                                                                                                                                                                                                                                                                    | The `AWSMigrationHubRefactorSpacesFullAccess` policy<br>grants full access to Refactor Spaces, the Refactor Spaces console features and<br>other related AWS services.                                                                                                                                                            | March 21, 2022    |
| [AWSMigrationHubRefactorSpacesFullAccess](#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess") – New<br>policy made available at launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | The `AWSMigrationHubRefactorSpacesFullAccess` policy<br>grants full access to Refactor Spaces, the Refactor Spaces console features and<br>other related AWS services.                                                                                                                                                            | November 29, 2021 |
| [MigrationHubRefactorSpacesServiceRolePolicy](using-service-linked-roles.md#slr-permissions "using-service-linked-roles.md#slr-permissions") – New<br>policy made available at launch                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | `MigrationHubRefactorSpacesServiceRolePolicy` provides<br>access to AWS resources managed or used by AWS Migration Hub Refactor Spaces. The<br>`AWSServiceRoleForMigrationHubRefactorSpaces`<br>service-linked role uses this policy.                                                                                             | November 29, 2021 |
| Refactor Spaces started tracking<br>changes                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Refactor Spaces started tracking changes for its AWS managed<br>policies.                                                                                                                                                                                                                                                         | November 29, 2021 |

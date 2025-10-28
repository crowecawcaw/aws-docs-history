AWS Migration Hub Refactor Spaces will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub Refactor Spaces, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Using service-linked roles for

Refactor Spaces

AWS Migration Hub Refactor Spaces uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role
that is linked directly to Refactor Spaces. Service-linked roles are predefined by
Refactor Spaces and include all the permissions that the service requires to call other AWS
services on your behalf.

A service-linked role makes setting up Refactor Spaces easier because you don’t have to
manually add the necessary permissions. Refactor Spaces defines the permissions of its
service-linked roles, and unless defined otherwise, only Refactor Spaces can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your Refactor Spaces resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS Services
That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-Linked Role** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role permissions for

Refactor Spaces

Refactor Spaces uses the service-linked role named **AWSServiceRoleForMigrationHubRefactorSpaces** and
associates it with the **MigrationHubRefactorSpacesServiceRolePolicy** IAM policy –
Provides access to AWS resources managed or used by AWS Migration Hub Refactor Spaces.

The AWSServiceRoleForMigrationHubRefactorSpaces service-linked role trusts the following services to assume the
role:

- `refactor-spaces.amazonaws.com`

The following is the Amazon Resource Name (ARN) for AWSServiceRoleForMigrationHubRefactorSpaces.

```
arn:aws:iam::111122223333:role/aws-service-role/refactor-spaces.amazonaws.com/AWSServiceRoleForMigrationHubRefactorSpaces
```

Refactor Spaces uses the **AWSServiceRoleForMigrationHubRefactorSpaces** service-linked role when performing
cross-account changes. This role must be present in your account to use Refactor Spaces. If it
is not present, Refactor Spaces creates it during the following API calls:

- `CreateEnvironment`
- `CreateService`
- `CreateApplication`
- `CreateRoute`

You must have `iam:CreateServiceLinkedRole` permissions to create the
service-linked role. If the service-linked role doesn't exist in your account and cannot
be created, the `Create` calls will fail. You must create the service-linked
role in the IAM console before using Refactor Spaces, unless you are using the Refactor Spaces
console.

Refactor Spaces does not use the service-linked role when making changes in the current
signed-in account. For example, when an application is created, Refactor Spaces updates all of
the VPCs in the environment so that they can communicate with the newly added VPC. If
the VPCs are in other accounts, Refactor Spaces uses the service-linked role and the
`ec2:CreateRoute` permission to update the route tables in other
accounts.

To further expand on the create application example, when creating an application,
Refactor Spaces updates the route tables that are in the virtual private cloud (VPC) provided
in the `CreateApplication` call. This way, the VPC can communicate with other
VPCs in the environment.

The caller must have the `ec2:CreateRoute` permission that we use to update
the route tables. This permission exists in the service-linked role, but Refactor Spaces does
not use the service-linked role in the caller’s account to gain this permission.
Instead, the caller must have the `ec2:CreateRoute` permission. Otherwise,
the call fails.

You cannot use the service-linked role to escalate your privileges. Your account must
already have the permissions in the service-linked role to make the changes in the
calling account. The `AWSMigrationHubRefactorSpacesFullAccess` managed
policy, together with a policy that grants the extra required permissions, defines all
of the necessary permissions to create Refactor Spaces resources. The service-linked role is a
subset of these permissions that is used for specific cross-account calls. For more
information about `AWSMigrationHubRefactorSpacesFullAccess`, see [AWS
managed policy: AWSMigrationHubRefactorSpacesFullAccess](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess "security-iam-awsmanpol.md#security-iam-awsmanpol-AWSMigrationHubRefactorSpacesFullAccess").

### Tags

When Refactor Spaces creates resources in your account, they are tagged with the
appropriate Refactor Spaces resource ID. For example, the Transit Gateway created from
`CreateEnvironment` is tagged with the
`refactor-spaces:environment-id` tag with the environment ID as the
value. The API Gateway API created from `CreateApplication` is tagged with
`refactor-spaces:application-id` with the application ID as the
value. These tags allow Refactor Spaces to manage these resources. If you edit or remove
the tags, Refactor Spaces can no longer update or delete the resource.

### MigrationHubRefactorSpacesServiceRolePolicy

The role permissions policy named MigrationHubRefactorSpacesServiceRolePolicy allows Refactor Spaces to
complete the following actions on the specified resources:

Amazon API Gateway actions

`apigateway:PUT`

`apigateway:POST`

`apigateway:GET`

`apigateway:PATCH`

`apigateway:DELETE`

Amazon Elastic Compute Cloud actions

`ec2:DescribeNetworkInterfaces`

`ec2:DescribeRouteTables`

`ec2:DescribeSubnets`

`ec2:DescribeSecurityGroups`

`ec2:DescribeVpcEndpointServiceConfigurations`

`ec2:DescribeTransitGatewayVpcAttachments`

`ec2:AuthorizeSecurityGroupIngress`

`ec2:RevokeSecurityGroupIngress`

`ec2:DeleteSecurityGroup`

`ec2:DeleteTransitGatewayVpcAttachment`

`ec2:CreateRoute`

`ec2:DeleteRoute`

`ec2:DeleteTags`

`ec2:DeleteVpcEndpointServiceConfigurations`

AWS Resource Access Manager actions

`ram:GetResourceShareAssociations`

`ram:DeleteResourceShare`

`ram:AssociateResourceShare`

`ram:DisassociateResourceShare`

Elastic Load Balancing; actions

`elasticloadbalancing:DescribeTargetHealth`

`elasticloadbalancing:DescribeListener`

`elasticloadbalancing:DescribeTargetGroups`

`elasticloadbalancing:RegisterTargets`

`elasticloadbalancing:CreateLoadBalancerListeners`

`elasticloadbalancing:CreateListener`

`elasticloadbalancing:DeleteListener`

`elasticloadbalancing:DeleteTargetGroup`

`elasticloadbalancing:DeleteLoadBalancer`

`elasticloadbalancing:DeregisterTargets`

`elasticloadbalancing:AddTags`

`elasticloadbalancing:CreateTargetGroup`

The following is the full policy showing which resources the preceding actions
apply to:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcEndpointServiceConfigurations",
                "ec2:DescribeTransitGatewayVpcAttachments",
                "elasticloadbalancing:DescribeTargetHealth",
                "elasticloadbalancing:DescribeListeners",
                "elasticloadbalancing:DescribeTargetGroups",
                "ram:GetResourceShareAssociations"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:DeleteSecurityGroup",
                "ec2:DeleteTransitGatewayVpcAttachment",
                "ec2:CreateRoute",
                "ec2:DeleteRoute",
                "ec2:DeleteTags",
                "ram:DeleteResourceShare",
                "ram:AssociateResourceShare",
                "ram:DisassociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:environment-id": "false"
                }
            }
        },
        {
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
            "Effect": "Allow",
            "Action": [
                "apigateway:PUT",
                "apigateway:POST",
                "apigateway:GET",
                "apigateway:PATCH",
                "apigateway:DELETE"
            ],
            "Resource": [
                "arn:aws:apigateway:*::/restapis",
                "arn:aws:apigateway:*::/restapis/*",
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
            "Effect": "Allow",
            "Action": "apigateway:GET",
            "Resource": "arn:aws:apigateway:*::/vpclinks/*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteLoadBalancer",
            "Resource": "arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:AddTags",
                "elasticloadbalancing:CreateListener"
            ],
            "Resource": ["arn:*:elasticloadbalancing:*:*:loadbalancer/net/refactor-spaces-nlb-*", "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"],
            "Condition": {
                "Null": {
                    "aws:RequestTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:DeleteListener",
            "Resource": "arn:*:elasticloadbalancing:*:*:listener/net/refactor-spaces-nlb-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DeleteTargetGroup",
                "elasticloadbalancing:RegisterTargets"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DeregisterTargets"
            ],
            "Resource": "arn:*:elasticloadbalancing:*:*:targetgroup/refactor-spaces-tg-*",
            "Condition": {
                "Null": {
                    "aws:ResourceTag/refactor-spaces:route-id": "false"
                }
            }
        },
        {
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
        }
    ]
}
```

You must configure permissions to allow an IAM entity (such as a user, group, or
role) to create, edit, or delete a service-linked role. For more information, see [Service-Linked Role Permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for Refactor Spaces

You don't need to manually create a service-linked role. When you
create Refactor Spaces environment, application, service, or route resources in the AWS Management Console, the AWS CLI, or the AWS API, Refactor Spaces
creates the service-linked role for you. For more information about creating a
service-linked role for Refactor Spaces, see [Service-linked role permissions for
Refactor Spaces](#slr-permissions "#slr-permissions").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create Refactor Spaces environment, application, service, or route resources, Refactor Spaces creates the service-linked role for you again.

## Editing a service-linked role for Refactor Spaces

Refactor Spaces does not allow you to edit the AWSServiceRoleForMigrationHubRefactorSpaces service-linked role. After you
create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role
using IAM. For more information, see [Editing a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting a service-linked role for Refactor Spaces

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don’t have an unused entity that is
not actively monitored or maintained. However, you must clean up the resources for your
service-linked role before you can manually delete it.

###### Note

If the Refactor Spaces service is using the role when you try to delete the
resources, then the deletion might fail. If that happens, wait for a few minutes and
try the operation again.

To delete the Refactor Spaces resources used by AWSServiceRoleForMigrationHubRefactorSpaces, use the Refactor Spaces console to
delete the resources, or use the delete API operations for the resources. For more
information about the delete API operations, see [Refactor Spaces API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForMigrationHubRefactorSpaces
service-linked role. For more information, see [Deleting a Service-Linked Role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for Refactor Spaces service-linked

roles

Refactor Spaces supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Regions and Endpoints](../../../general/latest/gr/rande.md "../../../general/latest/gr/rande.md").

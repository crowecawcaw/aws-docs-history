End of support notice: On June 30, 2027, AWS
will end support for AMS Advanced. After June 30, 2027, you will
no longer be able to access the AMS Advanced console or AMS Advanced resources.
For more information, see [AMS Advanced end of support](../userguide/SunsetPlan.md "../userguide/SunsetPlan.md").

# IAM user role in AMS

An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity
can and can't do in AWS.
However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it.

Currently there is one AMS default user role, `Customer_ReadOnly_Role`, for standard AMS accounts and an
additional role, `customer_managed_ad_user_role` for AMS accounts with Managed Active Directory.

The role policies set permissions for CloudWatch and Amazon S3 log actions, AMS console access,
read-only restrictions on most AWS services, restricted access to account S3 console, and
AMS change-type access.

Additionally, the `Customer_ReadOnly_Role` has mutative, reserved-instances
permissions that allow you to reserve instances. It has some cost-saving values, so, if you
know that you're going to need a certain number of Amazon EC2 instances for a long period of time,
you can call those APIs. To learn more, see
[Amazon EC2 Reserved Instances](https://aws.amazon.com/ec2/pricing/reserved-instances/ "https://aws.amazon.com/ec2/pricing/reserved-instances/").

###### Note

The AMS service level objective (SLO) for creating custom IAM policies for IAM users is four business days,
unless an existing policy is going to be reused. If you want to modify the existing IAM user role, or add a new one, submit an

[IAM: Update Entity](../ctref/management-advanced-identity-and-access-management-iam-update-entity-or-policy-review-required.md "../ctref/management-advanced-identity-and-access-management-iam-update-entity-or-policy-review-required.md") or
[IAM: Create Entity](../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy.md "../ctref/deployment-advanced-identity-and-access-management-iam-create-entity-or-policy.md") RFC, respectively.

If you're unfamiliar with Amazon IAM roles, see
[IAM Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") for important information.

## MALZ: Default IAM User Roles

The following are the default MALZ user roles. To make sure that you have the
policy set that you need, or to review the policies, run the AWS Command Line Interface (AWS CLI) command
[`get-role`](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md")
or sign in to the AWS Management -
[IAM console](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/") and choose **Roles** in the navigation pane.

###### Note

The user roles are customizable and may differ on a per-account basis.
Instructions on finding your role are provided.

### Core OU account roles

A core account is an MALZ-managed infrastructure account. AMS multi-account landing zone Core accounts include a management account
and a networking account.

Core OU account: Common roles and policies| Role | Policy or policies |
| --- | --- |
| AWSManagedServicesReadOnlyRole | ReadOnlyAccess (Public AWS Managed Policy). |
| AWSManagedServicesCaseRole | ReadOnlyAccess |
| AWSSupportAccess (Public AWS Managed Policy). |
| AWSManagedServicesChangeManagementRole (Core account version) | ReadOnlyAccess |
| AWSSupportAccess |
| AMSChangeManagementReadOnlyPolicy |
| AMSChangeManagementInfrastructurePolicy |

Core OU account: Management account roles and policies| Role | Policy or policies |
| --- | --- |
| AWSManagedServicesBillingRole | AMSBillingPolicy (AMSBillingPolicy). |
| AWSManagedServicesReadOnlyRole | ReadOnlyAccess (Public AWS Managed Policy). |
| AWSManagedServicesCaseRole | ReadOnlyAccess |
| AWSSupportAccess (Public AWS Managed Policy). |
| AWSManagedServicesChangeManagementRole (Management account version) | ReadOnlyAccess |
| AWSSupportAccess |
| AMSChangeManagementReadOnlyPolicy |
| AMSChangeManagementInfrastructurePolicy |
| `AMSMasterAccountSpecificChangeManagementInfrastructurePolicy` |

Core OU Account: Networking account roles and policies| Role | Policy or policies |
| --- | --- |
| AWSManagedServicesReadOnlyRole | ReadOnlyAccess (Public AWS Managed Policy). |
| AWSManagedServicesCaseRole | ReadOnlyAccess |
| AWSSupportAccess (Public AWS Managed Policy). |
| AWSManagedServicesChangeManagementRole (Networking account version) | ReadOnlyAccess |
| AWSSupportAccess |
| AMSChangeManagementReadOnlyPolicy |
| AMSChangeManagementInfrastructurePolicy |
| AMSNetworkingAccountSpecificChangeManagementInfrastructurePolicy |

### Application Account Roles

Application account roles are applied to your application-specific accounts.

Application account: Roles and policies| Role | Policy or policies |
| --- | --- |
| AWSManagedServicesReadOnlyRole | ReadOnlyAccess (Public AWS Managed Policy). |
| AWSManagedServicesCaseRole | ReadOnlyAccess |
| AWSSupportAccess (Public AWS Managed Policy).<br>This policy provides access to all support operations and resources. For<br>information, see [Getting Started with AWS Support](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md"). |
| AWSManagedServicesSecurityOpsRole | ReadOnlyAccess |
| AWSSupportAccess Example<br>This policy provides access to all support operations and resources. |
| [`AWSCertificateManagerFullAccess`](../../../acm/latest/userguide/authen-awsmanagedpolicies.md#acm-full-access-managed-policy "../../../acm/latest/userguide/authen-awsmanagedpolicies.md#acm-full-access-managed-policy") information, (Public AWS Managed Policy) |
| [`AWSWAFFullAccess`](../../../waf/latest/developerguide/access-control-identity-based.md "../../../waf/latest/developerguide/access-control-identity-based.md") information, (Public AWS Managed policy). This policy grants full access to AWS WAF resources. |
| AMSSecretsManagerSharedPolicy |
| AWSManagedServicesChangeManagementRole (Application account version) | ReadOnlyAccess |
| AWSSupportAccess (Public AWS Managed Policy).<br>This policy provides access to all support operations and resources. For<br>information, see [Getting Started<br>with AWS Support](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md"). |
| AMSSecretsManagerSharedPolicy |
| AMSChangeManagementPolicy |
| AMSReservedInstancesPolicy |
| AMSS3Policy |
| AWSManagedServicesAdminRole | ReadOnlyAccess |
| AWSSupportAccess |
| AMSChangeManagementInfrastructurePolicy |
| AWSMarketplaceManageSubscriptions |
| AMSSecretsManagerSharedPolicy |
| AMSChangeManagementPolicy |
| AWSCertificateManagerFullAccess |
| AWSWAFFullAccess |
| AMSS3Policy |
| AMSReservedInstancesPolicy |

## SALZ: Default IAM User Role

The following are the default SALZ user roles. To make sure that you have the
policies set for you, or to review the policies, run the
[`get-role`](../../../cli/latest/reference/iam/get-role.md "../../../cli/latest/reference/iam/get-role.md") command. Or,
sign in to the AWS Identity and Access Management console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"), and then choose
**Roles**.

###### Note

The SALZ default user role is customizable and might differ on a per-account basis.
Instructions on finding your role are provided.

The customer read-only role is a combination of multiple policies. A breakdown of the role
follows.

- Managed Services Audit Policy
- Managed Services IAM ReadOnly Policy
- Managed Services User Policy
- Customer Secrets Manager Shared Policy
- Customer Marketplace Subscribe Policy

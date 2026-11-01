

# Prerequisites
<a name="managed-entitlements-prerequisites"></a>

Before you can use managed entitlements for Amazon Bedrock, you must complete the following prerequisites.

**Recommendation**: If you use AWS Organizations, request that private offers for third-party models in Amazon Bedrock be issued to your management account. When you accept the offer from your management account, you can distribute it to every account in your organization directly from AWS Marketplace, immediately after you accept it.

If you prefer to manage private offers from an account other than your management account, you can register that account as your delegated administrator instead. You must complete delegated administrator registration before you accept the private offer, and you must accept the offer from that same account. To register a delegated administrator, see [Step 1: Determine if you need a delegated admin](managed-entitlements-setup.md#managed-entitlements-delegated-admin).

If you accept the private offer from any other account, you cannot distribute it from AWS Marketplace. You must create grants in AWS License Manager instead, as described in [Distribute through AWS License Manager](managed-entitlements-license-manager.md).

## AWS Organization requirements
<a name="managed-entitlements-org-requirements"></a>

**All features enabled**: Your AWS Organization must have all features enabled. Managed Entitlements for Bedrock requires this configuration to function properly. If your organization uses consolidated billing only, you must enable all features before proceeding. To enable all features, see [Enabling all features in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) in the AWS Organizations User Guide.

To check if your organization has all features enabled, navigate to the AWS Organizations console, choose Settings in the navigation pane, and look for Feature set under Organization details. If it displays All features, you are ready to proceed.

**Management account access**: You must have access to your organization's management account (also called the payer account) to complete the initial setup. The management account is required to enable trusted access and create service-linked roles.

**Member accounts associated**: All member accounts that will receive license grants must already be part of your AWS Organization. If you plan to add new accounts, they will automatically receive any licenses granted to your organization ID.

## Service-linked roles
<a name="managed-entitlements-slr"></a>

Service-linked roles (SLRs) are predefined IAM roles that are linked directly to AWS services. For Managed Entitlements, you must create SLRs for both AWS License Manager and AWS Marketplace. These roles include all permissions that the services require to call other AWS services on your behalf.

**Why SLRs are required**: For AWS Marketplace, this permission is required so that the service can successfully orchestrate license workflows and distributions across multiple AWS services on your behalf. For AWS License Manager, this permission enables the service to auto-accept grants between management and member accounts in an all-features-enabled organization and to track organization activity.

You will create these service-linked roles as part of the setup process described in the next section.

**Note**  
If you distribute a private offer for a third-party model in Amazon Bedrock from AWS Marketplace, License Manager automatically creates the required service-linked roles in every account in your organization. For more information, see [Using service-linked roles for License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/using-service-linked-roles.html). For all other subscriptions, create the service-linked roles as described in [Setting up managed entitlements](managed-entitlements-setup.md).

## Granting permissions to distribute from AWS Marketplace
<a name="managed-entitlements-marketplace-permissions"></a>

To distribute a private offer for a third-party model in Amazon Bedrock from AWS Marketplace, the IAM identity that accepts the offer needs the permissions in the following policy. The identity also needs permission to view and accept the private offer.

The `DistributeMarketplaceSubscription` statement covers the actions used on every distribution. The `FirstTimeOnboarding` statements cover the setup that AWS performs the first time your organization distributes from AWS Marketplace.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DistributeMarketplaceSubscription",
      "Effect": "Allow",
      "Action": [
        "organizations:DescribeOrganization",
        "organizations:ListDelegatedAdministrators",
        "organizations:ListAWSServiceAccessForOrganization",
        "license-manager:GetServiceSettings",
        "license-manager:ListReceivedLicenses",
        "license-manager:ListReceivedGrants",
        "license-manager:ListDistributedGrants",
        "license-manager:GetGrant",
        "license-manager:GetLicense",
        "license-manager:CreateGrant",
        "license-manager:CreateGrantVersion"
      ],
      "Resource": "*"
    },
    {
      "Sid": "FirstTimeOnboardingLM",
      "Effect": "Allow",
      "Action": [
        "license-manager:UpdateServiceSettings"
      ],
      "Resource": "*"
    },
    {
      "Sid": "FirstTimeOnboardingIAM",
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": [
            "license-manager.amazonaws.com",
            "license-manager.master-account.amazonaws.com",
            "license-management.marketplace.amazonaws.com"
          ]
        }
      }
    },
    {
      "Sid": "FirstTimeOnboardingOrganization",
      "Effect": "Allow",
      "Action": "organizations:EnableAWSServiceAccess",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "organizations:ServicePrincipal": [
            "license-manager.amazonaws.com",
            "license-manager.member-account.amazonaws.com"
          ]
        }
      }
    }
  ]
}
```

For all other subscriptions, the permissions in [Setting up managed entitlements](managed-entitlements-setup.md) and [Distributing licenses](managed-entitlements-distributing.md) still apply.


# Sharing your licenses
<a name="sharing-licenses"></a>

Only AMI, container, machine learning, data products, Oracle Database@AWS, and third-party Amazon Bedrock model subscriptions have licenses that can be shared.

Subscriptions in AWS Marketplace have an **Access level** shown in the product details:
+ Products with an **Agreement** level have a license that you can use and share with other accounts in your organization. 
+ Products with an **Entitlement** level are licenses that have been shared with your account—you can use these products, but you can't share them.

AWS Marketplace supports grants, which share the use of a license directly with AWS Organizations, an AWS account, or an organizational unit using AWS License Manager. The grant activation process now includes additional options to replace grants that are activated for the same product sourced from AWS Marketplace. For more information, see [Granted licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html) in the *AWS License Manager User Guide*.

**Note**  
For products that are restricted to specific AWS Regions, an account you share your license with can only activate the license if the account is within an allowed Region.

## Required permissions for license distribution
<a name="license-sharing-required-permissions"></a>

To distribute licenses, sign in to your organization's management account or your delegated administrator account. The IAM identity that you use needs the permissions in the following policy. To distribute a private offer when you accept it, the identity also needs permission to view and accept the private offer, for example through the `AWSMarketplaceManageSubscriptions` managed policy.

The `DistributeMarketplaceSubscription` statement covers the actions used on every distribution. The `FirstTimeOnboarding` statements cover the setup that AWS License Manager performs the first time your organization distributes licenses.

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

## Distributing third-party Amazon Bedrock model licenses
<a name="license-sharing-bedrock"></a>

If you accept a private offer for a third-party model in Amazon Bedrock from your management account or your delegated administrator account, you can distribute it to every account in your organization on the purchase confirmation page, right after you accept the offer. AWS License Manager completes the license sharing prerequisites for you. It creates the required service-linked roles and links your organization accounts.

You can't distribute private offers that you accept as part of an offer set from the purchase confirmation page. To distribute these offers, public offers, or licenses for specific accounts or organizational units (OUs), use AWS License Manager.

For more information, see the following topics in the *Amazon Bedrock User Guide*:
+ [Distribute through AWS Marketplace](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-marketplace.html)
+ [Distribute through AWS License Manager](https://docs.aws.amazon.com/bedrock/latest/userguide/managed-entitlements-license-manager.html)

## Distributing other licenses
<a name="license-sharing-other"></a>

For AMI, container, machine learning, data products, and Oracle Database@AWS subscriptions, set up license sharing for your organization, and then share licenses by using grants in AWS License Manager.

### Prerequisites for license sharing
<a name="license-sharing-prereqs"></a>

Before you can share licenses in AWS Marketplace you must set up license sharing for your organization. Complete the following tasks to set up license sharing for your organization:
+ Give AWS Marketplace permission to manage licenses on your behalf so that it can create the associated license grants when you purchase or share your licenses. For more information, see [Service-linked role to share entitlements for AWS Marketplace](buyer-using-service-linked-roles-license-manager.md).
+ Set up AWS License Manager for first use. For more information, see [ Getting started with AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/getting-started.html) in the *AWS License Manager User Guide*.
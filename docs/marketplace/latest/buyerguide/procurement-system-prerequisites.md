

# Prerequisites for procurement system integration

Before you can connect a procurement system to AWS Marketplace, two things need to be in place: Private Marketplace, and the permissions for the two personas involved, the administrator and the buyer.

## Private Marketplace
<a name="procurement-system-prerequisites-pmp"></a>

Private Marketplace is where the governance you apply to AWS Marketplace purchasing lives: which products your buyers can see, whether a purchase order is required, and the approval rules. It must be enabled for your organization before you can add any of those rules.

Enabling it is a one-time setup, done from your management account. It covers checking that your organization is ready, turning the feature on, and creating the service-linked role Private Marketplace uses to act on your behalf.

See [Prerequisites](prerequisites.md) for Private Marketplace, and then [Getting started](get-started.md) for the steps to enable it.

## Permissions
<a name="procurement-system-prerequisites-permissions"></a>

Procurement system integration involves two personas. The administrator connects the procurement tool and configures the approval rules. The buyer finds products in AWS Marketplace and submits purchases for approval. Those are different jobs, so each persona needs a different set of permissions.

Use the IAM managed policies rather than setting permissions by hand. They're less prone to error, and AWS updates them when the permissions change.

Administrator  
Configures the integration from your organization's management account, and needs all of the following:  
+ `AWS managed policy: AWSPrivateMarketplaceAdminFullAccess`, to manage Private Marketplace, which is where your approval rules live.
+ An account in your procurement system with enough access to set up a punchout catalog. AWS doesn't grant this access. It comes from your procurement system, so whoever administers it there has to be involved.

Buyer  
Purchases from AWS Marketplace and needs `AWS managed policy: AWSMarketplaceManageSubscriptions` to subscribe to products and to manage their subscriptions.

For more information about using IAM with AWS Marketplace, see [Security on AWS Marketplace](buyer-security.md).

## What to do next
<a name="procurement-system-prerequisites-next"></a>

With the prerequisites in place, setting up the integration takes two steps.

**To set up the integration**

1. Connect your procurement system on the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page. For detailed configuration steps, see [Configuring AWS Marketplace to integrate with Coupa](procurement-system-integration-coupa.md) or [Configuring AWS Marketplace to integrate with SAP Ariba](procurement-system-integration-ariba.md).

1. Configure the approval rules that govern which purchases go there, on the [**Procurement approval rules**](https://console.aws.amazon.com/marketplace/buying-policies/procurement-approval-rules?region=us-east-1) page. For more information about approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).

Both steps matter. A connection makes your procurement system available as a destination, and the rules decide what arrives there.
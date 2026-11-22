

# Configuring buying policies in AWS Marketplace

Buying policies give procurement, finance, and cloud governance teams control over how purchases in AWS Marketplace are approved. While Private Marketplace controls *which* products users in your organization can buy, buying policies control *how* individual purchases are approved and what buyers must provide at the point of purchase.

With buying policies, administrators can do the following:
+ **Require approval for purchases** – Create procurement approval rules that decide which purchases need review, or decline, and where each request is sent. Requests can go to your organization administrator in the AWS Marketplace console, to an approval chain of email approvers who don't need an AWS account, or to a connected procurement system such as Coupa or SAP Ariba. For more information, see [Configuring buyer approvals](buyer-approvals.md).
+ **Require purchase order numbers** – Require buyers to enter a purchase order number before they subscribe, for specific offer types and pricing types. For more information, see [Configuring purchase order number requirement settings](po-number-requirement-settings.md).
+ **Display a procurement administrator message** – Explain your organization's procurement requirements to buyers on AWS Marketplace procurement pages. For more information, see [Configuring custom procurement messaging](po-number-requirement-settings.md#bp-custom-procurement-messaging).

Buying policies work with the other governance capabilities in AWS Marketplace. For example, you can use Private Marketplace to restrict which products are available, buyer approvals to govern individual purchases, purchase order number requirements to require a purchase order before subscribing, and a blanket usage purchase order (one purchase order that covers ongoing usage charges) to capture charges for purchases that don't need individual approval. For more information about blanket usage purchase orders, see [Using blanket-usage purchase orders](buyer-purchase-orders.md#buyer-using-blanket-usage).

**Required permissions**  
To configure buying policies, sign in to the management account of your AWS organization or a delegated administrator account, and attach the `AWSPrivateMarketplaceAdminFullAccess` AWS managed policy to your IAM user or role. For more information, see [AWS managed policy: AWSPrivateMarketplaceAdminFullAccess](buyer-security-iam-awsmanpol.md#security-iam-awsmanpol-awsprivatemarketplaceadminfullaccess).  
To view, approve, or decline purchase approval requests in the AWS Marketplace console, see [Permissions for approval requests in the AWS Marketplace console](buyer-approvals-console-permissions.md).  
Buying policies are AWS Marketplace purchasing settings. They're separate from IAM policies and Organizations policies, such as service control policies (SCPs).

## Prerequisites for buying policies
<a name="buying-policies-prerequisites"></a>

Before you can configure buying policies, you must create a Private Marketplace integration with AWS Organizations from your AWS management account. This one-time setup enables trusted access across your organization and creates the necessary service-linked role. If you already created this integration for Private Marketplace, you can skip this setup.

**To set up buying policies**

1. Using your AWS management account, open [Buying policies](https://console.aws.amazon.com/marketplace/buying-policies) in the AWS Marketplace console.

1. Choose **Get started**.

1. Under **Organizations integration settings**, select **Enable trusted access across your AWS organization**.

1. Select **Create a Private Marketplace service-linked role for this account**.

1. Choose **Create integration**.

**Note**  
After an integration is created, you can't undo it from the AWS Marketplace console. To delete the service-linked role, use IAM. To disable trusted access, use Organizations.

After the integration is created, you return to the **Buying policies** page, where you can configure procurement approval rules, purchase order number requirements, and the procurement administrator message for your organization.
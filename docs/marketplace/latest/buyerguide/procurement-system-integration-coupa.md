# Configuring AWS Marketplace to integrate with Coupa

The topics in this section explain how to integrate AWS Marketplace with a Coupa procurment system

## Step 1. Set up IAM permissions

To configure the integration between AWS Marketplace and your procurement system, you start the process in AWS Marketplace and complete it in the procurement system.
You use the information generated in AWS Marketplace to configure the procurement system punchout.
To complete the configuration, the accounts that you use must meet the following requirements:

- The AWS account used to complete the AWS Marketplace configuration must be the management
  account and have the IAM permissions defined in the
  `AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess` managed policy.

We recommend that you use IAM managed permissions rather than manually configuring permissions.
Using this approach is less prone to human error, and if the permissions change, the managed policy is updated.
For more information about configuring and using IAM in AWS Marketplace, see [Security on AWS Marketplace](buyer-security.md "buyer-security.md") later in this guide.

- The procurement system account used to complete the configuration must have
  administration access to set up a contract, supplier, and punchout catalog in the
  procurement system.

## Step 2. Configure AWS Marketplace to integrate with Coupa

After you have set up your IAM permissions, you are ready to configure AWS Marketplace integration
with Coupa. Navigate to **Manage procurement**. In the **Manage
procurement systems** pane, enter a name and description for the punchout. You can
also switch the integration to test mode so that users can test the integration without
creating product subscriptions until you're ready. To configure the AWS Marketplace portion of the
integration, complete the following procedure.

###### To configure AWS Marketplace for integrating with Coupa

1. From [AWS Marketplace Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview "https://aws.amazon.com/marketplace/eprocurement/overview"), under **Procurement
   systems**, choose **Set up Coupa integration**.
2. On the **Manage Coupa integration** page, under **Account
   information**, enter the name and description of your integration.

###### Note

You might want your invoices in the AWS Billing console to reference the commerce
extensible markup language (cXML) purchase order used to subscribe to your software as a
service (SaaS) contract product. If so, you can enable the AWS Billing integration using a
service-linked role in AWS Marketplace settings. 3. You can turn on or turn off the configuration settings for **Enable
redirect** and **Test mode**, and then select
**Save** to complete the integration in the AWS Marketplace system.

After you have completed the integration in AWS Marketplace, you must go on to set up the
integration in Coupa. You use the information generated on this page to configure the punchout
in your Coupa system.

The AWS Marketplace configuration defaults to test mode being enabled. In test mode, subscription
requests go to the Coupa backend so you can see the full flow, but a final invoice is not
created. This helps you complete the configuration and enable the punchout in a planned
manner.

###### Note

You can toggle testing mode on or off, as needed.

Don't forget to turn off testing mode when you're finished with your integration.
Otherwise, users in your system will appear to be creating requests, but no software will be
purchased.

## Step 3. Configure Coupa

To configure the integration with AWS Marketplace in your Coupa system, copy the information
from the **Purchase information** pane of the **Manage Coupa
integration** page in AWS Marketplace. Use this information to complete the steps in
the following links that guide you through configuring your Coupa procurement system:

- [Coupa Punchout Setup](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Manage_Catalogs/Punchout_Catalogs/Punchout_Setup "https://success.coupa.com/Suppliers/For_Customers/Toolkit/Manage_Catalogs/Punchout_Catalogs/Punchout_Setup")
- [Configuring a Supplier for cXML Purchase Orders](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Document_Exchange/cXML/Configuring_a_Supplier_for_cXML_Purchase_Orders "https://success.coupa.com/Suppliers/For_Customers/Toolkit/Document_Exchange/cXML/Configuring_a_Supplier_for_cXML_Purchase_Orders")

###### Note

For information about UNSPSC codes used by AWS Marketplace, see [UNSPSC codes used by
AWS Marketplace](procurement-system-integration.md#procurement-integration-setup-unspsc-codes "procurement-system-integration.md#procurement-integration-setup-unspsc-codes") .



# Configuring AWS Marketplace to integrate with Coupa
<a name="procurement-system-integration-coupa"></a>

The topics in this section explain how to integrate AWS Marketplace with a Coupa procurment system 

## Step 1. Set up IAM permissions
<a name="procurement-system-coupa-step1"></a>

To configure the integration between AWS Marketplace and your procurement system, you start the process in AWS Marketplace and complete it in the procurement system. You use the information generated in AWS Marketplace to configure the procurement system punchout. To complete the configuration, the accounts that you use must meet the following requirements:
+ The AWS account used to complete the AWS Marketplace configuration must be the management account and have the IAM permissions defined in the `AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess` managed policy.

  We recommend that you use IAM managed permissions rather than manually configuring permissions. Using this approach is less prone to human error, and if the permissions change, the managed policy is updated. For more information about configuring and using IAM in AWS Marketplace, see [Security on AWS Marketplace](buyer-security.md) later in this guide.
+  The procurement system account used to complete the configuration must have administration access to set up a contract, supplier, and punchout catalog in the procurement system.

## Step 2. Configure AWS Marketplace to integrate with Coupa
<a name="procurement-system-coupa-step2"></a>

After you have set up your IAM permissions, you are ready to configure AWS Marketplace integration with Coupa. Navigate to **Manage procurement**. In the **Manage procurement systems** pane, you configure a billing entity connection with the credentials and settings for your Coupa integration. You can also switch the integration to test mode so that users can test the integration without creating product subscriptions until you're ready. To configure the AWS Marketplace portion of the integration, complete the following procedure.

**To configure AWS Marketplace for integrating with Coupa**

1.  From [Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview), under **Procurement systems**, choose **Set up Coupa integration**. 

1.  On the **Manage Coupa integration** page, under **Account information**, enter a name and description for your integration, and then configure the following fields:
   + **Buyer ID** – Your organization's unique identifier in Coupa. This identifies your organization as the buyer in the cXML exchange with AWS Marketplace.
   + **Supplier ID** – The AWS Marketplace supplier identifier for your Coupa system. This identifies which AWS endpoint receives purchase orders from your procurement portal.
   + **Shared secret** – The credential used to authenticate the cXML communication between your Coupa system and AWS Marketplace. Keep this value secure.
   + **Billing entities** (optional) – Select the AWS Billing entities (Seller of Record) that match the AWS Billing entity that you are setting up. If you don't select any, the connection accepts purchases from all AWS Billing entities. Select specific entities if your procurement portal uses different supplier configurations for different AWS Invoicing regions.
**Note**  
If you want your invoices in the AWS Billing and Cost Management console to reference the commerce extensible markup language (cXML) purchase order used to subscribe to your software as a service (SaaS) contract product, enable the AWS Billing and Cost Management integration using a service-linked role in AWS Marketplace settings.

1. You can turn on or turn off the configuration settings for **Enable redirect** and **Test mode**, and then select **Save** to complete the integration in the AWS Marketplace system.

After your first connection is set up, you can add and manage additional connections for other billing entities from the **Manage Procurement Systems** page. Each connection uses its own set of credentials and can be scoped to different AWS Billing entities. To add a connection and manage the connections in your account, complete the following procedure.

**To add and manage additional Coupa connections**

1. From [Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview), review your existing connections in the **Portal connections** table. Each row lists the connection's **Buyer ID**, **Supplier ID**, **Seller of Record**, **PunchOut status**, along with the **View**, **Enable**, and **Disable** actions.

1. Under **New Coupa connections**, enter the connection details – **Buyer ID**, **Shared secret**, **Supplier ID**, and optionally **Seller of Record (SOR)** to scope the connection to specific billing entities.

1. Submit the form to create the connection. The new connection appears in the **Portal connections** table.

1. On the new connection's row, choose **Enable** to activate AWS Marketplace PunchOut for that connection.

1. To stop routing PunchOut through a connection, choose **Disable** on its row.
**Note**  
Disabling a connection is reversible. The connection remains in your account, and you can enable it again later. Disabling the last connection that has a redirect endpoint turns off direct punchout (redirect) for the account.

1. To see or edit a connection's details, choose **View** on its row.
**Note**  
You can't edit a connection's **Seller of Record** or **Shared secret** from the AWS Marketplace procurement connections page. To update either field, use the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/home#/e-invoicing-preference/procurement-portal-preference/).

After you have completed the integration in AWS Marketplace, you must go on to set up the integration in Coupa. You use the information generated on this page to configure the punchout in your Coupa system. 

The AWS Marketplace configuration defaults to test mode being enabled. In test mode, subscription requests are transmitted to the Coupa backend, but transmitted purchase orders will not result in a subscription and will not generate an invoice. This helps you complete the configuration and enable the punchout in a planned manner.

**Note**  
You can toggle testing mode on or off, as needed.  
Don't forget to turn off testing mode when you're finished with your integration. Otherwise, users in your system will appear to be creating requests, but no software will be purchased.

## Step 3. Configure Coupa
<a name="procurement-system-coupa-step3"></a>

 To configure the integration with AWS Marketplace in your Coupa system, your Coupa administrator will copy the information from the **Purchase information** pane of the **Manage Coupa integration** page in AWS Marketplace. To send purchase orders to AWS Marketplace, your Coupa administrator must turn on **Enable Mutual TLS for PO cXML** under the **PO Transmission** setup section of your Coupa Supplier Portal. Use this information to complete the steps in the following links that guide you through configuring your Coupa procurement system: 
+  [Coupa Punchout Setup](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Manage_Catalogs/Punchout_Catalogs/Punchout_Setup) 
+  [Configuring a Supplier for cXML Purchase Orders](https://success.coupa.com/Suppliers/For_Customers/Toolkit/Document_Exchange/cXML/Configuring_a_Supplier_for_cXML_Purchase_Orders) 

**Note**  
For information about UNSPSC codes used by AWS Marketplace, see [UNSPSC codes used by AWS Marketplace](procurement-system-integration.md#procurement-integration-setup-unspsc-codes) .

**Note**  
For information about CloudTrail events for invoicing actions used with procurement system integrations, see [Logging procurement system API calls with AWS CloudTrail](buyer-cloudtrail-logging.md).
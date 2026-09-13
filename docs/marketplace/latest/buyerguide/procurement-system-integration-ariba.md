

# Configuring AWS Marketplace to integrate with SAP Ariba
<a name="procurement-system-integration-ariba"></a>

The following topics explain how to configure AWS Marketplace to work with the SAP Ariba procurement system. Configuration enables users to search for and purchase AWS Marketplace software without having to leave SAP Ariba. 

## Setting up IAM permissions
<a name="procurement-system-ariba-step1"></a>

The configuration process starts in AWS Marketplace and finishes in the SAP Ariba. You use the information generated in AWS Marketplace to configure the procurement system punchout. To complete the configuration, the accounts you use must meet the following requirements:
+ The AWS account used to complete the AWS Marketplace configuration must be the management account and have the IAM permissions defined in the `AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess` managed policy.

  We recommend that you use IAM managed permissions rather than manually configuring permissions. This approach is less prone to human error, and if the permissions change, the managed policy is updated. For more information about configuring and using IAM in AWS Marketplace, see [ Security on AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security.html) later in this guide.
+  The procurement system account used to complete the configuration must have administration access to set up a contract, supplier, and punchout catalog in the procurement system.

## Step 2. Configure AWS Marketplace to integrate with SAP Ariba
<a name="procurement-system-ariba-step2"></a>

 To configure AWS Marketplace to integrate with Ariba, you must work with the AWS Marketplace operations team to create a Level 1 punchout. For more information about SAP Ariba punchout, see [Introduction to SAP Ariba PunchOut](https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634) on the *SAP Community* website.

Gather the following information in preparation for configuring the setup:
+ Your AWS account ID. If your AWS account is part of an AWS organization, then you also need the management account ID.
+ The Ariba network ID (ANID) for your SAP Ariba system.

**To configure AWS Marketplace for integrating with Ariba**

1.  From [Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview), under **Procurement systems**, choose **Set up Ariba integration**. 

1.  On the **Manage SAP Ariba integration** page, under **Account information**, enter a name and description for your integration, and then configure the following fields:
   + **Buyer ANID** – Your organization's Ariba Network ID. This is a unique identifier that starts with `AN` followed by 11 or 12 digits. You can find this in your SAP Ariba account settings.
   + **Supplier ANID** – The AWS Marketplace Ariba Network ID. Select the appropriate AWS supplier for your Region from the list.
   + **Billing entities** (optional) – Select the AWS billing entities (Seller of Record) that match the AWS billing entity that you are setting up. If you don't select any, the connection accepts purchases from all AWS billing entities. Select specific entities if your procurement portal uses different supplier configurations for different AWS Invoicing regions.
**Note**  
If you want your invoices in the AWS Billing and Cost Management console to reference the cXML purchase order used to subscribe to your SaaS contract product, enable the AWS Billing and Cost Management integration using a service-linked role in AWS Marketplace settings.

1. Ensure that **Test mode** is enabled, then select **Save** to save your AWS Marketplace integration settings.

1. [Contact us](https://aws.amazon.com/marketplace/help/contact-us) to start the process of creating your SAP Ariba integration. Include the above information. AWS Marketplace sends you instructions for setting up and testing your Ariba integration.

After your first connection is set up, you can add and manage additional connections for other billing entities from the **Manage Procurement Systems** page. Each connection uses its own ANID configuration and can be scoped to different AWS Billing entities. To add a connection and manage the connections in your account, complete the following procedure.

**To add and manage additional Ariba connections**

1. From [Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview), review your existing connections in the **Portal connections** table. Each row lists the connection's **Buyer ANID**, **Supplier ANID**, **Seller of Record**, **PunchOut status**, along with the **View**, **Enable**, and **Disable** actions.

1. Under **New SAP Ariba connections**, enter the connection details – **Buyer ANID**, **Supplier ANID**, and optionally **Seller of Record (SOR)** to scope the connection to specific billing entities.

1. Submit the form to create the connection. The new connection appears in the **Portal connections** table.

1. On the new connection's row, choose **Enable** to activate AWS Marketplace PunchOut for that connection.

1. To stop routing PunchOut through a connection, choose **Disable** on its row.
**Note**  
Disabling a connection is reversible. The connection remains in your account, and you can enable it again later. Disabling the last connection that has a redirect endpoint turns off direct punchout (redirect) for the account.

1. To see or edit a connection's details, choose **View** on its row.
**Note**  
You can't edit a connection's **Seller of Record** from the AWS Marketplace procurement connections page. To update it, use the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/home#/e-invoicing-preference/procurement-portal-preference/).

**Note**  
You need to have administrator access to your SAP Ariba system to create the **Supplier Relationship** with AWS Marketplace.

Following the instructions and configuration settings from the AWS Marketplace team, you create the integration in your SAP Ariba test environment, with AWS Marketplace running in *test mode*. In the test environment, subscription requests go to the Ariba backend so you can see the full flow including approvals, without creating a subscription in AWS Marketplace, and no invoice is generated. This approach enables testing the configuration before enabling the punchout in production. After your testing is complete and you are ready to move to production, [contact us](https://aws.amazon.com/marketplace/help/contact-us) to set up the account in the production environment.

**Note**  
Don't forget to move to production when you're finished with testing your integration. Otherwise, users in your system will believe that they're creating requests, but no software will be purchased.

When your testing is complete, and you have worked with the AWS Marketplace team to turn off test mode, your integration is complete.

For more information about configuring SAP Ariba, see [Introduction to SAP Ariba PunchOut](https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634) on the *SAP Community*.

**Note**  
For information about UNSPSC codes, see [UNSPSC codes used by AWS Marketplace](procurement-system-integration.md#procurement-integration-setup-unspsc-codes) .

**Note**  
For information about CloudTrail events for invoicing actions used with procurement system integrations, see [Logging procurement system API calls with AWS CloudTrail](buyer-cloudtrail-logging.md).
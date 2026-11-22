

# Configuring AWS Marketplace to integrate with SAP Ariba

The topics in this section explain how to integrate AWS Marketplace with an SAP Ariba procurement system. Unlike other procurement systems, an SAP Ariba integration is set up with an AWS Marketplace representative rather than entirely by you, and that includes single sign-on if you want it.

## Step 1. Check the prerequisites
<a name="procurement-system-ariba-step1"></a>

Configuration starts in AWS Marketplace, where you create the connection, and finishes in SAP Ariba when an AWS Marketplace representative publishes the catalog to your account. You supply information from the AWS Marketplace connection for that request, so you need access to both systems.

For the permissions and the other prerequisites, see [Prerequisites for procurement system integration](procurement-system-prerequisites.md).

## Step 2. Configure AWS Marketplace to integrate with SAP Ariba
<a name="procurement-system-ariba-step2"></a>

The connection holds the identifiers that identify your SAP Ariba system and AWS Marketplace to each other. Setting up SAP Ariba also requires a Level 1 punchout, which you create with the AWS Marketplace operations team rather than on your own.

### Your buyer ANID
<a name="procurement-system-ariba-identifiers"></a>

The one value to have ready before you start is your buyer Ariba Network ID (ANID), which identifies your organization as the buyer. It starts with `AN` followed by 11 or 12 digits, and you can find it in your SAP Ariba account settings.

The value must match the ANID registered in the Ariba Network exactly.

### Creating the connection
<a name="procurement-system-ariba-connection"></a>

**To create the connection in AWS Marketplace**

1. On the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page, choose **Connect**.

1. Choose **Add new SAP Ariba Connection**, and then complete the following fields in the form:
   + **Buyer ANID** – Your organization's Ariba Network ID.
   + **Supplier ANID** – The AWS Marketplace Ariba Network ID. Select from the list of available AWS suppliers.
   + **Seller of Record** – Select the AWS Billing entities that match the AWS Billing entity that you are setting up. If you don't select any, the connection accepts purchases from all AWS Billing entities. Select specific entities if you plan to use different supplier configurations for different AWS Billing entities.

1. Choose **Save** to complete the integration on the AWS Marketplace side.

The connection now appears in your list of procurement connections.

**Note**  
Creating a connection doesn't send any purchases to SAP Ariba on its own. You decide which purchases go there by writing approval rules. For more information about approval rules, see [Routing purchases to your procurement system](procurement-system-routing.md).

### Managing your connections
<a name="procurement-system-ariba-managing-connections"></a>

You can add and manage additional connections for other billing entities from the same page. Each connection uses its own ANID configuration and can be scoped to different AWS Billing entities.

**To manage your SAP Ariba connections**

1. On the [**External system**](https://console.aws.amazon.com/marketplace/buying-policies/approvers-and-routing?region=us-east-1&tab=external-system) tab of the **Approvers and routing** page, review your existing connections in the **Portal connections** table. Each row lists the connection's **Buyer ANID**, **Supplier ANID**, **Seller of Record**, and **AWS Marketplace PunchOut status**.

1. To turn AWS Marketplace PunchOut on or off for a connection, select the connection. An edit section appears, where you enable or disable it.
**Note**  
Disabling a connection is reversible. The connection remains in your account, and you can enable it again later.

1. To edit more of a connection's configuration than this page carries, including electronic invoicing and cloud purchase order retrieval, use the [AWS Billing and Cost Management console](https://console.aws.amazon.com/costmanagement/home#/e-invoicing-preference/procurement-portal-preference/).

## Step 3. Request catalog publishing
<a name="procurement-system-ariba-step3"></a>

The AWS Marketplace catalog has to be published to your SAP Ariba account before your buyers can reach it. Publishing is done by an AWS Marketplace representative rather than by you. What you supply is the information that tells us where to publish it.

Two identifiers decide that, and you have both already from step 2: your buyer ANID, which identifies your organization in the Ariba Network, and the supplier ANID of the AWS Marketplace supplier you chose to purchase through.

An AWS Marketplace representative publishes the catalog to your buyer ANID for that supplier ANID. Until that has happened, the catalog doesn't appear in SAP Ariba for your buyers, even though your connection is configured.

To start the process, contact [AWS Marketplace Support on the AWS website](https://aws.amazon.com/marketplace/help/contact-us) with the information from step 2. An AWS Marketplace representative then reaches out to you and works with you through the rest of the setup, providing the configuration settings and instructions you need for your SAP Ariba environment, and helping you test the integration.

**Note**  
Single sign-on is part of this step rather than something you configure yourself. The SAP Ariba punchout endpoint is managed on the AWS supplier account in the Ariba Network, so if you want your buyers to sign in through your own identity provider instead of the default AWS sign-in page, ask for it as part of this request and supply your sign-in address. For more information about single sign-on, see [Configuring single sign-on for procurement system integration](procurement-system-sso.md).

### Configuring your SAP Ariba environment
<a name="procurement-system-ariba-configuring-ariba"></a>

Following the instructions and configuration settings from the AWS Marketplace team, you create the integration in your SAP Ariba environment.

You can build and check the configuration in your own SAP Ariba test realm before you use it for real purchases.

Once the catalog is published, confirm that the whole path works before your buyers use it. For more information about testing, see [Testing your procurement system integration](procurement-system-testing.md).

## Step 4. Set up electronic invoice delivery
<a name="procurement-system-ariba-step4"></a>

The punchout carries purchases to SAP Ariba. Invoices travel the other way, and they're configured separately, in the same way for every procurement system. Most organizations want both, so that a purchase that began as a requisition in SAP Ariba ends as an invoice there too.

For more information about electronic invoice delivery, see [Setting up electronic invoice delivery](procurement-system-invoicing.md).

**Note**  
You can ask for electronic invoice delivery as part of your catalog publishing request in step 3, rather than arranging it separately afterwards.

## SAP Ariba documentation
<a name="procurement-system-ariba-resources"></a>

For SAP's own instructions on the SAP Ariba side of the setup, see [Introduction to SAP Ariba PunchOut](https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634) on the SAP Community website.
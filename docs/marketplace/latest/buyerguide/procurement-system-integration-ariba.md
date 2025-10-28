# Configuring AWS Marketplace to integrate with SAP Ariba

The following topics explain how to configure AWS Marketplace to work with the SAP Ariba procurement system. Configuratiuon enables users to search for and purchase AWS Marketplace software
without having to leave SAP Ariba.

## Setting up IAM permissions

The configuration process starts in AWS Marketplace WS Marketplace and finishes in the SAP Ariba.
You use the information generated in AWS Marketplace to configure the procurement system punchout.
To complete the configuration, the accounts you use must meet the following requirements:

- The AWS account used to complete the AWS Marketplace configuration must be the management
  account and have the IAM permissions defined in the
  `AWS managed policy: AWSMarketplaceProcurementSystemAdminFullAccess` managed policy.

We recommend that you use IAM managed permissions rather than manually configuring permissions.
This approach is less prone to human error, and if the permissions change, the managed policy is updated.
For more information about configuring and using IAM in AWS Marketplace, see [Security on AWS Marketplace](buyer-security.md "buyer-security.md") later in this guide.

- The procurement system account used to complete the configuration must have
  administration access to set up a contract, supplier, and punchout catalog in the
  procurement system.

## Step 2. Configure AWS Marketplace to integrate with SAP Ariba

To configure AWS Marketplace to integrate with Ariba, you must work with the AWS Marketplace operations team
to create a Level 1 punchout. For more information about SAP Ariba punchout, see [Introduction to
SAP Ariba PunchOut](https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634 "https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634") on the _SAP Community_ website.

Gather the following information in preparation for configuring the setup:

- Your AWS account ID. If your AWS account is part of an AWS organization, then
  you also need the management account ID.
- The Ariba network ID (ANID) for your SAP Ariba system.

###### To configure AWS Marketplace for integrating with Ariba

1. From [AWS Marketplace Manage Procurement Systems](https://aws.amazon.com/marketplace/eprocurement/overview "https://aws.amazon.com/marketplace/eprocurement/overview"), under **Procurement
   systems**, choose **Set up Ariba integration**.
2. On the **Manage SAP Ariba integration** page, under
   **Account information**, enter the name and description of your
   integration, as well as the **SAP Ariba Network ID** (ANID) for your
   Ariba system.

###### Note

You might want your invoices in the AWS Billing console to reference the cXML
purchase order used to subscribe to your SaaS contract product. If so, you can enable
the AWS Billing integration using a service-linked role in AWS Marketplace settings. 3. Make sure that **Test mode** is enabled, then select
**Save** to save your AWS Marketplace integration settings. 4. [Contact us](https://aws.amazon.com/marketplace/help/contact-us "https://aws.amazon.com/marketplace/help/contact-us") to
start the process of creating your SAP Ariba integration. Include the above information.
AWS Marketplace sends you instructions for setting up and testing your Ariba integration.

###### Note

You need to have administrator access to your SAP Ariba system to create the
_Supplier Relationship_ with AWS Marketplace.

Following the instructions and configuration settings from the AWS Marketplace team, you create the
integration in your SAP Ariba test environment, with AWS Marketplace running in _test
mode_. In the test environment, subscription requests go to the Ariba backend so
you can see the full flow including approvals, without creating a subscription in AWS Marketplace, and
no invoice is generated. This approach enables testing the configuration prior to enabling the
punchout in production. After your testing is complete and you are ready to move to
production, [contact us](https://aws.amazon.com/marketplace/help/contact-us "https://aws.amazon.com/marketplace/help/contact-us")
to set up the account in the production environment.

###### Note

Don't forget to move to production when you're finished with testing your integration.
Otherwise, users in your system will believe that they're creating requests, but no software
will be purchased.

When your testing is complete, and you have worked with the AWS Marketplace team to turn off test
mode, your integration is complete.

For more information about configuring SAP Ariba, see [Introduction to SAP Ariba PunchOut](https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634 "https://community.sap.com/t5/spend-management-blogs-by-sap/introduction-to-sap-ariba-punchout/ba-p/13457634") on the _SAP Community_.

###### Note

For information about UNSPSC codes, see [UNSPSC codes used by
AWS Marketplace](procurement-system-integration.md#procurement-integration-setup-unspsc-codes "procurement-system-integration.md#procurement-integration-setup-unspsc-codes") .

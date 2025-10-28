# Linking AWS Partner Central and AWS accounts

AWS recently updated the
[AWS Partner Central Network (APN) fee policy](https://partnercentral.awspartner.com/partnercentral2/s/newsletter?url=APN-Fee-Requirement-Changes-for-2025 "https://partnercentral.awspartner.com/partnercentral2/s/newsletter?url=APN-Fee-Requirement-Changes-for-2025").
The change requires partners to link an AWS account to their AWS Partner Central account in order to confirm their AWS Partner Network (APN) membership.
The linked AWS account becomes the primary account for managing Partner Central engagements and activities, including APN fee billing, solutions management, and APN Customer Engagement (ACE)
opportunity tracking using the Partner Central APIs.

###### Important

This change is part of a larger migration to using AWS Identity and Access Management (IAM) to control user access to Partner Central.
You must link to an AWS account that has the IAM roles and permissions needed to access Partner Central.

Account linking has other benefits:

- You can use **Partner Connections** to work on coselling deals with other partners. This can progress deals faster and expand your reach.
  For more information, see [Partner connections](../sales-guide/partner-connections.md "../sales-guide/partner-connections.md")
  in the _AWS Partner Central Sales Guide_.
- You can use the [AWS Partner Central API](../APIReference/aws-partner-central-api-reference-guide.md "../APIReference/aws-partner-central-api-reference-guide.md")
  to integrate Partner Central with your CRM system. Integration synchronizes engagements, opportunities, solutions, and real-time event notifications.
  For more information, refer to [AWS Partner CRM integration](../crm/aws-partner-crm-integration.md "../crm/aws-partner-crm-integration.md")
  in the _AWS Partner CRM Integration Guide_.
- If you're an ACE eligible partner who links to an AWS Marketplace seller account, AWS Demand Generation Representatives pre-qualify leads from AWS Marketplace
  and transfer validated AWS originated opportunities to you.
  The following topics explain how to link accounts.

###### Topics

- [Prerequisites](linking-prerequisites.md "linking-prerequisites.md")
- [Linking AWS Partner Central and AWS
  accounts](linking-apc-aws-marketplace.md "linking-apc-aws-marketplace.md")
- [Unlinking AWS Partner Central and AWS
  accounts](unlinking-apc-aws-marketplace.md "unlinking-apc-aws-marketplace.md")
- [Account linking FAQ](account-linking-faq.md "account-linking-faq.md")

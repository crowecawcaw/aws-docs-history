The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Using the AWS Partner Central Selling API

This AWS Partner Central API reference is
designed to help [AWS
Partners](https://aws.amazon.com/partners/programs/ "https://aws.amazon.com/partners/programs/") integrate customer relationship management (CRM)
systems with Partner Central. The API automates interactions with
Partner Central, which helps to ensure effective engagements in joint
business activities.

The API provides standard AWS API functionality. Access it by
either using API [Actions](../selling-api/API_Operations.md "../selling-api/API_Operations.md") or by using an AWS SDK that's tailored to your
programming language or platform. For more information, see [Getting Started with
AWS](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started") and [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## Features offered by AWS Partner Central API

1. **Opportunity management:** Facilitates the management of
   coselling opportunities with AWS using API actions such as
   `CreateOpportunity`, `UpdateOpportunity`,
   `ListOpportunities`, `GetOpportunity`, and
   `AssignOpportunity`.
2. **AWS referral management:** Facilitates receiving
   referrals shared by AWS using actions like `ListEngagementInvitations`,
   `GetEngagementInvitation`, `StartEngagementByAcceptingInvitation`,
   and `RejectEngagementInvitation`.
3. **Entity association:** Associate related entities such
   as _AWS Products_, _Partner Solutions_,
   _AWS Marketplace Solutions_, _AWS Marketplace Products_, and
   _AWS Marketplace Private Offers_ with opportunities using the actions
   `AssociateOpportunity` and `DisassociateOpportunity`.
4. **View AWS opportunity details:** Use the
   `GetAWSOpportunitySummary` action to retrieve real-time summaries of AWS
   opportunities that are linked to your opportunities.
5. **List solutions:** Provides list APIs for listing
   solutions partners offer using `ListSolutions`.
6. **Event subscription:** Partners can subscribe to
   real-time updates on opportunities by listening to events such as _Opportunity
   Created_, _Opportunity Updated_, _Engagement
   Invitation Accepted_, _Engagement Invitation Rejected_ and
   _Engagement Invitation Created_ using Amazon EventBridge.

## Supported Regions and endpoints

The AWS Partner Central API is available in the US East (N. Virginia) Region.

| Region    | Endpoint                                 |
| --------- | ---------------------------------------- |
| us-east-1 | partnercentral-selling.us-east-1.api.aws |

Partners can test and validate API integrations in a secure sandbox environment. This
allows you to test API actions without affecting live data. For more information, see [Testing in a sandbox for the AWS Partner Central Selling API](testing-sandbox.md "testing-sandbox.md").

## Selling API entities

AWS Partner Central entities represent key business components used in coselling engagements
between partners and AWS. These entities encapsulate information related to opportunities,
solutions, products, and offers, enabling smooth collaboration and management of joint sales
activities. The following sections provide descriptions of the core entities in the Partner
Central Selling API.

### Opportunity

An opportunity is a potential sale or deal that a business identifies and actively
pursues. It's a qualified prospect or lead with a specific need that the company's products
or services can address. Opportunities are typically tracked in a sales pipeline or CRM
system and form the foundation of future revenue. Effective opportunity management involves
nurturing leads through the sales process, from the initial qualification to closing. For
more information, see [Working with your
opportunities](working-with-your-opportunities.md "working-with-your-opportunities.md") and [Data types](../APIReference/API_Types.md "../APIReference/API_Types.md")

### Partner Solutions

Represents a Partner Solution (referred to as offering on AWS Partner Central), which is a
software product or consulting practice created and delivered by AWS Partners. Partner
Solutions help customers address specific business challenges or achieve particular goals
using AWS services. For more information, see [What is a
solution?](../builder-guide/what-is-a-solution.md "../builder-guide/what-is-a-solution.md")

### AWS product

Represents a specific AWS service or product. AWS offers a wide range of products
and services designed to provide scalable, reliable, and cost-effective infrastructure
solutions. Partners can obtain the latest list of AWS Products from the [bulk import page on
Partner Central](https://partnercentral.awspartner.com/OpportunityBulkImportPage "https://partnercentral.awspartner.com/OpportunityBulkImportPage") (Start Import > AWS Products and Solutions). For more
information, you can [learn about AWS Products](https://aws.amazon.com/products "https://aws.amazon.com/products") or [view the list of all AWS Products](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json").

### AWS Marketplace private offer

AWS Marketplace private offer is a feature that allows AWS Marketplace sellers to offer specific pricing and
terms to individual AWS customers. Through private offers, sellers can negotiate custom
prices, payment schedules, and end user license terms. AWS customers can obtain software
solutions that meet their specific requirements, while also possibly benefiting from more
favorable terms or pricing compared to standard offerings. The private offer process
involves the seller creating a unique offer with tailored terms, which is then shared
privately with the designated AWS customer for their review and acceptance. For more
information, see [Private offers in
AWS Marketplace](../../../marketplace/latest/buyerguide/buyer-private-offers.md "../../../marketplace/latest/buyerguide/buyer-private-offers.md").

### Engagement invitation

Engagement Invitation refers to a formal request from AWS for partners to collaborate
on a specific referral. This allows AWS and the partner to work together to drive the
opportunity forward. The invitation can be accepted or rejected by the partner.

###### Topics

- [Working with your opportunities](working-with-your-opportunities.md "working-with-your-opportunities.md")
- [Working with opportunities from AWS](working-with-opportunities-from-aws.md "working-with-opportunities-from-aws.md")
- [Working with opportunity updates](working-with-opportunity-updates.md "working-with-opportunity-updates.md")
- [Working with multipartner opportunities](working-with-multi-partner-opportunities.md "working-with-multi-partner-opportunities.md")
- [Associating, disassociating and assigning opportunities](associating-disassociating-assigning-opportunities.md "associating-disassociating-assigning-opportunities.md")
- [Working with your leads](working-with-your-leads.md "working-with-your-leads.md")
- [Working with deal sizing insights](working-with-deal-sizing-insights.md "working-with-deal-sizing-insights.md")
- [Best practices](best-practices.md "best-practices.md")

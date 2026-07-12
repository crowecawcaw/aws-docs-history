The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Using the AWS Partner Central Benefits API

The AWS Partner Central Benefits API streamlines how partners discover, apply for, and manage benefits across all AWS Partner Programs. By centralizing benefit management into a single, intuitive interface, the service creates a transparent meritocracy that rewards partners while simplifying operations.

The API provides standard AWS API functionality. Access it by
either using API [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") or by using an AWS SDK that's tailored to your
programming language or platform. For more information, see [Getting Started with
AWS](https://aws.amazon.com/getting-started "https://aws.amazon.com/getting-started") and [Tools to Build on AWS](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/").

## What is a Benefit?

In the AWS Partner Network (APN), a Benefit represents an advantage or capability that a partner may obtain from AWS to support their business growth and customer success. Benefits are designed to reward partners based on their qualifications and contributions while providing tangible value that helps partners scale their AWS practices.

Benefits can take many forms, including:

- **Financial incentives** - Credits, cash disbursements, and funding programs like Migration Acceleration Program (MAP) or Marketing Development Funds (MDF)
- **Access benefits** - Preview access to new services, tools, or specialized resources
- **Recognition** - Digital badges, certifications, competency designations, and partner tier status
- **Technical resources** - Solution architecture assistance, technical support, and ProServe engagements
- **Marketing support** - Co-marketing opportunities, featured partner status, and success story publications

## Discovering Available Benefits

Partners begin their benefit journey by discovering what benefits are available to them and understanding eligibility requirements. The Benefits API provides comprehensive discovery capabilities through the Benefit Discovery APIs.

### Listing Available Benefits

Partners can view all available benefits using the `ListBenefits` API action. This action retrieves a catalog of benefits with optional filtering capabilities to help partners find relevant opportunities quickly.

To efficiently discover benefits, partners can filter by:

- **Program** - Filter by specific AWS partner programs such as MAP (Migration Acceleration Program), MDF (Marketing Development Funds), ISV Workload Migration, Innovation Sandbox, Proof of Concept, or Partner Initiative Funding
- **Fulfillment Type** - Filter by how benefits are delivered: `CREDITS`, `CASH`, `DISCOUNT`, `ACCESS`, `RECOGNITION`, or `RESOURCE`
- **Status** - Filter by benefit status: `ACTIVE` or `DEPRECATED`

The `ListBenefits` API returns benefit summaries containing essential information such as benefit ID, name, description, associated programs, and fulfillment types. This summary view allows partners to quickly scan available benefits and identify those most relevant to their business objectives.

**Example filtering approach:**

Partners focused on financial incentives might filter by fulfillment types `CREDITS` and `CASH` to see funding opportunities. Partners seeking technical enablement might filter by fulfillment type `RESOURCE` or `ACCESS` to find technical support benefits and tool access.

### Viewing Detailed Benefit Information

Once a partner identifies a benefit of interest, they can retrieve complete details using the `GetBenefit` API action. This provides comprehensive information including:

- **Eligibility criteria** - Detailed requirements that partners must meet to qualify for the benefit
- **Benefit request schema** - The specific information and documentation partners need to provide when applying
- **Grant details** - What partners will receive upon approval
- **Associated programs** - Which AWS partner programs the benefit supports

The benefit request schema is particularly important as it defines the structure and required fields for benefit applications. Partners should review this schema carefully before creating a benefit application to ensure they gather all necessary information upfront.

###### Important

Eligibility determination for each benefit is handled by the client or UI layer. For funding-related benefits, eligibility is typically based on the partner's scorecard performance and program participation.

###### Topics

- [Working with Benefit Applications](working-with-benefit-applications.md "working-with-benefit-applications.md")
- [Working with Benefit Allocations](working-with-benefit-allocations.md "working-with-benefit-allocations.md")

###### Topics

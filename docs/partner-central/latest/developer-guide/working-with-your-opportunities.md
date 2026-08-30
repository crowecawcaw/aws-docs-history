The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with opportunities in the AWS Partner Central API

## What is an Opportunity?

During the initial stages of the sales process, a sales representative assesses
whether an interested individual (called _lead_)
has the potential to become a customer. This assessment and validation phase is
referred to as _Qualification_. Once a lead is
deemed qualified and is considered to have a higher probability of converting to a
customer, it is then classified as an _Opportunity_.

## Working with Your Opportunities

Partners can manage opportunities created within their CRM systems and
synchronize them with AWS Partner Central using the AWS Partner Central Selling API. This allows
partners to track and manage opportunities from initiation to closure.

### Creating an Opportunity

The first step in managing opportunities is creating an opportunity using the
`CreateOpportunity` action. This creates an opportunity with the
`Lifecycle.ReviewStatus` set to `Pending Submission`.
However, the opportunity is not yet submitted to AWS for validation.

After the opportunity is created, you must associate at least one Partner
Solution, AWS Marketplace Solution, or AWS Marketplace Product with the
opportunity using the `AssociateOpportunity` action. This action
clearly defines what the opportunity is attempting to sell. You can view
the complete list of available solutions in your account using the
`ListSolutions` API, and you can associate between one and ten
solutions.

Optionally, you can also associate relevant AWS Products with the
opportunity using the `AssociateOpportunity` action. This step helps
AWS sales teams understand what AWS products are expected to be sold in
conjunction with the opportunity.

After the required solution or product is associated and, optionally, AWS
Products are linked, you can start engagement on the opportunity by using
the `StartEngagementFromOpportunityTask` action. This is when
you submit the opportunity to start an engagement.

### Review Process

After starting the engagement on the opportunity using the
`StartEngagementFromOpportunityTask` action, the opportunity
enters the AWS validation phase, and its `Lifecycle.ReviewStatus`
is set to `Submitted`. No changes can be made to the opportunity
until the review process is complete.

During this validation phase, AWS ensures that the opportunity details are
accurate and complete. While the validation is in progress, the
`Lifecycle.ReviewStatus` is set to `In-Review`.

If there are changes or additional details required from the partner, AWS
sets the `Lifecycle.ReviewStatus` to `Action Required`,
and any required updates are communicated via the
`Lifecycle.ReviewComments` field.

Once the opportunity passes validation, the
`Lifecycle.ReviewStatus` changes to `Approved`, making
the opportunity ready for co-selling activities.

Partners should monitor the `Opportunity Updated` event using
Amazon EventBridge. This will notify them of any status changes or feedback from AWS.
Upon receiving the event, partners can use the `GetOpportunity` API
action to fetch the latest opportunity details and verify the
`Lifecycle.ReviewStatus` field.

### Resolving Validation Issues

If the `Lifecycle.ReviewStatus` is set to `Action
 Required`, partners need to address the issues highlighted by AWS.
To resolve these, partners can update the opportunity using the
`UpdateOpportunity` API action.

During the `Action Required` state, only certain fields are
editable. These fields include:

1. `Customer.Account.Address.City`
2. `Customer.Account.Address.Country`
3. `Customer.Account.Address.PostalCode`
4. `Customer.Account.Address.StateOrRegion`
5. `Customer.Account.Address.StreetAddress`
6. `Customer.Account.WebsiteUrl`
7. `LifeCycle.TargetCloseDate`
8. `Project.ExpectedCustomerSpend.Amount`
9. `Project.ExpectedCustomerSpend.Currency`
10. `Project.CustomerBusinessProblem`
11. `PartnerOpportunityIdentifier`

After making the necessary changes, the opportunity re-enters the validation
phase, and the process repeats until the opportunity's
`Lifecycle.ReviewStatus` is set to `Approved` or
`Disqualified`.

### Post-Approval Updates

Once the opportunity is `Approved`, partners can continue to
update the opportunity as needed using the `UpdateOpportunity`
action, facilitating seamless co-selling activities.

Partners should continue monitoring the `Opportunity Updated`
events through Amazon EventBridge to remain updated on any changes. For more information
on tracking AWS updates, refer to the "Working with opportunity updates"
section. Partners can also update select fields based on the business validation
rules.

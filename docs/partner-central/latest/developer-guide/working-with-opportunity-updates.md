The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with opportunity updates

## Updating opportunities

Partners can use the `UpdateOpportunity` action to update opportunities,
with specific rules governing which fields are updated, and when they're updated:

1. Updates cannot be made if the `Lifecycle.ReviewStatus` is
   `Submitted` or `In-Review`.
2. Before submission, partners can make updates, but AWS will not process them
   unless the `StartEngagementFromOpportunityTask` action is
   invoked.
3. When the opportunity is in `Submitted` or `In-review`
   status, all updates are blocked.
4. If the opportunity is in `Action Required` status, AWS opens
   select fields for updates. These fields include:

   - `Customer.Account.Address.City`
   - `Customer.Account.Address.Country`
   - `Customer.Account.Address.PostalCode`
   - `Customer.Account.Address.StateOrRegion`
   - `Customer.Account.Address.StreetAddress`
   - `Customer.Account.WebsiteUrl`
   - `LifeCycle.TargetCloseDate`
   - `Project.ExpectedCustomerSpend.Amount`
   - `Project.ExpectedCustomerSpend.CurrencyCode`
   - `Project.ExpectedCustomerSpend.EstimationURL`
   - `Project.ExpectedCustomerSpend.Frequency`
   - `Project.ExpectedCustomerSpend.TargetCompany`
   - `Project.CustomerBusinessProblem`
   - `PartnerOpportunityIdentifier`

5. After the review process (i.e., when `Lifecycle.ReviewStatus` is
   set to `Approved`), the following fields cannot be updated:

   - `Customer.Account.Address.Country`
   - `Customer.Account.Address.PostalCode`
   - `Customer.Account.Industry`
   - `Customer.Account.WebsiteUrl`
   - `Project.CustomerBusinessProblem`
   - `PartnerOpportunityIdentifier`
   - `Project.Title`

6. For all other fields, updates can be made using the
   `UpdateOpportunity` action. However, additional restrictions may
   apply based on business rules for the specific program or opportunity type. For
   more details, refer to field-level validations.
7. For all updates made through both the UI and API, the _Opportunity
   Updated_ event is generated.

## Receiving updates from AWS on opportunities

AWS typically updates AWS opportunities, and each time an update is made, an
_Opportunity Updated_ event is generated.

###### To retrieve the latest updates from AWS, partners need to invoke two separate actions

1. `GetOpportunity` to retrieve details of the partner's
   opportunity.
2. `GetAWSOpportunitySummary` to retrieve real-time summaries of
   the AWS opportunity data.

Most regular updates from AWS will be available through the
`GetAWSOpportunitySummary` response. However, AWS may occasionally
update attributes in the partner's opportunity directly.

###### To consume updates from AWS

1. Invoke the `GetAWSOpportunitySummary` action to retrieve the latest
   details of the AWS Opportunity.
2. If changes need to be reflected in the partner's opportunity, use the
   `UpdateOpportunity` action to copy the relevant data onto the
   partner's opportunity.

Partners can choose to automate this process as a direct update mechanism or
implement a manual review process to validate and update the data.

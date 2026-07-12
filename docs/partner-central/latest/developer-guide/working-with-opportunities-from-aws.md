The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Working with opportunities from AWS

## 1. Receiving the AWS Opportunity

Opportunities are shared with partners when an AWS sales executive attaches a
partner to an opportunity in AWS's CRM system. These are referred to as AWS
Opportunities, distinct from opportunities created in the partner's own account.

When an AWS Opportunity has a partner attached, AWS creates an Engagement
Invitation containing a subset of data from the AWS Opportunity. Partners will receive
an _Engagement Invitation Created_ event.

## 2. Reviewing the Engagement Invitation

The Engagement Invitation contains essential information such as
`Project.Title`, `Project.CustomerUseCase`,
`Lifecycle.Stage`, `Project.CustomerBusinessProblem`, and a
few additional fields. Partners can use this data to decide whether to pursue the
opportunity.

However, the following fields from the AWS Opportunity are not included in the
Engagement Invitation:

```
Customer.Account.Address.StreetAddress
Customer.Account.Address.City
Customer.Account.Address.PostalCode
Customer.Contact
Customer.Account.AWSAccountId
Project.OtherSolutionDescription
RelatedEntityIdentifiers
```

## 3. Handling the Engagement Invitation

Upon receiving an _Engagement Invitation Created_ event, partners
can use the `GetEngagementInvitation` action to retrieve details of the AWS
Opportunity.

If the partner decides not to pursue the opportunity, they can reject the invitation
using the `RejectEngagementInvitation` action, along with the required
`RejectionReason`. Once rejected, access to the opportunity is lost.

To accept the invitation and proceed, partners should use the
`StartEngagementByAcceptingInvitationTask` action. This is an
asynchronous action that sequentially performs the following tasks:

1. Accepts the Engagement Invitation.
2. Creates a new opportunity in the partner's account using data from the AWS
   Opportunity.
3. Includes additional details required to identify the customer in the partner's
   account.

Upon completion, an _Opportunity Created_ event is triggered with
the corresponding Opportunity ID. Partners can then use this ID in the
`GetOpportunity` action to retrieve full details of the opportunity.

If the partner is not using events, they can call
`StartEngagementByAcceptingInvitationTask` again with the same payload to
check the latest status.

## 4. Managing the AWS Opportunity Post-Acceptance

Once the opportunity is in the partner's account, it can be managed and updated like
any other opportunity in the system. Partners can use actions like
`UpdateOpportunity` to make any necessary changes.

For more details on how to track AWS updates and manage opportunity updates, refer
to the [Working with opportunity updates](working-with-opportunity-updates.md "working-with-opportunity-updates.md") section.

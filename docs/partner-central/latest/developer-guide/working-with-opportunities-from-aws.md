

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Working with opportunities from AWS
<a name="working-with-opportunities-from-aws"></a>

## 1. Receiving the AWS Opportunity
<a name="receiving-aws-opportunity"></a>

 Opportunities are shared with partners when an AWS sales executive attaches a partner to an opportunity in AWS's CRM system. These are referred to as AWS Opportunities, distinct from opportunities created in the partner's own account. 

 When an AWS Opportunity has a partner attached, AWS creates an Engagement Invitation containing a subset of data from the AWS Opportunity. Partners will receive an *Engagement Invitation Created* event. 

## 2. Reviewing the Engagement Invitation
<a name="reviewing-the-engagement-invitation"></a>

 The Engagement Invitation contains essential information such as `Project.Title`, `Project.CustomerUseCase`, `Lifecycle.Stage`, `Project.CustomerBusinessProblem`, and a few additional fields. Partners can use this data to decide whether to pursue the opportunity. 

 However, the following fields from the AWS Opportunity are not included in the Engagement Invitation:

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
<a name="engagement-invitation-actions"></a>

 Upon receiving an *Engagement Invitation Created* event, partners can use the `GetEngagementInvitation` action to retrieve details of the AWS Opportunity. 

 If the partner decides not to pursue the opportunity, they can reject the invitation using the `RejectEngagementInvitation` action, along with the required `RejectionReason`. Once rejected, access to the opportunity is lost. 

 To accept the invitation and proceed, partners should use the `StartEngagementByAcceptingInvitationTask` action. This is an asynchronous action that sequentially performs the following tasks: 

1. Accepts the Engagement Invitation.

1. Creates a new opportunity in the partner's account using data from the AWS Opportunity.

1. Includes additional details required to identify the customer in the partner's account.

 Upon completion, an *Opportunity Created* event is triggered with the corresponding Opportunity ID. Partners can then use this ID in the `GetOpportunity` action to retrieve full details of the opportunity. 

 If the partner is not using events, they can call `StartEngagementByAcceptingInvitationTask` again with the same payload to check the latest status. 

## 4. Managing the AWS Opportunity Post-Acceptance
<a name="managing-aws-opportunity-post-acceptance"></a>

 Once the opportunity is in the partner's account, it can be managed and updated like any other opportunity in the system. Partners can use actions like `UpdateOpportunity` to make any necessary changes. 

 For more details on how to track AWS updates and manage opportunity updates, refer to the [Working with opportunity updates](working-with-opportunity-updates.md) section.
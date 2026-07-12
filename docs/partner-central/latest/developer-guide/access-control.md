The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

# Access for the Selling API

Access control and permissions are managed by AWS Identity and Access Management (IAM). This section provides
guidance for configuring the necessary permissions to interact with the API, including the
permissions required to list AWS Marketplace entities.

## Prerequisites

Before configuring permissions, ensure that your AWS account is linked to Partner Central and
that you created the necessary IAM roles and users. For more information, see [Setup and
Authentication](../APIReference/setup-authentication.md "../APIReference/setup-authentication.md").

## Using AWS managed policies

AWS provides managed policies that grant the required
permissions to interact with the API. To provide the necessary access to
manage opportunities, attach the
`AWSPartnerCentralOpportunityManagement` policy to your IAM
identities. For more information, see [AWS managed policies for AWS Partner Central users](../getting-started/managed-policies.md "../getting-started/managed-policies.md").

### AWSPartnerCentralOpportunityManagement policy

This policy grants full access to Partner Central opportunity management actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OpportunityManagement",
 "Effect": "Allow",
 "Action": [
 "partnercentral:AcceptEngagementInvitation",
 "partnercentral:AssignOpportunity",
 "partnercentral:AssociateOpportunity",
 "partnercentral:CreateEngagement",
 "partnercentral:CreateEngagementInvitation",
 "partnercentral:CreateOpportunity",
 "partnercentral:CreateResourceSnapshot",
 "partnercentral:CreateResourceSnapshotJob",
 "partnercentral:DeleteResourceSnapshotJob",
 "partnercentral:DisassociateOpportunity",
 "partnercentral:GetAwsOpportunitySummary",
 "partnercentral:GetEngagement",
 "partnercentral:GetEngagementInvitation",
 "partnercentral:GetOpportunity",
 "partnercentral:GetResourceSnapshot",
 "partnercentral:GetResourceSnapshotJob",
 "partnercentral:ListEngagementByAcceptingInvitationTasks",
 "partnercentral:ListEngagementFromOpportunityTasks",
 "partnercentral:ListEngagementInvitations",
 "partnercentral:ListEngagementMembers",
 "partnercentral:ListEngagementResourceAssociations",
 "partnercentral:ListEngagements",
 "partnercentral:ListOpportunities",
 "partnercentral:ListResourceSnapshotJobs",
 "partnercentral:ListResourceSnapshots",
 "partnercentral:ListSolutions",
 "partnercentral:RejectEngagementInvitation",
 "partnercentral:StartEngagementByAcceptingInvitationTask",
 "partnercentral:StartEngagementFromOpportunityTask",
 "partnercentral:StartResourceSnapshotJob",
 "partnercentral:StopResourceSnapshotJob",
 "partnercentral:SubmitOpportunity",
 "partnercentral:UpdateOpportunity"
 ],
 "Resource": "*"
 },
 {
 "Sid": "ListingAWSMarketplaceEntities",
 "Effect": "Allow",
 "Action": ["aws-marketplace:ListEntities"],
 "Resource": "*"
 },
 {
 "Sid": "AWSMarketplaceOffersAccess",
 "Effect": "Allow",
 "Action": ["aws-marketplace:DescribeEntity"],
 "Resource": [
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/Offer/*",
 "arn:aws:aws-marketplace:*:*:AWSMarketplace/OfferSet/*"
 ]
 }
 ]
}`

```

## Custom policies

If the managed policies don't meet your needs, create custom IAM policies that grant
the permissions required for your use case. The following example is a custom policy
that grants permissions to list AWS Marketplace entities:

###### Example of custom policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "partnercentral:ListOpportunities",
 "aws-marketplace:ListEntities"
 ],
 "Resource": "*"
 }
 ]
}`

```

**Custom permissive policy**

This policy provides broad access to Partner Central selling actions, including features that
may be added in the future without requiring policy updates. By using the wild card
action `partnercentral:*`, this policy automatically grants access to new
Partner Central selling features as they become available, reducing the need for manual updates.
This policy also includes permissions for interacting with AWS Marketplace entities, which helps
to ensure access is maintained for both selling and Marketplace actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":
 [
 {
 "Effect": "Allow",
 "Action":
 [
 "partnercentral:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "aws-marketplace:ListEntities",
 "aws-marketplace:DescribeEntity"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action":
 [
 "aws-marketplace:SearchAgreements",
 "aws-marketplace:DescribeAgreement"
 ],
 "Resource": "*",
 "Condition":
 {
 "StringEquals":
 {
 "aws-marketplace:PartyType": "Proposer"
 }
 }
 }
 ]
}`

```

## Assigning policies to IAM roles and users

Follow these steps to assign policies to IAM roles and users:

1. Sign in to the AWS Management Console.
2. Navigate to the IAM service.
3. Select roles or users, and choose the IAM role or user to which you want to
   attach a policy.
4. Attach the
   `AWSPartnerCentralOpportunityManagement` policy or your
   custom policy to the selected IAM role or user.

For more information, see [Adding and
removing IAM identity permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md").

## Managing permissions using condition keys

Condition keys in IAM policies provide resource-level permissions for when to
enforce statement policies. You can use condition keys to specify conditions that
dictate when certain permissions are allowed or denied.

For more information, see [IAM JSON policy elements: Condition operators](../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition_operators.md").

Condition keys overview| Condition key | Description | Applicable actions | Valid values |
| --- | --- | --- | --- |
| partnercentral:Catalog | filters access by the type of the associated catalog entity | all actions | AWS, sandbox |
| aws-marketplace:PartyType | filters access based on the type of party (e.g., proposer) | SearchAgreements, DescribeAgreement | proposer |

## Summary of required permissions

Summary of required permissions| Action | Description |
| --- | --- |
| partnercentral:CreateOpportunity | allows creating opportunities |
| partnercentral:UpdateOpportunity | allows updating opportunities |
| partnercentral:ListOpportunities | allows listing opportunities |
| partnercentral:GetOpportunity | allows retrieving opportunity details |
| partnercentral:ListSolutions | allows listing solutions |
| partnercentral:AssociateOpportunity | allows associating opportunities with other entities |
| partnercentral:DisassociateOpportunity | allows disassociating opportunities from other entities |
| partnercentral:AcceptEngagementInvitation | allows accepting engagement invitations |
| partnercentral:RejectEngagementInvitation | allows rejecting engagement invitations |
| partnercentral:GetEngagementInvitation | allows retrieving engagement invitation details |
| partnercentral:ListEngagementInvitations | allows listing engagement invitations |
| partnercentral:SubmitOpportunity | allows submitting opportunities |
| partnercentral:GetAwsOpportunitySummary | allows retrieving AWS opportunity summary |
| partnercentral:StartProspectingFromEngagementTask | Creates a prospecting task from engagements |
| partnercentral:GetProspectingFromEngagementTask | Returns prospecting task details |
| partnercentral:ListProspectingFromEngagementTasks | Returns a list of prospecting tasks |
| aws-marketplace:ListEntities | allows listing AWS Marketplace entities |
| aws-marketplace:DescribeEntity | allows describing AWS Marketplace entities |
| aws-marketplace:SearchAgreements | allows searching agreements in AWS Marketplace |
| aws-marketplace:DescribeAgreement | allows describing agreements in AWS Marketplace |

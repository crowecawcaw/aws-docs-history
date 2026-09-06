

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Testing in a sandbox for the AWS Partner Central Selling API
<a name="testing-sandbox"></a>

## How to use the sandbox
<a name="use-sandbox"></a>

1. Create an IAM role:

   Create an IAM role in the AWS account linked with your AWS Partner Central account.

1. Assign Policy:

   Assign the following policy to the IAM role. For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Effect": "Allow",
               "Action": [
                   "partnercentral:CreateOpportunity",
                   "partnercentral:UpdateOpportunity",
                   "partnercentral:ListOpportunities",
                   "partnercentral:GetOpportunity",
                   "partnercentral:GetAwsOpportunitySummary",
                   "partnercentral:ListSolutions",
                   "partnercentral:AssociateOpportunity",
                   "partnercentral:DisassociateOpportunity",
                   "partnercentral:AssignOpportunity",
                   "partnercentral:SubmitOpportunity",
                   "partnercentral:AcceptEngagementInvitation",
                   "partnercentral:CreateEngagementInvitation",
                   "partnercentral:RejectEngagementInvitation",
                   "partnercentral:GetEngagementInvitation",
                   "partnercentral:ListEngagementInvitations",
                   "partnercentral:StartEngagementFromOpportunityTask",
                   "partnercentral:StartEngagementByAcceptingInvitationTask",
                   "partnercentral:CreateResourceSnapshotJob",
                   "partnercentral:StartResourceSnapshotJob",
                   "partnercentral:CreateEngagement"
               ],
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "partnercentral:Catalog": "Sandbox"
                   }
               }
           },
           {
               "Effect": "Allow",
               "Action": [
                   "aws-marketplace:ListEntities",
                   "aws-marketplace:DescribeEntity"
               ],
               "Resource": "*"
           },
           {
               "Effect": "Allow",
               "Action": [
                   "aws-marketplace:SearchAgreements",
                   "aws-marketplace:DescribeAgreement"
               ],
               "Resource": "*",
               "Condition": {
                   "StringEquals": {
                       "aws-marketplace:PartyType": "Proposer"
                   }
               }
           }
       ]
   }
   ```

------

1. Use IAM role credentials:

   Use the credentials (secret key and access key) of this IAM role in your solution to perform the API actions.

## Testing AWS actions
<a name="testing-aws-actions"></a>

During the testing phase, it is often necessary to simulate AWS actions. This simulation enables partners to thoroughly test the complete end-to-end flow of their integration with AWS services.

### Simulating the creation of an AWS originated opportunity
<a name="simulating"></a>

To simulate the creation of an AWS originated opportunity, in the payload of the `CreateOpportunity` action, include `"Catalog": "Sandbox"` and `"Origin": "AWS Referral"`.

For example:

```
{
    "Catalog": "Sandbox",
    "Origin": "AWS Referral",
    "OpportunityIdentifier": "O123456",
    "Title": "Test Opportunity",
    ...
}
```

### Simulating updates to a partner-originated opportunity
<a name="simulate-updates"></a>

To simulate updates or other actions on a partner-originated opportunity, use the `UpdateOpportunity` action with `"Catalog": "Sandbox"` and `Lifecycle.ReviewStatus: “Approved”` or `“Action Required”` in the payload.

 If you are taking the payload from the `GetOpportunity` action to do the update, ensure that you change the ID to `Identifier`, and remove the following fields:
+ `CreatedDate`
+ `OpportunityTeam`
+ `RelatedEntityIdentifiers`

For example:

```
{
    "Catalog": "Sandbox",
    "Identifier": "O123456",
    "Title": "Updated Test Opportunity",
    "Lifecycle": {
        "ReviewStatus": "Approved"
    }
    ...
}
```

## Testing events in the sandbox environment
<a name="testing-events"></a>

Partners can consume opportunity events from the sandbox environment to help test the event-based implementations. Set up EventBridge in the same AWS account with rules to listen for sandbox events by specifying `catalog: sandbox` in the event details. For more information, see [Notifications for the AWS Partner Central Selling API](selling-api-events.md).

Example event rule:

```
{
    "source": ["aws.partnercentral-selling"],
    "detail": {
        "catalog": ["Sandbox"] 
    }
}
```

Event rules that specify `catalog` as `Sandbox` will only match events coming from the sandbox, generated by the actions you perform in the sandbox environment.

## Additional testing notes
<a name="additional-testing-notes"></a>

1. Testing `AssociateOpportunity` action:

   1. Use the default solution `"S-1234567"` for testing the `AssociateOpportunity` action.

   1. For testing Marketplace offers, use a real offer ID from your account.

1. To move to production, change the `catalog` value from `Sandbox` to `AWS`.

## Getting help
<a name="getting-help"></a>

If you encounter challenges integrating your CRM with AWS, or if you need to test a specific scenario not covered here, please reach out to support by raising a case through the following steps:

1. Sign in to the [AWS Partner Central](https://partnercentral.awspartner.com/) with your AWS Partner Network credentials.

1. On the [Support Center for Partner Central](https://partnercentral.awspartner.com/support), choose `Open New Case` to log a new case. Complete the fields as follows:

   1. Type of support case: `AWS Partner Central`.

   1. Question regarding: `Partner Central Tools or ACE leads and opportunities`.

   1. Get specific: Select the most appropriate CRM Integration case type.

   1. Subject: Include a brief description of the request.

   1. Description: Provide a detailed description of issues, questions, errors, and troubleshooting steps.

   1. Attachments: Include logs and screenshots, where applicable.
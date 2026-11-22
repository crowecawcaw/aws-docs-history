

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Testing in a sandbox for the AWS Partner Central Account API

## How to use the sandbox
<a name="use-sandbox"></a>

To use the sandbox, complete the following steps:

1. Create an IAM role:

   Create an IAM role in the AWS account linked with your AWS Partner Central account.

1. Assign Policy:

   Assign the following policy to the IAM role. For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

   ```json
   {
     "Version": "2012-10-17",		 	 	 
     "Statement": [
       {
         "Sid": "AccountManagement",
         "Effect": "Allow",
         "Action": [
           "partnercentral:AcceptConnectionInvitation",
           "partnercentral:AssociateAwsTrainingCertificationEmailDomain",
           "partnercentral:CancelConnection",
           "partnercentral:CancelConnectionInvitation",
           "partnercentral:CancelProfileUpdateTask",
           "partnercentral:CreateConnectionInvitation",
           "partnercentral:CreatePartner",
           "partnercentral:DisassociateAwsTrainingCertificationEmailDomain",
           "partnercentral:GetAllianceLeadContact",
           "partnercentral:GetConnection",
           "partnercentral:GetConnectionInvitation",
           "partnercentral:GetConnectionPreferences",
           "partnercentral:GetPartner",
           "partnercentral:GetProfileUpdateTask",
           "partnercentral:GetProfileVisibility",
   		"partnercentral:GetVerification",
           "partnercentral:ListConnectionInvitations",
           "partnercentral:ListConnections",
           "partnercentral:ListPartners",
           "partnercentral:PutAllianceLeadContact",
           "partnercentral:PutProfileVisibility",
           "partnercentral:RejectConnectionInvitation",
           "partnercentral:SendEmailVerificationCode",
           "partnercentral:StartProfileUpdateTask",
   		"partnercentral:StartVerification",
           "partnercentral:UpdateConnectionPreferences"
         ],
         "Resource": "*",
         "Condition": {
           "StringEquals": {
             "partnercentral:Catalog": [
               "Sandbox"
             ]
           }
         }
       },
       {
         "Sid": "BusinessPlanManagement",
         "Effect": "Allow",
         "Action": [
           "partnercentral:AssociateBusinessPlan",
           "partnercentral:CancelBusinessPlan",
           "partnercentral:CancelBusinessPlanSubmissionTask",
           "partnercentral:CreateBusinessPlan",
           "partnercentral:CreateBusinessPlanItem",
           "partnercentral:DeleteBusinessPlanAttachment",
           "partnercentral:DeleteBusinessPlanItem",
           "partnercentral:DisassociateBusinessPlan",
           "partnercentral:GetBusinessPlan",
           "partnercentral:GetBusinessPlanAttachment",
           "partnercentral:GetBusinessPlanAttachmentImportTask",
           "partnercentral:GetBusinessPlanItem",
           "partnercentral:GetBusinessPlanItemSchema",
           "partnercentral:GetBusinessPlanSettings",
           "partnercentral:GetBusinessPlanSubmissionTask",
           "partnercentral:ListBusinessPlanAssociations",
           "partnercentral:ListBusinessPlanAttachmentImportTasks",
           "partnercentral:ListBusinessPlanAttachments",
           "partnercentral:ListBusinessPlanHistory",
           "partnercentral:ListBusinessPlanItems",
           "partnercentral:ListBusinessPlans",
           "partnercentral:ListBusinessPlanSubmissionTasks",
           "partnercentral:PutBusinessPlanSettings",
           "partnercentral:StartBusinessPlanAttachmentImportTask",
           "partnercentral:StartBusinessPlanSubmissionTask",
           "partnercentral:UpdateBusinessPlan",
           "partnercentral:UpdateBusinessPlanItem"
         ],
         "Resource": "*",
         "Condition": {
           "StringEquals": {
             "partnercentral:Catalog": [
               "Sandbox"
             ]
           }
         }
       },
       {
         "Sid": "TaggingAccess",
         "Effect": "Allow",
         "Action": [
           "partnercentral:TagResource",
           "partnercentral:UntagResource",
           "partnercentral:ListTagsForResource"
         ],
         "Resource": [
           "arn:aws:partnercentral:*:*:catalog/Sandbox/partner/*",
           "arn:aws:partnercentral:*:*:catalog/Sandbox/business-plan/*"
         ],
         "Condition": {
           "StringEquals": {
             "partnercentral:Catalog": [
               "Sandbox"
             ]
           }
         }
       }
     ]
   }
   ```

1. Use IAM role credentials:

   Use the credentials (secret key and access key) of this IAM role in your solution to perform the API actions.

## Testing AWS actions
<a name="testing-aws-actions"></a>

During the testing phase, it is often necessary to simulate AWS actions. This simulation enables partners to thoroughly test the complete end-to-end flow of their integration with AWS services. Each request includes a catalog parameter, which determines the data environment.

### Simulating the creation of a Partner
<a name="simulating-partner"></a>

To simulate the creation of a Partner, in the payload of the `CreatePartner` action, include `"catalog": "Sandbox"` in the payload.

For example:

```json
{
  "ClientToken": "client-generated-uuid",
  "Catalog": "Sandbox",
  "LegalName": "Your Name",
  "PrimarySolutionType": "SOLUTION_TYPE",
  "AllianceLeadContact": {
    "FirstName": "Example First Name",
    "LastName": "Example Last Name",
    "BusinessTitle": "Example Title",
    "Email": "example@domain.com"
  },
  "EmailVerificationCode": "123456"
}
```

Note: In Sandbox email verification is disabled. You can use any six-digit EmailVerificationCode for testing. Also, don't use "Tags" in the request.

## Additional testing notes
<a name="additional-testing-notes"></a>

Note the following when testing in the sandbox:

1. To test other actions, set `"catalog": "Sandbox"` in the payload.

1. To test partner account connections in sandbox, you must execute `StartProfileUpdateTask` action after creating partner in sandbox catalog.

1. To move to production, change the catalog value from `Sandbox` to `AWS`.

## Testing events in the sandbox environment
<a name="testing-events"></a>

Partners can consume events from the sandbox environment to help test the event-based implementations. Set up EventBridge in the same AWS account with rules to listen for sandbox events by specifying `catalog: Sandbox` in the event details. For more information, see [Notifications for the AWS Partner Central Account API](account-api-events.md).

Example event rule:

```json
{
  "source": ["aws.partnercentral-account"],
  "detail": {
    "catalog": ["Sandbox"]
  }
}
```

Event rules that specify `catalog` as `Sandbox` will only match events coming from the sandbox, generated by the actions you perform in the sandbox environment.

## Testing business plans in the sandbox
<a name="testing-business-plans"></a>

Every business plan operation accepts `"catalog": "Sandbox"`. Plans that you create in the Sandbox catalog are separate from your plans in the AWS catalog, and the same validation, statuses, and limits apply. To call business plan operations in the Sandbox catalog, your account must first be registered as a partner in that catalog. For more information, see [Simulating the creation of a Partner](#simulating-partner).

Note the following differences in the Sandbox catalog:
+ Sandbox plans can't reach `ACTIVE` status, because AWS doesn't review them. After you call `StartBusinessPlanSubmissionTask`, the plan stays in `IN_REVIEW` status. To return it to `DRAFT`, call `CancelBusinessPlanSubmissionTask`.
+ Sandbox plans don't generate emails from AWS Partner Central.
+ Sandbox plans don't need the service-linked role or AWS engagement, because AWS doesn't make changes to them.
+ Sandbox plans don't generate the `Business Plan Activated` or `Business Plan Submission Task Succeeded` events, because no review happens. To test event handling, cancel a Sandbox plan and handle the `Business Plan Canceled` event.

Association targets must be opportunity or campaign ARNs in the Sandbox catalog, in your own account. AWS Partner Central doesn't check that the target exists.
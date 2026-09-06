

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Testing in a sandbox for the AWS Partner Central Account API
<a name="testing-sandbox-account"></a>

## How to use the sandbox
<a name="use-sandbox"></a>

To use the sandbox, complete the following steps:

1. Create an IAM role:

   Create an IAM role in the AWS account linked with your AWS Partner Central account.

1. Assign Policy:

   Assign the following policy to the IAM role. For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

   ```
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
         "Sid": "TaggingAccess",
         "Effect": "Allow",
         "Action": [
           "partnercentral:TagResource",
           "partnercentral:UntagResource",
           "partnercentral:ListTagsForResource"
         ],
         "Resource": [
           "arn:aws:partnercentral:*:*:catalog/Sandbox/partner/*"
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

```
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

```
{
  "source": ["aws.partnercentral-account"],
  "detail": {
    "catalog": ["Sandbox"]
  }
}
```

Event rules that specify `catalog` as `Sandbox` will only match events coming from the sandbox, generated by the actions you perform in the sandbox environment.
# Identity and access management in Amazon SES

You can use AWS Identity and Access Management (IAM) with Amazon Simple Email Service (Amazon SES) to specify which SES API
actions an user, group, or role can perform. (In this topic we refer to these
entities collectively as _user_.) You can also control which email
addresses the user can use for the "From", recipient, and "Return-Path" addresses of
emails.

For example, you can create an IAM policy that allows users in your organization to send
email, but not perform administrative actions such as checking sending statistics. As
another example, you can write a policy that allows a user to send emails through SES
from your account, but only if they use a specific "From" address.

To use IAM, you define an IAM policy, which is a document that explicitly defines
permissions, and attach the policy to a user. To learn how to create IAM policies, see the
[IAM User Guide](../../../IAM/latest/UserGuide/policies_overview.md "../../../IAM/latest/UserGuide/policies_overview.md"). Other than
applying the restrictions you set in your policy, there are no changes to how users interact
with SES or in how SES carries out requests.

###### Note

- If your account is in the SES sandbox, its restrictions well prevent
  the implementation of some of these polices - see [Request production
  access](request-production-access.md "request-production-access.md").
- You can also control access to SES by using sending authorization
  policies. Whereas IAM policies constrain what individual users
  can do, sending authorization policies constrain how individual verified
  identities can be used. Further, only sending authorization policies can grant
  cross-account access. For more information about sending authorization, see
  [Using sending authorization with Amazon SES](sending-authorization.md "sending-authorization.md").
  If you are looking for information about how to generate SES SMTP credentials for
  an existing user, see [Obtaining Amazon SES SMTP credentials](smtp-credentials.md "smtp-credentials.md").

## Creating IAM Policies for Access to SES

This section explains how you can use IAM policies specifically with SES. To
learn how to create IAM policies in general, see the [IAM User Guide](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md").

There are three reasons you might use IAM with SES:

- To restrict the email-sending action.
- To restrict the "From", recipient, and "Return-Path" addresses of the emails
  that the user sends.
- To control general aspects of API usage such as the time period during which a
  user is permitted to call the APIs that they are authorized to use.

### Restricting the Action

To control which SES actions a user can perform, you use the
`Action` element of an IAM policy. You can set the
`Action` element to any SES API action by prefixing the API
name with the lowercase string `ses:`. For example, you can set the
`Action` to `ses:SendEmail`,
`ses:GetSendStatistics`, or `ses:*` (for all
actions).

Then, depending on the `Action`, specify the `Resource`
element as follows:

**If the `Action` element only permits access to
email-sending APIs (that is, `ses:SendEmail` and/or
`ses:SendRawEmail`):**

- To allow the user to send from any identity in your AWS account, set
  `Resource` to \*
- To restrict the identities that a user is allowed to send from, set
  `Resource` to the ARNs of the identities that you are
  permitting the user to use.

**If the `Action` element permits access to all
APIs:**

- If you don't want to restrict the identities that the user can send from,
  set `Resource` to \*
- If you want to restrict the identities that a user is allowed to send
  from, you need to create two policies (or two statements within one
  policy):
  - One with `Action` set to an explicit list of the
    permitted non-email-sending APIs and `Resource` set to \*
  - One with `Action` set to one of the email-sending APIs
    (`ses:SendEmail` and/or
    `ses:SendRawEmail`), and `Resource` set to the
    ARN(s) of the identities you are permitting the user to use.

For a list of available SES actions, see the [Amazon Simple Email Service API Reference](../APIReference.md "../APIReference.md"). If the
user will be using the SMTP interface, you must allow access to
`ses:SendRawEmail` at a minimum.

### Restricting Email Addresses

If you want to restrict the user to specific email addresses, you can use a
`Condition` block. In the `Condition` block, you specify
conditions by using condition keys as described in the [IAM User Guide](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition"). By using condition keys, you can control the
following email addresses:

###### Note

These email address condition keys apply only to the APIs noted in the
following table.

| Condition Key               | Description                                                                                                                                                                                                                                                                                                                                                     | API                                       |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ses:Recipients`            | Restricts the recipient addresses, which include the To:, "CC", and "BCC" addresses.                                                                                                                                                                                                                                                                            | `SendEmail`, `SendRawEmail`               |
| `ses:FromAddress`           | Restricts the "From" address.                                                                                                                                                                                                                                                                                                                                   | `SendEmail`, `SendRawEmail`, `SendBounce` |
| `ses:FromDisplayName`       | Restricts the "From" address that is used as the display name.                                                                                                                                                                                                                                                                                                  | `SendEmail`, `SendRawEmail`               |
| `ses:FeedbackAddress`       | Restricts the "Return-Path" address, which is the address where bounces and complaints can be sent to you by email feedback forwarding. For information about email feedback forwarding, see [Receiving Amazon SES notifications through email](monitor-sending-activity-using-notifications-email.md "monitor-sending-activity-using-notifications-email.md"). | `SendEmail`, `SendRawEmail`               |
| `ses:MultiRegionEndpointId` | Allows you to control what endpoint ID is used when sending email                                                                                                                                                                                                                                                                                               | `SendEmail`, `SendBulkEmail`              | ### Restricting by SES API version By using the `ses:ApiVersion` key in conditions, you can restrict access to SES based on the version of the SES API. ###### Note The SES SMTP interface uses SES API version 2 of `ses:SendRawEmail`. ### Restricting General API Usage By using AWS-wide keys in conditions, you can restrict access to SES based on aspects such as the date and time that user is permitted access to APIs. SES implements only the following AWS-wide policy keys: <br>• `aws:CurrentTime` <br>• `aws:EpochTime` <br>• `aws:SecureTransport` <br>• `aws:SourceIp` <br>• `aws:SourceVpc` <br>• `aws:SourceVpce` <br>• `aws:UserAgent` <br>• `aws:VpcSourceIp` For more information about these keys, see the [IAM User Guide](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#Condition"). ## Example IAM Policies for SES This topic provides examples of policies that permit a user access to SES, but only under certain conditions. ###### Policy examples in this section: <br>• [Allowing Full Access to All SES Actions](#iam-and-ses-examples-full-access "#iam-and-ses-examples-full-access") <br>• [Allowing Access to only SES API version 2](#iam-and-ses-examples-access-specific-ses-api-version "#iam-and-ses-examples-access-specific-ses-api-version") <br>• [Allowing Access to Email-Sending Actions Only](#iam-and-ses-examples-email-sending-actions "#iam-and-ses-examples-email-sending-actions") <br>• [Restricting the Time Period of Sending](#iam-and-ses-examples-time-period "#iam-and-ses-examples-time-period") <br>• [Restricting the Recipient Addresses](#iam-and-ses-examples-recipients "#iam-and-ses-examples-recipients") <br>• [Restricting the "From" Address](#iam-and-ses-examples-from-address "#iam-and-ses-examples-from-address") <br>• [Restricting the Display Name of the Email Sender](#iam-and-ses-examples-display-name "#iam-and-ses-examples-display-name") <br>• [Restricting the Destination of Bounce and Complaint Feedback](#iam-and-ses-examples-feedback "#iam-and-ses-examples-feedback") ### Allowing Full Access to All SES Actions The following policy allows a user to call any SES action. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:*" ], "Resource":"*" } ] }` `` ### Allowing Access to only SES API version 2 The following policy allows a user to call only the SES actions of API version 2. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:*" ], "Resource":"*", "Condition": { "StringEquals" : { "ses:ApiVersion" : "2" } } } ] }` `` ### Allowing Access to Email-Sending Actions Only The following policy permits a user to send email using SES, but does not permit the user to perform administrative actions such as accessing SES sending statistics. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*" } ] }` `` ### Restricting the Time Period of Sending The following policy permits a user to call SES email-sending APIs only during the month of September 2018. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*", "Condition":{ "DateGreaterThan":{ "aws:CurrentTime":"2018-08-31T12:00Z" }, "DateLessThan":{ "aws:CurrentTime":"2018-10-01T12:00Z" } } } ] }` `` ### Restricting the Recipient Addresses The following policy permits a user to call the SES email-sending APIs, but only to recipient addresses in domain _example.com_ (`StringLike` _is case sensitive_). JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*", "Condition":{ "ForAllValues:StringLike":{ "ses:Recipients":[ "*@example.com" ] } } } ] }` `` ### Restricting the "From" Address The following policy permits a user to call the SES email-sending APIs, but only if the "From" address is *marketing@example.com*. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*", "Condition":{ "StringEquals":{ "ses:FromAddress":"marketing@example.com" } } } ] }` `` The following policy permits a user to call the [SendBounce](../APIReference/API_SendBounce.md "../APIReference/API_SendBounce.md") API, but only if the "From" address is *bounce@example.com*. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendBounce" ], "Resource":"*", "Condition":{ "StringEquals":{ "ses:FromAddress":"bounce@example.com" } } } ] }` `` ### Restricting the Display Name of the Email Sender The following policy permits a user to call the SES email-sending APIs, but only if the display name of the "From" address includes _Marketing_ (`StringLike` _is case sensitive_). JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*", "Condition":{ "StringLike":{ "ses:FromDisplayName":"Marketing" } } } ] }` `` ### Restricting the Destination of Bounce and Complaint Feedback The following policy permits a user to call the SES email-sending APIs, but only if the "Return-Path" of the email is set to *feedback@example.com*. JSON `` `{ "Version":"2012-10-17", "Statement":[ { "Effect":"Allow", "Action":[ "ses:SendEmail", "ses:SendRawEmail" ], "Resource":"*", "Condition":{ "StringEquals":{ "ses:FeedbackAddress":"feedback@example.com" } } } ] }` `` |

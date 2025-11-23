# Quotas for AWS End User Messaging SMS

Your AWS account has default quotas, formerly referred to as limits, for each
AWS service. Unless otherwise noted, each quota is Region-specific. You can request
increases for some quotas, and other quotas cannot be increased.

To request a quota increase, see [Requesting a quota increase with Support](#quotas-increase "#quotas-increase").

Your AWS account has the following quotas related to AWS End User Messaging SMS.

The following table lists the Requests Per Second (RPS) quota for each resource of the
AWS End User Messaging SMS and Voice v2 API. All Resources are eligible for a rate increase by following the
directions by following the directions in [Requesting a quota
increase](#quotas-increase "#quotas-increase").

| Resource                                        | Default quota rate (requests per second) |
| ----------------------------------------------- | ---------------------------------------- |
| AssociateOriginationIdentity                    | 1                                        |
| AssociateProtectConfiguration                   | 1                                        |
| CreateConfigurationSet                          | 1                                        |
| CreateEventDestination                          | 1                                        |
| CreateOptOutList                                | 1                                        |
| CreatePool                                      | 1                                        |
| CreateProtectConfiguration                      | 1                                        |
| CreateRegistration                              | 1                                        |
| CreateRegistrationAssociation                   | 1                                        |
| CreateRegistrationAttachment                    | 1                                        |
| CreateRegistrationVersion                       | 1                                        |
| CreateVerifiedDestinationNumber                 | 1                                        |
| DeleteAccountDefaultProtectConfiguration        | 1                                        |
| DeleteConfigurationSet                          | 1                                        |
| DeleteDefaultMessageType                        | 1                                        |
| DeleteDefaultSenderId                           | 1                                        |
| DeleteEventDestination                          | 1                                        |
| DeleteKeyword                                   | 1                                        |
| DeleteMediaMessageSpendLimitOverride            | 1                                        |
| DeleteOptedOutNumber                            | 10                                       |
| DeleteOptOutList                                | 1                                        |
| DeletePool                                      | 1                                        |
| DeleteProtectConfiguration                      | 1                                        |
| DeleteProtectConfigurationRuleSetNumberOverride | 1                                        |
| DeleteRegistration                              | 1                                        |
| DeleteRegistrationAttachment                    | 1                                        |
| DeleteRegistrationFieldValue                    | 1                                        |
| DeleteTextMessageSpendLimitOverride             | 1                                        |
| DeleteVerifiedDestinationNumber                 | 1                                        |
| DeleteVoiceMessageSpendLimitOverride            | 1                                        |
| DescribeAccountAttributes                       | 1                                        |
| DescribeAccountLimits                           | 1                                        |
| DescribeConfigurationSets                       | 1                                        |
| DescribeKeywords                                | 1                                        |
| DescribeOptedOutNumbers                         | 1                                        |
| DescribeOptOutLists                             | 1                                        |
| DescribePhoneNumbers                            | 1                                        |
| DescribePools                                   | 1                                        |
| DescribeProtectConfiguration                    | 1                                        |
| DescribeRegistrationAttachments                 | 1                                        |
| DescribeRegistrationFieldDefinitions            | 1                                        |
| DescribeRegistrationFieldValues                 | 1                                        |
| DescribeRegistrations                           | 1                                        |
| DescribeRegistrationSectionDefinitions          | 1                                        |
| DescribeRegistrationTypeDefinitions             | 1                                        |
| DescribeRegistrationVersions                    | 1                                        |
| DescribeSenderIds                               | 1                                        |
| DescribeSpendLimits                             | 1                                        |
| DescribeVerifiedDestinationNumbers              | 1                                        |
| DisassociateOriginationIdentity                 | 1                                        |
| DisassociateProtectConfiguration                | 1                                        |
| DiscardRegistrationVersion                      | 1                                        |
| GetProtectConfigurationCountryRuleSet           | 1                                        |
| ListPoolOriginationIdentities                   | 1                                        |
| ListProtectConfigurationRuleSetNumberOverrides  | 1                                        |
| ListRegistrationAssociations                    | 1                                        |
| ListTagsForResource                             | 10                                       |
| ProtectConfiguration                            | 1                                        |
| PutKeyword                                      | 1                                        |
| PutMessageFeedback                              | 20                                       |
| PutOptedOutNumber                               | 10                                       |
| PutProtectConfigurationRuleSetNumberOverride    | 1                                        |
| PutRegistrationFieldValue                       | 1                                        |
| ReleasePhoneNumber                              | 1                                        |
| ReleaseSenderId                                 | 1                                        |
| RequestPhoneNumber                              | 1                                        |
| RequestSenderId                                 | 1                                        |
| SendDestinationNumberVerificationCode           | 1                                        |
| SendMediaMessage                                | 1                                        |
| SendTextMessage                                 | 1                                        |
| SendVoiceMessage                                | 1                                        |
| SetAccountDefaultProtectConfiguration           | 1                                        |
| SetDefaultMessageFeedbackEnabled                | 1                                        |
| SetDefaultMessageType                           | 1                                        |
| SetDefaultSenderId                              | 1                                        |
| SetMediaMessageSpendLimitOverride               | 1                                        |
| SetTextMessageSpendLimitOverride                | 1                                        |
| SetVoiceMessageSpendLimitOverride               | 1                                        |
| SubmitRegistrationVersion                       | 1                                        |
| TagResource                                     | 1                                        |
| UntagResource                                   | 1                                        |
| UpdateEventDestination                          | 1                                        |
| UpdatePhoneNumber                               | 1                                        |
| UpdateProtectConfiguration                      | 1                                        |
| UpdateProtectConfigurationCountryRuleSet        | 1                                        |
| UpdatePool                                      | 1                                        |
| UpdateSenderId                                  | 1                                        |
| VerifyDestinationNumber                         | 1                                        |

## SMS and MMS quotas

The following quotas apply to the SMS and MMS channel.

| Resource                                                                                         | Default quota                                                                                                                                                                                                | Eligible for increase                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Spending threshold                                                                               | USD $1.00 per account                                                                                                                                                                                        | [Yes](awssupport-spend-threshold.md "awssupport-spend-threshold.md"), but<br>spending limits vary by region. You must specify the region(s) in<br>which you require an increase.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Number of SMS messages that can be sent each second (_sending rate_)                             | Varies depending on destination country and originating phone<br>number. For more information, see [What are the Message Parts per Second (MPS)<br>limits](sms-limitations-mps.md "sms-limitations-mps.md"). | [Yes](#quotas-increase "#quotas-increase"), however, you might<br>need to obtain a phone number that supports higher throughput. If<br>you're unsure of which number type to use, contact Support or your<br>AWS Account Manager for more information<br>If you use an alphanumeric Sender ID to send messages, you might<br>be able to increase your throughput rate. To find out if a<br>throughput increase is available for your Sender ID, [How to request a sender ID through Support](sender-id-awssupport-open.md "sender-id-awssupport-open.md") in the Support Center Console. In<br>your request, include your existing Sender ID, the country in which<br>you use that Sender ID, and the throughput rate you want to<br>request. |
| Number of SMS and MMS messages that can be sent to a single recipient<br>each second             | 1 message per second                                                                                                                                                                                         | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of Amazon SNS topics for two-way SMS                                                      | 100,000 per account                                                                                                                                                                                          | [Yes](#quotas-increase "#quotas-increase")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Number of Keywords for two-way SMS                                                               | 30 Keywords per number                                                                                                                                                                                       | [Yes](#quotas-increase "#quotas-increase")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Number of SMS, MMS, and Voice numbers                                                            | 25 per account                                                                                                                                                                                               | [Yes](#quotas-increase "#quotas-increase")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Number of dedicated phone numbers                                                                | 25 per account                                                                                                                                                                                               | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of opt-out lists<br>Note: The required Default opt-out list counts against this<br>quota. | 25 per account                                                                                                                                                                                               | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of configuration sets                                                                     | 25 per account                                                                                                                                                                                               | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of event destinations                                                                     | 5 per configuration set                                                                                                                                                                                      | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of verified destination phone numbers while in SMS<br>sandbox                             | 10 per account                                                                                                                                                                                               | No                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of phone number pools                                                                     | 25 per account                                                                                                                                                                                               | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Number of origination identities that can be associated with a phone<br>number pool              | 100 per phone number pool                                                                                                                                                                                    | [Yes](#quotas-increase "#quotas-increase")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Number of SenderIDs                                                                              | 200 per account                                                                                                                                                                                              | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## 10DLC quotas

The following quotas apply to SMS messages sent using 10DLC phone numbers. 10DLC
numbers can only be used to send messages to recipients in the United States.

| Resource            | Default quota         | Eligible for increase                      |
| ------------------- | --------------------- | ------------------------------------------ |
| Max 10DLC companies | 25 per account        | [Yes](#quotas-increase "#quotas-increase") |
| Max 10DLC campaigns | 10 per 10DLC brand    | [Yes](#quotas-increase "#quotas-increase") |
| Max 10DLC numbers   | 49 per 10DLC campaign | No                                         |

## Protect configuration quotas

The following quotas apply to protect configurations.

| Resource                         | Default quota  | Eligible for increase                                              |
| -------------------------------- | -------------- | ------------------------------------------------------------------ |
| Number of protect configurations | 25 per account | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service") |

## Registration quotas

The following quotas apply to registrations.

| Resource                           | Default quota  | Eligible for increase                                              |
| ---------------------------------- | -------------- | ------------------------------------------------------------------ |
| Number of registrations            | 25 per account | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service") |
| Number of registration attachments | 25 per account | [Yes](#quotas-increase-aws-service "#quotas-increase-aws-service") |

## Voice quotas

The following quotas apply to the voice channel.

###### Note

When your account is removed from the sandbox, you automatically qualify for the
maximum quotas shown in the following table.

| Resource                                                                                       | Default quota                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | Eligible for increase |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| Number of voice messages that can be sent during a 24-hour<br>period                           | If your account is in the sandbox: 20 messages                                                                                                                                                                                                                                                                                                                                                                                                                                     | No                    |
| Number of voice messages that can be sent to a single recipient<br>during a 24-hour period     | 5 messages                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | No                    |
| Number of voice messages that can be sent per minute                                           | If your account is in the sandbox: 5 calls per minuteIf your<br>account is out of the sandbox: 20 calls per minute                                                                                                                                                                                                                                                                                                                                                                 | No                    |
| Number of voice messages that can be sent from a single originating<br>phone number per second | 1 message per second                                                                                                                                                                                                                                                                                                                                                                                                                                                               | No                    |
| Voice message length                                                                           | If your account is in the sandbox: 30 secondsIf your account is<br>out of the sandbox: 5 minutes                                                                                                                                                                                                                                                                                                                                                                                   | No                    |
| Ability to send voice messages to international phone numbers                                  | If your account is in the sandbox, you can send messages to<br>recipients in only the following countries:<br>• Australia<br>• Canada<br>• Germany<br>• Hong Kong<br>• Israel<br>• Japan<br>• Mexico<br>• Singapore<br>• Sweden<br>• United States<br>• United Kingdom<br>If your account is out of the sandbox, you can send messages to<br>recipients in any country.<br>NoteInternational calls are subject to additional fees, which vary<br>by destination country or region. | No                    |
| Number of characters in a voice message                                                        | 3,000 billable characters, in words that are spoken 6,000<br>characters total, including billable characters and SSML<br>tags                                                                                                                                                                                                                                                                                                                                                      | No                    |
| Number of configuration sets                                                                   | 10,000 voice configuration sets                                                                                                                                                                                                                                                                                                                                                                                                                                                    | No                    |

## Requesting a quota increase with Support

If the value in the **Eligible for Increase** column in any of the
preceding tables is **Yes**, you can request an increase for that
quota.

###### To request a quota increase

1. Create an AWS Support case at [https://support.console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase](https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase "https://console.aws.amazon.com/support/home#/case/create?issueType=service-limit-increase").
2. Under **Service quota increase**, do the following:
   - For **Service**, choose
     **AWS End User Messaging SMS (Pinpoint)**.
   - (Optional) For **Provide a link to the site or app which will
     be sending SMS messages**, provide information about the
     website, application, or service that will send SMS messages.
   - (Optional) For **What type of messages do you plan to
     send**, choose the type of message that you plan to send
     using your long code:
     - **One Time Password** – Messages that
       provide passwords that your customers use to authenticate with
       your website or application.
     - **Promotional** – Noncritical messages
       that promote your business or service, such as special offers or
       announcements.
     - **Transactional** – Important
       informational messages that support customer transactions, such
       as order confirmations or account alerts. Transactional messages
       must not contain promotional or marketing content.

   - (Optional) For **Which AWS Region will you be sending
     messages from**, choose the AWS Region that you will be
     sending messages from.
   - (Optional) For **Which countries do you plan to send messages
     to**, enter the country or region that you want to purchase
     short codes in.
   - (Optional) In the **How do your customers opt to receive
     messages from you**, provide details about your opt-in
     process.
   - (Optional) In the **Please provide the message template that
     you plan to use to send messages to your customers** field,
     include the template that you will be using.

3. Under **Requests**, do one of the following:
   - For **Region**, choose your AWS Region.
   - For **Resource Type**, choose **General
     Limits**.
   - For **Quota**, choose the quota to change.
   - For **New quota value** enter a new value for the
     quota.
   - To request an increase to the same quota in an additional
     AWS Region, choose **Add another request**, and then
     choose the additional AWS Region and fill out the new request.

4. Under **Case description**, for **Use case
   description**, explain why you're requesting the quota
   increase.
5. Under **Contact options**, for **Preferred contact
   language**, choose the language that you prefer to use when
   communicating with the AWS Support team.
6. For **Contact method**, choose your preferred method of
   communicating with the AWS Support team.
7. Choose **Submit**.

## Requesting a quota increase using AWS

Service Quotas

Increase your quotas at the account or resource level in Getting Started with the AWS
Management Console.

###### To request a service quota increase

1. Sign in to the **AWS Management Console** and open the **Service Quotas** console at
   [https://console.aws.amazon.com/servicequotas/home](https://console.aws.amazon.com/servicequotas/home "https://console.aws.amazon.com/servicequotas/home").
2. In the navigation pane, choose **AWS Services**.
3. Choose an AWS service from the list, or enter the name of the service in the
   search box.
4. If the quota is adjustable, you can request a quota increase at either the
   account-level or resource-level, based on the value listed in the **Adjustability**
   column.
   - **Account-level** - Request a quota increase at the
     account-level for an account-level quota such as
     **TextMessageMonthlySpend per Region for AWS End
     User Messaging**. To request an account-level increase, select the quota from the list and choose
     **Request increase at account-level**.
   - **Resource-level** - Request a quota increase for a
     specific resource for a resource-level quota such as
     **TextMessageMonthlySpend for AWS End User
     Messaging**. To request a resource-level increase, choose the quota name to view additional
     information. Under the **Resource-level quotas** section, select
     the resource for which you want to increase the quota value, and choose
     **Request increase at resource-level**.

5. For the **Increase quota** value, enter the new value. The new
   value must be greater than the current value.
6. Choose **Request**.
7. To view any pending or recently resolved requests in the console, navigate to
   the **Request history** tab from the service's details page or
   choose **Dashboard** from the navigation pane. For pending
   requests, choose the status of the request to open the request receipt. The
   initial status of a request is **Pending**. After the status
   changes to **Quota requested**, the Support case number is
   shown. Choose the case number to open the ticket for your request.

The AWS Support team provides an initial response to your request within 24 hours.

In order to prevent our systems from being used to send unsolicited or malicious content, we have to
consider each request carefully. If we’re able to do so, we'll grant your request within this 24-hour
period. However, if we need to obtain additional information from you, it might take longer to resolve your
request.

We might not be able to grant your request if your use case doesn’t align with our policies.

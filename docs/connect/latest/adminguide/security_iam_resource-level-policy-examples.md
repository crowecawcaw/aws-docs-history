# Amazon Connect

resource-level policy examples

Amazon Connect supports resource-level permissions for users, so you can specify actions for them
for an instance, as shown in the following policies.

###### Contents

- [Deny all actions on an
  Amazon Connect instance](#connect-access-control-resources-example-all "#connect-access-control-resources-example-all")
- [Deny the "delete" and
  "update" actions](#connect-access-control-resources-example2 "#connect-access-control-resources-example2")
- [Allow actions for
  integrations with specific names](#connect-access-control-resources-integration-example "#connect-access-control-resources-integration-example")
- [Allow "create users" but
  deny if you're assigned to a specific security profile](#connect-access-control-resources-example3 "#connect-access-control-resources-example3")
- [Allow recording actions on a
  contact](#connect-access-control-resources-example4 "#connect-access-control-resources-example4")
- [Allow or Deny queue API
  actions for phone numbers in a replica Region](#allow-deny-queue-actions-replica-region "#allow-deny-queue-actions-replica-region")
- [View specific Amazon AppIntegrations
  resources](#view-specific-appintegrations-resources "#view-specific-appintegrations-resources")
- [Grant access to Amazon Connect Customer
  Profiles](#grant-access-to-customer-profiles "#grant-access-to-customer-profiles")
- [Grant read-only access to
  Customer Profiles data](#grant-read-only-access-to-customer-profiles "#grant-read-only-access-to-customer-profiles")
- [Query Amazon Q in Connect only for a specific
  Assistant](#query-wisdom-assistant "#query-wisdom-assistant")
- [Grant full access to
  Amazon Connect Voice ID](#grant-read-only-access-to-voiceid "#grant-read-only-access-to-voiceid")
- [Grant access to Amazon Connect
  outbound campaigns resources](#grant-read-only-access-to-outboundcommunications "#grant-read-only-access-to-outboundcommunications")
- [Restrict the
  ability to search on transcripts analyzed by Amazon Connect Contact Lens](#restrict-ability-to-search-transcripts-contact-lens "#restrict-ability-to-search-transcripts-contact-lens")

## Deny all actions on an

Amazon Connect instance

An Amazon Connect instance is the top-level resource within Amazon Connect. All other sub-resources are
created within its scope. To deny all actions on all resources within an Amazon Connect instance,
you can use one of the following methods:

- Use `connect:instanceId` context keys.
- Use Instance ARN followed by a wildcard (\*).

The following sample policy denies all connect actions for the instance with
instanceId 00fbeee1-123e-111e-93e3-11111bfbfcc1.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "connect:*",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "connect:instanceId": "00fbeee1-123e-111e-93e3-11111bfbfcc1"
 }
 }
 }
 ]
}`

```

Alternatively, you can deny all actions by specifying the Instance ARN followed by a
wildcard (\*) . The following sample policy denies all connect actions for the instance
with instance ARN
`arn:aws:connect:us-east-1:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc1`.

JSON

```
`{
"Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "connect:*"
 ],
 "Resource": "arn:aws:connect:us-east-1:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc1*"
 }
 ]
}`

```

## Deny the "delete" and

"update" actions

This following sample policy denies the "delete" and "update" actions for users in
one Amazon Connect instance. It uses a wild card at the end of the Amazon Connect user ARN so that "delete
user" and "update user" are denied on the full user ARN (that is, all Amazon Connect users in the
provided instance, such as
arn:aws:connect:us-east-1:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc1/agent/00dtcddd1-123e-111e-93e3-11111bfbfcc1).

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": [
 "connect:DeleteUser",
 "connect:UpdateUser*"
 ],
 "Resource": "arn:aws:connect:us-east-1:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc1/agent/*"
 }
 ]
}`

```

## Allow actions for

integrations with specific names

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AllowAllAppIntegrationsActions",
 "Effect": "Allow",
 "Action": [
 "app-integrations:ListEventIntegrations",
 "app-integrations:CreateEventIntegration",
 "app-integrations:GetEventIntegration",
 "app-integrations:UpdateEventIntegration",
 "app-integrations:DeleteEventIntegration"
 ],
 "Resource":"arn:aws:app-integrations:*:*:event-integration/MyNamePrefix-*"
 }
 ]
}`

```

## Allow "create users" but

deny if you're assigned to a specific security profile

The following sample policy allows "create users" but explicitly denies using
arn:aws:connect:us-west-2:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc1/security-profile/11dtcggg1-123e-111e-93e3-11111bfbfcc17
as the parameter for security profile in [CreateUser](../APIReference/API_CreateUser.md#API_CreateUser_RequestBody "../APIReference/API_CreateUser.md#API_CreateUser_RequestBody") request.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "connect:CreateUser"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Deny",
 "Action": [
 "connect:CreateUser"
 ],
 "Resource": "arn:aws:connect:us-west-2:123456789012:instance/00fbeee1-123e-111e-93e3-11111bfbfcc17/security-profile/11dtcggg1-123e-111e-93e3-11111bfbfcc17"
 }
 ]
}`

```

## Allow recording actions on a

contact

The following sample policy allows "start contact recording" on a contact in a
specific instance. Since contactID is dynamic, \* is used.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "connect:StartContactRecording"
 ],
 "Resource": "arn:aws:connect:us-west-2:111122223333:instance/instanceId/contact/*",
 "Effect": "Allow"
 }
 ]
}`

```

Set up a trusted relationship with _accountID_.

The following actions are defined for the recording APIs:

- "connect:StartContactRecording"
- "connect:StopContactRecording"
- "connect:SuspendContactRecording"
- "connect:ResumeContactRecording"

### Allow more contact Actions in the same

role

If the same role is used to calling other contact APIs, you can list the following
contact actions:

- GetContactAttributes
- ListContactFlows
- StartChatContact
- StartOutboundVoiceContact
- StopContact
- UpdateContactAttributes

Or use a wildcard to allow all contact actions, for example: "connect:\*"

### Allow more resources

You can also use a wildcard to allow more resources. For example, here's how to
allow all connect actions on all contact resources:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "connect:*"
 ],
 "Resource": "arn:aws:connect:us-west-2:111122223333:instance/*/contact/*",
 "Effect": "Allow"
 }
 ]
}`

```

## Allow or Deny queue API

actions for phone numbers in a replica Region

The [CreateQueue](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md") and [UpdateQueueOutboundCallerConfig](../APIReference/API_UpdateQueueOutboundCallerConfig.md "../APIReference/API_UpdateQueueOutboundCallerConfig.md") APIs contain an input field named
`OutboundCallerIdNumberId`. This field represents a phone number resource
that can be claimed to a traffic distribution group. It supports both the phone number
V1 ARN format that is returned by [ListPhoneNumbers](../APIReference/API_ListPhoneNumbers.md "../APIReference/API_ListPhoneNumbers.md")
and the V2 ARN format that is returned by [ListPhoneNumbersV2](../APIReference/API_ListPhoneNumbersV2.md "../APIReference/API_ListPhoneNumbersV2.md").

Following are the V1 and V2 ARN formats that `OutboundCallerIdNumberId`
supports:

- **V1 ARN format**:
  `arn:aws:connect:`your-region`:`your-account_id`:instance/`instance_id`/phone-number/`resource_id``
- **V2 ARN format**:
  `arn:aws:connect:`your-region`:`your-account_id`:phone-number/`resource_id``

###### Note

We recommend using the V2 ARN format. The V1 ARN format is going to be deprecated
in the future.

### Provide both ARN formats for phone number

resources in the replica Region

If the phone number is claimed to a traffic distribution group, to correctly
allow/deny access to queue API actions for phone number resources while operating in
the replica Region **you must provide the phone number resource
in both V1 and V2 ARN formats**. If you provide the phone number resource
in only one ARN format, it does not result in the correct allow/deny behavior while
operating in the replica Region.

### Example 1: Deny access to

CreateQueue

For example, you're operating in the replica Region us-west-2 with account `123456789012` and instance
`aaaaaaaa-bbbb-cccc-dddd-0123456789012`. You want to deny access to
[CreateQueue](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md") API when the `OutboundCallerIdNumberId` value is a
phone number claimed to a traffic distribution group with resource ID
`aaaaaaaa-eeee-ffff-gggg-0123456789012`. In this scenario you must use
the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyCreateQueueForSpecificNumber",
 "Effect": "Deny",
 "Action": "connect:CreateQueue",
 "Resource": [
 "arn:aws:connect:us-east-1:123456789012:phone-number/aaaaaaaa-eeee-ffff-gggg-0123456789012",
 "arn:aws:connect:us-west-2:123456789012:instance/aaaaaaaa-bbbb-cccc-dddd-0123456789012/phone-number/aaaaaaaa-eeee-ffff-gggg-0123456789012"
 ]
 }
 ]
}`

```

Where us-west-2 is the Region where the request is being made.

### Example 2: Only allow access to

UpdateQueueOutboundCallerConfig

For example, you're operating in the replica Region us-west-2 with account
`123456789012` and instance
`aaaaaaaa-bbbb-cccc-dddd-0123456789012`. You want to only allow access
to [UpdateQueueOutboundCallerConfig](../APIReference/API_UpdateQueueOutboundCallerConfig.md "../APIReference/API_UpdateQueueOutboundCallerConfig.md") API when the
`OutboundCallerIdNumberId` value is a phone number claimed to a traffic
distribution group with resource ID
`aaaaaaaa-eeee-ffff-gggg-0123456789012`. In this scenario you must use
the following policy:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "OnlyAllowUpdateQueueOutboundCallerConfigForSpecificNumber",
 "Effect": "Allow",
 "Action": "connect:UpdateQueueOutboundCallerConfig",
 "Resource": [
 "arn:aws:connect:us-east-1:123456789012:phone-number/aaaaaaaa-eeee-ffff-gggg-0123456789012",
 "arn:aws:connect:us-west-2:123456789012:instance/aaaaaaaa-bbbb-cccc-dddd-0123456789012/phone-number/aaaaaaaa-eeee-ffff-gggg-0123456789012"
 ]
 }
 ]
}`

```

## View specific Amazon AppIntegrations

resources

The following sample policy allows a specific event integrations to be
fetched.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "app-integrations:GetEventIntegration"
 ],
 "Resource": "arn:aws:app-integrations:us-west-2:`111122223333`:event-integration/Name"
 }
 ]
}`

```

## Grant access to Amazon Connect Customer

Profiles

Amazon Connect Customer Profiles use `profile` as the prefix for actions instead of
`connect`. The following policy grants full access to a specific domain in
Amazon Connect Customer Profiles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "profile:*"
 ],
 "Resource": "arn:aws:profile:us-west-2:`111122223333`:domains/domainName",
 "Effect": "Allow"
 }
 ]
}`

```

Set up a trusted relationship with accountID to domain domainName.

## Grant read-only access to

Customer Profiles data

Following is an example for granting read access to the data in Amazon Connect Customer
Profiles.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "profile:SearchProfiles"
 ],
 "Resource": "arn:aws:profile:`us-east-1`:`111122223333`:domains/domainName",
 "Effect": "Allow"
 }
 ]
}`

```

## Query Amazon Q in Connect only for a specific

Assistant

The following sample policy allows querying only a specific Assistant.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "wisdom:QueryAssistant"
 ],
 "Resource": "arn:aws:wisdom:`us-east-1`:`111122223333`:assistant/`assistantID`"
 }
 ]
}`

```

## Grant full access to

Amazon Connect Voice ID

Amazon Connect Voice ID uses `voiceid` as the prefix for actions instead of connect.
The following policy grants full access to a specific domain in Amazon Connect Voice ID:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "voiceid:*"
 ],
 "Resource": "arn:aws:voiceid:us-west-2:`111122223333`:domain/domainName",
 "Effect": "Allow"
 }
 ]
}`

```

Set up a trusted relationship with accountID to domain domainName.

## Grant access to Amazon Connect

outbound campaigns resources

Outbound campaigns uses `connect-campaign` as the prefix for actions instead of
`connect`. The following policy grants full access to a specific
outbound campaign.

```
{
    "Sid": "AllowConnectCampaignsOperations",
    "Effect": "Allow",
    "Action": [
        "connect-campaigns:DeleteCampaign",
        "connect-campaigns:DescribeCampaign",
        "connect-campaigns:UpdateCampaignName",
        "connect-campaigns:GetCampaignState"
        "connect-campaigns:UpdateOutboundCallConfig",
        "connect-campaigns:UpdateDialerConfig",
        "connect-campaigns:PauseCampaign",
        "connect-campaigns:ResumeCampaign",
        "connect-campaigns:StopCampaign"
    ],
    "Resource": "arn:aws:connect-campaigns:us-west-2:accountID:campaign/campaignId",
    }
```

## Restrict the

ability to search on transcripts analyzed by Amazon Connect Contact Lens

The following policy allows search and describe contacts, but denies searching a
contact using transcripts analyzed by Amazon Connect Contact Lens.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "VisualEditor0",
 "Effect": "Allow",
 "Action": [
 "connect:DescribeContact"
 ],
 "Resource": "arn:aws:connect:`us-east-1`:`111122223333`:instance/`instance-id`/contact/*"
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": [
 "connect:SearchContacts"
 ],
 "Resource": "arn:aws:connect:`us-east-1`:`111122223333`:instance/`instance-id`"
 },
 {
 "Sid": "VisualEditor2",
 "Effect": "Deny",
 "Action": [
 "connect:SearchContacts"
 ],
 "Resource": "arn:aws:connect:`us-east-1`:`111122223333`:instance/`instance-id`",
 "Condition": {
 "ForAnyValue:StringEquals": {
 "connect:SearchContactsByContactAnalysis": [
 "Transcript"
 ]
 }
 }
 }
 ]
}`

```

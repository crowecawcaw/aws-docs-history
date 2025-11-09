# Sending policy examples

Sending authorization enables you to specify the fine-grained conditions under which you
allow delegate senders to send on your behalf.

###### The following conditions and examples show you how to write policies to

control different aspects of sending:

- [Conditions specific to sending
  authorization](#sending-authorization-policy-conditions "#sending-authorization-policy-conditions")
- [Specifying the delegate
  sender](#sending-authorization-policy-example-sender "#sending-authorization-policy-example-sender")
- [Restricting the "From"
  address](#sending-authorization-policy-example-from "#sending-authorization-policy-example-from")
- [Restricting the time at which the
  delegate can send email](#sending-authorization-policy-example-time "#sending-authorization-policy-example-time")
- [Restricting the email sending
  action](#sending-authorization-policy-example-action "#sending-authorization-policy-example-action")
- [Restricting the display
  name of the email sender](#sending-authorization-policy-example-display-name "#sending-authorization-policy-example-display-name")
- [Using multiple
  statements](#sending-authorization-policy-example-multiple-statements "#sending-authorization-policy-example-multiple-statements")

## Conditions specific to sending

authorization

A _condition_ is any restriction about the permission in the statement.
The part of the statement that specifies the conditions can be the most detailed of all the
parts. A _key_ is the specific characteristic that's the basis for access
restriction, such as the date and time of the request.

You use both conditions and keys together to express the restriction. For example, if you
want to restrict the delegate sender from making requests to Amazon SES on your behalf after July
30, 2019, you use the condition called `DateLessThan`. You use the key called
`aws:CurrentTime` and set it to the value `2019-07-30T00:00:00Z`.

You can use any of the AWS-wide keys listed at [Available
Keys](../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#AvailableKeys "../../../IAM/latest/UserGuide/AccessPolicyLanguage_ElementDescriptions.md#AvailableKeys") in the _IAM User Guide_, or you can use one of the
following keys specific to SES that are useful in sending authorization
policies:

| Condition key         | Description                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ses:Recipients`      | Restricts the recipient addresses, which include the To:, "CC", and "BCC"<br>addresses.                                                                                                                                                                                                                                                                                 |
| `ses:FromAddress`     | Restricts the "From" address.                                                                                                                                                                                                                                                                                                                                           |
| `ses:FromDisplayName` | Restricts the contents of the string that is used as the "From" display name<br>(sometimes called "friendly from"). For example, the display name of "John Doe<br><johndoe@example.com>" is John Doe.                                                                                                                                                                   |
| `ses:FeedbackAddress` | Restricts the "Return Path" address, which is the address where bounce and<br>complaints can be sent to you by email feedback forwarding. For information about<br>email feedback forwarding, see [Receiving Amazon SES<br>notifications through email](monitor-sending-activity-using-notifications-email.md "monitor-sending-activity-using-notifications-email.md"). |

You can use the `StringEquals` and `StringLike` conditions with
Amazon SES keys. These conditions are for case-sensitive string matching. For
`StringLike`, the values can include a multi-character match wildcard (\*) or a
single-character match wildcard (?) anywhere in the string. For example, the following
condition specifies that the delegate sender can only send from a "From" address that starts
with _invoicing_ and ends with _@example.com_:

```
"Condition": {
    "StringLike": {
      "ses:FromAddress": "invoicing*@example.com"
    }
}
```

You can also use the `StringNotLike` condition to prevent delegate senders from
sending email from certain email addresses. For example, you can disallow sending from
*admin@example.com*, and also similar addresses such as
_"admin"@example.com_, *admin+1@example.com*, or
*sender@admin.example.com*, by including the following condition in your
policy statement:

```
"Condition": {
    "StringNotLike": {
      "ses:FromAddress": "*admin*example.com"
    }
 }
```

For more information about how to specify conditions, see [IAM JSON Policy Elements:
Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.

## Specifying the delegate

sender

The _principal_, which is the entity to which you are granting
permission, can be an AWS account, an AWS Identity and Access Management (IAM) user, or an AWS service.

The following example shows a simple policy that allows AWS ID
_123456789012_ to send email from the verified identity
_example.com_ (which is owned by AWS account
_888888888888_). The `Condition` statement in this policy only
allows the delegate (that is, AWS ID _123456789012_) to send email from
the address _marketing+.\*@example.com_, where \*\** is any
string that the sender wants to add after *marketing+.\*.

JSON

```
`{
 "Id":"SampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeMarketer",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition":{
 "StringLike":{
 "ses:FromAddress":"marketing+.*@example.com"
 }
 }
 }
 ]
}`

```

The following example policy grants permission to two IAM users to send from identity
_example.com_. IAM users are specified by their Amazon Resource Name
(ARN).

JSON

```
`{
 "Id":"ExampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeIAMUser",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "arn:aws:iam::111122223333:user/John",
 "arn:aws:iam::444455556666:user/Jane"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ]
 }
 ]
}`

```

The following example policy grants permission to Amazon Cognito to send from identity
_example.com_.

JSON

```
`{
 "Id":"ExampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeService",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "Service":[
 "cognito-idp.amazonaws.com"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "888888888888",
 "aws:SourceArn": "arn:aws:cognito-idp:us-east-1:888888888888:userpool/your-user-pool-id-goes-here"
 }
 }
 }
 ]
}`

```

The following example policy grants permission to all accounts within an AWS
Organization to send from identity example.com. The AWS Organization is specified using the
[PrincipalOrgID](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md#condition-keys-principalorgid") global condition key.

JSON

```
`{
 "Id":"ExampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeOrg",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":"*",
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition":{
 "StringEquals":{
 "aws:PrincipalOrgID":"o-xxxxxxxxxxx"
 }
 }
 }
 ]
}`

```

## Restricting the "From"

address

If you use a verified domain, you may want to create a policy that allows only the
delegate sender to send from a specified email address. To restrict the "From" address, you
set a condition on the key called _ses:FromAddress_. The following policy
enables AWS account ID _123456789012_ to send from the identity
_example.com_, but only from the email address
*sender@example.com*.

JSON

```
`{
 "Id":"ExamplePolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeFromAddress",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition":{
 "StringEquals":{
 "ses:FromAddress":"sender@example.com"
 }
 }
 }
 ]
}`

```

## Restricting the time at which the

delegate can send email

You can also configure your sender authorization policy so that a delegate sender can send
email only at a certain time of day, or within a certain date range. For example, if you plan
to send an email campaign during the month of September 2021, you can use the following policy
to restrict the delegate's ability to send email to that month only.

JSON

```
`{
 "Id":"ExamplePolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ControlTimePeriod",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition":{
 "DateGreaterThan":{
 "aws:CurrentTime":"2021-08-31T12:00Z"
 },
 "DateLessThan":{
 "aws:CurrentTime":"2021-10-01T12:00Z"
 }
 }
 }
 ]
}`

```

## Restricting the email sending

action

There are two actions that senders can use to send an email with Amazon SES:
`SendEmail` and `SendRawEmail`, depending on how much control the
sender wants over the format of the email. Sending authorization policies enable you to
restrict the delegate sender to one of those two actions. However, many identity owners leave
the details of the email sending calls up to the delegate sender by enabling both actions in
their policies.

###### Note

If you want to enable the delegate sender to access Amazon SES through the SMTP interface,
you must choose `SendRawEmail` at a minimum.

If your use case is such that you want to restrict the action, you can do so by including
only one of the actions in your sending authorization policy. The following example shows you
how to restrict the action to `SendRawEmail`.

JSON

```
`{
 "Id":"ExamplePolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"ControlAction",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:SendRawEmail"
 ]
 }
 ]
}`

```

## Restricting the display

name of the email sender

Some email clients display the "friendly" name of the email sender (if the email header
provides it), rather than the actual "From" address. For example, the display name of "John
Doe <johndoe@example.com>" is John Doe. For instance, you might send emails from
*user@example.com*, but you prefer that recipients see that the email is
from _Marketing_ rather than from *user@example.com*.
The following policy enables AWS account ID 123456789012 to send from identity
_example.com_, but only if the display name of the "From" address
includes _Marketing_.

JSON

```
`{
 "Id":"ExamplePolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeFromAddress",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:888888888888:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:SendEmail",
 "ses:SendRawEmail"
 ],
 "Condition":{
 "StringLike":{
 "ses:FromDisplayName":"Marketing"
 }
 }
 }
 ]
}`

```

## Using multiple

statements

Your sending authorization policy can include multiple statements. The following example
policy has two statements. The first statement authorizes two AWS accounts to send from
*sender@example.com* as long as the "From" address and the feedback
address both use the domain _example.com_. The second statement authorizes
an IAM user to send email from *sender@example.com* as long as the
recipient's email address is under the _example.com_ domain.

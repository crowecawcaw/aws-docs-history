# Identity policy examples in

Amazon SES

Identity authorization enables you to specify the fine-grained conditions under which you
allow or deny API actions for an identity.

###### The following examples show you how to write policies to control different

aspects API actions:

- [Specifying the
  principal](#identity-authorization-policy-example-delegate-user "#identity-authorization-policy-example-delegate-user")
- [Restricting the
  action](#sending-authorization-policy-example-restricting-action "#sending-authorization-policy-example-restricting-action")
- [Using multiple
  statements](#identity-authorization-policy-example-multiple-statements "#identity-authorization-policy-example-multiple-statements")

## Specifying the

principal

The _principal_, which is the entity to which you are granting
permission, can be an AWS account, an AWS Identity and Access Management (IAM) user, or an AWS service that
belongs to the same account.

The following example shows a simple policy that allows AWS ID
_123456789012_ to control the verified identity
_example.com_ which is also owned by AWS account
_123456789012_.

JSON

```
`{
 "Id":"SampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeMarketer",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:123456789012:identity/example.com",
 "Principal":{
 "AWS":[
 "123456789012"
 ]
 },
 "Action":[
 "ses:DeleteEmailIdentity",
 "ses:PutEmailIdentityDkimSigningAttributes"
 ]
 }
 ]
}`

```

The following example policy grants permission to two users to control the
verified identity _example.com_. Users are specified by their Amazon
Resource Name (ARN).

JSON

```
`{
 "Id":"ExampleAuthorizationPolicy",
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"AuthorizeIAMUser",
 "Effect":"Allow",
 "Resource":"arn:aws:ses:us-east-1:123456789012:identity/example.com",
 "Principal":{
 "AWS":[
 "arn:aws:iam::123456789012:user/John",
 "arn:aws:iam::123456789012:user/Jane"
 ]
 },
 "Action":[
 "ses:DeleteEmailIdentity",
 "ses:PutEmailIdentityDkimSigningAttributes"
 ]
 }
 ]
}`

```

## Restricting the

action

There are multiple actions that can be specified in an identity authorization policy
depending on the level of control you want to authorize:

```
"BatchGetMetricData",
"ListRecommendations",
"CreateDeliverabilityTestReport",
"CreateEmailIdentityPolicy",
"DeleteEmailIdentity",
"DeleteEmailIdentityPolicy",
"GetDomainStatisticsReport",
"GetEmailIdentity",
"GetEmailIdentityPolicies",
"PutEmailIdentityConfigurationSetAttributes",
"PutEmailIdentityDkimAttributes",
"PutEmailIdentityDkimSigningAttributes",
"PutEmailIdentityFeedbackAttributes",
"PutEmailIdentityMailFromAttributes",
"TagResource",
"UntagResource",
"UpdateEmailIdentityPolicy"
```

Identity authorization policies also enable you to restrict the principal to just one of
those actions.

JSON

```
`{
 "Id": "ExamplePolicy",
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ControlAction",
 "Effect": "Allow",
 "Resource": "arn:aws:ses:us-east-1:123456789012:identity/example.com",
 "Principal": {
 "AWS": [
 "123456789012"
 ]
 },
 "Action": [
 "ses:PutEmailIdentityMailFromAttributes"
 ]
 }
 ]
}`

```

## Using multiple

statements

Your identity authorization policy can include multiple statements. The following example
policy has two statements. The first statement denies two users to access
`getemailidentity` from *sender@example.com* within the same
account `123456789012`. The second statement denies
`UpdateEmailIdentityPolicy` for the principal, _Jack_, within
the same account `123456789012`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Sid":"DenyGet",
 "Effect":"Deny",
 "Resource":"arn:aws:ses:us-east-1:123456789012:identity/sender@example.com",
 "Principal":{
 "AWS":[
 "arn:aws:iam::123456789012:user/John",
 "arn:aws:iam::123456789012:user/Jane"
 ]
 },
 "Action":[
 "ses:GetEmailIdentity"
 ]
 },
 {
 "Sid":"DenyUpdate",
 "Effect":"Deny",
 "Resource":"arn:aws:ses:us-east-1:123456789012:identity/sender@example.com",
 "Principal":{
 "AWS":"arn:aws:iam::123456789012:user/Jack"
 },
 "Action":[
 "ses:UpdateEmailIdentityPolicy"
 ]
 }
 ]
}`

```

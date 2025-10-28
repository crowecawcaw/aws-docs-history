# Example SCPs for Amazon Bedrock

###### Topics

- [Deny access to specific Amazon Bedrock models](#example-bedrock-1 "#example-bedrock-1")
- [Restrict access to specific Amazon Bedrock models or model families
  across an entire organization](#example-bedrock-2 "#example-bedrock-2")
- [Restrict creation and use of Amazon Bedrock API keys](#example-bedrock-3 "#example-bedrock-3")
- [Restrict creation of long-term Amazon Bedrock API keys valid beyond
  30 days](#example-bedrock-4 "#example-bedrock-4")

## Deny access to specific Amazon Bedrock models

The following service control policy (SCP) blocks access to specific Amazon Bedrock models or model
families across an entire organization. This policy is useful when you want to prevent the use
of certain models that may not meet your organization's compliance, cost, or security
requirements.

The policy denies all Amazon Bedrock actions for the specified foundation model. In this example,
the policy blocks access to Deepseek models. The wildcard (`.*`) in the resource
ARN matches all versions and variants of the specified model family. You can add additional
model ARNs to the `Resource` array to block access to other models as
needed.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "DenyModelAccessEverywhere",
 "Effect": "Deny",
 "Action": "bedrock:*",
 "Resource": [
 "arn:aws:bedrock:*:*:foundation-model/`deepseek.*`"
 ]
 }
 ]
}`

```

## Restrict access to specific Amazon Bedrock models or model families

across an entire organization

The following service control policy (SCP) restricts users and roles from accessing
unapproved Amazon Bedrock foundation models. This policy denies access to all Amazon Bedrock models except those
you explicitly specify in the `NotResource` element.

To use this policy, replace `<model-unique-identifier>` with the specific
models you want to allow. For example, use `amazon.*` to allow all Amazon
foundation models, or specify individual model IDs like
`amazon.titan-text-premier-v1:0` for more granular control. You can add multiple
model ARNs to the `NotResource` array to allow access to several approved
models.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "PermittedModels",
 "Effect": "Deny",
 "Action": "bedrock:*",
 "NotResource": [
 "arn:aws:bedrock:*:*:foundation-model/`<model-unique-identifier>`"
 ]
 }
 ]
}`

```

## Restrict creation and use of Amazon Bedrock API keys

The following service control policy (SCP) restricts users from creating and using Amazon Bedrock
service-specific credentials API keys. Service-specific credentials API keys provide
programmatic access to Amazon Bedrock outside of standard IAM role-based authentication, which can
create security risks if not properly managed. This policy blocks both the creation of new
service-specific credentials API keys and the use of existing ones.

The policy works by denying two actions: `iam:CreateServiceSpecificCredential`
prevents users from generating new Amazon Bedrock service-specific credentials API keys, while
`bedrock:CallWithBearerToken` prevents the use of bearer tokens (service-specific
credentials API keys) to authenticate Amazon Bedrock API calls.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "iam:CreateServiceSpecificCredential",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:ServiceSpecificCredentialServiceName": "bedrock.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Deny",
 "Action": "bedrock:CallWithBearerToken",
 "Resource": "*"
 }
 ]
}`

```

## Restrict creation of long-term Amazon Bedrock API keys valid beyond

30 days

The following service control policy (SCP) restricts users from creating long-term Amazon Bedrock
service-specific credentials API keys that are valid for more than 30 days. By limiting
service-specific credentials API keys to 30 days or less, you reduce this risk and encourage
regular credential rotation.

The policy denies the creation of Amazon Bedrock service-specific credentials when the requested
validity period exceeds 30 days. The `iam:ServiceSpecificCredentialAgeDays`
condition key checks the requested expiration time during credential creation. You can adjust
the 30-day limit to match your organization's security requirements by changing the value in
the `NumericGreaterThanEquals` condition.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "iam:CreateServiceSpecificCredential",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:ServiceSpecificCredentialServiceName": "bedrock.amazonaws.com"
 },
 "NumericGreaterThanEquals": {
 "iam:ServiceSpecificCredentialAgeDays": "`30`"
 }
 }
 }
 ]
}`

```

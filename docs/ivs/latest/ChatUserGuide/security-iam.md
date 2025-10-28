# Identity and Access Management in IVS Chat

AWS Identity and Access Management (IAM) is an AWS service that helps an account
administrator securely control access to AWS resources. See
[Identity and Access Management in IVS](../LowLatencyUserGuide/security-iam.md "../LowLatencyUserGuide/security-iam.md") in the
_IVS Low-Latency Streaming User Guide_.

## Audience

How you use IAM differs, depending on the work you do in Amazon IVS. See
[Audience](../LowLatencyUserGuide/security-iam.md#security-iam-audience "../LowLatencyUserGuide/security-iam.md#security-iam-audience") in the
_IVS Low-Latency Streaming User Guide_.

## How Amazon IVS Works with IAM

Before you can make Amazon IVS API requests, you must create one or more IAM
_identities_ (users, groups, and roles) and IAM
_policies_, then attach policies to identities.
It takes up to a few minutes for the permissions to propagate; until then, API
requests are rejected.

For a high-level view of how Amazon IVS works with IAM, see [AWS
Services That Work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User
Guide_.

## Identities

You can create IAM identities to provide authentication for people and processes
in your AWS account. IAM groups are collections of IAM users that you can manage
as a unit. See [Identities
(Users, Groups, and Roles)](../../../IAM/latest/UserGuide/id.md "../../../IAM/latest/UserGuide/id.md") in the _IAM User
Guide_.

## Policies

Policies are JSON permissions-policy documents made up of _elements_. See
[Policies](../LowLatencyUserGuide/security-iam.md#security-iam-policies "../LowLatencyUserGuide/security-iam.md#security-iam-policies") in the
_IVS Low-Latency Streaming User Guide_.

Amazon IVS Chat supports three elements:

- **Actions** — Policy actions for Amazon IVS Chat
  use the `ivschat` prefix before the action. For example, to grant
  someone permission to create an Amazon IVS Chat room with the Amazon IVS Chat
  `CreateRoom` API method, you include the
  `ivschat:CreateRoom` action in the policy for that person.
  Policy statements must include either an `Action` or
  `NotAction` element.
- **Resources** — The Amazon IVS Chat room
  resource has the following [ARN](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") format:

```
arn:aws:ivschat:${Region}:${Account}:room/${roomId}
```

For example, to specify the `VgNkEJgOVX9N` room in your
statement, use this ARN:

```
"Resource": "arn:aws:ivschat:us-west-2:123456789012:room/VgNkEJgOVX9N"
```

Some Amazon IVS Chat actions, such as those for creating resources, cannot be
performed on a specific resource. In those cases, you must use the wildcard
(`*`):

```
"Resource":"*"
```

- **Conditions** — Amazon IVS Chat supports some
  global condition keys: `aws:RequestTag`,
  `aws:TagKeys`, and `aws:ResourceTag`.

You can use variables as placeholders in a policy. For example, you can grant an
IAM user permission to access a resource only if it is tagged with the user’s IAM
username. See [Variables and Tags](../../../IAM/latest/UserGuide/reference_policies_variables.md "../../../IAM/latest/UserGuide/reference_policies_variables.md") in the _IAM User
Guide_.

Amazon IVS provides AWS managed policies that can be used to grant a preconfigured
set of permissions to identities (read only or full access). You can choose to use managed
policies instead of the identity-based policies shown below. For details,
see [Managed Policies for Amazon IVS Chat](../LowLatencyUserGuide/security-iam-awsmanpol.md "../LowLatencyUserGuide/security-iam-awsmanpol.md").

## Authorization Based on Amazon IVS

Tags

You can attach tags to Amazon IVS Chat resources or pass tags in a request to Amazon
IVS Chat. To control access based on tags, you provide tag information in the condition
element of a policy using the `aws:ResourceTag/key-name`,
`aws:RequestTag/key-name`, or `aws:TagKeys` condition
keys. For more information about tagging Amazon IVS Chat resources, see “Tagging” in the
[IVS Chat API Reference](../ChatAPIReference/Welcome.md "../ChatAPIReference/Welcome.md").

## Roles

See [IAM
Roles](../../../IAM/latest/UserGuide/id_roles.md "../../../IAM/latest/UserGuide/id_roles.md") and [Temporary
Security Credentials](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md") in the _IAM User
Guide_.

An IAM _role_ is an entity within your AWS
account that has specific permissions.

Amazon IVS supports using _temporary security
credentials_. You can use temporary credentials to sign in with
federation, assume an IAM role, or assume a cross-account role. You obtain temporary
security credentials by calling [AWS Security Token
Service](../../../STS/latest/APIReference/welcome.md "../../../STS/latest/APIReference/welcome.md") API operations such as `AssumeRole` or
`GetFederationToken`.

## Privileged and Unprivileged

Access

API resources have privileged access. Unprivileged playback access can be set up
through private channels; see [Setting Up IVS Private Channels](../LowLatencyUserGuide/private-channels.md "../LowLatencyUserGuide/private-channels.md").

## Best Practices for

Policies

See [IAM Best
Practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User
Guide_.

Identity-based policies are very powerful. They determine whether someone can
create, access, or delete Amazon IVS resources in your account. These actions can
incur costs for your AWS account. Follow these recommendations:

- **Grant least privilege** — When you create
  custom policies, grant only the permissions required to perform a task.
  Start with a minimum set of permissions and grant more permissions as
  needed. Doing so is more secure than starting with permissions that are too
  lenient, then trying to tighten them later. Specifically, reserve
  `ivschat:*` for admin access; do not use it in
  applications.
- **Enable multi-factor authentication (MFA) for
  sensitive operations** — For extra security, require IAM users
  to use MFA to access sensitive resources or API operations.
- **Use policy conditions for extra security**
  — To the extent practical, define the conditions under which your
  identity-based policies allow access to a resource. For example, you can
  write conditions to specify a range of allowable IP addresses from which a
  request must come. You also can write conditions to allow requests only
  within a specified date or time range, or to require the use of SSL or
  MFA.

## Identity-Based Policy

Examples

### Use the Amazon IVS

Console

To access the Amazon IVS console, you must have a minimum set of permissions
which allow you to list and view details about the Amazon IVS Chat resources in your
AWS account. If you create an identity-based policy that is more restrictive
than the minimum required permissions, the console will not function as intended
for identities with that policy. To ensure access to the Amazon IVS console,
attach the following policy to the identities (see [Adding and Removing IAM Permissions](../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md "../../../IAM/latest/UserGuide/access_policies_manage-attach-detach.md") in the _IAM User Guide_).

The parts of the following policy provide access to:

- All Amazon IVS Chat API
  operations
- Your Amazon IVS Chat [service quotas](service-quotas.md "service-quotas.md")
- Listing lambdas and adding permissions for the chosen lambda for
  Amazon IVS Chat moderation
- Amazon Cloudwatch to get metrics for your chat session

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": "ivschat:*",
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "servicequotas:ListServiceQuotas"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "cloudwatch:GetMetricData"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "lambda:AddPermission",
 "lambda:ListFunctions"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Resource-Based Policy for Amazon IVS

Chat

You must give the Amazon IVS Chat service permission to invoke your lambda
resource to review messages. To do that, follow the instructions in [Using resource-based policies for AWS Lambda](../../../lambda/latest/dg/access-control-resource-based.md "../../../lambda/latest/dg/access-control-resource-based.md") (in the _AWS Lambda Developer Guide_) and fill out the fields
as specified below.

To control access to your lambda resource, you can use conditions based on:

- `SourceArn` — Our sample policy uses a wildcard (
  `*` ) to allow all rooms in your account to invoke the
  lambda. Optionally, you can specify a room in your account to allow only
  that room to invoke the lambda.
- `SourceAccount` — In the sample policy below, the AWS account
  ID is `123456789012`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Principal": {
 "Service": "ivschat.amazonaws.com"
 },
 "Action": [
 "lambda:InvokeFunction"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:lambda:us-west-2:123456789012:function:name",
 "Condition": {
 "StringEquals": {
 "AWS:SourceAccount": "123456789012"
 },
 "ArnLike": {
 "AWS:SourceArn": "arn:aws:ivschat:us-west-2:123456789012:room/*"
 }
 }
 }
 ]
}`

```

## Troubleshooting

See [Troubleshooting](../LowLatencyUserGuide/security-iam.md#security-iam-troubleshooting "../LowLatencyUserGuide/security-iam.md#security-iam-troubleshooting") in the _IVS Low-Latency Streaming User Guide_
for information about diagnosing and fixing common issues that you might encounter when working
with Amazon IVS Chat and IAM.

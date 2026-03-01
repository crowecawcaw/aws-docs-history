# AWS managed policies for AWS AppSync

To add permissions to users, groups, and roles, it is easier to use AWS managed
policies than to write policies yourself. It takes time and expertise to [create IAM customer managed policies](../../../IAM/latest/UserGuide/access_policies_create-console.md "../../../IAM/latest/UserGuide/access_policies_create-console.md") that provide your team with only the
permissions that they need. To get started quickly, you can use our AWS managed
policies. These policies cover common use cases and are available in your AWS account.
For more information about AWS managed policies, see [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") in the _IAM User Guide_.

AWS services maintain and update AWS managed policies. You can't change the
permissions in AWS managed policies. Services occasionally add additional permissions
to an AWS managed policy to support new features. This type of update affects all
identities (users, groups, and roles) where the policy is attached. Services are most
likely to update an AWS managed policy when a new feature is launched or when new
operations become available. Services do not remove permissions from an AWS managed
policy, so policy updates won't break your existing permissions.

Additionally, AWS supports managed policies for job functions that span multiple
services. For example, the **ReadOnlyAccess** AWS managed
policy provides read-only access to all AWS services and resources. When a service
launches a new feature, AWS adds read-only permissions for new operations and
resources. For a list and descriptions of job function policies, see [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the
_IAM User Guide_.

## AWS managed policy: AWSAppSyncInvokeFullAccess

Use the `AWSAppSyncInvokeFullAccess` AWS managed policy to allow your
administrators to access the AWS AppSync service through the console or
independently.

You can attach the `AWSAppSyncInvokeFullAccess` policy to your IAM
identities.

### Permissions details

This policy includes the following permissions.

- `AWS AppSync` – Allows full administrative access to all
  resources in AWS AppSync

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "appsync:GraphQL",
 "appsync:GetGraphqlApi",
 "appsync:ListGraphqlApis",
 "appsync:ListApiKeys"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSAppSyncSchemaAuthor

Use the `AWSAppSyncSchemaAuthor` AWS managed policy to allow IAM
users to access to create, update, and query their GraphQL
schemas. For
information about what users can do with these permissions, see [Designing GraphQL APIs with AWS AppSync](designing-a-graphql-api.md "designing-a-graphql-api.md").

You can attach the `AWSAppSyncSchemaAuthor` policy to your IAM
identities.

### Permissions details

This policy includes the following permissions.

- `AWS AppSync` – Allows the following actions:
  - Creating GraphQL schemas
  - Allowing the creation, modification, and deletion of GraphQL
    types, resolvers,
    and functions
  - Evaluating request and response template logic
  - Evaluating code with a runtime and context
  - Sending GraphQL queries to GraphQL APIs
  - Retrieving GraphQL data

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "appsync:GraphQL",
 "appsync:CreateResolver",
 "appsync:CreateType",
 "appsync:DeleteResolver",
 "appsync:DeleteType",
 "appsync:GetResolver",
 "appsync:GetType",
 "appsync:GetDataSource",
 "appsync:GetSchemaCreationStatus",
 "appsync:GetIntrospectionSchema",
 "appsync:GetGraphqlApi",
 "appsync:ListTypes",
 "appsync:ListApiKeys",
 "appsync:ListResolvers",
 "appsync:ListDataSources",
 "appsync:ListGraphqlApis",
 "appsync:StartSchemaCreation",
 "appsync:UpdateResolver",
 "appsync:UpdateType",
 "appsync:TagResource",
 "appsync:UntagResource",
 "appsync:ListTagsForResource",
 "appsync:CreateFunction",
 "appsync:UpdateFunction",
 "appsync:GetFunction",
 "appsync:DeleteFunction",
 "appsync:ListFunctions",
 "appsync:ListResolversByFunction",
 "appsync:EvaluateMappingTemplate",
 "appsync:EvaluateCode"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSAppSyncPushToCloudWatchLogs

AWS AppSync uses Amazon CloudWatch
to
monitor the performance of your application by generating logs that
you
can
use
to troubleshoot and optimize your GraphQL requests. For more information, see
[Using CloudWatch to monitor and log GraphQL API data](monitoring.md "monitoring.md").

Use the `AWSAppSyncPushToCloudWatchLogs` AWS managed policy to allow
AWS AppSync to push logs to
an
IAM user's CloudWatch account.

You can attach the `AWSAppSyncPushToCloudWatchLogs` policy to your
IAM identities.

### Permissions details

This policy includes the following permissions.

- `CloudWatch Logs`
  – Allows AWS AppSync to create log groups and streams with
  specified names. AWS AppSync
  pushes
  log events to the specified log stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogGroup",
 "logs:CreateLogStream",
 "logs:PutLogEvents"
 ],
 "Resource": "*"
 }
 ]
}`

```

## AWS managed policy: AWSAppSyncAdministrator

Use the `AWSAppSyncAdministrator` AWS managed policy to allow your
administrators to access
all
of AWS AppSync
except
for the AWS console.

You can attach `AWSAppSyncAdministrator` to your IAM entities.
AWS AppSync also attaches this policy to a service role that allows it to perform
actions on your
behalf.

### Permissions details

This policy includes the following permissions.

- `AWS AppSync`
  – Allows full administrative access to all resources in
  AWS AppSync
- `IAM`
  – Allows the following actions:
  - Creating service-linked roles to allow AWS AppSync to analyze
    resources in other services on your behalf
  - Deleting service-linked roles
  - Passing service-linked roles on to other AWS services to assume
    the role later and
    to
    perform actions on your behalf

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "appsync:*"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "appsync.amazonaws.com"
 ]
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "*",
 "Condition": {
 "StringEquals": {
 "iam:AWSServiceName": "appsync.amazonaws.com"
 }
 }
 },
 {
 "Effect": "Allow",
 "Action": [
 "iam:DeleteServiceLinkedRole",
 "iam:GetServiceLinkedRoleDeletionStatus"
 ],
 "Resource": "arn:aws:iam::*:role/aws-service-role/appsync.amazonaws.com/AWSServiceRoleForAppSync*"
 }
 ]
}`

```

## AWS managed policy: AWSAppSyncServiceRolePolicy

Use the `AWSAppSyncServiceRolePolicy` AWS managed policy to
allow
access to AWS services and resources
that
AWS AppSync
uses
or
manages.

You can't attach `AWSAppSyncServiceRolePolicy` to your IAM entities.
This policy is attached to a service-linked role that allows AWS AppSync to perform
actions on your behalf. For more information, see
[Service-linked roles for AWS AppSync](security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked "security_iam_service-with-iam.md#security_iam_service-with-iam-roles-service-linked").

### Permissions details

This policy includes the following permissions.

- `X-Ray`
  – AWS AppSync uses AWS X-Ray to collect data about requests
  made
  within your application. For more information, see
  [Using AWS X-Ray to trace requests in AWS AppSync](x-ray-tracing.md "x-ray-tracing.md").

This policy allows the following actions:

    + Retrieving sampling rules and their results
    + Sending trace data to the
     X-Ray
     daemon

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "xray:PutTraceSegments",
 "xray:PutTelemetryRecords",
 "xray:GetSamplingTargets",
 "xray:GetSamplingRules",
 "xray:GetSamplingStatisticSummaries"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

## AWS AppSync updates to AWS managed policies

View details about updates to AWS managed policies for AWS AppSync since this
service began tracking these changes. For automatic alerts about changes to this
page, subscribe to the RSS feed on the AWS AppSync Document history page.

| Change                                                                                                                                                      | Description                                                                                                                                                                                                                                                                                 | Date             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| [AWSAppSyncSchemaAuthor](#security-iam-awsmanpol-AWSAppSyncSchemaAuthor "#security-iam-awsmanpol-AWSAppSyncSchemaAuthor")<br>• Update to an existing policy | Added an `EvaluateCode` policy action to allow users to evaluate code with a<br>runtime and context.                                                                                                                                                                                        | February 7, 2023 |
| [AWSAppSyncSchemaAuthor](#security-iam-awsmanpol-AWSAppSyncSchemaAuthor "#security-iam-awsmanpol-AWSAppSyncSchemaAuthor")<br>• Update to an existing policy | Added policy actions to allow the list, get, create, update, and delete functions for<br>an API.<br>Added an `EvaluateMappingTemplate` policy action to allow users to evaluate<br>request and response resolver mapping template logic.<br>Added policy actions to allow resource tagging. | August 25, 2022  |
| AWS AppSync started tracking changes                                                                                                                        | AWS AppSync started tracking changes for its AWS managed policies.                                                                                                                                                                                                                          | August 25, 2022  |

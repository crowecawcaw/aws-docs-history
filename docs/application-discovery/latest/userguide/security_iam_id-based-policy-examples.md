AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# AWS Application Discovery Service identity-based

policy examples

By default, IAM users and roles don't have permission to create or modify
Application Discovery Service resources. They also can't perform tasks using the AWS Management Console, AWS CLI, or
AWS API. An IAM administrator must create IAM policies that grant users and roles
permission to perform specific API operations on the specified resources they need. The
administrator must then attach those policies to the IAM users or groups that require
those permissions.

To learn how to create an IAM identity-based policy using these example JSON policy
documents, see [Creating Policies on the JSON Tab](../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor "../../../IAM/latest/UserGuide/access_policies_create.md#access_policies_create-json-editor") in the
_IAM User Guide_.

###### Topics

- [Policy best
  practices](#security_iam_service-with-iam-policy-best-practices "#security_iam_service-with-iam-policy-best-practices")
- [Granting full
  access to Application Discovery Service](#security_iam_id-based-policy-examples-ads-fullaccess "#security_iam_id-based-policy-examples-ads-fullaccess")
- [Granting access
  to discovery agents](#security_iam_id-based-policy-examples-ads-agentaccess "#security_iam_id-based-policy-examples-ads-agentaccess")
- [Granting
  permissions for agent data collection](#security_iam_id-based-policy-examples-ads-export-service "#security_iam_id-based-policy-examples-ads-export-service")
- [Granting
  permissions for data exploration](#security_iam_id-based-policy-examples-ads-export-firehose "#security_iam_id-based-policy-examples-ads-export-firehose")
- [Granting permissions to use the Migration Hub console network diagram](#security_iam_id-based-policy-examples-network-connection-graph "#security_iam_id-based-policy-examples-network-connection-graph")

## Policy best

practices

Identity-based policies determine whether someone can create, access, or delete Application Discovery Service resources in your
account. These actions can incur costs for your AWS account. When you create or edit identity-based policies, follow these guidelines and
recommendations:

- **Get started with AWS managed policies and move toward least-privilege permissions**
  – To get started granting permissions to your users and workloads, use the _AWS
  managed policies_ that grant permissions for many common use cases. They are
  available in your AWS account. We recommend that you reduce permissions further by
  defining AWS customer managed policies that are specific to your use cases. For more information, see
  [AWS managed policies](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#aws-managed-policies") or [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md") in the _IAM User Guide_.
- **Apply least-privilege permissions** –
  When you set permissions with IAM policies, grant only the permissions required to
  perform a task. You do this by defining the actions that can be taken on specific resources
  under specific conditions, also known as _least-privilege permissions_.
  For more information about using IAM to apply permissions, see [Policies and permissions in IAM](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md") in the _IAM User Guide_.
- **Use conditions in IAM policies to further restrict access**
  – You can add a condition to your policies to limit access to actions and resources. For example, you can write a policy condition to specify that all requests must
  be sent using SSL. You can also use conditions to grant access to service actions
  if they are used through a specific AWS service, such as AWS CloudFormation. For more information, see
  [IAM JSON policy elements: Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") in the _IAM User Guide_.
- **Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions**
  – IAM Access Analyzer validates new and existing policies so that the policies adhere to the IAM policy language (JSON) and IAM best practices.
  IAM Access Analyzer provides more than 100 policy checks and actionable recommendations to help
  you author secure and functional policies. For more information, see [Validate policies with IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-validation.md") in the _IAM User Guide_.
- **Require multi-factor authentication (MFA)** –
  If you have a scenario that requires IAM users or a root user in your AWS account, turn on MFA for additional security. To require
  MFA when API operations are called, add MFA conditions to your policies. For
  more information, see [Secure API access with MFA](../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md "../../../IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.md") in the _IAM User Guide_.

For more information about best practices in IAM, see [Security best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md") in the _IAM User Guide_.

## Granting full

access to Application Discovery Service

The AWSApplicationDiscoveryServiceFullAccess managed policy grants the IAM user
account access to the Application Discovery Service and Migration Hub APIs.

An IAM user with this policy attached to their account can configure Application Discovery Service,
start and stop agents, start and stop agentless discovery, and query data from the AWS
Discovery Service database. For more information about this policy, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### Example AWSApplicationDiscoveryServiceFullAccess policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "mgh:*",
 "discovery:*"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "iam:GetRole"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

## Granting access

to discovery agents

The AWSApplicationDiscoveryAgentAccess managed policy grants the Application
Discovery Agent access to register and communicate with Application Discovery Service. For more information
about this policy, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

Attach this policy to any user whose credentials are used by Application Discovery
Agent.

This policy also grants the user access to Arsenal. Arsenal is an agent service that
is managed and hosted by AWS. Arsenal forwards data to Application Discovery Service in the cloud.

###### Example AWSApplicationDiscoveryAgentAccess Policy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "arsenal:RegisterOnPremisesAgent"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Granting

permissions for agent data collection

The ApplicationDiscoveryServiceContinuousExportServiceRolePolicy managed policy
allows AWS Application Discovery Service to create Amazon Data Firehose streams to transform and deliver data that's
collected by Application Discovery Service agents to an Amazon S3 bucket in your AWS account.

In addition, this policy creates an AWS Glue Data Catalog with a new database called
`application_discovery_service_database` and table schemas for mapping
data that's collected by the agents.

For information about using this policy, see [AWS managed policies for AWS Application Discovery Service](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

###### Example ApplicationDiscoveryServiceContinuousExportServiceRolePolicy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "glue:CreateDatabase",
 "glue:UpdateDatabase",
 "glue:CreateTable",
 "glue:UpdateTable",
 "firehose:CreateDeliveryStream",
 "firehose:DescribeDeliveryStream",
 "logs:CreateLogGroup"
 ],
 "Effect": "Allow",
 "Resource": "*"
 },
 {
 "Action": [
 "firehose:DeleteDeliveryStream",
 "firehose:PutRecord",
 "firehose:PutRecordBatch",
 "firehose:UpdateDestination"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:firehose:*:*:deliverystream/aws-application-discovery-service*"
 },
 {
 "Action": [
 "s3:CreateBucket",
 "s3:ListBucket",
 "s3:PutBucketLogging",
 "s3:PutEncryptionConfiguration"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::aws-application-discovery-service*"
 },
 {
 "Action": [
 "s3:GetObject"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:s3:::aws-application-discovery-service*/*"
 },
 {
 "Action": [
 "logs:CreateLogStream",
 "logs:PutRetentionPolicy"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:logs:*:*:log-group:/aws/application-discovery-service/firehose*"
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/AWSApplicationDiscoveryServiceFirehose",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "firehose.amazonaws.com"
 }
 }
 },
 {
 "Action": [
 "iam:PassRole"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iam::*:role/service-role/AWSApplicationDiscoveryServiceFirehose",
 "Condition": {
 "StringLike": {
 "iam:PassedToService": "firehose.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Granting

permissions for data exploration

The AWSDiscoveryContinuousExportFirehosePolicy policy is required to use data
exploration in Amazon Athena. It allows Amazon Data Firehose to write data that's collected from
Application Discovery Service to Amazon S3. For information about using this policy, see [Creating the
AWSApplicationDiscoveryServiceFirehose role](security-iam-awsmanpol.md#security-iam-awsmanpol-create-firehose-role "security-iam-awsmanpol.md#security-iam-awsmanpol-create-firehose-role").

###### Example AWSDiscoveryContinuousExportFirehosePolicy

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetTableVersions"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:AbortMultipartUpload",
 "s3:GetBucketLocation",
 "s3:GetObject",
 "s3:ListBucket",
 "s3:ListBucketMultipartUploads",
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::aws-application-discovery-service-*",
 "arn:aws:s3:::aws-application-discovery-service-*/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:*:*:log-group:/aws/application-discovery-service/firehose:log-stream:*"
 ]
 }
 ]
}`

```

## Granting permissions to use the Migration Hub console network diagram

To grant access to the AWS Migration Hub console network diagram when creating an
identity-based policy that allows or denies access to Application Discovery Service or Migration Hub, you
might need to add the `discovery:GetNetworkConnectionGraph` action to the
policy.

You must use the `discovery:GetNetworkConnectionGraph` action in new
policies or update older policies if the following are both true for the policy:

- The policy allows or denies access to Application Discovery Service or the Migration Hub.
- The policy grants access permissions using one more specific discovery actions
  like `discovery:`action-name``rather than`discovery:\*`.

The following example shows how to use the
`discovery:GetNetworkConnectionGraph` action in an IAM policy.

###### Example

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": ["discovery:GetNetworkConnectionGraph"],
 "Resource": "*"
 }
 ]
}`

```

For information about the Migration Hub network diagram, see [Viewing network connections in
Migration Hub](../../../migrationhub/latest/ug/network-diagram.md "../../../migrationhub/latest/ug/network-diagram.md").

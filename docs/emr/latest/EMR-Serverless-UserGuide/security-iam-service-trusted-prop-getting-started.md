# Getting started with Trusted-Identity Propagation for EMR Serverless

This section helps you configure EMR-Serverless application with Apache Livy Endpoint to integrate with AWS IAM Identity Center and
enable [Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").

## Prerequisites

- An Identity Center instance in the AWS Region where you want to create Trusted identity propagation
  enabled EMR Serverless Apache Livy Endpoint. An Identity Center instance can only exist in a single Region for an AWS account. refer [Enable IAM Identity Center](../../../singlesignon/latest/userguide/enable-identity-center.md "../../../singlesignon/latest/userguide/enable-identity-center.md")
  and [Provision the users and groups from your source of identities into IAM Identity Center](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md").
- Enable Trusted identity propagation for downstream services like Lake Formation or S3 Access Grants or Amazon Redshift cluster with which interactive workload interacts
  to access data.

## Required permissions to create trusted-identity propagation

enabled EMR Serverless Application

In addition to the basic [permissions that are required to access EMR Serverless](setting-up.md#setting-up-iam "setting-up.md#setting-up-iam"), you must
configure additional permissions for your IAM identity or role that is used to create trusted-identity propagation enabled EMR Serverless Application. For trusted-identity
propagation, EMR Serverless creates/bootstraps a single service managed Identity Center Application in your account that service leverages for identity validation and
identity propagation to downstream.

```
"sso:DescribeInstance",
"sso:CreateApplication",
"sso:DeleteApplication",
"sso:PutApplicationAuthenticationMethod",
"sso:PutApplicationAssignmentConfiguration",
"sso:PutApplicationGrant",
"sso:PutApplicationAccessScope"
```

- `sso:DescribeInstance` – Grants permission to describe and validate the IAM Identity Center instanceArn
  that you specify in identity-center-configuration parameter.
- `sso:CreateApplication` – Grants permission to create a EMR Serverless managed IAM Identity Center Application
  which is used for trusted-identity-propatgion actions.
- `sso:DeleteApplication` – grants permission to cleanup a EMR Serverless managed
  IAM Identity Center Application
- `sso:PutApplicationAuthenticationMethod` – Grants permission to put authenticationMethod on EMR Serverless managed IAM Identity Center Application that
  allows emr-serverless service principal to interact with IAM Identity Center Application.
- `sso:PutApplicationAssignmentConfiguration` – Grants permission to set "User-assignment-not-required" setting on IAM Identity Center Application.
- `sso:PutApplicationGrant` – Grants permission to apply token-exchange, introspectToken, refreshToken and revokeToken
  grants on an IAM Identity Center Application.
- `sso:PutApplicationAccessScope` – Grants permission to apply trusted-identity propagation enabled downstream scope to IAM Identity Center Application. We
  apply "redshift:connect", "lakeformation:query" and "s3:read_write" scopes to enable trusted-identity-propagation to these services.

## Create a trusted-identity propagation enabled EMR Serverless Application

You must specify `—identity-center-configuration` field with `identityCenterInstanceArn` to enable trusted-identity propagation in
the application. Use the following example command to create an EMR Serverless Application that has trusted-identity propagation enabled.

###### Note

You also must specify `--interactive-configuration '{"livyEndpointEnabled":true}'` as trusted-identity propagation
is enabled for Apache Livy Endpoint only.

```
aws emr-serverless create-application \
  --release-label emr-7.8.0 \
  --type "SPARK" \
  --identity-center-configuration '{"identityCenterInstanceArn" : "arn:aws:sso:::instance/ssoins-123456789"}' \
  --interactive-configuration '{"livyEndpointEnabled":true}'
```

- `identity-center-configuration` – (optional) Enables Identity Center trusted identity propagation if specified.
- `identityCenterInstanceArn` – (required) The Identity Center instance ARN.

In case you don't have the required Identity Center permissions (mentioned previously), first create the EMR Serverless Application without trusted-identity
propagation (for instance, dont specify `—identity-center-configuration` parameter) and later ask your Identity Center Admin to enable the trusted-identity propagation
by invoking update-application API, see example below:

```
aws emr-serverless update-application \
  --application-id `applicationId` \
  --identity-center-configuration '{"identityCenterInstanceArn" : "arn:aws:sso:::instance/ssoins-123456789"}'
```

EMR Serverless creates a service managed Identity Center Application in your account that service leverages for identity validations and identity
propagation to downstream services. EMR Serverless created managed Identity Center Application is shared across all trusted-identity-propagation enabled EMR Serverless
applications in your account.

###### Note

Do not manually modify settings on the managed Identity Center Application. Any changes could affect all trusted-identity-propagation enabled EMR Serverless applications in your account.

## Job Execution Role permissions to propagate identity

As EMR-Serverless leverage Identity-enhanced job-execution-role credentials to propagate identity to downstream AWS services, Job Execution Role's trust-policy
must have additional permission `sts:SetContext` to enhance job execution-role credential with identity to allow trusted-identity-propagation to downstream service, such as S3 access-grant, Lake Formation, or Amazon Redshift. To
learn more about how to create a role, refer to [Create a job runtime role](getting-started.md#gs-runtime-role "getting-started.md#gs-runtime-role").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "emr-serverless.amazonaws.com"
 },
 "Action": [ "sts:AssumeRole", "sts:SetContext"]
 }
 ]
}`

```

Additionally, JobExecutionRole needs permissions for downstream AWS services which job-run would invoke to fetch data using user identity. Please refer below
links to configure S3 Access Grant, Lake Formation.

- [Using Lake Formation with EMR Serverless](lake-formation-section.md "lake-formation-section.md")
- [Using Amazon S3 Access Grants with EMR Serverless](access-grants.md "access-grants.md")

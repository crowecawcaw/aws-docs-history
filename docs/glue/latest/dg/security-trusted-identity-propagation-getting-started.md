# Getting started with trusted identity propagation in AWS Glue ETL

This section helps you configure AWS Glue application with interactive sessions to integrate with IAM Identity Center and enable
[Trusted identity propagation](../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-overview.md").

## Prerequisites

- An Identity Center instance in the AWS region where you want to create Trusted identity propagation enabled AWS Glue
  interactive sessions. An Identity Center instance can only exist in a single region for an AWS account. For more information, see
  [Enable IAM Identity Center](../../../singlesignon/latest/userguide/get-started-enable-identity-center.md "../../../singlesignon/latest/userguide/get-started-enable-identity-center.md") and
  [provision the users and groups from your source of identities into IAM Identity Center](../../../singlesignon/latest/userguide/tutorials.md "../../../singlesignon/latest/userguide/tutorials.md") .
- Enable Trusted identity propagation for downstream services such as Lake Formation or Amazon S3 Access Grants or Amazon Redshift
  cluster with which interactive workload interacts to access data.

## Permissions needed to connect AWS Glue ETL with IAM Identity Center

###### Create an IAM role

The role that creates IAM Identity Center connection requires permissions to create and modify application configuration in
AWS Glue and IAM Identity Center as in the following inline policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:CreateGlueIdentityCenterConfiguration",
 "sso:CreateApplication",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant",
 "sso:PutApplicationAccessScope",
 "sso:ListInstances"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

The following inline policies contain specific permissions required to view, update, and delete properties of AWS Glue
integration with IAM Identity Center.

Use the following inline policy to allow an IAM role to view a AWS Glue integration with IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:GetGlueIdentityCenterConfiguration"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

Use the following inline policy to allow an IAM role to update AWS Glue integration with IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:UpdateGlueIdentityCenterConfiguration",
 "sso:PutApplicationAccessScope",
 "sso:DeleteApplicationAccessScope"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

Use the following inline policy to allow an IAM role to delete a AWS Glue integration with IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "glue:DeleteGlueIdentityCenterConfiguration",
 "sso:DeleteApplication"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

### Permissions description

- `glue:CreateGlueIdentityCenterConfiguration` – Grants permission to create the AWS Glue IdC configuration.
- `glue:GetGlueIdentityCenterConfiguration` – Grants permission to get an existing IdC configuration.
- `glue:DeleteGlueIdentityCenterConfiguration` – Grants permission to delete an existing AWS Glue IdC configuration.
- `glue:UpdateGlueIdentityCenterConfiguration` – Grants permission to update an existing AWS Glue IdC configuration.
- `sso:CreateApplication` – Grants permission to create a AWS Glue managed IAM Identity Center application.
- `sso:DescribeApplication` - Grants permission to describe a AWS Glue managed IAM Identity Center application.
- `sso:DeleteApplication` – Grants permission to delete a AWS Glue managed IAM Identity Center application.
- `sso:UpdateApplication` – Grants permission to update a AWS Glue managed IAM Identity Center application.
- `sso:PutApplicationGrant` – Grants permission to apply token-exchange, introspectToken, refreshToken and RevokeToken grants on IdC Application.
- `sso:PutApplicationAuthenticationMethod` – Grants permission to put authenticationMethod on AWS Glue managed IdC Application that allows AWS Glue service principal to interact with IdC Application.
- `sso:PutApplicationAccessScope` – Grants permission to add or update the list of authorized down stream service scopes on the AWS Glue managed IdC application.
- `sso:DeleteApplicationAccessScope` - Grants permission to delete downstream scopes if a scope is removed for the AWS Glue managed IdC application.
- `sso:PutApplicationAssignmentConfiguration` – Grants permission to set "User-assignment-not-required" setting on IdC Application.
- `sso:ListInstances` – Grants permission to list instances and validate the IdC InstanceArn that you specify in identity-center-configuration parameter.

## Connecting AWS Glue with IAM Identity Center

When AWS Glue is connected to IAM Identity Center, it creates a singleton managed IdC application per account. The following example shows how you can connect AWS Glue with IAM Identity Center:

```
aws glue create-glue-identity-center-configuration \
--instance-arn arn:aws:sso:::instance/ssoins-123456789 \
--scopes '["s3:access_grants:read_write", "redshift:connect","lakeformation:query"]'
```

To update the scopes of the managed application (usually done to propagate to more downstream services), you can use:

```
aws glue update-glue-identity-center-configuration \
--scopes '["s3:access_grants:read_write", "redshift:connect","lakeformation:query"]'
```

Scopes parameter is optional and all scopes will be added if not provided. The supported values are `s3:access_grants:read_write`, `redshift:connect` and `lakeformation:query`.

To get the details of the configuration, you can use:

```
aws glue get-glue-identity-center-configuration
```

You can delete the connection between AWS Glue and IAM Identity Center by using the following command:

```
aws glue delete-glue-identity-center-configuration
```

###### Note

AWS Glue creates a service managed Identity Center Application in your account that service leverages for identity validations and
identity propagation to downstream services. AWS Glue created managed Identity Center Application is shared across all
trusted-identity-propagation sessions in your account.

**Warning:** Do not manually modify settings on the managed Identity Center Application.
Any changes could affect all trusted-identity-propagation enabled AWS Glue interactive sessions in your account.

## Creating a AWS Glue Interactive Session with Trusted

Identity Propagation Enabled

After you connect AWS Glue with IAM Identity Center, you can use
[identity-enhanced role credentials](../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md")
to create a AWS Glue interactive session. You need not pass additional parameters when creating a 5.0 AWS Glue session. Since AWS Glue is
connected with IAM identity center, if AWS Glue detects identity-enhanced-role-credentials, it will automatically propagate the
identity information to downstream services which are called as part of your statements. However, the runtime role for the session needs
to have the `sts:SetContext` permission as depicted below.

###### Runtime Role permissions to propagate identity

As AWS Glue sessions leverage
[Identity-enhanced credentials](../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md "../../../singlesignon/latest/userguide/trustedidentitypropagation-identity-enhanced-iam-role-sessions.md")  
 to propagate identity to downstream AWS services, its runtime role's trust-policy need to have addition permission
`sts:SetContext` to allow identity propagation to downstream services (Amazon S3 access-grant, Lake Formation, Amazon Redshift). To learn more about how to
create a runtime role, see
[Setting up a runtime role](create-service-role.md "create-service-role.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "glue.amazonaws.com"
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext"
 ]
 }
 ]
}`

```

Additionally, Runtime role would need permissions for downstream AWS services which job-run would invoke to fetch data using user identity. Please refer to the following links to configure Amazon S3 Access Grants and Lake Formation:

- [Using Lake Formation with AWS Glue](security-lake-formation-fgac.md "security-lake-formation-fgac.md")
- [Using Amazon S3 Access Grants with AWS Glue](security-s3-access-grants.md "security-s3-access-grants.md")

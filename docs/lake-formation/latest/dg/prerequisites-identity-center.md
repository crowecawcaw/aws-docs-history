# Prerequisites for IAM Identity Center integration with Lake Formation

The following are the prerequisites for integrating IAM Identity Center with Lake Formation.

1. Enable IAM Identity Center – Enabling IAM Identity Center is a prerequisite to support authentication and identity propagation.
2. Choose your identity source – After you enable IAM Identity Center, you must have an
   identify provider to manage users and groups. You can either use the built-in
   Identity Center directory as an identity source or use external IdP, such as
   Microsoft Entra ID or Okta.

For more information, see [Manage your identity source](../../../singlesignon/latest/userguide/manage-your-identity-source.md "../../../singlesignon/latest/userguide/manage-your-identity-source.md") and
[Connect to an external identity provider](../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md "../../../singlesignon/latest/userguide/manage-your-identity-source-idp.md") in the AWS IAM Identity Center User Guide. 3. Create an IAM role – The role that creates IAM Identity Center connection requires
permissions to create and modify application configuration in Lake Formation and IAM Identity Center as
in the following inline policy.

You need to add permissions per IAM best practices. Specific permissions are detailed in the procedures that follow.

For more information, see [Getting started with IAM Identity Center](../../../singlesignon/latest/userguide/get-started-enable-identity-center.md "../../../singlesignon/latest/userguide/get-started-enable-identity-center.md").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:CreateLakeFormationIdentityCenterConfiguration",
 "sso:CreateApplication",
 "sso:PutApplicationAssignmentConfiguration",
 "sso:PutApplicationAuthenticationMethod",
 "sso:PutApplicationGrant",
 "sso:PutApplicationAccessScope"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

If you're sharing Data Catalog resources with external AWS accounts or organizations,
you must have the AWS Resource Access Manager (AWS RAM) permissions for creating resource shares.
For more information about the permissions required to share resources, see
[Cross-account data sharing
prerequisites](cross-account-prereqs.md "cross-account-prereqs.md").

The following inline policies contain specific permissions required to view, update, and delete properties of Lake Formation integration with IAM Identity Center.

- Use the following inline policy to allow an IAM role to view a Lake Formation integration with IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:DescribeLakeFormationIdentityCenterConfiguration",
 "sso:DescribeApplication"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

- Use the following inline policy to allow an IAM role to update a Lake Formation integration with
  IAM Identity Center. The policy also includes optional permissions required to share resources with external accounts.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:UpdateLakeFormationIdentityCenterConfiguration",
 "lakeformation:DescribeLakeFormationIdentityCenterConfiguration",
 "sso:DescribeApplication",
 "sso:UpdateApplication"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

- Use the following inline policy to allow an IAM role to delete a Lake Formation integration
  with IAM Identity Center.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "lakeformation:DeleteLakeFormationIdentityCenterConfiguration",
 "sso:DeleteApplication"
 ],
 "Resource": [
 "*"
 ]
 }
 ]
}`

```

- For IAM permissions required to grant or revoke data lake permissions for
  IAM Identity Center users and groups, see [IAM permissions required to grant or
  revoke Lake Formation permissions](required-permissions-for-grant.md "required-permissions-for-grant.md").
  _Permissions description_

- `lakeformation:CreateLakeFormationIdentityCenterConfiguration`
  – Creates the Lake Formation IdC configuration.
- `lakeformation:DescribeLakeFormationIdentityCenterConfiguration`
  – Describes an existing IdC configuration.
- `lakeformation:DeleteLakeFormationIdentityCenterConfiguration` – Gives the ability to delete an existing Lake Formation IdC configuration.
- `lakeformation:UpdateLakeFormationIdentityCenterConfiguration`
  – Used to change an existing Lake Formation configuration.
- `sso:CreateApplication` – Used to create an IAM Identity Center application.
- `sso:DeleteApplication` – Used to delete an IAM Identity Center application.
- `sso:UpdateApplication` – Used to update an IAM Identity Center application.
- `sso:PutApplicationGrant` – Used to change the trusted token issuer information.
- `sso:PutApplicationAuthenticationMethod` – Grants Lake Formation authentication access.
- `sso:GetApplicationGrant` – Used to list trusted token issuer information.
- `sso:DeleteApplicationGrant` – Deletes the trust token issuer information.
- `sso:PutApplicationAccessScope` – Adds or updates the list of
  authorized targets for an IAM Identity Center access scope for an
  application.
- `sso:PutApplicationAssignmentConfiguration` – Used to
  configure how users gain access to an application.

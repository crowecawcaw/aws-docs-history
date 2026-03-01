# Information to be provided to the Amazon Q Business team

Before an independent software provider or vendor (ISV) can become a verified data
accessor, they must provide either an Auth code or Trusted token issuer (TTI)
configuration information to the Amazon Q Business team.

Prerequisite for both Auth code and TTI configurations.

`tenantID`

The `tenantID` is a unique identifier for your application tenant. Each
application might have different terms for a tenant such as Workspace ID for Slack or
Domain ID for Asana. You can review the [Prerequisites](isv-prerequisites.md "isv-prerequisites.md") page
to see how to retrieve the `TenantId` for your application.

Auth code
**Prerequisites:**

- The display name to list on the AWS Management Console
- The business logo that Amazon Q Business customers will select
- The redirect URL for the `oAuth` authorization code
  flow.

###### Note

`oAuth` authorization code flow is an industry
standard for third-party applications to obtain user access
permissions. In the authorization code flow, ISV receives an
auth code from AWS and exchanges the auth code for an ID
token.

- The ISVs must create the following AWS Identity and Access Management (IAM) role
  with the necessary permissions and trust policy to interact with the
  Amazon Q Business services and APIs. This IAM role is granted access as a
  data accessor when Amazon Q Business customers provide access to their
  Amazon Q index. For more information, see [IAM role terms and concepts](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") and [Create
  a role to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").
  - **ISV IAM role**

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Action": [
   "qbusiness:SearchRelevantContent",
   "sso-oauth:CreateTokenWithIAM",
   "kms:Decrypt",
   "sts:SetContext"
   ],
   "Resource": "*",
   "Effect": "Allow",
   "Sid": "MultiServicePermissions"
   }
   ]
  }`

  ```

  - **ISV IAM role trust
    policy**

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Sid": "ISVRoleTrustPolicy",
   "Effect": "Allow",
   "Principal": {
   "AWS": [
   "arn:aws:iam::111122223333:role/`YourApplicationRole`"
   ]
   },
   "Action": [
   "sts:AssumeRole",
   "sts:SetContext",
   "sts:TagSession"
   ]
   }
   ]
  }`

  ```

  - ISV `tenantId`
    - What is `tenantId`?

    The `tenantID` is a unique identifier
    for your application tenant. Each application might
    have different terms for a tenant such as Workspace
    ID for Slack or Domain ID for Asana.
    - Where do you find the
      `tenantId`?

    Provide info as to where can the IT Admin of an
    enterprise can find this information on the
    ISV.

TTI
**Prerequisites:**

- The display name to list on the AWS Management Console
- The business logo that Amazon Q Business customers will select
- OIDC ClientId which can used to generate tokens for all the
  customers - The OAuth 2.0 authorization server (the trusted token
  issuer) that creates the token must have an [OpenID Connect (OIDC)](https://openid.net/specs/openid-connect-discovery-1_0.html "https://openid.net/specs/openid-connect-discovery-1_0.html") discovery endpoint that IAM
  Identity Center can use to obtain public keys to verify the token
  signatures. For more information, see [OIDC discovery endpoint URL (issuer URL)](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts").
- Discovery endpoint/[Issuer URL](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1 "https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1") - The entity that issued the token. This
  value must match the value that is configured in the OIDC discovery
  endpoint (issuer URL) in the trusted token issuer.

###### Note

[Trusted token issuer(App level authentication)](../../../singlesignon/latest/userguide/trusted-token-issuer-configuration-settings.md#oidc-discovery-endpoint-url "../../../singlesignon/latest/userguide/trusted-token-issuer-configuration-settings.md#oidc-discovery-endpoint-url") - A trusted
token issuer is an OAuth 2.0 authorization server that creates signed
tokens. These tokens authorize applications that initiate requests
(requesting applications) for access to AWS managed applications
(receiving applications).

The ISVs must create the following AWS Identity and Access Management (IAM) role with the
necessary permissions and trust policy to interact with the Amazon Q Business
services and APIs. This IAM role is granted access as a data accessor when
Amazon Q Business customers provide access to their Amazon Q index. For more
information, see [IAM
role terms and concepts](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") and [Create a role
to delegate permissions to an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md").

- **ISV IAM role**

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "qbusiness:SearchRelevantContent",
 "sso-oauth:CreateTokenWithIAM",
 "kms:Decrypt",
 "sts:SetContext"
 ],
 "Resource": "*",
 "Effect": "Allow",
 "Sid": "MultiServicePermissions"
 }
 ]
}`

```

- **ISV IAM role trust policy**

JSONJSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ISVRoleTrustPolicy",
 "Effect": "Allow",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111122223333:role/`YourApplicationRole`"
 ]
 },
 "Action": [
 "sts:AssumeRole",
 "sts:SetContext",
 "sts:TagSession"
 ]
 }
 ]
}`

```

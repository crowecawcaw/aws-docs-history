

# Configure OAuth access to AWS Glue Iceberg REST Catalog
<a name="configure-oauth-glue-iceberg-rest"></a>

## Overview
<a name="configure-oauth-glue-iceberg-rest-overview"></a>

The AWS Glue Data Catalog exposes your Apache Iceberg tables through an Iceberg REST Catalog (IRC) endpoint. With OAuth 2.0 support through AWS Sign-In, external integration partners and third-party query engines can access your Iceberg tables using industry-standard OAuth bearer tokens instead of AWS Signature Version 4 (SigV4) signing.

This integration uses the OAuth 2.0 Token Exchange Grant (RFC 8693). An integration partner presents an end user's JSON Web Token (JWT) to AWS Sign-In and exchanges it for a short-lived OAuth access token scoped to the AWS Glue service. The partner then presents that token to the AWS Glue Iceberg REST endpoint to read your tables.

OAuth authorization does not grant additional AWS permissions. Access is bounded by the IAM role the customer designates, the customer's AWS Lake Formation grants, and any optional session policy supplied at exchange time.

Three parties participate in this integration.
+ **Customer (data owner)** – Configures the IAM identity provider, the IAM role the partner assumes, and the Lake Formation grants that bound data access.
+ **Integration partner** – A third-party query engine or platform that performs the token exchange and calls the AWS Glue Iceberg REST endpoint on the end user's behalf.
+ **End user** – The partner's user, whose JWT is carried in the exchanged token.

For general information about OAuth support in AWS Sign-In, see [Sign-In with OAuth 2.0](oauth-sign-in-overview.md).

## Prerequisites
<a name="configure-oauth-glue-iceberg-rest-prereqs"></a>

Unlike OAuth integrations for AWS identities, the Glue Iceberg REST Catalog integration is driven by an external identity. Before a third-party identity provider can exchange a token, you must complete a one-time identity-federation setup.
+ **Create an IAM OIDC identity provider** for your specified third-party issuer. The provider's issuer URL must match the `iss` claim in the partner's JWT tokens. Register the audience that the partner will place in the token's `aud` claim. The audience must be the regional AWS Sign-In token exchange endpoint, `https://{region}.oauth.signin.aws`.
+ **Create an IAM role** that the partner assumes. The role's trust policy must permit `sts:AssumeRoleWithWebIdentity` for the identity provider you created. Constrain the trust policy with the `sts:RoleAuthorizedByIdp` condition so the role can be assumed only when the partner's token authorizes it through the `https://aws.amazon.com/roles` claim.
+ **Grant data access with AWS Lake Formation.** Grant the role fine-grained permissions (databases, tables) on the catalogs the partner should reach. Lake Formation grants are the fine-grained boundary on all data returned.
+ **Configure the partner connection.** Provide the partner with the AWS Glue Iceberg REST endpoint, the AWS Sign-In token exchange endpoint, the role ARN, and any resource scoping (see [Scoping access with a session policy](#configure-oauth-glue-iceberg-rest-scoping)).

## Setting up OAuth access
<a name="configure-oauth-glue-iceberg-rest-setup"></a>

The following steps configure identity and trust in IAM and data access in AWS Lake Formation. Create all resources in the AWS Region where your Iceberg tables reside; the examples use `{region}` as a placeholder.

### Step 1: Create an IAM OIDC identity provider
<a name="configure-oauth-glue-iceberg-rest-setup-step1"></a>

In the IAM console, open the Identity providers page and choose **Add provider** to create an OpenID Connect provider that trusts the integration partner's JWT issuer. The partner's issuer URL will be defined by the partner that you are integrating with.


**OIDC identity provider settings**  

| Setting | Value | 
| --- | --- | 
| Provider type | OpenID Connect | 
| Provider URL | The partner's JWT issuer URL (partner-supplied) | 
| Audience | https://{region}.oauth.signin.aws | 

For more information, see [Create an OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html).

### Step 2: Create an IAM role with a trust policy
<a name="configure-oauth-glue-iceberg-rest-setup-step2"></a>

Create an IAM role that the partner's federated identity assumes. Its trust policy must allow `sts:AssumeRoleWithWebIdentity`, reference the identity provider from Step 1, and validate the audience (`aud`) claim. Adding the `sts:RoleAuthorizedByIdp` condition ensures the role is assumed only when the partner's token authorizes it.

To create the IAM role, you can select your newly created IdP from the **Identity providers** page and choose **Assign Role**. Then, select **Web identity** from the **Trusted entity type**. The same can be done from the **Roles** page. After the role is created, confirm that the role trust policy looks similar to the following example (replace the account ID, provider issuer, and region with your values).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Federated": "arn:aws:iam::{your-account-id}:oidc-provider/{oidc-provider-issuer}"
      },
      "Action": "sts:AssumeRoleWithWebIdentity",
      "Condition": {
        "StringEquals": {
          "{oidc-provider-issuer}:aud": "https://{region}.oauth.signin.aws"
        },
        "Bool": {
          "sts:RoleAuthorizedByIdp": "true"
        }
      }
    }
  ]
}
```

If the partner's issuer is classified as a shared provider, you must add additional conditions in the trust policy to enforce tenancy. For more information, see [OIDC secure-by-default behavior](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_secure-by-default.html).

### Step 3: Grant Lake Formation permissions to the role
<a name="configure-oauth-glue-iceberg-rest-setup-step3"></a>

In AWS Lake Formation, grant the IAM role from Step 2 the permissions it needs on the databases, tables, and columns you want to expose. Lake Formation enforces fine-grained access on every query, so grant only what the partner's users should be able to read — for example, SELECT and DESCRIBE on specific tables. These grants are the primary control over which AWS data is visible to the partner.

### Step 4: Grant AWS Sign-In permissions to the role
<a name="configure-oauth-glue-iceberg-rest-setup-step4"></a>

Attach an identity-based policy to the IAM role from Step 2 that allows the token exchange to mint a Glue-scoped access token.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "arn:aws:signin:{region}:{your-account-id}:service-principal/glue.amazonaws.com"
    }
  ]
}
```

### Step 5 (optional): Narrow access with a managed policy
<a name="configure-oauth-glue-iceberg-rest-setup-step5"></a>

To further restrict what the connection can do, author an IAM managed policy that scopes the permitted AWS Glue actions and resources, and configure it as the `scope` on the partner connection. The effective access is the intersection of the role's permissions, this policy, and your Lake Formation grants. See [Scoping access with a session policy](#configure-oauth-glue-iceberg-rest-scoping).

### Step 6: Configure the partner connection
<a name="configure-oauth-glue-iceberg-rest-setup-step6"></a>

Provide the partner with the AWS Glue Iceberg REST endpoint, the AWS Sign-In token exchange endpoint, the role ARN from Step 2, and any resource scoping from Step 5. After the connection is configured, token exchange and querying happen transparently; the partner's users simply query the external tables.

## Authorization model
<a name="configure-oauth-glue-iceberg-rest-authorization-model"></a>

AWS Glue Iceberg REST Catalog uses the token exchange authorization model provided by AWS Sign-In. The integration partner exchanges the end user's OIDC token (the subject token) for a Glue-scoped OAuth access token at the AWS Sign-In token endpoint, and then presents that access token to the AWS Glue Iceberg REST endpoint.

**Token exchange flow**

1. The partner sends a token exchange request to the AWS Sign-In token endpoint with the end user's OIDC token.

1. AWS Sign-In performs a pre-authentication authorization check on the `signin:Authenticate` action, evaluating resource-based and network condition keys before any downstream call when using a private network or VPCE.

1. AWS STS validates the subject token (issuer, audience, signature) against the customer's IAM OIDC provider, enforces the role trust policy and the `sts:RoleAuthorizedByIdp` condition, and assumes the single role named in the token's `https://aws.amazon.com/roles` claim.

1. AWS Sign-In performs the principal-based `signin:CreateOAuth2Token` authorization, then issues an OAuth access token scoped to the AWS Glue service principal (`glue.amazonaws.com`).

1. The partner calls the AWS Glue Iceberg REST endpoint with the access token in the `Authorization: Bearer` header.

1. AWS Glue validates the token and enforces the customer's Lake Formation permissions on every request.

**Token exchange request**

```
POST /v1/token HTTP/1.1
Host: {region}.oauth.signin.aws
Content-Type: application/x-www-form-urlencoded

grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Atoken-exchange
&subject_token={partner-jwt}
&subject_token_type=urn%3Aietf%3Aparams%3Aoauth%3Atoken-type%3Ajwt
&resource=glue.amazonaws.com
&scope={managed-policy-arn}
```


**Token exchange request parameters**  

| Parameter | Required | Description | 
| --- | --- | --- | 
| grant\_type | Yes | urn:ietf:params:oauth:grant-type:token-exchange | 
| subject\_token | Yes | The partner's JWT representing the end user. | 
| subject\_token\_type | Yes | urn:ietf:params:oauth:token-type:jwt | 
| resource | Yes | The AWS Glue service principal, glue.amazonaws.com. | 
| scope | No | The ARN of a customer-managed IAM policy applied as a session policy. See [Scoping access with a session policy](#configure-oauth-glue-iceberg-rest-scoping). | 

**Token exchange response**

```
{
    "access_token": "{oauth-access-token}",
    "issued_token_type": "urn:ietf:params:oauth:token-type:access_token",
    "token_type": "Bearer",
    "expires_in": 3600
}
```

**Calling the AWS Glue Iceberg REST endpoint**

```
GET /iceberg/v1/catalogs/{catalog}/namespaces HTTP/1.1
Host: glue.{region}.amazonaws.com
Authorization: Bearer {oauth-access-token}
```

**Subject token claims**

The subject token is the partner's JWT token representing the end user. AWS STS validates it by discovering the issuer's keys through the issuer's `/.well-known/openid-configuration` document.


**Subject token claims**  

| Claim | Required | Purpose | 
| --- | --- | --- | 
| iss | Yes | Issuer. Must match the IAM OIDC provider registered in the customer's account. | 
| sub | Yes | Subject. Identifies the partner end user. | 
| aud | Yes | Audience. Must match the audience registered on the customer's OIDC provider — the regional token exchange endpoint URL. | 
| exp | Yes | Expiration time (epoch seconds). | 
| iat | Yes | Issued-at time (epoch seconds). | 
| nbf | No | Not-before time (epoch seconds). Validated if present. | 
| jti | No | Unique token identifier. | 
| https://aws.amazon.com/roles | Yes | The IAM role ARN the principal is authorized to assume. Must contain exactly one ARN. | 
| https://aws.amazon.com/role\_session\_name | Yes | The role session name. Must be 2–64 characters matching [\\w\+=,.@-]. | 
| https://aws.amazon.com/session\_duration | No | Session duration ceiling in seconds (900–43200), capped by the role's maximum session duration. | 

## Scoping access with a session policy
<a name="configure-oauth-glue-iceberg-rest-scoping"></a>

By default, the issued access token is scoped to the `glue.amazonaws.com` service principal, and access is bounded by the assumed role's IAM permissions and your Lake Formation grants.

To narrow access further at exchange time, you can author an IAM managed policy that scopes the permitted AWS Glue actions and resources, and configures the partner connection to pass that policy's ARN as the `scope` parameter. AWS Sign-In applies the policy as a session policy on the assumed role. The resulting access token is bounded by the intersection of the assumed role and the session policy.

The `scope` parameter accepts only a customer-owned managed policy in the customer's account. Cross-account policies are not accepted.

## OAuth resource types
<a name="configure-oauth-glue-iceberg-rest-resource-types"></a>

AWS Sign-In represents OAuth authorization targets as IAM resources. Reference these resources in IAM policies to grant or control OAuth authorization.


| Resource type | ARN format | Description | 
| --- | --- | --- | 
| AWS Glue service principal | arn:aws:signin:{{region}}:{{account-id}}:service-principal/glue.amazonaws.com | Represents AWS Glue as an OAuth authorization target. Use this resource to grant or control OAuth authorization for applications that access the AWS Glue Iceberg REST Catalog. | 

## Token lifecycle
<a name="configure-oauth-glue-iceberg-rest-token-lifecycle"></a>


| Token | Description | 
| --- | --- | 
| Access token | Issued by the token exchange grant. Valid for up to one hour. No refresh token is issued; the partner performs a new token exchange when the token expires. | 

## Managing OAuth tokens
<a name="configure-oauth-glue-iceberg-rest-token-management"></a>

AWS Sign-In provides APIs for validating OAuth authorizations.


| API | Purpose | 
| --- | --- | 
| [`IntrospectOAuth2Token`](https://docs.aws.amazon.com/signin/latest/APIReference/API_dataplane-signin_IntrospectOAuth2TokenWithIAM.html) | Returns metadata describing an OAuth token. | 

## Monitoring OAuth activity
<a name="configure-oauth-glue-iceberg-rest-monitoring"></a>

OAuth-related activities are recorded in AWS CloudTrail. CloudTrail records the token exchange and token introspection.

Token exchange requests that present an invalid subject token (bad signature, wrong issuer, or expired token) are rejected without generating a CloudTrail event in the target account. Only requests carrying a valid subject token with a valid issuer are logged.

**Example – CreateOAuth2Token (token exchange) event:**

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "AssumedRole",
        "arn": "arn:aws:sts::111111111111:assumed-role/PartnerReadOnly/partner-session",
        "accountId": "111111111111"
    },
    "eventTime": "2026-09-25T05:10:04Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "CreateOAuth2Token",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.1",
    "requestParameters": {
        "resource": "glue.amazonaws.com"
    },
    "additionalEventData": {
        "grant_type": "urn:ietf:params:oauth:grant-type:token-exchange",
        "success": "true"
    },
    "readOnly": true,
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111111111111",
    "eventCategory": "Management"
}
```

## Troubleshooting
<a name="configure-oauth-glue-iceberg-rest-troubleshooting"></a>

**Invalid or expired subject token**  
Verify that the partner's OIDC token has not expired and that its signature validates against the issuer's published keys. AWS STS validates the subject token; an invalid token causes the token exchange to fail without issuing an access token.

**Issuer or audience mismatch**  
Verify that the token's `iss` claim matches the IAM OIDC provider registered in the customer's account, and that the `aud` claim matches the audience registered on that provider (the regional token exchange endpoint, `https://{region}.oauth.signin.aws`).

**Role cannot be assumed**  
Verify that the role trust policy permits `sts:AssumeRoleWithWebIdentity` for the OIDC provider, that the `https://aws.amazon.com/roles` claim contains exactly one ARN naming that role, and that the `sts:RoleAuthorizedByIdp` condition is satisfied.

**Scope policy rejected**  
The `scope` parameter accepts only a customer-owned managed policy in the customer's account. Cross-account policies and policies that are not resolvable in the account are rejected.

**Access denied when reading tables**  
Access to table data is bounded by the customer's Lake Formation grants on the assumed role. Verify that the role has Lake Formation permissions on the target databases, tables, and columns.

**Network condition denies the request**  
The token exchange propagates the real caller's network context (`aws:SourceIp`, `aws:SourceVpc`, `aws:SourceVpce`, `aws:VpcSourceIp`). Verify that the role trust policy, resource control policies, and VPC endpoint policies permit the partner's network origin.
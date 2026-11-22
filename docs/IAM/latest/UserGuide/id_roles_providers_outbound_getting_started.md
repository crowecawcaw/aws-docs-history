

# Getting started with outbound identity federation

This guide shows you how to enable outbound identity federation for your AWS account and obtain your first JSON Web Token (JWT) using the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API. You will enable the feature, establish a trust relationship with an external service, configure IAM permissions, and request a token using either the AWS CLI or AWS SDK for Python (Boto3). The guide also explains how to use credentials that carry [trusted identity propagation (TIP)](id_roles_providers_tip.md) context, set `SubjectMode` to `OriginIdentity` so `sub` contains the session's TIP Subject, and optionally request Scope values for the external service.

## Prerequisites
<a name="outbound-federation-prerequisites"></a>

Before you begin, make sure you have:
+ Latest version of the AWS CLI or Python 3.8 (or later) and Boto3 installed (for AWS SDK examples)
+ An external service account where you can configure trust relationships (such as an external cloud provider, SaaS provider, or a test application)

If you plan to set `SubjectMode` to `OriginIdentity`, you also need:
+ Credentials from a TIP session whose context contains a Subject and either an Issuer or a federated-provider ARN. Use [Trusted identity propagation with IAM](id_roles_providers_tip.md) to complete the applicable source-specific setup.
+ A TIP Subject that the external service will use to identify the represented human user or workload. The Subject cannot be blank, begin with `arn:` in any capitalization, contain leading or trailing spaces, or contain control or formatting characters.

AWS STS rejects a request that sets `SubjectMode` to `OriginIdentity` when the session or Subject does not meet these requirements.

If you plan to request Scope, define the accepted Scope values and their authorization meaning in the external service before requesting tokens.

**Note**  
The `GetWebIdentityToken` API is not available on the STS Global endpoint.
To assume a role in a different AWS partition, exchange the JWT returned by [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) by calling [AssumeRoleWithWebIdentity](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html). This JWT exchange is supported only when the source and destination roles are in different AWS partitions. For more information, see [Federating AWS identities across AWS partitions](id_roles_providers_outbound_cross_partition.md). To assume a role in the same partition, call [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) using the caller's existing AWS credentials.

## Enable outbound identity federation for your account
<a name="enable-outbound-federation"></a>

You must enable outbound identity federation before you can request tokens. You can enable the feature using the AWS Management Console or programmatically using the [EnableOutboundWebIdentityFederation](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EnableOutboundWebIdentityFederation.html) API.

### Using the AWS CLI
<a name="enable-using-cli"></a>

```bash
aws iam enable-outbound-web-identity-federation
```

### Using AWS SDK for Python
<a name="enable-using-sdk"></a>

```python
import boto3

# Create IAM client
iam_client = boto3.client('iam')

# Enable outbound identity federation
response = iam_client.enable_outbound_web_identity_federation()
print(f"Feature enabled. Issuer URL: {response['IssuerUrl']}")
print(f"Status: {response['Status']}")
```

### Using the AWS Console
<a name="enable-using-console"></a>

Navigate to IAM and select **Account Settings** under the **Access Management** section of the left-hand navigation menu

![Account settings menu item highlighted in left navigation under Access management section.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/outbound-screen-1.png)


Once you enable the feature, make note of your account-specific issuer URL. You will use this URL when configuring trust relationships in external services. You can also retrieve this issuer URL as needed using the [GetOutboundWebIdentityFederationInfo](https://docs.aws.amazon.com/IAM/latest/APIReference/API_GetOutboundWebIdentityFederationInfo.html) API.

![Outbound Identity Federation interface showing Enabled status with Disable button and token issuer URL.](https://docs.aws.amazon.com/IAM/latest/UserGuide/images/outbound-screen-2.png)


## Establish trust relationship in external service
<a name="establish-trust-relationship"></a>

Configure the external service to trust and accept tokens issued by your AWS account. The specific steps vary by service, but generally involve:
+ Registering your AWS account issuer URL as a trusted identity provider.
+ Configuring validation of the token signature, issuer, audience, and expiration.
+ Deciding which identity the external service expects in `sub` and how to map it. With the default `AWSIdentity` mode, `sub` contains the IAM principal ARN. When `SubjectMode` is set to `OriginIdentity`, `sub` contains the TIP Subject. If authorization also depends on the requesting IAM principal, use the `principal_id` claim under the `https://sts.amazonaws.com/` namespace.
+ Defining how validated identities, claims, and optional Scope values map to permissions in the external service. Scope is a request from the caller, not a permission grant from AWS STS.

Refer to the external service documentation for its trust, identity-mapping, Scope, and authorization requirements. If the relying party is AWS in another partition, see [Federating AWS identities across AWS partitions](id_roles_providers_outbound_cross_partition.md).

## Configure IAM permissions
<a name="configure-iam-permissions"></a>

Create an IAM policy that grants permission to call the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API and attach the policy to an IAM role that needs to generate tokens.

The base request examples on this page include tags. Every request requires `sts:GetWebIdentityToken`, and a request that includes tags also requires `sts:TagGetWebIdentityToken`. AWS STS evaluates `sts:TagGetWebIdentityToken` as an additional authorization check, not as a separate API operation. If your request does not include tags, omit this permission.

The following policy allows token requests only for `https://api.example.com` as the audience and enforces a maximum token lifetime of 5 minutes (300 seconds).

### Example IAM policy
<a name="example-iam-policy"></a>

```json
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:GetWebIdentityToken",
                "sts:TagGetWebIdentityToken"
            ],
            "Resource": "*",
            "Condition": {
                "ForAllValues:StringEquals": {
                    "sts:IdentityTokenAudience": "https://api.example.com"
                },
                "Null": {
                    "sts:IdentityTokenAudience": "false"
                },
                "NumericLessThanEquals": {
                    "sts:DurationSeconds": 300
                }
            }
        }
    ]
}
```

This policy does not restrict `SubjectMode`, so it permits requests that use either valid mode when the other policy conditions match. A request that sets `SubjectMode` to `OriginIdentity` still requires credentials that meet the `OriginIdentity` requirements in [Prerequisites](#outbound-federation-prerequisites). Setting `SubjectMode` does not require another action permission. Use the `sts:SubjectMode` condition key if you need to restrict which mode the role can request.

A request that includes Scope also requires `sts:SetWebIdentityTokenScope`. AWS STS evaluates this permission as an additional authorization check, not as a separate API operation. Use the multivalued `sts:IdentityTokenScope` condition key to restrict every requested Scope value. For complete least-privilege examples, see [Controlling access with IAM policies](id_roles_providers_outbound_policies.md).

## Request your first JSON Web Token (JWT)
<a name="request-first-jwt"></a>

You can request a JSON Web Token using the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API. You can specify the following parameters when calling the API:
+ **Audience (required):** The intended recipient of the token. This value populates the `aud` claim in the JWT. External services validate this claim to make sure the token was intended for them.
+ **SigningAlgorithm (required):** The cryptographic algorithm used to sign the token. Valid values are `ES384` and `RS256`. Use `ES384` for optimal security and performance, or `RS256` for broader compatibility with systems that do not support ECDSA.
+ **DurationSeconds (optional):** The token lifetime in seconds. Valid values range from 60 to 3600. The default is 300 (5 minutes). We recommend shorter token lifetimes for increased security.
+ **Tags (optional):** A list of key-value pairs to include as custom claims in the token. External services can use these claims for fine-grained authorization.
+ **SubjectMode (optional):** Controls which identity AWS STS places in `sub`. `AWSIdentity` places the requesting IAM principal ARN in `sub` and is the default when you omit this parameter. `OriginIdentity` places the TIP Subject carried by the calling session in `sub`. It requires credentials that meet the `OriginIdentity` requirements in [Prerequisites](#outbound-federation-prerequisites).
+ **Scope (optional):** A space-delimited string containing distinct values requested from the external service. You can include Scope only when `SubjectMode` is set to `OriginIdentity` and `Audience` contains exactly one value. The complete Scope string must contain 1 through 256 characters. Each value can contain printable ASCII characters except a space, double quotation mark (`"`), comma, or backslash (`\`). Separate values with single spaces. Do not include leading, trailing, or repeated spaces. AWS STS rejects exact duplicate values but treats values that differ only by capitalization as distinct. AWS STS copies an accepted Scope value unchanged into the top-level `scope` claim.

The API returns the following fields:
+ **WebIdentityToken:** The signed JWT as a base64url-encoded string. Include this token in requests to external services.
+ **Expiration:** The UTC timestamp for when the token expires.

### Using the AWS CLI
<a name="using-aws-cli"></a>

```
aws sts get-web-identity-token \
    --region us-east-1 \
    --endpoint-url https://sts.us-east-1.amazonaws.com \
    --audience "https://api.example.com" \
    --signing-algorithm ES384 \
    --duration-seconds 300 \
    --tags Key=team,Value=data-engineering \
           Key=environment,Value=production \
           Key=cost-center,Value=analytics
```

### Using AWS SDK for Python
<a name="using-aws-sdk-python"></a>

```python
import boto3

# GetWebIdentityToken requires a Regional STS endpoint.
sts_client = boto3.client(
    'sts',
    region_name='us-east-1',
    endpoint_url='https://sts.us-east-1.amazonaws.com'
)

response = sts_client.get_web_identity_token(
    Audience=['https://api.example.com'],
    DurationSeconds=300,
    SigningAlgorithm='ES384',
    Tags=[
        {'Key': 'team', 'Value': 'data-engineering'},
        {'Key': 'environment', 'Value': 'production'},
        {'Key': 'cost-center', 'Value': 'analytics'}
    ]
)

token = response['WebIdentityToken']
```

### Request a token with `SubjectMode` set to `OriginIdentity` and Scope
<a name="outbound-request-origin-identity-scope"></a>

Use credentials that meet the `OriginIdentity` requirements in [Prerequisites](#outbound-federation-prerequisites). These examples set `SubjectMode` to `OriginIdentity` and request the `read` and `write` Scope values.

In addition to the permissions from the previous section, grant the role `sts:SetWebIdentityTokenScope` and restrict the permitted values as described in [Controlling access with IAM policies](id_roles_providers_outbound_policies.md). To request `OriginIdentity` without Scope, omit `--scope` from the AWS CLI request or `Scope` from the SDK request. A request without Scope does not require `sts:SetWebIdentityTokenScope`.

#### AWS CLI example
<a name="outbound-request-origin-identity-scope-cli"></a>

```bash
aws sts get-web-identity-token \
    --region us-east-1 \
    --endpoint-url https://sts.us-east-1.amazonaws.com \
    --audience "https://api.example.com" \
    --signing-algorithm ES384 \
    --duration-seconds 300 \
    --subject-mode OriginIdentity \
    --scope "read write"
```

#### AWS SDK for Python example
<a name="outbound-request-origin-identity-scope-sdk-python"></a>

```python
import boto3

sts_client = boto3.client(
    'sts',
    region_name='us-east-1',
    endpoint_url='https://sts.us-east-1.amazonaws.com'
)

response = sts_client.get_web_identity_token(
    Audience=['https://api.example.com'],
    DurationSeconds=300,
    SigningAlgorithm='ES384',
    SubjectMode='OriginIdentity',
    Scope='read write'
)

token = response['WebIdentityToken']
```

Decode the returned token locally and inspect the locations in the following table. Replace the illustrative Subject and IAM principal ARN with the exact values expected for your session.


| Where to inspect | Expected value | Meaning of a missing or different value | 
| --- | --- | --- | 
| Top-level sub | The exact TIP Subject carried by the calling session | Do not treat the token as representing the expected origin identity. Confirm the calling session contains the expected TIP Subject and that the request sets SubjectMode to OriginIdentity. | 
| subject\_mode under the https://sts.amazonaws.com/ namespace | OriginIdentity | OriginIdentity was not applied. Do not interpret sub as the TIP Subject. | 
| principal\_id under the https://sts.amazonaws.com/ namespace | The ARN of the IAM principal that requested the token | The token does not provide the expected AWS caller identity. Do not use it for authorization that depends on that principal. | 
| Top-level scope | read write | The requested Scope was not included unchanged. Do not grant Scope-based access with the token. Verify the request and sts:SetWebIdentityTokenScope authorization. | 

These checks confirm the expected `SubjectMode`, TIP, and Scope output. Before accepting the token, also validate its signature and the essential claims described later on this page.

For the complete claim schema and examples, see [Understanding token claims](id_roles_providers_outbound_token_claims.md).

You can also decode the JWT to inspect its contents using standard JWT libraries like PyJWT, Python-jose for Python, Nimbus JOSE\+JWT for Java or debuggers like jwt.io. Refer to [Understanding token claims](id_roles_providers_outbound_token_claims.md) for more information on claims included in the token.

## Use the token with an external service
<a name="use-token-with-external-service"></a>

After receiving the token, include it in requests to the external service. The method varies by service, but most services accept tokens in the `Authorization` header. Before granting access, the external service must [fetch the verification keys and metadata](#fetch-verification-keys), verify the token signature, and complete the [essential claim validations](#essential-claim-validations). After validation, the external service applies its configured identity, claim, and Scope mappings to make authorization decisions.

## Fetch verification keys and metadata from the OpenID Connect (OIDC) endpoints
<a name="fetch-verification-keys"></a>

The unique issuer URL for your AWS account hosts the OpenID Connect (OIDC) discovery endpoints that contain verification keys and metadata necessary for token verification.

The OIDC discovery endpoint URL contains metadata some providers use to verify tokens. It is available at:

```
{issuer_url}/.well-known/openid-configuration
```

The JWKS (JSON Web Key Set) endpoint contains keys used to verify token signatures. It is available at:

```
{issuer_url}/.well-known/jwks.json
```

### Fetch JWKS using curl
<a name="fetch-jwks-curl"></a>

```bash
curl https://{issuer_url}/.well-known/jwks.json
```

Response:

```json
{
  "keys": [
    {
      "kty": "EC",
      "use": "sig",
      "kid": "key-id-1",
      "alg": "ES384",
      "crv": "P-384",
      "x": "base64-encoded-x-coordinate",
      "y": "base64-encoded-y-coordinate"
    },
    {
      "kty": "RSA",
      "use": "sig",
      "kid": "key-id-2",
      "n": "base64-encoded-modulus",
      "e": "AQAB"
    }
  ]
}
```

### Using AWS SDK for Python
<a name="fetch-using-sdk"></a>

```python
import requests

# Fetch Openid Configuration
open_id_config_response = requests.get("https://{issuer_url}/.well-known/openid-configuration")
open_id_config = open_id_config_response.json()

# Fetch JWKS
jwks_response = requests.get("https://{issuer_url}/.well-known/jwks.json")
jwks = jwks_response.json()
```

We recommend caching these keys to avoid fetching them for every token verification.

### Essential claim validations
<a name="essential-claim-validations"></a>
+ **Subject (`sub`):** Validate the identity expected for the token's subject mode. For `AWSIdentity`, require the expected IAM principal ARN or permitted ARN pattern. For `OriginIdentity`, require the expected TIP Subject or permitted Subject format, and validate it together with `iss` and the origin identity source.
+ **Expiration (`exp`):** Make sure the token has not expired. JWT libraries typically handle this automatically.
+ **Audience (`aud`):** Verify the audience matches your expected value. This prevents tokens intended for other services from being used with yours.
+ **Issuer (`iss`):** Verify the issuer matches an AWS account you trust. Maintain a list of trusted issuer URLs.
+ **Subject mode (`subject_mode`):** Inspect this claim under the `https://sts.amazonaws.com/` namespace. A missing claim means the token uses the default `AWSIdentity` representation. If the claim is present, require the value `OriginIdentity`. A different value does not match the documented token schema. If your authorization model requires the TIP Subject in `sub`, reject a token with a missing or different value.
+ **Origin identity source:** When `subject_mode` is `OriginIdentity`, inspect `origin_identity.issuer` and `origin_identity.federated_provider_arn` under the `https://sts.amazonaws.com/` namespace. Require either the Issuer or federated-provider ARN used by your authorization model to match the expected identity provider. A missing or unexpected value means that you must not authorize access based on `sub`.
+ **IAM principal (`principal_id`):** Inspect this claim under the `https://sts.amazonaws.com/` namespace. AWS STS includes it when the caller has an IAM principal ARN, regardless of `subject_mode`. For a role session, the value is the role ARN, not the assumed-role session ARN. Validate it when your authorization model depends on the requesting IAM principal. A missing or unexpected value means you must not grant access based on the IAM principal.
+ **Scope (`scope`):** If your authorization model uses Scope, require only values your external service recognizes and permits for the identity in `sub`. A missing or unrecognized value means you must not grant the corresponding Scope-based access.

Whenever possible, you should validate additional AWS-specific claims to implement fine-grained access control in your external service. For example, validate the org\_id claim to restrict access to IAM principals in your AWS Organization, check principal\_tags to enforce attribute-based access control (such as allowing only production environments or specific teams), or verify session context claims like lambda\_source\_function\_arn or ec2\_instance\_source\_vpc to restrict access based on the compute resource. Refer to [Understanding token claims](id_roles_providers_outbound_token_claims.md) for a full list of claims included in the token.
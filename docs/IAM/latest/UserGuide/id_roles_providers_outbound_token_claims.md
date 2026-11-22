

# Understanding token claims

When you call the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API, AWS Security Token Service (AWS STS) returns a signed JSON Web Token (JWT) that contains claims about the calling IAM principal and, when applicable, the requesting session. Understanding these claims helps you implement secure authentication flows, configure claim validation in external services, and use claims for fine-grained access control.

The JWT includes standard OpenID Connect (OIDC) claims such as subject (`sub`), audience (`aud`), and issuer (`iss`). AWS STS also includes AWS identity and session-context claims when they apply to the request. These claims appear under the `https://sts.amazonaws.com/` namespace, as shown in the following sample. If the request includes tags, AWS STS places them in the `request_tags` object under the same namespace.

When credentials that contain [trusted identity propagation (TIP)](id_roles_providers_tip.md) context call `GetWebIdentityToken`, AWS STS includes each applicable `origin_identity` and `transaction_context` claim from that context in the resulting JWT, regardless of `SubjectMode`. `SubjectMode` controls which identity AWS STS places in `sub`; it does not suppress TIP claims. If the request includes an accepted `Scope` value, AWS STS adds it as the top-level `scope` claim.

**Note**  
TIP context is Customer-Created Metadata and does not constitute Customer Content. The Subject and identity provider claims can contain personally identifying, confidential, or sensitive information. Do not configure these values with information that you do not want included in the JWT and disclosed to its intended external recipient.

The following sample shows the default token structure and the placement of AWS identity, session-context, and request-tag claims. See [TIP and Scope claims](#outbound-token-claims-tip-scope) for the additional conditional claims. Not every claim is present in every token.

```
{
  "iss": "https://abc123-def456-ghi789-jkl012.tokens.sts.global.api.aws",
  "aud": "https://api.example.com",
  "sub": "arn:aws:iam::123456789012:role/DataProcessingRole",
  "iat": 1700000000,
  "exp": 1700000900,
  "jti": "xyz123-def456-ghi789-jkl012",
  "https://sts.amazonaws.com/": {
    "aws_account": "123456789012",
    "source_region": "us-east-1",
    "org_id": "o-abc1234567",
    "ou_path": "o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/ou-ab12-22222222/",
    "principal_tags": {
      "environment": "production",
      "team": "data-engineering",
      "cost-center": "engineering"
    },
    "lambda_source_function_arn": "arn:aws:lambda:us-east-1:123456789012:function:process-data",
    "request_tags": {
      "job-id": "job-2024-001",
      "priority": "high",
      "data-classification": "sensitive"
    }
  }
}
```

## Standard claims
<a name="standard-claims"></a>

The standard OIDC claims present in the tokens facilitate interoperability with a wide range of external services. These claims can be validated using most JWT libraries.


| Claim | Name | Description | Example value | 
| --- | --- | --- | --- | 
| iss | Issuer | Your account-specific issuer URL. External services validate this claim to ensure it matches their trusted issuer. | https://abc123-def456-ghi789-jkl012.tokens.sts.global.api.aws | 
| aud | Audience | The intended recipient for the token specified in the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) request. | https://api.example.com | 
| sub | Subject | The identity represented by the token. If SubjectMode is omitted or set to AWSIdentity, the value is the ARN of the IAM principal that requested the token. If SubjectMode is set to OriginIdentity, the value is the TIP Subject carried by the calling session. | arn:aws:iam::123456789012:role/DataProcessingRole or user@example.com | 
| iat | Issued At | NumericDate value that identifies the time at which the JWT was issued. | 1700000000 | 
| exp | Expiration | NumericDate value that identifies the expiration time on or after which the JWT MUST NOT be accepted for processing. | 1700000900 | 
| jti | JWT ID | Unique identifier for this token instance. | xyz123-def456-ghi789-jkl012 | 

### Understand the subject claim
<a name="outbound-token-claims-subject"></a>

The optional `SubjectMode` request parameter determines which identity AWS STS places in the standard `sub` claim:
+ If you omit `SubjectMode` or set it to `AWSIdentity`, `sub` contains the ARN of the IAM principal that requested the token.
+ If you set `SubjectMode` to `OriginIdentity`, `sub` contains the TIP Subject carried by the calling session.

AWS STS includes `principal_id` when the caller has an IAM principal ARN, regardless of `SubjectMode`. For a role session, `principal_id` contains the role ARN, not the assumed-role session ARN. When `SubjectMode` is `OriginIdentity`, AWS STS also includes the `subject_mode` claim with the value `OriginIdentity`. The [TIP and Scope claims](#outbound-token-claims-tip-scope) example shows where these claims appear in the token.

If an existing relying party expects `sub` to contain an IAM principal ARN, omit `SubjectMode` or set it to `AWSIdentity`.

## Custom claims
<a name="custom-claims"></a>

In addition to standard OIDC claims, AWS STS can include claims derived from the AWS identity, session context, request tags, and TIP context. AWS STS nests these claims under the `https://sts.amazonaws.com/` namespace. The tables in this section explain what each claim contains and when it appears. The optional `scope` claim is an exception: AWS STS places it at the top level when the request includes an accepted `Scope` value.

For the condition keys used in cross-partition role assumption and their availability in the destination session, see the AWS STS tab under [Available keys for AWS OIDC federation](reference_policies_iam-condition-keys.md#condition-keys-wif).

### AWS identity claims
<a name="aws-identity-claims"></a>

These claims provide detailed information about your AWS account, organization structure, and IAM principal.


| Claim | Description | Maps to Condition Key | Example Value | 
| --- | --- | --- | --- | 
| aws\_account | Your AWS account ID | [aws:PrincipalAccount](reference_policies_condition-keys.md#condition-keys-principalaccount) | 123456789012 | 
| source\_region | The AWS region where the token was requested | [aws:RequestedRegion](reference_policies_condition-keys.md#condition-keys-requestedregion) | us-east-1 | 
| org\_id | Your AWS Organizations ID (if your account is part of an organization) | [aws:PrincipalOrgID](reference_policies_condition-keys.md#condition-keys-principalorgid) | o-abc1234567 | 
| ou\_path | The AWS Organizations paths for the source account, as an array. Present when organization paths are available in the source request context. | [aws:PrincipalOrgPaths](reference_policies_condition-keys.md#condition-keys-principalorgpaths) | ["o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/ou-ab12-22222222/"] | 
| principal\_tags | Tags attached to the IAM principal or assumed role session. When a token is requested where the requesting IAM principal has both principal tags and session tags, the session tags will be present in the JWT. | [aws:PrincipalTag/<tag-key>](reference_policies_condition-keys.md#condition-keys-principaltag) | {"environment": "production", "team": "data-engineering", "cost-center":"engineering"} | 

### Session context claims
<a name="session-context-claims"></a>

These claims provide information about the compute environment and session where the token request originated. AWS STS automatically includes these claims when applicable based on the requesting principal's session context.


| Claim | Description | Maps to Condition Key | Example Value | 
| --- | --- | --- | --- | 
| original\_session\_exp | When the original role session credentials will expire (for assumed roles) | N/A | 2024-01-15T10:00:00Z | 
| federated\_provider | The identity provider name for federated sessions | [aws:FederatedProvider](reference_policies_condition-keys.md#condition-keys-federatedprovider) | arn:aws:iam::111122223333:oidc-provider/your\_oidc\_provider | 
| identity\_store\_user\_id | IAM Identity Center user ID | [identitystore:UserId](reference_policies_condition-keys.md#condition-keys-identity-store-user-id) | user-abc123def456 | 
| identity\_store\_arn | ARN of the IAM Identity Center identity store | [identitystore:IdentityStoreArn](https://docs.aws.amazon.com/singlesignon/latest/userguide/condition-context-keys-sts-idc.html#condition-keys-identity-store-arn) | arn:aws:identitystore::123456789012:identitystore/d-abc1234567 | 
| ec2\_source\_instance\_arn | ARN of the requesting EC2 instance | [ec2:SourceInstanceArn](reference_policies_condition-keys.md#condition-keys-ec2-source-instance-arn) | arn:aws:ec2:us-east-1:123456789012:instance/i-abc123def456 | 
| ec2\_instance\_source\_vpc | VPC ID where EC2 role credentials were delivered | [aws:Ec2InstanceSourceVpc](reference_policies_condition-keys.md#condition-keys-ec2instancesourcevpc) | vpc-abc123def456 | 
| ec2\_instance\_source\_private\_ipv4 | Private IPv4 address of the EC2 instance | [aws:Ec2InstanceSourcePrivateIPv4](reference_policies_condition-keys.md#condition-keys-ec2instancesourceprivateip4) | 10.0.1.25 | 
| ec2\_role\_delivery | The instance metadata service (IMDS) version that delivered the source role credentials: 1.0 for IMDSv1 or 2.0 for IMDSv2. | [ec2:RoleDelivery](reference_policies_condition-keys.md#condition-keys-ec2-role-delivery) | 2.0 | 
| source\_identity | Source identity set by the principal | [aws:SourceIdentity](reference_policies_condition-keys.md#condition-keys-sourceidentity) | admin-user | 
| lambda\_source\_function\_arn | ARN of the calling Lambda function | [lambda:SourceFunctionArn](reference_policies_condition-keys.md#condition-keys-lambda-source-function-arn) | arn:aws:lambda:us-east-1:123456789012:function:my-function | 
| glue\_credential\_issuing\_service | AWS Glue service identifier for Glue jobs | [glue:CredentialIssuingService](reference_policies_condition-keys.md#condition-keys-glue-credential-issuing) | glue.amazonaws.com | 
| invoked\_by | The AWS service acting on the customer's behalf by assuming the source role, or the last service in a [forward access session](access_forward_access_sessions.md). This claim is present only when the source session includes that service's identity. | N/A | ec2.amazonaws.com | 
| mfa\_present | Indicates that the IAM principal authenticated with MFA. Present only when MFA was used, with the string value "true". It is never "false". | [aws:MultiFactorAuthPresent](reference_policies_condition-keys.md#condition-keys-multifactorauthpresent) | "true" | 
| mfa\_age | The number of seconds since the IAM principal authenticated with MFA, encoded as a string. Present only when MFA was used and the authentication age is available. | [aws:MultiFactorAuthAge](reference_policies_condition-keys.md#condition-keys-multifactorauthage) | "1800" | 

### TIP and Scope claims
<a name="outbound-token-claims-tip-scope"></a>

When the credentials used to call AWS STS contain TIP context, AWS STS can include supported TIP claims in the JWT. If the request also includes an accepted `Scope` value, AWS STS includes the `scope` claim. Except for `scope`, the claims in the following table are nested under the `https://sts.amazonaws.com/` namespace. The table explains what each claim contains and when AWS STS includes it.


| Claim | Description | When included | 
| --- | --- | --- | 
| principal\_id | The ARN of the IAM principal that requested the token. For a role session, this is the role ARN, not the assumed-role session ARN. This value corresponds to the [aws:PrincipalArn](reference_policies_condition-keys.md#condition-keys-principalarn) condition key. | The caller has an IAM principal ARN. | 
| subject\_mode | Indicates that AWS STS placed the TIP Subject in sub. The value is OriginIdentity. | SubjectMode is set to OriginIdentity. | 
| origin\_identity | Contains the supported origin identity claims carried in TIP context. | At least one supported origin identity claim is present. | 
| origin\_identity.subject | The TIP Subject carried by the calling session. | The calling credentials contain a TIP Subject. | 
| origin\_identity.subject\_type | The optional type value carried with the TIP Subject. | The calling credentials contain a Subject type. | 
| origin\_identity.issuer | The issuer value carried with the TIP Subject. | The calling credentials contain an Issuer. | 
| origin\_identity.federated\_provider\_arn | The ARN of the IAM identity provider used to establish the originating federated session. | The calling credentials contain the federated-provider ARN. | 
| origin\_identity.identity\_provider\_account | The JWT representation of aws:OriginIdentity/IdentityProviderAccount. Contains the AWS account ID that owns the identity provider used to establish the originating federated session. | The calling credentials contain the identity provider account. | 
| origin\_identity.identity\_provider\_org\_id | The JWT representation of aws:OriginIdentity/IdentityProviderOrgID. Contains the AWS Organizations ID for the account that owns the identity provider. | The identity provider account belongs to an organization and the calling credentials contain its organization ID. | 
| transaction\_context.identity\_provider | Contains customer-configured identity provider runtime claims carried in TIP context. | At least one mapped identity provider runtime claim is present. | 
| scope | Contains the accepted Scope request value unchanged. This claim is top level. | The request includes an accepted Scope value. | 

For a TIP session established through SAML federation, `origin_identity.issuer` is the SHA-384 hash of the signing public key that AWS used to verify the SAML assertion. The value changes when the identity provider rotates its signing certificate. If an external service uses this value, update its approved values before rotation so it does not reject valid tokens. Use `origin_identity.federated_provider_arn` when the external service needs a stable identifier for the configured SAML provider.

The following fragment shows where the claims appear in the JWT. It includes only claims relevant to `SubjectMode`, TIP, and Scope. Values are illustrative.

```json
{
  "sub": "user@example.com",
  "scope": "session:role:analyst",
  "https://sts.amazonaws.com/": {
    "principal_id": "arn:aws:iam::123456789012:role/DataProcessingRole",
    "subject_mode": "OriginIdentity",
    "origin_identity": {
      "subject": "user@example.com",
      "subject_type": "user",
      "issuer": "idp.example.com",
      "federated_provider_arn": "arn:aws:iam::123456789012:oidc-provider/idp.example.com",
      "identity_provider_account": "123456789012",
      "identity_provider_org_id": "o-a1b2c3d4e5"
    },
    "transaction_context": {
      "identity_provider": {
        "department": "analytics"
      }
    }
  }
}
```

TIP and Scope claims count toward the 20,000-byte JWT payload limit. AWS STS rejects a request that would exceed this limit.

Scope represents what the caller requests from the external service. It is not a grant from AWS STS. IAM policies control which Scope values the caller can request, and the external service independently decides what each value means and whether the identity in `sub` is authorized to use it.

### Request tags
<a name="request-tags"></a>

You can add custom claims to tokens by specifying tags in the [GetWebIdentityToken](https://docs.aws.amazon.com/STS/latest/APIReference/API_GetWebIdentityToken.html) API request. These claims appear under the `request_tags` field in the token and enable you to pass specific information that external services can use for fine-grained authorization decisions. You can specify up to 50 tags per request.

Example request:

```python
response = sts_client.get_web_identity_token(
    Audience=['https://api.example.com'],
    SigningAlgorithm='ES384',
    Tags=[
        {'Key': 'team', 'Value': 'data-engineering'},
        {'Key': 'cost-center', 'Value': 'analytics'},
        {'Key': 'environment', 'Value': 'production'}
    ]
)
```

Resulting claims in token:

```json
{
  "request_tags": {
    "team": "data-engineering",
    "cost-center": "analytics",
    "environment": "production"
  }
}
```
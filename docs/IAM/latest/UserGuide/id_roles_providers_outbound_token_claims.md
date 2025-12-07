# Understanding token claims

When you call the [GetWebIdentityToken](../../../STS/latest/APIReference/API_GetWebIdentityToken.md "../../../STS/latest/APIReference/API_GetWebIdentityToken.md") API, AWS Security Token Service returns a signed JSON Web Token (JWT) that contains a set of claims that represent the identity of the IAM principal. These tokens are compliant with [RFC 7519](https://datatracker.ietf.org/doc/html/rfc7519 "https://datatracker.ietf.org/doc/html/rfc7519"). Understanding the structure and contents of these tokens helps you implement secure authentication flows, configure appropriate claim validations in external services, and effectively use custom claims for fine-grained access control.

The JWT includes standard OpenID Connect (OIDC) claims such as subject ("sub"), audience ("aud"), issuer ("iss") to facilitate interoperability across different external services. AWS STS populates the token with AWS identity-specific claims (like the AWS Account ID and Principal tags) and session context claims (like EC2 instance ARNs) when applicable. You can also add custom claims to the token by passing them as request tags to the [GetWebIdentityToken](../../../STS/latest/APIReference/API_GetWebIdentityToken.md "../../../STS/latest/APIReference/API_GetWebIdentityToken.md") API. The AWS identity-specific claims, and session context claims and custom claims are nested under the "https://sts.amazonaws.com/" namespace in the token.

Refer to the sample token below for a list of claims included in the token. Please note that all these claims may not be present in a token at the same time.

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

The standard OIDC claims present in the tokens facilitate interoperability with a wide range of external services. These claims can be validated using most JWT libraries.

| Claim | Name       | Description                                                                                                                                                                                                     | Example Value                                                 |
| ----- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| iss   | Issuer     | Your account-specific issuer URL. External services validate this claim to ensure it matches their trusted issuer.                                                                                              | https://abc123-def456-ghi789-jkl012.tokens.sts.global.api.aws |
| aud   | Audience   | The intended recipient for the token specified in the [GetWebIdentityToken](../../../STS/latest/APIReference/API_GetWebIdentityToken.md "../../../STS/latest/APIReference/API_GetWebIdentityToken.md") request. | https://api.example.com                                       |
| sub   | Subject    | The ARN of the IAM principal that requested the token.                                                                                                                                                          | arn:aws:iam::123456789012:role/DataProcessingRole             |
| iat   | Issued At  | NumericDate value that identifies the time at which the JWT was issued.                                                                                                                                         | 1700000000                                                    |
| exp   | Expiration | NumericDate value that identifies the expiration time on or after which the JWT MUST NOT be accepted for processing.                                                                                            | 1700000900                                                    |
| jti   | JWT ID     | Unique identifier for this token instance.                                                                                                                                                                      | xyz123-def456-ghi789-jkl012                                   |

## Custom claims

In addition to the standard OIDC claims, AWS STS adds claims about the identity and session context when applicable. You can also add your own claims to the token by passing them as request tags. Custom claims are nested under the https://sts.amazonaws.com/ namespace.

### AWS identity claims

These claims provide detailed information about your AWS account, organization structure, and IAM principal.

| Claim          | Description                                                                                                                                                                                                     | Maps to Condition Key                                                                                                                                                  | Example Value                                                                          |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| aws_account    | Your AWS account ID                                                                                                                                                                                             | [aws:PrincipalAccount](reference_policies_condition-keys.md#condition-keys-principalaccount "reference_policies_condition-keys.md#condition-keys-principalaccount")    | 123456789012                                                                           |
| source_region  | The AWS region where the token was requested                                                                                                                                                                    | [aws:RequestedRegion](reference_policies_condition-keys.md#condition-keys-requestedregion "reference_policies_condition-keys.md#condition-keys-requestedregion")       | us-east-1                                                                              |
| org_id         | Your AWS Organizations ID (if your account is part of an organization)                                                                                                                                          | [aws:PrincipalOrgID](reference_policies_condition-keys.md#condition-keys-principalorgid "reference_policies_condition-keys.md#condition-keys-principalorgid")          | o-abc1234567                                                                           |
| ou_path        | Your organizational unit path (if applicable)                                                                                                                                                                   | [aws:PrincipalOrgPaths](reference_policies_condition-keys.md#condition-keys-principalorgpaths "reference_policies_condition-keys.md#condition-keys-principalorgpaths") | o-a1b2c3d4e5/r-ab12/ou-ab12-11111111/ou-ab12-22222222/                                 |
| principal_tags | Tags attached to the IAM principal or assumed role session. When a token is requested where the requesting IAM principal has both principal tags and session tags, the session tags will be present in the JWT. | [aws:PrincipalTag/<tag-key>](reference_policies_condition-keys.md#condition-keys-principaltag "reference_policies_condition-keys.md#condition-keys-principaltag")      | {"environment": "production", "team": "data-engineering", "cost-center":"engineering"} |

### Session context claims

These claims provide information about the compute environment and session where the token request originated. AWS AWS STS automatically includes these claims when applicable based on the requesting principal's session context.

| Claim                            | Description                                                                | Maps to Condition Key                                                                                                                                                                                                                                     | Example Value                                                  |
| -------------------------------- | -------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| original_session_exp             | When the original role session credentials will expire (for assumed roles) | N/A                                                                                                                                                                                                                                                       | 2024-01-15T10:00:00Z                                           |
| federated_provider               | The identity provider name for federated sessions                          | [aws:FederatedProvider](reference_policies_condition-keys.md#condition-keys-federatedprovider "reference_policies_condition-keys.md#condition-keys-federatedprovider")                                                                                    | arn:aws:iam::111122223333:oidc-provider/your_oidc_provider     |
| identity_store_user_id           | IAM Identity Center user ID                                                | [identitystore:UserId](reference_policies_condition-keys.md#condition-keys-identity-store-user-id "reference_policies_condition-keys.md#condition-keys-identity-store-user-id")                                                                           | user-abc123def456                                              |
| identity_store_arn               | ARN of the Identity Center identity store                                  | [identitystore:IdentityStoreArn](../../../singlesignon/latest/userguide/condition-context-keys-sts-idc.md#condition-keys-identity-store-arn "../../../singlesignon/latest/userguide/condition-context-keys-sts-idc.md#condition-keys-identity-store-arn") | arn:aws:identitystore::123456789012:identitystore/d-abc1234567 |
| ec2_source_instance_arn          | ARN of the requesting EC2 instance                                         | [ec2:SourceInstanceArn](reference_policies_condition-keys.md#condition-keys-ec2-source-instance-arn "reference_policies_condition-keys.md#condition-keys-ec2-source-instance-arn")                                                                        | arn:aws:ec2:us-east-1:123456789012:instance/i-abc123def456     |
| ec2_instance_source_vpc          | VPC ID where EC2 role credentials were delivered                           | [aws:Ec2InstanceSourceVpc](reference_policies_condition-keys.md#condition-keys-ec2instancesourcevpc "reference_policies_condition-keys.md#condition-keys-ec2instancesourcevpc")                                                                           | vpc-abc123def456                                               |
| ec2_instance_source_private_ipv4 | Private IPv4 address of the EC2 instance                                   | [aws:Ec2InstanceSourcePrivateIPv4](reference_policies_condition-keys.md#condition-keys-ec2instancesourceprivateip4 "reference_policies_condition-keys.md#condition-keys-ec2instancesourceprivateip4")                                                     | 10.0.1.25                                                      |
| ec2_role_delivery                | Instance metadata service version                                          | [ec2:RoleDelivery](reference_policies_condition-keys.md#condition-keys-ec2-role-delivery "reference_policies_condition-keys.md#condition-keys-ec2-role-delivery")                                                                                         | 2                                                              |
| source_identity                  | Source identity set by the principal                                       | [aws:SourceIdentity](reference_policies_condition-keys.md#condition-keys-sourceidentity "reference_policies_condition-keys.md#condition-keys-sourceidentity")                                                                                             | admin-user                                                     |
| lambda_source_function_arn       | ARN of the calling Lambda function                                         | [lambda:SourceFunctionArn](reference_policies_condition-keys.md#condition-keys-lambda-source-function-arn "reference_policies_condition-keys.md#condition-keys-lambda-source-function-arn")                                                               | arn:aws:lambda:us-east-1:123456789012:function:my-function     |
| glue_credential_issuing_service  | AWS Glue service identifier for Glue jobs                                  | [glue:CredentialIssuingService](reference_policies_condition-keys.md#condition-keys-glue-credential-issuing "reference_policies_condition-keys.md#condition-keys-glue-credential-issuing")                                                                | glue.amazonaws.com                                             |

### Request tags

You can add custom claims to tokens by specifying tags in the [GetWebIdentityToken](../../../STS/latest/APIReference/API_GetWebIdentityToken.md "../../../STS/latest/APIReference/API_GetWebIdentityToken.md") API request. These claims appear under the request_tags field in the token and enable you to pass specific information that external services can use for fine-grained authorization decisions. You can specify up to 50 tags per request.

Example request:

```
response = sts_client.get_web_identity_token(
    Audience=['https://api.example.com'],
    SigningAlgorithm='ES384'
    Tags=[
        {'Key': 'team', 'Value': 'data-engineering'},
        {'Key': 'cost-center', 'Value': 'analytics'},
        {'Key': 'environment', 'Value': 'production'}
    ]
)
```

Resulting claims in token:

```
{
  "request_tags": {
    "team": "data-engineering",
    "cost-center": "analytics",
    "environment": "production"
  }
}
```

# AWS Sign-In condition keys reference

This page lists the condition keys you can use in AWS Sign-In resource-based policies and
resource control policies (RCPs), and shows the evaluation phase and action that each key
applies to. Only `signin:PrincipalArn` is specific to AWS Sign-In; the others are
AWS global condition keys. For the global key definitions, see [AWS global condition
context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md").

For the complete list of actions and condition keys in the Service Authorization
Reference, see [Actions, resources,
and condition keys for AWS Sign-In](../../../service-authorization/latest/reference/list_awssignin.md "../../../service-authorization/latest/reference/list_awssignin.md").

## Network-based condition keys

These condition keys check where the request originates from. AWS Sign-In evaluates them
for all AWS Sign-In actions (`signin:Authenticate`,
`signin:AuthorizeOAuth2Access`, and `signin:CreateOAuth2Token`) in
both resource-based policies and RCPs.

Network-based condition keys| Condition key | Operators | Description | Usage rules |
| --- | --- | --- | --- |
| `aws:SourceIp` | `IpAddress`, `NotIpAddress` | Public IP address or CIDR range | Not present when a request uses a VPC endpoint. Use<br>`IfExists` operators when combining with VPC-based<br>conditions in the same statement. |
| `aws:SourceVpc` | `StringEquals`,<br>`StringNotEquals` | VPC ID (`vpc-xxxxxxxx`) | Only present when a request uses a VPC endpoint. Use with<br>`aws:RequestedRegion` to prevent cross-region VPC ID<br>collision. |
| `aws:SourceVpce` | `StringEquals`,<br>`StringNotEquals` | VPC endpoint ID (`vpce-xxxxxxxx`) | Only present when a request uses a VPC endpoint. |
| `aws:VpcSourceIp` | `IpAddress`, `NotIpAddress` | Private IP within the VPC | Always use the `aws:VpcSourceIp` condition key with the<br>`aws:SourceVpc` or `aws:SourceVpce` condition<br>keys. |
| `aws:RequestedRegion` | `StringEquals`,<br>`StringNotEquals` | Target AWS Region code | Recommended when using `aws:SourceVpc` to prevent<br>cross-region VPC ID collision. Multiple Regions can be<br>specified. |

###### Important

A single request contains either `aws:SourceIp` (public network) or
`aws:SourceVpc` (VPC endpoint), not both. When writing deny-unless
policies covering both paths, use `IfExists` operators (for example,
`NotIpAddressIfExists`) or create separate statements.

## Identity-based condition keys

These condition keys check who is making the request. They are available only for the
post-authentication actions (`signin:AuthorizeOAuth2Access` and
`signin:CreateOAuth2Token`), where the principal identity has been
established.

Identity-based condition keys| Condition key | Operators | Description | Examples |
| --- | --- | --- | --- |
| `aws:PrincipalArn` | `ArnEquals`, `ArnLike`,<br>`ArnNotEquals`, `StringEquals`,<br>`StringLike` | ARN of the authenticated IAM principal | `arn:aws:iam::123456789012:user/alice`,<br>`arn:aws:iam::123456789012:role/Admin` |
| `aws:PrincipalAccount` | `StringEquals`,<br>`StringNotEquals` | AWS account ID of the principal | `123456789012` |

## Service-specific condition key: signin:PrincipalArn

The following condition key is specific to AWS Sign-In and is not a global AWS key. It
is available only during pre-authentication evaluation. Use
`signin:PrincipalArn` to identify the principal initiating sign-in before
authentication completes. This is the pre-authentication equivalent of
`aws:PrincipalArn`, which is not available until after authentication.

Operators

ARN operators (`ArnEquals`, `ArnLike`,
`ArnNotEquals`, `ArnNotLike`) and string operators
(`StringEquals`, `StringLike`).

Availability

AWS Sign-In includes this key in the request context during the
pre-authentication phase (the `signin:Authenticate` action). It
is not available for the post-authentication actions
(`signin:AuthorizeOAuth2Access` and
`signin:CreateOAuth2Token`).

Data type

ARN. Use ARN operators rather than string operators.

Value type

Single-valued.

Supported in

Resource-based policies and RCPs.

Use ARN operators to compare values. You can specify the following principal
types:

- AWS account root user (`arn:aws:iam::123456789012:root`)
- IAM user (`arn:aws:iam::123456789012:user/`user-name``)
- IAM role (`arn:aws:iam::123456789012:role/`role-name``)

**Use case:** Exempt an excluded principal identity from
network restrictions, preventing lockout while still enforcing network controls for all
other access attempts.

**Example – Deny pre-authentication access from
unauthorized networks, except for the root user:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": { "AWS": "*" },
      "Action": ["signin:Authenticate"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "signin:PrincipalArn": "arn:aws:iam::123456789012:root"
        },
        "NotIpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        },
        "StringEquals": {
          "aws:ResourceAccount": "123456789012"
        }
      }
    },
    {
      "Effect": "Deny",
      "Principal": { "AWS": "*" },
      "Action": ["signin:CreateOAuth2Token", "signin:AuthorizeOAuth2Access"],
      "Resource": "*",
      "Condition": {
        "ArnNotEquals": {
          "aws:PrincipalArn": "arn:aws:iam::123456789012:root"
        },
        "NotIpAddress": {
          "aws:SourceIp": "203.0.113.0/24"
        },
        "StringEquals": {
          "aws:ResourceAccount": "123456789012"
        }
      }
    }
  ]
}
```

This policy denies console access from outside the `203.0.113.0/24` IP
range, except for the account root user. The pre-authentication statement uses
`signin:PrincipalArn` to exempt the root user before authentication completes.
The post-authentication statement uses `aws:PrincipalArn` to exempt the same
principal after authentication, during OAuth token exchange. See [Policy examples](console-access-control.md#console-access-control-policy-examples "console-access-control.md#console-access-control-policy-examples").

## OAuth condition keys

AWS Sign-In provides OAuth-specific condition keys that you can use in IAM policies
to control how applications obtain OAuth authorization and OAuth tokens. These condition
keys allow you to restrict which OAuth clients can connect, which redirect URIs are
trusted, which OAuth authorization flows are permitted, how OAuth clients authenticate,
and which OAuth tokens can be managed.

OAuth condition keys can be used in IAM identity policies, service control policies
(SCPs), resource control policies (RCPs), and other IAM policy types that support
AWS Sign-In actions.

The following OAuth condition keys are available.

| Condition key                      | Type   | Description                                                                                                                   | Applicable actions                                                                                  |
| ---------------------------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `signin:OAuthClientId`             | String | Restricts authorization to approved OAuth clients.                                                                            | `signin:AuthorizeOAuth2Access`,<br>`signin:CreateOAuth2Token`,<br>`signin:IntrospectOAuth2Token`    |
| `signin:OAuthRedirectUri`          | String | Restricts OAuth authorization to approved redirect URIs.                                                                      | `signin:AuthorizeOAuth2Access`,<br>`signin:CreateOAuth2Token`,<br>`signin:CreateOAuth2PublicClient` |
| `signin:OAuthGrantType`            | String | Controls which OAuth grant types are permitted. Values:<br>`authorization_code`,<br>`refresh_token`,<br>`client_credentials`. | `signin:CreateOAuth2Token`                                                                          |
| `signin:OAuthClientAuthentication` | String | Controls permitted OAuth client authentication methods.                                                                       | `signin:CreateOAuth2Token`                                                                          |
| `signin:OAuthTokenType`            | String | Controls operations performed on OAuth access and refresh tokens.<br>Values: `access_token`,<br>`refresh_token`.              | `signin:RevokeOAuth2Token`,<br>`signin:IntrospectOAuth2Token`                                       |

### signin:OAuthClientId

Use `signin:OAuthClientId` to allow or deny OAuth authorization based
on the registered OAuth client requesting access.

OAuth client IDs are represented as AWS Sign-In Dynamic Client Registration (DCR)
ARNs.

For the non-interactive (client credentials) flow, the implicit client ID is
`arn:aws:signin:::client-credentials/sigv4`.

Applicable actions

- `signin:AuthorizeOAuth2Access`
- `signin:CreateOAuth2Token`
- `signin:IntrospectOAuth2Token`

**Example – Allow only a specific registered OAuth
client:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource": "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com",
      "Condition": {
        "StringEquals": {
          "signin:OAuthClientId": "arn:aws:signin:us-east-1::external-client/dcr/081e0aeb-e779-4dfe-9648-bd5bf6e6afa4"
        }
      }
    }
  ]
}
```

### signin:OAuthRedirectUri

Use `signin:OAuthRedirectUri` to restrict where OAuth authorization
responses are delivered.

This is commonly used to ensure OAuth authorization responses are returned only
to trusted redirect URIs, such as localhost during development.

For the `signin:CreateOAuth2PublicClient` action, this condition key
only applies in VPC endpoint (VPCE) policy evaluation.

Applicable actions

- `signin:AuthorizeOAuth2Access`
- `signin:CreateOAuth2Token`
- `signin:CreateOAuth2PublicClient`

**Example – Allow browser-based authorization only for
localhost redirect URIs and only for interactive OAuth flows:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "signin:AuthorizeOAuth2Access",
        "signin:CreateOAuth2Token"
      ],
      "Resource": "arn:aws:signin:*:*:service-principal/aws-mcp.amazonaws.com",
      "Condition": {
        "StringLike": {
          "signin:OAuthRedirectUri": "http://localhost:*"
        },
        "StringEquals": {
          "signin:OAuthGrantType": [
            "authorization_code",
            "refresh_token"
          ]
        }
      }
    }
  ]
}
```

### signin:OAuthGrantType

Use `signin:OAuthGrantType` to control which OAuth grant types
applications are allowed to use.

Supported values include:

- `authorization_code`
- `refresh_token`
- `client_credentials`

Applicable actions

- `signin:CreateOAuth2Token`

**Example – Allow only browser-based OAuth
authorization while preventing applications from using the Client Credentials
Grant:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "signin:OAuthGrantType": [
            "authorization_code",
            "refresh_token"
          ]
        }
      }
    }
  ]
}
```

### signin:OAuthClientAuthentication

Use `signin:OAuthClientAuthentication` to control which client
authentication methods OAuth clients can use when requesting access tokens.

Currently supported value:

- `none`

Applicable actions

- `signin:CreateOAuth2Token`

**Example – Deny public clients for OAuth
operations:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "signin:CreateOAuth2Token",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "signin:OAuthClientAuthentication": "none"
        }
      }
    }
  ]
}
```

### signin:OAuthTokenType

Use `signin:OAuthTokenType` to control which OAuth token types may be
introspected or revoked.

Supported values include:

- `access_token`
- `refresh_token`

Applicable actions

- `signin:IntrospectOAuth2Token`
- `signin:RevokeOAuth2Token`

**Example – Allow revocation of refresh tokens
only:**

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "signin:RevokeOAuth2Token",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "signin:OAuthTokenType": "refresh_token"
        }
      }
    }
  ]
}
```

## Condition key availability by action

The following table shows which condition keys are available for each action.

| Condition key                      | signin:Authenticate | signin:AuthorizeOAuth2Access | signin:CreateOAuth2Token | signin:RevokeOAuth2Token | signin:IntrospectOAuth2Token | signin:CreateOAuth2PublicClient |
| ---------------------------------- | ------------------- | ---------------------------- | ------------------------ | ------------------------ | ---------------------------- | ------------------------------- |
| `aws:SourceIp`                     | Yes                 | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:SourceVpc`                    | Yes                 | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:SourceVpce`                   | Yes                 | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:VpcSourceIp`                  | Yes                 | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:RequestedRegion`              | Yes                 | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:PrincipalArn`                 | No                  | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `aws:PrincipalAccount`             | No                  | Yes                          | Yes                      | Yes                      | Yes                          | No                              |
| `signin:PrincipalArn`              | Yes                 | No                           | No                       | No                       | No                           | No                              |
| `signin:OAuthClientId`             | No                  | Yes                          | Yes                      | No                       | Yes                          | No                              |
| `signin:OAuthRedirectUri`          | No                  | Yes                          | Yes                      | No                       | No                           | Yes                             |
| `signin:OAuthGrantType`            | No                  | No                           | Yes                      | No                       | No                           | No                              |
| `signin:OAuthClientAuthentication` | No                  | No                           | Yes                      | No                       | No                           | No                              |
| `signin:OAuthTokenType`            | No                  | No                           | No                       | Yes                      | Yes                          | No                              |

###### Note

The `signin:CreateAccount` action is used exclusively in VPC endpoint
policies for Console Private Access and is not available for resource-based
policies or RCPs. No
service-specific condition keys are associated with it. See [Console
Private Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md").

## Related information

- [Controlling console access with resource-based policies and resource control policies](console-access-control.md "console-access-control.md")
- [AWS Management Console
  Private Access](../../../awsconsolehelpdocs/latest/gsg/console-private-access.md "../../../awsconsolehelpdocs/latest/gsg/console-private-access.md")
- [AWS
  global condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md")
- [Actions,
  resources, and condition keys for AWS Sign-In](../../../service-authorization/latest/reference/list_awssignin.md "../../../service-authorization/latest/reference/list_awssignin.md")

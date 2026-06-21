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

| Network-based condition keys | Condition key                        | Operators                         | Description                                                                                                                                    | Usage rules |
| ---------------------------- | ------------------------------------ | --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| `aws:SourceIp`               | `IpAddress`, `NotIpAddress`          | Public IP address or CIDR range   | Not present when a request uses a VPC endpoint. Use<br>`IfExists` operators when combining with VPC-based<br>conditions in the same statement. |
| `aws:SourceVpc`              | `StringEquals`,<br>`StringNotEquals` | VPC ID (`vpc-xxxxxxxx`)           | Only present when a request uses a VPC endpoint. Use with<br>`aws:RequestedRegion` to prevent cross-region VPC ID<br>collision.                |
| `aws:SourceVpce`             | `StringEquals`,<br>`StringNotEquals` | VPC endpoint ID (`vpce-xxxxxxxx`) | Only present when a request uses a VPC endpoint.                                                                                               |
| `aws:VpcSourceIp`            | `IpAddress`, `NotIpAddress`          | Private IP within the VPC         | Always use the `aws:VpcSourceIp` condition key with the<br>`aws:SourceVpc` or `aws:SourceVpce` condition<br>keys.                              |
| `aws:RequestedRegion`        | `StringEquals`,<br>`StringNotEquals` | Target AWS Region code            | Recommended when using `aws:SourceVpc` to prevent<br>cross-region VPC ID collision. Multiple Regions can be<br>specified.                      |

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

| Identity-based condition keys | Condition key                                                              | Operators                              | Description                                                                       | Examples |
| ----------------------------- | -------------------------------------------------------------------------- | -------------------------------------- | --------------------------------------------------------------------------------- | -------- |
| `aws:PrincipalArn`            | `ArnEquals`, `ArnLike`,<br>`ArnNotEquals`, `StringEquals`,<br>`StringLike` | ARN of the authenticated IAM principal | `arn:aws:iam::123456789012:user/alice`,<br>`arn:aws:iam::123456789012:role/Admin` |
| `aws:PrincipalAccount`        | `StringEquals`,<br>`StringNotEquals`                                       | AWS account ID of the principal        | `123456789012`                                                                    |

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

## Condition key availability by action

| Condition key availability by action | Condition key | signin:Authenticate | signin:AuthorizeOAuth2Access | signin:CreateOAuth2Token |
| ------------------------------------ | ------------- | ------------------- | ---------------------------- | ------------------------ |
| `aws:SourceIp`                       | Yes           | Yes                 | Yes                          |
| `aws:SourceVpc`                      | Yes           | Yes                 | Yes                          |
| `aws:SourceVpce`                     | Yes           | Yes                 | Yes                          |
| `aws:VpcSourceIp`                    | Yes           | Yes                 | Yes                          |
| `aws:RequestedRegion`                | Yes           | Yes                 | Yes                          |
| `aws:PrincipalArn`                   | –             | Yes                 | Yes                          |
| `aws:PrincipalAccount`               | –             | Yes                 | Yes                          |
| `signin:PrincipalArn`                | Yes           | –                   | –                            |

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

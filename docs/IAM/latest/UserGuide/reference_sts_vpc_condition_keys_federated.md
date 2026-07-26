# Use VPC condition keys to control federated access

Federated users can assume roles using `AssumeRoleWithSAML` or
`AssumeRoleWithWebIdentity` through a VPC endpoint. When they do, you can
use VPC-specific condition keys in the role's trust policy or in resource control policies
(RCPs) to restrict where these requests can originate. This provides a network-level
boundary in addition to the identity-level controls in the trust policy.

###### Topics

- [How VPC condition keys work for federated requests](#reference_sts_vpc_condition_keys_federated_how "#reference_sts_vpc_condition_keys_federated_how")
- [Example: Restrict OIDC federation to a specific VPC](#reference_sts_vpc_condition_keys_federated_example_oidc_vpc "#reference_sts_vpc_condition_keys_federated_example_oidc_vpc")
- [Example: Restrict SAML federation to a specific VPC endpoint](#reference_sts_vpc_condition_keys_federated_example_saml_vpce "#reference_sts_vpc_condition_keys_federated_example_saml_vpce")
- [Example: Restrict OIDC federation by private IP range within a VPC](#reference_sts_vpc_condition_keys_federated_example_ip "#reference_sts_vpc_condition_keys_federated_example_ip")
- [Example: Restrict SAML federation to multiple VPCs](#reference_sts_vpc_condition_keys_federated_example_saml_multi_vpc "#reference_sts_vpc_condition_keys_federated_example_saml_multi_vpc")
- [Example: Combine VPC and provider-specific conditions](#reference_sts_vpc_condition_keys_federated_example_combined "#reference_sts_vpc_condition_keys_federated_example_combined")
- [Example: Use an RCP to restrict federated access to a specific VPC](#reference_sts_vpc_condition_keys_federated_example_rcp "#reference_sts_vpc_condition_keys_federated_example_rcp")

## How VPC condition keys work for federated requests

The condition keys available in the request context depend on the network path of the
federated request.

VPC condition key availability by network path| Condition key | Through VPC endpoint | Over public internet | Description |
| --- | --- | --- | --- |
| `aws:SourceVpc` | Yes | No | VPC ID that the request traverses |
| `aws:SourceVpcArn` | Yes | No | ARN of the VPC that the request traverses |
| `aws:SourceVpce` | Yes | No | VPC endpoint ID that the request traverses |
| `aws:VpcSourceIp` | Yes | No | Private IP address of the caller within the VPC |
| `aws:SourceIp` | No | Yes | Public IP address of the caller |

If your trust policy uses `aws:SourceVpc`,
`aws:SourceVpcArn`, or `aws:SourceVpce` in an
`Allow` statement and the request does not come through a VPC endpoint,
the condition does not match and AWS implicitly denies the request. This effectively
requires federated requests to traverse the VPC endpoint to succeed.

###### Important

For requests made through a VPC endpoint, `aws:SourceIp` is not
populated. Use `aws:VpcSourceIp` for IP-based restrictions
instead.

We recommend using `aws:SourceVpcArn` instead of
`aws:SourceVpc` in trust policies. VPC IDs are regionally unique but not
globally unique, whereas `aws:SourceVpcArn` includes the Region and account,
providing globally unique identification of the VPC.

###### Note

The audience (`aud`) value in the following OIDC examples uses
`sts.amazonaws.com`, which is the default for Amazon EKS. For other
OIDC providers, replace this with the audience value configured for your application
(for example, a client ID or application URI).

## Example: Restrict OIDC federation to a specific VPC

The following trust policy allows an OIDC provider to assume the role only when the
request originates from a specific VPC through a VPC endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOIDCFromVpc",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "idp.example.com:aud": "sts.amazonaws.com",
                    "aws:SourceVpcArn": "arn:aws:ec2:us-west-2:111122223333:vpc/vpc-111bbb22"
                }
            }
        }
    ]
}
```

AWS implicitly denies requests from outside the specified VPC because the
`aws:SourceVpcArn` condition does not match. No explicit deny statement is
needed.

## Example: Restrict SAML federation to a specific VPC endpoint

The following trust policy allows a SAML provider to assume the role only when the
request comes through a specific VPC endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSAMLFromVpce",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::111122223333:saml-provider/ExampleProvider"
            },
            "Action": "sts:AssumeRoleWithSAML",
            "Condition": {
                "StringEquals": {
                    "SAML:aud": "https://signin.aws.amazon.com/saml",
                    "aws:SourceVpce": "vpce-0abcdef1234567890"
                }
            }
        }
    ]
}
```

Using `aws:SourceVpce` instead of `aws:SourceVpc` provides more
granular control when you have multiple VPC endpoints in the same VPC and want to
restrict access to a specific endpoint.

## Example: Restrict OIDC federation by private IP range within a VPC

The following trust policy restricts federation to requests originating from a specific
subnet within the VPC. Use `aws:VpcSourceIp` for IP-based restrictions on
requests made through a VPC endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOIDCFromSubnet",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "idp.example.com:aud": "sts.amazonaws.com",
                    "aws:SourceVpcArn": "arn:aws:ec2:us-west-2:111122223333:vpc/vpc-111bbb22"
                },
                "IpAddress": {
                    "aws:VpcSourceIp": "10.0.1.0/24"
                }
            }
        }
    ]
}
```

###### Important

Do not use `aws:SourceIp` with private IP ranges for requests through a
VPC endpoint. The `aws:SourceIp` key is not available for VPC endpoint
requests. Use `aws:VpcSourceIp` instead.

## Example: Restrict SAML federation to multiple VPCs

The following trust policy allows a SAML provider to assume the role from any of
several VPCs. This is useful when your organization has multiple VPCs across different
environments or Regions that need federated access to the same role.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSAMLFromMultipleVpcs",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::111122223333:saml-provider/ExampleProvider"
            },
            "Action": "sts:AssumeRoleWithSAML",
            "Condition": {
                "StringEquals": {
                    "SAML:aud": "https://signin.aws.amazon.com/saml",
                    "aws:SourceVpcArn": [
                        "arn:aws:ec2:us-west-2:111122223333:vpc/vpc-111aaa11",
                        "arn:aws:ec2:us-east-1:111122223333:vpc/vpc-222bbb22"
                    ]
                }
            }
        }
    ]
}
```

## Example: Combine VPC and provider-specific conditions

You can combine VPC condition keys with provider-specific conditions such as audience
(`aud`) and subject (`sub`) for fine-grained access control.
The following trust policy restricts role assumption to a specific federated user and
requires the request to originate from a specific VPC.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOIDCUserFromVpc",
            "Effect": "Allow",
            "Principal": {
                "Federated": "arn:aws:iam::111122223333:oidc-provider/idp.example.com"
            },
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Condition": {
                "StringEquals": {
                    "idp.example.com:aud": "sts.amazonaws.com",
                    "idp.example.com:sub": "user123",
                    "aws:SourceVpcArn": "arn:aws:ec2:us-west-2:111122223333:vpc/vpc-111bbb22"
                }
            }
        }
    ]
}
```

This combines identity-level controls (restricting to a specific federated user) with
network-level controls (restricting to a specific VPC), providing defense in
depth.

## Example: Use an RCP to restrict federated access to a specific VPC

The following resource control policy (RCP) denies `AssumeRoleWithSAML` and
`AssumeRoleWithWebIdentity` requests unless they originate from a
specific VPC. Unlike trust policies that apply per-role, a resource control policy (RCP)
applies across all roles in the target accounts. This provides a centralized network
boundary.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DenyFederatedAccessOutsideVpc",
            "Effect": "Deny",
            "Principal": "*",
            "Action": [
                "sts:AssumeRoleWithWebIdentity",
                "sts:AssumeRoleWithSAML"
            ],
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:SourceVpcArn": "arn:aws:ec2:us-west-2:111122223333:vpc/vpc-111bbb22"
                },
                "Null": {
                    "aws:SourceVpcArn": "false"
                }
            }
        }
    ]
}
```

The `Null` condition ensures the deny only applies when
`aws:SourceVpcArn` is present in the request context (that is, the
request came through a VPC endpoint but from the wrong VPC). Without it, requests over
the public internet (where `aws:SourceVpcArn` is absent) would also be denied
by `StringNotEquals`. If you remove the `Null` check, the deny
also applies to requests that do not traverse any VPC endpoint, including requests over
the public internet. We recommend testing thoroughly before removing the
`Null` check in production environments.

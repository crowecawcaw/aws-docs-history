# Control access to AWS STS with VPC endpoint policies

When you create an interface VPC endpoint for AWS Security Token Service (AWS STS), you can attach an
endpoint policy. The policy controls which principals can use the endpoint and which AWS STS
actions they can perform. If you don't attach a policy, the endpoint uses the default policy
that allows unrestricted access to all AWS STS actions for all principals.

VPC endpoint policies don't grant permissions on their own. They act as an additional
boundary that works alongside other policies. Both the endpoint policy and the caller's
applicable policies must allow a request for it to succeed.

For more information about VPC endpoint policies, see [Control access to VPC endpoints
using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User
Guide_.

###### Topics

- [Default VPC endpoint policy](#reference_sts_vpc_endpoint_policies_default "#reference_sts_vpc_endpoint_policies_default")
- [Important considerations for AWS STS VPC endpoint policies](#reference_sts_vpc_endpoint_policies_considerations "#reference_sts_vpc_endpoint_policies_considerations")
- [Condition keys available for AWS STS VPC endpoint policies](#reference_sts_vpc_endpoint_policies_condition_keys "#reference_sts_vpc_endpoint_policies_condition_keys")
- [Example: Allow all AWS STS actions for your organization](#reference_sts_vpc_endpoint_policies_example_org "#reference_sts_vpc_endpoint_policies_example_org")
- [Example: Allow all AWS STS actions for specific accounts](#reference_sts_vpc_endpoint_policies_example_accounts "#reference_sts_vpc_endpoint_policies_example_accounts")
- [Example: Restrict to specific AWS STS actions](#reference_sts_vpc_endpoint_policies_example_actions "#reference_sts_vpc_endpoint_policies_example_actions")
- [Example: Deny non-organization access while allowing federation](#reference_sts_vpc_endpoint_policies_example_deny "#reference_sts_vpc_endpoint_policies_example_deny")

## Default VPC endpoint policy

If you don't attach a custom policy when you create the endpoint, AWS attaches the
following default policy. This policy allows unrestricted access to the endpoint.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        }
    ]
}
```

To limit access to the endpoint, attach a custom endpoint policy.

## Important considerations for AWS STS VPC endpoint policies

AWS STS handles requests from two fundamentally different types of callers. Your VPC
endpoint policy must account for both types to avoid unintentionally blocking legitimate
requests.

**Authenticated AWS principals**

IAM users and IAM roles that sign requests with AWS Signature Version 4
(SigV4). These callers have standard condition keys such as
`aws:PrincipalOrgID`, `aws:PrincipalAccount`, and
`aws:PrincipalArn` available in the request context.

**Federated callers**

SAML 2.0 and OpenID Connect (OIDC) principals that call
`AssumeRoleWithSAML` or
`AssumeRoleWithWebIdentity`. These callers authenticate with
SAML assertions or JSON Web Tokens (JWTs), not SigV4 signatures. Because
they have no AWS identity at the time of the request, the request context
does not include principal-based condition keys such as
`aws:PrincipalOrgID`, `aws:PrincipalAccount`, and
`aws:PrincipalArn`.

###### Important

If your VPC endpoint policy relies solely on `aws:PrincipalOrgID` to
allow access, federated `AssumeRoleWithSAML` and
`AssumeRoleWithWebIdentity` calls are implicitly denied because the
condition key is absent for non-AWS principals.

### How AWS STS evaluates VPC endpoint policies for federated callers

When a federated caller invokes `AssumeRoleWithSAML` or
`AssumeRoleWithWebIdentity` through a VPC endpoint, the following
applies:

- The caller is not an AWS principal. Condition keys such as
  `aws:PrincipalOrgID`, `aws:PrincipalAccount`, and
  `aws:PrincipalArn` are not available in the request
  context.
- Federated callers do not have the condition key
  `aws:PrincipalIsAWSService` in the request context.
- The role being assumed is an AWS resource. Resource-based condition keys
  such as `aws:ResourceOrgID` and
  `aws:ResourceAccount` are available and refer to the target
  role.
- The role's trust policy remains the primary authorization gate for
  federated access. The VPC endpoint policy provides an additional
  network-level boundary.

We recommend using `aws:ResourceOrgID` or `aws:ResourceAccount` when
writing VPC endpoint policy statements that must apply to federated callers, because
these callers do not have principal-based condition keys available.

## Condition keys available for AWS STS VPC endpoint policies

The following table shows commonly used condition keys and their availability in the
request context for each caller type when making requests through an AWS STS VPC endpoint.
Additional condition keys are available beyond those listed here.

Condition key availability by caller type| Condition key | Authenticated AWS principals | Federated callers | Description |
| --- | --- | --- | --- |
| `aws:PrincipalOrgID` | Yes | No | The organization ID of the calling principal |
| `aws:PrincipalAccount` | Yes | No | The account ID of the calling principal |
| `aws:PrincipalArn` | Yes | No | The ARN of the calling principal |
| `aws:PrincipalIsAWSService` | Yes (evaluates to false) | No (key is absent) | Whether the caller is an AWS service principal |
| `aws:ResourceOrgID` | Yes | Yes | The organization ID of the account that owns the requested resource |
| `aws:ResourceAccount` | Yes | Yes | The account ID that owns the requested resource |

###### Note

For authenticated AWS principals (IAM users and roles),
`aws:PrincipalIsAWSService` is present in the request context and
evaluates to false. For federated callers, this key is absent from the request
context entirely. A condition that checks `"Bool":
 {"aws:PrincipalIsAWSService": "false"}` does not match federated callers
because the key is not present.

## Example: Allow all AWS STS actions for your organization

The following endpoint policy restricts your AWS STS VPC endpoint to your organization
while supporting federated access. It allows all AWS STS actions for authenticated
principals in your organization and separately permits federated callers to assume roles
within your organization. Federated callers (`AssumeRoleWithSAML` and
`AssumeRoleWithWebIdentity`) require a separate statement because they
don't have an `aws:PrincipalOrgID` in the request context.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowOrganizationPrincipals",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "sts:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-exampleorgid"
                }
            }
        },
        {
            "Sid": "AllowFederatedAssumeRole",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "sts:AssumeRoleWithSAML",
                "sts:AssumeRoleWithWebIdentity"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-exampleorgid"
                }
            }
        }
    ]
}
```

The first statement uses `"Principal": {"AWS": "*"}` with
`aws:PrincipalOrgID` to allow authenticated AWS principals from
your organization. The second statement uses `"Principal": "*"` to match
federated callers and restricts the target role to your organization using
`aws:ResourceOrgID`. The role's trust policy remains the primary control
for which federated identities can assume which roles.

For more information about implementing network perimeter controls, see [Building a data perimeter on AWS](../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md "../../../whitepapers/latest/building-a-data-perimeter-on-aws/building-a-data-perimeter-on-aws.md") and the [data perimeter
policy examples](https://github.com/aws-samples/data-perimeter-policy-examples "https://github.com/aws-samples/data-perimeter-policy-examples") on the GitHub website.

## Example: Allow all AWS STS actions for specific accounts

The following endpoint policy allows all AWS STS actions for principals in specific
accounts. Use this policy when your accounts are not part of an
organization. Federated callers are allowed in a separate statement because they don't
have an `aws:PrincipalAccount` in the request context.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowSpecificAccountPrincipals",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "sts:*",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalAccount": [
                        "111122223333",
                        "444455556666"
                    ]
                }
            }
        },
        {
            "Sid": "AllowFederatedAssumeRole",
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "sts:AssumeRoleWithSAML",
                "sts:AssumeRoleWithWebIdentity"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceAccount": [
                        "111122223333",
                        "444455556666"
                    ]
                }
            }
        }
    ]
}
```

The first statement uses `"Principal": {"AWS": "*"}` with
`aws:PrincipalAccount` to allow authenticated AWS principals from
the specified accounts. The second statement uses `"Principal": "*"` to match
federated callers and restricts the target role to the same accounts using
`aws:ResourceAccount`. The role's trust policy remains the primary control
for which federated identities can assume which roles.

## Example: Restrict to specific AWS STS actions

The following endpoint policy allows only `AssumeRole` for authenticated
principals and `AssumeRoleWithSAML` for federated callers, both scoped to
roles in your organization.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAssumeRoleByOrgPrincipals",
            "Effect": "Allow",
            "Principal": {
                "AWS": "*"
            },
            "Action": "sts:AssumeRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:PrincipalOrgID": "o-exampleorgid"
                }
            }
        },
        {
            "Sid": "AllowSAMLFederation",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "sts:AssumeRoleWithSAML",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceOrgID": "o-exampleorgid"
                }
            }
        }
    ]
}
```

This policy blocks other AWS STS actions such as `GetCallerIdentity`,
`GetSessionToken`, and `AssumeRoleWithWebIdentity` through
this endpoint. Adjust the `Action` elements to match your
requirements.

## Example: Deny non-organization access while allowing federation

The following endpoint policy uses an explicit deny to block authenticated principals
outside your organization, while preserving access for federated callers. This approach
starts with a broad allow and adds a targeted deny statement.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowAll",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "*",
            "Resource": "*"
        },
        {
            "Sid": "DenyNonOrgPrincipals",
            "Effect": "Deny",
            "Principal": {
                "AWS": "*"
            },
            "Action": "sts:*",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "aws:PrincipalOrgID": "o-exampleorgid"
                }
            }
        }
    ]
}
```

The deny statement uses `"Principal": {"AWS": "*"}`, which scopes it to
authenticated AWS principals only. Federated callers (SAML and OIDC) are not AWS
principals and are not matched by this `Principal` element, so the deny does
not apply to them. This approach avoids the need for complex `Null` or
`Bool` conditions to carve out exceptions for federated callers.

###### Note

The first statement allows all actions for all principals. The deny in the second
statement takes precedence for authenticated AWS principals outside your
organization. Federated callers are allowed by the first statement and are unaffected
by the deny because the `Principal` element in the deny statement does not
match them.

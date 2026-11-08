

# Example IAM policies for AWS RAM
<a name="security-iam-policies-examples"></a>

This topic includes examples of IAM policies for AWS RAM that demonstrate sharing specific resources and resource types, restricting sharing, and controlling the use of managed permissions.

When you write policies for AWS RAM, keep the following in mind:
+ A `CreateResourceShare`, `AssociateResourceShare`, or `DisassociateResourceShare` request can include several resources and principals. AWS RAM evaluates a separate [request context](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_evaluation-logic_policy-eval-reqcontext.html) for each resource and each principal.
+ We recommend the multivalued condition keys `ram:RequestedResourceArns`, `ram:RequestedResourceTypes`, `ram:RequestedPrincipals`, `ram:RequestedPermissionArns`, and `ram:RequestedPermissionResourceTypes`. Each one contains the values of its kind in the request, and it is present in every request context for the action. One condition therefore evaluates the whole request at once.
+ The older single-valued keys (`ram:ResourceArn`, `ram:RequestedResourceType`, `ram:Principal`, `ram:PermissionArn`, and `ram:PermissionResourceType`) are present only in the request context for the one resource, principal, or permission that they describe. For example, `ram:RequestedResourceType` isn't present when a principal is evaluated, so policies that use these keys need extra `Null` conditions.
+ Use the multivalued keys with the `ForAnyValue` or `ForAllValues` set operators. If a request has no values of a kind, for example a request that adds only principals, the key isn't present. A `ForAnyValue` condition then doesn't match, and a `ForAllValues` condition matches. Most examples in this topic pair an `Allow` statement with a `Deny` statement that uses `ForAnyValue`, so that requests without the key are judged by the `Allow` statement alone.
+ If your users add tags when they create a resource share, also grant `ram:TagResource`. The example policies don't include it.

For the list of condition keys, see [Condition](security-iam-policies.md#iam-policies-condition).

**Topics**
+ [Allow sharing of specific resources](#owner-share-specific-resources)
+ [Allow sharing of specific resource types](#owner-share-resource-types)
+ [Restrict sharing with external AWS accounts](#control-access-owner-external)
+ [Allow sharing with specific principals](#owner-share-specific-principals)
+ [Allow only managed permissions from a trusted account](#control-cmp-usage)
+ [Restrict template parameter values](#control-template-parameter-values)
+ [Allow sharing of customer managed permissions](#allow-share-cmp)

## Example 1: Allow sharing of specific resources
<a name="owner-share-specific-resources"></a>

In the following policy, principals can create resource shares and add to them, but AWS RAM denies the request if it adds any resource other than the specified Amazon Route 53 resolver rule. A request that adds only principals has no resources, so the `Deny` statement doesn't apply to it.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:ArnNotEquals": {
                    "ram:RequestedResourceArns": "arn:aws:route53resolver:us-west-2:123456789012:resolver-rule/rslvr-rr-5328a0899aexample"
                }
            }
        }
    ]
}
```

## Example 2: Allow sharing of specific resource types
<a name="owner-share-resource-types"></a>

The following policy denies a request that adds any resource that isn't a Amazon Route 53 resolver rule. Requests that add only principals are still allowed.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotEquals": {
                    "ram:RequestedResourceTypes": "route53resolver:ResolverRule"
                }
            }
        }
    ]
}
```

Specify resource types in the format shown in the list of [shareable resource types](shareable.md), for example `ec2:Subnet`.

## Example 3: Restrict sharing with external AWS accounts
<a name="control-access-owner-external"></a>

The following policy keeps resource shares inside your organization in AWS Organizations:
+ It denies `CreateResourceShare` unless the request sets `allowExternalPrincipals` to `false`. If the request omits the parameter, it defaults to `true`, so the policy uses `BoolIfExists`.
+ It denies `UpdateResourceShare` requests that set `allowExternalPrincipals` to `true`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:UpdateResourceShare"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": "ram:CreateResourceShare",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "ram:RequestedAllowsExternalPrincipals": "true"
                }
            }
        },
        {
            "Effect": "Deny",
            "Action": "ram:UpdateResourceShare",
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "ram:RequestedAllowsExternalPrincipals": "true"
                }
            }
        }
    ]
}
```

## Example 4: Allow sharing with specific principals
<a name="owner-share-specific-principals"></a>

The following policy denies a request that adds any principal other than the two specified AWS accounts. `ram:RequestedPrincipals` contains the principals exactly as the request specifies them, so list each principal in the form that your users pass it, such as an account ID or an organizational unit ARN.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringNotEquals": {
                    "ram:RequestedPrincipals": [
                        "111122223333",
                        "444455556666"
                    ]
                }
            }
        }
    ]
}
```

## Example 5: Allow only managed permissions from a trusted account
<a name="control-cmp-usage"></a>

You can use the multivalued `ram:RequestedPermissionArns` condition key to control which managed permissions principals can associate with resource shares. For example, a central team in account `444455556666` shares approved customer managed permissions with the accounts in your organization. The following policy denies associating any managed permission other than those customer managed permissions and AWS managed permissions. The `ForAnyValue` operator makes the statement apply if any managed permission in the request doesn't match one of the ARN patterns. Use it together with the policies that grant these actions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceSharePermission",
                "ram:ReplacePermissionAssociations"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:ArnNotLike": {
                    "ram:RequestedPermissionArns": [
                        "arn:aws:ram:*:444455556666:permission/*",
                        "arn:aws:ram::aws:permission/*"
                    ]
                }
            }
        }
    ]
}
```

If a `create-resource-share` request doesn't specify a managed permission, the key contains the default AWS managed permissions for the resource types in the request, which match the second pattern.

## Example 6: Restrict template parameter values
<a name="control-template-parameter-values"></a>

You can use the `ram:PermissionTemplateParameter/{{parameter-name}}` condition key to control the values that principals supply for a parameterized managed permission. For an example policy, see [Control template parameter values with IAM policies](parameterized-managed-permissions.md#template-iam-condition-keys).

## Example 7: Allow sharing of customer managed permissions
<a name="allow-share-cmp"></a>

To share a customer managed permission, a principal needs the usual permissions to create and update resource shares. It also needs permission for two more actions on the customer managed permission:
+ `ram:PutCustomerManagedPermissionPolicy`
+ `ram:DeleteCustomerManagedPermissionPolicy`

When you add a customer managed permission to a resource share or remove it, AWS RAM updates the resource-based policy of the customer managed permission on your behalf, and it might need either action. These are permission-only actions. You can't call them directly.

The following policy lets principals share the customer managed permissions in account `123456789012`. The first statement grants the actions that create and update resource shares. The second statement grants the two actions on the account's customer managed permissions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ram:CreateResourceShare",
                "ram:AssociateResourceShare",
                "ram:DisassociateResourceShare"
            ],
            "Resource": [
                "arn:aws:ram:*:123456789012:resource-share/*",
                "arn:aws:ram:*:123456789012:permission/*",
                "arn:aws:ram::aws:permission/AWSRAMDefaultPermissionRAMCustomerManagedPermission"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ram:PutCustomerManagedPermissionPolicy",
                "ram:DeleteCustomerManagedPermissionPolicy"
            ],
            "Resource": "arn:aws:ram:*:123456789012:permission/*"
        }
    ]
}
```
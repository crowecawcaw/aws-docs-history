# Tag policy syntax and

examples

This page describes tag policy syntax and provides examples.

## Tag policy syntax

A tag policy is a plaintext file that is structured according to the rules of [JSON](http://json.org "http://json.org"). The syntax for tag policies follows the syntax
for management policy types. For a complete discussion of that syntax, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic focuses on
applying that general syntax to the specific requirements of the tag policy type.

The following tag policy shows basic tag policy syntax:

```
{
    "tags": {
        "costcenter": {
            "tag_key": {
                "@@assign": "CostCenter"
            },
            "tag_value": {
                "@@assign": [
                    "100",
                    "200",
                    "300*"
                ]
            },
            "enforced_for": {
                "@@assign": [
                    "secretsmanager:ALL_SUPPORTED"
                ]
            }
        }
    }
}

```

Tag policy syntax includes the following elements:

- The `tags` field key name. Tag policies always start with this
  fixed key name. It's the top line in the example policy above.
- A _policy key_ that uniquely identifies the policy
  statement. It must match the value for the _tag key_, except
  for the case treatment. The policy value is case sensitive.

In this example, `costcenter` is the policy key.

- At least one _tag key_ that specifies the allowed tag key
  with the capitalization that you want resources to be compliant with. If case
  treatment isn't defined, lowercase is the default case treatment for tag keys.
  The value for the tag key must match the value for the policy key. But since the
  policy key value is case insensitive, the capitalization can be different.

In this example, `CostCenter` is the tag key. This is the case
treatment that is required for compliance with the tag policy. Resources with
alternate case treatment for this tag key are noncompliant with the tag policy.

You can define multiple tag keys in a tag policy.

- (Optional) A list of one or more acceptable _tag values_
  for the tag key. If the tag policy doesn't specify a tag value for a tag key,
  any value (including no value at all) is considered compliant.

In this example, acceptable values for the `CostCenter` tag key are
`100`, `200`, and `300*`.

- (Optional) An `enforced_for` option that indicates whether to
  prevent any noncompliant tagging operations on specified services and resources.
  In the console, this is the **Prevent noncompliant operations for this
  tag** option in the visual editor for creating tag policies. The
  default setting for this option is null.

The example tag policy specifies that the `CostCenter` tag passed on all AWS Secrets Manager resources must be compliant with this policy.

###### Warning

You should only change this option from the default if you are experienced
with using tag policies. Otherwise, you could prevent users in your
organization's accounts from creating the resources they need.

- _Operators_ that specify how the tag policy merges with
  other tag policies within the organization tree to create an account's [effective tag
  policy](orgs_manage_policies_effective.md "orgs_manage_policies_effective.md"). In this example, `@@assign` is used to assign
  strings to `tag_key`, `tag_value`, and
  `enforced_for`. For more information about operators, see [Inheritance operators](policy-operators.md "policy-operators.md").
- You can use the `*` wildcard in
  tag values.
  - You can use only one wildcard per tag value. For example,
    `*@example.com` is allowed, but `*@*.com` is
    not.
  - You can use the `ALL_SUPPORTED` wildcard in the `enforced_for` field with some services
    to enable enforcement for all resources for that
    service. For a list of services and resource types that support
    `enforced_for`, see [Services and resource
    types that support enforcement](orgs_manage_policies_supported-resources-enforcement.md "orgs_manage_policies_supported-resources-enforcement.md").
  - You can't use a wildcard to specify all services or to specify a
    resource for all services.

## Tag policy examples

The example [tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md") that
follow are for information purposes only.

###### Note

Before you attempt to use these example tag policies in your organization, note
the following:

- Make sure that you've followed the [recommended workflow](orgs_manage_policies_tag-policies-getting-started.md "orgs_manage_policies_tag-policies-getting-started.md") for getting started with tag
  policies.
- You should carefully review and customize these tag policies for your
  unique requirements.
- All characters in your tag policy are subject to a [maximum size](orgs_reference_limits.md#min-max-values "orgs_reference_limits.md#min-max-values"). The examples in this guide
  show tag policies formatted with extra white space to improve their
  readability. However, to save space if your policy size approaches the
  maximum size, you can delete any white space. Examples of white space
  include space characters and line breaks that are outside quotation
  marks.
- Untagged resources don't appear as noncompliant in results.

## Example 1: Define organization-wide tag

key case

The following example shows a tag policy that only defines two tag keys and the
capitalization that you want accounts in your organization to standardize on.

**Policy A – organization root tag policy**

```
{
    "tags": {
        "CostCenter": {
            "tag_key": {
                "@@assign": "CostCenter",
                "@@operators_allowed_for_child_policies": ["@@none"]
            }
        },
        "Project": {
            "tag_key": {
                "@@assign": "Project",
                "@@operators_allowed_for_child_policies": ["@@none"]
            }
        }
    }
}
```

This tag policy defines two tag keys: `CostCenter` and
`Project`. Attaching this tag policy to the organization root has the
following effects:

- All accounts in your organization inherit this tag policy.
- All accounts in your organization must use the defined case treatment for
  compliance. Resources with `CostCenter` and `Project` tags
  are compliant. Resources with alternate case treatment for the tag key (for
  example, `costcenter`, `Costcenter`, or
  `COSTCENTER`) are noncompliant.
- The `@@operators_allowed_for_child_policies": ["@@none"]` lines
  lock down the tag keys. Tag policies that are attached lower in the organization
  tree (child policies) can't use value-setting operators to change the tag key,
  including its case treatment.
- As with all tag policies, untagged resources or tags that aren't defined in
  the tag policy aren't evaluated for compliance with the tag policy.

AWS recommends that you use this example as a guide in creating a similar tag policy
for tag keys that you want to use. Attach it to the organization root. Then create a tag
policy similar to the next example, which only defines the acceptable values for the
defined tag keys.

### Next step: Define values

Assume that you attached the previous tag policy to the organization root. Next,
you can create a tag policy like the following and attach it to an account. This
policy defines acceptable values for the `CostCenter` and
`Project` tag keys.

**Policy B – account tag policy**

```
{
    "tags": {
        "CostCenter": {
            "tag_value": {
                "@@assign": [
                    "Production",
                    "Test"
                ]
            }
        },
        "Project": {
            "tag_value": {
                "@@assign": [
                    "A",
                    "B"
                ]
            }
        }
    }
}
```

If you attach Policy A to the organization root and Policy B to an account, the
policies combine to create the following effective tag policy for the
account:

**Policy A + Policy B = effective tag policy for
account**

```
{
    "tags": {
        "Project": {
            "tag_value": [
                "A",
                "B"
            ],
            "tag_key": "Project"
        },
        "CostCenter": {
            "tag_value": [
                "Production",
                "Test"
            ],
            "tag_key": "CostCenter"
        }
    }
}
```

For more information about policy inheritance, including examples of how the
inheritance operators work and example effective tag policies, see [Understanding management policy
inheritance](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md").

## Example 2: Prevent use of a tag

key

To prevent the use of a tag key, you can attach a tag policy like the following to an
organization entity.

This example policy specifies that no values are acceptable for the `Color`
tag key. It also specifies that no [operators](policy-operators.md "policy-operators.md") are allowed in child tag policies.
Therefore, any `Color` tags on resources in affected accounts are considered
non-compliant. However, the `enforced_for` option actually prevents affected
accounts from tagging **_only_** Amazon DynamoDB tables with the `Color` tag.

```
{
    "tags": {
        "Color": {
            "tag_key": {
                "@@operators_allowed_for_child_policies": [
                    "@@none"
                ],
                "@@assign": "Color"
            },
            "tag_value": {
                "@@operators_allowed_for_child_policies": [
                    "@@none"
                ],
                "@@assign": []
            },
            "enforced_for": {
                "@@assign": [
                    "dynamodb:table"
                ]
            }
        }
    }
}
```

## Example 3: Specify a tag policy for all supported resource types

of a specific AWS service

To specify a tag policy for all supported resource types of a specific AWS service,
you use the `ALL_SUPPORTED` wildcard.

This policy uses the `ALL_SUPPORTED` wildcard to specify that all Amazon EC2 instances with the tag key `Environment`
can only have a tag value of `Prod` or `Non-prod`. This wildcard provides an effective, single-line alternative to
listing each Amazon EC2 instance individually. For a list of services and resource types that support the
`ALL_SUPPORTED` wildcard, see [Services and resource
types that support enforcement](orgs_manage_policies_supported-resources-enforcement.md "orgs_manage_policies_supported-resources-enforcement.md").

```
{
    "tags": {
        "Environment": {
            "tag_key": {
                "@@assign": "Environment",
                "@@operators_allowed_for_child_policies": ["@@none"]
            },
            "tag_value": {
                "@@assign": [
                    "Prod",
                    "Non-prod"
                ],
                "@@operators_allowed_for_child_policies": ["@@none"]
            },
            "enforced_for": {
                "@@assign": [
                    "ec2:ALL_SUPPORTED"
                ]
            }
        }
    }
}
```

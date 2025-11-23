# Upgrade rollout policy syntax and

examples

An upgrade rollout policy defines how AWS services apply automatic upgrades across your
resources. Understanding the policy syntax helps you create effective policies that match
your organization's upgrade requirements.

###### Topics

- [Considerations](#orgs_manage_policies_upgrade_syntax_considerations "#orgs_manage_policies_upgrade_syntax_considerations")
- [Basic policy
  structure](#orgs_manage_policies_upgrade_syntax_structure "#orgs_manage_policies_upgrade_syntax_structure")
- [Policy
  components](#orgs_manage_policies_upgrade_syntax_components "#orgs_manage_policies_upgrade_syntax_components")
- [Upgrade rollout policy
  examples](#orgs_manage_policies_upgrade_syntax_examples "#orgs_manage_policies_upgrade_syntax_examples")

## Considerations

When implementing upgrade rollout policies, consider these important factors:

- Policy names must be unique within your organization and should be clear and
  descriptive. Choose names that reflect the policy's purpose and scope. For more
  information, see [Optimize
  operational efficiency](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_optimize "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_optimize").
- Testing is crucial before broad deployment. Validate new policies in
  non-production environments first and expand gradually to ensure desired
  behavior. For more information, see [Start small and
  scale gradually](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_scale "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_scale").
- Policy changes may take several hours to propagate across your organization.
  Plan your implementations accordingly and ensure proper monitoring is in place.
  For more information, see [Monitor and
  communicate changes](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_monitor "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_monitor").
- JSON formatting must be valid and stay within the maximum policy size of 5,120
  bytes. Keep policy structures as simple as possible while meeting your
  requirements.
- Regular policy reviews help maintain effectiveness. Schedule periodic
  evaluations of your policies to ensure they continue to meet your organizational
  needs. For more information, see [Establish review
  processes](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_review "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_review").
- Resources without an assigned upgrade order default to the "Second" order.
  Consider explicitly setting upgrade orders for critical resources rather than
  relying on defaults. For more information, see [Validate policy
  changes effectively](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_validate "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_validate").
- Manual upgrades take precedence over policy-defined upgrade orders. Ensure
  your change management processes account for both automatic and manual upgrade
  scenarios. For more information, see [Establish review
  processes](orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_review "orgs_manage_policies_upgrade_best_practices.md#orgs_manage_policies_upgrade_best_practices_review").

###### Note

When implementing tag-based upgrade rollout policies from your management account,
be aware that the management account cannot directly view or access resource-level
tags in member accounts. We recommend establishing a process where member accounts
apply consistent resource tags, and then create organization-level policies that
reference these tags. This ensures proper coordination between resource-level
tagging and organizational policy enforcement. You can also use [Tag policies](orgs_manage_policies_tag-policies.md "orgs_manage_policies_tag-policies.md") to help maintain consistent
tags when resources are tagged across your organization.

## Basic policy

structure

Upgrade rollout policies use a JSON structure that includes the following main
elements:

- Policy metadata (such as version information)
- Resource targeting rules
- Upgrade order specifications
- Optional exception messages
- Service-specific attributes

The following example shows a basic upgrade rollout policy structure:

```
{
   "upgrade_rollout":{
      "default":{
         "patch_order":{
            "@@assign":"last"
         }
      },
      "tags":{
         "devtag":{
            "tag_values":{
               "tag1":{
                  "patch_order":{
                     "@@assign":"first"
                  }
               },
               "tag2":{
                  "patch_order":{
                     "@@assign":"second"
                  }
               },
               "tag3":{
                  "patch_order":{
                     "@@assign":"last"
                  }
               }
            }
         }
      }
   }
}
```

## Policy

components

An upgrade rollout policy consists of two key components that work together to control
how upgrades are applied across your resources. These components include configuration
options for both default behaviors and tag-based overrides. Understanding how these
components interact helps you create effective policies that match your organizational
needs.

### Default

patch order setup

When you create an upgrade rollout policy without specifying any resource-specific
overrides, all resources default to a base upgrade order. You can set this default
using the "default" field in your policy. Resources without explicit upgrade order
assignments through tags will follow this default order.

###### Note

The console experience today requires a default order to be specified.

The following example shows how to set all resources to receive upgrades last by
default, unless overridden by tags. This approach is useful when you want to ensure
most resources update later in the upgrade cycle:

```
"upgrade_rollout": {
    "default": {
        "patch_order": "last"
    }
}
```

### Resource level

overriding via Tags

You can override the default upgrade order for specific resources using tags. This
allows you to create granular control over which resources receive upgrades in which
order. For example, you can assign different upgrade orders based on your
environment types, development stages, or workload criticality.

The following example shows how to configure development resources to receive
upgrades first and production resources to receive them last. This configuration
ensures your development environments can validate upgrades before they reach
production:

```
"upgrade_rollout": {
    "tags": {
        "environment": {
            "tag_values": {
                "development": {
                    "patch_order": "first"
                },
                "production": {
                    "patch_order": "last"
                }
            }
        }
    }
}
```

## Upgrade rollout policy

examples

Here are common upgrade rollout policy scenarios:

### Example 1:

Development environment first

This example shows how to configure resources in your development environment to
receive upgrades first. By targeting resources with the "development" environment
tag, you ensure your development environments are the first to receive and validate
new upgrades. This pattern helps identify potential issues before upgrades reach
more critical environments:

```
{
    "tags": {
        "environment": {
            "tag_values": {
                "development": {
                    "upgrade_order": "first"
                }
            }
        }
    }
}
```

### Example 2: Production

environment last

This example demonstrates how to ensure your production environments receive
upgrades last. By explicitly setting production-tagged resources to the last upgrade
order, you maintain stability in your production environment while allowing adequate
testing in pre-production environments. This approach is particularly useful for
organizations with strict change management requirements:

```
{
    "tags": {
        "environment": {
            "tag_values": {
                "production": {
                    "upgrade_order": "last"
                }
            }
        }
    }
}
```

### Example 3: Multiple

upgrade orders using tags

The following example demonstrates how to use a single tag key with different
values to specify all three upgrade orders. This approach is useful when you want to
manage upgrade orders through a single tagging scheme:

```
{
   "upgrade_rollout":{
      "default":{
         "patch_order":{
            "@@assign":"last"
         }
      },
      "tags":{
         "devtag":{
            "tag_values":{
               "tag1":{
                  "patch_order":{
                     "@@assign":"first"
                  }
               },
               "tag2":{
                  "patch_order":{
                     "@@assign":"second"
                  }
               },
               "tag3":{
                  "patch_order":{
                     "@@assign":"last"
                  }
               }
            }
         }
      }
   }
}
```

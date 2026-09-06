

# Security Hub policy syntax and examples
<a name="orgs_manage_policies_security_hub_syntax"></a>

Security Hub policies follow a standardized JSON syntax that defines how Security Hub is enabled and configured across your organization. Understanding the policy structure helps you create effective policies for your security requirements.

## Considerations
<a name="security-hub-policy-considerations"></a>

Before creating Security Hub policies, understand these key points about policy syntax:
+ Both `enable_in_regions` and `disable_in_regions` lists are required in the policy, though they can be empty.
+ When processing effective policies, `disable_in_regions` takes precedence over `enable_in_regions`.
+ Child policies can modify parent policies using inheritance operators unless explicitly restricted.
+ The `ALL_SUPPORTED` designation includes both current and future Regions.
+ Region names must be valid and available in Security Hub.
+ The `features` map is optional and is available only in commercial AWS Regions (Regions other than the AWS GovCloud (US) Regions and the China Regions). It is not available in the AWS GovCloud (US) Regions or China Regions.
+ Both `enable_in_regions` and `disable_in_regions` lists within a feature are required, though they can be empty.
+ When processing effective policies, `disable_in_regions` takes precedence over `enable_in_regions` for a feature, the same as for the top-level lists.
+ A feature is configured only in Regions where Security Hub is enabled by the same effective policy. Disabling Security Hub in a Region also disables its features in that Region.
+ Regions that appear in neither the `enable_in_regions` nor the `disable_in_regions` list for a feature are left unmanaged by the policy.
+ When the `features` map, or a feature within it, is omitted, that feature is left unmanaged by the policy.

## Basic policy structure
<a name="security-hub-basic-structure"></a>

A Security Hub policy uses this basic structure:

```
{
  "securityhub": {
    "enable_in_regions": {
      "@@append": ["ALL_SUPPORTED"],
      "@@operators_allowed_for_child_policies": ["@@all"]
    },
    "disable_in_regions": {
      "@@append": [],
      "@@operators_allowed_for_child_policies": ["@@all"]
    }
  }
}
```

A Security Hub policy can also include an optional `features` map to manage opt-in Security Hub features, such as network scanning, across your organization. The `features` map is available only in commercial AWS Regions.

```
{
  "securityhub": {
    "enable_in_regions": {
      "@@assign": ["ALL_SUPPORTED"],
      "@@operators_allowed_for_child_policies": ["@@all"]
    },
    "disable_in_regions": {
      "@@assign": [],
      "@@operators_allowed_for_child_policies": ["@@all"]
    },
    "features": {
      "network_scanning": {
        "enable_in_regions": {
          "@@assign": ["us-east-1", "us-west-2"],
          "@@operators_allowed_for_child_policies": ["@@all"]
        },
        "disable_in_regions": {
          "@@assign": [],
          "@@operators_allowed_for_child_policies": ["@@all"]
        }
      }
    }
  }
}
```

## Policy components
<a name="security-hub-policy-components"></a>

Security Hub policies contain these key components:

`securityhub`  
The top-level container for policy settings.  
Required for all Security Hub policies.

`enable_in_regions`  
List of Regions where Security Hub should be enabled.  
Can contain specific Region names or `ALL_SUPPORTED`.  
Required field but can be empty.  
When using `ALL_SUPPORTED`, includes future Regions.

`disable_in_regions`  
List of Regions where Security Hub should be disabled.  
Can contain specific Region names or `ALL_SUPPORTED`.  
Required field but can be empty.  
Takes precedence over `enable_in_regions` when Regions appear in both lists.

Inheritance operators  
@@assign - Overwrites inherited values.  
@@append - Adds new values to existing ones.  
@@remove - Removes specific values from inherited settings.

`features`  
The container for opt-in Security Hub feature settings.  
Optional, and available only in commercial AWS Regions.  
When omitted, all features are left unmanaged by the policy.  
Each feature is configured by its own child block, such as `network_scanning`.

`network_scanning`  
Controls the network scanning feature within the `features` map.  
Optional. When omitted, network scanning is left unmanaged by the policy.  
Contains its own `enable_in_regions` and `disable_in_regions` lists.

`enable_in_regions` (within `network_scanning`)  
List of Regions where network scanning should be enabled.  
Can contain specific Region names or `ALL_SUPPORTED`.  
Required field but can be empty.  
When using `ALL_SUPPORTED`, includes all Regions where Security Hub is enabled by this policy.  
Network scanning is enabled only in Regions where Security Hub is also enabled by this policy.

`disable_in_regions` (within `network_scanning`)  
List of Regions where network scanning should be disabled.  
Can contain specific Region names or `ALL_SUPPORTED`.  
Required field but can be empty.  
Takes precedence over `enable_in_regions` when Regions appear in both lists.

## Security Hub policy examples
<a name="security-hub-policy-examples"></a>

The following examples demonstrate common Security Hub policy configurations. 

The example below enables Security Hub in all current and future Regions. By using `ALL_SUPPORTED` in the `enable_in_regions` list and leaving `disable_in_regions` empty, this policy ensures comprehensive security coverage as new Regions become available.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            
         ]
      }
   }
}
```

This example disables Security Hub in all Regions including any future Regions since `disable_in_regions` list takes precedence over `enable_in_regions`.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      }
   }
}
```

The following example demonstrates how child policies can modify parent policy settings using inheritance operators. This approach allows for granular control while maintaining the overall policy structure. The child policy adds a new Region to `enable_in_regions` and removes a Region from `disable_in_regions`.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@append":[
            "eu-central-1"
         ]
      },
      "disable_in_regions":{
         "@@remove":[
            "us-west-2"
         ]
      }
   }
}
```

This example shows how to enable Security Hub in multiple specific Regions without using `ALL_SUPPORTED`. This provides precise control over which Regions have Security Hub enabled, while leaving unspecified Regions unmanaged by the policy.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2",
            "eu-west-1",
            "ap-southeast-1"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            
         ]
      }
   }
}
```

The following example demonstrates how to handle regional compliance requirements by enabling Security Hub in most Regions while explicitly disabling it in specific locations. The `disable_in_regions` list takes precedence, ensuring Security Hub remains disabled in those Regions regardless of other policy settings.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[
            "ap-east-1",
            "me-south-1"
         ]
      }
   }
}
```

The following example enables Security Hub in two Regions and enables network scanning in those same Regions. The `features` map is available only in commercial AWS Regions.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      },
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@assign":[
                  "us-east-1",
                  "us-west-2"
               ]
            },
            "disable_in_regions":{
               "@@assign":[

               ]
            }
         }
      }
   }
}
```

This example enables Security Hub in three Regions but enables network scanning in only two of them. In `eu-west-1`, Security Hub is enabled while network scanning is left unmanaged by the policy because that Region is in neither feature list.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2",
            "eu-west-1"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      },
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@assign":[
                  "us-east-1",
                  "us-west-2"
               ]
            },
            "disable_in_regions":{
               "@@assign":[

               ]
            }
         }
      }
   }
}
```

The following example enables network scanning in `us-east-1` and disables it in `us-west-2`. Because `disable_in_regions` takes precedence, network scanning remains disabled in `us-west-2` even when a Region appears in both lists.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "us-east-1",
            "us-west-2"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      },
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@assign":[
                  "us-east-1"
               ]
            },
            "disable_in_regions":{
               "@@assign":[
                  "us-west-2"
               ]
            }
         }
      }
   }
}
```

This example keeps Security Hub enabled in all current and future Regions while disabling network scanning in all of them, since the `disable_in_regions` list takes precedence.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      },
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@assign":[

               ]
            },
            "disable_in_regions":{
               "@@assign":[
                  "ALL_SUPPORTED"
               ]
            }
         }
      }
   }
}
```

This example enables Security Hub in all current and future Regions and leaves network scanning unmanaged by the policy by using empty feature lists. This has the same effect as omitting the `features` map.

```
{
   "securityhub":{
      "enable_in_regions":{
         "@@assign":[
            "ALL_SUPPORTED"
         ]
      },
      "disable_in_regions":{
         "@@assign":[

         ]
      },
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@assign":[

               ]
            },
            "disable_in_regions":{
               "@@assign":[

               ]
            }
         }
      }
   }
}
```

The following example demonstrates how a child policy can extend a parent policy's network scanning Regions using inheritance operators. The child policy adds a Region to the inherited `enable_in_regions` list with `@@append`, the same way inheritance works on the top-level Region lists.

```
{
   "securityhub":{
      "features":{
         "network_scanning":{
            "enable_in_regions":{
               "@@append":[
                  "us-west-2"
               ]
            }
         }
      }
   }
}
```
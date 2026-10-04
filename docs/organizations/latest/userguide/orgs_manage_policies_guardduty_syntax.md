

# Amazon GuardDuty policy syntax and examples
<a name="orgs_manage_policies_guardduty_syntax"></a>

Amazon GuardDuty policies follow a standardized JSON syntax that defines how GuardDuty is enabled and configured across your organization. A GuardDuty policy is a plaintext file structured according to the rules of JSON, and its syntax follows the syntax for all declarative policy types. For a complete discussion of that general syntax, see [Understanding declarative policy inheritance](orgs_manage_policies_inheritance_mgmt.md). This topic applies that general syntax to the specific requirements of the GuardDuty policy type: it defines which features GuardDuty automatically enables, and in which Regions, for the organizational entities the policy is attached to.

## Key considerations
<a name="guardduty-policy-considerations"></a>

Before creating GuardDuty policies, understand these key points about policy syntax:
+ GuardDuty uses a default with Regional override model. The optional `default` block defines the baseline feature configuration applied to every Region where GuardDuty is available. Optional Region-specific blocks, keyed by Region name, apply to that Region only.
+ A policy must contain at least one block (a `default`, a Region-specific block, or both).
+ A Region-specific block fully replaces the default for that Region; it is not merged with it. List every feature you want in that Region, because any feature omitted from a Region block is not inherited from `default`.
+ A Region that has neither a `default` block nor a Region-specific block is unmanaged. The policy neither enables nor disables GuardDuty there, and existing settings are left unchanged.
+ Within any block, `foundational` must be enabled if any other feature in that same block is enabled.
+ Each feature is set with a status of `enabled` or `disabled`. The `runtime_monitoring` feature additionally supports an `additional_configuration` object for its agent-management sub-features.
+ Child policies set values using the `@@assign` inheritance operator. The authored form (for example `{"status": {"@@assign": "enabled"}}`) is distinct from the effective form returned by `DescribeEffectivePolicy` (which resolves to plain `{"status": "enabled"}`).
+ Region names must be valid AWS Regions where GuardDuty is supported. A feature listed in a Region where it is not available is ignored for that Region.

## Basic policy structure
<a name="guardduty-basic-structure"></a>

A GuardDuty policy uses this basic structure:

```
{
  "guardduty": {
    "enablement": {
      "default": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        }
      },
      "us-east-1": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "runtime_monitoring": {
          "status": { "@@assign": "enabled" },
          "additional_configuration": {
            "ec2_agent_management": {
              "status": { "@@assign": "enabled" }
            }
          }
        }
      }
    }
  }
}
```

## Policy components
<a name="guardduty-policy-components"></a>

GuardDuty policies contain these key components:

`guardduty`  
The top-level key for GuardDuty policy documents.  
Required for all GuardDuty policies.

`enablement`  
Defines how GuardDuty is enabled across the organization.  
Maps `default` or a Region name to a feature block.  
Must contain at least one block.

`default`  
Optional baseline feature block applied to every Region where GuardDuty is available.

`<region-name>` (for example `us-east-1`)  
Optional Region-specific feature block that fully replaces the default for that Region.

`status`  
Set on each feature to `enabled` or `disabled`.

`additional_configuration`  
Optional object on `runtime_monitoring` for its agent-management sub-features, each with its own `status`.

## Features
<a name="guardduty-features"></a>

The following table lists the features you can manage in a GuardDuty policy. Each feature is optional, and foundational threat detection must be enabled whenever any other feature in the same block is enabled.


**GuardDuty policy features**  

| Feature | Key | Sub-features | 
| --- | --- | --- | 
| Foundational threat detection | foundational | None | 
| S3 protection | s3\_data\_events | None | 
| EKS audit log monitoring | eks\_audit\_logs | None | 
| EBS malware protection | ebs\_malware\_protection | None | 
| RDS login activity monitoring | rds\_login\_events | None | 
| Lambda network activity monitoring | lambda\_network\_logs | None | 
| Runtime monitoring | runtime\_monitoring | additional\_configuration: eks\_addon\_management, ec2\_agent\_management, ecs\_fargate\_agent\_management | 
| GuardDuty AI protection | ai\_protection | None | 

**Note**  
Feature availability varies by Region and partition. A feature listed in a Region where it is not yet available has no effect in that Region.

## Amazon GuardDuty policy examples
<a name="guardduty-policy-examples"></a>

The following examples demonstrate common GuardDuty policy configurations.

### Example 1: Enable GuardDuty organization-wide
<a name="guardduty-example-org-wide"></a>

The following policy enables foundational threat detection and S3 protection in every Region for all accounts, using a single `default` block. When attached to the organization root, all accounts automatically enable these GuardDuty features, and their findings are available to the GuardDuty delegated administrator. Any new account joining the organization inherits enablement automatically.

```
{
  "guardduty": {
    "enablement": {
      "default": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "s3_data_events": {
          "status": { "@@assign": "enabled" }
        }
      }
    }
  }
}
```

### Example 2: Override a specific Region
<a name="guardduty-example-region-override"></a>

The following policy enables a broad feature set everywhere through `default`, but overrides `us-east-1` to disable EBS malware protection there. Because a Region block fully replaces the default, the `us-east-1` block re-lists every feature it wants active in that Region.

```
{
  "guardduty": {
    "enablement": {
      "default": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "s3_data_events": {
          "status": { "@@assign": "enabled" }
        },
        "ebs_malware_protection": {
          "status": { "@@assign": "enabled" }
        }
      },
      "us-east-1": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "s3_data_events": {
          "status": { "@@assign": "enabled" }
        },
        "ebs_malware_protection": {
          "status": { "@@assign": "disabled" }
        }
      }
    }
  }
}
```

When attached to an OU, all accounts in it get the default feature set in every Region except `us-east-1`, where EBS malware protection is disabled. Accounts outside the OU are unaffected.

### Example 3: Enable runtime monitoring with sub-features
<a name="guardduty-example-runtime-monitoring"></a>

The `runtime_monitoring` feature supports an `additional_configuration` object for its agent-management sub-features. The following policy enables runtime monitoring with automated agent management for EKS, EC2, and Fargate.

```
{
  "guardduty": {
    "enablement": {
      "default": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "runtime_monitoring": {
          "status": { "@@assign": "enabled" },
          "additional_configuration": {
            "eks_addon_management": {
              "status": { "@@assign": "enabled" }
            },
            "ec2_agent_management": {
              "status": { "@@assign": "enabled" }
            },
            "ecs_fargate_agent_management": {
              "status": { "@@assign": "enabled" }
            }
          }
        }
      }
    }
  }
}
```

When attached, all accounts in scope enable runtime monitoring and have GuardDuty manage the runtime agents automatically across the supported compute types.

### Example 4: Manage specific Regions only, with no default
<a name="guardduty-example-regions-only"></a>

The `default` block is optional. The following policy omits it and configures only two Regions: `us-east-1` and `eu-west-1`. Every other Region is left unmanaged; the policy neither enables nor disables GuardDuty there, and existing settings in those Regions are unchanged.

```
{
  "guardduty": {
    "enablement": {
      "us-east-1": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        },
        "s3_data_events": {
          "status": { "@@assign": "enabled" }
        }
      },
      "eu-west-1": {
        "foundational": {
          "status": { "@@assign": "enabled" }
        }
      }
    }
  }
}
```

Because there is no default, only the two named Regions are managed. Use this pattern when you want a policy to govern GuardDuty in a specific set of Regions without asserting any baseline for the rest.
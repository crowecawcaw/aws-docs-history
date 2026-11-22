

# Security Hub CSPM policy syntax and examples

Security Hub CSPM policies follow a standardized JSON syntax that defines how Security Hub CSPM and its security standards and controls are enabled and configured across your organization. Understanding the policy structure helps you create effective policies for your security requirements.

A Security Hub CSPM policy is a plaintext file structured according to the rules of JSON. Its syntax follows the syntax for all management policy types. For a complete discussion of that general syntax, see [Understanding declarative policy inheritance](orgs_manage_policies_inheritance_mgmt.md). This topic applies that syntax to the specific requirements of the Security Hub CSPM policy type.

## Considerations
<a name="security-hub-cspm-policy-considerations"></a>

Before creating Security Hub CSPM policies, understand these key points about policy syntax:
+ Both `enable_in_regions` and `disable_in_regions` lists under the `cspm_enablement` key are required in the policy, though they can be empty.
+ When processing effective policies, `disable_in_regions` takes precedence over `enable_in_regions`.
+ Regions that appear in neither the `enable_in_regions` nor the `disable_in_regions` list are left unmanaged by the policy.
+ Child policies can modify parent policies using inheritance operators unless explicitly restricted.
+ The `ALL_SUPPORTED` designation includes both current and future Regions for Security Hub CSPM.
+ Region names must be valid and available in Security Hub CSPM.
+ The `cspm_standards_controls` object contains a complete specification of how Security Hub CSPM standards and controls are enabled or disabled and how custom control parameters are set across the Regions and accounts in scope of the policy.
+ The configurations in the `cspm_standards_controls` object only apply in Regions where Security Hub CSPM is enabled by the same effective policy. Disabling Security Hub CSPM in a Region also disables standards and controls in that Region.
+ By default, the Security Hub CSPM standards and control configurations under the `default` block apply to all Regions where Security Hub CSPM is set to be enabled by the policy.
+ Each policy requires a non-empty `cspm_standards_controls` object containing a `default` object with a `default_control_association_status` key set to either `ENABLED` or `DISABLED`.
+ The `default_control_association_status` determines the default enablement status of controls for standards enabled by the effective policy.
+ When processing control status, `disabled_controls` takes precedence over `enabled_controls`. Both `disabled_controls` and `enabled_controls` take precedence over `default_control_association_status`.
+ The `cspm_standards_controls` block also optionally supports Region-specific configuration overrides when you don't want a uniform Security Hub CSPM configuration across your members' in-scope Regions. Region-specific configurations completely replace the settings in the `default` block for the target Region or Regions.
+ Security Hub CSPM Organizations policies are available only in the commercial AWS Regions, the AWS GovCloud (US) Regions, and China Regions.
+ Security Hub CSPM Organizations policies do not support configuring multi-cloud standards and controls (for example, Azure).
+ Security Hub CSPM Organizations policies do not support configuring service-managed standards and controls (for example, the AWS Control Tower service-managed standard).
+ A policy can't list `enabled_controls` when `default_control_association_status` is `ENABLED`, or `disabled_controls` when it is `DISABLED`.
+ Each control in `enabled_controls` and `disabled_controls` must belong to a standard that the same policy enables.
+ Deprecated control IDs are accepted and have no effect.

## Basic policy structure
<a name="security-hub-cspm-basic-structure"></a>

A Security Hub CSPM policy uses this basic structure:

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"],
        "@@operators_allowed_for_child_policies": ["@@all"]
      },
      "disable_in_regions": {
        "@@assign": [],
        "@@operators_allowed_for_child_policies": ["@@all"]
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"],
          "@@operators_allowed_for_child_policies": ["@@all"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED",
            "@@operators_allowed_for_child_policies": ["@@all"]
          }
        }
      }
    }
  }
}
```

The preceding policy enables Security Hub CSPM in all current and future Regions where Security Hub CSPM is available, and enables the AWS Foundational Security Best Practices v1.0.0 standard and all of its associated controls in those Regions.

## Policy components
<a name="security-hub-cspm-policy-components"></a>

Security Hub CSPM policies contain these key components:

Inheritance operators  
`@@assign` overwrites inherited values. `@@append` adds new values to existing ones. `@@remove` removes specific values from inherited settings.

`securityhub_cspm`  
The top-level container for policy settings. Required for all Security Hub CSPM policies.

`cspm_enablement`  
Intermediary field for specifying which Regions are enabled or disabled by the policy. Contains `enable_in_regions` and `disable_in_regions` keys. Regions omitted from both are left ungoverned. Required field.

`enable_in_regions`  
List of Regions where Security Hub CSPM should be enabled. Can contain specific Region names or `ALL_SUPPORTED`. Required field but accepts an empty list. When using `ALL_SUPPORTED`, includes future Regions.

`disable_in_regions`  
List of Regions where Security Hub CSPM should be disabled. Can contain specific Region names or `ALL_SUPPORTED`. Required field but accepts an empty list. Takes precedence over `enable_in_regions` when Regions appear in both lists.

`cspm_standards_controls`  
Intermediary field for specifying the Security Hub CSPM resource configurations for in-scope enabled Regions. Contains a complete specification of enabled or disabled standards and controls, and custom control parameters. Required field.

`default`  
Container for the default Security Hub CSPM standards and control configuration applied to all policy-enabled Regions defined in the `cspm_enablement` object. Can be overridden per Region by a sibling Region key (for example, `us-east-1`) under the `cspm_standards_controls` object. Required field.

`Region name` (for example, `us-east-1`)  
Optional Region-specific configuration block with the same structure as `default`. Fully replaces the `default` configuration for that Region. Has no effect in a Region where the policy doesn't enable Security Hub CSPM.

`enabled_standards`  
List of standards to enable. Standards omitted from this list are governed as disabled. Pertains only to Security Hub CSPM managed standards for AWS (excludes multi-cloud standards such as Azure). Optional. If omitted, all standards are governed as disabled.

`controls_configuration`  
Intermediary field for specifying configurations pertaining to controls enablement. Required field.

`custom_control_parameters`  
Intermediary field for specifying custom control parameters. Contains a mapping of SecurityControlIds to a parameters object that maps ParameterNames to ParameterValues. Optional. If omitted, customizable control parameters are set to their defaults.

`default_control_association_status`  
The default standards control association enablement status for the controls associated with the standards specified in `enabled_standards`. Also dictates the AutoEnableControls Hub setting. Valid values are `ENABLED` or `DISABLED`. Required field.

`enabled_controls`  
List of controls for Security Hub CSPM to enable (by SecurityControlId). Takes precedence over `default_control_association_status`.  
Only allowed when `default_control_association_status` is `DISABLED`.

`disabled_controls`  
List of controls for Security Hub CSPM to disable (by SecurityControlId). Takes precedence over `default_control_association_status`. Takes precedence over `enabled_controls` when controls appear in both lists.  
Only allowed when `default_control_association_status` is `ENABLED`.

## Security Hub CSPM policy examples
<a name="security-hub-cspm-policy-examples"></a>

The following examples demonstrate common Security Hub CSPM policy configurations.

This first example enables Security Hub CSPM in all current and future Regions. By using `ALL_SUPPORTED` in the `enable_in_regions` list and leaving `disable_in_regions` empty, this policy ensures comprehensive security coverage as new Regions become available. In each Region where Security Hub CSPM is enabled, the AWS Foundational Security Best Practices standard and all of its regionally available controls are also enabled.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"]
      },
      "disable_in_regions": {
        "@@assign": []
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          }
        }
      }
    }
  }
}
```

This example disables Security Hub CSPM in all Regions, including any future Regions, because the `disable_in_regions` list takes precedence over `enable_in_regions`. The configurations under `default` in `cspm_standards_controls` do not apply to any Region, because no Region has Security Hub CSPM enabled by the policy.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["us-east-1", "us-west-2"]
      },
      "disable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"]
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          }
        }
      }
    }
  }
}
```

This example enables Security Hub CSPM in multiple specific Regions without using `ALL_SUPPORTED`. This provides precise control over which Regions have Security Hub CSPM enabled, while leaving unspecified Regions unmanaged by the policy. In this case, four Regions (us-east-1, us-east-2, us-west-1, and eu-central-1) have the AWS Foundational Security Best Practices standard enabled, and all other Regions are left ungoverned.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["us-east-1", "us-east-2", "us-west-1", "eu-central-1"]
      },
      "disable_in_regions": {
        "@@assign": []
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          }
        }
      }
    }
  }
}
```

This example shows how to enable specific controls in Security Hub CSPM. This provides precise control over which controls are enabled and generate Security Hub CSPM findings. In this example, Security Hub CSPM is enabled in us-east-1, us-east-2, us-west-1, and eu-central-1. The `default_control_association_status` is set to `DISABLED`, and only the controls ACM.1, Account.1, Config.1, IAM.7, and EC2.20 are enabled.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["us-east-1", "us-east-2", "us-west-1", "eu-central-1"]
      },
      "disable_in_regions": {
        "@@assign": []
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "enabled_controls": {
            "@@assign": ["ACM.1", "Account.1", "Config.1", "IAM.7", "EC2.20"]
          },
          "default_control_association_status": {
            "@@assign": "DISABLED"
          }
        }
      }
    }
  }
}
```

The following example enables Security Hub CSPM in all current and future Regions. By default, every Region has only the AWS Foundational Security Best Practices v1.0.0 standard and all its controls enabled. However, in us-east-1 and us-west-2, both the AWS Foundational Security Best Practices v1.0.0 standard and the NIST Special Publication 800-171 Revision 2 standard are enabled, with all of their regionally available controls except ACM.1, which is explicitly disabled.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"]
      },
      "disable_in_regions": {
        "@@assign": []
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          }
        }
      },
      "us-east-1": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0", "nist-800-171/v/2.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          },
          "disabled_controls": {
            "@@assign": ["ACM.1"]
          }
        }
      },
      "us-west-2": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0", "nist-800-171/v/2.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          },
          "disabled_controls": {
            "@@assign": ["ACM.1"]
          }
        }
      }
    }
  }
}
```

This example uses the `custom_control_parameters` field to set custom control parameters in the Security Hub CSPM policy. By using `ALL_SUPPORTED`, this policy ensures comprehensive security coverage as new Regions become available. In each Region where Security Hub CSPM is enabled, the AWS Foundational Security Best Practices standard and all of its regionally available controls are enabled.

In addition, the policy sets the `daysToExpiration` customizable parameter for the ACM.1 control to 30 days instead of its default value. Parameters that aren't listed use their default values.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"]
      },
      "disable_in_regions": {
        "@@assign": []
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED"
          }
        },
        "custom_control_parameters": {
          "ACM.1": {
            "daysToExpiration": {
              "@@assign": 30
            }
          }
        }
      }
    }
  }
}
```

The following example enables Security Hub CSPM in most Regions and explicitly disables it in two Regions. Because `disable_in_regions` takes precedence, Security Hub CSPM stays disabled in those Regions regardless of other policy settings.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": { "@@assign": ["ALL_SUPPORTED"] },
      "disable_in_regions": { "@@assign": ["ap-east-1", "me-south-1"] }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": { "@@assign": "ENABLED" }
        }
      }
    }
  }
}
```

Security Hub CSPM policies don't have a home Region. The following example enables the AWS Foundational Security Best Practices standard in every Region, but disables controls that evaluate global IAM resources in every Region except `us-east-1`. This avoids duplicate findings for the same global resources.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": { "@@assign": ["ALL_SUPPORTED"] },
      "disable_in_regions": { "@@assign": [] }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": { "@@assign": "ENABLED" },
          "disabled_controls": {
            "@@assign": ["IAM.1", "IAM.2", "IAM.3", "IAM.4", "IAM.6"]
          }
        }
      },
      "us-east-1": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"]
        },
        "controls_configuration": {
          "default_control_association_status": { "@@assign": "ENABLED" }
        }
      }
    }
  }
}
```

The following example shows how a child policy can extend a parent policy with inheritance operators. The parent policy, attached to the organization root, sets the baseline and prevents child policies from disabling Security Hub CSPM in any Region.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": {
        "@@assign": ["ALL_SUPPORTED"],
        "@@operators_allowed_for_child_policies": ["@@none"]
      },
      "disable_in_regions": {
        "@@assign": [],
        "@@operators_allowed_for_child_policies": ["@@none"]
      }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@assign": ["aws-foundational-security-best-practices/v/1.0.0"],
          "@@operators_allowed_for_child_policies": ["@@append"]
        },
        "controls_configuration": {
          "default_control_association_status": {
            "@@assign": "ENABLED",
            "@@operators_allowed_for_child_policies": ["@@none"]
          }
        }
      }
    }
  }
}
```

The child policy, attached to an OU for payment workloads, adds the PCI DSS v4.0.1 standard with `@@append`. Accounts in that OU run both standards. All other accounts run only the baseline standard.

```json
{
  "securityhub_cspm": {
    "cspm_enablement": {
      "enable_in_regions": { "@@append": [] },
      "disable_in_regions": { "@@append": [] }
    },
    "cspm_standards_controls": {
      "default": {
        "enabled_standards": {
          "@@append": ["pci-dss/v/4.0.1"]
        },
        "controls_configuration": {
          "default_control_association_status": { "@@assign": "ENABLED" }
        }
      }
    }
  }
}
```
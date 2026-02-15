# Amazon Inspector policy syntax and

examples

Amazon Inspector policies follow a standardized JSON syntax that defines how Amazon Inspector is enabled and
configured across your organization. An Amazon Inspector policy is a JSON document structured according to the AWS Organizations management-policy syntax. It defines which organizational entities will have Amazon Inspector automatically enabled.

## Basic policy structure

An Amazon Inspector policy uses this basic structure:

```
{
    "inspector": {
        "enablement": {
            "ec2_scanning": {
                "enable_in_regions": {
                    "@@assign": ["us-east-1", "us-west-2"]
                },
                "disable_in_regions": {
                    "@@assign": ["eu-west-1"]
                }
            }
        }
    }
}
```

## Policy components

Amazon Inspector policies contain these key components:

`inspector`

The top-level key for Amazon Inspector policy documents, which is required for all Amazon Inspector policies.

`enablement`

Defines how Amazon Inspector is enabled across the organization, and contains scan type configurations.

`Regions (Array of Strings)`

Specifies the Regions where Amazon Inspector should be auto-enabled.

## Amazon Inspector policy examples

The following examples demonstrate common Amazon Inspector policy configurations.

### Example 1 – Enable Amazon Inspector organization-wide

The following example enables Amazon Inspector in `us-east-1` and `us-west-2` for all accounts in the organization root.

Create a file `inspector-policy-enable.json`:

```
{
  "inspector": {
    "enablement": {
      "lambda_standard_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "us-east-1",
            "us-west-2"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        },
        "lambda_code_scanning": {
          "enable_in_regions": {
            "@@assign": [
              "us-east-1",
              "us-west-2"
            ]
          },
          "disable_in_regions": {
            "@@assign": [
              "eu-west-1"
            ]
          }
        }
      },
      "ec2_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "us-east-1",
            "us-west-2"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        }
      },
      "ecr_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "us-east-1",
            "us-west-2"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        }
      },
      "code_repository_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "us-east-1",
            "us-west-2"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        }
      }
    }
  }
}
```

When attached to the root, all accounts in the organization automatically enable Amazon Inspector, and their scan findings are available to the Amazon Inspector delegated administrator.

Create and attach the policy:

```
POLICY_ID=$(aws organizations create-policy \
  --content file://inspector-policy-enable.json \
  --name InspectorOrgPolicy \
  --type INSPECTOR_POLICY \
  --description "Inspector organization policy to enable all resources in IAD and PDX." \
  --query 'Policy.PolicySummary.Id' \
  --output text)
aws organizations attach-policy --policy-id $POLICY_ID --target-id <root-id>
```

Any new account joining the organization automatically inherits enablement.

If detached, existing accounts remain enabled, but future accounts are not auto-enabled:

```
aws organizations detach-policy --policy-id $POLICY_ID --target-id <root-id>
```

### Example 2 – Enable Amazon Inspector for a specific OU

Create a file `inspector-policy-eu-west-1.json`:

```
{
  "inspector": {
    "enablement": {
      "lambda_standard_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-2"
          ]
        },
        "lambda_code_scanning": {
          "enable_in_regions": {
            "@@assign": [
              "eu-west-1"
            ]
          },
          "disable_in_regions": {
            "@@assign": [
              "eu-west-2"
            ]
          }
        }
      },
      "ec2_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-2"
          ]
        }
      },
      "ecr_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-2"
          ]
        }
      },
      "code_repository_scanning": {
        "enable_in_regions": {
          "@@assign": [
            "eu-west-1"
          ]
        },
        "disable_in_regions": {
          "@@assign": [
            "eu-west-2"
          ]
        }
      }
    }
  }
}
```

Attach this to an OU to ensure all production accounts in `eu-west-1` will have Amazon Inspector enabled and linked to the Amazon Inspector delegated administrator:

```
aws organizations update-policy --policy-id $POLICY_ID --content file://inspector-policy-eu-west-1.json --description "Inspector organization policy - Enable all (eu-west-1)"
aws organizations attach-policy --policy-id $POLICY_ID --target-id ou-aaaa-12345678
```

Accounts outside the OU are unaffected.

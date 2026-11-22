

# Manage Networking Flexible Cost Allocation within an AWS Organization

If you are using AWS Organizations to manage accounts in your organization, you can use an [AWS Organizations declarative policy](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) to configure Networking Flexible Cost Allocation (FCA) for member accounts in the organization. For more information about the FCA service attribute in Amazon EC2 policies, see [Supported attributes for Amazon EC2 policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ec2.html#orgs_manage_policies_ec2-supported-controls) in the *AWS Organizations User Guide*.

## How a declarative policy affects Networking Flexible Cost Allocation for member accounts
<a name="networking-flex-cost-allocation-orgs-effects"></a>
+ The delegated administrator can specify FCA configuration for one or more supported network resource types, including `natgw`, `ec2`, and `pcx`.
+ For organization members whose effective Amazon EC2 policy contains FCA configuration, a flexible cost allocation policy is created for each configured network resource type, along with an account scope association to the flexible cost allocation policy. These flexible cost allocation policies and associations are owned by the member account but managed by the declarative policy.
+ Organization members whose effective Amazon EC2 policy contains a FCA configuration lose access to create, modify, and delete flexible cost allocation policies, along with access to associate and disassociate flexible cost allocation policies. Member accounts can continue to view flexible cost allocation policies and associations in their account, including ones managed by the declarative policy.
+ After the declarative-policy-managed FCA policies and associations become effective, metering rules start applying to the matching network resources for the managed network resource types. If member accounts have existing flexible cost allocation policies and associations that they created before the declarative policy for any network resource type, these policies and associations aren't effective while the member's effective Amazon EC2 policy contains flexible cost allocation configuration.

## Updates to the flexible cost allocation configuration in a member's effective EC2 policy
<a name="networking-flex-cost-allocation-orgs-updates"></a>

Both Amazon EC2 policy modification and Amazon EC2 policy [inheritance](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_inheritance_mgmt.html) can affect a member's FCA configuration in their effective policy. Different types of change in a member's effective Amazon EC2 policy FCA attribute affect the member's FCA policies and associations in different ways:
+ When a new network resource block is added to the member's effective Amazon EC2 policy, a new FCA policy is created in the member's account with an account scope association.
+ When the metering configuration changes for an existing network resource block in the member's effective Amazon EC2 policy, a new version is created for the member's existing declarative-policy-managed FCA policy of that type. Changes to the description don't affect the metering configuration and don't result in a new version.
+ When a network resource block is removed from the member's effective Amazon EC2 policy, the member's existing declarative-policy-managed FCA policy of that type is deleted. No cost allocation is applied for the member's network resources matching the removed type.

## Remove declarative policy effects from member accounts
<a name="networking-flex-cost-allocation-orgs-removing"></a>

The delegated administrator can remove a member account from declarative policy control by one of the following methods:
+ Remove the flexible cost allocation configuration for all network resource types from every Amazon EC2 policy that contributes to the member account's effective policy.
+ Detach every Amazon EC2 policy that contains flexible cost allocation configuration from the member account and from the organizational units (OUs) and root that it inherits policies from.

## How removal of a declarative policy affects Networking Flexible Cost Allocation for member accounts
<a name="networking-flex-cost-allocation-orgs-removal-effects"></a>

After a member account is removed from declarative policy control for FCA, expect the following effects:
+ The member account no longer has declarative-policy-managed flexible cost allocation policies or associations.
+ The member account regains access to create, modify, and delete flexible cost allocation policies, along with access to associate and disassociate flexible cost allocation policies.
+ The member account's existing flexible cost allocation policies and associations become active again automatically after the declarative policy removal propagates to the metering service.

## Notes
<a name="networking-flex-cost-allocation-orgs-notes"></a>
+ Flexible cost allocation policies and associations aren't included in the [account status report for AWS Organizations Amazon EC2 policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_ec2.html#orgs_manage_policies_ec2-account-status-report).
+ FCA limitations apply to declarative-policy-managed flexible cost allocation policies and associations. For more information, see [Networking Flexible Cost Allocation limitations](networking-flex-cost-allocation-limitations.md).

## Example – Manage Networking Flexible Cost Allocation within an AWS Organization
<a name="networking-flex-cost-allocation-orgs-example"></a>

Managing FCA within an AWS Organization begins with two steps. The following example shows how to create an Amazon EC2 policy with the FCA attribute, and how it affects members attached to the policy.

### Step 1: Configure the Networking Flexible Cost Allocation service attribute
<a name="networking-flex-cost-allocation-orgs-example-step1"></a>

The delegated administrator creates an Amazon EC2 policy using the following AWS CLI command. The new policy has the ID `p-abcd1234a1`.

```
aws organizations create-policy \
  --type DECLARATIVE_POLICY_EC2 \
  --name example-networking-flexible-cost-allocation-ec2-policy \
  --description "Networking Flexible Cost Allocation declarative policy" \
  --content file://example-networking-flexible-cost-allocation-ec2-policy-content.json
```

The following is the policy document for `example-networking-flexible-cost-allocation-ec2-policy-content.json`:

```json
{
  "ec2_attributes": {
    "networking_flex_cost_allocation": {
      "natgw": {
        "show_back_status": {
          "@@assign": "enabled"
        },
        "description": {
          "@@assign": "Networking Flexible Cost Allocation for natgateways"
        },
        "reporting_granularity": {
          "@@assign": [
            "vpc"
          ]
        },
        "dimensions": {
          "@@assign": [
            "data-transfer",
            "data-processing"
          ]
        }
      },
      "ec2": {
        "show_back_status": {
          "@@assign": "enabled"
        },
        "description": {
          "@@assign": "Networking Flexible Cost Allocation for EC2 instances"
        },
        "reporting_granularity": {
          "@@assign": [
            "cidr"
          ]
        },
        "dimensions": {
          "@@assign": [
            "data-transfer"
          ]
        },
        "cidr_prefixes_type": {
          "@@assign": "source_prefixes"
        },
        "cidr_source_range_specifications": {
          "10.0.0.0/16": {
            "cidr_label": {
              "@@assign": "infra-team"
            }
          },
          "10.1.0.0/16": {
            "cidr_label": {
              "@@assign": "app-team"
            }
          }
        }
      },
      "pcx": {
        "show_back_status": {
          "@@assign": "enabled"
        },
        "description": {
          "@@assign": "Networking Flexible Cost Allocation for VPC peering connections"
        },
        "reporting_granularity": {
          "@@assign": [
            "eni"
          ]
        },
        "dimensions": {
          "@@assign": [
            "data-transfer"
          ]
        }
      }
    }
  }
}
```

### Step 2: Attach the policy to a member account
<a name="networking-flex-cost-allocation-orgs-example-step2"></a>

The delegated administrator attaches account `123456789012` to policy `p-abcd1234a1`:

```
aws organizations attach-policy --policy-id p-abcd1234a1 --target-id 123456789012
```

When member `123456789012` calls the `DescribeNetworkingFlexCostAllocationPolicies` API, expect the following list of FCA policies:

```
{
  "FlexCostAllocationPolicies": [
    {
      "Description": "Networking Flexible Cost Allocation for natgateways",
      "FcaPolicyArn": "arn:aws:ec2:aa-example-1:123456789012:fca-policy/fcap-0123456789abcdef1",
      "FcaPolicyId": "fcap-0123456789abcdef1",
      "LatestVersion": 1,
      "ManagedBy": "declarative-policy",
      "NatFcaPolicyDocument": {
        "Dimensions": ["data-transfer", "data-processing"],
        "ReportingGranularity": ["vpc"]
      },
      "Tags": [],
      "NetworkResourceType": "natgw",
      "OwnerAccount": "123456789012",
      "PolicyCreatedAt": "2026-10-29T20:46:32.000Z",
      "ShowBackEnabled": true,
      "UpdatedAt": "2026-10-29T20:46:32.000Z",
      "VersionExpectedEffectiveAt": "2026-10-29T22:00:00.000Z"
    },
    {
      "Description": "Networking Flexible Cost Allocation for EC2 instances",
      "FcaPolicyArn": "arn:aws:ec2:aa-example-1:123456789012:fca-policy/fcap-0123456789abcdef2",
      "FcaPolicyId": "fcap-0123456789abcdef2",
      "InstanceFcaPolicyDocument": {
        "CidrRangeSpecifications": {
          "Prefixes": [
            {
              "CidrLabel": "infra-team",
              "CidrRange": "10.0.0.0/16"
            },
            {
              "CidrLabel": "app-team",
              "CidrRange": "10.1.0.0/16"
            }
          ],
          "PrefixesType": "source-prefixes"
        },
        "Dimensions": ["data-transfer"],
        "ReportingGranularity": ["cidr"]
      },
      "LatestVersion": 1,
      "ManagedBy": "declarative-policy",
      "Tags": [],
      "NetworkResourceType": "ec2",
      "OwnerAccount": "123456789012",
      "PolicyCreatedAt": "2026-10-29T20:46:32.000Z",
      "ShowBackEnabled": true,
      "UpdatedAt": "2026-10-29T20:46:32.000Z",
      "VersionExpectedEffectiveAt": "2026-10-29T22:00:00.000Z"
    },
    {
      "Description": "Networking Flexible Cost Allocation for VPC peering connections",
      "FcaPolicyArn": "arn:aws:ec2:aa-example-1:123456789012:fca-policy/fcap-0123456789abcdef3",
      "FcaPolicyId": "fcap-0123456789abcdef3",
      "LatestVersion": 1,
      "ManagedBy": "declarative-policy",
      "NetworkResourceType": "pcx",
      "OwnerAccount": "123456789012",
      "PcxFcaPolicyDocument": {
        "Dimensions": ["data-transfer"],
        "ReportingGranularity": ["eni"]
      },
      "Tags": [],
      "PolicyCreatedAt": "2026-10-29T20:46:32.000Z",
      "ShowBackEnabled": true,
      "UpdatedAt": "2026-10-29T20:46:32.000Z",
      "VersionExpectedEffectiveAt": "2026-10-29T22:00:00.000Z"
    }
  ]
}
```

When member `123456789012` calls the `DescribeNetworkingFlexCostAllocationPolicyAssociations` API, expect the following list of FCA policy associations:

```
{
  "FcaPolicyAssociations": [
    {
      "AssociatedAt": "2026-10-29T20:46:32.000Z",
      "AssociationMode": "scope",
      "ExpectedEffectiveAt": "2026-10-29T22:00:00.000Z",
      "FcaPolicyAssociationId": "fcapassoc-0123456789abcdef1",
      "FcaPolicyId": "fcap-0123456789abcdef1",
      "NetworkResourceId": "123456789012",
      "OwnerAccount": "123456789012",
      "ManagedBy": "declarative-policy"
    },
    {
      "AssociatedAt": "2026-10-29T20:46:32.000Z",
      "AssociationMode": "scope",
      "ExpectedEffectiveAt": "2026-10-29T22:00:00.000Z",
      "FcaPolicyAssociationId": "fcapassoc-0123456789abcdef2",
      "FcaPolicyId": "fcap-0123456789abcdef2",
      "NetworkResourceId": "123456789012",
      "OwnerAccount": "123456789012",
      "ManagedBy": "declarative-policy"
    },
    {
      "AssociatedAt": "2026-10-29T20:46:32.000Z",
      "AssociationMode": "scope",
      "ExpectedEffectiveAt": "2026-10-29T22:00:00.000Z",
      "FcaPolicyAssociationId": "fcapassoc-0123456789abcdef3",
      "FcaPolicyId": "fcap-0123456789abcdef3",
      "NetworkResourceId": "123456789012",
      "OwnerAccount": "123456789012",
      "ManagedBy": "declarative-policy"
    }
  ]
}
```

When member `123456789012` calls the `DeleteNetworkingFlexCostAllocationPolicies` API to delete `fcap-0123456789abcdef1`, expect a client exception with the `DeclarativePolicyViolation` error code:

```
An error occurred (DeclarativePolicyViolation) when calling the DeleteNetworkingFlexCostAllocationPolicies operation: This functionality has been disabled by a Declarative Policy.
```
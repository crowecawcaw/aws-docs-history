# Declarative policy syntax and

examples

This page describes declarative policy syntax and provides examples.

## Considerations

- When you configure a service attribute using a declarative policy, it might
  impact multiple APIs. Any noncompliant actions will fail.
- Account administrators will not be able to modify the value of the service
  attribute at the individual account level.

## Syntax for declarative

policies

A declarative policy is a plaintext file that is structured according to the rules of
[JSON](http://json.org "http://json.org"). The syntax for declarative policies
follows the syntax for all management policy types. For a complete discussion of that
syntax, see [Policy syntax and
inheritance for management policy types](orgs_manage_policies_inheritance_mgmt.md "orgs_manage_policies_inheritance_mgmt.md"). This topic focuses on applying that
general syntax to the specific requirements of the declarative policy type.

The following example shows basic declarative policy syntax:

```
{
  "ec2_attributes": {
    "exception_message": {
      "@@assign": "Your custom error message.https://myURL"
    }
  }
}
```

- The `ec2_attributes` field key name. Declarative policies always
  start with a fixed key name for the given AWS service. It's the top line in
  the example policy above. Currently declarative policies only supported Amazon EC2
  related services.
- Under `ec2_attributes`, you can use `exception_message`
  to set a custom error message. For more information, see [Custom error
  messages for declarative policies](orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-custom-message "orgs_manage_policies_declarative.md#orgs_manage_policies_declarative-custom-message").
- Under `ec2_attributes`, you can insert one or more of the supported
  declarative policies. For those schemas, see [Supported declarative policies](#declarative-policy-examples "#declarative-policy-examples").

## Supported declarative policies

The following are the AWS services and attributes that declarative policies support.
In some of the following examples, the JSON whitespace formatting might be compressed to
save space.

- VPC Block Public Access
- Serial Console Access
- Image Block Public Access
- Allowed Images Settings
- Instance Metadata Defaults
- Snapshot Block Public Access

VPC Block Public Access
**Policy effect**

Controls if resources in Amazon VPCs and subnets can reach the internet through
internet gateways (IGWs). For more information, see [Configuration
for internet access](../../../vpc/latest/userguide/vpc-igw-internet-access.md "../../../vpc/latest/userguide/vpc-igw-internet-access.md") in the _Amazon Virtual Private Cloud User
Guide_.

**Policy contents**

```
{
  "ec2_attributes": {
    "vpc_block_public_access": {
      "internet_gateway_block": {
        "mode": {
          "@@assign": "block_ingress"
        },
        "exclusions_allowed": {
          "@@assign": "enabled"
        }
      }
    }
  }
}
```

The following are the available fields for this attribute:

- `"internet_gateway"`:
  - `"mode"`:
    - `"off"`: VPC BPA is not enabled.
    - `"block_ingress"`: All internet traffic
      to the VPCs (except for VPCs or subnets which are
      excluded) is blocked. Only traffic to and from NAT
      gateways and egress-only internet gateways is
      allowed because these gateways only allow outbound
      connections to be established.
    - `"block_bidirectional"`: All traffic to
      and from internet gateways and egress-only internet
      gateways (except for excluded VPCs and subnets) is
      blocked.

- `"exclusions_allowed"`: An exclusion is a mode that can
  be applied to a single VPC or subnet that exempts it from the
  account’s VPC BPA mode and will allow bidirectional or egress-only
  access.
  - `"enabled"`: Exclusions can be created by the
    account.
  - `"disabled"`: Exclusions cannot be created by
    the account.

###### Note

You can use the attribute to configure if exclusions are
allowed, but you cannot create exclusions with this attribute
itself. To create exclusions, you must create them in the
account that owns the VPC. For more information about creating
VPC BPA exclusions, see [Create and delete exclusions](../../../vpc/latest/userguide/security-vpc-bpa.md#security-vpc-bpa-exclusions "../../../vpc/latest/userguide/security-vpc-bpa.md#security-vpc-bpa-exclusions") in the
_Amazon VPC User Guide_.

**Considerations**

If you use this attribute in a declarative policy, you cannot use the
following operations to modify the enforced configuration for the accounts
in scope. This list is not exhaustive:

- `ModifyVpcBlockPublicAccessOptions`
- `CreateVpcBlockPublicAccessExclusion`
- `ModifyVpcBlockPublicAccessExclusion`

Serial Console Access
**Policy effect**

Controls if the EC2 serial console is accessible. For more information
about the EC2 serial console, see [EC2 Serial
Console](../../../AWSEC2/latest/UserGuide/ec2-serial-console.md "../../../AWSEC2/latest/UserGuide/ec2-serial-console.md") in the _Amazon Elastic Compute Cloud User Guide_.

**Policy contents**

```
{
  "ec2_attributes": {
    "serial_console_access": {
      "status": {
        "@@assign": "enabled"
      }
    }
  }
}
```

The following are the available fields for this attribute:

- `"status"`:
  - `"enabled"`: EC2 serial console access is
    allowed.
  - `"disabled"`: EC2 serial console access is
    blocked.

**Considerations**

If you use this attribute in a declarative policy, you cannot use the
following operations to modify the enforced configuration for the accounts
in scope. This list is not exhaustive:

- `EnableSerialConsoleAccess`
- `DisableSerialConsoleAccess`

Image Block Public Access
**Policy effect**

Controls if Amazon Machine Images (AMIs) are publicly sharable. For more
information about AMIs, see [Amazon Machine Images
(AMIs)](../../../AWSEC2/latest/UserGuide/AMIs.md "../../../AWSEC2/latest/UserGuide/AMIs.md") in the _Amazon Elastic Compute Cloud User Guide_.

**Policy contents**

```
{
  "ec2_attributes": {
    "image_block_public_access": {
      "state": {
        "@@assign": "block_new_sharing"
      }
    }
  }
}
```

The following are the available fields for this attribute:

- `"state"`:
  - `"unblocked"`: No restrictions on the public
    sharing of AMIs.
  - `"block_new_sharing"`: Blocks new public
    sharing of AMIs. AMIs that were already publicly shared
    remain publicly available.

**Considerations**

If you use this attribute in a declarative policy, you cannot use the
following operations to modify the enforced configuration for the accounts
in scope. This list is not exhaustive:

- `EnableImageBlockPublicAccess`
- `DisableImageBlockPublicAccess`

Allowed Images Settings
**Policy effect**

Controls the discovery and use of Amazon Machine Images (AMI) in Amazon EC2
with Allowed AMIs. For more information about AMIs, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md "../../../AWSEC2/latest/UserGuide/ec2-allowed-amis.md") in the _Amazon Elastic Compute Cloud User
Guide_.

**Policy contents**

The following are the available fields for this attribute:

```
{
  "ec2_attributes": {
    "allowed_images_settings": {
      "state": {
        "@@assign": "enabled"
      },
      "image_criteria": {
        "criteria_1": {
          "allowed_image_providers": {
            "@@append": [
              "amazon"
            ]
          }
        }
      }
    }
  }
}
```

- `"state"`:
  - `"enabled"`: The attribute is active and
    enforced.
  - `"disabled"`: The attribute is inactive and not
    enforced.
  - `"audit_mode"`: The attribute is in audit mode.
    This means it will identify noncompliant images but not
    block their use.

- `"image_criteria"`: A list of criteria. Support up to 10 criteria with the name from criteria_1 to criteria_10
  - `"allowed_image_providers"`: A comma-separated
    list of 12 digit account IDs or owner alias of amazon, aws_marketplace, aws_backup_vault.
  - `"image_names"`: The names of the allowed images. Names can include wildcards (? and \*). Length: 1–128 characters. With ?, the minimum is 3 characters.
  - `"marketplace_product_codes"`: The AWS Marketplace product codes for allowed images. Length: 1-25 characters Valid characters: Letters (A–Z, a–z) and numbers (0–9)
  - `"creation_date_condition"`: The maximum age for allowed images.
    - `"maximum_days_since_created"`: The maximum number of days that have elapsed since the image was created. Valid Range: Minimum value of 0. Maximum value of 2147483647.

  - `"deprecation_time_condition"`: The maximum period since deprecation for allowed images.
    - `"maximum_days_since_deprecated"`: The maximum number of days that have elapsed since the image was deprecated. Valid Range: Minimum value of 0. Maximum value of 2147483647.

**Considerations**

If you use this attribute in a declarative policy, you cannot use the
following operations to modify the enforced configuration for the accounts
in scope. This list is not exhaustive:

- `EnableAllowedImagesSettings`
- `ReplaceImageCriteriaInAllowedImagesSettings`
- `DisableAllowedImagesSettings`

Instance Metadata Defaults
**Policy effect**

Controls IMDS defaults for all new EC2 instance launches. Note that this
configuration sets defaults only and does not enforce IMDS version settings.
For more information about IMDS defaults, see [IMDS](../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md "../../../AWSEC2/latest/UserGuide/configuring-instance-metadata-service.md") in the _Amazon Elastic Compute Cloud User Guide_.

**Policy contents**

The following are the available fields for this attribute:

```
{
  "ec2_attributes": {
    "instance_metadata_defaults": {
      "http_tokens": {
        "@@assign": "required"
      },
      "http_put_response_hop_limit": {
        "@@assign": "4"
      },
      "http_endpoint": {
        "@@assign": "enabled"
      },
      "instance_metadata_tags": {
        "@@assign": "enabled"
      }
    }
  }
}
```

- `"http_tokens"`:
  - `"no_preference"`: Other defaults apply. For
    example, AMI defaults if applicable.
  - `"required"`: IMDSv2 must be used. IMDSv1 is
    not allowed.
  - `"optional"`: Both IMDSv1 and IMDSv2 are
    allowed.

###### Note

**Metadata version**

Before setting `http_tokens` to
`required` (IMDSv2 must be used), make sure that
none of your instances are making IMDSv1 calls.

- `"http_put_response_hop_limit"`:
  - `"`Integer`"`: Integer
    value from -1 to 64, representing the maximum number of hops
    the metadata token can travel. To indicate no preference,
    specify -1.

  ###### Note

  **Hop limit**

  If `http_tokens` is set to
  `required`, it is recommended to set
  `http_put_response_hop_limit` to a
  minimum of 2. For more information, see [Instance metadata access considerations](../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md#imds-considerations "../../../AWSEC2/latest/UserGuide/instancedata-data-retrieval.md#imds-considerations") in
  the _Amazon Elastic Compute Cloud User Guide_.

- `"http_endpoint"`:
  - `"no_preference"`: Other defaults apply. For
    example, AMI defaults if applicable.
  - `"enabled"`: The instance metadata service
    endpoint is accessible.
  - `"disabled"`: The instance metadata service
    endpoint is not accessible.

- `"instance_metadata_tags"`:
  - `"no_preference"`: Other defaults apply. For
    example, AMI defaults if applicable.
  - `"enabled"`: Instance tags can be accessed from
    instance metadata.
  - `"disabled"`: Instance tags cannot be accessed
    from instance metadata.

Snapshot Block Public Access
**Policy effect**

Controls if Amazon EBS snapshots are publicly accessible. For more
information about EBS snapshots, see [Amazon EBS snapshots](../../../ebs/latest/userguide/ebs-snapshots.md "../../../ebs/latest/userguide/ebs-snapshots.md") in
the _Amazon Elastic Block Store User Guide_.

**Policy contents**

```
{
  "ec2_attributes": {
    "snapshot_block_public_access": {
      "state": {
        "@@assign": "block_new_sharing"
      }
    }
  }
}
```

The following are the available fields for this attribute:

- `"state"`:
  - `"block_all_sharing"`: Blocks all public
    sharing of snapshots. Snapshots that were already publicly
    shared are treated as private and are no longer publicly
    available.
  - `"block_new_sharing"`: Blocks new public
    sharing of snapshots. Snapshots that were already publicly
    shared remain publicly available.
  - `"unblocked"`: No restrictions on the public
    sharing of snapshots.

**Considerations**

If you use this attribute in a declarative policy, you cannot use the
following operations to modify the enforced configuration for the accounts
in scope. This list is not exhaustive:

- `EnableSnapshotBlockPublicAccess`
- `DisableSnapshotBlockPublicAccess`

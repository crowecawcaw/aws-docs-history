# [CT.EC2.PV.11] Disallow public sharing of Amazon Machine Images (AMIs)

This control prevents the public sharing of your AMIs by configuring block public access for AMIs at an account level. If you already have public AMIs, they remain publicly available.

This is a preventive control with elective guidance, based on declarative policies. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Declarative policy for EC2
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control disallows new public sharing of AMIs. It does not restrict access to AMIs that have been shared publicly before this control was enabled.
- This control governs Amazon EC2 AMI Block Public Access (BPA) settings that are configured by means of EC2 `EnableImageBlockPublicAccess` and `DisableImageBlockPublicAccess` operations. If you apply this control, you cannot use these operations to modify these settings within an enrolled AWS account.
- This control includes an AWS Organizations inheritance operator for each policy setting that applies to child policies (`@@operators_allowed_for_child_policies` with a value of `@@all`). This operator allows you to add to, negate, or override each policy setting in this control, when it is applied to child OUs and accounts, by using the AWS Organizations declarative policy syntax. For more information on policy inheritance for AWS Organizations policies, see [Inheritance operators](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") in the _AWS Organizations User Guide_.
  The artifact for this control is the following declarative policy.

```

{
    "ec2_attributes": {
        "image_block_public_access": {
            "state": {
                "@@assign": "block_new_sharing",
                "@@operators_allowed_for_child_policies": ["@@all"]
            }
        }
    }
}

```

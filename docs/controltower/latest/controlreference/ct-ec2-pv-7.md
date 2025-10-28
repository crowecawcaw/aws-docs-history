# [CT.EC2.PV.7] Disallow all public sharing of Amazon EBS snapshots

This control blocks the public sharing of your Amazon EBS snapshots by configuring block public access for Amazon EBS snapshot settings at an account level. This setting has the effect of preventing all public sharing of your EBS snapshots, so that snapshots that previously were publicly shared are treated as private, and are no longer publicly available.

This is a preventive control with elective guidance, based on declarative policies. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Declarative policy for EC2
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`

###### Usage considerations

- Enabling this control does not change the permissions for snapshots that are publicly shared already. Instead, it prevents snapshots from being publicly visible and publicly accessible. Therefore, the attributes for these snapshots still indicate that they are publicly shared, even though they are not publicly available. If you later disable this control or adopt the related control to block new sharing in place of this control, these snapshots will become publicly available again.
- Enabling this control on an AWS account means that users in the account can no longer request new public sharing of EBS snapshots.
- This control includes an AWS Organizations inheritance operator for each policy setting that applies to child policies (`@@operators_allowed_for_child_policies` with a value of `@@all`). This operator allows you to add to, negate, or override each policy setting in this control, when it is applied to child OUs and accounts, by using the AWS Organizations declarative policy syntax. For more information on policy inheritance for AWS Organizations policies, see [Inheritance operators](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") in the _AWS Organizations User Guide_.
  The artifact for this control is the following declarative policy.

```

{
    "ec2_attributes": {
        "snapshot_block_public_access": {
            "state": {
                "@@assign": "block_all_sharing",
                "@@operators_allowed_for_child_policies": ["@@all"]
            }
        }
    }
}

```

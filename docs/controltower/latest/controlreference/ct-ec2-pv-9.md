# [CT.EC2.PV.9] Disallow access to the EC2 serial console for all EC2 instances

This control prevents access to the Amazon EC2 serial console of all EC2 instances for your account.

This is a preventive control with elective guidance, based on declarative policies. By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Limit network access
- **Implementation:** Declarative policy for EC2
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Resource types:** `AWS::::Account`

###### Usage considerations

- With the EC2 serial console, you have access to your Amazon EC2 instance's serial port, which you can use to troubleshoot boot, network configuration, and other issues. If you require EC2 serial console access, do not enable this control.
- This control governs Amazon EC2 Serial Console for instance settings that are configured by means of EC2 `EnableSerialConsoleAccess` and `DisableSerialConsoleAccess` operations. If you apply this control, you cannot use these operations to modify these settings within an enrolled AWS account.
- This control includes an AWS Organizations inheritance operator for each policy setting that applies to child policies (`@@operators_allowed_for_child_policies` with a value of `@@all`). This operator allows you to add to, negate, or override each policy setting in this control, when it is applied to child OUs and accounts, by using the AWS Organizations declarative policy syntax. For more information on policy inheritance for AWS Organizations policies, see [Inheritance operators](../../../organizations/latest/userguide/policy-operators.md "../../../organizations/latest/userguide/policy-operators.md") in the _AWS Organizations User Guide_.
  The artifact for this control is the following declarative policy.

```

{
    "ec2_attributes": {
        "serial_console_access": {
            "status": {
                "@@assign": "disabled",
                "@@operators_allowed_for_child_policies": ["@@all"]
            }
        }
    }
}

```

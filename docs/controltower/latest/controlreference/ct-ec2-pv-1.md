# [CT.EC2.PV.1] Require an Amazon EBS snapshot to be created from an encrypted EC2 volume

This control disallows creation of new snapshots that are based on unencrypted EBS volumes.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Encrypt data at rest
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control does not prevent creation of unencrypted EBS snapshots that are created by means of the `CopySnapshot` operation. AWS Control Tower recommends that you enable EBS encryption by default, so that encryption is applied to copies of unencrypted snapshots. See [Encryption scenarios](../../../AWSEC2/latest/UserGuide/EBSEncryption.md#encryption-examples "../../../AWSEC2/latest/UserGuide/EBSEncryption.md#encryption-examples") in the _Amazon EC2 User Guide for Linux Instances_ for more information.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV1",
            "Effect": "Deny",
            "Action": [
                "ec2:CreateSnapshot",
                "ec2:CreateSnapshots"
            ],
            "Resource": "arn:*:ec2:*:*:volume/*",
            "Condition": {
                "Bool": {
                    "ec2:Encrypted": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

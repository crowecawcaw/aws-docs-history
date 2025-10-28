# [CT.EC2.PV.3] Require that an Amazon EBS snapshot cannot be publicly restorable

This control disallows sharing of an EBS snapshot with all AWS accounts.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control prevents unencrypted EBS snapshots from being made public, by disallowing sharing of EBS snapshots with all AWS accounts. Encrypted snapshots and snapshots with AWS Marketplace product codes cannot be made public.
- To prevent the public sharing of snapshots, AWS Control Tower recommends enabling block public access for snapshots. For more information, see [Block public access for snapshots](../../../AWSEC2/latest/UserGuide/block-public-access-snapshots.md "../../../AWSEC2/latest/UserGuide/block-public-access-snapshots.md") in the _Amazon EC2 User Guide for Linux Instances_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV3",
            "Effect": "Deny",
            "Action": "ec2:ModifySnapshotAttribute",
            "Resource": "arn:*:ec2:*::snapshot/*",
            "Condition": {
                "StringEquals": {
                    "ec2:Add/group": "all"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

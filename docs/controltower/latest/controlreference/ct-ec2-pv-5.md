# [CT.EC2.PV.5] Disallow the use of Amazon EC2 VM import and export

This control disallows use of EC2 VM Import/Export APIs that can be used to import and export EC2 instance, snapshot, image and volume data.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** Amazon EC2

###### Control metadata

- **Control objective:** Enforce least privilege, Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::::Account`

###### Usage considerations

- This control disallows the use of VM Import/Export APIs that can be used to import and export EC2 image, snapshot, instance and volume data. If you need to use VM Import/Export functionality, do not enable this control.
- This control does not prevent cancelling existing VM Import/Export import, export or conversion tasks.
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV5",
            "Effect": "Deny",
            "Action": [
                "ec2:CreateInstanceExportTask",
                "ec2:ExportImage",
                "ec2:ImportImage",
                "ec2:ImportSnapshot",
                "ec2:ImportInstance",
                "ec2:ImportVolume"
            ],
            "Resource": "*"{% if ExemptedPrincipalArns %},
            "Condition": {
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }
            }{% endif %}
        }
    ]
}


```

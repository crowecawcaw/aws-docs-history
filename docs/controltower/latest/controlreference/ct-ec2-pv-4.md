# [CT.EC2.PV.4] Require that Amazon EBS direct APIs are not called

This control disallows usage of all EBS direct APIs.

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

- Do not enable this control if you use EBS direct APIs, either directly or through an AWS Backup partner product.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTEC2PV4",
            "Effect": "Deny",
            "Action": "ebs:*",
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

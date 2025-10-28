# [CT.KMS.PV.3] Require that an AWS KMS key is configured with the bypass policy lockout safety check enabled

This control disallows bypassing the KMS key policy lockout safety check when creating a KMS key or updating its key policy.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Key Management Service (AWS KMS)

###### Control metadata

- **Control objective:** Enforce least privilege, Protect configurations
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::KMS::Key`

###### Usage considerations

- This control disallows bypassing the policy lockout safety check, because bypassing this check increases the risk that a KMS key becomes unmanageable.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTKMSPV3",
            "Effect": "Deny",
            "Action": [
                "kms:CreateKey",
                "kms:PutKeyPolicy"
            ],
            "Resource": "*",
            "Condition": {
                "Bool": {
                    "kms:BypassPolicyLockoutSafetyCheck": "true"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

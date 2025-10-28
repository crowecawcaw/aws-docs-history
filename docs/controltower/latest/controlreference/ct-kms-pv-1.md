# [CT.KMS.PV.1] Require an AWS KMS key policy to have a statement that limits creation of AWS KMS grants to AWS services

This control requires that KMS grants are issued only to AWS services that are integrated with AWS KMS, or to an AWS service principal.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Key Management Service (AWS KMS)

###### Control metadata

- **Control objective:** Enforce least privilege
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::KMS::Key`

###### Usage considerations

- This control disallows the creation of AWS KMS grants for your KMS keys if the request does not originate from an AWS service that's integrated with AWS KMS, or from an AWS service principal.
- If you need to issue AWS KMS grants directly to your IAM principals for a customer-managed key, do not enable this control.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTKMSPV1",
            "Effect": "Deny",
            "Action": "kms:CreateGrant",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "kms:GrantIsForAWSResource": "false",
                    "aws:PrincipalIsAWSService": "false"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

# [CT.KMS.PV.2] Require that an AWS KMS asymmetric key with RSA key material used for encryption does not have a key length of 2048 bits

This control disallows the creation of KMS keys used for encryption and decryption that also have a key spec of `RSA_2048`.

This is a preventive control with elective guidance based on service control policies (SCPs). By default, this control is not enabled. You can enable this control through the AWS Control Tower console, or though the AWS Control Tower APIs.

**AWS service:** AWS Key Management Service (AWS KMS)

###### Control metadata

- **Control objective:** Encrypt data at rest, Encrypt data in transit
- **Implementation:** Service control policy (SCP)
- **Control behavior:** Preventive
- **Control owner:** AWS Control Tower
- **Control groups:** digital-sovereignty
- **Resource types:** `AWS::KMS::Key`

###### Usage considerations

- This control requires that you use a `KeySpec` other than `RSA_2048` when creating asymmetric KMS keys used for encryption and decryption.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTKMSPV2",
            "Effect": "Deny",
            "Action": "kms:CreateKey",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "kms:KeyUsage": "ENCRYPT_DECRYPT",
                    "kms:KeySpec": "RSA_2048"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

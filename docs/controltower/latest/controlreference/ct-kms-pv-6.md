# [CT.KMS.PV.6] Require that an AWS KMS customer-managed key (CMK) is configured with key material originating from an external key store (XKS)

This control disallows creation of KMS keys that do not have a key origin of `EXTERNAL_KEY_STORE`.

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

- This control restricts creation of AWS KMS keys to those that use a specific key material origin. It is suitable when enforcing a KMS key management strategy that requires all KMS keys to an external key store custom key store.
- Before enforcing the exclusive use of keys whose key material resides in an external key store, carefully evaluate the trade-offs documented in the [External key stores](../../../kms/latest/developerguide/keystore-external.md "../../../kms/latest/developerguide/keystore-external.md") section of the _AWS KMS Developer Guide_.
- This control supports configuration. It contains elements that are included by AWS Control Tower conditionally, based on the configuration you select. This control supports the following configuration parameters: **ExemptedPrincipalArns**. For more information, see [Configure controls with parameters](control-parameter-concepts.md "control-parameter-concepts.md").
  The artifact for this control is the following service control policy (SCP).

```

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CTKMSPV6",
            "Effect": "Deny",
            "Action": "kms:CreateKey",
            "Resource": "*",
            "Condition": {
                "StringNotEquals": {
                    "kms:KeyOrigin": "EXTERNAL_KEY_STORE"
                }{% if ExemptedPrincipalArns %},
                "ArnNotLike": {
                    "aws:PrincipalArn": {{ExemptedPrincipalArns}}
                }{% endif %}
            }
        }
    ]
}


```

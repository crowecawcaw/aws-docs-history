# Condition keys for NitroTPM

The following condition keys are specific to NitroTPM attestation:

## kms:RecipientAttestation:NitroTPMPCR<PCR_ID>

| AWS KMS Condition Keys                         | Condition Type | Value type    | API Operations                                                                                      | Policy Type                   |
| ---------------------------------------------- | -------------- | ------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:RecipientAttestation:NitroTPMPCR<PCR_ID>` | String         | Single-valued | `Decrypt`<br>`DeriveSharedSecret`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateRandom` | Key policies and IAM policies |

The `kms:RecipientAttestation:NitroTPMPCR<PCR_ID>` condition key controls
access to `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`,
`GenerateDataKeyPair`, and `GenerateRandom` with a KMS key
only when the platform configuration registers (PCRs) from the signed attestation
document in the request match the PCRs in the condition key. This condition key is
effective only when the `Recipient` parameter in the request specifies a
signed attestation document from NitroTPM.

This value is also included in [CloudTrail
events](ct-nitro-tpm.md "ct-nitro-tpm.md") that represent requests to AWS KMS for NitroTPM.

To specify a PCR value, use the following format. Concatenate the PCR ID to the
condition key name. The PCR value must be a lower-case hexadecimal string of up to 96
bytes.

```
`"kms:RecipientAttestation:NitroTPMPCR`PCR_ID`": "`PCR_value`"`
```

For example, the following condition key specifies a particular value for PCR4:

```
`kms:RecipientAttestation:NitroTPMPCR**4**: "abc1abcdef2abcdef3abcdef4abcdef5abcdef6abcdef7abcdef8abcdef9abcdef8abcdef7abcdef6abcdef5abcdef4abcdef3abcdef2abcdef1abcdef0abcde"`
```

The following example key policy statement allows the `data-processing`
role to use the KMS key for the [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operation.

The `kms:RecipientAttestation:NitroTPMPCR` condition key in this statement allows the
operation only when the PCR4 value in the signed attestation document in the request matches
`kms:RecipientAttestation:NitroTPMPCR4` value in the condition. Use the
`StringEqualsIgnoreCase` policy operator to require a case-insensitive
comparison of the PCR values.

If the request does not include an attestation document, permission is denied because
this condition is not satisfied.

```
{
  "Sid" : "Enable NitroTPM data processing",
  "Effect" : "Allow",
  "Principal" : {
    "AWS" : "arn:aws:iam::111122223333:role/data-processing"
  },
  "Action": "kms:Decrypt",
  "Resource" : "*",
  "Condition": {
    "StringEqualsIgnoreCase": {
      **"kms:RecipientAttestation:NitroTPMPCR4": "abc1de4f2dcf774f6e3b679f62e5f120065b2e408dcea327bd1c9dddaea6664e7af7935581474844767453082c6f1586116376cede396a30a39a611b9aad7966c87"**
    }
  }
}
```

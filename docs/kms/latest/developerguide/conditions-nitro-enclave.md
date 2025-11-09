# Condition keys for Nitro Enclaves

The following condition keys are specific to Nitro Enclaves attestation:

## kms:RecipientAttestation:ImageSha384

| AWS KMS Condition Keys                 | Condition Type | Value type    | API Operations                                                                                      | Policy Type                   |
| -------------------------------------- | -------------- | ------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:RecipientAttestation:ImageSha384` | String         | Single-valued | `Decrypt`<br>`DeriveSharedSecret`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateRandom` | Key policies and IAM policies |

The `kms:RecipientAttestation:ImageSha384` condition key controls
access to `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`,
`GenerateDataKeyPair`, and `GenerateRandom` with a KMS key
when the image digest from the signed attestation document in the request matches
the value in the condition key. The `ImageSha384` value corresponds to
PCR0 in the attestation document. This condition key is effective only when the
`Recipient` parameter in the request specifies a signed attestation
document for an AWS Nitro enclave.

This value is also included in [CloudTrail
events](ct-nitro-enclave.md "ct-nitro-enclave.md") for requests to AWS KMS for Nitro enclaves.

For example, the following key policy statement allows the
`data-processing` role to use the KMS key for [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"), and
[GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md")
operations. The `kms:RecipientAttestation:ImageSha384` condition key
allows the operations only when the image digest value (PCR0) of the attestation
document in the request matches the image digest value in the condition. This
condition key is effective only when the `Recipient` parameter in the
request specifies a signed attestation document for an AWS Nitro enclave.

If the request does not include a valid attestation document from an AWS Nitro
enclave, permission is denied because this condition is not satisfied.

```
{
  "Sid" : "Enable enclave data processing",
  "Effect" : "Allow",
  "Principal" : {
    "AWS" : "arn:aws:iam::111122223333:role/data-processing"
  },
  "Action": [
    "kms:Decrypt",
    "kms:DeriveSharedSecret",
    "kms:GenerateDataKey",
    "kms:GenerateDataKeyPair",
    "kms:GenerateRandom"
  ],
  "Resource" : "*",
  "Condition": {
    "StringEqualsIgnoreCase": {
      **"kms:RecipientAttestation:ImageSha384": "9fedcba8abcdef7abcdef6abcdef5abcdef4abcdef3abcdef2abcdef1abcdef1abcdef0abcdef1abcdef2abcdef3abcdef4abcdef5abcdef6abcdef7abcdef99"**
    }
  }
}
```

## kms:RecipientAttestation:PCR<PCR_ID>

| AWS KMS Condition Keys                 | Condition Type | Value type    | API Operations                                                                                      | Policy Type                   |
| -------------------------------------- | -------------- | ------------- | --------------------------------------------------------------------------------------------------- | ----------------------------- |
| `kms:RecipientAttestation:PCR<PCR_ID>` | String         | Single-valued | `Decrypt`<br>`DeriveSharedSecret`<br>`GenerateDataKey`<br>`GenerateDataKeyPair`<br>`GenerateRandom` | Key policies and IAM policies |

The `kms:RecipientAttestation:PCR<PCR_ID>` condition key controls
access to `Decrypt`, `DeriveSharedSecret`, `GenerateDataKey`,
`GenerateDataKeyPair`, and `GenerateRandom` with a KMS key
only when the platform configuration registers (PCRs) from the signed attestation
document in the request match the PCRs in the condition key. This condition key is
effective only when the `Recipient` parameter in the request specifies a
signed attestation document from an AWS Nitro enclave.

This value is also included in [CloudTrail
events](ct-nitro-enclave.md "ct-nitro-enclave.md") that represent requests to AWS KMS for Nitro enclaves.

To specify a PCR value, use the following format. Concatenate the PCR ID to the
condition key name. You can specify a PCR ID that identifies one of the [six enclave measurements](../../../enclaves/latest/user/set-up-attestation.md#where "../../../enclaves/latest/user/set-up-attestation.md#where")
or a custom PCR ID that you defined for a specific use case. The PCR value must be a lower-case hexadecimal string of up to 96
bytes.

```
`"kms:RecipientAttestation:PCR`PCR_ID`": "`PCR_value`"`
```

For example, the following condition key specifies a particular value for PCR1, which
corresponds to the hash of the kernel used for the enclave and the bootstrap process.

```
`kms:RecipientAttestation:PCR**1**: "abc1abcdef2abcdef3abcdef4abcdef5abcdef6abcdef7abcdef8abcdef9abcdef8abcdef7abcdef6abcdef5abcdef4abcdef3abcdef2abcdef1abcdef0abcde"`
```

The following example key policy statement allows the `data-processing`
role to use the KMS key for the [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operation.

The `kms:RecipientAttestation:PCR` condition key in this statement allows the
operation only when the PCR1 value in the signed attestation document in the request matches
`kms:RecipientAttestation:PCR1` value in the condition. Use the
`StringEqualsIgnoreCase` policy operator to require a case-insensitive
comparison of the PCR values.

If the request does not include an attestation document, permission is denied because
this condition is not satisfied.

```
{
  "Sid" : "Enable enclave data processing",
  "Effect" : "Allow",
  "Principal" : {
    "AWS" : "arn:aws:iam::111122223333:role/data-processing"
  },
  "Action": "kms:Decrypt",
  "Resource" : "*",
  "Condition": {
    "StringEqualsIgnoreCase": {
      **"kms:RecipientAttestation:PCR1": "abc1de4f2dcf774f6e3b679f62e5f120065b2e408dcea327bd1c9dddaea6664e7af7935581474844767453082c6f1586116376cede396a30a39a611b9aad7966c87"**
    }
  }
}
```

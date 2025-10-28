# Using cryptographic attestation with AWS KMS

This section explains how to set up attestation to work with AWS Key Management Service. AWS KMS integrates
with Nitro Enclaves to provide built-in attestation support.

## Secret data preparation

Before using Nitro Enclaves with AWS KMS, it is important that you encrypt your sensitive data
before sending it to the parent instance or the enclave. This section provides an
overview of the steps needed to prepare your sensitive data for processing inside
the enclave.

1. Create a AWS KMS key. For more information, see [Creating Keys](../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk "../../../kms/latest/developerguide/create-keys.md#create-symmetric-cmk") in
   the _AWS Key Management Service Developer Guide_.
2. Generate a plaintext and encrypted data key using the KMS key. For more information, see
   [generate-data-key](../../../cli/latest/reference/kms/generate-data-key.md "../../../cli/latest/reference/kms/generate-data-key.md") in the _AWS KMS AWS CLI Command Reference_.
3. Encrypt the secret data under the KMS key using the plaintext data key and a client-side
   cryptographic library, such as the [AWS Encryption SDK](../../../encryption-sdk/latest/developer-guide/introduction.md "../../../encryption-sdk/latest/developer-guide/introduction.md"). For more information, see [Encrypt
   data with a data key](../../../kms/latest/developerguide/concepts.md#data-keys-encrypt "../../../kms/latest/developerguide/concepts.md#data-keys-encrypt") in the
   _AWS Key Management Service Developer Guide_. You must modify the KMS key policy to
   grant the IAM principal that you’re using in your client permission to call
   the GenerateDataKey API action.
4. Upload the encrypted secret data and the encrypted data key to a storage location, such as Amazon S3. If you’re
   using the AWS Encryption SDK, the encrypted data key is automatically included in the header of the encrypted
   message.

## KMS key preparation

After you have created your KMS key and you have encrypted your sensitive data under it, you need to ensure
that only the enclave can access it to decrypt the encrypted data.

AWS KMS enables you to create KMS key policies with condition keys that are based on an enclave's measurements.
For more information about using condition keys in KMS key policies, see [AWS KMS
condition keys for AWS Nitro Enclaves](../../../kms/latest/developerguide/policy-conditions.md#conditions-nitro-enclaves "../../../kms/latest/developerguide/policy-conditions.md#conditions-nitro-enclaves")
in the _AWS Key Management Service Developer Guide_.

The Nitro Enclaves SDK includes some APIs (`kms-decrypt`,
`kms-generate-data-key`, and `kms-generate-random`) that
integrate with AWS KMS. When these APIs are called against a specific key, the
enclave's attestation document, which includes its measurements, is attached to the
request. AWS KMS receives the request and validates the measurements in the provided
attestation document against the measurements specified in the condition keys of the
KMS key policy. It uses this information to determine whether the enclave should be
granted permission to perform the requested action using the requested KMS key.

To prepare AWS KMS for attestation you must have the enclave's measurements. When you have
the measurements, you can create a KMS key policy that includes condition keys that are
based on those measurements.

AWS KMS provides `kms:RecipientAttestation:ImageSha384` and
`kms:RecipientAttestation:PCR` condition keys that enable you to create
attestation-based condition keys for KMS key policies. These policies ensure that AWS KMS only allows operations using the
KMS key if the enclave provides a signed attestation document that contains measurements that match
the measurements specified in the KMS key policy's condition keys. For more information about the condition keys,
see [kms:RecipientAttestation:ImageSha384](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-recipient-image-sha "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-recipient-image-sha") and [kms:RecipientAttestation:PCR](../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-recipient-pcrs "../../../kms/latest/developerguide/policy-conditions.md#conditions-kms-recipient-pcrs")
in the _AWS Key Management Service Developer Guide_.

For example, the following KMS key policy allows enclaves running on instances that have the
`data-processing` instance profile to use the KMS key for the
`Decrypt`, `GenerateDataKey`, and
`GenerateRandom` actions. The condition key allows the operation only
when measurements in the attestation document in the request matches the
measurements in the condition. If the request doesn't include an attestation
document, the role doesn't have permission to call the operation because this
condition cannot be satisfied.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [{
 "Sid" : "Enable enclave data processing",
 "Effect" : "Allow",
 "Principal" : {
 "AWS" : "arn:aws:iam::123456789012:role/data-processing"
 },
 "Action": [
 "kms:Decrypt",
 "kms:GenerateDataKey",
 "kms:GenerateRandom"
 ],
 "Resource": "*",
 "Condition": {
 "StringEqualsIgnoreCase": {
 "kms:RecipientAttestation:ImageSha384":"EXAMPLE8abcdef7abcdef6abcdef5abcdef4abcdef3abcdef2abcdef1abcdef1abcdef0abcdef1abcdEXAMPLE",
 "kms:RecipientAttestation:PCR0":"EXAMPLE8abcdef7abcdef6abcdef5abcdef4abcdef3abcdef2abcdef1abcdef1abcdef0abcdef1abcdEXAMPLE",
 "kms:RecipientAttestation:PCR1":"EXAMPLE050abf6b993c915505f3220e2d82b51aff830ad14cbecc2eec1bf0b4ae749d311c663f464cde9f718aEXAMPLE",
 "kms:RecipientAttestation:PCR2":"EXAMPLEc300289e872e6ac4d19b0b5ac4a9b020c98295643ff3978610750ce6a86f7edff24e3c0a4a445f2ff8EXAMPLE",
 "kms:RecipientAttestation:PCR3":"EXAMPLE11de9baee597508183477f097ae385d4a2c885aa655432365b53b812694e230bbe8e1bb1b8de748fe1EXAMPLE",
 "kms:RecipientAttestation:PCR4":"EXAMPLE6b9b3d89a53b13f5dfd14a1049ec0b80a9ae4b159adde479e9f7f512f33e835a0b9023ca51ada02160EXAMPLE",
 "kms:RecipientAttestation:PCR8":"EXAMPLE34a884328944cd806127c7784677ab60a154249fd21546a217299ccfa1ebfe4fa96a163bf41d3bcfaeEXAMPLE"
 }
 }
 }]
}`

```

# Prepare AWS KMS for attestation

###### Note

If you are attesting to a third-party service, you must build your own custom mechanisms for receiving,
parsing, and validating Attestation Documents. For more information, see [Validate a NitroTPM Attestation Document](nitrotpm-attestation-document-validate.md "nitrotpm-attestation-document-validate.md").

After you have created your Attestable AMI, you should have reference measurements that you can use to validate requests
from an Amazon EC2 instance. AWS KMS provides built-in support for attestation with NitroTPM.

For the AWS KMS key that you used to encrypt your secret data, add a key policy that allows key access only
if API requests include an Attestation Document with PCR4 or PCR7 measurements that match the reference measurements you
generated during the Attestable AMI creation process. This ensures that only requests from instances launched
using the Attestable AMI can perform cryptographic operations using the AWS KMS key.

AWS KMS provides `kms:RecipientAttestation:NitroTPMPCR4` and `kms:RecipientAttestation:NitroTPMPCR7`
condition keys that enable you to create attestation-based conditions for NitroTPM KMS key policies. For more information,
see [Condition keys for
NitroTPM](../../../kms/latest/developerguide/conditions-nitro-tpm.md "../../../kms/latest/developerguide/conditions-nitro-tpm.md").

For example, the following AWS KMS key policy allows key access only if the request originates from an
instance with the `MyEC2InstanceRole` instance profile attached, and if the request includes an
Attestation Document with specific PCR 4 and PCR 7 values.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Allow requests from instances with attested AMI only",
      "Effect": "Allow",
      "Principal": {
        "AWS": "`arn:aws:iam::111122223333:role/MyEC2InstanceRole`"
      },
      "Action": [
        "kms:Decrypt",
        "kms:GenerateDataKey",
        "kms:GenerateRandom"
      ],
      "Resource": "*",
      **"Condition": {
 "StringEqualsIgnoreCase": {
 "kms:RecipientAttestation:NitroTPMPCR4":"`EXAMPLE6b9b3d89a53b13f5dfd14a1049ec0b80a9ae4b159adde479e9f7f512f33e835a0b9023ca51ada02160EXAMPLE`",
 "kms:RecipientAttestation:NitroTPMPCR7":"`EXAMPLE34a884328944cd806127c7784677ab60a154249fd21546a217299ccfa1ebfe4fa96a163bf41d3bcfaeEXAMPLE`"
 }
 }**
    }
  ]
}
```

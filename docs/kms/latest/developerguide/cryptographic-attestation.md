

# Cryptographic attestation support in AWS KMS
<a name="cryptographic-attestation"></a>

AWS KMS supports *cryptographic attestation* for [AWS Nitro Enclaves](https://docs.aws.amazon.com/enclaves/latest/user/) and [AWS NitroTPM](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm-attestation.html). Applications that support these attestation methods call the following AWS KMS cryptographic operations with a signed attestation document. AWS KMS verifies that the attestation document came from a valid source (either a Nitro enclave or NitroTPM). Then, instead of returning plaintext data in the response, these APIs encrypt the plaintext with the public key from the attestation document and return ciphertext that can be decrypted only by the corresponding private key in the enclave or EC2 instance.
+ [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt)
+ [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret)
+ [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey)
+ [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair)
+ [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom) 

The following table shows how the response to attested requests differs from the standard response for each API operation.


| AWS KMS operation | Standard response | Response for attested requests | 
| --- | --- | --- | 
| Decrypt | Returns plaintext data | Returns the plaintext data encrypted by the public key from the attestation document | 
| DeriveSharedSecret | Returns raw shared secret | Returns the raw shared secret encrypted by the public key from the attestation document | 
| GenerateDataKey | Returns a plaintext copy of the data key(Also returns a copy of the data key encrypted by a KMS key) | Returns a copy of the data key encrypted by the public key from the attestation document(Also returns a copy of the data key encrypted by a KMS key) | 
| GenerateDataKeyPair | Returns a plaintext copy of the private key(Also returns the public key and a copy of the private key encrypted by a KMS key) | Returns a copy of the private key encrypted by the public key from the attestation document(Also returns the public key and a copy of the private key encrypted by a KMS key) | 
| GenerateRandom | Returns a random byte string | Returns the random byte string encrypted by the public key from the attestation document | 

AWS KMS supports [policy condition keys](conditions-attestation.md) that you can use to allow or deny attested operations with an AWS KMS key based on the content of the attestation document. You can also [monitor attested requests to AWS KMS](ct-attestation.md) in your AWS CloudTrail logs.

**Learn more**
+ [Cryptographic attestation](https://docs.aws.amazon.com/enclaves/latest/user/set-up-attestation.html)
+ [AWS KMS condition keys for attested platforms](conditions-attestation.md)
+ [How to make attested calls to AWS KMS](attested-calls.md)
+ [Monitoring attested requests](ct-attestation.md)
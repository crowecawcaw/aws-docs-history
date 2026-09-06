

# Monitoring attested requests
<a name="ct-attestation"></a>

You can use your AWS CloudTrail logs to monitor [Decrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decrypt), [DeriveSharedSecret](https://docs.aws.amazon.com/kms/latest/APIReference/API_DeriveSharedSecret), [GenerateDataKey](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKey), [GenerateDataKeyPair](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateDataKeyPair), and [GenerateRandom](https://docs.aws.amazon.com/kms/latest/APIReference/API_GenerateRandom) operations that use attestation. In these log entries, the `additionalEventData` field has a `recipient` field with information from the attestation document in the request. These fields are included only when the `Recipient` parameter in the request specifies a signed attestation document. 

The specific information included in the CloudTrail log depends on the attestation method used.
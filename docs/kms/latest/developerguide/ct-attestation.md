# Monitoring attested requests

You can use your AWS CloudTrail logs to monitor [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md"), [DeriveSharedSecret](../APIReference/API_DeriveSharedSecret.md "../APIReference/API_DeriveSharedSecret.md"), [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md"), [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md"), and [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md") operations that use attestation. In these log entries, the
`additionalEventData` field has a `recipient` field with
information from the attestation document in the request. These fields are included only
when the `Recipient` parameter in the request specifies a signed attestation
document.

The specific information included in the CloudTrail log depends on the attestation
method used.

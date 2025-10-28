# Monitoring requests for Nitro enclaves

For Nitro enclave attestation, the CloudTrail log includes the module ID
(`attestationDocumentModuleId`), image digest
(`attestationDocumentEnclaveImageDigest`), and platform configuration
registers (PCRs) from the attestation document.

The module ID is the [enclave ID](../../../enclaves/latest/user/nitro-enclave-concepts.md#term-enclaveid "../../../enclaves/latest/user/nitro-enclave-concepts.md#term-enclaveid") of the Nitro enclave. The image digest is the SHA384 hash of
the enclave image. You can use the image digest and PCR values in [conditions for key policies and IAM
policies](conditions-attestation.md "conditions-attestation.md"). For information about the PCRs, see [Where to get an enclave's
measurements](../../../enclaves/latest/user/set-up-attestation.md#where "../../../enclaves/latest/user/set-up-attestation.md#where") in the _AWS Nitro Enclaves User
Guide_.

This section shows an example CloudTrail log entry for each of the supported Nitro
enclave requests to AWS KMS.

## Decrypt (for an enclave)

The following example shows an AWS CloudTrail log entry of a [Decrypt](../APIReference/API_Decrypt.md "../APIReference/API_Decrypt.md") operation for an AWS Nitro
enclave.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "userName": "Alice"
    },
    "eventTime": "2020-07-27T22:58:24Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decrypt",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "encryptionAlgorithm": "SYMMETRIC_DEFAULT",
        "keyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "responseElements": null,
    "additionalEventData": {
        **"recipient": {
 "attestationDocumentModuleId": "i-123456789abcde123-enc123456789abcde12",
 "attestationDocumentEnclaveImageDigest": "<AttestationDocument.PCR0>",
 "attestationDocumentEnclavePCR1": "<AttestationDocument.PCR1>",
 "attestationDocumentEnclavePCR2": "<AttestationDocument.PCR2>",
 "attestationDocumentEnclavePCR3": "<AttestationDocument.PCR3>",
 "attestationDocumentEnclavePCR4": "<AttestationDocument.PCR4>",
 "attestationDocumentEnclavePCR8": "<AttestationDocument.PCR8>"
 }**
    },
    "requestID": "b4a65126-30d5-4b28-98b9-9153da559963",
    "eventID": "e5a2f202-ba1a-467c-b4ba-f729d45ae521",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

[Show moreShow less](# "#")

## GenerateDataKey (for an enclave)

The following example shows an AWS CloudTrail log entry of a [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") operation for an AWS Nitro enclave.

```
{
    "eventVersion": "1.02",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "userName": "Alice"
    },
    "eventTime": "2014-11-04T00:52:40Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKey",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "numberOfBytes": 32
    },
    "responseElements": null,
    "additionalEventData": {
        **"recipient": {
 "attestationDocumentModuleId": "i-123456789abcde123-enc123456789abcde12",
 "attestationDocumentEnclaveImageDigest": "<AttestationDocument.PCR0>",
 "attestationDocumentEnclavePCR1": "<AttestationDocument.PCR1>",
 "attestationDocumentEnclavePCR2": "<AttestationDocument.PCR2>",
 "attestationDocumentEnclavePCR3": "<AttestationDocument.PCR3>",
 "attestationDocumentEnclavePCR4": "<AttestationDocument.PCR4>",
 "attestationDocumentEnclavePCR8": "<AttestationDocument.PCR8>"
 }**
    },
    "requestID": "e0eb83e3-63bc-11e4-bc2b-4198b6150d5c",
    "eventID": "a9dea4f9-8395-46c0-942c-f509c02c2b71",
    "readOnly": true,
    "resources": [{
        "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "accountId": "111122223333"
    }],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

[Show moreShow less](# "#")

## GenerateDataKeyPair (for an enclave)

The following example shows an AWS CloudTrail log entry of a [GenerateDataKeyPair](../APIReference/API_GenerateDataKeyPair.md "../APIReference/API_GenerateDataKeyPair.md") operation for an AWS Nitro
enclave.

```
{
    "eventVersion": "1.05",
    "userIdentity": {
            "type": "IAMUser",
            "principalId": "EX_PRINCIPAL_ID",
            "arn": "arn:aws:iam::111122223333:user/Alice",
            "accountId": "111122223333",
            "accessKeyId": "EXAMPLE_KEY_ID",
            "userName": "Alice"
    },
    "eventTime": "2020-07-27T18:57:57Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateDataKeyPair",
    "awsRegion": "us-west-2",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "AWS Internal",
    "requestParameters": {
        "keyPairSpec": "RSA_3072",
        "encryptionContext": {
            "Project": "Alpha"
        },
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab"
    },
    "responseElements": null,
    "additionalEventData": {
        **"recipient": {
 "attestationDocumentModuleId": "i-123456789abcde123-enc123456789abcde12",
 "attestationDocumentEnclaveImageDigest": "<AttestationDocument.PCR0>",
 "attestationDocumentEnclavePCR1": "<AttestationDocument.PCR1>",
 "attestationDocumentEnclavePCR2": "<AttestationDocument.PCR2>",
 "attestationDocumentEnclavePCR3": "<AttestationDocument.PCR3>",
 "attestationDocumentEnclavePCR4": "<AttestationDocument.PCR4>",
 "attestationDocumentEnclavePCR8": "<AttestationDocument.PCR8>"
 }**
    },
    "requestID": "52fb127b-0fe5-42bb-8e5e-f560febde6b0",
    "eventID": "9b6bd6d2-529d-4890-a949-593b13800ad7",
    "readOnly": true,
    "resources": [
        {
            "accountId": "111122223333",
            "type": "AWS::KMS::Key",
            "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

[Show moreShow less](# "#")

## GenerateRandom (for an enclave)

The following example shows an AWS CloudTrail log entry of a [GenerateRandom](../APIReference/API_GenerateRandom.md "../APIReference/API_GenerateRandom.md") operation for an AWS Nitro enclave.

```
{
    "eventVersion": "1.02",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "userName": "Alice"
    },
    "eventTime": "2014-11-04T00:52:37Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "GenerateRandom",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "AWS Internal",
    "requestParameters": null,
    "responseElements": null,
    "additionalEventData": {
        **"recipient": {
 "attestationDocumentModuleId": "i-123456789abcde123-enc123456789abcde12",
 "attestationDocumentEnclaveImageDigest": "<AttestationDocument.PCR0>",
 "attestationDocumentEnclavePCR1": "<AttestationDocument.PCR1>",
 "attestationDocumentEnclavePCR2": "<AttestationDocument.PCR2>",
 "attestationDocumentEnclavePCR3": "<AttestationDocument.PCR3>",
 "attestationDocumentEnclavePCR4": "<AttestationDocument.PCR4>",
 "attestationDocumentEnclavePCR8": "<AttestationDocument.PCR8>"
 }**
    },
    "requestID": "df1e3de6-63bc-11e4-bc2b-4198b6150d5c",
    "eventID": "239cb9f7-ae05-4c94-9221-6ea30eef0442",
    "readOnly": true,
    "resources": [],
    "eventType": "AwsApiCall",
    "recipientAccountId": "111122223333"
}
```

[Show moreShow less](# "#")



# Decapsulate
<a name="ct-decapsulate"></a>

The following example shows an AWS CloudTrail log entry for the [Decapsulate](https://docs.aws.amazon.com/kms/latest/APIReference/API_Decapsulate.html) operation. The encapsulated shared secret passed in the request is omitted from the log entry.

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "EX_PRINCIPAL_ID",
        "arn": "arn:aws:iam::111122223333:user/Alice",
        "accountId": "111122223333",
        "accessKeyId": "EXAMPLE_KEY_ID",
        "userName": "Alice"
    },
    "eventTime": "2026-10-18T19:10:44Z",
    "eventSource": "kms.amazonaws.com",
    "eventName": "Decapsulate",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "aws-sdk-java/2.30.22 md/io#async md/http#AwsCommonRuntime ...",
    "requestParameters": {
        "keyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "encapsulationAlgorithm": "ML_KEM"
    },
    "responseElements": null,
    "requestID": "23456237-41e6-4c39-a9c0-a264eb660a74",
    "eventID": "bcdef313-cb2b-478d-c5cb-a830e56bf632",
    "readOnly": true,
    "resources": [{
        "accountId": "111122223333",
        "type": "AWS::KMS::Key",
        "ARN": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": true,
    "recipientAccountId": "111122223333",
    "eventCategory": "Management",
    "tlsDetails": {
        "tlsVersion": "TLSv1.3",
        "cipherSuite": "TLS_AES_256_GCM_SHA384",
        "clientProvidedHostHeader": "kms.us-east-1.amazonaws.com",
        "keyExchange": "X25519MLKEM768"
    }
}
```
# CloudTrail log file example for S3 Vectors

The following examples show CloudTrail log entries for S3 Vectors data events. Data events are logged when you perform operations on vector data within your vector indexes.

## Example: CloudTrail log file for `GetVectors` data event

```
{
    "eventVersion": "1.11",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "`123456789012`",
        "arn": "arn:aws:iam::123456789012:user/`myUserName`",
        "accountId": "123456789012",
        "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
        "userName": "`myUserName`"
    },
    "eventTime": "2024-11-22T17:12:25Z",
    "eventSource": "s3vectors.amazonaws.com",
    "eventName": "GetVectors",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "192.0.2.0",
    "userAgent": "[aws-cli/2.18.5]",
    "requestParameters": {
        "vectorBucketName": "amzn-s3-demo-vector-bucket",
        "returnMetadata": "false",
        "indexName": "`111aa1111-22bb-33cc-44dd-5555eee66ffff`",
        "returnData": "false"
    },
    "responseElements": null,
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256"
    },
    "requestID": "07D681123BD12AED",
    "eventID": "f2b287f3-0df1-1234-a2f4-c4bdfed47657",
    "readOnly": true,
    "resources": [{
        "accountId": "123456789012",
        "type": "AWS::S3Vectors::VectorBucket",
        "ARN": "arn:aws:s3vectors:us-east-1:123456789012:bucket/`amzn-s3-demo-vector-bucket`"
    }, {
        "accountId": "123456789012",
        "type": "AWS::S3Vectors::Index",
        "ARN": "arn:aws:s3vectors:us-east-1:123456789012:bucket/`amzn-s3-demo-vector-bucket`/index/`111aa1111-22bb-33cc-44dd-5555eee66ffff`"
    }],
    "eventType": "AwsApiCall",
    "managementEvent": false,
    "recipientAccountId": "444455556666",
    "eventCategory": "Data",
    "tlsDetails": {
        "tlsVersion": "TLSv1.2",
        "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "clientProvidedHostHeader": "`client-host`"
    }
}
```

## Understanding S3 Vectors log file entries

CloudTrail log files contain one or more log entries. An event represents a single request from any source and includes information about the requested action, the date and time of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so they don't appear in any specific order.

S3 Vectors CloudTrail log entries contain the following key elements:

- **eventSource** - Always `s3vectors.amazonaws.com` for S3 Vectors events.
- **eventName** - The S3 Vectors API operation that was performed.
- **eventCategory** - Either `Management` for control plane operations or `Data` for data plane operations.
- **readOnly**: `true` for read operations (for examples, [GetVectors](../API/API_S3VectorBuckets_GetVectors.md "../API/API_S3VectorBuckets_GetVectors.md"), [QueryVectors](../API/API_S3VectorBuckets_QueryVectors.md "../API/API_S3VectorBuckets_QueryVectors.md"), [ListVectors](../API/API_S3VectorBuckets_ListVectors.md "../API/API_S3VectorBuckets_ListVectors.md")) and `false` for write operations ([PutVectors](../API/API_S3VectorBuckets_PutVectors.md "../API/API_S3VectorBuckets_PutVectors.md"), [DeleteVectors](../API/API_S3VectorBuckets_DeleteVectors.md "../API/API_S3VectorBuckets_DeleteVectors.md")).
- **resources** - The S3 Vectors resources involved in the operation, including vector buckets and vector indexes.
- **requestParameters** - The parameters that were sent with the request.
- **responseElements** - The response elements returned by the S3 Vectors service.

# Logging AWS KMS requests that use a VPC endpoint

AWS CloudTrail logs all operations that use the VPC endpoint. When a request to AWS KMS uses a VPC
endpoint, the VPC endpoint ID appears in the [AWS CloudTrail
log](logging-using-cloudtrail.md "logging-using-cloudtrail.md") entry that records the request. You can use the endpoint ID to audit the use of
your AWS KMS VPC endpoint.

However, your CloudTrail logs don't include operations requested by principals in other accounts
or requests for AWS KMS operations on KMS keys and aliases in other accounts. Also, to protect
your VPC, requests that are denied by a VPC endpoint
policy, but otherwise would have been allowed, are not recorded in [AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

For example, this sample log entry records a [GenerateDataKey](../APIReference/API_GenerateDataKey.md "../APIReference/API_GenerateDataKey.md") request that used the
VPC endpoint. The `vpcEndpointId` field appears at the end of the log entry.

```
{
  "eventVersion":"1.05",
  "userIdentity": {
    "type": "IAMUser",
    "principalId": "EX_PRINCIPAL_ID",
    "arn": "arn:aws:iam::111122223333:user/Alice",
    "accessKeyId": "EXAMPLE_KEY_ID",
    "accountId": "111122223333",
    "userName": "Alice"
  },
  "eventTime":"2018-01-16T05:46:57Z",
  "eventSource":"kms.amazonaws.com",
  "eventName":"GenerateDataKey",
  "awsRegion":"eu-west-1",
  "sourceIPAddress":"172.01.01.001",
  "userAgent":"aws-cli/1.14.23 Python/2.7.12 Linux/4.9.75-25.55.amzn1.x86_64 botocore/1.8.27",
  "requestParameters":{
    "keyId":"1234abcd-12ab-34cd-56ef-1234567890ab",
    "numberOfBytes":128
  },
  "responseElements":null,
  "requestID":"a9fff0bf-fa80-11e7-a13c-afcabff2f04c",
  "eventID":"77274901-88bc-4e3f-9bb6-acf1c16f6a7c",
  "readOnly":true,
  "resources":[{
    "ARN":"arn:aws:kms:eu-west-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "accountId":"111122223333",
    "type":"AWS::KMS::Key"
  }],
  "eventType":"AwsApiCall",
  "recipientAccountId":"111122223333",
  **"vpcEndpointId": "vpce-1234abcdf5678c90a"**
}
```

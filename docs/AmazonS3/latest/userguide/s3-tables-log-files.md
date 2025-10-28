# AWS CloudTrail data event log file examples for S3 Tables

A AWS CloudTrail log file includes information about the requested API operation, the date and
time of the operation, request parameters, and so on. This topic provides example log files for
CloudTrail data events for S3 Tables.

###### Topics

- [Example – CloudTrail log file for GetObject data event](#example-ct-log-s3tables "#example-ct-log-s3tables")
- [Example – CloudTrail log file for a table maintenance management event](#example-ct-log-s3tables-3 "#example-ct-log-s3tables-3")
- [Example – CloudTrail log file for PutObject data event](#example-ct-log-s3tables-2 "#example-ct-log-s3tables-2")

## Example – CloudTrail log file for `GetObject` data event

The following example shows a CloudTrail log file example that demonstrates the [`GetObject`](../API/API_GetObject.md "../API/API_GetObject.md") API operation.

```
    {
        "eventVersion": "1.11",
        "userIdentity": {
          "type": "IAMUser",
          "principalId": "`123456789012`",
          "arn": "arn:aws:iam::`111122223333`:user/"`myUserName`",
          "accountId": "`111122223333`",
          "accessKeyId": "`AKIAIOSFODNN7EXAMPLE`",
          "userName":"`myUserName`"
        },
        "eventTime": "2024-11-22T17:12:25Z",
        "eventSource": "s3tables.amazonaws.com",
        "eventName": "GetObject",
        "awsRegion": "`us-east-1`",
        "sourceIPAddress": "`192.0.2.0`",
        "userAgent": "[aws-cli/2.18.5]",
        "requestParameters": {
            "Host": "tableWarehouseLocation.s3.us-east-1.amazonaws.com",
            "key": "product-info.json"
        },
        "responseElements":  null,
        "additionalEventData": {
            "SignatureVersion": "SigV4",
            "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "bytesTransferredIn": 0,
            "AuthenticationMethod": "AuthHeader",
            "xAmzId2": "q6xhNJYmhg",
            "bytesTransferredOut": 28441

          },
          "requestID": "07D681123BD12AED",
          "eventID": "f2b287f3-0df1-1234-a2f4-c4bdfed47657",
          "readOnly": true,
          "resources": [{
              "accountId": "111122223333",
              "type": "AWS::S3Tables::TableBucket",
               "ARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket1`"
           }, {
              "accountId": "111122223333",
              "type": "AWS::S3Tables::Table",
              "ARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-bucket`/table/111aa1111-22bb-33cc-44dd-5555eee66ffff"

           }],
           "eventType": "AwsApiCall",
           "managementEvent": false,
           "recipientAccountId": "444455556666",
           "eventCategory": "Data",
           "tlsDetails": {
             "tlsVersion": "TLSv1.2",
             "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
             "clientProvidedHostHeader": "tableWarehouseLocation.s3.us-east-1.amazonaws.com"
          }
    }
```

## Example – CloudTrail log file for a table maintenance management event

The following is a CloudTrail log file example that demonstrates a maintenance event for table compaction performed by S3 as part of automatic table maintenance. For more information on events for table maintenance, see [CloudTrail management events for S3 Tables maintenance](s3-tables-logging.md#s3-tables-maintenance-events "s3-tables-logging.md#s3-tables-maintenance-events")

```
{
  "eventVersion": "1.11",
  "userIdentity": {
    "type": "AWSService",
    "invokedBy": "maintenance.s3tables.amazonaws.com"
  },
  "eventTime": "`2025-09-18T20:13:14Z`",
  "eventSource": "s3tables.amazonaws.com",
  "eventName": "TablesMaintenanceEvent",
  "awsRegion": "`us-east-1`",
  "sourceIPAddress": "maintenance.s3tables.amazonaws.com",
  "userAgent": "maintenance.s3tables.amazonaws.com",
  "requestParameters": null,
  "responseElements": null,
  "eventID": "`b8f96329-ef5c-32b5-94f6-eeed9061ea32`",
  "readOnly": false,
  "resources": [
    {
      "accountId": "`111122223333`",
      "type": "AWS::S3Tables::TableBucket",
      "ARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`"
    },
    {
      "accountId": "`111122223333`",
      "type": "AWS::S3Tables::Table",
      "ARN": "arn:aws:s3tables:`us-east-1`:`111122223333`:bucket/`amzn-s3-demo-table-bucket`/table/`7ff7750e-23b3-481e-a90a-7d87d423d336`"
    }
  ],
  "eventType": "AwsServiceEvent",
  "managementEvent": true,
  "recipientAccountId": "`111122223333`",
  "sharedEventID": "`62a57826-a66e-479b-befa-0e65663ee9e8`",
  "serviceEventDetails": {
    "activityType": "`icebergCompaction`"
  },
  "eventCategory": "Management"
}

```

## Example – CloudTrail log file for `PutObject` data event

The following example shows a CloudTrail log file example that demonstrates the [`PutObject`](../API/API_PutObject.md "../API/API_PutObject.md") API operation.

```
{
        "eventVersion": "1.11",
        "userIdentity": {
          "type": "IAMUser",
          "principalId": "`123456789012`",
          "arn":  "arn:aws:iam::`444455556666`:user/"`myUserName`",
          "accountId": "`444455556666`",
          "accessKeyId": "`AKIAI44QH8DHBEXAMPLE`",
          "userName":"`myUserName`"
        },
        "eventTime": "2024-11-22T17:12:25Z",
        "eventSource": "s3tables.amazonaws.com",
        "eventName": "PutObject",
        "awsRegion": "`us-east-1`",
        "sourceIPAddress": "`192.0.2.0`",
        "userAgent": "[aws-cli/2.18.5]",
        "requestParameters": {
            "Host": "tableWarehouseLocation.s3.us-east-1.amazonaws.com",
            "key": "product-info.json"
        },
        "responseElements":  {
            "x-amz-server-side-encryption": "AES256",
            "x-amz-version-id": "13zAFMdccAjt3MWd6ehxgCCCDRdkAKDw"
        },
        "additionalEventData": {
            "SignatureVersion": "SigV4",
            "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
            "bytesTransferredIn": 28441,
            "AuthenticationMethod": "AuthHeader",
            "xAmzId2": "q6xhCJYmhg",
            "bytesTransferredOut": 0

          },
          "requestID": "28d2faaf-1234-4649-997d-EXAMPLE72818",
          "eventID": "694d604a-d190-1234-0dd1-EXAMPLEe20c1",
          "readOnly": false,
          "resources": [{
              "accountId": "444455556666",
              "type": "AWS::S3Tables::TableBucket",
               "ARN": "arn:aws:s3tables:`us-east-1`:`444455556666`:bucket/`amzn-s3-demo-bucket1`"
           }, {
              "accountId": "444455556666",
              "type": "AWS::S3Tables::Table",
              "ARN": "arn:aws:s3tables:`us-east-1`:`444455556666`:bucket/`amzn-s3-demo-bucket1`/table/b89ec883-b1d9-4b37-9cd7-b86f590123f4"
           }],
           "eventType": "AwsApiCall",
           "managementEvent": false,
           "recipientAccountId": "111122223333",
           "eventCategory": "Data",
           "tlsDetails": {
             "tlsVersion": "TLSv1.2",
             "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
             "clientProvidedHostHeader": "tableWarehouseLocation.s3.us-east-1.amazonaws.com"
            }
          }
```

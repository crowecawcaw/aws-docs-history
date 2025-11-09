# Example: WorkSpaces Applications Log File Entries

A trail is a configuration that enables delivery of events as log files to an Amazon S3 bucket
that you specify. CloudTrail log files contain one or more log entries. An event represents a single
request from any source and includes information about the requested action, the date and time
of the action, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of
the public API calls, so they don't appear in any specific order.

The following example shows a CloudTrail log entry that demonstrates the `AssociateFleet` event.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "AIDACKCEVSQ6C2EXAMPLE:janeroe",
    "arn": "arn:aws:sts:: 123456789012:assumed-role/Admin/janeroe",
    "accountId": "123456789012",
    "accessKeyId": "AKIAIOSFODNN7EXAMPLE",
    "sessionContext": {
      "attributes": {
        "mfaAuthenticated": "false",
        "creationDate": "2019-03-12T06:41:50Z"
      },
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AIDACKCEVSQ6C2EXAMPLE",
        "arn": "arn:aws:iam:: 123456789012:role/Admin",
        "accountId": "123456789012",
        "userName": "Admin"
      }
    }
  },
  "eventTime": "2019-03-12T06:58:09Z",
  "eventSource": "appstream.amazonaws.com",
  "eventName": "AssociateFleet",
  "awsRegion": "us-east-1",
  "sourceIPAddress": "198.51.100.15",
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
  "requestParameters": {
    "fleetName": "ExampleFleet1",
    "stackName": "ExampleStack1"
  },
  "responseElements": null,
  "requestID": "3210a159-4494-11e9-8017-873084baf125",
  "eventID": "a6fbde60-a55a-46fe-87d4-89ead558dffd",
  "eventType": "AwsApiCall",
  "recipientAccountId": "123456789012"
}
```

The following example shows a CloudTrail log entry that demonstrates the
`CreateImage` event when an image is created using the WorkSpaces Applications image builder.

```
{
  "eventVersion": "1.05",
  "userIdentity": {
    "arn": "arn:aws:appstream:us-east-1: 123456789012:image-builder/ExampleImageBuilder",
    "accountId": "123456789012"
  },
  "eventTime": "2019-03-21T22:32:05Z",
  "eventSource": "appstream.amazonaws.com",
  "eventName": "CreateImage",
  "awsRegion": "us-east-1",
  "requestParameters": null,
  "responseElements": null,
  "eventID": "12b2d6e2-c9a9-402e-8886-2c388d3df610",
  "readOnly": false,
  "eventType": "AwsServiceEvent",
  "recipientAccountId": "123456789012",
  "serviceEventDetails": {
    "ImageName": "ExampleImage1",
    "ImagePlatform": "WINDOWS",
    "PublicBaseImageReleasedDate": "Tue Jan 15 22:19:56 UTC 2019",
    "ImageDisPlayName": "Example Image 1",
    "ImageBuilderSupported": "True",
    "ImageCreatedTime": "Thu Mar 21 22:32:05 UTC 2019",
    "ImageDescription": "Example image for testing",
    "ImageState": "PENDING"
  }
}
```

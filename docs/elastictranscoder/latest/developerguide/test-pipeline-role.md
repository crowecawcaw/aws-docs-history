End of support notice: On November 13, 2025, AWS will discontinue support for Amazon Elastic Transcoder. After November 13, 2025, you will no longer be able to access the Elastic Transcoder console or Elastic Transcoder resources.

For more information about transitioning to AWS Elemental MediaConvert, visit this [blog post](https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/ "https://aws.amazon.com/blogs/media/how-to-migrate-workflows-from-amazon-elastic-transcoder-to-aws-elemental-mediaconvert/").

# Test Role

###### Topics

- [Description](#test-pipeline-role-description "#test-pipeline-role-description")
- [Requests](#test-pipeline-role-requests "#test-pipeline-role-requests")
- [Responses](#test-pipeline-role-responses "#test-pipeline-role-responses")
- [Errors](#test-pipeline-role-response-errors "#test-pipeline-role-response-errors")
- [Examples](#test-pipeline-role-examples "#test-pipeline-role-examples")

## Description

To test the settings for a pipeline to ensure that Elastic Transcoder can create and process jobs, send a POST request to the
`/2012-09-25/roleTests` resource.

## Requests

### Syntax

```
POST /2012-09-25/roleTests HTTP/1.1
Content-Type: application/json; charset=UTF-8
Accept: */*
Host: elastictranscoder.`Elastic Transcoder endpoint`.amazonaws.com:443
x-amz-date: 20130114T174952Z
Authorization: AWS4-HMAC-SHA256
               Credential=`AccessKeyID`/`request-date`/`Elastic Transcoder endpoint`/elastictranscoder/aws4_request,
               SignedHeaders=host;x-amz-date;x-amz-target,
               Signature=`calculated-signature`
Content-Length: `number of characters in the JSON string`
{
   "InputBucket":"`Amazon S3 bucket that contains files to transcode`",
   "OutputBucket":"`Amazon S3 bucket in which to save transcoded files`",
   "Role":"`IAM ARN for the role to test`",
   "Topics": [
      "`ARN of SNS topic to test`"
   ]
}
```

### Request Parameters

This operation does not use request parameters.

### Request Headers

This operation uses only request headers that are common to all operations.
For information about common request headers, see [HTTP Header Contents](making-http-requests.md#http-request-header "making-http-requests.md#http-request-header").

### Request Body

The JSON string in the request body contains the following objects.

**InputBucket**

The Amazon S3 bucket in which you saved the media files that you want to transcode. `Test Role`
tries to read from this bucket.

**OutputBucket**

The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. `Test Role`
tries to read from this bucket.

**Role**

The IAM Amazon Resource Name (ARN) for the role that you want Elastic Transcoder to use to transcode jobs. `Test Role`
tries to assume the specified role.

**Topics**

The ARNs of one or more Amazon Simple Notification Service (Amazon SNS) topics to which you want `Test Role` to send
test notifications. If you aren't using Amazon SNS notifications, you can specify an empty list.

## Responses

### Syntax

```
Status: 200 OK
x-amzn-RequestId: c321ec43-378e-11e2-8e4c-4d5b971203e9
Content-Type: application/json
Content-Length: `number of characters in the response`
Date: Mon, 14 Jan 2013 06:01:47 GMT

{
   "Messages": [
      "`error messages, if any`"
   ],
   "Success": "true | false"
}
```

### Response Headers

This operation uses only response headers that are common to most responses.
For information about common response headers, see [HTTP Responses](making-http-requests.md#http-response-header "making-http-requests.md#http-response-header").

### Response Body

When you test settings for a pipeline, Elastic Transcoder returns the following values.

**Messages**

If the value of `Success` is `false`, `Messages` contains an array of one or more
messages that explain which tests failed.

**Success**

If the operation is successful, this value is `true`; otherwise, the value is `false`.

## Errors

For information about Elastic Transcoder exceptions and error messages, see [Handling Errors in Elastic Transcoder](error-handling.md "error-handling.md").

## Examples

### Sample Request

```
POST /2012-09-25/roleTests HTTP/1.1
Content-Type: application/json; charset=UTF-8
Accept: */*
Host: elastictranscoder.`Elastic Transcoder endpoint`.amazonaws.com:443
x-amz-date: 20130114T174952Z
Authorization: AWS4-HMAC-SHA256
               Credential=`AccessKeyID`/`request-date`/`Elastic Transcoder endpoint`/elastictranscoder/aws4_request,
               SignedHeaders=host;x-amz-date;x-amz-target,
               Signature=`calculated-signature`
Content-Length: `number of characters in the JSON string`
{
   "InputBucket":"salesoffice.example.com-source",
   "OutputBucket":"salesoffice.example.com-public-promos",
   "Role":"arn:aws:iam::123456789012:role/transcode-service",
   "Topics":
      ["arn:aws:sns:us-east-1:111222333444:ETS_Errors",
       "arn:aws:sns:us-east-1:111222333444:ETS_Progressing"]
}
```

### Sample Response

```
Status: 201 Created
x-amzn-RequestId: c321ec43-378e-11e2-8e4c-4d5b971203e9
Content-Type: application/json
Content-Length: `number of characters in the response`
Date: Mon, 14 Jan 2013 06:01:47 GMT
{
   "Messages":[
      "The role arn:aws:iam::123456789012:role/transcode-service does not have access to the bucket: salesoffice.example.com-source",
      "The role arn:aws:iam::123456789012:role/transcode-service does not have access to the topic: arn:aws:sns:us-east-1:111222333444:ETS_Errors"
   ],
   "Success": "false"
}
```

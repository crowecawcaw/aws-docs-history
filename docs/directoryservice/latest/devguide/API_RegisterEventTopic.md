# RegisterEventTopic

Associates a directory with an Amazon SNS topic. This establishes the directory as a
publisher to the specified Amazon SNS topic. You can then receive email or text (SMS) messages when
the status of your directory changes. You get notified if your directory goes from an Active
status to an Impaired or Inoperable status. You also receive a notification when the directory
returns to an Active status.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "TopicName": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_RegisterEventTopic_RequestSyntax "#API_RegisterEventTopic_RequestSyntax")**

The Directory ID that will publish status messages to the Amazon SNS topic.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[TopicName](#API_RegisterEventTopic_RequestSyntax "#API_RegisterEventTopic_RequestSyntax")**

The Amazon SNS topic name to which the directory will publish status messages. This Amazon SNS
topic must be in the same region as the specified Directory ID.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `[a-zA-Z0-9_-]+`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of RegisterEventTopic.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 63
X-Amz-Target: DirectoryService_20150416.RegisterEventTopic
X-Amz-Date: 20161214T232258Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=6e1e2996789f568cf057fa66e70b1ba114d7388510787be6092055ab97a07828

 {
   "DirectoryId": "d-926example",
   "TopicName": "snstopicexample"
 }
```

### Example Response

This example illustrates one usage of RegisterEventTopic.

```
HTTP/1.1 200 OK
x-amzn-RequestId: a68a1e79-c19b-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Wed, 14 Dec 2016 23:23:01 GMT

{

}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/RegisterEventTopic.md "../../../goto/cli2/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/RegisterEventTopic.md "../../../goto/DotNetSDKV4/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForCpp/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForGoV2/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForJavaV2/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForKotlin/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForPHPV3/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/RegisterEventTopic.md "../../../goto/boto3/ds-2015-04-16/RegisterEventTopic.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/RegisterEventTopic.md "../../../goto/SdkForRubyV3/ds-2015-04-16/RegisterEventTopic.md")

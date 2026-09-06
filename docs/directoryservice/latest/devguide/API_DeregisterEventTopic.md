

# DeregisterEventTopic
<a name="API_DeregisterEventTopic"></a>

Removes the specified directory as a publisher to the specified Amazon SNS topic.

## Request Syntax
<a name="API_DeregisterEventTopic_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "TopicName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeregisterEventTopic_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DeregisterEventTopic_RequestSyntax) **   <a name="DirectoryService-DeregisterEventTopic-request-DirectoryId"></a>
The Directory ID to remove as a publisher. This directory will no longer send messages to the specified Amazon SNS topic.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [TopicName](#API_DeregisterEventTopic_RequestSyntax) **   <a name="DirectoryService-DeregisterEventTopic-request-TopicName"></a>
The name of the Amazon SNS topic from which to remove the directory as a publisher.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: Yes

## Response Elements
<a name="API_DeregisterEventTopic_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterEventTopic_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** EntityDoesNotExistException **   
The specified entity could not be found.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidParameterException **   
One or more parameters are not valid.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** ServiceException **   
An exception has occurred in AWS Directory Service.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 500

## Examples
<a name="API_DeregisterEventTopic_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DeregisterEventTopic_Example_1"></a>

This example illustrates one usage of DeregisterEventTopic.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 52
X-Amz-Target: DirectoryService_20150416.DeregisterEventTopic
X-Amz-Date: 20161214T014408Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=e3b8ad858165a3dd7d4fb35b0adf17bee8d71aed26b0f49e6db792ed8b10f8b1

 {
   "DirectoryId": "d-926example",
   "TopicName": "snstopicexample"
 }
```

### Example Response
<a name="API_DeregisterEventTopic_Example_2"></a>

This example illustrates one usage of DeregisterEventTopic.

```
HTTP/1.1 200 OK
x-amzn-RequestId: a68a1e79-c19b-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Wed, 14 Dec 2016 01:44:10 GMT

{  
  
}
```

## See Also
<a name="API_DeregisterEventTopic_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DeregisterEventTopic) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DeregisterEventTopic) 
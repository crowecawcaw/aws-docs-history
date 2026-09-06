

# DescribeEventTopics
<a name="API_DescribeEventTopics"></a>

Obtains information about which Amazon SNS topics receive status messages from the specified directory.

If no input parameters are provided, such as DirectoryId or TopicName, this request describes all of the associations in the account.

## Request Syntax
<a name="API_DescribeEventTopics_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "TopicNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeEventTopics_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeEventTopics_RequestSyntax) **   <a name="DirectoryService-DescribeEventTopics-request-DirectoryId"></a>
The Directory ID for which to get the list of associated Amazon SNS topics. If this member is null, associations for all Directory IDs are returned.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** [TopicNames](#API_DescribeEventTopics_RequestSyntax) **   <a name="DirectoryService-DescribeEventTopics-request-TopicNames"></a>
A list of Amazon SNS topic names for which to obtain the information. If this member is null, all associations for the specified Directory ID are returned.  
An empty list results in an `InvalidParameterException` being thrown.  
Type: Array of strings  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9_-]+`   
Required: No

## Response Syntax
<a name="API_DescribeEventTopics_ResponseSyntax"></a>

```
{
   "EventTopics": [ 
      { 
         "CreatedDateTime": number,
         "DirectoryId": "string",
         "Status": "string",
         "TopicArn": "string",
         "TopicName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeEventTopics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [EventTopics](#API_DescribeEventTopics_ResponseSyntax) **   <a name="DirectoryService-DescribeEventTopics-response-EventTopics"></a>
A list of Amazon SNS topic names that receive status messages from the specified Directory ID.  
Type: Array of [EventTopic](API_EventTopic.md) objects

## Errors
<a name="API_DescribeEventTopics_Errors"></a>

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
<a name="API_DescribeEventTopics_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeEventTopics_Example_1"></a>

This example illustrates one usage of DescribeEventTopics.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 66
X-Amz-Target: DirectoryService_20150416.DescribeEventTopics
X-Amz-Date: 20161214T025225Z
User-Agent: aws-cli/1.11.24 Python/2.7.9 Windows/7 botocore/1.4.81
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256 
 Credential=AKIAI7E3BYXS3example/20161214/us-west-2/ds/aws4_request, 
 SignedHeaders=content-type;host;x-amz-date;x-amz-target, 
 Signature=d04fcf5cf8439dd8d0503933cab61c2bad6d6b29b9e1e5dca25f6d6de1704e17

 {
   "DirectoryId": "d-926example",
   "TopicNames": "snstopicexample"
 }
```

### Example Response
<a name="API_DescribeEventTopics_Example_2"></a>

This example illustrates one usage of DescribeEventTopics.

```
HTTP/1.1 200 OK
x-amzn-RequestId: a68a1e79-c19b-11e6-870b-c3330207df37
Content-Type: application/x-amz-json-1.1
Content-Length: 29
Date: Wed, 14 Dec 2016 02:52:27 GMT

{  
  "EventTopics": ["eventtopicexample"]
}
```

## See Also
<a name="API_DescribeEventTopics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeEventTopics) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeEventTopics) 


# DescribeHybridADUpdate
<a name="API_DescribeHybridADUpdate"></a>

Retrieves information about update activities for a hybrid directory. This operation provides details about configuration changes, administrator account updates, and self-managed instance settings (IDs and DNS IPs).

## Request Syntax
<a name="API_DescribeHybridADUpdate_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "NextToken": "{{string}}",
   "UpdateType": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeHybridADUpdate_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_DescribeHybridADUpdate_RequestSyntax) **   <a name="DirectoryService-DescribeHybridADUpdate-request-DirectoryId"></a>
The identifier of the hybrid directory for which to retrieve update information.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: Yes

 ** [NextToken](#API_DescribeHybridADUpdate_RequestSyntax) **   <a name="DirectoryService-DescribeHybridADUpdate-request-NextToken"></a>
The pagination token from a previous request to [DescribeHybridADUpdate](#API_DescribeHybridADUpdate). Pass null if this is the first request.  
Type: String  
Required: No

 ** [UpdateType](#API_DescribeHybridADUpdate_RequestSyntax) **   <a name="DirectoryService-DescribeHybridADUpdate-request-UpdateType"></a>
The type of update activities to retrieve. Valid values include `SelfManagedInstances` and `HybridAdministratorAccount`.  
Type: String  
Valid Values: `SelfManagedInstances | HybridAdministratorAccount`   
Required: No

## Response Syntax
<a name="API_DescribeHybridADUpdate_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "UpdateActivities": { 
      "HybridAdministratorAccount": [ 
         { 
            "AssessmentId": "string",
            "InitiatedBy": "string",
            "LastUpdatedDateTime": number,
            "NewValue": { 
               "DnsIps": [ "string" ],
               "InstanceIds": [ "string" ]
            },
            "PreviousValue": { 
               "DnsIps": [ "string" ],
               "InstanceIds": [ "string" ]
            },
            "StartTime": number,
            "Status": "string",
            "StatusReason": "string"
         }
      ],
      "SelfManagedInstances": [ 
         { 
            "AssessmentId": "string",
            "InitiatedBy": "string",
            "LastUpdatedDateTime": number,
            "NewValue": { 
               "DnsIps": [ "string" ],
               "InstanceIds": [ "string" ]
            },
            "PreviousValue": { 
               "DnsIps": [ "string" ],
               "InstanceIds": [ "string" ]
            },
            "StartTime": number,
            "Status": "string",
            "StatusReason": "string"
         }
      ]
   }
}
```

## Response Elements
<a name="API_DescribeHybridADUpdate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeHybridADUpdate_ResponseSyntax) **   <a name="DirectoryService-DescribeHybridADUpdate-response-NextToken"></a>
If not null, more results are available. Pass this value for the `NextToken` parameter in a subsequent request to retrieve the next set of items.  
Type: String

 ** [UpdateActivities](#API_DescribeHybridADUpdate_ResponseSyntax) **   <a name="DirectoryService-DescribeHybridADUpdate-response-UpdateActivities"></a>
Information about update activities for the hybrid directory, organized by update type.  
Type: [HybridUpdateActivities](API_HybridUpdateActivities.md) object

## Errors
<a name="API_DescribeHybridADUpdate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ClientException **   
A client exception has occurred.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** DirectoryDoesNotExistException **   
The specified directory does not exist in the system.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
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

 ** UnsupportedOperationException **   
The operation is not supported.    
 ** Message **   
The descriptive message for the exception.  
 ** RequestId **   
The AWS request identifier.
HTTP Status Code: 400

## Examples
<a name="API_DescribeHybridADUpdate_Examples"></a>

The following examples are formatted for legibility.

### Example Request
<a name="API_DescribeHybridADUpdate_Example_1"></a>

This example illustrates one usage of DescribeHybridADUpdate.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 95
X-Amz-Target: DirectoryService_20150416.DescribeHybridADUpdate
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAIOSFODNN7EXAMPLE/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
    "DirectoryId": "d-926example",
    "UpdateType": "HybridAdministratorAccount"
}
```

### Example Response
<a name="API_DescribeHybridADUpdate_Example_2"></a>

This example illustrates one usage of DescribeHybridADUpdate.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 456
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "HybridActivities": {
        "HybridAdministratorAccount": [
            {
                "Status": "UPDATE_REQUESTED",
                "InitiatedBy": "061086805150",
                "StartTime": "2025-07-14T20:27:59.002000-04:00",
                "LastUpdatedDateTime": "2025-07-14T20:27:59.002000-04:00",
                "AssessmentId": "da-1234567890example1"
            }
        ]
    }
}
```

## See Also
<a name="API_DescribeHybridADUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/DescribeHybridADUpdate) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/DescribeHybridADUpdate) 
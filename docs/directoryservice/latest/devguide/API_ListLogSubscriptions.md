

# ListLogSubscriptions
<a name="API_ListLogSubscriptions"></a>

Lists the active log subscriptions for the AWS account.

## Request Syntax
<a name="API_ListLogSubscriptions_RequestSyntax"></a>

```
{
   "DirectoryId": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListLogSubscriptions_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [DirectoryId](#API_ListLogSubscriptions_RequestSyntax) **   <a name="DirectoryService-ListLogSubscriptions-request-DirectoryId"></a>
If a *DirectoryID* is provided, lists only the log subscription associated with that directory. If no *DirectoryId* is provided, lists all log subscriptions associated with your AWS account. If there are no log subscriptions for the AWS account or the directory, an empty list will be returned.  
Type: String  
Pattern: `^d-[0-9a-f]{10}$`   
Required: No

 ** [Limit](#API_ListLogSubscriptions_RequestSyntax) **   <a name="DirectoryService-ListLogSubscriptions-request-Limit"></a>
The maximum number of items returned.  
Type: Integer  
Valid Range: Minimum value of 0.  
Required: No

 ** [NextToken](#API_ListLogSubscriptions_RequestSyntax) **   <a name="DirectoryService-ListLogSubscriptions-request-NextToken"></a>
The token for the next set of items to return.  
Type: String  
Required: No

## Response Syntax
<a name="API_ListLogSubscriptions_ResponseSyntax"></a>

```
{
   "LogSubscriptions": [ 
      { 
         "DirectoryId": "string",
         "LogGroupName": "string",
         "SubscriptionCreatedDateTime": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListLogSubscriptions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LogSubscriptions](#API_ListLogSubscriptions_ResponseSyntax) **   <a name="DirectoryService-ListLogSubscriptions-response-LogSubscriptions"></a>
A list of active [LogSubscription](API_LogSubscription.md) objects for calling the AWS account.  
Type: Array of [LogSubscription](API_LogSubscription.md) objects

 ** [NextToken](#API_ListLogSubscriptions_ResponseSyntax) **   <a name="DirectoryService-ListLogSubscriptions-response-NextToken"></a>
The token for the next set of items to return.  
Type: String

## Errors
<a name="API_ListLogSubscriptions_Errors"></a>

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

 ** InvalidNextTokenException **   
The `NextToken` value is not valid.    
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

## See Also
<a name="API_ListLogSubscriptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ds-2015-04-16/ListLogSubscriptions) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ds-2015-04-16/ListLogSubscriptions) 
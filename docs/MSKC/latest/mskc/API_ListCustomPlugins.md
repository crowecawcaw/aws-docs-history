

# ListCustomPlugins
<a name="API_ListCustomPlugins"></a>

Returns a list of all of the custom plugins in this account and Region.

## Request Syntax
<a name="API_ListCustomPlugins_RequestSyntax"></a>

```
GET /v1/custom-plugins?maxResults={{maxResults}}&namePrefix={{namePrefix}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCustomPlugins_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListCustomPlugins_RequestSyntax) **   <a name="MSKC-ListCustomPlugins-request-uri-maxResults"></a>
The maximum number of custom plugins to list in one response.  
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [namePrefix](#API_ListCustomPlugins_RequestSyntax) **   <a name="MSKC-ListCustomPlugins-request-uri-namePrefix"></a>
Lists custom plugin names that start with the specified text string.

 ** [nextToken](#API_ListCustomPlugins_RequestSyntax) **   <a name="MSKC-ListCustomPlugins-request-uri-nextToken"></a>
If the response of a ListCustomPlugins operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.

## Request Body
<a name="API_ListCustomPlugins_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCustomPlugins_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "customPlugins": [ 
      { 
         "creationTime": "string",
         "customPluginArn": "string",
         "customPluginState": "string",
         "description": "string",
         "latestRevision": { 
            "contentType": "string",
            "creationTime": "string",
            "description": "string",
            "fileDescription": { 
               "fileMd5": "string",
               "fileSize": number
            },
            "location": { 
               "s3Location": { 
                  "bucketArn": "string",
                  "fileKey": "string",
                  "objectVersion": "string"
               }
            },
            "revision": number
         },
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListCustomPlugins_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [customPlugins](#API_ListCustomPlugins_ResponseSyntax) **   <a name="MSKC-ListCustomPlugins-response-customPlugins"></a>
An array of custom plugin descriptions.  
Type: Array of [CustomPluginSummary](API_CustomPluginSummary.md) objects

 ** [nextToken](#API_ListCustomPlugins_ResponseSyntax) **   <a name="MSKC-ListCustomPlugins-response-nextToken"></a>
If the response of a ListCustomPlugins operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where the previous operation left off.  
Type: String

## Errors
<a name="API_ListCustomPlugins_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **   
HTTP Status Code 400: Bad request due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 400

 ** ForbiddenException **   
HTTP Status Code 403: Access forbidden. Correct your credentials and then retry your request.  
HTTP Status Code: 403

 ** InternalServerErrorException **   
HTTP Status Code 500: Unexpected internal server error. Retrying your request might resolve the issue.  
HTTP Status Code: 500

 ** NotFoundException **   
HTTP Status Code 404: Resource not found due to incorrect input. Correct your request and then retry it.  
HTTP Status Code: 404

 ** ServiceUnavailableException **   
HTTP Status Code 503: Service Unavailable. Retrying your request in some time might resolve the issue.  
HTTP Status Code: 503

 ** TooManyRequestsException **   
HTTP Status Code 429: Limit exceeded. Resource limit reached.  
HTTP Status Code: 429

 ** UnauthorizedException **   
HTTP Status Code 401: Unauthorized request. The provided credentials couldn't be validated.  
HTTP Status Code: 401

## See Also
<a name="API_ListCustomPlugins_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/kafkaconnect-2021-09-14/ListCustomPlugins) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kafkaconnect-2021-09-14/ListCustomPlugins) 
# GetAccessPointScope

 Returns the access point scope for a directory bucket.

To use this operation, you must have the permission to perform the
 `s3express:GetAccessPointScope`
 action.

For information about REST API errors, see [REST error responses](ErrorResponses.md#RESTErrorResponses "ErrorResponses.md#RESTErrorResponses").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspoint/`name`/scope HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetAccessPointScope_RequestSyntax "#API_control_GetAccessPointScope_RequestSyntax")**


The name of the access point with the scope you want to retrieve.


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetAccessPointScope_RequestSyntax "#API_control_GetAccessPointScope_RequestSyntax")**


 The AWS account ID that owns the access point with the scope that you want to retrieve.
 


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessPointScopeResult](#AmazonS3-control_GetAccessPointScope-response-GetAccessPointScopeResult "#AmazonS3-control_GetAccessPointScope-response-GetAccessPointScopeResult")>
   <[Scope](#AmazonS3-control_GetAccessPointScope-response-Scope "#AmazonS3-control_GetAccessPointScope-response-Scope")>
      <[Permissions](API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions "API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions")>
         <Permission>***string***</Permission>
      </[Permissions](API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions "API_control_Scope.md#AmazonS3-Type-control_Scope-Permissions")>
      <[Prefixes](API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes "API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes")>
         <Prefix>***string***</Prefix>
      </[Prefixes](API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes "API_control_Scope.md#AmazonS3-Type-control_Scope-Prefixes")>
   </[Scope](#AmazonS3-control_GetAccessPointScope-response-Scope "#AmazonS3-control_GetAccessPointScope-response-Scope")>
</[GetAccessPointScopeResult](#AmazonS3-control_GetAccessPointScope-response-GetAccessPointScopeResult "#AmazonS3-control_GetAccessPointScope-response-GetAccessPointScopeResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessPointScopeResult](#API_control_GetAccessPointScope_ResponseSyntax "#API_control_GetAccessPointScope_ResponseSyntax")**


Root level tag for the GetAccessPointScopeResult parameters.


Required: Yes




**[Scope](#API_control_GetAccessPointScope_ResponseSyntax "#API_control_GetAccessPointScope_ResponseSyntax")**


The contents of the access point scope.


Type: [Scope](API_control_Scope.md "API_control_Scope.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointScope")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointScope "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointScope")

# GetAccessPointForObjectLambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

###### Note

This operation is not supported by directory buckets.

Returns configuration information about the specified Object Lambda Access Point

The following actions are related to `GetAccessPointForObjectLambda`:


* [CreateAccessPointForObjectLambda](API_control_CreateAccessPointForObjectLambda.md "API_control_CreateAccessPointForObjectLambda.md")
* [DeleteAccessPointForObjectLambda](API_control_DeleteAccessPointForObjectLambda.md "API_control_DeleteAccessPointForObjectLambda.md")
* [ListAccessPointsForObjectLambda](API_control_ListAccessPointsForObjectLambda.md "API_control_ListAccessPointsForObjectLambda.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspointforobjectlambda/`name` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetAccessPointForObjectLambda_RequestSyntax "#API_control_GetAccessPointForObjectLambda_RequestSyntax")**


The name of the Object Lambda Access Point.


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessPointForObjectLambda_RequestSyntax "#API_control_GetAccessPointForObjectLambda_RequestSyntax")**


The account ID for the account that owns the specified Object Lambda Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessPointForObjectLambdaResult](#AmazonS3-control_GetAccessPointForObjectLambda-response-GetAccessPointForObjectLambdaResult "#AmazonS3-control_GetAccessPointForObjectLambda-response-GetAccessPointForObjectLambdaResult")>
   <[Name](#AmazonS3-control_GetAccessPointForObjectLambda-response-Name "#AmazonS3-control_GetAccessPointForObjectLambda-response-Name")>***string***</[Name](#AmazonS3-control_GetAccessPointForObjectLambda-response-Name "#AmazonS3-control_GetAccessPointForObjectLambda-response-Name")>
   <[PublicAccessBlockConfiguration](#AmazonS3-control_GetAccessPointForObjectLambda-response-PublicAccessBlockConfiguration "#AmazonS3-control_GetAccessPointForObjectLambda-response-PublicAccessBlockConfiguration")>
      <[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>***boolean***</[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>
      <[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>***boolean***</[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>
      <[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>***boolean***</[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>
      <[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>***boolean***</[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>
   </[PublicAccessBlockConfiguration](#AmazonS3-control_GetAccessPointForObjectLambda-response-PublicAccessBlockConfiguration "#AmazonS3-control_GetAccessPointForObjectLambda-response-PublicAccessBlockConfiguration")>
   <[CreationDate](#AmazonS3-control_GetAccessPointForObjectLambda-response-CreationDate "#AmazonS3-control_GetAccessPointForObjectLambda-response-CreationDate")>***timestamp***</[CreationDate](#AmazonS3-control_GetAccessPointForObjectLambda-response-CreationDate "#AmazonS3-control_GetAccessPointForObjectLambda-response-CreationDate")>
   <[Alias](#AmazonS3-control_GetAccessPointForObjectLambda-response-Alias "#AmazonS3-control_GetAccessPointForObjectLambda-response-Alias")>
      <[Status](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status")>***string***</[Status](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status")>
      <[Value](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value")>***string***</[Value](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value")>
   </[Alias](#AmazonS3-control_GetAccessPointForObjectLambda-response-Alias "#AmazonS3-control_GetAccessPointForObjectLambda-response-Alias")>
</[GetAccessPointForObjectLambdaResult](#AmazonS3-control_GetAccessPointForObjectLambda-response-GetAccessPointForObjectLambdaResult "#AmazonS3-control_GetAccessPointForObjectLambda-response-GetAccessPointForObjectLambdaResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessPointForObjectLambdaResult](#API_control_GetAccessPointForObjectLambda_ResponseSyntax "#API_control_GetAccessPointForObjectLambda_ResponseSyntax")**


Root level tag for the GetAccessPointForObjectLambdaResult parameters.


Required: Yes




**[Alias](#API_control_GetAccessPointForObjectLambda_ResponseSyntax "#API_control_GetAccessPointForObjectLambda_ResponseSyntax")**


The alias of the Object Lambda Access Point.


Type: [ObjectLambdaAccessPointAlias](API_control_ObjectLambdaAccessPointAlias.md "API_control_ObjectLambdaAccessPointAlias.md") data type




**[CreationDate](#API_control_GetAccessPointForObjectLambda_ResponseSyntax "#API_control_GetAccessPointForObjectLambda_ResponseSyntax")**


The date and time when the specified Object Lambda Access Point was created.


Type: Timestamp




**[Name](#API_control_GetAccessPointForObjectLambda_ResponseSyntax "#API_control_GetAccessPointForObjectLambda_ResponseSyntax")**


The name of the Object Lambda Access Point.


Type: String


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`





**[PublicAccessBlockConfiguration](#API_control_GetAccessPointForObjectLambda_ResponseSyntax "#API_control_GetAccessPointForObjectLambda_ResponseSyntax")**


Configuration to block all public access. This setting is turned on and can not be
 edited. 


Type: [PublicAccessBlockConfiguration](API_control_PublicAccessBlockConfiguration.md "API_control_PublicAccessBlockConfiguration.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointForObjectLambda")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointForObjectLambda")

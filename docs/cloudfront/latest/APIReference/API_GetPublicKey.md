# GetPublicKey

Gets a public key.


## Request Syntax



```
GET /2020-05-31/public-key/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetPublicKey_RequestSyntax "#API_GetPublicKey_RequestSyntax")**


The identifier of the public key you are getting.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PublicKey>
   <CreatedTime>***timestamp***</CreatedTime>
   <Id>***string***</Id>
   <PublicKeyConfig>
      <CallerReference>***string***</CallerReference>
      <Comment>***string***</Comment>
      <EncodedKey>***string***</EncodedKey>
      <Name>***string***</Name>
   </PublicKeyConfig>
</PublicKey>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[PublicKey](#API_GetPublicKey_ResponseSyntax "#API_GetPublicKey_ResponseSyntax")**


Root level tag for the PublicKey parameters.


Required: Yes




**[CreatedTime](#API_GetPublicKey_ResponseSyntax "#API_GetPublicKey_ResponseSyntax")**


The date and time when the public key was uploaded.


Type: Timestamp




**[Id](#API_GetPublicKey_ResponseSyntax "#API_GetPublicKey_ResponseSyntax")**


The identifier of the public key.


Type: String




**[PublicKeyConfig](#API_GetPublicKey_ResponseSyntax "#API_GetPublicKey_ResponseSyntax")**


Configuration information about a public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: [PublicKeyConfig](API_PublicKeyConfig.md "API_PublicKeyConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchPublicKey** 


The specified public key doesn't exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetPublicKey")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetPublicKey "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetPublicKey")

# GetPublicKeyConfig

Gets a public key configuration.


## Request Syntax



```
GET /2020-05-31/public-key/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetPublicKeyConfig_RequestSyntax "#API_GetPublicKeyConfig_RequestSyntax")**


The identifier of the public key whose configuration you are getting.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<PublicKeyConfig>
   <CallerReference>***string***</CallerReference>
   <Comment>***string***</Comment>
   <EncodedKey>***string***</EncodedKey>
   <Name>***string***</Name>
</PublicKeyConfig>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[PublicKeyConfig](#API_GetPublicKeyConfig_ResponseSyntax "#API_GetPublicKeyConfig_ResponseSyntax")**


Root level tag for the PublicKeyConfig parameters.


Required: Yes




**[CallerReference](#API_GetPublicKeyConfig_ResponseSyntax "#API_GetPublicKeyConfig_ResponseSyntax")**


A string included in the request to help make sure that the request can't be
 replayed.


Type: String




**[Comment](#API_GetPublicKeyConfig_ResponseSyntax "#API_GetPublicKeyConfig_ResponseSyntax")**


A comment to describe the public key. The comment cannot be longer than 128
 characters.


Type: String




**[EncodedKey](#API_GetPublicKeyConfig_ResponseSyntax "#API_GetPublicKeyConfig_ResponseSyntax")**


The public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: String




**[Name](#API_GetPublicKeyConfig_ResponseSyntax "#API_GetPublicKeyConfig_ResponseSyntax")**


A name to help identify the public key.


Type: String




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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetPublicKeyConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetPublicKeyConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetPublicKeyConfig")

# CreatePublicKey

Uploads a public key to CloudFront that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


## Request Syntax



```
POST /2020-05-31/public-key HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<PublicKeyConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>`string`</CallerReference>
   <Comment>`string`</Comment>
   <EncodedKey>`string`</EncodedKey>
   <Name>`string`</Name>
</PublicKeyConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[PublicKeyConfig](#API_CreatePublicKey_RequestSyntax "#API_CreatePublicKey_RequestSyntax")**


Root level tag for the PublicKeyConfig parameters.


Required: Yes




**[CallerReference](#API_CreatePublicKey_RequestSyntax "#API_CreatePublicKey_RequestSyntax")**


A string included in the request to help make sure that the request can't be
 replayed.


Type: String


Required: Yes




**[Comment](#API_CreatePublicKey_RequestSyntax "#API_CreatePublicKey_RequestSyntax")**


A comment to describe the public key. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[EncodedKey](#API_CreatePublicKey_RequestSyntax "#API_CreatePublicKey_RequestSyntax")**


The public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: String


Required: Yes




**[Name](#API_CreatePublicKey_RequestSyntax "#API_CreatePublicKey_RequestSyntax")**


A name to help identify the public key.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[PublicKey](#API_CreatePublicKey_ResponseSyntax "#API_CreatePublicKey_ResponseSyntax")**


Root level tag for the PublicKey parameters.


Required: Yes




**[CreatedTime](#API_CreatePublicKey_ResponseSyntax "#API_CreatePublicKey_ResponseSyntax")**


The date and time when the public key was uploaded.


Type: Timestamp




**[Id](#API_CreatePublicKey_ResponseSyntax "#API_CreatePublicKey_ResponseSyntax")**


The identifier of the public key.


Type: String




**[PublicKeyConfig](#API_CreatePublicKey_ResponseSyntax "#API_CreatePublicKey_ResponseSyntax")**


Configuration information about a public key that you can use with [signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md"), or with [field-level encryption](../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md "../../../AmazonCloudFront/latest/DeveloperGuide/field-level-encryption.md").


Type: [PublicKeyConfig](API_PublicKeyConfig.md "API_PublicKeyConfig.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**PublicKeyAlreadyExists** 


The specified public key already exists.


HTTP Status Code: 409




**TooManyPublicKeys** 


The maximum number of public keys for field-level encryption have been created. To
 create a new public key, delete one of the existing keys.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreatePublicKey")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreatePublicKey "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreatePublicKey")

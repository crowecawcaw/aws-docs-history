# CreateKeyGroup

Creates a key group that you can use with [CloudFront signed URLs and signed cookies](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md").

To create a key group, you must specify at least one public key for the key group.
 After you create a key group, you can reference it from one or more cache behaviors.
 When you reference a key group in a cache behavior, CloudFront requires signed URLs or signed
 cookies for all requests that match the cache behavior. The URLs or cookies must be
 signed with a private key whose corresponding public key is in the key group. The signed
 URL or cookie contains information about which public key CloudFront should use to verify the
 signature. For more information, see [Serving private content](../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md "../../../AmazonCloudFront/latest/DeveloperGuide/PrivateContent.md") in the
 *Amazon CloudFront Developer Guide*.


## Request Syntax



```
POST /2020-05-31/key-group HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroupConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <Comment>`string`</Comment>
   <Items>
      <PublicKey>`string`</PublicKey>
   </Items>
   <Name>`string`</Name>
</KeyGroupConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[KeyGroupConfig](#API_CreateKeyGroup_RequestSyntax "#API_CreateKeyGroup_RequestSyntax")**


Root level tag for the KeyGroupConfig parameters.


Required: Yes




**[Comment](#API_CreateKeyGroup_RequestSyntax "#API_CreateKeyGroup_RequestSyntax")**


A comment to describe the key group. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[Items](#API_CreateKeyGroup_RequestSyntax "#API_CreateKeyGroup_RequestSyntax")**


A list of the identifiers of the public keys in the key group.


Type: Array of strings


Required: Yes




**[Name](#API_CreateKeyGroup_RequestSyntax "#API_CreateKeyGroup_RequestSyntax")**


A name to identify the key group.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 201
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroup>
   <Id>***string***</Id>
   <KeyGroupConfig>
      <Comment>***string***</Comment>
      <Items>
         <PublicKey>***string***</PublicKey>
      </Items>
      <Name>***string***</Name>
   </KeyGroupConfig>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
</KeyGroup>
```

## Response Elements


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[KeyGroup](#API_CreateKeyGroup_ResponseSyntax "#API_CreateKeyGroup_ResponseSyntax")**


Root level tag for the KeyGroup parameters.


Required: Yes




**[Id](#API_CreateKeyGroup_ResponseSyntax "#API_CreateKeyGroup_ResponseSyntax")**


The identifier for the key group.


Type: String




**[KeyGroupConfig](#API_CreateKeyGroup_ResponseSyntax "#API_CreateKeyGroup_ResponseSyntax")**


The key group configuration.


Type: [KeyGroupConfig](API_KeyGroupConfig.md "API_KeyGroupConfig.md") object




**[LastModifiedTime](#API_CreateKeyGroup_ResponseSyntax "#API_CreateKeyGroup_ResponseSyntax")**


The date and time when the key group was last modified.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**KeyGroupAlreadyExists** 


A key group with this name already exists. You must provide a unique name. To modify
 an existing key group, use `UpdateKeyGroup`.


HTTP Status Code: 409




**TooManyKeyGroups** 


You have reached the maximum number of key groups for this AWS account. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




**TooManyPublicKeysInKeyGroup** 


The number of public keys in this key group is more than the maximum allowed. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateKeyGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateKeyGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateKeyGroup")

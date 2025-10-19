# UpdateKeyGroup

Updates a key group.

When you update a key group, all the fields are updated with the values provided in
 the request. You cannot update some fields independent of others. To update a key
 group:


1. Get the current key group with `GetKeyGroup` or
 `GetKeyGroupConfig`.
2. Locally modify the fields in the key group that you want to update. For
 example, add or remove public key IDs.
3. Call `UpdateKeyGroup` with the entire key group object, including
 the fields that you modified and those that you didn't.

## Request Syntax



```
PUT /2020-05-31/key-group/`Id` HTTP/1.1
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





**[KeyGroupConfig](#API_UpdateKeyGroup_RequestSyntax "#API_UpdateKeyGroup_RequestSyntax")**


Root level tag for the KeyGroupConfig parameters.


Required: Yes




**[Comment](#API_UpdateKeyGroup_RequestSyntax "#API_UpdateKeyGroup_RequestSyntax")**


A comment to describe the key group. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[Items](#API_UpdateKeyGroup_RequestSyntax "#API_UpdateKeyGroup_RequestSyntax")**


A list of the identifiers of the public keys in the key group.


Type: Array of strings


Required: Yes




**[Name](#API_UpdateKeyGroup_RequestSyntax "#API_UpdateKeyGroup_RequestSyntax")**


A name to identify the key group.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
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


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[KeyGroup](#API_UpdateKeyGroup_ResponseSyntax "#API_UpdateKeyGroup_ResponseSyntax")**


Root level tag for the KeyGroup parameters.


Required: Yes




**[Id](#API_UpdateKeyGroup_ResponseSyntax "#API_UpdateKeyGroup_ResponseSyntax")**


The identifier for the key group.


Type: String




**[KeyGroupConfig](#API_UpdateKeyGroup_ResponseSyntax "#API_UpdateKeyGroup_ResponseSyntax")**


The key group configuration.


Type: [KeyGroupConfig](API_KeyGroupConfig.md "API_KeyGroupConfig.md") object




**[LastModifiedTime](#API_UpdateKeyGroup_ResponseSyntax "#API_UpdateKeyGroup_ResponseSyntax")**


The date and time when the key group was last modified.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**KeyGroupAlreadyExists** 


A key group with this name already exists. You must provide a unique name. To modify
 an existing key group, use `UpdateKeyGroup`.


HTTP Status Code: 409




**NoSuchResource** 


A resource that was specified is not valid.


HTTP Status Code: 404




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




**TooManyPublicKeysInKeyGroup** 


The number of public keys in this key group is more than the maximum allowed. For more
 information, see [Quotas](../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md "../../../AmazonCloudFront/latest/DeveloperGuide/cloudfront-limits.md") (formerly known as limits) in the
 *Amazon CloudFront Developer Guide*.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/UpdateKeyGroup")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateKeyGroup "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/UpdateKeyGroup")

# GetKeyGroupConfig

Gets a key group configuration.

To get a key group configuration, you must provide the key group's identifier. If the
 key group is referenced in a distribution's cache behavior, you can get the key group's
 identifier using `ListDistributions` or `GetDistribution`. If the
 key group is not referenced in a cache behavior, you can get the identifier using
 `ListKeyGroups`.


## Request Syntax



```
GET /2020-05-31/key-group/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetKeyGroupConfig_RequestSyntax "#API_GetKeyGroupConfig_RequestSyntax")**


The identifier of the key group whose configuration you are getting. To get the
 identifier, use `ListKeyGroups`.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<KeyGroupConfig>
   <Comment>***string***</Comment>
   <Items>
      <PublicKey>***string***</PublicKey>
   </Items>
   <Name>***string***</Name>
</KeyGroupConfig>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[KeyGroupConfig](#API_GetKeyGroupConfig_ResponseSyntax "#API_GetKeyGroupConfig_ResponseSyntax")**


Root level tag for the KeyGroupConfig parameters.


Required: Yes




**[Comment](#API_GetKeyGroupConfig_ResponseSyntax "#API_GetKeyGroupConfig_ResponseSyntax")**


A comment to describe the key group. The comment cannot be longer than 128
 characters.


Type: String




**[Items](#API_GetKeyGroupConfig_ResponseSyntax "#API_GetKeyGroupConfig_ResponseSyntax")**


A list of the identifiers of the public keys in the key group.


Type: Array of strings




**[Name](#API_GetKeyGroupConfig_ResponseSyntax "#API_GetKeyGroupConfig_ResponseSyntax")**


A name to identify the key group.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**NoSuchResource** 


A resource that was specified is not valid.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetKeyGroupConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetKeyGroupConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetKeyGroupConfig")

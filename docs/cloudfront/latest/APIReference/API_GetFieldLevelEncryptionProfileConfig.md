# GetFieldLevelEncryptionProfileConfig

Get the field-level encryption profile configuration information.


## Request Syntax



```
GET /2020-05-31/field-level-encryption-profile/`Id`/config HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetFieldLevelEncryptionProfileConfig_RequestSyntax "#API_GetFieldLevelEncryptionProfileConfig_RequestSyntax")**


Get the ID for the field-level encryption profile configuration information.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfileConfig>
   <CallerReference>***string***</CallerReference>
   <Comment>***string***</Comment>
   <EncryptionEntities>
      <Items>
         <EncryptionEntity>
            <FieldPatterns>
               <Items>
                  <FieldPattern>***string***</FieldPattern>
               </Items>
               <Quantity>***integer***</Quantity>
            </FieldPatterns>
            <ProviderId>***string***</ProviderId>
            <PublicKeyId>***string***</PublicKeyId>
         </EncryptionEntity>
      </Items>
      <Quantity>***integer***</Quantity>
   </EncryptionEntities>
   <Name>***string***</Name>
</FieldLevelEncryptionProfileConfig>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryptionProfileConfig](#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax "#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax")**


Root level tag for the FieldLevelEncryptionProfileConfig parameters.


Required: Yes




**[CallerReference](#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax "#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax")**


A unique number that ensures that the request can't be replayed.


Type: String




**[Comment](#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax "#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax")**


An optional comment for the field-level encryption profile. The comment cannot be
 longer than 128 characters.


Type: String




**[EncryptionEntities](#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax "#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax")**


A complex data type of encryption entities for the field-level encryption profile that
 include the public key ID, provider, and field patterns for specifying which fields to
 encrypt with this key.


Type: [EncryptionEntities](API_EncryptionEntities.md "API_EncryptionEntities.md") object




**[Name](#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax "#API_GetFieldLevelEncryptionProfileConfig_ResponseSyntax")**


Profile name for the field-level encryption profile.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchFieldLevelEncryptionProfile** 


The specified profile for field-level encryption doesn't exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfileConfig")

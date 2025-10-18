# GetFieldLevelEncryptionProfile

Get the field-level encryption profile information.


## Request Syntax



```
GET /2020-05-31/field-level-encryption-profile/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetFieldLevelEncryptionProfile_RequestSyntax "#API_GetFieldLevelEncryptionProfile_RequestSyntax")**


Get the ID for the field-level encryption profile information.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfile>
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
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
</FieldLevelEncryptionProfile>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryptionProfile](#API_GetFieldLevelEncryptionProfile_ResponseSyntax "#API_GetFieldLevelEncryptionProfile_ResponseSyntax")**


Root level tag for the FieldLevelEncryptionProfile parameters.


Required: Yes




**[FieldLevelEncryptionProfileConfig](#API_GetFieldLevelEncryptionProfile_ResponseSyntax "#API_GetFieldLevelEncryptionProfile_ResponseSyntax")**


A complex data type that includes the profile name and the encryption entities for the
 field-level encryption profile.


Type: [FieldLevelEncryptionProfileConfig](API_FieldLevelEncryptionProfileConfig.md "API_FieldLevelEncryptionProfileConfig.md") object




**[Id](#API_GetFieldLevelEncryptionProfile_ResponseSyntax "#API_GetFieldLevelEncryptionProfile_ResponseSyntax")**


The ID for a field-level encryption profile configuration which includes a set of
 profiles that specify certain selected data fields to be encrypted by specific public
 keys.


Type: String




**[LastModifiedTime](#API_GetFieldLevelEncryptionProfile_ResponseSyntax "#API_GetFieldLevelEncryptionProfile_ResponseSyntax")**


The last time the field-level encryption profile was updated.


Type: Timestamp




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



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryptionProfile")

# GetFieldLevelEncryption

Get the field-level encryption configuration information.


## Request Syntax



```
GET /2020-05-31/field-level-encryption/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_GetFieldLevelEncryption_RequestSyntax "#API_GetFieldLevelEncryption_RequestSyntax")**


Request the ID for the field-level encryption configuration information.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryption>
   <FieldLevelEncryptionConfig>
      <CallerReference>***string***</CallerReference>
      <Comment>***string***</Comment>
      <ContentTypeProfileConfig>
         <ContentTypeProfiles>
            <Items>
               <ContentTypeProfile>
                  <ContentType>***string***</ContentType>
                  <Format>***string***</Format>
                  <ProfileId>***string***</ProfileId>
               </ContentTypeProfile>
            </Items>
            <Quantity>***integer***</Quantity>
         </ContentTypeProfiles>
         <ForwardWhenContentTypeIsUnknown>***boolean***</ForwardWhenContentTypeIsUnknown>
      </ContentTypeProfileConfig>
      <QueryArgProfileConfig>
         <ForwardWhenQueryArgProfileIsUnknown>***boolean***</ForwardWhenQueryArgProfileIsUnknown>
         <QueryArgProfiles>
            <Items>
               <QueryArgProfile>
                  <ProfileId>***string***</ProfileId>
                  <QueryArg>***string***</QueryArg>
               </QueryArgProfile>
            </Items>
            <Quantity>***integer***</Quantity>
         </QueryArgProfiles>
      </QueryArgProfileConfig>
   </FieldLevelEncryptionConfig>
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
</FieldLevelEncryption>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryption](#API_GetFieldLevelEncryption_ResponseSyntax "#API_GetFieldLevelEncryption_ResponseSyntax")**


Root level tag for the FieldLevelEncryption parameters.


Required: Yes




**[FieldLevelEncryptionConfig](#API_GetFieldLevelEncryption_ResponseSyntax "#API_GetFieldLevelEncryption_ResponseSyntax")**


A complex data type that includes the profile configurations specified for field-level
 encryption.


Type: [FieldLevelEncryptionConfig](API_FieldLevelEncryptionConfig.md "API_FieldLevelEncryptionConfig.md") object




**[Id](#API_GetFieldLevelEncryption_ResponseSyntax "#API_GetFieldLevelEncryption_ResponseSyntax")**


The configuration ID for a field-level encryption configuration which includes a set
 of profiles that specify certain selected data fields to be encrypted by specific public
 keys.


Type: String




**[LastModifiedTime](#API_GetFieldLevelEncryption_ResponseSyntax "#API_GetFieldLevelEncryption_ResponseSyntax")**


The last time the field-level encryption configuration was changed.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**NoSuchFieldLevelEncryptionConfig** 


The specified configuration for field-level encryption doesn't exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetFieldLevelEncryption")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryption "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetFieldLevelEncryption")

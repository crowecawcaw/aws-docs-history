# CreateFieldLevelEncryptionProfile

Create a field-level encryption profile.


## Request Syntax



```
POST /2020-05-31/field-level-encryption-profile HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionProfileConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>`string`</CallerReference>
   <Comment>`string`</Comment>
   <EncryptionEntities>
      <Items>
         <EncryptionEntity>
            <FieldPatterns>
               <Items>
                  <FieldPattern>`string`</FieldPattern>
               </Items>
               <Quantity>`integer`</Quantity>
            </FieldPatterns>
            <ProviderId>`string`</ProviderId>
            <PublicKeyId>`string`</PublicKeyId>
         </EncryptionEntity>
      </Items>
      <Quantity>`integer`</Quantity>
   </EncryptionEntities>
   <Name>`string`</Name>
</FieldLevelEncryptionProfileConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[FieldLevelEncryptionProfileConfig](#API_CreateFieldLevelEncryptionProfile_RequestSyntax "#API_CreateFieldLevelEncryptionProfile_RequestSyntax")**


Root level tag for the FieldLevelEncryptionProfileConfig parameters.


Required: Yes




**[CallerReference](#API_CreateFieldLevelEncryptionProfile_RequestSyntax "#API_CreateFieldLevelEncryptionProfile_RequestSyntax")**


A unique number that ensures that the request can't be replayed.


Type: String


Required: Yes




**[Comment](#API_CreateFieldLevelEncryptionProfile_RequestSyntax "#API_CreateFieldLevelEncryptionProfile_RequestSyntax")**


An optional comment for the field-level encryption profile. The comment cannot be
 longer than 128 characters.


Type: String


Required: No




**[EncryptionEntities](#API_CreateFieldLevelEncryptionProfile_RequestSyntax "#API_CreateFieldLevelEncryptionProfile_RequestSyntax")**


A complex data type of encryption entities for the field-level encryption profile that
 include the public key ID, provider, and field patterns for specifying which fields to
 encrypt with this key.


Type: [EncryptionEntities](API_EncryptionEntities.md "API_EncryptionEntities.md") object


Required: Yes




**[Name](#API_CreateFieldLevelEncryptionProfile_RequestSyntax "#API_CreateFieldLevelEncryptionProfile_RequestSyntax")**


Profile name for the field-level encryption profile.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryptionProfile](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax "#API_CreateFieldLevelEncryptionProfile_ResponseSyntax")**


Root level tag for the FieldLevelEncryptionProfile parameters.


Required: Yes




**[FieldLevelEncryptionProfileConfig](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax "#API_CreateFieldLevelEncryptionProfile_ResponseSyntax")**


A complex data type that includes the profile name and the encryption entities for the
 field-level encryption profile.


Type: [FieldLevelEncryptionProfileConfig](API_FieldLevelEncryptionProfileConfig.md "API_FieldLevelEncryptionProfileConfig.md") object




**[Id](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax "#API_CreateFieldLevelEncryptionProfile_ResponseSyntax")**


The ID for a field-level encryption profile configuration which includes a set of
 profiles that specify certain selected data fields to be encrypted by specific public
 keys.


Type: String




**[LastModifiedTime](#API_CreateFieldLevelEncryptionProfile_ResponseSyntax "#API_CreateFieldLevelEncryptionProfile_ResponseSyntax")**


The last time the field-level encryption profile was updated.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**FieldLevelEncryptionProfileAlreadyExists** 


The specified profile for field-level encryption already exists.


HTTP Status Code: 409




**FieldLevelEncryptionProfileSizeExceeded** 


The maximum size of a profile for field-level encryption was exceeded.


HTTP Status Code: 400




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchPublicKey** 


The specified public key doesn't exist.


HTTP Status Code: 404




**TooManyFieldLevelEncryptionEncryptionEntities** 


The maximum number of encryption entities for field-level encryption have been
 created.


HTTP Status Code: 400




**TooManyFieldLevelEncryptionFieldPatterns** 


The maximum number of field patterns for field-level encryption have been
 created.


HTTP Status Code: 400




**TooManyFieldLevelEncryptionProfiles** 


The maximum number of profiles for field-level encryption have been created.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionProfile")

# CreateFieldLevelEncryptionConfig

Create a new field-level encryption configuration.


## Request Syntax



```
POST /2020-05-31/field-level-encryption HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionConfig xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CallerReference>`string`</CallerReference>
   <Comment>`string`</Comment>
   <ContentTypeProfileConfig>
      <ContentTypeProfiles>
         <Items>
            <ContentTypeProfile>
               <ContentType>`string`</ContentType>
               <Format>`string`</Format>
               <ProfileId>`string`</ProfileId>
            </ContentTypeProfile>
         </Items>
         <Quantity>`integer`</Quantity>
      </ContentTypeProfiles>
      <ForwardWhenContentTypeIsUnknown>`boolean`</ForwardWhenContentTypeIsUnknown>
   </ContentTypeProfileConfig>
   <QueryArgProfileConfig>
      <ForwardWhenQueryArgProfileIsUnknown>`boolean`</ForwardWhenQueryArgProfileIsUnknown>
      <QueryArgProfiles>
         <Items>
            <QueryArgProfile>
               <ProfileId>`string`</ProfileId>
               <QueryArg>`string`</QueryArg>
            </QueryArgProfile>
         </Items>
         <Quantity>`integer`</Quantity>
      </QueryArgProfiles>
   </QueryArgProfileConfig>
</FieldLevelEncryptionConfig>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[FieldLevelEncryptionConfig](#API_CreateFieldLevelEncryptionConfig_RequestSyntax "#API_CreateFieldLevelEncryptionConfig_RequestSyntax")**


Root level tag for the FieldLevelEncryptionConfig parameters.


Required: Yes




**[CallerReference](#API_CreateFieldLevelEncryptionConfig_RequestSyntax "#API_CreateFieldLevelEncryptionConfig_RequestSyntax")**


A unique number that ensures the request can't be replayed.


Type: String


Required: Yes




**[Comment](#API_CreateFieldLevelEncryptionConfig_RequestSyntax "#API_CreateFieldLevelEncryptionConfig_RequestSyntax")**


An optional comment about the configuration. The comment cannot be longer than 128
 characters.


Type: String


Required: No




**[ContentTypeProfileConfig](#API_CreateFieldLevelEncryptionConfig_RequestSyntax "#API_CreateFieldLevelEncryptionConfig_RequestSyntax")**


A complex data type that specifies when to forward content if a content type isn't
 recognized and profiles to use as by default in a request if a query argument doesn't
 specify a profile to use.


Type: [ContentTypeProfileConfig](API_ContentTypeProfileConfig.md "API_ContentTypeProfileConfig.md") object


Required: No




**[QueryArgProfileConfig](#API_CreateFieldLevelEncryptionConfig_RequestSyntax "#API_CreateFieldLevelEncryptionConfig_RequestSyntax")**


A complex data type that specifies when to forward content if a profile isn't found
 and the profile that can be provided as a query argument in a request.


Type: [QueryArgProfileConfig](API_QueryArgProfileConfig.md "API_QueryArgProfileConfig.md") object


Required: No




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryption](#API_CreateFieldLevelEncryptionConfig_ResponseSyntax "#API_CreateFieldLevelEncryptionConfig_ResponseSyntax")**


Root level tag for the FieldLevelEncryption parameters.


Required: Yes




**[FieldLevelEncryptionConfig](#API_CreateFieldLevelEncryptionConfig_ResponseSyntax "#API_CreateFieldLevelEncryptionConfig_ResponseSyntax")**


A complex data type that includes the profile configurations specified for field-level
 encryption.


Type: [FieldLevelEncryptionConfig](API_FieldLevelEncryptionConfig.md "API_FieldLevelEncryptionConfig.md") object




**[Id](#API_CreateFieldLevelEncryptionConfig_ResponseSyntax "#API_CreateFieldLevelEncryptionConfig_ResponseSyntax")**


The configuration ID for a field-level encryption configuration which includes a set
 of profiles that specify certain selected data fields to be encrypted by specific public
 keys.


Type: String




**[LastModifiedTime](#API_CreateFieldLevelEncryptionConfig_ResponseSyntax "#API_CreateFieldLevelEncryptionConfig_ResponseSyntax")**


The last time the field-level encryption configuration was changed.


Type: Timestamp




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**FieldLevelEncryptionConfigAlreadyExists** 


The specified configuration for field-level encryption already exists.


HTTP Status Code: 409




**InconsistentQuantities** 


The value of `Quantity` and the size of `Items` don't
 match.


HTTP Status Code: 400




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**NoSuchFieldLevelEncryptionProfile** 


The specified profile for field-level encryption doesn't exist.


HTTP Status Code: 404




**QueryArgProfileEmpty** 


No profile specified for the field-level encryption query argument.


HTTP Status Code: 400




**TooManyFieldLevelEncryptionConfigs** 


The maximum number of configurations for field-level encryption have been
 created.


HTTP Status Code: 400




**TooManyFieldLevelEncryptionContentTypeProfiles** 


The maximum number of content type profiles for field-level encryption have been
 created.


HTTP Status Code: 400




**TooManyFieldLevelEncryptionQueryArgProfiles** 


The maximum number of query arg profiles for field-level encryption have been
 created.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateFieldLevelEncryptionConfig")

# ListFieldLevelEncryptionConfigs

List all field-level encryption configurations that have been created in CloudFront for this
 account.


## Request Syntax



```
GET /2020-05-31/field-level-encryption?Marker=`Marker`&MaxItems=`MaxItems` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Marker](#API_ListFieldLevelEncryptionConfigs_RequestSyntax "#API_ListFieldLevelEncryptionConfigs_RequestSyntax")**


Use this when paginating results to indicate where to begin in your list of
 configurations. The results include configurations in the list that occur after the
 marker. To get the next page of results, set the `Marker` to the value of the
 `NextMarker` from the current page's response (which is also the ID of
 the last configuration on that page).




**[MaxItems](#API_ListFieldLevelEncryptionConfigs_RequestSyntax "#API_ListFieldLevelEncryptionConfigs_RequestSyntax")**


The maximum number of field-level encryption configurations you want in the response
 body.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<FieldLevelEncryptionList>
   <Items>
      <FieldLevelEncryptionSummary>
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
         <Id>***string***</Id>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
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
      </FieldLevelEncryptionSummary>
   </Items>
   <MaxItems>***integer***</MaxItems>
   <NextMarker>***string***</NextMarker>
   <Quantity>***integer***</Quantity>
</FieldLevelEncryptionList>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[FieldLevelEncryptionList](#API_ListFieldLevelEncryptionConfigs_ResponseSyntax "#API_ListFieldLevelEncryptionConfigs_ResponseSyntax")**


Root level tag for the FieldLevelEncryptionList parameters.


Required: Yes




**[Items](#API_ListFieldLevelEncryptionConfigs_ResponseSyntax "#API_ListFieldLevelEncryptionConfigs_ResponseSyntax")**


An array of field-level encryption items.


Type: Array of [FieldLevelEncryptionSummary](API_FieldLevelEncryptionSummary.md "API_FieldLevelEncryptionSummary.md") objects




**[MaxItems](#API_ListFieldLevelEncryptionConfigs_ResponseSyntax "#API_ListFieldLevelEncryptionConfigs_ResponseSyntax")**


The maximum number of elements you want in the response body.


Type: Integer




**[NextMarker](#API_ListFieldLevelEncryptionConfigs_ResponseSyntax "#API_ListFieldLevelEncryptionConfigs_ResponseSyntax")**


If there are more elements to be listed, this element is present and contains the
 value that you can use for the `Marker` request parameter to continue listing
 your configurations where you left off.


Type: String




**[Quantity](#API_ListFieldLevelEncryptionConfigs_ResponseSyntax "#API_ListFieldLevelEncryptionConfigs_ResponseSyntax")**


The number of field-level encryption items.


Type: Integer




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListFieldLevelEncryptionConfigs")

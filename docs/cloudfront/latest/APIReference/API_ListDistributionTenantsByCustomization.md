# ListDistributionTenantsByCustomization

Lists distribution tenants by the customization that you specify.

You must specify either the `CertificateArn` parameter or `WebACLArn` parameter, but not both in the same request.


## Request Syntax



```
POST /2020-05-31/distribution-tenants-by-customization HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<ListDistributionTenantsByCustomizationRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <CertificateArn>`string`</CertificateArn>
   <Marker>`string`</Marker>
   <MaxItems>`integer`</MaxItems>
   <WebACLArn>`string`</WebACLArn>
</ListDistributionTenantsByCustomizationRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[ListDistributionTenantsByCustomizationRequest](#API_ListDistributionTenantsByCustomization_RequestSyntax "#API_ListDistributionTenantsByCustomization_RequestSyntax")**


Root level tag for the ListDistributionTenantsByCustomizationRequest parameters.


Required: Yes




**[CertificateArn](#API_ListDistributionTenantsByCustomization_RequestSyntax "#API_ListDistributionTenantsByCustomization_RequestSyntax")**


Filter by the ARN of the associated ACM certificate.


Type: String


Required: No




**[Marker](#API_ListDistributionTenantsByCustomization_RequestSyntax "#API_ListDistributionTenantsByCustomization_RequestSyntax")**


The marker for the next set of results.


Type: String


Required: No




**[MaxItems](#API_ListDistributionTenantsByCustomization_RequestSyntax "#API_ListDistributionTenantsByCustomization_RequestSyntax")**


The maximum number of distribution tenants to return by the specified customization.


Type: Integer


Required: No




**[WebACLArn](#API_ListDistributionTenantsByCustomization_RequestSyntax "#API_ListDistributionTenantsByCustomization_RequestSyntax")**


Filter by the ARN of the associated AWS WAF web ACL.


Type: String


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<ListDistributionTenantsByCustomizationResult>
   <DistributionTenantList>
      <DistributionTenantSummary>
         <Arn>***string***</Arn>
         <ConnectionGroupId>***string***</ConnectionGroupId>
         <CreatedTime>***timestamp***</CreatedTime>
         <Customizations>
            <Certificate>
               <Arn>***string***</Arn>
            </Certificate>
            <GeoRestrictions>
               <Locations>
                  <Location>***string***</Location>
               </Locations>
               <RestrictionType>***string***</RestrictionType>
            </GeoRestrictions>
            <WebAcl>
               <Action>***string***</Action>
               <Arn>***string***</Arn>
            </WebAcl>
         </Customizations>
         <DistributionId>***string***</DistributionId>
         <Domains>
            <DomainResult>
               <Domain>***string***</Domain>
               <Status>***string***</Status>
            </DomainResult>
         </Domains>
         <Enabled>***boolean***</Enabled>
         <ETag>***string***</ETag>
         <Id>***string***</Id>
         <LastModifiedTime>***timestamp***</LastModifiedTime>
         <Name>***string***</Name>
         <Status>***string***</Status>
      </DistributionTenantSummary>
   </DistributionTenantList>
   <NextMarker>***string***</NextMarker>
</ListDistributionTenantsByCustomizationResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListDistributionTenantsByCustomizationResult](#API_ListDistributionTenantsByCustomization_ResponseSyntax "#API_ListDistributionTenantsByCustomization_ResponseSyntax")**


Root level tag for the ListDistributionTenantsByCustomizationResult parameters.


Required: Yes




**[DistributionTenantList](#API_ListDistributionTenantsByCustomization_ResponseSyntax "#API_ListDistributionTenantsByCustomization_ResponseSyntax")**


A list of distribution tenants with the specified customization.


Type: Array of [DistributionTenantSummary](API_DistributionTenantSummary.md "API_DistributionTenantSummary.md") objects




**[NextMarker](#API_ListDistributionTenantsByCustomization_ResponseSyntax "#API_ListDistributionTenantsByCustomization_ResponseSyntax")**


A token used for pagination of results returned in the response. You can use the token from the previous request to define where the current request should begin.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/ListDistributionTenantsByCustomization")

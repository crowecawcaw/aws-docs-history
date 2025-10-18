# GetDistributionTenant

Gets information about a distribution tenant.


## Request Syntax



```
GET /2020-05-31/distribution-tenant/`Identifier` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[Identifier](#API_GetDistributionTenant_RequestSyntax "#API_GetDistributionTenant_RequestSyntax")**


The identifier of the distribution tenant. You can specify the ARN, ID, or name of the distribution tenant.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<DistributionTenant>
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
   <Id>***string***</Id>
   <LastModifiedTime>***timestamp***</LastModifiedTime>
   <Name>***string***</Name>
   <Parameters>
      <Parameter>
         <Name>***string***</Name>
         <Value>***string***</Value>
      </Parameter>
   </Parameters>
   <Status>***string***</Status>
   <Tags>
      <Items>
         <Tag>
            <Key>***string***</Key>
            <Value>***string***</Value>
         </Tag>
      </Items>
   </Tags>
</DistributionTenant>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[DistributionTenant](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


Root level tag for the DistributionTenant parameters.


Required: Yes




**[Arn](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The Amazon Resource Name (ARN) of the distribution tenant.


Type: String




**[ConnectionGroupId](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.


Type: String




**[CreatedTime](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The date and time when the distribution tenant was created.


Type: Timestamp




**[Customizations](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.


Type: [Customizations](API_Customizations.md "API_Customizations.md") object




**[DistributionId](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The ID of the multi-tenant distribution.


Type: String




**[Domains](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The domains associated with the distribution tenant.


Type: Array of [DomainResult](API_DomainResult.md "API_DomainResult.md") objects




**[Enabled](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.


Type: Boolean




**[Id](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The ID of the distribution tenant.


Type: String




**[LastModifiedTime](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The date and time when the distribution tenant was updated.


Type: Timestamp




**[Name](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The name of the distribution tenant.


Type: String




**[Parameters](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects




**[Status](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


The status of the distribution tenant.


Type: String




**[Tags](#API_GetDistributionTenant_ResponseSyntax "#API_GetDistributionTenant_ResponseSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetDistributionTenant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetDistributionTenant "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetDistributionTenant")

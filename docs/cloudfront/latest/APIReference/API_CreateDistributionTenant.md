# CreateDistributionTenant

Creates a distribution tenant.


## Request Syntax



```
POST /2020-05-31/distribution-tenant HTTP/1.1
<?xml version="1.0" encoding="UTF-8"?>
<CreateDistributionTenantRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <ConnectionGroupId>`string`</ConnectionGroupId>
   <Customizations>
      <Certificate>
         <Arn>`string`</Arn>
      </Certificate>
      <GeoRestrictions>
         <Locations>
            <Location>`string`</Location>
         </Locations>
         <RestrictionType>`string`</RestrictionType>
      </GeoRestrictions>
      <WebAcl>
         <Action>`string`</Action>
         <Arn>`string`</Arn>
      </WebAcl>
   </Customizations>
   <DistributionId>`string`</DistributionId>
   <Domains>
      <DomainItem>
         <Domain>`string`</Domain>
      </DomainItem>
   </Domains>
   <Enabled>`boolean`</Enabled>
   <ManagedCertificateRequest>
      <CertificateTransparencyLoggingPreference>`string`</CertificateTransparencyLoggingPreference>
      <PrimaryDomainName>`string`</PrimaryDomainName>
      <ValidationTokenHost>`string`</ValidationTokenHost>
   </ManagedCertificateRequest>
   <Name>`string`</Name>
   <Parameters>
      <Parameter>
         <Name>`string`</Name>
         <Value>`string`</Value>
      </Parameter>
   </Parameters>
   <Tags>
      <Items>
         <Tag>
            <Key>`string`</Key>
            <Value>`string`</Value>
         </Tag>
      </Items>
   </Tags>
</CreateDistributionTenantRequest>
```

## URI Request Parameters


The request does not use any URI parameters.


## Request Body


The request accepts the following data in XML format.





**[CreateDistributionTenantRequest](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


Root level tag for the CreateDistributionTenantRequest parameters.


Required: Yes




**[ConnectionGroupId](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


The ID of the connection group to associate with the distribution tenant.


Type: String


Required: No




**[Customizations](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.


Type: [Customizations](API_Customizations.md "API_Customizations.md") object


Required: No




**[DistributionId](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


The ID of the multi-tenant distribution to use for creating the distribution tenant.


Type: String


Required: Yes




**[Domains](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


The domains associated with the distribution tenant. You must specify at least one domain in the request.


Type: Array of [DomainItem](API_DomainItem.md "API_DomainItem.md") objects


Required: Yes




**[Enabled](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


Indicates whether the distribution tenant should be enabled when created. If the distribution tenant is disabled, the distribution tenant won't serve traffic.


Type: Boolean


Required: No




**[ManagedCertificateRequest](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


The configuration for the CloudFront managed ACM certificate request.


Type: [ManagedCertificateRequest](API_ManagedCertificateRequest.md "API_ManagedCertificateRequest.md") object


Required: No




**[Name](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


The name of the distribution tenant. Enter a friendly identifier that is unique within your AWS account. This name can't be updated after you create the distribution tenant.


Type: String


Pattern: `[a-zA-Z0-9][a-zA-Z0-9-.]{1,126}[a-zA-Z0-9]`



Required: Yes




**[Parameters](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects


Required: No




**[Tags](#API_CreateDistributionTenant_RequestSyntax "#API_CreateDistributionTenant_RequestSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object


Required: No




## Response Syntax



```
HTTP/1.1 201
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


If the action is successful, the service sends back an HTTP 201 response.


The following data is returned in XML format by the service.





**[DistributionTenant](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


Root level tag for the DistributionTenant parameters.


Required: Yes




**[Arn](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The Amazon Resource Name (ARN) of the distribution tenant.


Type: String




**[ConnectionGroupId](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The ID of the connection group for the distribution tenant. If you don't specify a connection group, CloudFront uses the default connection group.


Type: String




**[CreatedTime](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The date and time when the distribution tenant was created.


Type: Timestamp




**[Customizations](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


Customizations for the distribution tenant. For each distribution tenant, you can specify the geographic restrictions, and the Amazon Resource Names (ARNs) for the ACM certificate and AWS WAF web ACL. These are specific values that you can override or disable from the multi-tenant distribution that was used to create the distribution tenant.


Type: [Customizations](API_Customizations.md "API_Customizations.md") object




**[DistributionId](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The ID of the multi-tenant distribution.


Type: String




**[Domains](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The domains associated with the distribution tenant.


Type: Array of [DomainResult](API_DomainResult.md "API_DomainResult.md") objects




**[Enabled](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


Indicates whether the distribution tenant is in an enabled state. If disabled, the distribution tenant won't serve traffic.


Type: Boolean




**[Id](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The ID of the distribution tenant.


Type: String




**[LastModifiedTime](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The date and time when the distribution tenant was updated.


Type: Timestamp




**[Name](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The name of the distribution tenant.


Type: String




**[Parameters](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


A list of parameter values to add to the resource. A parameter is specified as a key-value pair. A valid parameter value must exist for any parameter that is marked as required in the multi-tenant distribution.


Type: Array of [Parameter](API_Parameter.md "API_Parameter.md") objects




**[Status](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


The status of the distribution tenant.


Type: String




**[Tags](#API_CreateDistributionTenant_ResponseSyntax "#API_CreateDistributionTenant_ResponseSyntax")**


A complex type that contains zero or more `Tag` elements.


Type: [Tags](API_Tags.md "API_Tags.md") object




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**CNAMEAlreadyExists** 


The CNAME specified is already defined for CloudFront.


HTTP Status Code: 409




**EntityAlreadyExists** 


The entity already exists. You must provide a unique
 entity.


HTTP Status Code: 409




**EntityLimitExceeded** 


The entity limit has been exceeded.


HTTP Status Code: 400




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**InvalidArgument** 


An argument is invalid.


HTTP Status Code: 400




**InvalidAssociation** 


The specified CloudFront resource can't be associated.


HTTP Status Code: 409




**InvalidTagging** 


The tagging specified is not valid.


HTTP Status Code: 400




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/CreateDistributionTenant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateDistributionTenant "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/CreateDistributionTenant")

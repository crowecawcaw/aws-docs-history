# GetInvalidationForDistributionTenant

Gets information about a specific invalidation for a distribution tenant.


## Request Syntax



```
GET /2020-05-31/distribution-tenant/`DistributionTenantId`/invalidation/`Id` HTTP/1.1

```

## URI Request Parameters


The request uses the following URI parameters.





**[DistributionTenantId](#API_GetInvalidationForDistributionTenant_RequestSyntax "#API_GetInvalidationForDistributionTenant_RequestSyntax")**


The ID of the distribution tenant.


Required: Yes




**[Id](#API_GetInvalidationForDistributionTenant_RequestSyntax "#API_GetInvalidationForDistributionTenant_RequestSyntax")**


The ID of the invalidation to retrieve.


Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<Invalidation>
   <CreateTime>***timestamp***</CreateTime>
   <Id>***string***</Id>
   <InvalidationBatch>
      <CallerReference>***string***</CallerReference>
      <Paths>
         <Items>
            <Path>***string***</Path>
         </Items>
         <Quantity>***integer***</Quantity>
      </Paths>
   </InvalidationBatch>
   <Status>***string***</Status>
</Invalidation>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[Invalidation](#API_GetInvalidationForDistributionTenant_ResponseSyntax "#API_GetInvalidationForDistributionTenant_ResponseSyntax")**


Root level tag for the Invalidation parameters.


Required: Yes




**[CreateTime](#API_GetInvalidationForDistributionTenant_ResponseSyntax "#API_GetInvalidationForDistributionTenant_ResponseSyntax")**


The date and time the invalidation request was first made.


Type: Timestamp




**[Id](#API_GetInvalidationForDistributionTenant_ResponseSyntax "#API_GetInvalidationForDistributionTenant_ResponseSyntax")**


The identifier for the invalidation request. For example:
 `IDFDVBD632BHDS5`.


Type: String




**[InvalidationBatch](#API_GetInvalidationForDistributionTenant_ResponseSyntax "#API_GetInvalidationForDistributionTenant_ResponseSyntax")**


The current invalidation information for the batch request.


Type: [InvalidationBatch](API_InvalidationBatch.md "API_InvalidationBatch.md") object




**[Status](#API_GetInvalidationForDistributionTenant_ResponseSyntax "#API_GetInvalidationForDistributionTenant_ResponseSyntax")**


The status of the invalidation request. When the invalidation batch is finished, the
 status is `Completed`.


Type: String




## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**EntityNotFound** 


The entity was not found.


HTTP Status Code: 404




**NoSuchInvalidation** 


The specified invalidation does not exist.


HTTP Status Code: 404




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/GetInvalidationForDistributionTenant")

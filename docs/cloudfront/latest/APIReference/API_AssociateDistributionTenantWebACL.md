# AssociateDistributionTenantWebACL

Associates the AWS WAF web ACL with a distribution tenant.


## Request Syntax



```
PUT /2020-05-31/distribution-tenant/`Id`/associate-web-acl HTTP/1.1
If-Match: `IfMatch`
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionTenantWebACLRequest xmlns="http://cloudfront.amazonaws.com/doc/2020-05-31/">
   <WebACLArn>`string`</WebACLArn>
</AssociateDistributionTenantWebACLRequest>
```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_AssociateDistributionTenantWebACL_RequestSyntax "#API_AssociateDistributionTenantWebACL_RequestSyntax")**


The ID of the distribution tenant.


Required: Yes




**[If-Match](#API_AssociateDistributionTenantWebACL_RequestSyntax "#API_AssociateDistributionTenantWebACL_RequestSyntax")**


The current `ETag` of the distribution tenant. This value is returned in the response of the `GetDistributionTenant` API operation.




## Request Body


The request accepts the following data in XML format.





**[AssociateDistributionTenantWebACLRequest](#API_AssociateDistributionTenantWebACL_RequestSyntax "#API_AssociateDistributionTenantWebACL_RequestSyntax")**


Root level tag for the AssociateDistributionTenantWebACLRequest parameters.


Required: Yes




**[WebACLArn](#API_AssociateDistributionTenantWebACL_RequestSyntax "#API_AssociateDistributionTenantWebACL_RequestSyntax")**


The Amazon Resource Name (ARN) of the AWS WAF web ACL to associate.


Type: String


Required: Yes




## Response Syntax



```
HTTP/1.1 200
ETag: `ETag`
<?xml version="1.0" encoding="UTF-8"?>
<AssociateDistributionTenantWebACLResult>
   <Id>***string***</Id>
   <WebACLArn>***string***</WebACLArn>
</AssociateDistributionTenantWebACLResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[ETag](#API_AssociateDistributionTenantWebACL_ResponseSyntax "#API_AssociateDistributionTenantWebACL_ResponseSyntax")**


The current version of the distribution tenant.




The following data is returned in XML format by the service.





**[AssociateDistributionTenantWebACLResult](#API_AssociateDistributionTenantWebACL_ResponseSyntax "#API_AssociateDistributionTenantWebACL_ResponseSyntax")**


Root level tag for the AssociateDistributionTenantWebACLResult parameters.


Required: Yes




**[Id](#API_AssociateDistributionTenantWebACL_ResponseSyntax "#API_AssociateDistributionTenantWebACL_ResponseSyntax")**


The ID of the distribution tenant.


Type: String




**[WebACLArn](#API_AssociateDistributionTenantWebACL_ResponseSyntax "#API_AssociateDistributionTenantWebACL_ResponseSyntax")**


The ARN of the AWS WAF web ACL that you associated with the distribution tenant.


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




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/AssociateDistributionTenantWebACL")

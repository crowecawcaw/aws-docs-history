# DisassociateDistributionWebACL

Disassociates a distribution from the AWS WAF web ACL.


## Request Syntax



```
PUT /2020-05-31/distribution/`Id`/disassociate-web-acl HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_DisassociateDistributionWebACL_RequestSyntax "#API_DisassociateDistributionWebACL_RequestSyntax")**


The ID of the distribution.


Required: Yes




**[If-Match](#API_DisassociateDistributionWebACL_RequestSyntax "#API_DisassociateDistributionWebACL_RequestSyntax")**


The value of the `ETag` header that you received when retrieving the distribution that you're disassociating from the AWS WAF web ACL.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
ETag: `ETag`
<?xml version="1.0" encoding="UTF-8"?>
<DisassociateDistributionWebACLResult>
   <Id>***string***</Id>
</DisassociateDistributionWebACLResult>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The response returns the following HTTP headers.





**[ETag](#API_DisassociateDistributionWebACL_ResponseSyntax "#API_DisassociateDistributionWebACL_ResponseSyntax")**


The current version of the distribution.




The following data is returned in XML format by the service.





**[DisassociateDistributionWebACLResult](#API_DisassociateDistributionWebACL_ResponseSyntax "#API_DisassociateDistributionWebACL_ResponseSyntax")**


Root level tag for the DisassociateDistributionWebACLResult parameters.


Required: Yes




**[Id](#API_DisassociateDistributionWebACL_ResponseSyntax "#API_DisassociateDistributionWebACL_ResponseSyntax")**


The ID of the distribution.


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



* [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DisassociateDistributionWebACL")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DisassociateDistributionWebACL "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DisassociateDistributionWebACL")

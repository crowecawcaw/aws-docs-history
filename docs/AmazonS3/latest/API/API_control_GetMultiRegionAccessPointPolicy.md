# GetMultiRegionAccessPointPolicy

###### Note

This operation is not supported by directory buckets.

Returns the access control policy of the specified Multi-Region Access Point.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

The following actions are related to
 `GetMultiRegionAccessPointPolicy`:


* [GetMultiRegionAccessPointPolicyStatus](API_control_GetMultiRegionAccessPointPolicyStatus.md "API_control_GetMultiRegionAccessPointPolicyStatus.md")
* [PutMultiRegionAccessPointPolicy](API_control_PutMultiRegionAccessPointPolicy.md "API_control_PutMultiRegionAccessPointPolicy.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/mrap/instances/`name+`/policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetMultiRegionAccessPointPolicy_RequestSyntax "#API_control_GetMultiRegionAccessPointPolicy_RequestSyntax")**


Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more
 information about the distinction between the name and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming "../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming") in the
 *Amazon S3 User Guide*.


Length Constraints: Maximum length of 50.


Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`



Required: Yes




**[x-amz-account-id](#API_control_GetMultiRegionAccessPointPolicy_RequestSyntax "#API_control_GetMultiRegionAccessPointPolicy_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetMultiRegionAccessPointPolicyResult](#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-GetMultiRegionAccessPointPolicyResult "#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-GetMultiRegionAccessPointPolicyResult")>
   <[Policy](#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-Policy "#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-Policy")>
      <[Established](API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Established "API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Established")>
         <[Policy](API_control_EstablishedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_EstablishedMultiRegionAccessPointPolicy-Policy "API_control_EstablishedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_EstablishedMultiRegionAccessPointPolicy-Policy")>***string***</[Policy](API_control_EstablishedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_EstablishedMultiRegionAccessPointPolicy-Policy "API_control_EstablishedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_EstablishedMultiRegionAccessPointPolicy-Policy")>
      </[Established](API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Established "API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Established")>
      <[Proposed](API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Proposed "API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Proposed")>
         <[Policy](API_control_ProposedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_ProposedMultiRegionAccessPointPolicy-Policy "API_control_ProposedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_ProposedMultiRegionAccessPointPolicy-Policy")>***string***</[Policy](API_control_ProposedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_ProposedMultiRegionAccessPointPolicy-Policy "API_control_ProposedMultiRegionAccessPointPolicy.md#AmazonS3-Type-control_ProposedMultiRegionAccessPointPolicy-Policy")>
      </[Proposed](API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Proposed "API_control_MultiRegionAccessPointPolicyDocument.md#AmazonS3-Type-control_MultiRegionAccessPointPolicyDocument-Proposed")>
   </[Policy](#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-Policy "#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-Policy")>
</[GetMultiRegionAccessPointPolicyResult](#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-GetMultiRegionAccessPointPolicyResult "#AmazonS3-control_GetMultiRegionAccessPointPolicy-response-GetMultiRegionAccessPointPolicyResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetMultiRegionAccessPointPolicyResult](#API_control_GetMultiRegionAccessPointPolicy_ResponseSyntax "#API_control_GetMultiRegionAccessPointPolicy_ResponseSyntax")**


Root level tag for the GetMultiRegionAccessPointPolicyResult parameters.


Required: Yes




**[Policy](#API_control_GetMultiRegionAccessPointPolicy_ResponseSyntax "#API_control_GetMultiRegionAccessPointPolicy_ResponseSyntax")**


The policy associated with the specified Multi-Region Access Point.


Type: [MultiRegionAccessPointPolicyDocument](API_control_MultiRegionAccessPointPolicyDocument.md "API_control_MultiRegionAccessPointPolicyDocument.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicy")

# PutMultiRegionAccessPointPolicy

###### Note

This operation is not supported by directory buckets.

Associates an access control policy with the specified Multi-Region Access Point. Each Multi-Region Access Point can have only
 one policy, so a request made to this action replaces any existing policy that is
 associated with the specified Multi-Region Access Point.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

The following actions are related to
 `PutMultiRegionAccessPointPolicy`:


* [GetMultiRegionAccessPointPolicy](API_control_GetMultiRegionAccessPointPolicy.md "API_control_GetMultiRegionAccessPointPolicy.md")
* [GetMultiRegionAccessPointPolicyStatus](API_control_GetMultiRegionAccessPointPolicyStatus.md "API_control_GetMultiRegionAccessPointPolicyStatus.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/async-requests/mrap/put-policy HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PutMultiRegionAccessPointPolicyRequest](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-PutMultiRegionAccessPointPolicyRequest "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-PutMultiRegionAccessPointPolicyRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[ClientToken](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-ClientToken "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-ClientToken")>`string`</[ClientToken](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-ClientToken "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-ClientToken")>
   <[Details](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-Details "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-Details")>
      <[Name](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name")>`string`</[Name](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name")>
      <[Policy](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy")>`string`</[Policy](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy")>
   </[Details](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-Details "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-Details")>
</[PutMultiRegionAccessPointPolicyRequest](#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-PutMultiRegionAccessPointPolicyRequest "#AmazonS3-control_PutMultiRegionAccessPointPolicy-request-PutMultiRegionAccessPointPolicyRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax "#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PutMultiRegionAccessPointPolicyRequest](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax "#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax")**


Root level tag for the PutMultiRegionAccessPointPolicyRequest parameters.


Required: Yes




**[ClientToken](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax "#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax")**


An idempotency token used to identify the request and guarantee that requests are
 unique.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `\S+`



Required: Yes




**[Details](#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax "#API_control_PutMultiRegionAccessPointPolicy_RequestSyntax")**


A container element containing the details of the policy for the Multi-Region Access Point.


Type: [PutMultiRegionAccessPointPolicyInput](API_control_PutMultiRegionAccessPointPolicyInput.md "API_control_PutMultiRegionAccessPointPolicyInput.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[PutMultiRegionAccessPointPolicyResult](#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-PutMultiRegionAccessPointPolicyResult "#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-PutMultiRegionAccessPointPolicyResult")>
   <[RequestTokenARN](#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-RequestTokenARN "#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-RequestTokenARN")>***string***</[RequestTokenARN](#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-RequestTokenARN "#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-RequestTokenARN")>
</[PutMultiRegionAccessPointPolicyResult](#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-PutMultiRegionAccessPointPolicyResult "#AmazonS3-control_PutMultiRegionAccessPointPolicy-response-PutMultiRegionAccessPointPolicyResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[PutMultiRegionAccessPointPolicyResult](#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax "#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax")**


Root level tag for the PutMultiRegionAccessPointPolicyResult parameters.


Required: Yes




**[RequestTokenARN](#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax "#API_control_PutMultiRegionAccessPointPolicy_ResponseSyntax")**


The request token associated with the request. You can use this token with [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md") to determine the status of asynchronous
 requests.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:.+`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicy")

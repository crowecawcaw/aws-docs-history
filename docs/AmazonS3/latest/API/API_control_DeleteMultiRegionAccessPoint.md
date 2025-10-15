# DeleteMultiRegionAccessPoint

###### Note

This operation is not supported by directory buckets.

Deletes a Multi-Region Access Point. This action does not delete the buckets associated with the Multi-Region Access Point,
 only the Multi-Region Access Point itself.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

This request is asynchronous, meaning that you might receive a response before the
 command has completed. When this request provides a response, it provides a token that you
 can use to monitor the status of the request with
 `DescribeMultiRegionAccessPointOperation`.

The following actions are related to `DeleteMultiRegionAccessPoint`:


* [CreateMultiRegionAccessPoint](API_control_CreateMultiRegionAccessPoint.md "API_control_CreateMultiRegionAccessPoint.md")
* [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md")
* [GetMultiRegionAccessPoint](API_control_GetMultiRegionAccessPoint.md "API_control_GetMultiRegionAccessPoint.md")
* [ListMultiRegionAccessPoints](API_control_ListMultiRegionAccessPoints.md "API_control_ListMultiRegionAccessPoints.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/async-requests/mrap/delete HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[DeleteMultiRegionAccessPointRequest](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-DeleteMultiRegionAccessPointRequest "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-DeleteMultiRegionAccessPointRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[ClientToken](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-ClientToken "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-ClientToken")>`string`</[ClientToken](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-ClientToken "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-ClientToken")>
   <[Details](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-Details "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-Details")>
      <[Name](API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name "API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name")>`string`</[Name](API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name "API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name")>
   </[Details](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-Details "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-Details")>
</[DeleteMultiRegionAccessPointRequest](#AmazonS3-control_DeleteMultiRegionAccessPoint-request-DeleteMultiRegionAccessPointRequest "#AmazonS3-control_DeleteMultiRegionAccessPoint-request-DeleteMultiRegionAccessPointRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax "#API_control_DeleteMultiRegionAccessPoint_RequestSyntax")**


The AWS account ID for the owner of the Multi-Region Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[DeleteMultiRegionAccessPointRequest](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax "#API_control_DeleteMultiRegionAccessPoint_RequestSyntax")**


Root level tag for the DeleteMultiRegionAccessPointRequest parameters.


Required: Yes




**[ClientToken](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax "#API_control_DeleteMultiRegionAccessPoint_RequestSyntax")**


An idempotency token used to identify the request and guarantee that requests are
 unique.


Type: String


Length Constraints: Maximum length of 64.


Pattern: `\S+`



Required: Yes




**[Details](#API_control_DeleteMultiRegionAccessPoint_RequestSyntax "#API_control_DeleteMultiRegionAccessPoint_RequestSyntax")**


A container element containing details about the Multi-Region Access Point.


Type: [DeleteMultiRegionAccessPointInput](API_control_DeleteMultiRegionAccessPointInput.md "API_control_DeleteMultiRegionAccessPointInput.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[DeleteMultiRegionAccessPointResult](#AmazonS3-control_DeleteMultiRegionAccessPoint-response-DeleteMultiRegionAccessPointResult "#AmazonS3-control_DeleteMultiRegionAccessPoint-response-DeleteMultiRegionAccessPointResult")>
   <[RequestTokenARN](#AmazonS3-control_DeleteMultiRegionAccessPoint-response-RequestTokenARN "#AmazonS3-control_DeleteMultiRegionAccessPoint-response-RequestTokenARN")>***string***</[RequestTokenARN](#AmazonS3-control_DeleteMultiRegionAccessPoint-response-RequestTokenARN "#AmazonS3-control_DeleteMultiRegionAccessPoint-response-RequestTokenARN")>
</[DeleteMultiRegionAccessPointResult](#AmazonS3-control_DeleteMultiRegionAccessPoint-response-DeleteMultiRegionAccessPointResult "#AmazonS3-control_DeleteMultiRegionAccessPoint-response-DeleteMultiRegionAccessPointResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[DeleteMultiRegionAccessPointResult](#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax "#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax")**


Root level tag for the DeleteMultiRegionAccessPointResult parameters.


Required: Yes




**[RequestTokenARN](#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax "#API_control_DeleteMultiRegionAccessPoint_ResponseSyntax")**


The request token associated with the request. You can use this token with [DescribeMultiRegionAccessPointOperation](API_control_DescribeMultiRegionAccessPointOperation.md "API_control_DescribeMultiRegionAccessPointOperation.md") to determine the status of asynchronous
 requests.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:.+`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DeleteMultiRegionAccessPoint")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DeleteMultiRegionAccessPoint")

# DescribeMultiRegionAccessPointOperation

###### Note

This operation is not supported by directory buckets.

Retrieves the status of an asynchronous request to manage a Multi-Region Access Point. For more information
 about managing Multi-Region Access Points and how asynchronous requests work, see [Using Multi-Region Access Points](../userguide/MrapOperations.md "../userguide/MrapOperations.md") in the
 *Amazon S3 User Guide*.

The following actions are related to `GetMultiRegionAccessPoint`:


* [CreateMultiRegionAccessPoint](API_control_CreateMultiRegionAccessPoint.md "API_control_CreateMultiRegionAccessPoint.md")
* [DeleteMultiRegionAccessPoint](API_control_DeleteMultiRegionAccessPoint.md "API_control_DeleteMultiRegionAccessPoint.md")
* [GetMultiRegionAccessPoint](API_control_GetMultiRegionAccessPoint.md "API_control_GetMultiRegionAccessPoint.md")
* [ListMultiRegionAccessPoints](API_control_ListMultiRegionAccessPoints.md "API_control_ListMultiRegionAccessPoints.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/async-requests/mrap/`request_token+` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[request\_token](#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax "#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax")**


The request token associated with the request you want to know about. This request token
 is returned as part of the response when you make an asynchronous request. You provide this
 token to query about the status of the asynchronous action.


Length Constraints: Minimum length of 1. Maximum length of 1024.


Pattern: `arn:.+`



Required: Yes




**[x-amz-account-id](#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax "#API_control_DescribeMultiRegionAccessPointOperation_RequestSyntax")**


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
<[DescribeMultiRegionAccessPointOperationResult](#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-DescribeMultiRegionAccessPointOperationResult "#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-DescribeMultiRegionAccessPointOperationResult")>
   <[AsyncOperation](#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-AsyncOperation "#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-AsyncOperation")>
      <[CreationTime](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-CreationTime "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-CreationTime")>***timestamp***</[CreationTime](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-CreationTime "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-CreationTime")>
      <[Operation](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-Operation "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-Operation")>***string***</[Operation](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-Operation "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-Operation")>
      <[RequestParameters](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestParameters "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestParameters")>
         <[CreateMultiRegionAccessPointRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-CreateMultiRegionAccessPointRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-CreateMultiRegionAccessPointRequest")>
            <[Name](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name")>***string***</[Name](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Name")>
            <[PublicAccessBlock](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock")>
               <[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>***boolean***</[BlockPublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicAcls")>
               <[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>***boolean***</[BlockPublicPolicy](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-BlockPublicPolicy")>
               <[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>***boolean***</[IgnorePublicAcls](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-IgnorePublicAcls")>
               <[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>***boolean***</[RestrictPublicBuckets](API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets "API_control_PublicAccessBlockConfiguration.md#AmazonS3-Type-control_PublicAccessBlockConfiguration-RestrictPublicBuckets")>
            </[PublicAccessBlock](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-PublicAccessBlock")>
            <[Regions](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions")>
               <Region>
                  <[Bucket](API_control_Region.md#AmazonS3-Type-control_Region-Bucket "API_control_Region.md#AmazonS3-Type-control_Region-Bucket")>***string***</[Bucket](API_control_Region.md#AmazonS3-Type-control_Region-Bucket "API_control_Region.md#AmazonS3-Type-control_Region-Bucket")>
                  <[BucketAccountId](API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId "API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId")>***string***</[BucketAccountId](API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId "API_control_Region.md#AmazonS3-Type-control_Region-BucketAccountId")>
               </Region>
            </[Regions](API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions "API_control_CreateMultiRegionAccessPointInput.md#AmazonS3-Type-control_CreateMultiRegionAccessPointInput-Regions")>
         </[CreateMultiRegionAccessPointRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-CreateMultiRegionAccessPointRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-CreateMultiRegionAccessPointRequest")>
         <[DeleteMultiRegionAccessPointRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-DeleteMultiRegionAccessPointRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-DeleteMultiRegionAccessPointRequest")>
            <[Name](API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name "API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name")>***string***</[Name](API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name "API_control_DeleteMultiRegionAccessPointInput.md#AmazonS3-Type-control_DeleteMultiRegionAccessPointInput-Name")>
         </[DeleteMultiRegionAccessPointRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-DeleteMultiRegionAccessPointRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-DeleteMultiRegionAccessPointRequest")>
         <[PutMultiRegionAccessPointPolicyRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-PutMultiRegionAccessPointPolicyRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-PutMultiRegionAccessPointPolicyRequest")>
            <[Name](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name")>***string***</[Name](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name")>
            <[Policy](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy")>***string***</[Policy](API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy "API_control_PutMultiRegionAccessPointPolicyInput.md#AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy")>
         </[PutMultiRegionAccessPointPolicyRequest](API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-PutMultiRegionAccessPointPolicyRequest "API_control_AsyncRequestParameters.md#AmazonS3-Type-control_AsyncRequestParameters-PutMultiRegionAccessPointPolicyRequest")>
      </[RequestParameters](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestParameters "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestParameters")>
      <[RequestStatus](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestStatus "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestStatus")>***string***</[RequestStatus](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestStatus "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestStatus")>
      <[RequestTokenARN](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestTokenARN "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestTokenARN")>***string***</[RequestTokenARN](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestTokenARN "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-RequestTokenARN")>
      <[ResponseDetails](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-ResponseDetails "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-ResponseDetails")>
         <[ErrorDetails](API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-ErrorDetails "API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-ErrorDetails")>
            <[Code](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Code "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Code")>***string***</[Code](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Code "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Code")>
            <[Message](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Message "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Message")>***string***</[Message](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Message "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Message")>
            <[RequestId](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-RequestId "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-RequestId")>***string***</[RequestId](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-RequestId "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-RequestId")>
            <[Resource](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Resource "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Resource")>***string***</[Resource](API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Resource "API_control_AsyncErrorDetails.md#AmazonS3-Type-control_AsyncErrorDetails-Resource")>
         </[ErrorDetails](API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-ErrorDetails "API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-ErrorDetails")>
         <[MultiRegionAccessPointDetails](API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-MultiRegionAccessPointDetails "API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-MultiRegionAccessPointDetails")>
            <[Regions](API_control_MultiRegionAccessPointsAsyncResponse.md#AmazonS3-Type-control_MultiRegionAccessPointsAsyncResponse-Regions "API_control_MultiRegionAccessPointsAsyncResponse.md#AmazonS3-Type-control_MultiRegionAccessPointsAsyncResponse-Regions")>
               <Region>
                  <[Name](API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-Name "API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-Name")>***string***</[Name](API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-Name "API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-Name")>
                  <[RequestStatus](API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-RequestStatus "API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-RequestStatus")>***string***</[RequestStatus](API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-RequestStatus "API_control_MultiRegionAccessPointRegionalResponse.md#AmazonS3-Type-control_MultiRegionAccessPointRegionalResponse-RequestStatus")>
               </Region>
            </[Regions](API_control_MultiRegionAccessPointsAsyncResponse.md#AmazonS3-Type-control_MultiRegionAccessPointsAsyncResponse-Regions "API_control_MultiRegionAccessPointsAsyncResponse.md#AmazonS3-Type-control_MultiRegionAccessPointsAsyncResponse-Regions")>
         </[MultiRegionAccessPointDetails](API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-MultiRegionAccessPointDetails "API_control_AsyncResponseDetails.md#AmazonS3-Type-control_AsyncResponseDetails-MultiRegionAccessPointDetails")>
      </[ResponseDetails](API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-ResponseDetails "API_control_AsyncOperation.md#AmazonS3-Type-control_AsyncOperation-ResponseDetails")>
   </[AsyncOperation](#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-AsyncOperation "#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-AsyncOperation")>
</[DescribeMultiRegionAccessPointOperationResult](#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-DescribeMultiRegionAccessPointOperationResult "#AmazonS3-control_DescribeMultiRegionAccessPointOperation-response-DescribeMultiRegionAccessPointOperationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[DescribeMultiRegionAccessPointOperationResult](#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax "#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax")**


Root level tag for the DescribeMultiRegionAccessPointOperationResult parameters.


Required: Yes




**[AsyncOperation](#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax "#API_control_DescribeMultiRegionAccessPointOperation_ResponseSyntax")**


A container element containing the details of the asynchronous operation.


Type: [AsyncOperation](API_control_AsyncOperation.md "API_control_AsyncOperation.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/DescribeMultiRegionAccessPointOperation")

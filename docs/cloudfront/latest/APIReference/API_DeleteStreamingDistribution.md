# DeleteStreamingDistribution

Delete a streaming distribution. To delete an RTMP distribution using the CloudFront API,
 perform the following steps.


**To delete an RTMP distribution using the CloudFront
 API**:


1. Disable the RTMP distribution.
2. Submit a `GET Streaming Distribution Config` request to get the
 current configuration and the `Etag` header for the distribution.
3. Update the XML document that was returned in the response to your `GET
 Streaming Distribution Config` request to change the value of
 `Enabled` to `false`.
4. Submit a `PUT Streaming Distribution Config` request to update the
 configuration for your distribution. In the request body, include the XML
 document that you updated in Step 3. Then set the value of the HTTP
 `If-Match` header to the value of the `ETag` header
 that CloudFront returned when you submitted the `GET Streaming Distribution
 Config` request in Step 2.
5. Review the response to the `PUT Streaming Distribution Config`
 request to confirm that the distribution was successfully disabled.
6. Submit a `GET Streaming Distribution Config` request to confirm
 that your changes have propagated. When propagation is complete, the value of
 `Status` is `Deployed`.
7. Submit a `DELETE Streaming Distribution` request. Set the value of
 the HTTP `If-Match` header to the value of the `ETag`
 header that CloudFront returned when you submitted the `GET Streaming
 Distribution Config` request in Step 2.
8. Review the response to your `DELETE Streaming Distribution` request
 to confirm that the distribution was successfully deleted.
For information about deleting a distribution using the CloudFront console, see [Deleting a
 Distribution](../../../AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.md "../../../AmazonCloudFront/latest/DeveloperGuide/HowToDeleteDistribution.md") in the *Amazon CloudFront Developer Guide*.


## Request Syntax



```
DELETE /2020-05-31/streaming-distribution/`Id` HTTP/1.1
If-Match: `IfMatch`

```

## URI Request Parameters


The request uses the following URI parameters.





**[Id](#API_DeleteStreamingDistribution_RequestSyntax "#API_DeleteStreamingDistribution_RequestSyntax")**


The distribution ID.


Required: Yes




**[If-Match](#API_DeleteStreamingDistribution_RequestSyntax "#API_DeleteStreamingDistribution_RequestSyntax")**


The value of the `ETag` header that you received when you disabled the
 streaming distribution. For example: `E2QWRUHAPOMQZL`.




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 204

```

## Response Elements


If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.


## Errors


For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").





**AccessDenied** 


Access denied.


HTTP Status Code: 403




**InvalidIfMatchVersion** 


The `If-Match` version is missing or not valid.


HTTP Status Code: 400




**NoSuchStreamingDistribution** 


The specified streaming distribution does not exist.


HTTP Status Code: 404




**PreconditionFailed** 


The precondition in one or more of the request fields evaluated to
 `false`.


HTTP Status Code: 412




**StreamingDistributionNotDisabled** 


The specified CloudFront distribution is not disabled. You must disable the distribution
 before you can delete it.


HTTP Status Code: 409




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/cli2/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/DotNetSDKV3/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForGoV2/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForKotlin/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForPHPV3/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/boto3/cloudfront-2020-05-31/DeleteStreamingDistribution")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteStreamingDistribution "https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/DeleteStreamingDistribution")

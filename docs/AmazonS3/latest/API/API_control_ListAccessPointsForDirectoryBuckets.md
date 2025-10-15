# ListAccessPointsForDirectoryBuckets

Returns a list of the access points that are owned by the AWS account and that are associated
 with the specified directory bucket.

To list access points for general purpose buckets, see [ListAccesspoints](API_control_ListAccessPoints.md "API_control_ListAccessPoints.md").

To use this operation, you must have the permission to perform the
 `s3express:ListAccessPointsForDirectoryBuckets`
 action.

For information about REST API errors, see [REST error responses](ErrorResponses.md#RESTErrorResponses "ErrorResponses.md#RESTErrorResponses").

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspointfordirectory?directoryBucket=`DirectoryBucket`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[directoryBucket](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax "#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax")**


The name of the directory bucket associated with the access points you want to list.


Length Constraints: Minimum length of 3. Maximum length of 255.




**[maxResults](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax "#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax")**


The maximum number of access points that you would like returned in the
 `ListAccessPointsForDirectoryBuckets` response. If the directory bucket is
 associated with more than this number of access points, the results include the pagination token
 `NextToken`. Make another call using the `NextToken` to retrieve
 more results.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax "#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax")**


 If `NextToken` is returned, there are more access points available than requested in
 the `maxResults` value. The value of `NextToken` is a unique
 pagination token for each page. Make the call again using the returned token to retrieve
 the next page. Keep all other arguments unchanged. Each pagination token expires after 24
 hours. 


Length Constraints: Minimum length of 1. Maximum length of 1024.




**[x-amz-account-id](#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax "#API_control_ListAccessPointsForDirectoryBuckets_RequestSyntax")**


The AWS account ID that owns the access points.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListAccessPointsForDirectoryBucketsResult](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-ListAccessPointsForDirectoryBucketsResult "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-ListAccessPointsForDirectoryBucketsResult")>
   <[AccessPointList](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-AccessPointList "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-AccessPointList")>
      <AccessPoint>
         <[AccessPointArn](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-AccessPointArn "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-AccessPointArn")>***string***</[AccessPointArn](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-AccessPointArn "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-AccessPointArn")>
         <[Alias](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Alias "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Alias")>***string***</[Alias](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Alias "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Alias")>
         <[Bucket](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Bucket "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Bucket")>***string***</[Bucket](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Bucket "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Bucket")>
         <[BucketAccountId](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-BucketAccountId "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-BucketAccountId")>***string***</[BucketAccountId](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-BucketAccountId "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-BucketAccountId")>
         <[DataSourceId](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceId "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceId")>***string***</[DataSourceId](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceId "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceId")>
         <[DataSourceType](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceType "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceType")>***string***</[DataSourceType](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceType "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-DataSourceType")>
         <[Name](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Name "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Name")>***string***</[Name](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Name "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-Name")>
         <[NetworkOrigin](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-NetworkOrigin "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-NetworkOrigin")>***string***</[NetworkOrigin](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-NetworkOrigin "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-NetworkOrigin")>
         <[VpcConfiguration](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-VpcConfiguration "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-VpcConfiguration")>
            <[VpcId](API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId "API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId")>***string***</[VpcId](API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId "API_control_VpcConfiguration.md#AmazonS3-Type-control_VpcConfiguration-VpcId")>
         </[VpcConfiguration](API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-VpcConfiguration "API_control_AccessPoint.md#AmazonS3-Type-control_AccessPoint-VpcConfiguration")>
      </AccessPoint>
   </[AccessPointList](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-AccessPointList "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-AccessPointList")>
   <[NextToken](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-NextToken "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-NextToken "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-NextToken")>
</[ListAccessPointsForDirectoryBucketsResult](#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-ListAccessPointsForDirectoryBucketsResult "#AmazonS3-control_ListAccessPointsForDirectoryBuckets-response-ListAccessPointsForDirectoryBucketsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAccessPointsForDirectoryBucketsResult](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax "#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax")**


Root level tag for the ListAccessPointsForDirectoryBucketsResult parameters.


Required: Yes




**[AccessPointList](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax "#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax")**


Contains identification and configuration information for one or more access points associated
 with the directory bucket.


Type: Array of [AccessPoint](API_control_AccessPoint.md "API_control_AccessPoint.md") data types




**[NextToken](#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax "#API_control_ListAccessPointsForDirectoryBuckets_ResponseSyntax")**


 If `NextToken` is returned, there are more access points available than requested in
 the `maxResults` value. The value of `NextToken` is a unique
 pagination token for each page. Make the call again using the returned token to retrieve
 the next page. Keep all other arguments unchanged. Each pagination token expires after 24
 hours. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPointsForDirectoryBuckets")

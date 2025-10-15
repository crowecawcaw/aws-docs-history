# ListAccessPoints

###### Note

This operation is not supported by directory buckets.

Returns a list of the access points. You can retrieve up to 1,000 access points per call. If the call
 returns more than 1,000 access points (or the number specified in `maxResults`,
 whichever is less), the response will include a continuation token that you can use to list
 the additional access points.

Returns only access points attached to S3 buckets by default. To return all access points specify
 `DataSourceType` as `ALL`.

All Amazon S3 on Outposts REST API requests for this action require an additional parameter of `x-amz-outpost-id` to be passed with the request. In addition, you must use an S3 on Outposts endpoint hostname prefix instead of `s3-control`. For an example of the request syntax for Amazon S3 on Outposts that uses the S3 on Outposts endpoint hostname prefix and the `x-amz-outpost-id` derived by using the access point ARN, see the [Examples](API_control_GetAccessPoint.md#API_control_GetAccessPoint_Examples "API_control_GetAccessPoint.md#API_control_GetAccessPoint_Examples") section.

The following actions are related to `ListAccessPoints`:


* [CreateAccessPoint](API_control_CreateAccessPoint.md "API_control_CreateAccessPoint.md")
* [DeleteAccessPoint](API_control_DeleteAccessPoint.md "API_control_DeleteAccessPoint.md")
* [GetAccessPoint](API_control_GetAccessPoint.md "API_control_GetAccessPoint.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspoint?bucket=`Bucket`&dataSourceId=`DataSourceId`&dataSourceType=`DataSourceType`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[bucket](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


The name of the bucket whose associated access points you want to list.


For using this parameter with Amazon S3 on Outposts with the REST API, you must specify the name and the x-amz-outpost-id as well.


For using this parameter with S3 on Outposts with the AWS SDK and CLI, you must specify the ARN of the bucket accessed in the format `arn:aws:s3-outposts:<Region>:<account-id>:outpost/<outpost-id>/bucket/<my-bucket-name>`. For example, to access the bucket `reports` through Outpost `my-outpost` owned by account `123456789012` in Region `us-west-2`, use the URL encoding of `arn:aws:s3-outposts:us-west-2:123456789012:outpost/my-outpost/bucket/reports`. The value must be URL encoded. 


Length Constraints: Minimum length of 3. Maximum length of 255.




**[dataSourceId](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


The unique identifier for the data source of the access point.


Length Constraints: Maximum length of 191.




**[dataSourceType](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


The type of the data source that the access point is attached to. Returns only access points attached to
 S3 buckets by default. To return all access points specify `DataSourceType` as
 `ALL`.




**[maxResults](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


The maximum number of access points that you want to include in the list. If the specified
 bucket has more than this number of access points, then the response will include a continuation
 token in the `NextToken` field that you can use to retrieve the next page of
 access points.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


A continuation token. If a previous call to `ListAccessPoints` returned a
 continuation token in the `NextToken` field, then providing that value here
 causes Amazon S3 to retrieve the next page of results.


Length Constraints: Minimum length of 1. Maximum length of 1024.




**[x-amz-account-id](#API_control_ListAccessPoints_RequestSyntax "#API_control_ListAccessPoints_RequestSyntax")**


The AWS account ID for the account that owns the specified access points.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListAccessPointsResult](#AmazonS3-control_ListAccessPoints-response-ListAccessPointsResult "#AmazonS3-control_ListAccessPoints-response-ListAccessPointsResult")>
   <[AccessPointList](#AmazonS3-control_ListAccessPoints-response-AccessPointList "#AmazonS3-control_ListAccessPoints-response-AccessPointList")>
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
   </[AccessPointList](#AmazonS3-control_ListAccessPoints-response-AccessPointList "#AmazonS3-control_ListAccessPoints-response-AccessPointList")>
   <[NextToken](#AmazonS3-control_ListAccessPoints-response-NextToken "#AmazonS3-control_ListAccessPoints-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListAccessPoints-response-NextToken "#AmazonS3-control_ListAccessPoints-response-NextToken")>
</[ListAccessPointsResult](#AmazonS3-control_ListAccessPoints-response-ListAccessPointsResult "#AmazonS3-control_ListAccessPoints-response-ListAccessPointsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAccessPointsResult](#API_control_ListAccessPoints_ResponseSyntax "#API_control_ListAccessPoints_ResponseSyntax")**


Root level tag for the ListAccessPointsResult parameters.


Required: Yes




**[AccessPointList](#API_control_ListAccessPoints_ResponseSyntax "#API_control_ListAccessPoints_ResponseSyntax")**


Contains identification and configuration information for one or more access points associated
 with the specified bucket.


Type: Array of [AccessPoint](API_control_AccessPoint.md "API_control_AccessPoint.md") data types




**[NextToken](#API_control_ListAccessPoints_ResponseSyntax "#API_control_ListAccessPoints_ResponseSyntax")**


If the specified bucket has more access points than can be returned in one call to this API,
 this field contains a continuation token that you can provide in subsequent calls to this
 API to retrieve additional access points.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 1024.




## Examples


### Sample request syntax for ListAccessPoints for Amazon S3 on Outposts


The following request returns a list access points of the specified Amazon S3 on Outposts
 bucket `example-outpost-bucket`.



```

           GET /v20180820/accesspoint?Bucket=example-outpost-bucket&MaxResults=MaxResults&NextToken=NextToken HTTP/1.1
           Host: s3-outposts.<Region>.amazonaws.com
           Date: Wed, 28 Oct 2020 22:32:00 GMT
           Authorization: authorization string
           x-amz-account-id: example-account-id
           x-amz-outpost-id: op-01ac5d28a6a232904
         
```

## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessPoints")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPoints "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessPoints")

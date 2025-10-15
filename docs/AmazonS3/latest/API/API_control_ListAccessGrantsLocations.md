# ListAccessGrantsLocations

Returns a list of the locations registered in your S3 Access Grants instance.



Permissions

You must have the `s3:ListAccessGrantsLocations` permission to use
 this operation. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstance/locations?locationscope=`LocationScope`&maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[locationscope](#API_control_ListAccessGrantsLocations_RequestSyntax "#API_control_ListAccessGrantsLocations_RequestSyntax")**


The S3 path to the location that you are registering. The location scope can be the
 default S3 location `s3://`, the S3 path to a bucket
 `s3://<bucket>`, or the S3 path to a bucket and prefix
 `s3://<bucket>/<prefix>`. A prefix in S3 is a string of
 characters at the beginning of an object key name used to organize the objects that you
 store in your S3 buckets. For example, object key names that start with the
 `engineering/` prefix or object key names that start with the
 `marketing/campaigns/` prefix.


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`





**[maxResults](#API_control_ListAccessGrantsLocations_RequestSyntax "#API_control_ListAccessGrantsLocations_RequestSyntax")**


The maximum number of access grants that you would like returned in the `List
 Access Grants` response. If the results include the pagination token
 `NextToken`, make another call using the `NextToken` to determine
 if there are more results.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListAccessGrantsLocations_RequestSyntax "#API_control_ListAccessGrantsLocations_RequestSyntax")**


A pagination token to request the next page of results. Pass this value into a
 subsequent `List Access Grants Locations` request in order to retrieve the next
 page of results.




**[x-amz-account-id](#API_control_ListAccessGrantsLocations_RequestSyntax "#API_control_ListAccessGrantsLocations_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[ListAccessGrantsLocationsResult](#AmazonS3-control_ListAccessGrantsLocations-response-ListAccessGrantsLocationsResult "#AmazonS3-control_ListAccessGrantsLocations-response-ListAccessGrantsLocationsResult")>
   <[NextToken](#AmazonS3-control_ListAccessGrantsLocations-response-NextToken "#AmazonS3-control_ListAccessGrantsLocations-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListAccessGrantsLocations-response-NextToken "#AmazonS3-control_ListAccessGrantsLocations-response-NextToken")>
   <[AccessGrantsLocationsList](#AmazonS3-control_ListAccessGrantsLocations-response-AccessGrantsLocationsList "#AmazonS3-control_ListAccessGrantsLocations-response-AccessGrantsLocationsList")>
      <AccessGrantsLocation>
         <[AccessGrantsLocationArn](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationArn "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationArn")>***string***</[AccessGrantsLocationArn](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationArn "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationArn")>
         <[AccessGrantsLocationId](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationId "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationId")>***string***</[AccessGrantsLocationId](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationId "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-AccessGrantsLocationId")>
         <[CreatedAt](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-CreatedAt "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-CreatedAt")>***timestamp***</[CreatedAt](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-CreatedAt "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-CreatedAt")>
         <[IAMRoleArn](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-IAMRoleArn "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-IAMRoleArn")>***string***</[IAMRoleArn](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-IAMRoleArn "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-IAMRoleArn")>
         <[LocationScope](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-LocationScope "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-LocationScope")>***string***</[LocationScope](API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-LocationScope "API_control_ListAccessGrantsLocationsEntry.md#AmazonS3-Type-control_ListAccessGrantsLocationsEntry-LocationScope")>
      </AccessGrantsLocation>
   </[AccessGrantsLocationsList](#AmazonS3-control_ListAccessGrantsLocations-response-AccessGrantsLocationsList "#AmazonS3-control_ListAccessGrantsLocations-response-AccessGrantsLocationsList")>
</[ListAccessGrantsLocationsResult](#AmazonS3-control_ListAccessGrantsLocations-response-ListAccessGrantsLocationsResult "#AmazonS3-control_ListAccessGrantsLocations-response-ListAccessGrantsLocationsResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAccessGrantsLocationsResult](#API_control_ListAccessGrantsLocations_ResponseSyntax "#API_control_ListAccessGrantsLocations_ResponseSyntax")**


Root level tag for the ListAccessGrantsLocationsResult parameters.


Required: Yes




**[AccessGrantsLocationsList](#API_control_ListAccessGrantsLocations_ResponseSyntax "#API_control_ListAccessGrantsLocations_ResponseSyntax")**


A container for a list of registered locations in an S3 Access Grants instance.


Type: Array of [ListAccessGrantsLocationsEntry](API_control_ListAccessGrantsLocationsEntry.md "API_control_ListAccessGrantsLocationsEntry.md") data types




**[NextToken](#API_control_ListAccessGrantsLocations_ResponseSyntax "#API_control_ListAccessGrantsLocations_ResponseSyntax")**


A pagination token to request the next page of results. Pass this value into a
 subsequent `List Access Grants Locations` request in order to retrieve the next
 page of results.


Type: String




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsLocations")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsLocations "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsLocations")

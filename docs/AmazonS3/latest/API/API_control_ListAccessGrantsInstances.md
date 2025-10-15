# ListAccessGrantsInstances

Returns a list of S3 Access Grants instances. An S3 Access Grants instance serves as a logical grouping for
 your individual access grants. You can only have one S3 Access Grants instance per Region per
 account.



Permissions

You must have the `s3:ListAccessGrantsInstances` permission to use
 this operation. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstances?maxResults=`MaxResults`&nextToken=`NextToken` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[maxResults](#API_control_ListAccessGrantsInstances_RequestSyntax "#API_control_ListAccessGrantsInstances_RequestSyntax")**


The maximum number of access grants that you would like returned in the `List
 Access Grants` response. If the results include the pagination token
 `NextToken`, make another call using the `NextToken` to determine
 if there are more results.


Valid Range: Minimum value of 0. Maximum value of 1000.




**[nextToken](#API_control_ListAccessGrantsInstances_RequestSyntax "#API_control_ListAccessGrantsInstances_RequestSyntax")**


A pagination token to request the next page of results. Pass this value into a
 subsequent `List Access Grants Instances` request in order to retrieve the next
 page of results.




**[x-amz-account-id](#API_control_ListAccessGrantsInstances_RequestSyntax "#API_control_ListAccessGrantsInstances_RequestSyntax")**


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
<[ListAccessGrantsInstancesResult](#AmazonS3-control_ListAccessGrantsInstances-response-ListAccessGrantsInstancesResult "#AmazonS3-control_ListAccessGrantsInstances-response-ListAccessGrantsInstancesResult")>
   <[NextToken](#AmazonS3-control_ListAccessGrantsInstances-response-NextToken "#AmazonS3-control_ListAccessGrantsInstances-response-NextToken")>***string***</[NextToken](#AmazonS3-control_ListAccessGrantsInstances-response-NextToken "#AmazonS3-control_ListAccessGrantsInstances-response-NextToken")>
   <[AccessGrantsInstancesList](#AmazonS3-control_ListAccessGrantsInstances-response-AccessGrantsInstancesList "#AmazonS3-control_ListAccessGrantsInstances-response-AccessGrantsInstancesList")>
      <AccessGrantsInstance>
         <[AccessGrantsInstanceArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceArn")>***string***</[AccessGrantsInstanceArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceArn")>
         <[AccessGrantsInstanceId](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceId "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceId")>***string***</[AccessGrantsInstanceId](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceId "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-AccessGrantsInstanceId")>
         <[CreatedAt](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-CreatedAt "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-CreatedAt")>***timestamp***</[CreatedAt](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-CreatedAt "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-CreatedAt")>
         <[IdentityCenterApplicationArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterApplicationArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterApplicationArn")>***string***</[IdentityCenterApplicationArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterApplicationArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterApplicationArn")>
         <[IdentityCenterArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterArn")>***string***</[IdentityCenterArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterArn")>
         <[IdentityCenterInstanceArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterInstanceArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterInstanceArn")>***string***</[IdentityCenterInstanceArn](API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterInstanceArn "API_control_ListAccessGrantsInstanceEntry.md#AmazonS3-Type-control_ListAccessGrantsInstanceEntry-IdentityCenterInstanceArn")>
      </AccessGrantsInstance>
   </[AccessGrantsInstancesList](#AmazonS3-control_ListAccessGrantsInstances-response-AccessGrantsInstancesList "#AmazonS3-control_ListAccessGrantsInstances-response-AccessGrantsInstancesList")>
</[ListAccessGrantsInstancesResult](#AmazonS3-control_ListAccessGrantsInstances-response-ListAccessGrantsInstancesResult "#AmazonS3-control_ListAccessGrantsInstances-response-ListAccessGrantsInstancesResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[ListAccessGrantsInstancesResult](#API_control_ListAccessGrantsInstances_ResponseSyntax "#API_control_ListAccessGrantsInstances_ResponseSyntax")**


Root level tag for the ListAccessGrantsInstancesResult parameters.


Required: Yes




**[AccessGrantsInstancesList](#API_control_ListAccessGrantsInstances_ResponseSyntax "#API_control_ListAccessGrantsInstances_ResponseSyntax")**


A container for a list of S3 Access Grants instances.


Type: Array of [ListAccessGrantsInstanceEntry](API_control_ListAccessGrantsInstanceEntry.md "API_control_ListAccessGrantsInstanceEntry.md") data types




**[NextToken](#API_control_ListAccessGrantsInstances_ResponseSyntax "#API_control_ListAccessGrantsInstances_ResponseSyntax")**


A pagination token to request the next page of results. Pass this value into a
 subsequent `List Access Grants Instances` request in order to retrieve the next
 page of results.


Type: String




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/ListAccessGrantsInstances")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsInstances "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/ListAccessGrantsInstances")

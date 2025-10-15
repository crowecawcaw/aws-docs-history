# GetMultiRegionAccessPointPolicyStatus

###### Note

This operation is not supported by directory buckets.

Indicates whether the specified Multi-Region Access Point has an access control policy that allows public
 access.

This action will always be routed to the US West (Oregon) Region. For more information
 about the restrictions around working with Multi-Region Access Points, see [Multi-Region Access Point
 restrictions and limitations](../userguide/MultiRegionAccessPointRestrictions.md "../userguide/MultiRegionAccessPointRestrictions.md") in the *Amazon S3 User Guide*.

The following actions are related to
 `GetMultiRegionAccessPointPolicyStatus`:


* [GetMultiRegionAccessPointPolicy](API_control_GetMultiRegionAccessPointPolicy.md "API_control_GetMultiRegionAccessPointPolicy.md")
* [PutMultiRegionAccessPointPolicy](API_control_PutMultiRegionAccessPointPolicy.md "API_control_PutMultiRegionAccessPointPolicy.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/mrap/instances/`name+`/policystatus HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax "#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax")**


Specifies the Multi-Region Access Point. The name of the Multi-Region Access Point is different from the alias. For more
 information about the distinction between the name and the alias of an Multi-Region Access Point, see [Rules for naming Amazon S3 Multi-Region Access Points](../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming "../userguide/CreatingMultiRegionAccessPoints.md#multi-region-access-point-naming") in the
 *Amazon S3 User Guide*.


Length Constraints: Maximum length of 50.


Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`



Required: Yes




**[x-amz-account-id](#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax "#API_control_GetMultiRegionAccessPointPolicyStatus_RequestSyntax")**


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
<[GetMultiRegionAccessPointPolicyStatusResult](#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-GetMultiRegionAccessPointPolicyStatusResult "#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-GetMultiRegionAccessPointPolicyStatusResult")>
   <[Established](#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-Established "#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-Established")>
      <[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>***boolean***</[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>
   </[Established](#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-Established "#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-Established")>
</[GetMultiRegionAccessPointPolicyStatusResult](#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-GetMultiRegionAccessPointPolicyStatusResult "#AmazonS3-control_GetMultiRegionAccessPointPolicyStatus-response-GetMultiRegionAccessPointPolicyStatusResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetMultiRegionAccessPointPolicyStatusResult](#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax "#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax")**


Root level tag for the GetMultiRegionAccessPointPolicyStatusResult parameters.


Required: Yes




**[Established](#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax "#API_control_GetMultiRegionAccessPointPolicyStatus_ResponseSyntax")**


Indicates whether this access point policy is public. For more information about how Amazon S3
 evaluates policies to determine whether they are public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status") in the *Amazon S3 User Guide*. 


Type: [PolicyStatus](API_control_PolicyStatus.md "API_control_PolicyStatus.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetMultiRegionAccessPointPolicyStatus")

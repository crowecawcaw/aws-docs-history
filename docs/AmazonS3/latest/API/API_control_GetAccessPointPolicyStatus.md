# GetAccessPointPolicyStatus

###### Note

This operation is not supported by directory buckets.

Indicates whether the specified access point currently has a policy that allows public access.
 For more information about public access through access points, see [Managing Data Access with Amazon S3
 access points](../userguide/access-points.md "../userguide/access-points.md") in the *Amazon S3 User Guide*.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspoint/`name`/policyStatus HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetAccessPointPolicyStatus_RequestSyntax "#API_control_GetAccessPointPolicyStatus_RequestSyntax")**


The name of the access point whose policy status you want to retrieve.


Length Constraints: Minimum length of 3. Maximum length of 255.


Required: Yes




**[x-amz-account-id](#API_control_GetAccessPointPolicyStatus_RequestSyntax "#API_control_GetAccessPointPolicyStatus_RequestSyntax")**


The account ID for the account that owns the specified access point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessPointPolicyStatusResult](#AmazonS3-control_GetAccessPointPolicyStatus-response-GetAccessPointPolicyStatusResult "#AmazonS3-control_GetAccessPointPolicyStatus-response-GetAccessPointPolicyStatusResult")>
   <[PolicyStatus](#AmazonS3-control_GetAccessPointPolicyStatus-response-PolicyStatus "#AmazonS3-control_GetAccessPointPolicyStatus-response-PolicyStatus")>
      <[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>***boolean***</[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>
   </[PolicyStatus](#AmazonS3-control_GetAccessPointPolicyStatus-response-PolicyStatus "#AmazonS3-control_GetAccessPointPolicyStatus-response-PolicyStatus")>
</[GetAccessPointPolicyStatusResult](#AmazonS3-control_GetAccessPointPolicyStatus-response-GetAccessPointPolicyStatusResult "#AmazonS3-control_GetAccessPointPolicyStatus-response-GetAccessPointPolicyStatusResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessPointPolicyStatusResult](#API_control_GetAccessPointPolicyStatus_ResponseSyntax "#API_control_GetAccessPointPolicyStatus_ResponseSyntax")**


Root level tag for the GetAccessPointPolicyStatusResult parameters.


Required: Yes




**[PolicyStatus](#API_control_GetAccessPointPolicyStatus_ResponseSyntax "#API_control_GetAccessPointPolicyStatus_ResponseSyntax")**


Indicates the current policy status of the specified access point.


Type: [PolicyStatus](API_control_PolicyStatus.md "API_control_PolicyStatus.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyStatus")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyStatus "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyStatus")

# GetAccessPointPolicyStatusForObjectLambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

###### Note

This operation is not supported by directory buckets.

Returns the status of the resource policy associated with an Object Lambda Access Point.

###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accesspointforobjectlambda/`name`/policyStatus HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_GetAccessPointPolicyStatusForObjectLambda_RequestSyntax "#API_control_GetAccessPointPolicyStatusForObjectLambda_RequestSyntax")**


The name of the Object Lambda Access Point.


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessPointPolicyStatusForObjectLambda_RequestSyntax "#API_control_GetAccessPointPolicyStatusForObjectLambda_RequestSyntax")**


The account ID for the account that owns the specified Object Lambda Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request does not have a request body.


## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[GetAccessPointPolicyStatusForObjectLambdaResult](#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-GetAccessPointPolicyStatusForObjectLambdaResult "#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-GetAccessPointPolicyStatusForObjectLambdaResult")>
   <[PolicyStatus](#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-PolicyStatus "#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-PolicyStatus")>
      <[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>***boolean***</[IsPublic](API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic "API_control_PolicyStatus.md#AmazonS3-Type-control_PolicyStatus-IsPublic")>
   </[PolicyStatus](#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-PolicyStatus "#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-PolicyStatus")>
</[GetAccessPointPolicyStatusForObjectLambdaResult](#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-GetAccessPointPolicyStatusForObjectLambdaResult "#AmazonS3-control_GetAccessPointPolicyStatusForObjectLambda-response-GetAccessPointPolicyStatusForObjectLambdaResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessPointPolicyStatusForObjectLambdaResult](#API_control_GetAccessPointPolicyStatusForObjectLambda_ResponseSyntax "#API_control_GetAccessPointPolicyStatusForObjectLambda_ResponseSyntax")**


Root level tag for the GetAccessPointPolicyStatusForObjectLambdaResult parameters.


Required: Yes




**[PolicyStatus](#API_control_GetAccessPointPolicyStatusForObjectLambda_ResponseSyntax "#API_control_GetAccessPointPolicyStatusForObjectLambda_ResponseSyntax")**


Indicates whether this access point policy is public. For more information about how Amazon S3
 evaluates policies to determine whether they are public, see [The Meaning of "Public"](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status "https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html#access-control-block-public-access-policy-status") in the *Amazon S3 User Guide*. 


Type: [PolicyStatus](API_control_PolicyStatus.md "API_control_PolicyStatus.md") data type




## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessPointPolicyStatusForObjectLambda")

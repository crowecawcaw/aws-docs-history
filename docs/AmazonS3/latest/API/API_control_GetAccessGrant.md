# GetAccessGrant

Get the details of an access grant from your S3 Access Grants instance.



Permissions

You must have the `s3:GetAccessGrant` permission to use this
 operation. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstance/grant/`id` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_GetAccessGrant_RequestSyntax "#API_control_GetAccessGrant_RequestSyntax")**


The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access
 grant.


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessGrant_RequestSyntax "#API_control_GetAccessGrant_RequestSyntax")**


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
<[GetAccessGrantResult](#AmazonS3-control_GetAccessGrant-response-GetAccessGrantResult "#AmazonS3-control_GetAccessGrant-response-GetAccessGrantResult")>
   <[CreatedAt](#AmazonS3-control_GetAccessGrant-response-CreatedAt "#AmazonS3-control_GetAccessGrant-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_GetAccessGrant-response-CreatedAt "#AmazonS3-control_GetAccessGrant-response-CreatedAt")>
   <[AccessGrantId](#AmazonS3-control_GetAccessGrant-response-AccessGrantId "#AmazonS3-control_GetAccessGrant-response-AccessGrantId")>***string***</[AccessGrantId](#AmazonS3-control_GetAccessGrant-response-AccessGrantId "#AmazonS3-control_GetAccessGrant-response-AccessGrantId")>
   <[AccessGrantArn](#AmazonS3-control_GetAccessGrant-response-AccessGrantArn "#AmazonS3-control_GetAccessGrant-response-AccessGrantArn")>***string***</[AccessGrantArn](#AmazonS3-control_GetAccessGrant-response-AccessGrantArn "#AmazonS3-control_GetAccessGrant-response-AccessGrantArn")>
   <[Grantee](#AmazonS3-control_GetAccessGrant-response-Grantee "#AmazonS3-control_GetAccessGrant-response-Grantee")>
      <[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>***string***</[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>
      <[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>***string***</[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>
   </[Grantee](#AmazonS3-control_GetAccessGrant-response-Grantee "#AmazonS3-control_GetAccessGrant-response-Grantee")>
   <[Permission](#AmazonS3-control_GetAccessGrant-response-Permission "#AmazonS3-control_GetAccessGrant-response-Permission")>***string***</[Permission](#AmazonS3-control_GetAccessGrant-response-Permission "#AmazonS3-control_GetAccessGrant-response-Permission")>
   <[AccessGrantsLocationId](#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationId "#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationId")>***string***</[AccessGrantsLocationId](#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationId "#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationId")>
   <[AccessGrantsLocationConfiguration](#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationConfiguration "#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationConfiguration")>
      <[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>***string***</[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>
   </[AccessGrantsLocationConfiguration](#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationConfiguration "#AmazonS3-control_GetAccessGrant-response-AccessGrantsLocationConfiguration")>
   <[GrantScope](#AmazonS3-control_GetAccessGrant-response-GrantScope "#AmazonS3-control_GetAccessGrant-response-GrantScope")>***string***</[GrantScope](#AmazonS3-control_GetAccessGrant-response-GrantScope "#AmazonS3-control_GetAccessGrant-response-GrantScope")>
   <[ApplicationArn](#AmazonS3-control_GetAccessGrant-response-ApplicationArn "#AmazonS3-control_GetAccessGrant-response-ApplicationArn")>***string***</[ApplicationArn](#AmazonS3-control_GetAccessGrant-response-ApplicationArn "#AmazonS3-control_GetAccessGrant-response-ApplicationArn")>
</[GetAccessGrantResult](#AmazonS3-control_GetAccessGrant-response-GetAccessGrantResult "#AmazonS3-control_GetAccessGrant-response-GetAccessGrantResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessGrantResult](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


Root level tag for the GetAccessGrantResult parameters.


Required: Yes




**[AccessGrantArn](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The Amazon Resource Name (ARN) of the access grant. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`





**[AccessGrantId](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access
 grant.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[AccessGrantsLocationConfiguration](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The configuration options of the grant location. The grant location is the S3 path to
 the data to which you are granting access. 


Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md "API_control_AccessGrantsLocationConfiguration.md") data type




**[AccessGrantsLocationId](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[ApplicationArn](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated
 with your Identity Center instance. If the grant includes an application ARN, the grantee
 can only access the S3 data through this application. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`





**[CreatedAt](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The date and time when you created the access grant. 


Type: Timestamp




**[Grantee](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The user, group, or role to which you are granting access. You can grant access to an
 IAM user or role. If you have added a corporate directory to AWS IAM Identity Center
 and associated this Identity Center instance with the S3 Access Grants instance, the grantee can also
 be a corporate directory user or group.


Type: [Grantee](API_control_Grantee.md "API_control_Grantee.md") data type




**[GrantScope](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The S3 path of the data to which you are granting access. It is the result of appending
 the `Subprefix` to the location scope.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`





**[Permission](#API_control_GetAccessGrant_ResponseSyntax "#API_control_GetAccessGrant_ResponseSyntax")**


The type of permission that was granted in the access grant. Can be one of the following
 values:



* `READ` – Grant read-only access to the S3 data.
* `WRITE` – Grant write-only access to the S3 data.
* `READWRITE` – Grant both read and write access to the S3 data.

Type: String


Valid Values: `READ | WRITE | READWRITE`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrant "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrant")

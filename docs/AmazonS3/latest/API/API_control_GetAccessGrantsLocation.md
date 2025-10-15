# GetAccessGrantsLocation

Retrieves the details of a particular location registered in your S3 Access Grants instance. 



Permissions

You must have the `s3:GetAccessGrantsLocation` permission to use
 this operation. 



###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
GET /v20180820/accessgrantsinstance/location/`id` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`

```

## URI Request Parameters


The request uses the following URI parameters.





**[id](#API_control_GetAccessGrantsLocation_RequestSyntax "#API_control_GetAccessGrantsLocation_RequestSyntax")**


The ID of the registered location that you are retrieving. S3 Access Grants assigns this ID when
 you register the location. S3 Access Grants assigns the ID `default` to the default
 location `s3://` and assigns an auto-generated ID to other locations that you
 register. 


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: Yes




**[x-amz-account-id](#API_control_GetAccessGrantsLocation_RequestSyntax "#API_control_GetAccessGrantsLocation_RequestSyntax")**


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
<[GetAccessGrantsLocationResult](#AmazonS3-control_GetAccessGrantsLocation-response-GetAccessGrantsLocationResult "#AmazonS3-control_GetAccessGrantsLocation-response-GetAccessGrantsLocationResult")>
   <[CreatedAt](#AmazonS3-control_GetAccessGrantsLocation-response-CreatedAt "#AmazonS3-control_GetAccessGrantsLocation-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_GetAccessGrantsLocation-response-CreatedAt "#AmazonS3-control_GetAccessGrantsLocation-response-CreatedAt")>
   <[AccessGrantsLocationId](#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationId "#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationId")>***string***</[AccessGrantsLocationId](#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationId "#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationId")>
   <[AccessGrantsLocationArn](#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationArn "#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationArn")>***string***</[AccessGrantsLocationArn](#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationArn "#AmazonS3-control_GetAccessGrantsLocation-response-AccessGrantsLocationArn")>
   <[LocationScope](#AmazonS3-control_GetAccessGrantsLocation-response-LocationScope "#AmazonS3-control_GetAccessGrantsLocation-response-LocationScope")>***string***</[LocationScope](#AmazonS3-control_GetAccessGrantsLocation-response-LocationScope "#AmazonS3-control_GetAccessGrantsLocation-response-LocationScope")>
   <[IAMRoleArn](#AmazonS3-control_GetAccessGrantsLocation-response-IAMRoleArn "#AmazonS3-control_GetAccessGrantsLocation-response-IAMRoleArn")>***string***</[IAMRoleArn](#AmazonS3-control_GetAccessGrantsLocation-response-IAMRoleArn "#AmazonS3-control_GetAccessGrantsLocation-response-IAMRoleArn")>
</[GetAccessGrantsLocationResult](#AmazonS3-control_GetAccessGrantsLocation-response-GetAccessGrantsLocationResult "#AmazonS3-control_GetAccessGrantsLocation-response-GetAccessGrantsLocationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[GetAccessGrantsLocationResult](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


Root level tag for the GetAccessGrantsLocationResult parameters.


Required: Yes




**[AccessGrantsLocationArn](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


The Amazon Resource Name (ARN) of the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`





**[AccessGrantsLocationId](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[CreatedAt](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


The date and time when you registered the location. 


Type: Timestamp




**[IAMRoleArn](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants
 assumes this role to manage access to the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:iam::\d{12}:role/.*`





**[LocationScope](#API_control_GetAccessGrantsLocation_ResponseSyntax "#API_control_GetAccessGrantsLocation_ResponseSyntax")**


The S3 URI path to the registered location. The location scope can be the default S3
 location `s3://`, the S3 path to a bucket, or the S3 path to a bucket and
 prefix. A prefix in S3 is a string of characters at the beginning of an object key name
 used to organize the objects that you store in your S3 buckets. For example, object key
 names that start with the `engineering/` prefix or object key names that start
 with the `marketing/campaigns/` prefix.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/GetAccessGrantsLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/GetAccessGrantsLocation")

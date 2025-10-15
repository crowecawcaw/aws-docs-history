# CreateAccessGrantsLocation

The S3 data location that you would like to register in your S3 Access Grants instance. Your S3
 data must be in the same Region as your S3 Access Grants instance. The location can be one of the
 following: 


* The default S3 location `s3://`
* A bucket - `S3://<bucket-name>`
* A bucket and prefix - `S3://<bucket-name>/<prefix>`
When you register a location, you must include the IAM role that has permission to
 manage the S3 location that you are registering. Give S3 Access Grants permission to assume this role
 [using a policy](../userguide/access-grants-location.md "../userguide/access-grants-location.md"). S3 Access Grants assumes this role to manage access to the location and
 to vend temporary credentials to grantees or client applications. 



Permissions

You must have the `s3:CreateAccessGrantsLocation` permission to use
 this operation. 



Additional Permissions

You must also have the following permission for the specified IAM role:
 `iam:PassRole`




###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/accessgrantsinstance/location HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantsLocationRequest](#AmazonS3-control_CreateAccessGrantsLocation-request-CreateAccessGrantsLocationRequest "#AmazonS3-control_CreateAccessGrantsLocation-request-CreateAccessGrantsLocationRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[LocationScope](#AmazonS3-control_CreateAccessGrantsLocation-request-LocationScope "#AmazonS3-control_CreateAccessGrantsLocation-request-LocationScope")>`string`</[LocationScope](#AmazonS3-control_CreateAccessGrantsLocation-request-LocationScope "#AmazonS3-control_CreateAccessGrantsLocation-request-LocationScope")>
   <[IAMRoleArn](#AmazonS3-control_CreateAccessGrantsLocation-request-IAMRoleArn "#AmazonS3-control_CreateAccessGrantsLocation-request-IAMRoleArn")>`string`</[IAMRoleArn](#AmazonS3-control_CreateAccessGrantsLocation-request-IAMRoleArn "#AmazonS3-control_CreateAccessGrantsLocation-request-IAMRoleArn")>
   <[Tags](#AmazonS3-control_CreateAccessGrantsLocation-request-Tags "#AmazonS3-control_CreateAccessGrantsLocation-request-Tags")>
      <Tag>
         <[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>`string`</[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>
         <[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>`string`</[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_CreateAccessGrantsLocation-request-Tags "#AmazonS3-control_CreateAccessGrantsLocation-request-Tags")>
</[CreateAccessGrantsLocationRequest](#AmazonS3-control_CreateAccessGrantsLocation-request-CreateAccessGrantsLocationRequest "#AmazonS3-control_CreateAccessGrantsLocation-request-CreateAccessGrantsLocationRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_CreateAccessGrantsLocation_RequestSyntax "#API_control_CreateAccessGrantsLocation_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateAccessGrantsLocationRequest](#API_control_CreateAccessGrantsLocation_RequestSyntax "#API_control_CreateAccessGrantsLocation_RequestSyntax")**


Root level tag for the CreateAccessGrantsLocationRequest parameters.


Required: Yes




**[IAMRoleArn](#API_control_CreateAccessGrantsLocation_RequestSyntax "#API_control_CreateAccessGrantsLocation_RequestSyntax")**


The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants
 assumes this role to manage access to the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:iam::\d{12}:role/.*`



Required: Yes




**[LocationScope](#API_control_CreateAccessGrantsLocation_RequestSyntax "#API_control_CreateAccessGrantsLocation_RequestSyntax")**


The S3 path to the location that you are registering. The location scope can be the
 default S3 location `s3://`, the S3 path to a bucket
 `s3://<bucket>`, or the S3 path to a bucket and prefix
 `s3://<bucket>/<prefix>`. A prefix in S3 is a string of
 characters at the beginning of an object key name used to organize the objects that you
 store in your S3 buckets. For example, object key names that start with the
 `engineering/` prefix or object key names that start with the
 `marketing/campaigns/` prefix.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`



Required: Yes




**[Tags](#API_control_CreateAccessGrantsLocation_RequestSyntax "#API_control_CreateAccessGrantsLocation_RequestSyntax")**


The AWS resource tags that you are adding to the S3 Access Grants location. Each tag is a label
 consisting of a user-defined key and value. Tags can help you manage, identify, organize,
 search for, and filter resources.


Type: Array of [Tag](API_control_Tag.md "API_control_Tag.md") data types


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantsLocationResult](#AmazonS3-control_CreateAccessGrantsLocation-response-CreateAccessGrantsLocationResult "#AmazonS3-control_CreateAccessGrantsLocation-response-CreateAccessGrantsLocationResult")>
   <[CreatedAt](#AmazonS3-control_CreateAccessGrantsLocation-response-CreatedAt "#AmazonS3-control_CreateAccessGrantsLocation-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_CreateAccessGrantsLocation-response-CreatedAt "#AmazonS3-control_CreateAccessGrantsLocation-response-CreatedAt")>
   <[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationId")>***string***</[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationId")>
   <[AccessGrantsLocationArn](#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationArn "#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationArn")>***string***</[AccessGrantsLocationArn](#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationArn "#AmazonS3-control_CreateAccessGrantsLocation-response-AccessGrantsLocationArn")>
   <[LocationScope](#AmazonS3-control_CreateAccessGrantsLocation-response-LocationScope "#AmazonS3-control_CreateAccessGrantsLocation-response-LocationScope")>***string***</[LocationScope](#AmazonS3-control_CreateAccessGrantsLocation-response-LocationScope "#AmazonS3-control_CreateAccessGrantsLocation-response-LocationScope")>
   <[IAMRoleArn](#AmazonS3-control_CreateAccessGrantsLocation-response-IAMRoleArn "#AmazonS3-control_CreateAccessGrantsLocation-response-IAMRoleArn")>***string***</[IAMRoleArn](#AmazonS3-control_CreateAccessGrantsLocation-response-IAMRoleArn "#AmazonS3-control_CreateAccessGrantsLocation-response-IAMRoleArn")>
</[CreateAccessGrantsLocationResult](#AmazonS3-control_CreateAccessGrantsLocation-response-CreateAccessGrantsLocationResult "#AmazonS3-control_CreateAccessGrantsLocation-response-CreateAccessGrantsLocationResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateAccessGrantsLocationResult](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


Root level tag for the CreateAccessGrantsLocationResult parameters.


Required: Yes




**[AccessGrantsLocationArn](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


The Amazon Resource Name (ARN) of the location you are registering.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/location/[a-zA-Z0-9\-]+`





**[AccessGrantsLocationId](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[CreatedAt](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


The date and time when you registered the location. 


Type: Timestamp




**[IAMRoleArn](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


The Amazon Resource Name (ARN) of the IAM role for the registered location. S3 Access Grants
 assumes this role to manage access to the registered location. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:iam::\d{12}:role/.*`





**[LocationScope](#API_control_CreateAccessGrantsLocation_ResponseSyntax "#API_control_CreateAccessGrantsLocation_ResponseSyntax")**


The S3 URI path to the location that you are registering. The location scope can be the
 default S3 location `s3://`, the S3 path to a bucket, or the S3 path to a bucket
 and prefix. A prefix in S3 is a string of characters at the beginning of an object key name
 used to organize the objects that you store in your S3 buckets. For example, object key
 names that start with the `engineering/` prefix or object key names that start
 with the `marketing/campaigns/` prefix.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrantsLocation")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrantsLocation "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrantsLocation")

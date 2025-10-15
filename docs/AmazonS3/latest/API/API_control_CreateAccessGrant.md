# CreateAccessGrant

Creates an access grant that gives a grantee access to your S3 data. The grantee can be
 an IAM user or role or a directory user, or group. Before you can create a grant, you
 must have an S3 Access Grants instance in the same Region as the S3 data. You can create an S3 Access Grants
 instance using the [CreateAccessGrantsInstance](API_control_CreateAccessGrantsInstance.md "API_control_CreateAccessGrantsInstance.md"). You must also have registered at least one S3 data
 location in your S3 Access Grants instance using [CreateAccessGrantsLocation](API_control_CreateAccessGrantsLocation.md "API_control_CreateAccessGrantsLocation.md"). 



Permissions

You must have the `s3:CreateAccessGrant` permission to use this
 operation. 



Additional Permissions

For any directory identity - `sso:DescribeInstance` and
 `sso:DescribeApplication`



For directory users - `identitystore:DescribeUser`



For directory groups - `identitystore:DescribeGroup`




###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
POST /v20180820/accessgrantsinstance/grant HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantRequest](#AmazonS3-control_CreateAccessGrant-request-CreateAccessGrantRequest "#AmazonS3-control_CreateAccessGrant-request-CreateAccessGrantRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationId")>`string`</[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationId")>
   <[AccessGrantsLocationConfiguration](#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationConfiguration "#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationConfiguration")>
      <[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>`string`</[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>
   </[AccessGrantsLocationConfiguration](#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationConfiguration "#AmazonS3-control_CreateAccessGrant-request-AccessGrantsLocationConfiguration")>
   <[Grantee](#AmazonS3-control_CreateAccessGrant-request-Grantee "#AmazonS3-control_CreateAccessGrant-request-Grantee")>
      <[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>`string`</[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>
      <[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>`string`</[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>
   </[Grantee](#AmazonS3-control_CreateAccessGrant-request-Grantee "#AmazonS3-control_CreateAccessGrant-request-Grantee")>
   <[Permission](#AmazonS3-control_CreateAccessGrant-request-Permission "#AmazonS3-control_CreateAccessGrant-request-Permission")>`string`</[Permission](#AmazonS3-control_CreateAccessGrant-request-Permission "#AmazonS3-control_CreateAccessGrant-request-Permission")>
   <[ApplicationArn](#AmazonS3-control_CreateAccessGrant-request-ApplicationArn "#AmazonS3-control_CreateAccessGrant-request-ApplicationArn")>`string`</[ApplicationArn](#AmazonS3-control_CreateAccessGrant-request-ApplicationArn "#AmazonS3-control_CreateAccessGrant-request-ApplicationArn")>
   <[S3PrefixType](#AmazonS3-control_CreateAccessGrant-request-S3PrefixType "#AmazonS3-control_CreateAccessGrant-request-S3PrefixType")>`string`</[S3PrefixType](#AmazonS3-control_CreateAccessGrant-request-S3PrefixType "#AmazonS3-control_CreateAccessGrant-request-S3PrefixType")>
   <[Tags](#AmazonS3-control_CreateAccessGrant-request-Tags "#AmazonS3-control_CreateAccessGrant-request-Tags")>
      <Tag>
         <[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>`string`</[Key](API_control_Tag.md#AmazonS3-Type-control_Tag-Key "API_control_Tag.md#AmazonS3-Type-control_Tag-Key")>
         <[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>`string`</[Value](API_control_Tag.md#AmazonS3-Type-control_Tag-Value "API_control_Tag.md#AmazonS3-Type-control_Tag-Value")>
      </Tag>
   </[Tags](#AmazonS3-control_CreateAccessGrant-request-Tags "#AmazonS3-control_CreateAccessGrant-request-Tags")>
</[CreateAccessGrantRequest](#AmazonS3-control_CreateAccessGrant-request-CreateAccessGrantRequest "#AmazonS3-control_CreateAccessGrant-request-CreateAccessGrantRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[x-amz-account-id](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The AWS account ID of the S3 Access Grants instance.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateAccessGrantRequest](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


Root level tag for the CreateAccessGrantRequest parameters.


Required: Yes




**[AccessGrantsLocationConfiguration](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The configuration options of the grant location. The grant location is the S3 path to
 the data to which you are granting access. It contains the `S3SubPrefix` field.
 The grant scope is the result of appending the subprefix to the location scope of the
 registered location.


Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md "API_control_AccessGrantsLocationConfiguration.md") data type


Required: No




**[AccessGrantsLocationId](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


If you are passing the `default` location, you cannot create an access grant
 for the entire default location. You must also specify a bucket or a bucket and prefix in
 the `Subprefix` field. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`



Required: Yes




**[ApplicationArn](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated
 with your Identity Center instance. If an application ARN is included in the request to
 create an access grant, the grantee can only access the S3 data through this application.
 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`



Required: No




**[Grantee](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The user, group, or role to which you are granting access. You can grant access to an
 IAM user or role. If you have added your corporate directory to AWS IAM Identity
 Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee
 can also be a corporate directory user or group.


Type: [Grantee](API_control_Grantee.md "API_control_Grantee.md") data type


Required: Yes




**[Permission](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The type of access that you are granting to your S3 data, which can be set to one of the
 following values:



* `READ` – Grant read-only access to the S3 data.
* `WRITE` – Grant write-only access to the S3 data.
* `READWRITE` – Grant both read and write access to the S3 data.

Type: String


Valid Values: `READ | WRITE | READWRITE`



Required: Yes




**[S3PrefixType](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The type of `S3SubPrefix`. The only possible value is `Object`.
 Pass this value if the access grant scope is an object. Do not pass this value if the
 access grant scope is a bucket or a bucket and a prefix. 


Type: String


Valid Values: `Object`



Required: No




**[Tags](#API_control_CreateAccessGrant_RequestSyntax "#API_control_CreateAccessGrant_RequestSyntax")**


The AWS resource tags that you are adding to the access grant. Each tag is a label
 consisting of a user-defined key and value. Tags can help you manage, identify, organize,
 search for, and filter resources. 


Type: Array of [Tag](API_control_Tag.md "API_control_Tag.md") data types


Array Members: Minimum number of 0 items. Maximum number of 50 items.


Required: No




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessGrantResult](#AmazonS3-control_CreateAccessGrant-response-CreateAccessGrantResult "#AmazonS3-control_CreateAccessGrant-response-CreateAccessGrantResult")>
   <[CreatedAt](#AmazonS3-control_CreateAccessGrant-response-CreatedAt "#AmazonS3-control_CreateAccessGrant-response-CreatedAt")>***timestamp***</[CreatedAt](#AmazonS3-control_CreateAccessGrant-response-CreatedAt "#AmazonS3-control_CreateAccessGrant-response-CreatedAt")>
   <[AccessGrantId](#AmazonS3-control_CreateAccessGrant-response-AccessGrantId "#AmazonS3-control_CreateAccessGrant-response-AccessGrantId")>***string***</[AccessGrantId](#AmazonS3-control_CreateAccessGrant-response-AccessGrantId "#AmazonS3-control_CreateAccessGrant-response-AccessGrantId")>
   <[AccessGrantArn](#AmazonS3-control_CreateAccessGrant-response-AccessGrantArn "#AmazonS3-control_CreateAccessGrant-response-AccessGrantArn")>***string***</[AccessGrantArn](#AmazonS3-control_CreateAccessGrant-response-AccessGrantArn "#AmazonS3-control_CreateAccessGrant-response-AccessGrantArn")>
   <[Grantee](#AmazonS3-control_CreateAccessGrant-response-Grantee "#AmazonS3-control_CreateAccessGrant-response-Grantee")>
      <[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>***string***</[GranteeIdentifier](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeIdentifier")>
      <[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>***string***</[GranteeType](API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType "API_control_Grantee.md#AmazonS3-Type-control_Grantee-GranteeType")>
   </[Grantee](#AmazonS3-control_CreateAccessGrant-response-Grantee "#AmazonS3-control_CreateAccessGrant-response-Grantee")>
   <[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationId")>***string***</[AccessGrantsLocationId](#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationId "#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationId")>
   <[AccessGrantsLocationConfiguration](#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationConfiguration "#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationConfiguration")>
      <[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>***string***</[S3SubPrefix](API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix "API_control_AccessGrantsLocationConfiguration.md#AmazonS3-Type-control_AccessGrantsLocationConfiguration-S3SubPrefix")>
   </[AccessGrantsLocationConfiguration](#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationConfiguration "#AmazonS3-control_CreateAccessGrant-response-AccessGrantsLocationConfiguration")>
   <[Permission](#AmazonS3-control_CreateAccessGrant-response-Permission "#AmazonS3-control_CreateAccessGrant-response-Permission")>***string***</[Permission](#AmazonS3-control_CreateAccessGrant-response-Permission "#AmazonS3-control_CreateAccessGrant-response-Permission")>
   <[ApplicationArn](#AmazonS3-control_CreateAccessGrant-response-ApplicationArn "#AmazonS3-control_CreateAccessGrant-response-ApplicationArn")>***string***</[ApplicationArn](#AmazonS3-control_CreateAccessGrant-response-ApplicationArn "#AmazonS3-control_CreateAccessGrant-response-ApplicationArn")>
   <[GrantScope](#AmazonS3-control_CreateAccessGrant-response-GrantScope "#AmazonS3-control_CreateAccessGrant-response-GrantScope")>***string***</[GrantScope](#AmazonS3-control_CreateAccessGrant-response-GrantScope "#AmazonS3-control_CreateAccessGrant-response-GrantScope")>
</[CreateAccessGrantResult](#AmazonS3-control_CreateAccessGrant-response-CreateAccessGrantResult "#AmazonS3-control_CreateAccessGrant-response-CreateAccessGrantResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateAccessGrantResult](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


Root level tag for the CreateAccessGrantResult parameters.


Required: Yes




**[AccessGrantArn](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The Amazon Resource Name (ARN) of the access grant. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[a-z\-]+:s3:[a-z0-9\-]+:\d{12}:access\-grants\/grant/[a-zA-Z0-9\-]+`





**[AccessGrantId](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The ID of the access grant. S3 Access Grants auto-generates this ID when you create the access
 grant.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[AccessGrantsLocationConfiguration](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The configuration options of the grant location. The grant location is the S3 path to
 the data to which you are granting access. 


Type: [AccessGrantsLocationConfiguration](API_control_AccessGrantsLocationConfiguration.md "API_control_AccessGrantsLocationConfiguration.md") data type




**[AccessGrantsLocationId](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The ID of the registered location to which you are granting access. S3 Access Grants assigns this
 ID when you register the location. S3 Access Grants assigns the ID `default` to the
 default location `s3://` and assigns an auto-generated ID to other locations
 that you register. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 64.


Pattern: `[a-zA-Z0-9\-]+`





**[ApplicationArn](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The Amazon Resource Name (ARN) of an AWS IAM Identity Center application associated
 with your Identity Center instance. If the grant includes an application ARN, the grantee
 can only access the S3 data through this application. 


Type: String


Length Constraints: Minimum length of 10. Maximum length of 1224.


Pattern: `arn:[^:]+:sso::\d{12}:application/.*$`





**[CreatedAt](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The date and time when you created the access grant. 


Type: Timestamp




**[Grantee](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The user, group, or role to which you are granting access. You can grant access to an
 IAM user or role. If you have added your corporate directory to AWS IAM Identity
 Center and associated your Identity Center instance with your S3 Access Grants instance, the grantee
 can also be a corporate directory user or group.


Type: [Grantee](API_control_Grantee.md "API_control_Grantee.md") data type




**[GrantScope](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The S3 path of the data to which you are granting access. It is the result of appending
 the `Subprefix` to the location scope. 


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2000.


Pattern: `^.+$`





**[Permission](#API_control_CreateAccessGrant_ResponseSyntax "#API_control_CreateAccessGrant_ResponseSyntax")**


The type of access that you are granting to your S3 data, which can be set to one of the
 following values:



* `READ` – Grant read-only access to the S3 data.
* `WRITE` – Grant write-only access to the S3 data.
* `READWRITE` – Grant both read and write access to the S3 data.

Type: String


Valid Values: `READ | WRITE | READWRITE`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessGrant")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrant "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessGrant")

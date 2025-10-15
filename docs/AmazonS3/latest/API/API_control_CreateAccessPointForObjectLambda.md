# CreateAccessPointForObjectLambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

###### Note

This operation is not supported by directory buckets.

Creates an Object Lambda Access Point. For more information, see [Transforming objects with
 Object Lambda Access Points](../userguide/transforming-objects.md "../userguide/transforming-objects.md") in the *Amazon S3 User Guide*.

The following actions are related to
 `CreateAccessPointForObjectLambda`:


* [DeleteAccessPointForObjectLambda](API_control_DeleteAccessPointForObjectLambda.md "API_control_DeleteAccessPointForObjectLambda.md")
* [GetAccessPointForObjectLambda](API_control_GetAccessPointForObjectLambda.md "API_control_GetAccessPointForObjectLambda.md")
* [ListAccessPointsForObjectLambda](API_control_ListAccessPointsForObjectLambda.md "API_control_ListAccessPointsForObjectLambda.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/accesspointforobjectlambda/`name` HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessPointForObjectLambdaRequest](#AmazonS3-control_CreateAccessPointForObjectLambda-request-CreateAccessPointForObjectLambdaRequest "#AmazonS3-control_CreateAccessPointForObjectLambda-request-CreateAccessPointForObjectLambdaRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Configuration](#AmazonS3-control_CreateAccessPointForObjectLambda-request-Configuration "#AmazonS3-control_CreateAccessPointForObjectLambda-request-Configuration")>
      <[AllowedFeatures](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-AllowedFeatures "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-AllowedFeatures")>
         <AllowedFeature>`string`</AllowedFeature>
      </[AllowedFeatures](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-AllowedFeatures "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-AllowedFeatures")>
      <[CloudWatchMetricsEnabled](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-CloudWatchMetricsEnabled "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-CloudWatchMetricsEnabled")>`boolean`</[CloudWatchMetricsEnabled](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-CloudWatchMetricsEnabled "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-CloudWatchMetricsEnabled")>
      <[SupportingAccessPoint](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-SupportingAccessPoint "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-SupportingAccessPoint")>`string`</[SupportingAccessPoint](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-SupportingAccessPoint "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-SupportingAccessPoint")>
      <[TransformationConfigurations](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-TransformationConfigurations "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-TransformationConfigurations")>
         <TransformationConfiguration>
            <[Actions](API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-Actions "API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-Actions")>
               <Action>`string`</Action>
            </[Actions](API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-Actions "API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-Actions")>
            <[ContentTransformation](API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-ContentTransformation "API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-ContentTransformation")>
               <[AwsLambda](API_control_ObjectLambdaContentTransformation.md#AmazonS3-Type-control_ObjectLambdaContentTransformation-AwsLambda "API_control_ObjectLambdaContentTransformation.md#AmazonS3-Type-control_ObjectLambdaContentTransformation-AwsLambda")>
                  <[FunctionArn](API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionArn "API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionArn")>`string`</[FunctionArn](API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionArn "API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionArn")>
                  <[FunctionPayload](API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionPayload "API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionPayload")>`string`</[FunctionPayload](API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionPayload "API_control_AwsLambdaTransformation.md#AmazonS3-Type-control_AwsLambdaTransformation-FunctionPayload")>
               </[AwsLambda](API_control_ObjectLambdaContentTransformation.md#AmazonS3-Type-control_ObjectLambdaContentTransformation-AwsLambda "API_control_ObjectLambdaContentTransformation.md#AmazonS3-Type-control_ObjectLambdaContentTransformation-AwsLambda")>
            </[ContentTransformation](API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-ContentTransformation "API_control_ObjectLambdaTransformationConfiguration.md#AmazonS3-Type-control_ObjectLambdaTransformationConfiguration-ContentTransformation")>
         </TransformationConfiguration>
      </[TransformationConfigurations](API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-TransformationConfigurations "API_control_ObjectLambdaConfiguration.md#AmazonS3-Type-control_ObjectLambdaConfiguration-TransformationConfigurations")>
   </[Configuration](#AmazonS3-control_CreateAccessPointForObjectLambda-request-Configuration "#AmazonS3-control_CreateAccessPointForObjectLambda-request-Configuration")>
</[CreateAccessPointForObjectLambdaRequest](#AmazonS3-control_CreateAccessPointForObjectLambda-request-CreateAccessPointForObjectLambdaRequest "#AmazonS3-control_CreateAccessPointForObjectLambda-request-CreateAccessPointForObjectLambdaRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_CreateAccessPointForObjectLambda_RequestSyntax "#API_control_CreateAccessPointForObjectLambda_RequestSyntax")**


The name you want to assign to this Object Lambda Access Point.


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`



Required: Yes




**[x-amz-account-id](#API_control_CreateAccessPointForObjectLambda_RequestSyntax "#API_control_CreateAccessPointForObjectLambda_RequestSyntax")**


The AWS account ID for owner of the specified Object Lambda Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[CreateAccessPointForObjectLambdaRequest](#API_control_CreateAccessPointForObjectLambda_RequestSyntax "#API_control_CreateAccessPointForObjectLambda_RequestSyntax")**


Root level tag for the CreateAccessPointForObjectLambdaRequest parameters.


Required: Yes




**[Configuration](#API_control_CreateAccessPointForObjectLambda_RequestSyntax "#API_control_CreateAccessPointForObjectLambda_RequestSyntax")**


Object Lambda Access Point configuration as a JSON document.


Type: [ObjectLambdaConfiguration](API_control_ObjectLambdaConfiguration.md "API_control_ObjectLambdaConfiguration.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200
<?xml version="1.0" encoding="UTF-8"?>
<[CreateAccessPointForObjectLambdaResult](#AmazonS3-control_CreateAccessPointForObjectLambda-response-CreateAccessPointForObjectLambdaResult "#AmazonS3-control_CreateAccessPointForObjectLambda-response-CreateAccessPointForObjectLambdaResult")>
   <[ObjectLambdaAccessPointArn](#AmazonS3-control_CreateAccessPointForObjectLambda-response-ObjectLambdaAccessPointArn "#AmazonS3-control_CreateAccessPointForObjectLambda-response-ObjectLambdaAccessPointArn")>***string***</[ObjectLambdaAccessPointArn](#AmazonS3-control_CreateAccessPointForObjectLambda-response-ObjectLambdaAccessPointArn "#AmazonS3-control_CreateAccessPointForObjectLambda-response-ObjectLambdaAccessPointArn")>
   <[Alias](#AmazonS3-control_CreateAccessPointForObjectLambda-response-Alias "#AmazonS3-control_CreateAccessPointForObjectLambda-response-Alias")>
      <[Status](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status")>***string***</[Status](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Status")>
      <[Value](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value")>***string***</[Value](API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value "API_control_ObjectLambdaAccessPointAlias.md#AmazonS3-Type-control_ObjectLambdaAccessPointAlias-Value")>
   </[Alias](#AmazonS3-control_CreateAccessPointForObjectLambda-response-Alias "#AmazonS3-control_CreateAccessPointForObjectLambda-response-Alias")>
</[CreateAccessPointForObjectLambdaResult](#AmazonS3-control_CreateAccessPointForObjectLambda-response-CreateAccessPointForObjectLambdaResult "#AmazonS3-control_CreateAccessPointForObjectLambda-response-CreateAccessPointForObjectLambdaResult")>
```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response.


The following data is returned in XML format by the service.





**[CreateAccessPointForObjectLambdaResult](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax "#API_control_CreateAccessPointForObjectLambda_ResponseSyntax")**


Root level tag for the CreateAccessPointForObjectLambdaResult parameters.


Required: Yes




**[Alias](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax "#API_control_CreateAccessPointForObjectLambda_ResponseSyntax")**


The alias of the Object Lambda Access Point.


Type: [ObjectLambdaAccessPointAlias](API_control_ObjectLambdaAccessPointAlias.md "API_control_ObjectLambdaAccessPointAlias.md") data type




**[ObjectLambdaAccessPointArn](#API_control_CreateAccessPointForObjectLambda_ResponseSyntax "#API_control_CreateAccessPointForObjectLambda_ResponseSyntax")**


Specifies the ARN for the Object Lambda Access Point.


Type: String


Length Constraints: Minimum length of 1. Maximum length of 2048.


Pattern: `arn:[^:]+:s3-object-lambda:[^:]*:\d{12}:accesspoint/.*`





## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/CreateAccessPointForObjectLambda")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPointForObjectLambda "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/CreateAccessPointForObjectLambda")

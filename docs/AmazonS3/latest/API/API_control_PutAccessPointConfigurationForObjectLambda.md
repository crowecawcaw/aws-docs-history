# PutAccessPointConfigurationForObjectLambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on 11/7/2025. If you would like to use the service, please sign up prior to 11/7/2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](../userguide/amazons3-ol-change.md "../userguide/amazons3-ol-change.md").

###### Note

This operation is not supported by directory buckets.

Replaces configuration for an Object Lambda Access Point.

The following actions are related to
 `PutAccessPointConfigurationForObjectLambda`:


* [GetAccessPointConfigurationForObjectLambda](API_control_GetAccessPointConfigurationForObjectLambda.md "API_control_GetAccessPointConfigurationForObjectLambda.md")
###### Important

You must URL encode any signed header values that contain spaces. For example, if your header value is `my file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.


## Request Syntax



```
PUT /v20180820/accesspointforobjectlambda/`name`/configuration HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: `AccountId`
<?xml version="1.0" encoding="UTF-8"?>
<[PutAccessPointConfigurationForObjectLambdaRequest](#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-PutAccessPointConfigurationForObjectLambdaRequest "#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-PutAccessPointConfigurationForObjectLambdaRequest") xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <[Configuration](#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-Configuration "#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-Configuration")>
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
   </[Configuration](#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-Configuration "#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-Configuration")>
</[PutAccessPointConfigurationForObjectLambdaRequest](#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-PutAccessPointConfigurationForObjectLambdaRequest "#AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-PutAccessPointConfigurationForObjectLambdaRequest")>
```

## URI Request Parameters


The request uses the following URI parameters.





**[name](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax "#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax")**


The name of the Object Lambda Access Point.


Length Constraints: Minimum length of 3. Maximum length of 45.


Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`



Required: Yes




**[x-amz-account-id](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax "#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax")**


The account ID for the account that owns the specified Object Lambda Access Point.


Length Constraints: Maximum length of 64.


Pattern: `^\d{12}$`



Required: Yes




## Request Body


The request accepts the following data in XML format.





**[PutAccessPointConfigurationForObjectLambdaRequest](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax "#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax")**


Root level tag for the PutAccessPointConfigurationForObjectLambdaRequest parameters.


Required: Yes




**[Configuration](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax "#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax")**


Object Lambda Access Point configuration document.


Type: [ObjectLambdaConfiguration](API_control_ObjectLambdaConfiguration.md "API_control_ObjectLambdaConfiguration.md") data type


Required: Yes




## Response Syntax



```
HTTP/1.1 200

```

## Response Elements


If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.


## See Also


For more information about using this API in one of the language-specific AWS SDKs, see the following:



* [AWS Command Line Interface](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for .NET](https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/DotNetSDKV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for C++](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")
* [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda "https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda")

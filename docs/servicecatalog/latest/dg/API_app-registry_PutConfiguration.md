# PutConfiguration

Associates a `TagKey` configuration
to an account.

## Request Syntax

```
PUT /configuration HTTP/1.1
Content-type: application/json

{
   "configuration": {
      "tagQueryConfiguration": {
         "tagKey": "`string`"
      }
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[configuration](#API_app-registry_PutConfiguration_RequestSyntax "#API_app-registry_PutConfiguration_RequestSyntax")**

Associates a `TagKey` configuration
to an account.

Type: [AppRegistryConfiguration](API_app-registry_AppRegistryConfiguration.md "API_app-registry_AppRegistryConfiguration.md") object

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ConflictException**

There was a conflict when processing the request (for example, a resource with the given
name already exists within the account).

HTTP Status Code: 409

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

**ValidationException**

The request has invalid or missing parameters.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/PutConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/PutConfiguration.md")

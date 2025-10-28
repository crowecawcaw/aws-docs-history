# GetConfiguration

Retrieves a `TagKey` configuration
from an account.

## Request Syntax

```
GET /configuration HTTP/1.1

```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "configuration": {
      "tagQueryConfiguration": {
         "tagKey": "***string***"
      }
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[configuration](#API_app-registry_GetConfiguration_ResponseSyntax "#API_app-registry_GetConfiguration_ResponseSyntax")**

Retrieves `TagKey` configuration
from an account.

Type: [AppRegistryConfiguration](API_app-registry_AppRegistryConfiguration.md "API_app-registry_AppRegistryConfiguration.md") object

## Errors

**InternalServerException**

The service is experiencing internal problems.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/cli2/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/DotNetSDKV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForCpp/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForGoV2/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForJavaV2/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForJavaScriptV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForKotlin/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForPHPV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/boto3/AWS242AppRegistry-2020-06-24/GetConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md "../../../goto/SdkForRubyV3/AWS242AppRegistry-2020-06-24/GetConfiguration.md")

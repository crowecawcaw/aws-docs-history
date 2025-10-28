# UpdateTrust

Updates the trust that has been set up between your AWS Managed Microsoft AD directory and an
self-managed Active Directory.

## Request Syntax

```
{
   "SelectiveAuth": "`string`",
   "TrustId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[SelectiveAuth](#API_UpdateTrust_RequestSyntax "#API_UpdateTrust_RequestSyntax")**

Updates selective authentication for the trust.

Type: String

Valid Values: `Enabled | Disabled`

Required: No

**[TrustId](#API_UpdateTrust_RequestSyntax "#API_UpdateTrust_RequestSyntax")**

Identifier of the trust relationship.

Type: String

Pattern: `^t-[0-9a-f]{10}$`

Required: Yes

## Response Syntax

```
{
   "RequestId": "***string***",
   "TrustId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RequestId](#API_UpdateTrust_ResponseSyntax "#API_UpdateTrust_ResponseSyntax")**

The AWS request identifier.

Type: String

Pattern: `^([A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12})$`

**[TrustId](#API_UpdateTrust_ResponseSyntax "#API_UpdateTrust_ResponseSyntax")**

Identifier of the trust relationship.

Type: String

Pattern: `^t-[0-9a-f]{10}$`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateTrust.md "../../../goto/cli2/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateTrust.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateTrust.md "../../../goto/boto3/ds-2015-04-16/UpdateTrust.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateTrust.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateTrust.md")

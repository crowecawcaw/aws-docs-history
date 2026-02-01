# UpdateNumberOfDomainControllers

Adds or removes domain controllers to or from the directory. Based on the difference
between current value and new value (provided through this API call), domain controllers will
be added or removed. It may take up to 45 minutes for any new domain controllers to become
fully active once the requested number of domain controllers is updated. During this time, you
cannot make another update request.

## Request Syntax

```
{
   "DesiredNumber": `number`,
   "DirectoryId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DesiredNumber](#API_UpdateNumberOfDomainControllers_RequestSyntax "#API_UpdateNumberOfDomainControllers_RequestSyntax")**

The number of domain controllers desired in the directory.

Type: Integer

Valid Range: Minimum value of 2.

Required: Yes

**[DirectoryId](#API_UpdateNumberOfDomainControllers_RequestSyntax "#API_UpdateNumberOfDomainControllers_RequestSyntax")**

Identifier of the directory to which the domain controllers will be added or
removed.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryUnavailableException**

The specified directory is unavailable.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DomainControllerLimitExceededException**

The maximum allowed number of domain controllers per directory was exceeded. The
default limit per directory is 20 domain controllers.

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

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/cli2/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/DotNetSDKV4/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/boto3/ds-2015-04-16/UpdateNumberOfDomainControllers.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateNumberOfDomainControllers.md")

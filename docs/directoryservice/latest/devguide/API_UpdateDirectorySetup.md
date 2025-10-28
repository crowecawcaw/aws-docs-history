# UpdateDirectorySetup

Updates directory configuration for the specified update type.

## Request Syntax

```
{
   "CreateSnapshotBeforeUpdate": `boolean`,
   "DirectoryId": "`string`",
   "DirectorySizeUpdateSettings": {
      "DirectorySize": "`string`"
   },
   "NetworkUpdateSettings": {
      "CustomerDnsIpsV6": [ "`string`" ],
      "NetworkType": "`string`"
   },
   "OSUpdateSettings": {
      "OSVersion": "`string`"
   },
   "UpdateType": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[CreateSnapshotBeforeUpdate](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

Specifies whether to create a directory snapshot before performing the update.

Type: Boolean

Required: No

**[DirectoryId](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

The identifier of the directory to update.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: Yes

**[DirectorySizeUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

Directory size configuration to apply during the update operation.

Type: [DirectorySizeUpdateSettings](API_DirectorySizeUpdateSettings.md "API_DirectorySizeUpdateSettings.md") object

Required: No

**[NetworkUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

Network configuration to apply during the directory update operation.

Type: [NetworkUpdateSettings](API_NetworkUpdateSettings.md "API_NetworkUpdateSettings.md") object

Required: No

**[OSUpdateSettings](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

Operating system configuration to apply during the directory update operation.

Type: [OSUpdateSettings](API_OSUpdateSettings.md "API_OSUpdateSettings.md") object

Required: No

**[UpdateType](#API_UpdateDirectorySetup_RequestSyntax "#API_UpdateDirectorySetup_RequestSyntax")**

The type of update to perform on the directory.

Type: String

Valid Values: `OS | NETWORK | SIZE`

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

You do not have sufficient access to perform this action.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryInDesiredStateException**

The directory is already updated to desired update type settings.

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

**SnapshotLimitExceededException**

The maximum number of manual snapshots for the directory has been reached. You can
use the [GetSnapshotLimits](API_GetSnapshotLimits.md "API_GetSnapshotLimits.md") operation to determine the snapshot limits
for a directory.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/cli2/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/DotNetSDKV3/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForCpp/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForGoV2/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForJavaV2/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForKotlin/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForPHPV3/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/boto3/ds-2015-04-16/UpdateDirectorySetup.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateDirectorySetup.md "../../../goto/SdkForRubyV3/ds-2015-04-16/UpdateDirectorySetup.md")

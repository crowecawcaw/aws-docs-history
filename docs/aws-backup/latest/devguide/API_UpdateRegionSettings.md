# UpdateRegionSettings

Updates the current service opt-in settings for the Region.

Use
the `DescribeRegionSettings` API to determine the resource types that are
supported.

## Request Syntax

```
PUT /account-settings HTTP/1.1
Content-type: application/json

{
   "ResourceTypeManagementPreference": {
      "`string`" : `boolean`
   },
   "ResourceTypeOptInPreference": {
      "`string`" : `boolean`
   }
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[ResourceTypeManagementPreference](#API_UpdateRegionSettings_RequestSyntax "#API_UpdateRegionSettings_RequestSyntax")**

Enables or disables full AWS Backup management of backups for a resource type.
To enable full AWS Backup management for DynamoDB along with [AWS Backup's advanced DynamoDB backup features](advanced-ddb-backup.md "advanced-ddb-backup.md"), follow the
procedure to [enable advanced DynamoDB backup programmatically](advanced-ddb-backup.md#advanced-ddb-backup-enable-cli "advanced-ddb-backup.md#advanced-ddb-backup-enable-cli").

Type: String to boolean map

Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

**[ResourceTypeOptInPreference](#API_UpdateRegionSettings_RequestSyntax "#API_UpdateRegionSettings_RequestSyntax")**

Updates the list of services along with the opt-in preferences for the Region.

If resource assignments are only based on tags, then service opt-in settings are applied.
If a resource type is explicitly assigned to a backup plan, such as Amazon S3,
Amazon EC2, or Amazon RDS, it will be included in the
backup even if the opt-in is not enabled for that particular service.
If both a resource type and tags are specified in a resource assignment,
the resource type specified in the backup plan takes priority over the
tag condition. Service opt-in settings are disregarded in this situation.

Type: String to boolean map

Key Pattern: `^[a-zA-Z0-9\-\_\.]{1,50}$`

Required: No

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**MissingParameterValueException**

Indicates that a required parameter is missing.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/cli2/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/DotNetSDKV4/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForCpp/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForGoV2/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForJavaV2/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForKotlin/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForPHPV3/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/boto3/backup-2018-11-15/UpdateRegionSettings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRegionSettings.md "../../../goto/SdkForRubyV3/backup-2018-11-15/UpdateRegionSettings.md")

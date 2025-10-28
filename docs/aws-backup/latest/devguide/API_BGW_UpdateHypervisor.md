# UpdateHypervisor

Updates a hypervisor metadata, including its host, username, and password. Specify which
hypervisor to update using the Amazon Resource Name (ARN) of the hypervisor in your
request.

## Request Syntax

```
{
   "Host": "`string`",
   "HypervisorArn": "`string`",
   "LogGroupArn": "`string`",
   "Name": "`string`",
   "Password": "`string`",
   "Username": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Host](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The updated host of the hypervisor. This can be either an IP address or a fully-qualified
domain name (FQDN).

Type: String

Length Constraints: Minimum length of 3. Maximum length of 128.

Pattern: `.+`

Required: No

**[HypervisorArn](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The Amazon Resource Name (ARN) of the hypervisor to update.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: Yes

**[LogGroupArn](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The Amazon Resource Name (ARN) of the group of gateways within the requested log.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `$|^arn:(aws|aws-cn|aws-us-gov):logs:([a-zA-Z0-9-]+):([0-9]+):log-group:[a-zA-Z0-9_\-\/\.]+:\*`

Required: No

**[Name](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The updated name for the hypervisor

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**[Password](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The updated password for the hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[ -~]+`

Required: No

**[Username](#API_BGW_UpdateHypervisor_RequestSyntax "#API_BGW_UpdateHypervisor_RequestSyntax")**

The updated username for the hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[ -\.0-\[\]-~]*[!-\.0-\[\]-~][ -\.0-\[\]-~]*`

Required: No

## Response Syntax

```
{
   "HypervisorArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[HypervisorArn](#API_BGW_UpdateHypervisor_ResponseSyntax "#API_BGW_UpdateHypervisor_ResponseSyntax")**

The Amazon Resource Name (ARN) of the hypervisor you updated.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**AccessDeniedException**

The operation cannot proceed because you have insufficient permissions.

**ErrorCode**

A description of why you have insufficient permissions.

HTTP Status Code: 400

**ConflictException**

The operation cannot proceed because it is not supported.

**ErrorCode**

A description of why the operation is not supported.

HTTP Status Code: 400

**InternalServerException**

The operation did not succeed because an internal error occurred. Try again later.

**ErrorCode**

A description of which internal error occured.

HTTP Status Code: 500

**ResourceNotFoundException**

A resource that is required for the action wasn't found.

**ErrorCode**

A description of which resource wasn't found.

HTTP Status Code: 400

**ThrottlingException**

TPS has been limited to protect against intentional or unintentional
high request volumes.

**ErrorCode**

Error: TPS has been limited to protect against intentional or unintentional
high request volumes.

HTTP Status Code: 400

**ValidationException**

The operation did not succeed because a validation error occurred.

**ErrorCode**

A description of what caused the validation error.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/cli2/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForGoV2/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForKotlin/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for Python](../../../goto/boto3/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/boto3/backup-gateway-2021-01-01/UpdateHypervisor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/UpdateHypervisor.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/UpdateHypervisor.md")

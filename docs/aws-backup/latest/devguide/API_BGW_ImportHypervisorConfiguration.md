# ImportHypervisorConfiguration

Connect to a hypervisor by importing its configuration.

## Request Syntax

```
{
   "Host": "`string`",
   "KmsKeyArn": "`string`",
   "Name": "`string`",
   "Password": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "Username": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[Host](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The server host of the hypervisor. This can be either an IP address or a fully-qualified
domain name (FQDN).

Type: String

Length Constraints: Minimum length of 3. Maximum length of 128.

Pattern: `.+`

Required: Yes

**[KmsKeyArn](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The AWS Key Management Service for the hypervisor.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`

Required: No

**[Name](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The name of the hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: Yes

**[Password](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The password for the hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[ -~]+`

Required: No

**[Tags](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The tags of the hypervisor configuration to import.

Type: Array of [Tag](API_BGW_Tag.md "API_BGW_Tag.md") objects

Required: No

**[Username](#API_BGW_ImportHypervisorConfiguration_RequestSyntax "#API_BGW_ImportHypervisorConfiguration_RequestSyntax")**

The username for the hypervisor.

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

**[HypervisorArn](#API_BGW_ImportHypervisorConfiguration_ResponseSyntax "#API_BGW_ImportHypervisorConfiguration_ResponseSyntax")**

The Amazon Resource Name (ARN) of the hypervisor you disassociated.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/cli2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/DotNetSDKV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForGoV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForKotlin/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for Python](../../../goto/boto3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/boto3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/ImportHypervisorConfiguration.md")

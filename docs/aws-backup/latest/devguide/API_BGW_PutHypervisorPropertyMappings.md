# PutHypervisorPropertyMappings

This action sets the property mappings for the specified hypervisor.
A hypervisor property mapping displays the relationship of entity properties
available from the hypervisor to the properties available in AWS.

## Request Syntax

```
{
   "HypervisorArn": "`string`",
   "IamRoleArn": "`string`",
   "VmwareToAwsTagMappings": [
      {
         "AwsTagKey": "`string`",
         "AwsTagValue": "`string`",
         "VmwareCategory": "`string`",
         "VmwareTagName": "`string`"
      }
   ]
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[HypervisorArn](#API_BGW_PutHypervisorPropertyMappings_RequestSyntax "#API_BGW_PutHypervisorPropertyMappings_RequestSyntax")**

The Amazon Resource Name (ARN) of the hypervisor.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: Yes

**[IamRoleArn](#API_BGW_PutHypervisorPropertyMappings_RequestSyntax "#API_BGW_PutHypervisorPropertyMappings_RequestSyntax")**

The Amazon Resource Name (ARN) of the IAM role.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Pattern: `arn:(aws|aws-cn|aws-us-gov):iam::([0-9]+):role/(\S+)`

Required: Yes

**[VmwareToAwsTagMappings](#API_BGW_PutHypervisorPropertyMappings_RequestSyntax "#API_BGW_PutHypervisorPropertyMappings_RequestSyntax")**

This action requests the mappings of VMware tags to the
AWS tags.

Type: Array of [VmwareToAwsTagMapping](API_BGW_VmwareToAwsTagMapping.md "API_BGW_VmwareToAwsTagMapping.md") objects

Required: Yes

## Response Syntax

```
{
   "HypervisorArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[HypervisorArn](#API_BGW_PutHypervisorPropertyMappings_ResponseSyntax "#API_BGW_PutHypervisorPropertyMappings_ResponseSyntax")**

The Amazon Resource Name (ARN) of the hypervisor.

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/cli2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/DotNetSDKV4/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForGoV2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForKotlin/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for Python](../../../goto/boto3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/boto3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/PutHypervisorPropertyMappings.md")

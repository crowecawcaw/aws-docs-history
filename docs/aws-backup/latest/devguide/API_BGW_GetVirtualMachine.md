# GetVirtualMachine

By providing the ARN (Amazon Resource Name), this API returns the virtual machine.

## Request Syntax

```
{
   "ResourceArn": "`string`"
}
```

## Request Parameters

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md "CommonParameters.md").

The request accepts the following data in JSON format.

**[ResourceArn](#API_BGW_GetVirtualMachine_RequestSyntax "#API_BGW_GetVirtualMachine_RequestSyntax")**

The Amazon Resource Name (ARN) of the virtual machine.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: Yes

## Response Syntax

```
{
   "VirtualMachine": {
      "HostName": "***string***",
      "HypervisorId": "***string***",
      "LastBackupDate": ***number***,
      "Name": "***string***",
      "Path": "***string***",
      "ResourceArn": "***string***",
      "VmwareTags": [
         {
            "VmwareCategory": "***string***",
            "VmwareTagDescription": "***string***",
            "VmwareTagName": "***string***"
         }
      ]
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[VirtualMachine](#API_BGW_GetVirtualMachine_ResponseSyntax "#API_BGW_GetVirtualMachine_ResponseSyntax")**

This object contains the basic attributes of `VirtualMachine` contained by the output of
`GetVirtualMachine`

Type: [VirtualMachineDetails](API_BGW_VirtualMachineDetails.md "API_BGW_VirtualMachineDetails.md") object

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

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

- [AWS Command Line Interface V2](../../../goto/cli2/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/cli2/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/DotNetSDKV4/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForGoV2/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForJavaScriptV3/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForKotlin/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForPHPV3/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for Python](../../../goto/boto3/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/boto3/backup-gateway-2021-01-01/GetVirtualMachine.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/GetVirtualMachine.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/GetVirtualMachine.md")

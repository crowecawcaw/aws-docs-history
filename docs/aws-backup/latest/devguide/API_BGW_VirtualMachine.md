# VirtualMachine

A virtual machine that is on a hypervisor.

## Contents

**HostName**

The host name of the virtual machine.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**HypervisorId**

The ID of the virtual machine's hypervisor.

Type: String

Required: No

**LastBackupDate**

The most recent date a virtual machine was backed up, in Unix format and UTC time.

Type: Timestamp

Required: No

**Name**

The name of the virtual machine.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**Path**

The path of the virtual machine.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 4096.

Pattern: `[^\x00]+`

Required: No

**ResourceArn**

The Amazon Resource Name (ARN) of the virtual machine. For example,
`arn:aws:backup-gateway:us-west-1:0000000000000:vm/vm-0000ABCDEFGIJKL`.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/VirtualMachine.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/VirtualMachine.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/VirtualMachine.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/VirtualMachine.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/VirtualMachine.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/VirtualMachine.md")

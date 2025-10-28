# Hypervisor

Represents the hypervisor's permissions to which the gateway will connect.

A hypervisor is hardware, software, or firmware that creates and manages virtual machines,
and allocates resources to them.

## Contents

**Host**

The server host of the hypervisor. This can be either an IP address or a fully-qualified
domain name (FQDN).

Type: String

Length Constraints: Minimum length of 3. Maximum length of 128.

Pattern: `.+`

Required: No

**HypervisorArn**

The Amazon Resource Name (ARN) of the hypervisor.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `arn:(aws|aws-cn|aws-us-gov):backup-gateway(:[a-zA-Z-0-9]+){3}\/[a-zA-Z-0-9]+`

Required: No

**KmsKeyArn**

The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the
hypervisor.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`

Required: No

**Name**

The name of the hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**State**

The state of the hypervisor.

Type: String

Valid Values: `PENDING | ONLINE | OFFLINE | ERROR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/Hypervisor.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/Hypervisor.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/Hypervisor.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/Hypervisor.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/Hypervisor.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/Hypervisor.md")

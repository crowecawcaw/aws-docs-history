# HypervisorDetails

These are the details of the specified hypervisor. A hypervisor is hardware,
software, or firmware that creates and manages virtual machines, and allocates
resources to them.

## Contents

**Host**

The server host of the hypervisor. This can be either an IP address or
a fully-qualified domain name (FQDN).

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

The Amazon Resource Name (ARN) of the AWS KMS
used to encrypt the hypervisor.

Type: String

Length Constraints: Minimum length of 50. Maximum length of 500.

Pattern: `(^arn:(aws|aws-cn|aws-us-gov):kms:([a-zA-Z0-9-]+):([0-9]+):(key|alias)/(\S+)$)|(^alias/(\S+)$)`

Required: No

**LastSuccessfulMetadataSyncTime**

This is the time when the most recent successful sync
of metadata occurred.

Type: Timestamp

Required: No

**LatestMetadataSyncStatus**

This is the most recent status for the indicated metadata sync.

Type: String

Valid Values: `CREATED | RUNNING | FAILED | PARTIALLY_FAILED | SUCCEEDED`

Required: No

**LatestMetadataSyncStatusMessage**

This is the most recent status for the indicated metadata sync.

Type: String

Required: No

**LogGroupArn**

The Amazon Resource Name (ARN) of the group of gateways within
the requested log.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 2048.

Pattern: `$|^arn:(aws|aws-cn|aws-us-gov):logs:([a-zA-Z0-9-]+):([0-9]+):log-group:[a-zA-Z0-9_\-\/\.]+:\*`

Required: No

**Name**

This is the name of the specified hypervisor.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `[a-zA-Z0-9-]*`

Required: No

**State**

This is the current state of the specified hypervisor.

The possible states are `PENDING`, `ONLINE`,
`OFFLINE`, or `ERROR`.

Type: String

Valid Values: `PENDING | ONLINE | OFFLINE | ERROR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/backup-gateway-2021-01-01/HypervisorDetails.md "../../../goto/SdkForCpp/backup-gateway-2021-01-01/HypervisorDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/HypervisorDetails.md "../../../goto/SdkForJavaV2/backup-gateway-2021-01-01/HypervisorDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/HypervisorDetails.md "../../../goto/SdkForRubyV3/backup-gateway-2021-01-01/HypervisorDetails.md")

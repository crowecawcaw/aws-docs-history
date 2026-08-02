# RegionStatus

Represents the status of a multi-region operation in a specific AWS Region. This
structure is used to report per-region progress for both telemetry evaluation and telemetry
rule replication.

## Contents

**FailureReason**

The reason for a failure status in this region. This field is only populated when
`Status` indicates a failure.

Type: String

Required: No

**Region**

The AWS Region code (for example, `eu-west-1` or `us-west-2`)
that this status applies to.

Type: String

Length Constraints: Minimum length of 1.

Required: No

**RuleArn**

The Amazon Resource Name (ARN) of the telemetry rule in this spoke region. This field is
only present for telemetry rule region statuses and is populated when the rule has been
successfully created in the spoke region (status is `ACTIVE`).

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1011.

Pattern: `arn:aws([a-z0-9\-]+)?:([a-zA-Z0-9\-]+):([a-z0-9\-]+)?:([0-9]{12})?:(.+)`

Required: No

**Status**

The status of the operation in this region. For telemetry evaluation, valid values
include `STARTING`, `RUNNING`, and `FAILED_START`. For
telemetry rules, valid values include `PENDING`, `ACTIVE`, and
`FAILED`.

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/observabilityadmin-2018-05-10/RegionStatus.md "../../../goto/SdkForCpp/observabilityadmin-2018-05-10/RegionStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/RegionStatus.md "../../../goto/SdkForJavaV2/observabilityadmin-2018-05-10/RegionStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/RegionStatus.md "../../../goto/SdkForRubyV3/observabilityadmin-2018-05-10/RegionStatus.md")

# Pipe

An object that represents a pipe. Amazon EventBridgePipes connect event sources to
targets and reduces the need for specialized knowledge and integration code.

## Contents

**Arn**

The ARN of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:aws([a-z]|\-)*:([a-zA-Z0-9\-]+):([a-z]|\d|\-)*:([0-9]{12})?:(.+)`

Required: No

**CreationTime**

The time the pipe was created.

Type: Timestamp

Required: No

**CurrentState**

The state the pipe is in.

Type: String

Valid Values: `RUNNING | STOPPED | CREATING | UPDATING | DELETING | STARTING | STOPPING | CREATE_FAILED | UPDATE_FAILED | START_FAILED | STOP_FAILED | DELETE_FAILED | CREATE_ROLLBACK_FAILED | DELETE_ROLLBACK_FAILED | UPDATE_ROLLBACK_FAILED`

Required: No

**DesiredState**

The state the pipe should be in.

Type: String

Valid Values: `RUNNING | STOPPED`

Required: No

**Enrichment**

The ARN of the enrichment resource.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 1600.

Pattern: `$|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

**LastModifiedTime**

When the pipe was last updated, in [ISO-8601 format](https://www.w3.org/TR/NOTE-datetime "https://www.w3.org/TR/NOTE-datetime") (YYYY-MM-DDThh:mm:ss.sTZD).

Type: Timestamp

Required: No

**Name**

The name of the pipe.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 64.

Pattern: `[\.\-_A-Za-z0-9]+`

Required: No

**Source**

The ARN of the source resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `smk://(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]):[0-9]{1,5}|arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

**StateReason**

The reason the pipe is in its current state.

Type: String

Length Constraints: Minimum length of 0. Maximum length of 512.

Pattern: `.*`

Required: No

**Target**

The ARN of the target resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 1600.

Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-]+):([a-z]{2,4}((-gov)|(-de)|(-iso([a-z]?)))?-[a-z]+(-\d{1})?)?:(\d{12})?:(.+)`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/pipes-2015-10-07/Pipe.md "../../../goto/SdkForCpp/pipes-2015-10-07/Pipe.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/pipes-2015-10-07/Pipe.md "../../../goto/SdkForJavaV2/pipes-2015-10-07/Pipe.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/pipes-2015-10-07/Pipe.md "../../../goto/SdkForRubyV3/pipes-2015-10-07/Pipe.md")

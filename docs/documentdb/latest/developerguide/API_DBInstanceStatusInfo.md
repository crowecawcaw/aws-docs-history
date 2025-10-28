# DBInstanceStatusInfo

Provides a list of status information for an instance.

## Contents

###### Note

In the following list, the required parameters are described first.

**Message**

Details of the error if there is an error for the instance. If the instance is not in
an error state, this value is blank.

Type: String

Required: No

**Normal**

A Boolean value that is `true` if the instance is operating normally, or
`false` if the instance is in an error state.

Type: Boolean

Required: No

**Status**

Status of the instance. For a `StatusType` of read replica, the values
can be `replicating`, error, `stopped`, or
`terminated`.

Type: String

Required: No

**StatusType**

This value is currently "`read replication`."

Type: String

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/docdb-2014-10-31/DBInstanceStatusInfo.md "../../../goto/SdkForCpp/docdb-2014-10-31/DBInstanceStatusInfo.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/docdb-2014-10-31/DBInstanceStatusInfo.md "../../../goto/SdkForJavaV2/docdb-2014-10-31/DBInstanceStatusInfo.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/docdb-2014-10-31/DBInstanceStatusInfo.md "../../../goto/SdkForRubyV3/docdb-2014-10-31/DBInstanceStatusInfo.md")

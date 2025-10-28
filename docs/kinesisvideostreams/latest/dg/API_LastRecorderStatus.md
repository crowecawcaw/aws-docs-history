# LastRecorderStatus

The latest status of a stream's edge recording job.

## Contents

**JobStatusDetails**

A description of a recorder job’s latest status.

Type: String

Required: No

**LastCollectedTime**

The timestamp at which the recorder job was last executed and media stored to local disk.

Type: Timestamp

Required: No

**LastUpdatedTime**

The timestamp at which the recorder status was last updated.

Type: Timestamp

Required: No

**RecorderStatus**

The status of the latest recorder job.

Type: String

Valid Values: `SUCCESS | USER_ERROR | SYSTEM_ERROR`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/kinesisvideo-2017-09-30/LastRecorderStatus.md "../../../goto/SdkForCpp/kinesisvideo-2017-09-30/LastRecorderStatus.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/LastRecorderStatus.md "../../../goto/SdkForJavaV2/kinesisvideo-2017-09-30/LastRecorderStatus.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/LastRecorderStatus.md "../../../goto/SdkForRubyV3/kinesisvideo-2017-09-30/LastRecorderStatus.md")

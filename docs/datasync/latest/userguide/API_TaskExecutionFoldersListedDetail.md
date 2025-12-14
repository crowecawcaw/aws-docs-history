# TaskExecutionFoldersListedDetail

The number of directories that DataSync finds at your locations.

###### Note

Applies only to [Enhanced mode
tasks](choosing-task-mode.md "choosing-task-mode.md").

## Contents

**AtDestinationForDelete**

The number of directories that DataSync finds at your destination location. This
counter is only applicable if you [configure your task](configure-metadata.md#task-option-file-object-handling "configure-metadata.md#task-option-file-object-handling") to delete data in the destination that isn't in the
source.

Type: Long

Required: No

**AtSource**

The number of directories that DataSync finds at your source location.

- With a [manifest](transferring-with-manifest.md "transferring-with-manifest.md"), DataSync
  lists only what's in your manifest (and not everything at your source location).
- With an include [filter](filtering.md "filtering.md"), DataSync lists only what
  matches the filter at your source location.
- With an exclude filter, DataSync lists everything at your source location before applying
  the filter.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md "../../../goto/SdkForCpp/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md "../../../goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md "../../../goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionFoldersListedDetail.md")

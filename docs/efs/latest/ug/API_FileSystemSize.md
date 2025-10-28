# FileSystemSize

The latest known metered size (in bytes) of data stored in the file system, in its
`Value` field, and the time at which that size was determined in its
`Timestamp` field. The value doesn't represent the size of a consistent
snapshot of the file system, but it is eventually consistent when there are no writes to the
file system. That is, the value represents the actual size only if the file system is not
modified for a period longer than a couple of hours. Otherwise, the value is not necessarily
the exact size the file system was at any instant in time.

## Contents

**Value**

The latest known metered size (in bytes) of data stored in the file system.

Type: Long

Valid Range: Minimum value of 0.

Required: Yes

**Timestamp**

The time at which the size of data, returned in the `Value` field, was
determined. The value is the integer number of seconds since 1970-01-01T00:00:00Z.

Type: Timestamp

Required: No

**ValueInArchive**

The latest known metered size (in bytes) of data stored in the Archive
storage class.

Type: Long

Valid Range: Minimum value of 0.

Required: No

**ValueInIA**

The latest known metered size (in bytes) of data stored in the Infrequent Access storage
class.

Type: Long

Valid Range: Minimum value of 0.

Required: No

**ValueInStandard**

The latest known metered size (in bytes) of data stored in the Standard
storage class.

Type: Long

Valid Range: Minimum value of 0.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemSize.md "../../../goto/SdkForCpp/elasticfilesystem-2015-02-01/FileSystemSize.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemSize.md "../../../goto/SdkForJavaV2/elasticfilesystem-2015-02-01/FileSystemSize.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemSize.md "../../../goto/SdkForRubyV3/elasticfilesystem-2015-02-01/FileSystemSize.md")

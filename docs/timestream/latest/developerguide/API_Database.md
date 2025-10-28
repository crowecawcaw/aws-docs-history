For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Database

A top-level container for a table. Databases and tables are the fundamental management concepts in Amazon
Timestream. All tables in a database are encrypted with the same AWS KMS key.

## Contents

**Arn**

The Amazon Resource Name that uniquely identifies this database.

Type: String

Required: No

**CreationTime**

The time when the database was created, calculated from the Unix epoch time.

Type: Timestamp

Required: No

**DatabaseName**

The name of the Timestream database.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: No

**KmsKeyId**

The identifier of the AWS KMS key used to encrypt the data stored in the database.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**LastUpdatedTime**

The last time that this database was updated.

Type: Timestamp

Required: No

**TableCount**

The total number of tables found within a Timestream database.

Type: Long

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Database.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Database.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Database.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Database.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Database.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Database.md")

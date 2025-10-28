For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Table

Represents a database table in Timestream. Tables contain one or more related time series. You can
modify the retention duration of the memory store and the magnetic store for a table.

## Contents

**Arn**

The Amazon Resource Name that uniquely identifies this table.

Type: String

Required: No

**CreationTime**

The time when the Timestream table was created.

Type: Timestamp

Required: No

**DatabaseName**

The name of the Timestream database that contains this table.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: No

**LastUpdatedTime**

The time when the Timestream table was last updated.

Type: Timestamp

Required: No

**MagneticStoreWriteProperties**

Contains properties to set on the table when enabling magnetic store writes.

Type: [MagneticStoreWriteProperties](API_MagneticStoreWriteProperties.md "API_MagneticStoreWriteProperties.md") object

Required: No

**RetentionProperties**

The retention duration for the memory store and magnetic store.

Type: [RetentionProperties](API_RetentionProperties.md "API_RetentionProperties.md") object

Required: No

**Schema**

The schema of the table.

Type: [Schema](API_Schema.md "API_Schema.md") object

Required: No

**TableName**

The name of the Timestream table.

Type: String

Length Constraints: Minimum length of 3. Maximum length of 256.

Required: No

**TableStatus**

The current state of the table:

- `DELETING` - The table is being deleted.
- `ACTIVE` - The table is ready for use.

Type: String

Valid Values: `ACTIVE | DELETING | RESTORING`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/timestream-write-2018-11-01/Table.md "../../../goto/SdkForCpp/timestream-write-2018-11-01/Table.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Table.md "../../../goto/SdkForJavaV2/timestream-write-2018-11-01/Table.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Table.md "../../../goto/SdkForRubyV3/timestream-write-2018-11-01/Table.md")

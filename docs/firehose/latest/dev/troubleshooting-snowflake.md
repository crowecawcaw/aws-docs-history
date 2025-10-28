# Troubleshooting Snowflake

This section describes common troubleshooting steps while using Snowflake as a
destination

## Firehose stream creation fails

If Firehose stream creation fails for a stream delivering data to a
PrivateLink-enabled Snowflake Cluster, it indicates that the VPCE-ID is not
reachable by Firehose. This can be due to one of the following reasons:

- Incorrect VPCE-ID. Confirm that there are no typographic errors.
- Firehose does not support region-less Snowflake URLs in preview. Provide the
  URL using Snowflake Account Locator. See [Snowflake documentation](https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-legacy-account-locator-in-a-region "https://docs.snowflake.com/en/user-guide/admin-account-identifier#format-2-legacy-account-locator-in-a-region") for more details.
- Confirm that the Firehose stream is created in the same AWS Region as the Snowflake
  Region.
- If the issue persists, reach out to AWS support.

### Delivery failures

Check the following if data is not getting delivered to your Snowflake table. Snowflake delivery failed data will be delivered to the S3 error bucket along with an error code and an error message that corresponds to the payload.
Following are few a common error scenarios. For the entire list of error codes, see [Snowflake Data delivery
errors](monitoring-with-cloudwatch-logs.md#monitoring-snowflake-errors "monitoring-with-cloudwatch-logs.md#monitoring-snowflake-errors").

- **Error code: Snowflake.DefaultRoleMissing**: Indicates that snowflake role is not configured while creating Firehose stream. If Snowflake role is not configured, make sure you set a default role to the Snowflake user specified.
- **Error code: Snowflake.ExtraColumns**: Indicates that insert to Snowflake is rejected due to extra columns in the input payload. Columns not present in table shouldn’t be specified. Note that Snowflake column names are case-sensitive. If the delivery is failing with this error despite column being present in table, make sure that the case of the column name in input payload matches the column name declared in table definition.
- **Error code: Snowflake.MissingColumns**: Indicates that insert to Snowflake is rejected due to missing columns in input payload. Make sure that values are specified for all non-nullable columns.
- **Error code: Snowflake.InvalidInput**: This could happen when Firehose failed to parse the input payload provided into valid JSON format. Make sure that the json payload is well formed, doesn’t have extra double quotes, quotes, escape characters etc. Currently Firehose supports only single JSON item as record payload, JSON arrays are not supported.
- **Error code: Snowflake.InvalidValue**: Indicates that delivery failed due to incorrect data type in the input payload. Make sure that the JSON values specified in input payload adhere to the datatype declared in Snowflake table definition.
- **Error code: Snowflake.InvalidTableType**: Indicates that table type configured in the Firehose stream is not supported. Refer to the limitations at [Limitations](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview#limitations "https://docs.snowflake.com/en/user-guide/data-load-snowpipe-streaming-overview#limitations")) of snowpipe streaming for the supported tables, columns and data types.

###### Note

For any reason, if the table definition or role permissions are changed on your Snowflake destination after creating the Firehose stream, it can take several minutes for Firehose to detect those changes. If you are seeing delivery errors due to this, try deleting and recreating the Firehose stream.

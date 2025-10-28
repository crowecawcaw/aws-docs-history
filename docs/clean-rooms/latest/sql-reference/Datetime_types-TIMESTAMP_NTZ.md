# TIMESTAMP_NTZ

Use the TIMESTAMP_NTZ data type to store complete timestamp values that include the
date, the time of day, without the local time zone.

TIMESTAMP represents values comprising values of fields `year`,
`month`, `day`, `hour`, `minute`, and
`second`. All operations are performed without taking any time zone into
account.

TIMESTAMP in Spark is a user-specified alias associated with one of the TIMESTAMP_LTZ
and TIMESTAMP_NTZ variations. You can set the default timestamp type as TIMESTAMP_LTZ
(default value) or TIMESTAMP_NTZ via the configuration
`spark.sql.timestampType`.

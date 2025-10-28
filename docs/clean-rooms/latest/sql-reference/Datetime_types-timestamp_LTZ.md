# TIMESTAMP_LTZ

Use the TIMESTAMP_LTZ data type to store complete timestamp values that include the
date, the time of day, and the local time zone.

TIMESTAMP represents values comprising values of fields `year`,
`month`, `day`, `hour`, `minute`, and
`second`, with the session local timezone. The `timestamp`
value represents an absolute point in time.

TIMESTAMP in Spark is a user-specified alias associated with one of the TIMESTAMP_LTZ
and TIMESTAMP_NTZ variations. You can set the default timestamp type as TIMESTAMP_LTZ
(default value) or TIMESTAMP_NTZ via the configuration
`spark.sql.timestampType`.

# Quotas, naming rules and data types

## Quota terminologies

- Read Request Unit (RRU): Measure of read throughput, where the number of RRUs
  per read request is equal to the ceiling of read record's size divided into 4KB
  chunks. The minimum RRU per request is 0.
- Write Request Unit (WRU): Measure of write throughput, where the number of
  WRUs per write request is equal to the ceiling of the written record's size
  divided into 1KB chunks. The minimum WRU per request is 1 (including delete
  operations).

## Limits and quotas

###### Note

Soft limits can be increased based on your needs.

- **Maximum number of feature groups per AWS
  account:** Soft limit of 100.
- **Maximum number of feature definitions per feature
  group:** 2500.
- **Maximum number of RRU per record identifier:**
  2400 RRU per second.
- **Maximum number of WRU per record identifier:**
  500 WRU per second.
- **Max Read Capacity Units (RCU) that can be provisioned on a
  single feature group:** 40000 RCU.
- **Max Write Capacity Units (WCU) that can be provisioned on
  a single feature group:** 40000 WCU.
- **Max Read Capacity Units that can be provisioned across all
  feature groups in a region:** 80000 RCU.
- **Max Write Capacity Units that can be provisioned across
  all feature groups in a region:** 80000 WCU.
- **Maximum Transactions per second (TPS) per API per
  AWS account:** Soft limit of 10000 TPS per API excluding the
  `BatchGetRecord` API call, which has a soft limit of 500
  TPS.
- **Maximum size of a record:** 350KB.
- **Maximum size of a record identifier:** 2KB.
- **Maximum size of a feature value:** 350KB.
- **Maximum number of concurrent feature group creation
  workflows:** 4.
- **BatchGetRecord API:** Can contain as many as
  100 records and can query up to 100 feature groups.

For information about service quotas and how to request a quota increase, see [AWS service
quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

## Naming rules

- **Reserved Words:** The following are reserved
  words and cannot be used as feature names in feature definitions:
  `is_deleted`, `write_time`, and
  `api_invocation_time`.

## Data types

- **String Feature Type:** Strings are Unicode with
  UTF-8 binary encoding. The minimum length of a string can be zero, the maximum
  length is constrained by the maximum size of a record.
- **Fractional Feature Type:** Fractional feature
  values must conform to a double precision floating point number as defined by
  the [IEEE 754
  standard](https://en.wikipedia.org/wiki/IEEE_754 "https://en.wikipedia.org/wiki/IEEE_754").
- **Integral Feature Type:** Feature Store supports
  integral values in the range of a 64-bit signed integer. Minimum value of
  -263 and a maximum value:
  263 - 1.
- **Event Time Features:** All feature groups have an
  event time feature with nanosecond precision. Any event time with lower than
  nanosecond precision will lead to backwards incompatibility. The feature can
  have a feature type of either String or Fractional.
  - A string event time is accepted in ISO-8601 format, in UTC time,
    conforming to the pattern(s): [yyyy-MM-dd'T'HH:mm:ssZ,
    yyyy-MM-dd'T'HH:mm:ss.SSSSSSSSSZ].
  - A fractional event time value is accepted as seconds from unix epoch.
    Event times must be in the range of [0000-01-01T00:00:00.000000000Z,
    9999-12-31T23:59:59.999999999Z]. For feature groups in the
    `Iceberg` table format, you can only use String type for
    the event time.

# Create and query a table for Amazon VPC

flow logs using partition projection

Use a `CREATE TABLE` statement like the following to create a table,
partition the table, and populate the partitions automatically by using [partition
projection](partition-projection.md "partition-projection.md"). Replace the table name `test_table_vpclogs` in the
example with the name of your table. Edit the `LOCATION` clause to specify
the Amazon S3 bucket that contains your Amazon VPC log data.

The following `CREATE TABLE` statement is for VPC flow logs delivered in
non-Hive style partitioning format. The example allows for multi-account aggregation. If
you are centralizing VPC Flow logs from multiple accounts into one Amazon S3 bucket, the
account ID must be entered in the Amazon S3 path.

```
CREATE EXTERNAL TABLE IF NOT EXISTS test_table_vpclogs (
  version int,
  account_id string,
  interface_id string,
  srcaddr string,
  dstaddr string,
  srcport int,
  dstport int,
  protocol bigint,
  packets bigint,
  bytes bigint,
  start bigint,
  `end` bigint,
  action string,
  log_status string,
  vpc_id string,
  subnet_id string,
  instance_id string,
  tcp_flags int,
  type string,
  pkt_srcaddr string,
  pkt_dstaddr string,
  az_id string,
  sublocation_type string,
  sublocation_id string,
  pkt_src_aws_service string,
  pkt_dst_aws_service string,
  flow_direction string,
  traffic_path int
)
PARTITIONED BY (accid string, region string, day string)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ' '
LOCATION '`$LOCATION_OF_LOGS`'
TBLPROPERTIES
(
"skip.header.line.count"="1",
"projection.enabled" = "true",
"projection.accid.type" = "enum",
"projection.accid.values" = "`$ACCID_1`,`$ACCID_2`",
"projection.region.type" = "enum",
"projection.region.values" = "`$REGION_1`,`$REGION_2`,`$REGION_3`",
"projection.day.type" = "date",
"projection.day.range" = "`$START_RANGE`,NOW",
"projection.day.format" = "yyyy/MM/dd",
"storage.location.template" = "s3://amzn-s3-demo-bucket/AWSLogs/${accid}/vpcflowlogs/${region}/${day}"
)
```

## Example queries for

test_table_vpclogs

The following example queries query the `test_table_vpclogs` created by
the preceding `CREATE TABLE` statement. Replace
`test_table_vpclogs` in the queries with the name of your own table.
Modify the column values and other variables according to your requirements.

To return the first 100 access log entries in chronological order for a specified
period of time, run a query like the following.

```
SELECT *
FROM test_table_vpclogs
WHERE day >= '2021/02/01' AND day < '2021/02/28'
ORDER BY day ASC
LIMIT 100
```

To view which server receives the top ten number of HTTP packets for a specified
period of time, run a query like the following. The query counts the number of
packets received on HTTPS port 443, groups them by destination IP address, and
returns the top 10 entries from the previous week.

```
SELECT SUM(packets) AS packetcount,
       dstaddr
FROM test_table_vpclogs
WHERE dstport = 443
  AND day >= '2021/03/01'
  AND day < '2021/03/31'
GROUP BY dstaddr
ORDER BY packetcount DESC
LIMIT 10
```

To return the logs that were created during a specified period of time, run a
query like the following.

```
SELECT interface_id,
       srcaddr,
       action,
       protocol,
       to_iso8601(from_unixtime(start)) AS start_time,
       to_iso8601(from_unixtime("end")) AS end_time
FROM test_table_vpclogs
WHERE DAY >= '2021/04/01'
  AND DAY < '2021/04/30'
```

To return the access logs for a source IP address between specified time periods,
run a query like the following.

```
SELECT *
FROM test_table_vpclogs
WHERE srcaddr = '10.117.1.22'
  AND day >= '2021/02/01'
  AND day < '2021/02/28'
```

To list rejected TCP connections, run a query like the following.

```
SELECT day,
       interface_id,
       srcaddr,
       action,
       protocol
FROM test_table_vpclogs
WHERE action = 'REJECT' AND protocol = 6 AND day >= '2021/02/01' AND day < '2021/02/28'
LIMIT 10
```

To return the access logs for the IP address range that starts with
`10.117`, run a query like the following.

```
SELECT *
FROM test_table_vpclogs
WHERE split_part(srcaddr,'.', 1)='10'
  AND split_part(srcaddr,'.', 2) ='117'
```

To return the access logs for a destination IP address between a certain time
range, run a query like the following.

```
SELECT *
FROM test_table_vpclogs
WHERE dstaddr = '10.0.1.14'
  AND day >= '2021/01/01'
  AND day < '2021/01/31'
```

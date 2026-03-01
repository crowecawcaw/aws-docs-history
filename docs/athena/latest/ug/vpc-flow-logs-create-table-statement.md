# Create a table for Amazon VPC flow logs and query it

The following procedure creates an Amazon VPC table for Amazon VPC flow logs. When you create a
flow log with a custom format, you create a table with fields that match the fields that
you specified when you created the flow log in the same order that you specified
them.

###### To create an Athena table for Amazon VPC flow logs

1. Enter a DDL statement like the following into the Athena console query editor,
   following the guidelines in the [Considerations and limitations](vpc-flow-logs.md#vpc-flow-logs-common-considerations "vpc-flow-logs.md#vpc-flow-logs-common-considerations") section. The sample
   statement creates a table that has the columns for Amazon VPC flow logs versions 2
   through 5 as documented in [Flow log
   records](../../../vpc/latest/userguide/flow-logs.md#flow-log-records "../../../vpc/latest/userguide/flow-logs.md#flow-log-records"). If you use a different set of columns or order of columns,
   modify the statement accordingly.

```
CREATE EXTERNAL TABLE IF NOT EXISTS `vpc_flow_logs` (
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
  region string,
  az_id string,
  sublocation_type string,
  sublocation_id string,
  pkt_src_aws_service string,
  pkt_dst_aws_service string,
  flow_direction string,
  traffic_path int
)
PARTITIONED BY (`date` date)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ' '
LOCATION 's3://amzn-s3-demo-bucket/`prefix`/AWSLogs/`{account_id}`/vpcflowlogs/`{region_code}`/'
TBLPROPERTIES ("skip.header.line.count"="1");

```

Note the following points:

    * The query specifies `ROW FORMAT DELIMITED` and omits
     specifying a SerDe. This means that the query uses the [Lazy Simple SerDe for CSV, TSV, and custom-delimited files](lazy-simple-serde.md "lazy-simple-serde.md"). In
     this query, fields are terminated by a space.
    * The `PARTITIONED BY` clause uses the `date`
     type. This makes it possible to use mathematical operators in queries to
     select what's older or newer than a certain date.


    ###### Note

    Because `date` is a reserved keyword in DDL statements,
     it is escaped by back tick characters. For more information, see
     [Escape reserved keywords in queries](reserved-words.md "reserved-words.md").
    * For a VPC flow log with a different custom format, modify the fields
     to match the fields that you specified when you created the flow
     log.

2. Modify the `LOCATION
's3://amzn-s3-demo-bucket/`prefix`/AWSLogs/`{account_id}`/vpcflowlogs/`{region_code}`/'`
   to point to the Amazon S3 bucket that contains your log data.
3. Run the query in Athena console. After the query completes, Athena registers the
   `vpc_flow_logs` table, making the data in it ready for you to
   issue queries.
4. Create partitions to be able to read the data, as in the following sample
   query. This query creates a single partition for a specified date. Replace the
   placeholders for date and location as needed.

###### Note

This query creates a single partition only, for a date that you specify.
To automate the process, use a script that runs this query and creates
partitions this way for the `year/month/day`, or use a
`CREATE TABLE` statement that specifies [partition
projection](vpc-flow-logs-partition-projection.md "vpc-flow-logs-partition-projection.md").

```
ALTER TABLE vpc_flow_logs
ADD PARTITION (`date`='`YYYY-MM-dd`')
LOCATION 's3://amzn-s3-demo-bucket/`prefix`/AWSLogs/`{account_id}`/vpcflowlogs/`{region_code}`/`YYYY`/`MM`/`dd`';

```

## Example queries for the vpc_flow_logs table

Use the query editor in the Athena console to run SQL statements on the table that
you create. You can save the queries, view previous queries, or download query
results in CSV format. In the following examples, replace `vpc_flow_logs`
with the name of your table. Modify the column values and other variables according
to your requirements.

The following example query lists a maximum of 100 flow logs for the date
specified.

```
SELECT *
FROM vpc_flow_logs
WHERE date = DATE('2020-05-04')
LIMIT 100;
```

The following query lists all of the rejected TCP connections and uses the newly
created date partition column, `date`, to extract from it the day of the
week for which these events occurred.

```
SELECT day_of_week(date) AS
  day,
  date,
  interface_id,
  srcaddr,
  action,
  protocol
FROM vpc_flow_logs
WHERE action = 'REJECT' AND protocol = 6
LIMIT 100;
```

To see which one of your servers is receiving the highest number of HTTPS
requests, use the following query. It counts the number of packets received on HTTPS
port 443, groups them by destination IP address, and returns the top 10 from the
last week.

```
SELECT SUM(packets) AS
  packetcount,
  dstaddr
FROM vpc_flow_logs
WHERE dstport = 443 AND date > current_date - interval '7' day
GROUP BY dstaddr
ORDER BY packetcount DESC
LIMIT 10;
```

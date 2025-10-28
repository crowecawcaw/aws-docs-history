AWS Application Discovery Service will discontinue onboarding new customers starting November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Using predefined queries in Amazon Athena

This section contains a set of predefined queries that perform typical use cases, such
as TCO analysis and network visualization. You can use these queries as is or modify
them to suit your needs.

###### To use a predefined query

1. In the AWS Migration Hub console, choose **Servers** in the
   navigation pane.
2. To open the Amazon Athena console, choose **Explore data in
   Amazon Athena**.
3. On the **Query Editor** page, in the navigation pane under
   **Database**, make sure that
   **application_discovery_service_database** is
   selected.
4. Choose the plus (**+**) sign in the Query Editor
   to create a tab for a new query.
5. Copy one of the queries from [Predefined queries](#pq-query-examples "#pq-query-examples").
6. Paste the query into the query pane of the new query tab you just
   created.
7. Choose **Run Query**.

## Predefined queries

Choose a title to see information about the query.

This view helper function retrieves IP addresses and hostnames for a given
server. You can use this view in other queries. For information about how to
create a view, see [CREATE
VIEW](../../../athena/latest/ug/create-view.md "../../../athena/latest/ug/create-view.md") in the _Amazon Athena User Guide_.

```
CREATE OR REPLACE VIEW hostname_ip_helper AS
SELECT DISTINCT
  "os"."host_name"
, "nic"."agent_id"
, "nic"."ip_address"
FROM
  os_info_agent os
, network_interface_agent nic
WHERE ("os"."agent_id" = "nic"."agent_id");
```

This query can help you perform data validation. If you've deployed agents
on a number of servers in your network, you can use this query to understand
if there are other servers in your network without agents deployed on them.
In this query, we look into the inbound and outbound network traffic, and
filter the traffic for private IP addresses only. That is, IP addresses
starting with `192`, `10`, or `172`.

```
SELECT DISTINCT "destination_ip" "IP Address" ,
         (CASE
    WHEN (
    (SELECT "count"(*)
    FROM network_interface_agent
    WHERE ("ip_address" = "destination_ip") ) = 0) THEN
        'no'
        WHEN (
        (SELECT "count"(*)
        FROM network_interface_agent
        WHERE ("ip_address" = "destination_ip") ) > 0) THEN
            'yes' END) "agent_running"
    FROM outbound_connection_agent
WHERE ((("destination_ip" LIKE '192.%')
        OR ("destination_ip" LIKE '10.%'))
        OR ("destination_ip" LIKE '172.%'))
UNION
SELECT DISTINCT "source_ip" "IP ADDRESS" ,
         (CASE
    WHEN (
    (SELECT "count"(*)
    FROM network_interface_agent
    WHERE ("ip_address" = "source_ip") ) = 0) THEN
        'no'
        WHEN (
        (SELECT "count"(*)
        FROM network_interface_agent
        WHERE ("ip_address" = "source_ip") ) > 0) THEN
            'yes' END) "agent_running"
    FROM inbound_connection_agent
WHERE ((("source_ip" LIKE '192.%')
        OR ("source_ip" LIKE '10.%'))
        OR ("source_ip" LIKE '172.%'));
```

You can use this query to analyze system performance and utilization
pattern data for your on-premises servers that have agents installed on
them. The query combines the `system_performance_agent` table
with the `os_info_agent` table to identify the hostname for each
server. This query returns the time series utilization data (in 15 minute
intervals) for all the servers where agents are running.

```
SELECT "OS"."os_name" "OS Name" ,
    "OS"."os_version" "OS Version" ,
    "OS"."host_name" "Host Name" ,
     "SP"."agent_id" ,
     "SP"."total_num_cores" "Number of Cores" ,
     "SP"."total_num_cpus" "Number of CPU" ,
     "SP"."total_cpu_usage_pct" "CPU Percentage" ,
     "SP"."total_disk_size_in_gb" "Total Storage (GB)" ,
     "SP"."total_disk_free_size_in_gb" "Free Storage (GB)" ,
     ("SP"."total_disk_size_in_gb" - "SP"."total_disk_free_size_in_gb") "Used Storage" ,
     "SP"."total_ram_in_mb" "Total RAM (MB)" ,
     ("SP"."total_ram_in_mb" - "SP"."free_ram_in_mb") "Used RAM (MB)" ,
     "SP"."free_ram_in_mb" "Free RAM (MB)" ,
     "SP"."total_disk_read_ops_per_sec" "Disk Read IOPS" ,
     "SP"."total_disk_bytes_written_per_sec_in_kbps" "Disk Write IOPS" ,
     "SP"."total_network_bytes_read_per_sec_in_kbps" "Network Reads (kbps)" ,
     "SP"."total_network_bytes_written_per_sec_in_kbps" "Network Write (kbps)"
FROM "sys_performance_agent" "SP" , "OS_INFO_agent" "OS"
WHERE ("SP"."agent_id" = "OS"."agent_id") limit 10;
```

This query gets the details on the outbound traffic for each service,
along with the port number and process details.

Before running the query, if you have not already done so, you must create
the `iana_service_ports_import` table that contains the IANA port
registry database downloaded from IANA. For information about how to create
this table, see [Creating the IANA port registry import
table](#pq-create-iana-import-table "#pq-create-iana-import-table").

After the `iana_service_ports_import` table is created, create
two view helper functions for tracking outbound traffic. For information
about how to create a view, see [CREATE VIEW](../../../athena/latest/ug/create-view.md "../../../athena/latest/ug/create-view.md") in the _Amazon Athena User Guide_.

###### To create outbound tracking helper functions

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Create the `valid_outbound_ips_helper` view, using the
   following helper function that lists all distinct outbound
   destination IP addresses.

```
CREATE OR REPLACE VIEW valid_outbound_ips_helper AS
SELECT DISTINCT "destination_ip"
FROM outbound_connection_agent;
```

3. Create the `outbound_query_helper` view, using the
   following helper function that determines the frequency of
   communication for outbound traffic.

```
CREATE OR REPLACE VIEW outbound_query_helper AS
SELECT "agent_id" ,
         "source_ip" ,
         "destination_ip" ,
         "destination_port" ,
         "agent_assigned_process_id" ,
         "count"(*) "frequency"
FROM outbound_connection_agent
WHERE (("ip_version" = 'IPv4')
        AND ("destination_ip" IN
    (SELECT *
    FROM valid_outbound_ips_helper )))
GROUP BY  "agent_id", "source_ip", "destination_ip", "destination_port", "agent_assigned_process_id";
```

4. After you create the `iana_service_ports_import` table
   and your two helper functions, you can run the following query to
   get the details on the outbound traffic for each service, along with
   the port number and process details.

```
SELECT hip1.host_name "Source Host Name",
         outbound_connections_results0.source_ip "Source IP Address",
         hip2.host_name "Destination Host Name",
         outbound_connections_results0.destination_ip "Destination IP Address",
         outbound_connections_results0.frequency "Connection Frequency",
         outbound_connections_results0.destination_port "Destination Communication Port",
         outbound_connections_results0.servicename "Process Service Name",
         outbound_connections_results0.description "Process Service Description"
FROM
    (SELECT DISTINCT o.source_ip,
         o.destination_ip,
         o.frequency,
         o.destination_port,
         ianap.servicename,
         ianap.description
    FROM outbound_query_helper o, iana_service_ports_import ianap
    WHERE o.destination_port = TRY_CAST(ianap.portnumber AS integer)) AS outbound_connections_results0 LEFT OUTER
JOIN hostname_ip_helper hip1
    ON outbound_connections_results0.source_ip = hip1.ip_address LEFT OUTER
JOIN hostname_ip_helper hip2
    ON outbound_connections_results0.destination_ip = hip2.ip_address
```

This query gets information about inbound traffic for each service, along
with the port number and process details.

Before running this query, if you have not already done so, you must
create the `iana_service_ports_import` table that contains the
IANA port registry database downloaded from IANA. For information about how
to create this table, see [Creating the IANA port registry import
table](#pq-create-iana-import-table "#pq-create-iana-import-table").

After the `iana_service_ports_import` table is created, create
two view helper functions for tracking inbound traffic. For information
about how to create a view, see [CREATE VIEW](../../../athena/latest/ug/create-view.md "../../../athena/latest/ug/create-view.md") in the _Amazon Athena User Guide_.

###### To create import tracking helper functions

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. Create the `valid_inbound_ips_helper` view, using the
   following helper function that lists all distinct inbound source IP
   addresses.

```
CREATE OR REPLACE VIEW valid_inbound_ips_helper AS
SELECT DISTINCT "source_ip"
FROM inbound_connection_agent;
```

3. Create the `inbound_query_helper` view, using the
   following helper function that determines the frequency of
   communication for inbound traffic.

```
CREATE OR REPLACE VIEW inbound_query_helper AS
SELECT "agent_id" ,
         "source_ip" ,
         "destination_ip" ,
         "destination_port" ,
         "agent_assigned_process_id" ,
         "count"(*) "frequency"
FROM inbound_connection_agent
WHERE (("ip_version" = 'IPv4')
        AND ("source_ip" IN
    (SELECT *
    FROM valid_inbound_ips_helper )))
GROUP BY  "agent_id", "source_ip", "destination_ip", "destination_port", "agent_assigned_process_id";
```

4. After you create the `iana_service_ports_import` table
   and your two helper functions, you can run the following query to
   get the details on the inbound traffic for each service, along with
   the port number and process details.

```
SELECT hip1.host_name "Source Host Name",
         inbound_connections_results0.source_ip "Source IP Address",
         hip2.host_name "Destination Host Name",
         inbound_connections_results0.destination_ip "Destination IP Address",
         inbound_connections_results0.frequency "Connection Frequency",
         inbound_connections_results0.destination_port "Destination Communication Port",
         inbound_connections_results0.servicename "Process Service Name",
         inbound_connections_results0.description "Process Service Description"
FROM
    (SELECT DISTINCT i.source_ip,
         i.destination_ip,
         i.frequency,
         i.destination_port,
         ianap.servicename,
         ianap.description
    FROM inbound_query_helper i, iana_service_ports_import ianap
    WHERE i.destination_port = TRY_CAST(ianap.portnumber AS integer)) AS inbound_connections_results0 LEFT OUTER
JOIN hostname_ip_helper hip1
    ON inbound_connections_results0.source_ip = hip1.ip_address LEFT OUTER
JOIN hostname_ip_helper hip2
    ON inbound_connections_results0.destination_ip = hip2.ip_address
```

This query identifies the running software based on port numbers.

Before running this query, if you have not already done so, you must
create the `iana_service_ports_import` table that contains the
IANA port registry database downloaded from IANA. For information about how
to create this table, see [Creating the IANA port registry import
table](#pq-create-iana-import-table "#pq-create-iana-import-table").

Run the following query to identify the running software based on port
numbers.

```
SELECT o.host_name "Host Name",
       ianap.servicename "Service",
       ianap.description "Description",
       con.destination_port,
       con.cnt_dest_port "Destination Port Count"
FROM   (SELECT agent_id,
               destination_ip,
               destination_port,
               Count(destination_port) cnt_dest_port
        FROM   inbound_connection_agent
        GROUP  BY agent_id,
                  destination_ip,
                  destination_port) con,
       (SELECT agent_id,
               host_name,
               Max("timestamp")
        FROM   os_info_agent
        GROUP  BY agent_id,
                  host_name) o,
       iana_service_ports_import ianap
WHERE  ianap.transportprotocol = 'tcp'
       AND con.destination_ip NOT LIKE '172%'
       AND con.destination_port = ianap.portnumber
       AND con.agent_id = o.agent_id
ORDER BY cnt_dest_port DESC;
```

## Creating the IANA port registry import

table

Some of the predefined queries require a table named
`iana_service_ports_import` that contains information downloaded from
Internet Assigned Numbers Authority (IANA).

###### To create the iana_service_ports_import table

1. Download the IANA port registry database **CSV** file
   from [Service Name and Transport Protocol Port Number Registry](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml "https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml") on
   _iana.org_.
2. Upload the file to Amazon S3. For more information, see [How Do I Upload Files and Folders
   to an S3 Bucket?](../../../AmazonS3/latest/userguide/upload-objects.md "../../../AmazonS3/latest/userguide/upload-objects.md").
3. Create a new table in Athena named `iana_service_ports_import`.
   For instructions, see [Create a
   Table](../../../athena/latest/ug/getting-started.md#step-2-create-a-table "../../../athena/latest/ug/getting-started.md#step-2-create-a-table") in the _Amazon Athena User Guide_. In the
   following example, you need to replace `my_bucket_name` with the
   name of the S3 bucket that you uploaded the CSV file to in the previous
   step.

```
CREATE EXTERNAL TABLE IF NOT EXISTS iana_service_ports_import (
         ServiceName STRING,
         PortNumber INT,
         TransportProtocol STRING,
         Description STRING,
         Assignee STRING,
         Contact STRING,
         RegistrationDate STRING,
         ModificationDate STRING,
         Reference STRING,
         ServiceCode STRING,
         UnauthorizedUseReported STRING,
         AssignmentNotes STRING
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = ',',
  'quoteChar' = '"',
  'field.delim' = ','
) LOCATION 's3://`my_bucket_name`/'
TBLPROPERTIES ('has_encrypted_data'='false',"skip.header.line.count"="1");
```

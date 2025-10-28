For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Creating partition keys for

existing tables

If you already have tables in Timestream for LiveAnalytics and want to use customer-defined partition keys, you
will need to migrate your data into a new table with the desired partitioning schema
definition. This can be done using export to S3 and batch load together, which involves
exporting the data from the existing table to S3, modifying the data to include the
partition key (if necessary) and adding headers to your CSV files, and then importing
the data into a new table with the desired partitioning schema defined. Keep in mind
that this method can be time consuming and costly, especially for large tables.

Alternatively, you can use scheduled queries to migrate your data to a new table with
the desired partitioning schema. This method involves creating a scheduled query that
reads from the existing table and writes to the new table. The scheduled query can be
set up to run on a regular basis until all the data has been migrated. Keep in mind that
you will be charged for reading and writing the data during the migration
process.

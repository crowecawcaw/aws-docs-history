# Tutorial: Loading data into Amazon Keyspaces using cqlsh

This tutorial guides you through the process of migrating data from Apache Cassandra to Amazon Keyspaces using the `cqlsh COPY FROM` command.
The `cqlsh COPY FROM` command is useful to quickly and easily upload small datasets to Amazon Keyspaces for academic or test purposes.
For more information about how to migrate production workloads, see [Offline migration process: Apache Cassandra to Amazon Keyspaces](migrating-offline.md "migrating-offline.md").
In this tutorial, you'll complete the following steps:

Prerequisites – Set up an AWS account with credentials, create a JKS trust store file for the
certificate, and configure `cqlsh` to connect to Amazon Keyspaces.

1. **Create source CSV and target table** – Prepare a CSV file
   as the source data and create the target keyspace and table in Amazon Keyspaces.
2. **Prepare the data** – Randomize the data in the CSV file
   and analyze it to determine the average and maximum row sizes.
3. **Set throughput capacity** – Calculate the required write capacity
   units (WCUs) based on the data size and desired load time, and configure the table's provisioned capacity.
4. **Configure cqlsh parameters** – Determine optimal values for `cqlsh COPY FROM`
   parameters like `INGESTRATE`, `NUMPROCESSES`, `MAXBATCHSIZE`, and `CHUNKSIZE` to distribute the workload evenly.
5. **Run the `cqlsh COPY FROM` command** – Run the `cqlsh COPY FROM` command to
   upload the data from the CSV file to the Amazon Keyspaces table, and monitor the progress.
   Troubleshooting – Resolve common issues like invalid requests, parser errors, capacity errors, and cqlsh errors during the data upload process.

###### Topics

- [Prerequisites: Steps to complete before you can upload data using cqlsh COPY FROM](bulk-upload-prequs.md "bulk-upload-prequs.md")
- [Step 1: Create the source CSV file and a target table for the data upload](bulk-upload-source.md "bulk-upload-source.md")
- [Step 2: Prepare the source data for a successful data upload](bulk-upload-prepare-data.md "bulk-upload-prepare-data.md")
- [Step 3: Set throughput capacity for the
  table](bulk-upload-capacity.md "bulk-upload-capacity.md")
- [Step 4: Configure cqlsh COPY FROM
  settings](bulk-upload-config.md "bulk-upload-config.md")
- [Step 5: Run the cqlsh COPY FROM command to upload data from the CSV file to the target table](bulk-upload-run.md "bulk-upload-run.md")
- [Troubleshooting](bulk-upload-troubleshooting.md "bulk-upload-troubleshooting.md")

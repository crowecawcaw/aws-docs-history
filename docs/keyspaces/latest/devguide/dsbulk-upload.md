# Tutorial: Loading data into Amazon Keyspaces using DSBulk

This step-by-step tutorial guides you through migrating data from Apache Cassandra to
Amazon Keyspaces using the DataStax Bulk Loader (DSBulk) available on [GitHub](https://github.com/datastax/dsbulk.git "https://github.com/datastax/dsbulk.git"). Using DSBulk is useful to
upload datasets to Amazon Keyspaces for academic or test purposes. For more information about how to
migrate production workloads, see [Offline migration process: Apache Cassandra to Amazon Keyspaces](migrating-offline.md "migrating-offline.md"). In this tutorial, you
complete the following steps.

Prerequisites – Set up an AWS account with credentials, create a JKS trust store file for the
certificate, configure `cqlsh`, download and install DSBulk, and configure an `application.conf` file.

1. **Create source CSV and target table** – Prepare a CSV file
   as the source data and create the target keyspace and table in Amazon Keyspaces.
2. **Prepare the data** – Randomize the data in the CSV file
   and analyze it to determine the average and maximum row sizes.
3. **Set throughput capacity** – Calculate the required write capacity
   units (WCUs) based on the data size and desired load time, and configure the table's provisioned capacity.
4. **Configure DSBulk settings** – Create a DSBulk configuration file with settings
   like authentication, SSL/TLS, consistency level, and connection pool size.
5. **Run the DSBulk load command** – Run the DSBulk load command to
   upload the data from the CSV file to the Amazon Keyspaces table, and monitor the progress.

###### Topics

- [Prerequisites: Steps you have to complete before you can upload data with DSBulk](dsbulk-upload-prequs.md "dsbulk-upload-prequs.md")
- [Step 1: Create the source CSV file and a target table for the data upload using DSBulk](dsbulk-upload-source.md "dsbulk-upload-source.md")
- [Step 2: Prepare the data to upload using DSBulk](dsbulk-upload-prepare-data.md "dsbulk-upload-prepare-data.md")
- [Step 3: Set the throughput capacity for the target table](dsbulk-upload-capacity.md "dsbulk-upload-capacity.md")
- [Step 4: Configure DSBulk
  settings to upload data from the CSV file to the target table](dsbulk-upload-config.md "dsbulk-upload-config.md")
- [Step 5: Run the DSBulk load
  command to upload data from the CSV file to the target table](dsbulk-upload-run.md "dsbulk-upload-run.md")

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Preparation

Data migration for InfluxDB is accomplished with a Python script that utilizes InfluxDB CLI features and the InfluxDB v2 API. Execution of the migration script requires the following environment configuration:

- **Supported Versions:** A minimum version of 2.3 of InfluxDB and Influx CLI is supported.
- **Token Environment Variables**
  - Create the environment variable `INFLUX_SRC_TOKEN` containing the token for your source InfluxDB instance.
  - Create the environment variable `INFLUX_DEST_TOKEN` containing the token for your destination InfluxDB instance.

- **Python 3**
  - Check installation: `python3 --version`.
  - If not installed, install from the Python website. Minimum version 3.7 required. On Windows the default Python 3 alias is simply python.
  - The Python module requests is required. Install it with: `shell python3 -m pip install requests`
  - TThe Python module influxdb_client is required. Install it with: `shell python3 -m pip install influxdb_client`

- **InfluxDB CLI**
  - Confirm installation: `influx version`.
  - If not installed, follow the installation guide in the [InfluxDB documentation](https://docs.influxdata.com/influxdb/cloud/tools/influx-cli/#install-the-influx-cli "https://docs.influxdata.com/influxdb/cloud/tools/influx-cli/#install-the-influx-cli").

  Add influx to your $PATH.

- **S3 Mounting Tools (Optional)**

When S3 mounting is used, all backup files are stored in a user-defined S3 bucket.
S3 mounting can be useful to save space on the executing machine or when backup files need to be shared.
If S3 mounting isn't used, by omitting the `--s3-bucket` option, then a local `influxdb-backup-<millisecond timestamp>`
directory will be created to store backup files in the same directory that the script was run.

For Linux: [mountpoint-s3](https://github.com/awslabs/mountpoint-s3 "https://github.com/awslabs/mountpoint-s3").

For Windows: [rclone](https://rclone.org/ "https://rclone.org/") (Prior rclone configuration is needed).

- **Disk Space**
  - The migration process automatically creates unique directories to store sets of backup files and retains these backup directories in either S3 or on the local filesystem, depending on the program arguments provided.
  - Ensure there is enough disk space for database backup, ideally double the size of the existing
    InfluxDB database if you choose to omit the `--s3-bucket` option and use local storage for backup and restoration.
  - Check space with `df -h (UNIX/Linux)` or by checking drive properties on Windows.

- **Direct Connection**

Ensure a direct network connection exists between the system running the migration script and the source and destination systems. `influx ping --host <host>` is one way to verify a direct connection.

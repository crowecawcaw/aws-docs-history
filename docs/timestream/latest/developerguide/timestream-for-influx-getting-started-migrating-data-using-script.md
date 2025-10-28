For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# How to use scripts

A simple example of running the script is the command:

```
python3 influx_migration.py --src-host <source host> --src-bucket <source bucket> --dest-host <destination host>

```

Which migrates a single bucket.

All options can be viewed by running:

```
python3 influx_migration.py -h

```

**Usage**

```
shell   influx_migration.py [-h] [--src-bucket SRC_BUCKET] [--dest-bucket DEST_BUCKET] [--src-host SRC_HOST] --dest-host DEST_HOST [--full] [--confirm-full] [--src-org SRC_ORG] [--dest-org DEST_ORG] [--csv] [--retry-restore-dir RETRY_RESTORE_DIR] [--dir-name DIR_NAME] [--log-level LOG_LEVEL] [--skip-verify] [--s3-bucket S3_BUCKET]
```

**Options**

- **-confirm-full** (optional): Using `--full` without `--csv` will replace all tokens, users, buckets,
  dashboards, and any other key-value data in the destination database with the tokens, users, buckets, dashboards,
  and any other key-value data in the source database. `--full` with `--csv` only migrates all bucket and bucket metadata,
  including bucket organizations. This option (`--confirm-full`) will confirm a full migration and proceed without user input.
  If this option is not provided, and `--full` has been provided and `--csv` not provided, then the script will pause for
  execution and wait for user confirmation. This is a critical action, proceed with caution. Defaults to false.
- **-csv** (optional): Whether to use csv files for backing up and restoring. If
  `--full` is passed as well then all user-defined buckets in all organizations will be migrated, not system buckets, users, tokens, or dashboards.
  If a singular organization is desired for all buckets in the destination server instead of their already-existing source organizations,
  use `--dest-org`.
- **-dest-bucket DEST_BUCKET** (optional): The name of the InfluxDB bucket in the destination server, must not be an already existing bucket. Defaults to value of `--src-bucket` or `None`
  if `--src-bucket` not provided.
- **-dest-host DEST_HOST**: The host for the destination server. Example: http://localhost:8086.
- **-dest-org DEST_ORG** (optional): The name of the organization to restore buckets to in the destination server. If this is omitted, then all migrated buckets from the source server will retain their original organization and migrated buckets may not be visible in the destination server without creating and switching organizations. This value will be used in all forms of restoration whether a single bucket, a full migration, or any migration using csv files for backup and restoration.
- **-dir-name DIR_NAME** (optional): The name of the backup directory to create. Defaults to `influxdb-backup-<timestamp>`.
  Must not already exist.
- **-full** (optional): Whether to perform a full restore, replacing all data on destination server with all data from source server from all organizations, including all key-value data such as tokens, dashboards, users, etc.
  Overrides `--src-bucket` and `--dest-bucket`. If used with `--csv`, only migrates data and metadata of buckets. Defaults to false.
- **h, --help**: Shows help message and exits.
- **-log-level LOG_LEVEL**(optional): The log level to be used during execution. Options are debug, error, and info. Defaults to info.
- **-retry-restore-dir RETRY_RESTORE_DIR**(optional): Directory to use for restoration when a previous restore failed, will skip backup and directory creation, will fail if the directory doesn't exist, can be a directory within an S3 bucket.
  If a restoration fails, the backup directory path that can be used for restoration will be indicated relative to the current directory.
  S3 buckets will be in the form `influxdb-backups/<s3 bucket>/<backup directory>`. The default backup directory name is `influxdb-backup-<timestamp>`.
- **-s3-bucket S3_BUCKET**(optional): The name of the S3 bucket to use to store backup files.
  On Linux this is simply the name of the S3 bucket, such as `amzn-s3-demo-bucket1`, given `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
  environment variables have been set or `${HOME}/.aws/credentials` exists. On Windows, this is the `rclone`
  configured remote and bucket name, such as `my-remote:amzn-s3-demo-bucket1`. All backup files will be left in the S3 bucket after migration in a
  created `influxdb-backups-<timestamp>` directory. A temporary mount directory named `influx-backups` will be created
  in the directory from where this script is ran. If not provided, then all backup files will be stored locally in a created
  `influxdb-backups-<timestamp>` directory from where this script is run.
- **-skip-verify**(optional): Skip TLS certificate verification.
- **-src-bucket SRC_BUCKET**(optional): The name of the InfluxDB bucket in the source server. If not provided, then `--full`
  must be provided.
- **-src-host SRC_HOST**(optional): The host for the source server. Defaults to http://localhost:8086.
  As noted previously, `mountpoint-s3` and `rclone` are needed if `--s3-bucket` is to be used,
  but can be ignored if the user doesn't provide a value for `--s3-bucket`, in which case backup files will be stored in a
  unique directory locally.

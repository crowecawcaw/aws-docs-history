# Step 1: Set up the Amazon S3 bucket and Fluent Bit configuration

Create an Amazon S3 bucket to store the uploaded log files and the Fluent
Bit configuration that each instance downloads at boot. The Amazon S3 bucket
organizes content under two prefixes. The `ecs-logs/`
prefix stores the compressed log files that each instance uploads, organized by instance
ID. The `fluent-bit/` prefix stores the configuration files that each
instance downloads at boot time.

You upload the Fluent Bit configuration files to the
`fluent-bit/` prefix. These include the main configuration, parser
definitions, and Lua redaction scripts.

Sample configuration files are available in the [companion GitHub repository](https://github.com/aws-samples/sample-batch-host-level-logs "https://github.com/aws-samples/sample-batch-host-level-logs"). We recommend that you customize these
samples for your workloads. Review and adjust the input sources, redaction
patterns, and upload intervals to match your requirements.

AWS Console

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**.
3. For **Bucket name**, enter a unique name
   for your bucket (for example,
   `host-level-logs-bucket`).
4. Keep **Block all public access**
   enabled.
5. Under **Default encryption**, keep the
   default settings or choose your preferred encryption
   type.
6. Create the bucket.
7. Open the bucket you created and choose
   **Create folder**. Enter
   `fluent-bit` as the folder name and choose
   **Create folder**.
8. Open the `fluent-bit/` folder, choose
   **Upload**, and upload the following
   configuration files from the sample repository:

   - `fluent-bit.conf`
   - `parsers.conf`
   - `redact_secret_vars.lua`
   - `redact_ecs_config.lua`
   - `redact_docker_env.lua`

AWS CLI
Run the following commands to create the bucket and upload the
configuration files:

```
aws s3 mb s3://`host-level-logs-bucket`

aws s3api put-public-access-block \
    --bucket `host-level-logs-bucket` \
    --public-access-block-configuration \
    "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=true,RestrictPublicBuckets=true"

aws s3 cp fluent-bit.conf s3://`host-level-logs-bucket`/fluent-bit/
aws s3 cp parsers.conf s3://`host-level-logs-bucket`/fluent-bit/
aws s3 cp redact_secret_vars.lua s3://`host-level-logs-bucket`/fluent-bit/
aws s3 cp redact_ecs_config.lua s3://`host-level-logs-bucket`/fluent-bit/
aws s3 cp redact_docker_env.lua s3://`host-level-logs-bucket`/fluent-bit/
```

After the configuration is uploaded, Fluent Bit organizes log output
using the following Amazon S3 key structure:

```
s3://`host-level-logs-bucket`/ecs-logs/`instance-id`/`source-tag`/YYYY/MM/DD/HHMM-`uuid`.log.gz
```

Each instance writes to a folder identified by its instance ID. Within that folder,
logs are organized by source tag (for example, `ecs-agent`,
`docker`, `kernel`) and further partitioned by date and
time.

Customize the configuration by removing unneeded INPUT sections or adjusting
collection intervals to match your requirements.

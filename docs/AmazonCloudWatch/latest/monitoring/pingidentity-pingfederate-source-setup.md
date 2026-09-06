

# Source configuration for Ping Identity PingFederate
<a name="pingidentity-pingfederate-source-setup"></a>

## Integrating with Ping Identity PingFederate
<a name="pingidentity-pingfederate-integration"></a>

Ping Identity PingFederate integration uses Amazon S3 and Amazon SQS to ingest audit log data into CloudWatch pipelines. PingFederate is deployed on-premises and does not expose a REST API for audit log retrieval. Fluent Bit tails the JSON-formatted audit log files on the PingFederate host and delivers them to an Amazon S3 bucket. Amazon SQS notifications alert the pipeline when new log objects arrive.

## Prerequisites
<a name="pingidentity-pingfederate-prerequisites"></a>
+ An AWS account with permissions to create Amazon S3 buckets, Amazon SQS queues, and IAM roles
+ A Ping Identity PingFederate server with administrative access
+ A Linux host with Fluent Bit installed (can be the same host as PingFederate)
+ Network connectivity between the PingFederate host and AWS

## Log forwarding setup
<a name="pingidentity-pingfederate-log-forwarding"></a>

PingFederate writes audit logs to local files using Log4j2. You configure JSON-formatted output by adding JsonTemplateLayout appenders to the `log4j2.xml` configuration file. Fluent Bit tails these JSON log files and delivers them to Amazon S3. For detailed configuration instructions, see Step 5 in the following section.

## Instructions to setup Amazon S3 and Amazon SQS
<a name="pingidentity-pingfederate-s3-sqs-setup"></a>

Complete the following steps to configure the Amazon S3 and Amazon SQS infrastructure for Ping Identity PingFederate log ingestion.

### Step 1: Create Amazon S3 bucket
<a name="pingidentity-pingfederate-step1"></a>

Create an Amazon S3 bucket to store PingFederate audit logs. The bucket must reside in the same AWS Region where you plan to create the CloudWatch pipeline.

### Step 2: Create Amazon SQS queue
<a name="pingidentity-pingfederate-step2"></a>

Create an Amazon SQS queue in the same AWS Region as your Amazon S3 bucket. This queue receives notifications when new log files are added to the bucket.

### Step 3: Connect Amazon S3 to Amazon SQS
<a name="pingidentity-pingfederate-step3"></a>

Configure the Amazon S3 bucket to send event notifications for `s3:ObjectCreated:*` events to the Amazon SQS queue.

### Step 4: Configure Amazon SQS queue policy
<a name="pingidentity-pingfederate-step4"></a>

Configure the Amazon SQS queue policy to allow the Amazon S3 bucket to send messages to the queue. Apply the following policy to your Amazon SQS queue:

```
{
  "Version": "2012-10-17",
  "Id": "AllowS3ToSQS",
  "Statement": [
    {
      "Sid": "AllowS3BucketNotification",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "sqs:SendMessage",
      "Resource": "arn:aws:sqs:<region>:<account-id>:<queue-name>",
      "Condition": {
        "ArnEquals": {
          "aws:SourceArn": "arn:aws:s3:::<YOUR-BUCKET>"
        },
        "StringEquals": {
          "aws:SourceAccount": "<account-id>"
        }
      }
    }
  ]
}
```

### Step 5: Configure Ping Identity PingFederate log export and Fluent Bit
<a name="pingidentity-pingfederate-step5"></a>

Enable JSON logging on PingFederate by editing `<PF_HOME>/server/default/conf/log4j2.xml`. Add the following RollingFile appenders:

```
<RollingFile name="AdminAudit-JsonTemplateLayout"
             fileName="${sys:pf.log.dir}/admin_json.log"
             filePattern="${sys:pf.log.dir}/admin_json.%d{yyyy-MM-dd}.log"
             ignoreExceptions="false">
    <JsonTemplateLayout eventTemplateUri="${sys:pf.log4j.json.templates.uri}/admin-audit-log.json"/>
    <Policies>
        <TimeBasedTriggeringPolicy maxRandomDelay="45"/>
    </Policies>
</RollingFile>

<RollingFile name="SecurityAudit-JsonTemplateLayout"
             fileName="${sys:pf.log.dir}/audit_json.log"
             filePattern="${sys:pf.log.dir}/audit_json.%d{yyyy-MM-dd}.log"
             ignoreExceptions="false">
    <JsonTemplateLayout eventTemplateUri="${sys:pf.log4j.json.templates.uri}/runtime-audit-log.json"/>
    <Policies>
        <TimeBasedTriggeringPolicy maxRandomDelay="45"/>
    </Policies>
</RollingFile>
```

Update the Loggers section to reference the new appenders for the multiple audit loggers:

```
<Logger name="org.sourceid.websso.profiles.sp.SpAuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="org.sourceid.websso.profiles.idp.IdpAuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="org.sourceid.websso.profiles.idp.AsAuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="org.sourceid.websso.profiles.idp.ClientRegistrationAuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="org.sourceid.wstrust.log.STSAuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="com.pingidentity.sdk.logging.LoggingUtil" level="INFO" additivity="false">
    <AppenderRef ref="SecurityAudit-JsonTemplateLayout"/>
</Logger>
<Logger name="AuditLogger" level="INFO" additivity="false">
    <AppenderRef ref="AdminAudit-JsonTemplateLayout"/>
</Logger>
```

Configure Fluent Bit to collect both audit log files and deliver them to Amazon S3:

```
########################################
# SERVICE SECTION
########################################
[SERVICE]
    Flush        5
    Daemon       Off
    Log_Level    info
    storage.path /etc/fluent-bit/db/storage
    storage.sync normal
    storage.checksum off
    storage.backlog.mem_limit 10M

########################################
# INPUT SECTION - Audit Log
########################################
[INPUT]
    Name             tail
    Path             /opt/pingfederate/log/audit_json.log
    Tag              pingfederate.audit
    Read_from_Head   True
    DB               /etc/fluent-bit/db/audit_checkpoint.db
    DB.Sync          Normal
    storage.type     filesystem
    Rotate_Wait      30
    Refresh_Interval 60

########################################
# INPUT SECTION - Admin Log
########################################
[INPUT]
    Name             tail
    Path             /opt/pingfederate/log/admin_json.log
    Tag              pingfederate.admin
    Read_from_Head   True
    DB               /etc/fluent-bit/db/admin_checkpoint.db
    DB.Sync          Normal
    storage.type     filesystem
    Rotate_Wait      30
    Refresh_Interval 60

########################################
# OUTPUT SECTION
########################################
[OUTPUT]
    Name              s3
    Match             pingfederate.*
    Bucket            <YOUR-BUCKET>
    Region            <region>
    S3_Key_Format     /pingfederate/%Y/%m/%d/%H/%M/%S.log.gz
    compression       gzip
    use_put_object    On
    store_dir         /etc/fluent-bit/db/s3
    total_file_size   1M
    log_key           log
    upload_timeout    60
```

**Note**  
PingFederate writes independent log files per cluster node. You must install Fluent Bit on each node.
+ The `audit_json.log` file captures runtime authentication events (SSO, credential validation, assertion issuance).
+ The `admin_json.log` file captures administrative console activity (configuration changes, admin logins).
+ Fluent Bit delivers gzip-compressed NDJSON files to Amazon S3.
+ The `storage.type filesystem` setting ensures buffering to disk for reliability.

**Important**  
Use only the default PingFederate-provided JSON templates. Modifying the `.json` template files changes the output schema and might break downstream processing.

### Step 6: IAM permissions
<a name="pingidentity-pingfederate-step6"></a>

Create an IAM policy with the following permissions for the Fluent Bit host to write objects to the Amazon S3 bucket:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "FluentBitS3Write",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetBucketLocation",
        "s3:ListBucket",
        "s3:ListMultipartUploadParts",
        "s3:AbortMultipartUpload",
        "s3:CreateMultipartUpload",
        "s3:CompleteMultipartUpload"
      ],
      "Resource": [
        "arn:aws:s3:::<YOUR-BUCKET>",
        "arn:aws:s3:::<YOUR-BUCKET>/pingfederate/*"
      ]
    }
  ]
}
```

### Step 7: Verify
<a name="pingidentity-pingfederate-step7"></a>

Verify the setup by confirming that log files appear in the Amazon S3 bucket and that Amazon SQS notifications are being generated. Check the Amazon SQS queue for messages indicating new object creation events.

## Configuring the CloudWatch pipeline
<a name="pingidentity-pingfederate-pipeline-config"></a>
+ Choose Ping Identity PingFederate as the data source when creating the pipeline.
+ Provide the Amazon SQS queue URL and IAM role ARN.
+ Select the destination CloudWatch Logs log group.
+ After you create the pipeline, data will be available in the selected log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="pingidentity-pingfederate-ocsf-events"></a>

This integration supports OCSF schema version v1.5.0. The following table shows the mapping between PingFederate audit log types and OCSF event classes.


| Event name | OCSF event class | 
| --- | --- | 
| Security Audit (runtime authentication lifecycle) | Authentication [3002] | 
| Administrator Audit (admin login/logout) | Authentication [3002] | 
| Administrator Audit (CRUD on configuration objects) | Entity Management [3004] | 
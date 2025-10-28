# Default application configuration for EMR Serverless

You can specify a common set of runtime and monitoring configurations at the application
level for all the jobs that you submit under the same application. This reduces the additional
overhead that is associated with the need to submit the same configurations for each
job.

You can modify the configurations at the following points in time:

- [Declare application-level configurations at
  job submission.](#default-configs-declare "#default-configs-declare")
- [Override default configurations during job
  run.](#default-configs-override "#default-configs-override")
  The following sections provide more details and an example for further context.

## Declaring configurations at the application level

You can specify application-level logging and runtime configuration properties for the
jobs that you submit under the application.

**`monitoringConfiguration`**

To specify the log configurations for jobs that you submit with the application,
use the [`monitoringConfiguration`](../../../emr-serverless/latest/APIReference/API_MonitoringConfiguration.md "../../../emr-serverless/latest/APIReference/API_MonitoringConfiguration.md") field. For more information on
logging for EMR Serverless, refer to [Storing logs](logging.md "logging.md").

**`runtimeConfiguration`**

To specify runtime configuration properties such as `spark-defaults`,
provide a configuration object in the `runtimeConfiguration` field. This
affects the default configurations for all the jobs that you submit with the
application. For more information, refer to [Hive configuration override
parameter](jobs-hive.md#hive-defaults-configurationOverrides "jobs-hive.md#hive-defaults-configurationOverrides") and [Spark configuration override
parameter](jobs-spark.md#spark-defaults-configurationOverrides "jobs-spark.md#spark-defaults-configurationOverrides").

Available configuration classifications vary by specific EMR Serverless release. For
example, classifications for custom Log4j `spark-driver-log4j2` and
`spark-executor-log4j2` are only available with releases 6.8.0 and higher. For
a list of application-specific properties, refer to [Spark job properties](jobs-spark.md#spark-defaults "jobs-spark.md#spark-defaults") and [Hive job properties](jobs-hive.md#hive-defaults "jobs-hive.md#hive-defaults").

You can also configure [Apache Log4j2 properties](log4j2.md "log4j2.md"), [AWS Secrets Manager for data protection](secrets-manager.md "secrets-manager.md"), and [Java 17 runtime](using-java-runtime.md "using-java-runtime.md") at the application level.

To pass Secrets Manager secrets at the application level, attach the following policy to
users and roles that need to create or update EMR Serverless applications with
secrets.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "SecretsManagerPolicy",
 "Effect": "Allow",
 "Action": [
 "secretsmanager:GetSecretValue",
 "secretsmanager:DescribeSecret"
 ],
 "Resource": [
 "arn:aws:secretsmanager:us-east-1:123456789012:secret:my-secret-name-123abc"
 ]
 },
 {
 "Sid": "KMSDecryptPolicy",
 "Effect": "Allow",
 "Action": [
 "kms:Decrypt"
 ],
 "Resource": [
 "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
 ]
 }
 ]
}`

```

For more information on creating custom policies for secrets, refer to [Permissions policy examples for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access_examples.md "../../../secretsmanager/latest/userguide/auth-and-access_examples.md") in the _AWS Secrets Manager User
Guide_.

###### Note

The `runtimeConfiguration` that you specify at application level maps to
`applicationConfiguration` in the [`StartJobRun`](../../../emr-serverless/latest/APIReference/API_StartJobRun.md "../../../emr-serverless/latest/APIReference/API_StartJobRun.md") API.

### Example declaration

The following example shows how to declare default configurations with
`create-application`.

```
aws emr-serverless create-application \
    --release-label `release-version`  \
    --type SPARK \
    --name `my-application-name` \
    --runtime-configuration '[
        {
            "classification": "spark-defaults",
            "properties": {
                "spark.driver.cores": "4",
                "spark.executor.cores": "2",
                "spark.driver.memory": "8G",
                "spark.executor.memory": "8G",
                "spark.executor.instances": "2",
                "spark.hadoop.javax.jdo.option.ConnectionDriverName":"org.mariadb.jdbc.Driver",
                "spark.hadoop.javax.jdo.option.ConnectionURL":"jdbc:mysql://`db-host`:`db-port`/`db-name`",
                "spark.hadoop.javax.jdo.option.ConnectionUserName":"`connection-user-name`",
                "spark.hadoop.javax.jdo.option.ConnectionPassword": "EMR.secret@`SecretID`"
            }
        },
        {
            "classification": "spark-driver-log4j2",
            "properties": {
                "rootLogger.level":"error",
                "logger.IdentifierForClass.name": "`classpathForSettingLogger`",
                "logger.IdentifierForClass.level": "info"
            }
        }
    ]' \
    --monitoring-configuration '{
        "s3MonitoringConfiguration": {
            "logUri": "s3://`amzn-s3-demo-logging-bucket`/logs/app-level"
        },
        "managedPersistenceMonitoringConfiguration": {
            "enabled": false
        }
    }'
```

## Overriding configurations during a job

run

You can specify configuration overrides for the application configuration and monitoring
configuration with the [`StartJobRun`](../../../emr-serverless/latest/APIReference/API_StartJobRun.md "../../../emr-serverless/latest/APIReference/API_StartJobRun.md") API. EMR Serverless then merges the configurations that
you specify at the application level and the job level to determine the configurations for
the job execution.

The granularity level when the merge occurs is as follows:

- **[`ApplicationConfiguration`](../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-applicationConfiguration "../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-applicationConfiguration")** - Classification type,
  for example `spark-defaults`.
- **[`MonitoringConfiguration`](../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-monitoringConfiguration "../../../emr-serverless/latest/APIReference/API_ConfigurationOverrides.md#emrserverless-Type-ConfigurationOverrides-monitoringConfiguration")** - Configuration type, for
  example `s3MonitoringConfiguration`.

###### Note

The priority of configurations that you provide at [`StartJobRun`](../../../emr-serverless/latest/APIReference/API_StartJobRun.md "../../../emr-serverless/latest/APIReference/API_StartJobRun.md") supersede the configurations that you provide at the
application level.

For more information priority
rankings, refer to [Hive configuration override
parameter](jobs-hive.md#hive-defaults-configurationOverrides "jobs-hive.md#hive-defaults-configurationOverrides") and [Spark configuration override
parameter](jobs-spark.md#spark-defaults-configurationOverrides "jobs-spark.md#spark-defaults-configurationOverrides").

When you start a job, if you don’t specify a particular configuration, it will be
inherited from the application. If you declare the configurations at job level, you can
perform the following operations:

- **Override an existing configuration** - Provide the
  same configuration parameter in the `StartJobRun` request with your override
  values.
- **Add an additional configuration** - Add the new
  configuration parameter in the `StartJobRun` request with the values that you
  want to specify.
- **Remove an existing configuration** - To remove an
  application _runtime configuration_, provide the key for the
  configuration that you want to remove, and pass an empty declaration `{}` for
  the configuration. We don't recommend removing any classifications that contain
  parameters that are required for a job run. For example, if you try to remove the required properties for a Hive job,
  the job will fail.

To remove an application _monitoring configuration_, use the
appropriate method for the relevant configuration type:

    + **`cloudWatchLoggingConfiguration`** -
     To remove `cloudWatchLogging`, pass the enabled flag as
     `false`.
    + **`managedPersistenceMonitoringConfiguration`** - To remove
     managed persistence settings and fall back to the default enabled state, pass an
     empty declaration `{}` for the configuration.
    + **`s3MonitoringConfiguration`** - To
     remove `s3MonitoringConfiguration`, pass an empty declaration
     `{}` for the configuration.

### Example override

The following example shows different operations you can perform during job submission
at `start-job-run`.

```
aws emr-serverless start-job-run \
    --application-id `your-application-id` \
    --execution-role-arn `your-job-role-arn` \
    --job-driver '{
        "sparkSubmit": {
            "entryPoint": "s3://`us-east-1`.elasticmapreduce/emr-containers/samples/wordcount/scripts/wordcount.py",
            "entryPointArguments": ["s3://`amzn-s3-demo-destination-bucket1`/wordcount_output"]
        }
    }' \
    --configuration-overrides '{
        "applicationConfiguration": [
            {
                // Override existing configuration for spark-defaults in the application
                "classification": "spark-defaults",
                "properties": {
                    "spark.driver.cores": "2",
                    "spark.executor.cores": "1",
                    "spark.driver.memory": "4G",
                    "spark.executor.memory": "4G"
                }
            },
            {
                // Add configuration for spark-executor-log4j2
                "classification": "spark-executor-log4j2",
                "properties": {
                    "rootLogger.level": "error",
                    "logger.IdentifierForClass.name": "`classpathForSettingLogger`",
                    "logger.IdentifierForClass.level": "info"
                }
            },
            {
                // Remove existing configuration for spark-driver-log4j2 from the application
                "classification": "spark-driver-log4j2",
                "properties": {}
            }
        ],
        "monitoringConfiguration": {
            "managedPersistenceMonitoringConfiguration": {
                // Override existing configuration for managed persistence
                "enabled": true
            },
            "s3MonitoringConfiguration": {
                // Remove configuration of S3 monitoring
            },
            "cloudWatchLoggingConfiguration": {
                // Add configuration for CloudWatch logging
                "enabled": true
            }
        }
    }'
```

At the time of job execution, the following classifications and configurations will
apply based on the priority override ranking described in [Hive configuration override
parameter](jobs-hive.md#hive-defaults-configurationOverrides "jobs-hive.md#hive-defaults-configurationOverrides") and [Spark configuration override
parameter](jobs-spark.md#spark-defaults-configurationOverrides "jobs-spark.md#spark-defaults-configurationOverrides").

- The classification `spark-defaults` will be updated with the properties
  specified at the job level. Only the properties included in `StartJobRun`
  is considered for this classification.
- The classification `spark-executor-log4j2` will be added in the
  existing list of classifications.
- The classification `spark-driver-log4j2` will be removed.
- The configurations for `managedPersistenceMonitoringConfiguration` will
  be updated with configurations at job level.
- The configurations for `s3MonitoringConfiguration` will be removed.
- The configurations for `cloudWatchLoggingConfiguration` will be added
  to existing monitoring configurations.



# Managing Web Function revisions
<a name="web-functions-revisions"></a>

A revision is an immutable snapshot of your Web Function application code and configuration. To change your code or any revision setting, such as `timeoutSeconds`, `maxConcurrencyPerEnvironment`, or `environmentVariables`, you create a new revision. Whether the new revision receives traffic depends on each endpoint's auto-deployment mode. An endpoint in **LatestRevision** mode routes all traffic to the new revision after it becomes **Active**. An endpoint in **Disabled** mode keeps its current revision weights until you change them. Because revisions are immutable, you can roll back by routing traffic to an earlier revision. The earlier revision must remain **Active**, and its code, key, role, and other dependencies must remain available. For information about routing traffic between revisions, see [Deployment patterns](web-functions-deployment.md).

## Revision properties
<a name="web-functions-revisions-properties"></a>

Each revision contains the following configuration:


| Property | Description | Default | Changeable | 
| --- | --- | --- | --- | 
| revisionId | A unique ID that Lambda generates when you create the revision. | – | No (generated) | 
| revisionArn | The Amazon Resource Name (ARN) of the revision. | – | No (generated) | 
| functionArn | The ARN of the Web Function that the revision belongs to. | – | No (generated) | 
| state | The lifecycle state of the revision (Pending, Active, or Failed). For details, see [Revision states](web-functions-how-it-works.md#web-functions-revision-states). | – | No (managed by Lambda) | 
| stateReason | A description of why the revision is in its current state, for example the cause of a Failed state. | – | No (managed by Lambda) | 
| errors | A list of errors that Lambda found while creating or reading the revision. Each error names the affected attribute and includes an error code and a message. Absent when the revision has no errors. | – | No (managed by Lambda) | 
| createdAt | The timestamp when the revision was created. | – | No (generated) | 
| description | An optional description for the revision that you provide when you create it. | None | No (immutable) | 
| buildConfig | The code and runtime for the revision. Contains the codeConfig and runtimeConfig settings described in the following rows. | – | No (immutable) | 
| codeConfig | The location of the deployment package. Contains the s3Object setting described in the following rows. Part of buildConfig. | – | No (immutable) | 
| s3Object | The Amazon S3 location of the deployment package. Contains the bucket, key, and versionId settings described in the following rows. For details, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md). Part of codeConfig. | – | No (immutable) | 
| bucket | The name of the Amazon S3 bucket that contains the deployment package. The bucket must have S3 versioning enabled. Part of s3Object. | – | No (immutable) | 
| key | The Amazon S3 object key of the deployment package. Part of s3Object. | – | No (immutable) | 
| versionId | The version ID of the Amazon S3 object. Optional. If you omit it, Lambda uses the latest version of the object at creation time. Either way, Lambda pins the revision to a specific object version. Part of s3Object. | Latest version | No (immutable) | 
| runtimeConfig | The runtime configuration. Contains the runtime setting described in the following row. Part of buildConfig. | – | No (immutable) | 
| runtime | The runtime identifier (for example, nodejs24.x). For supported runtimes, see [Lambda Web Function runtimes](web-functions-runtimes.md). Although the runtime identifier is fixed for the revision, the runtime itself is not frozen. Lambda automatically applies security patches and bug fixes to the runtime, so the identifier (for example, nodejs24.x) always resolves to the latest patched version. For details, see [Automatic runtime patching](web-functions-runtimes.md#web-functions-runtimes-patching). Part of runtimeConfig. | – | No (immutable) | 
| serviceConfig | The runtime settings for the revision. Contains the executionRoleArn, timeoutSeconds, maxConcurrencyPerEnvironment, environmentVariables, and telemetryConfig settings described in the following rows. | – | No (immutable) | 
| executionRoleArn | The ARN of the IAM role that the Web Function assumes at runtime. The role grants permissions to access AWS services and resources. Required. For details, see [Execution role](web-functions-permissions.md#web-functions-permissions-execution-role). Part of serviceConfig. | – | No (immutable) | 
| timeoutSeconds | The maximum time in seconds that a single HTTP request can run. Valid values: 3–900. Part of serviceConfig. | 30 | No (immutable) | 
| maxConcurrencyPerEnvironment | The maximum number of concurrent HTTP requests per execution environment. Valid values: 1–128. Part of serviceConfig. | 64 | No (immutable) | 
| environmentVariables | Key-value pairs available to your application at runtime. Set per-revision and immutable after creation. Part of serviceConfig. | None | No (immutable) | 
| telemetryConfig | Telemetry settings for the revision. Contains the loggingConfig setting described in the following rows. If you omit telemetryConfig, Lambda still sends your application logs to the default log group. Part of serviceConfig. | None | No (immutable) | 
| loggingConfig | The logging configuration for the revision. Contains the logGroup, applicationLogLevel, and systemLogLevel settings described in the following rows. For details, see [Logging controls](web-functions-logging.md#web-functions-logging-format-levels). Part of telemetryConfig. | None | No (immutable) | 
| logGroup | The Amazon CloudWatch Logs log group that receives your logs. Log group names that start with aws/ are reserved and rejected. For details, see [Using a custom log group](web-functions-logging.md#web-functions-logging-custom-group). Part of loggingConfig. | /aws/lambda/web/{{function-name}} | No (immutable) | 
| applicationLogLevel | The minimum severity of your application's logs that Lambda sends to Amazon CloudWatch Logs. Valid values: TRACE, DEBUG, INFO, WARN, ERROR, and FATAL. Part of loggingConfig. | INFO | No (immutable) | 
| systemLogLevel | The minimum severity of Lambda-generated system logs that Lambda sends to Amazon CloudWatch Logs. Valid values: DEBUG, INFO, and WARN. Part of loggingConfig. | INFO | No (immutable) | 
| kmsKeyArn | The ARN of the customer managed key used to encrypt code and environment variables. Optional. If a MultiRegion or PerRegion endpoint routes traffic to the revision, use a multi-Region key with a replica in each of the endpoint's Regions. For details, see [Encryption at rest for Web Functions](web-functions-encryption.md). | None | No (immutable) | 

All revision properties are immutable after creation. To change any configuration, create a new revision with the updated values.

## Creating a revision
<a name="web-functions-revisions-create"></a>

Lambda creates a revision when you call `CreateWebFunctionRevision`. You provide the code location and configuration in the request. A new revision doesn't copy settings from an existing revision. Specify every setting that you want to keep, including environment variables. Settings that you omit use their defaults. To start from the current values, run `get-web-function-revision` and reuse its `buildConfig` and `serviceConfig` with your changes. The new revision starts in the **Pending** state while Lambda downloads your code and prepares a code artifact from it. When preparation completes, the revision transitions to **Active**. If an error occurs during preparation, the revision transitions to **Failed** and cannot serve traffic. For details about each state, see [Revision states](web-functions-how-it-works.md#web-functions-revision-states).

Before you create a revision, upload your .zip deployment package to a versioned Amazon S3 bucket, and get the ARN of an execution role that Lambda can assume. For details, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md) and [Execution role](web-functions-permissions.md#web-functions-permissions-execution-role).

**To create a revision with updated code (AWS CLI)**

1. Run the following command to create a new revision. Replace the S3 bucket, key, role ARN, and configuration values with your own.

   ```
   aws lambda-web create-web-function-revision \
       --function-name {{my-web-app}} \
       --build-config '{
         "codeConfig": {
           "s3Object": {
             "bucket": "{{my-bucket}}",
             "key": "{{my-app-v2.zip}}"
           }
         },
         "runtimeConfig": { "runtime": "nodejs24.x" }
       }' \
       --service-config '{
         "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}"
       }'
   ```

   The command uses the following objects. For each setting and its default, see [Revision properties](#web-functions-revisions-properties).
   + `buildConfig` contains `codeConfig`, the Amazon S3 bucket and key of your deployment package, and `runtimeConfig`, the runtime (for example, `nodejs24.x`). Both are required.
   + `serviceConfig` contains the required `executionRoleArn`, the ARN of the execution role that your Web Function assumes when it runs. It can also contain `timeoutSeconds`, `maxConcurrencyPerEnvironment`, `environmentVariables`, and `telemetryConfig`.

   The command returns details about the new revision, including its `revisionId`. The revision starts in the **Pending** state.

1. To confirm that the revision is **Active**, run the following command. Replace {{my-web-app}} with your function name and {{rev-a1b2c}} with the `revisionId` from the response.

   ```
   aws lambda-web get-web-function-revision \
       --function-name {{my-web-app}} \
       --revision-id {{rev-a1b2c}}
   ```

   The revision is ready when `state` is `Active`. If `state` is `Failed`, `stateReason` describes the cause. For details, see [Revision states](web-functions-how-it-works.md#web-functions-revision-states).

   Right after you create a revision, its `state` is usually `Pending`. To wait until it's `Active`, run `aws lambda-web wait web-function-revision-active` with the same options.

**To create a revision with updated configuration (AWS CLI)**

1. To change configuration without changing code, specify the same code location with the new settings. The following example changes the timeout to 60 seconds and adds an environment variable.

   ```
   aws lambda-web create-web-function-revision \
       --function-name {{my-web-app}} \
       --build-config '{
         "codeConfig": {
           "s3Object": {
             "bucket": "{{my-bucket}}",
             "key": "{{my-app-v2.zip}}"
           }
         },
         "runtimeConfig": { "runtime": "nodejs24.x" }
       }' \
       --service-config '{
         "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}",
         "timeoutSeconds": 60,
         "maxConcurrencyPerEnvironment": 32,
         "environmentVariables": {
           "DATABASE_URL": "{{my-database-endpoint}}",
           "LOG_LEVEL": "info"
         }
       }'
   ```

1. To confirm that the revision is **Active**, run the following command. Replace {{my-web-app}} with your function name and {{rev-a1b2c}} with the `revisionId` from the response.

   ```
   aws lambda-web get-web-function-revision \
       --function-name {{my-web-app}} \
       --revision-id {{rev-a1b2c}}
   ```

   The revision is ready when `state` is `Active`. If `state` is `Failed`, `stateReason` describes the cause. For details, see [Revision states](web-functions-how-it-works.md#web-functions-revision-states).

   Right after you create a revision, its `state` is usually `Pending`. To wait until it's `Active`, run `aws lambda-web wait web-function-revision-active` with the same options.

After creating the revision, how traffic reaches it depends on the endpoint's auto-deployment mode. For details, see [Deployment patterns](web-functions-deployment.md).

## Listing revisions
<a name="web-functions-revisions-list"></a>

To view all revisions for a Web Function, use the following command:

```
aws lambda-web list-web-function-revisions \
    --function-name {{my-web-app}}
```

The response includes each revision's identifier, state, creation timestamp, and configuration summary. Use the revision identifier when updating endpoint revision weights or when deleting a revision.

## Deleting a revision
<a name="web-functions-revisions-delete"></a>

You can delete a revision that is no longer needed. Deleting a revision permanently removes it. Your deployment package in Amazon S3 is not affected.

**Important**  
You cannot delete a revision that any endpoint routes traffic to (a revision with a non-zero weight on any endpoint). Remove the revision from the revision weights of every endpoint before deleting it.

**To delete a revision (AWS CLI)**
+ Run the following command to delete a specific revision.

  ```
  aws lambda-web delete-web-function-revision \
      --function-name {{my-web-app}} \
      --revision-id {{rev-a1b2c}}
  ```

### Revision limits and automatic cleanup
<a name="web-functions-revisions-limits"></a>

Lambda uses 50 revisions per Web Function as its automatic cleanup target. The target is not adjustable. In the Service Quotas console, it appears as **Revisions per Web Function** (`web-function-revisions-per-function`).

You don't need to delete old revisions to stay within the cleanup target. When a new revision becomes **Active** and the total revision count exceeds the cleanup target, Lambda automatically deletes the oldest revisions that are not in use. A revision is in use when any endpoint routes traffic to it, including when it's referenced anywhere in the `regionalEndpoints` property of a `MultiRegion` or `PerRegion` endpoint. Lambda doesn't automatically delete a revision that is in use or the revision that just became **Active**. Cleanup is asynchronous. The revision count might temporarily exceed 50 while older revisions are still in use or cleanup is in progress. A revision that you remove from all revision weights, such as a rollback target, can be deleted by cleanup.

You can also delete revisions manually at any time. For the procedure, see the preceding section.

Each revision's deployment package can be up to 512 MB (unzipped). Because you provide your deployment package in your own Amazon S3 bucket and Lambda references your code directly from the bucket, there is no separate code storage quota for Web Functions. For details, see [Deploying Web Function code from Amazon S3](web-functions-code-s3.md).

## Configuring revision settings
<a name="web-functions-revisions-configuration"></a>

All configuration is set per-revision and is immutable after creation. To change any setting, create a new revision with the updated values. The following settings control execution behavior.

For the request timeout and environment variable settings, see [Request timeout](web-functions-revisions-timeout.md) and [Environment variables](web-functions-revisions-env-vars.md) in [Configuring Lambda Web Functions](web-functions-configuration.md).

### Concurrency per environment
<a name="web-functions-revisions-concurrency"></a>

The `maxConcurrencyPerEnvironment` setting controls how many HTTP requests a single execution environment handles at the same time. Valid values are 1–128. The default is 64.

For I/O-bound applications (many requests waiting on database or network calls), a higher value maximizes utilization. For CPU-bound applications, a lower value reduces contention. For more guidance, see [Scaling behavior for Lambda Web Functions](web-functions-scaling.md).
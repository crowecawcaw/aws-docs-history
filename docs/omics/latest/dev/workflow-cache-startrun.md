# Using the run cache

By default, runs don't use a run cache. To use a cache for the run, you specify the run cache and the run
cache behavior when you start the run.

After a run completes, you can use the console, CloudWatch Logs, or API operations to track cache hits or troubleshoot
cache issues. For details, see [Tracking call caching information](#workflow-cache-track "#workflow-cache-track") and
[Troubleshooting call caching issues](troubleshooting.md#workflow-cache-troubleshooting "troubleshooting.md#workflow-cache-troubleshooting").

If one or more tasks in a run generate non-deterministic outputs, we strongly recommend that you don’t use
call caching for the run, or you opt out these specific tasks from caching. For more information, see
[Shared responsibility model](how-run-cache.md#run-cache-srm "how-run-cache.md#run-cache-srm").

###### Note

You provide an IAM service role when you start a run. To use call caching, the service role needs permission
to access the run cache Amazon S3 location.
For more information, see [Service roles for AWS HealthOmics](permissions-service.md "permissions-service.md").

You can use [Amazon Q CLI](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md")
to analyze and manage your run cache data. For more information, see
[Example prompts for Amazon Q CLI](getting-started.md#omics-q-prompts "getting-started.md#omics-q-prompts") and the
[HealthOmics Agentic generative AI tutorial](https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai "https://github.com/aws-samples/aws-healthomics-tutorials/tree/main/generative-ai")
on GitHub.

###### Topics

- [Configuring a run with run cache using the console](#workflow-cache-startrun-console "#workflow-cache-startrun-console")
- [Configuring a run with run cache using the CLI](#workflow-cache-startrun-api "#workflow-cache-startrun-api")
- [Error cases for run caches](#workflow-cache-errors "#workflow-cache-errors")
- [Tracking call caching information](#workflow-cache-track "#workflow-cache-track")

## Configuring a run with run cache using the console

From the console, you configure the run cache for a run when you start the run.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, choose the run to start.
4. Choose **Start run** and complete steps 1 and 2 of **Start run**
   as described in [Starting a run using the console](starting-a-run.md#starting-a-run-console "starting-a-run.md#starting-a-run-console").
5. In step 3 of **Start run**, choose **Select an existing run
   cache**.
6. Select the cache from the **Run cache ID** drop-down list.
7. To override the default run cache behavior, choose the **Cache behavior** for the
   run. For more information, see [Run cache behavior](how-run-cache.md#run-cache-behavior "how-run-cache.md#run-cache-behavior").
8. Continue to step 4 of **Start run**.

## Configuring a run with run cache using the CLI

To start a run that uses a run cache, add the cache-id parameter to the **start-run** CLI command. Optionally, use the `cache-behavior` parameter to override the
default behavior that you configured for the run cache. The following example shows only the cache fields for
the command:

```
aws omics start-run \
        ...
      --cache-id "xxxxxx"    \
      --cache-behavior  CACHE_ALWAYS

```

If the operation is successful, you receive a response with no data fields.

## Error cases for run caches

For the following scenarios, HealthOmics may not cache task outputs, even for a run with cache behavior set to
**Cache always**.

- If the run encounters an error before the first task completes successfully, there are no cache outputs
  to export.
- If the export process fails, HealthOmics doesn't save the task outputs to the Amazon S3 cache location.
- If the run fails due to a **filesystem out of space** error, call caching doesn't save
  any task outputs.
- If you cancel a run, call caching doesn't save any task outputs.
- If the run experiences a run timeout, call caching doesn't save any task outputs,
  even if you configured the run to use cache on failure.

## Tracking call caching information

You can track call caching events (such as run cache hits) using the console, the CLI, or CloudWatch Logs.

###### Topics

- [Track cache hits using the console](#workflow-cache-track-console "#workflow-cache-track-console")
- [Track call caching using the CLI](#workflow-cache-track-cli "#workflow-cache-track-cli")
- [Track call caching using CloudWatch Logs](#workflow-cache-track-cwl "#workflow-cache-track-cwl")

### Track cache hits using the console

In the run details page for a run, the **Run tasks** table displays
**Cache hit** information for each task. The table also includes a link to the
associated cache entry. Use the following procedure to view cache hit information for a run.

1. Open the [HealthOmics console](https://console.aws.amazon.com/omics/ "https://console.aws.amazon.com/omics/").
2. If required, open the left navigation pane (≡). Choose **Runs**.
3. On the **Runs** page, choose the run to inspect.
4. On the run details page, choose the **Run tasks** tab to display the tasks table.
5. If a task has a cache hit, the **Cache hit** column contains
   a link to the run cache entry location in Amazon S3.
6. Choose the link to inspect the run cache entry.

### Track call caching using the CLI

Use the **get-run** CLI command confirm whether the run used a call cache.

```
 aws omics get-run --id 1234567
```

In the response, if the `cacheId` field is set, the run uses that cache.

Use the **list-run-tasks** CLI command to retrieve the cache data location for each
cached task in the run.

```
 aws omics list-run-tasks --id 1234567
```

In the response, if the cacheHit field for a task is true, the cacheS3Uri field provides the
cache data location for that task.

You can also use the **get-run-task** CLI command to retrieve the cache data location for a
specific task:

```
 aws omics get-run-task --id 1234567 --task-id <task_id>
```

### Track call caching using CloudWatch Logs

HealthOmics creates cache activity logs in the `/aws/omics/WorkflowLog` CloudWatch log group. There is a
log stream for each run cache: **runCache/<cache_id>/<cache_uuid>**.

For runs that use call caching, HealthOmics generates CloudWatch Logs entries for these events:

- creating a cache entry (CACHE_ENTRY_CREATED)
- matching a cache entry (CACHE_HIT)
- failing to match a cache entry (CACHE_MISS)

For more information about these logs, see [Logs in CloudWatch](monitoring-cloudwatch-logs.md#cloudwatch-logs "monitoring-cloudwatch-logs.md#cloudwatch-logs") .

Use the following CloudWatch Insights query on the `/aws/omics/WorkflowLog` log group to return
the number of cache hits per run for this cache:

```
filter @logStream like 'runCache/<CACHE_ID>/'
 fields @timestamp, @message
 filter logMessage like 'CACHE_HIT'
 parse "run: *," as run
 stats count(*) as cacheHits by run
```

Use the following query to return
the number of cache entries created by each run:

```
filter @logStream like 'runCache/<CACHE_ID>/'
 fields @timestamp, @message
 filter logMessage like 'CACHE_ENTRY_CREATED'
 parse "run: *," as run
 stats count(*) as cacheEntries by run
```

AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# How call caching works

To use call caching, you create a run cache and configure it to have an associated Amazon S3 location for the
cached data. When you start a run, you specify the run cache. A run cache isn't dedicated to one workflow. Runs
from multiple workflows can use the same cache.

During the export phase of a run, the system exports the completed task outputs to the Amazon S3 location. To
export intermediate task files, declare these files as task outputs in the workflow definition. Call caching also
internally saves metadata and creates unique hashes for each cache entry.

For each task in a run, the workflow engine detects whether there is a matching cache entry for this task.
If there is no matching cache entry, HealthOmics computes the task. If there is a matching cache entry, the engine
retrieves the cached results.

To match cache entries, HealthOmics uses the hashing mechanism that's included in the native workflow engines. HealthOmics
extends these existing hash implementations to account for HealthOmics variables, such as S3 eTags and ECR container
digests.

HealthOmics supports call caching for these workflow language versions:

- WDL versions 1.0, 1.1, and the development version
- Nextflow version 23.10 and 24.10
- All CWL versions

###### Note

HealthOmics doesn't support call caching for Ready2Run workflows.

###### Topics

- [Shared responsibility model](#run-cache-srm "#run-cache-srm")
- [Caching requirements for tasks](#workflow-cache-task-prereqs "#workflow-cache-task-prereqs")
- [Run cache performance](#run-cache-performance "#run-cache-performance")
- [Cache data retention and invalidation events](#workflow-cache-data "#workflow-cache-data")

## Shared responsibility model

There is a shared responsibility between users and AWS to determine whether tasks and runs are good
candidates for call caching. Call caching achieves the best outcomes when all tasks are idempotent (repeated
executions of a task using the same inputs produce the same results).

However, if a task includes non-deterministic elements (such as random number generations or system time),
repeated executions of the task using the same inputs may result in different outputs. This can impact the
effectiveness of call caching in the following ways:

- If HealthOmics uses a cache entry (created by a previous run) that is not identical to the output that the task execution
  would produce for the current run, the run may yield different results than the same run with no
  caching.
- HealthOmics may not find a matching cache entry for a task that should match, because of non-deterministic task outputs.
  If it doesn't find the valid cache entry, the run unnecessarily recomputes the task, which reduces the cost
  saving benefits of using call caching.

The following are known task behaviors that can cause non-deterministic results that affect call caching
outcomes:

- Using random number generators.
- Dependence on the system time.
- Using concurrency (race-conditions can cause output variance).
- Fetching local or remote files beyond what is specified in the task input parameters.

For other scenarios that can cause non-deterministic behavior, see [Non-deterministic process inputs](https://www.nextflow.io/docs/latest/cache-and-resume.html#non-deterministic-process-inputs "https://www.nextflow.io/docs/latest/cache-and-resume.html#non-deterministic-process-inputs") on the Nextflow documentation site.

If you suspect that a task produces outputs that are non-deterministic, consider using workflow engine
features, such as cache opt-out in Nextflow, to avoid caching specific tasks that are
non-deterministic.

We recommend that you thoroughly review your specific workflow and task requirements before enabling call caching
in any environments in which ineffective call caching or different outputs than expected can present risk.
For example, the potential limitations of call caching should be carefully considered in determining whether
call caching is appropriate for clinical use cases.

## Caching requirements for tasks

HealthOmics caches task outputs for tasks that meet the following requirements:

- The task must define a container. HealthOmics won't cache outputs for a task with no container.
- The task must produce one or more outputs. You specify task outputs in the workflow definition.
- The workflow definition must not use dynamic values. For example, if you pass a parameter to a task with
  a value that increments with every run, HealthOmics doesn't cache the task outputs.

###### Note

If multiple tasks in a run use the same container image, HealthOmics provides the same image version to all of these
tasks. After HealthOmics pulls the image, it ignores any updates to the container image for the duration of the run.
This approach provides a predictable and consistent experience and prevents potential issues that could arise
from updates to the container image that are deployed mid-run.

## Run cache performance

When you turn on call caching for a run, you may notice the following impacts on run performance:

- During the first run, HealthOmics saves the cache data for tasks in the run. You may experience longer export times
  for this run, because call caching increases the amount of export data.
- In subsequent runs, when resuming a run from cache, it may shorten the number of processing steps and reduce your
  run time.
- If you also choose to declare intermediate files as outputs, then your export times might be even longer since
  this data can be more verbose.

## Cache data retention and invalidation events

The main purpose of a run cache is to optimize computation of tasks in the run. If there is a valid matching
cache entry for a task, HealthOmics uses the cache entry instead of recomputing the task. Otherwise, HealthOmics reverts to the
default service behavior, which is to recompute the task and its dependent tasks. By using this approach, cache
misses don't cause the run to fail.

We recommend that you manage the run cache size. Over time, cache entries may no longer be valid because of
workflow engine or HealthOmics service updates or because of changes you made in the run or the run tasks. The following
sections provide additional details.

###### Topics

- [Manifest version updates and data freshness](#workflow-cache-data-versions "#workflow-cache-data-versions")
- [Run cache behavior](#run-cache-behavior "#run-cache-behavior")
- [Control run cache size](#workflow-cache-manage "#workflow-cache-manage")

### Manifest version updates and data freshness

Periodically, the HealthOmics service may introduce new features or workflow engine updates that invalidate some or
all run cache entries. In this situation, your runs can experience a one-time cache miss.

HealthOmics creates a [JSON manifest file](workflow-cache-contents.md "workflow-cache-contents.md") for each cache entry. For runs
started after February 12th 2025, the manifest file includes a version parameter. If a service update
invalidates any cache entries, HealthOmics increments the version number so that you can identify the legacy cache
entries for removal.

The following example shows a manifest file with the version set to 2:

```
{
     "arn": "arn:aws:omics:us-west-2:12345678901:runCache/0123456/cacheEntry/1234567-195f-3921-a1fa-ffffcef0a6a4",
     "s3uri": "s3://example/1234567-d0d1-e230-d599-10f1539f4a32/1348677/4795326/7e8c69b1-145f-3991-a1fa-ffffcef0a6a4",
     "taskArn": "arn:aws:omics:us-west-2:12345678901:task/4567891",
     "workDir": "/mnt/workflow/1234567-d0d1-e230-d599-10f1539f4a32/workdir/call-TxtFileCopyTask/5w6tn5feyga7noasjuecdeoqpkltrfo3/wxz2fuddlo6hc4uh5s2lreaayczduxdm",
     "files": [
         {
             "name": "output_txt_file",
             "path": "out/output_txt_file/outfile.txt",
             "etag": "ajdhyg9736b9654673b9fbb486753bc8"
         }
     ],
     "nextflowContext": {},
     "otherOutputs": {},
     "version": 2,
  }
```

For runs with cache entries that are no longer valid, rebuild the cache to create new valid entries. Perform
the following steps for each run:

1. Start the run once with cache retention set to CACHE ALWAYS. This run creates the new cache entries.
2. For subsequent runs, set the cache retention to its former setting (CACHE ALWAYS or CACHE ON FAILURE).

To clean-up cache entries that are no longer valid, you can delete these cache entries from the cache Amazon S3
bucket. HealthOmics never reuses these cache entries. If you choose to retain entries that aren't valid, there is no
impact on your runs.

###### Note

Call caching saves task output data in the Amazon S3 location specified for the cache, which incurs charges to
your AWS account.

### Run cache behavior

You can set run cache behavior to save the task outputs for runs that fail (cache on failure) or for all runs
(cache always). When you create a run cache, you set the default cache behavior for all runs that use this cache.
You can override the default behavior when you start a run.

**Cache on failure** is useful if you're debugging a workflow that fails after several tasks
completed successfully. The subsequent run resumes from the last successfully completed task if all the unique
variables considered by the hash are identical to the prior run.

**Cache always** is useful if you're updating a task in a workflow that completes
successfully. We recommend that you follow these steps:

1. Create a new run. Set the **Cache behavior** to **Cache
   always**, and start the run.
2. After the run completes, update the task in the workflow and start a new run with behavior set
   **Cache always**. This run processes the updated task and any subsequent
   tasks that have a dependency on the updated task. All other tasks use the cached results.
3. Repeat step 2 as required, until development is complete for the updated task.
4. Use the updated task as needed on future runs. Remember to switch subsequent runs to **Cache on failure** if you plan to use new or different inputs for these runs.

###### Note

We recommend **Cache always** mode while using the same test data set, but
not for a batch of runs. If you set this mode for a large batch of runs, the system can export large amounts
of data to Amazon S3, resulting in increased export times and storage costs.

### Control run cache size

HealthOmics doesn't delete or auto-archive any run cache data or apply Amazon S3 clean-up rules for managing the cache
data. We recommend that you perform regular cache clean-ups to save on Amazon S3 storage costs and to keep your run
cache size manageable. You can delete files directly or set data retention/replication policies on the run cache
bucket.

For example, you can configure an Amazon S3 lifecycle policy to expire objects after 90 days, or you can manually
clean-up the cache data at the end of each development project.

The following information can help you manage cache data size:

- You can view how much data is in the cache by checking Amazon S3. HealthOmics doesn't monitor or report on cache
  size.
- If you delete a valid cache entry, the subsequent run doesn't fail. HealthOmics recomputes the task and its
  dependent tasks.
- If you modify cache names or directory structures such that HealthOmics can’t find a matching entry for a task,
  HealthOmics recomputes the task.

If you need to check whether a cache entry is still valid, check the cache manifest version number.
For more information, see [Manifest version updates and data freshness](#workflow-cache-data-versions "#workflow-cache-data-versions").

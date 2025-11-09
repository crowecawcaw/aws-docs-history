# Contents of a run cache

HealthOmics organizes your run cache with the following structure in your S3 bucket:

```
s3://{cache.S3location}/{cache.uuid}/runID/taskID/{cacheentry.uuid}/
```

The cache.uuid is the globally unique id for the cache. The cacheentry.uuid is the globally unique uuid for a
cached task. HealthOmics assigns the uuids to caches and tasks.

For all workflow engines, the cache contains the following files:

- The **{cacheentryuuid}.json** file – HealthOmics creates this manifest file, which contains
  information about the cache, including a list of all items in the cache,
  and the [cache version](how-run-cache.md#workflow-cache-data-versions "how-run-cache.md#workflow-cache-data-versions").
- Task output files – Each task output consists of one or more files, as defined by the task.
  For a workflow that uses Nextflow, the Nextflow engine creates these additional files in the cache:

- The **command.out** file – This file contains the task execution stdout contents.
- The **.exitcode** file – This file contains the task exit code (an integer).

###### Note

If you want to access intermediate task files in your run cache for advanced troubleshooting, declare these
files as task outputs in the workflow definition.

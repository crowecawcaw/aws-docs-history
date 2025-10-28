AWS HealthOmics variant stores and annotation stores will no longer be open to new customers starting
November 7th, 2025. If you would like to use variant stores or annotation stores,
sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see
[AWS HealthOmics variant store and annotation store availability change](variant-store-availability-change.md "variant-store-availability-change.md").

# Call caching for HealthOmics runs

AWS HealthOmics supports call caching, also known as resume, for private workflows. Call caching saves the outputs of
completed workflow tasks after a run finishes. Subsequent runs can use the task outputs from the cache, rather than
computing the task outputs again. Call caching reduces compute resource usage, which results in shorter run
durations and compute cost savings.

You can access the cached task output files after the run completes. To perform advanced task debugging and
troubleshooting, you can cache intermediate task files by specifying these files as task outputs in the workflow
definition.

You can use call caching to save the completed task results from failed runs. The next run starts from the last
successfully completed task, rather than computing the completed tasks again.

If HealthOmics doesn't find a matching cache entry for a task, the run doesn't fail. HealthOmics recomputes the task and its
dependent tasks.

For information about troubleshooting call caching issues, see [Troubleshooting call caching issues](troubleshooting.md#workflow-cache-troubleshooting "troubleshooting.md#workflow-cache-troubleshooting").

###### Topics

- [How call caching works](how-run-cache.md "how-run-cache.md")
- [Creating a run cache](workflow-cache-create.md "workflow-cache-create.md")
- [Updating a run cache](workflow-cache-update.md "workflow-cache-update.md")
- [Deleting a run cache](workflow-cache-delete.md "workflow-cache-delete.md")
- [Contents of a run cache](workflow-cache-contents.md "workflow-cache-contents.md")
- [Engine-specific caching features](workflow-cache-per-engine.md "workflow-cache-per-engine.md")
- [Using the run cache](workflow-cache-startrun.md "workflow-cache-startrun.md")

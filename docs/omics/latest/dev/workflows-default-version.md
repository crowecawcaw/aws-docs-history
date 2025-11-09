# Default workflow version

After you create one or more versions of a workflow, HealthOmics treats the original workflow as the default version.
When you start a run, you can optionally specify a workflow version for the run. If you don't specify a version
when you start a run, HealthOmics uses the default version.

In the console, HealthOmics indicates the original workflow with a **Default version** label. The
console uses this label only after you create one or more workflow versions. The original workflow always remains
the default version. You can't assign any other version to be the default.

You can't delete a workflow's default version if there are other versions associated with the workflow. For
more information, see [Delete a private workflow](delete-private-workflow.md "delete-private-workflow.md").

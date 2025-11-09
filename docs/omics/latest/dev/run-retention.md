# Run retention mode for HealthOmics runs

After a run completes, HealthOmics archives the run metadata to CloudWatch. By default, CloudWatch keeps the run data
indefinitely, unless you change the CloudWatch retention policy. Run outputs are also stored in Amazon S3 until you delete
them.

One of the adjustable [HealthOmics service quotas](service-quotas.md "service-quotas.md") is the **maximum
number of runs (active and inactive)** in a region. HealthOmics retains run metatdata for up to this number of
runs for use by the console and API operations (ListRuns and GetRun). When you start a run, you can set the run
retention mode parameter to indicate the retention behavior for the run. The parameter supports the values REMOVE
and RETAIN.

For a new run with retention mode set to REMOVE, if HealthOmics tries to add the run after it has already saved the
maximum number of runs, it automatically removes the metadata for the oldest run that has set REMOVE mode. This
removal doesn't affect the data stored in CloudWatch or Amazon S3.

RETAIN is the default value for run retention mode. For runs in this mode, the system doesn't delete the run
metadata. If HealthOmics reaches the maximum number of runs, all set to RETAIN, you won't be able to create additional
runs until you delete some runs.

If you're planning to run a batch of more than the maximum number of runs at the same time, make sure to set the
run retention mode to REMOVE. Otherwise, the batch fails when HealthOmics tries to start the next run after the maximum.

Additional considerations for using REMOVE retention mode:

- When you first start using REMOVE as the retention mode, consider deleting one or more runs that use
  RETAIN mode, to free up slots. As you start additional REMOVE runs, the automatic removal takes over, so
  enough slots are available for new runs.
- If you want to re-run an archived run (or a set of runs), use the HealthOmics rerun CLI tool. For more information
  and examples of how to use this tool, see [Omics rerun](https://github.com/awslabs/amazon-omics-tools?tab=readme-ov-file#omics-rerun "https://github.com/awslabs/amazon-omics-tools?tab=readme-ov-file#omics-rerun") in the
  HealthOmics tools GitHub repository.
- We recommend that you configure a unique name for each run. After HealthOmics removes a run, you can't use the
  console or API to find the run name or run ID. However, you can use CloudWatch to search for the run name, so use
  unique names to get the best search results.
- You can use the CloudWatch **start-query** command to get information about an archived run. If the
  run name isn't unique, the query may return multiple manifests. The start-time and end-time parameters define
  the time range for the search.

```
aws logs start-query  \
    --log-group-name "/aws/omics/WorkflowLog" \
    --query-string 'filter @logStream like "manifest" and @message like "`myRunName`"' \
    --end-time <END-EPOCH-TIME> --start-time <START-EPOCH-TIME>
```

The **start-query** command returns a query ID. Passing the query ID to the **get-query-results**
command returns the query results.

```
aws logs get-query-results --query-id `QueryId`
```

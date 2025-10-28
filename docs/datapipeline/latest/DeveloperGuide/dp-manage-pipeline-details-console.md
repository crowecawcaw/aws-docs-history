AWS Data Pipeline is no longer available to new customers. Existing customers of AWS Data Pipeline can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/ "https://aws.amazon.com/blogs/big-data/migrate-workloads-from-aws-data-pipeline/")

# Viewing Pipeline Instance

Details

You can monitor the progress of your pipeline. For more information about instance
status, see [Interpreting Pipeline Status Details](dp-pipeline-status.md "dp-pipeline-status.md").
For more information about troubleshooting failed or incomplete instance runs of
your pipeline, see [Resolving Common Problems](dp-check-when-run-fails.md "dp-check-when-run-fails.md").

###### To monitor the progress of a pipeline using the AWS CLI

To retrieve pipeline instance details, such as a history of the times that a
pipeline has run, use the [list-runs](../../../cli/latest/reference/datapipeline/list-runs.md "../../../cli/latest/reference/datapipeline/list-runs.md") command. This command enables you to filter the list of
runs returned based on either their current status or the date-range in which
they were launched. Filtering the results is useful because, depending on the
pipeline's age and scheduling, the run history can be large.

The following example retrieves information for all runs.

```
`aws datapipeline list-runs --pipeline-id `df-00627471SOVYZEXAMPLE``
```

The following example retrieves information for all runs that have
completed.

```
`aws datapipeline list-runs --pipeline-id `df-00627471SOVYZEXAMPLE` --status finished`
```

The following example retrieves information for all runs launched in the specified
time frame.

```
`aws datapipeline list-runs --pipeline-id `df-00627471SOVYZEXAMPLE` --start-interval "2013-09-02","2013-09-11"`
```

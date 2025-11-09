# Starting HealthOmics Ready2Run workflows using the API

Most of the API operations behave in a similar fashion for Ready2Run workflows and private workflows.

To return a list of available Ready2Run workflows, use **list-workflows** with the
`type` parameter set to READY2RUN.

```
aws omics list-workflows --type READY2RUN
```

After you identify the workflow to run from the
**list-workflows** response, you can use
**get-workflow** with the `--id` parameter to get
more details.

```
aws omics get-workflow --type READY2RUN --id ``workflow id``
```

To run a Ready2Run workflow, you can use **start-run** API
operation with the workflow-type parameter set to `READY2RUN`, as
shown in the following example

```
aws-omics start-run \
  --workflow-type READY2RUN \
  --workflow-id `workflow id` \
  --output-uri &example-s3-bucket; \
  --role-arn arn:aws:iam::1234567892012:role/service-role/OmicsWorkflow-20221004T164236 \
  --parameters file:///path/to/parameters.json
```

To specify a workflow version, use the **workflow-version** parameter,
as shown in this example.

```
aws-omics start-run \
  --workflow-type READY2RUN \
  ...
  --version-name `'3.0.0'`
```

To monitor your run, you can use the **get-run** API operation,
as shown.

```
aws-omics get-run \
  --id `run id`
```

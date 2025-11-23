# Control capacity usage

You can control the number of DPU that Athena allocates to your queries by setting maximum or minimum DPU controls. You can configure these at the workgroup level to establish baseline controls for all queries, or at the individual query level for fine-grained control. This gives you direct control over query performance, workload concurrency, and cost.

- When you set a maximum number of DPU, queries are prevented from consuming more capacity than you specify. This makes it simple to control cost and workload concurrency. For example, if your capacity reservation has 200 DPU, setting the maximum DPU per query to 8 allows you to run 25 queries concurrently. If you increase your reservation to 400 DPU, you can run 50 queries concurrently.
- When you set a minimum number of DPU, you ensure queries are executed with a desired minimum number of DPU. This is helpful when you know the typical capacity usage profile for your queries in advance.

###### Note

DPU usage controls only apply to queries executed with capacity reservations.

###### Note

To use the same number of DPU for all queries, use the same value for the minimum and maximum DPU.

## Set DPU controls at the workgroup level

Set DPU controls at the workgroup level to manage costs and control workload performance for the workgroup that you choose. DPU controls set at the workgroup level apply to all queries when **Override client-side settings** is enabled.

###### To set DPU controls using the console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Workgroups**.
3. Select a workgroup that uses a capacity reservation.
4. On the **Execution controls** tab, choose **Edit controls**.
5. Configure the following:
   - For **Min DPU per query**, enter a value between 4 and 124 in increments of 4.
   - For **Max DPU per query**, enter a value between 4 and 124 in increments of 4.

6. Choose **Save**.
7. (Optional) Select **Override client-side settings** to enforce these settings and ignore query-level DPU configurations.

###### To set DPU controls using the AWS CLI

- Use the `update-work-group` command to set DPU controls for a workgroup:

```
aws athena update-work-group \
  --work-group my_workgroup \
  --configuration-updates '{
        "EngineConfiguration": {
            "Classifications": [
                {
                    "Name": "athena-query-engine-properties",
                    "Properties": {
                        "max-dpu-count" : "24",
                        "min-dpu-count" : "12"
                        }
                    }
                ]
        }}'
```

If you set `EnforceWorkGroupConfiguration` to `true`, the workgroup settings override any DPU controls specified at the query level when submitted via [StartQueryExecution](../APIReference/API_StartQueryExecution.md "../APIReference/API_StartQueryExecution.md"). This ensures consistent resource allocation across all queries in the workgroup.

## Set DPU controls with individual queries

Set query-level DPU controls when you need fine-grained control with queries that have different resource requirements. Query-level DPU controls take precedence over workgroup-level settings unless the workgroup has **Override client-side settings** enabled.

###### To set DPU controls for a query using the console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Query editor**.
3. Select a workgroup that uses a capacity reservation.
4. Choose the **Query settings** tab.
5. In the **Execution controls** section, choose **Edit controls**.
6. Configure the following:
   - For **Min DPU per query**, enter a value between 4 and 124 in increments of 4.
   - For **Max DPU per query**, enter a value between 4 and 124 in increments of 4.

7. Choose **Save**.

###### To set DPU controls for a query using the AWS CLI

- Use the `start-query-execution` command with the `engine-configuration` parameter:

```
aws athena start-query-execution \
  --query-string "SELECT * FROM my_table LIMIT 10" \
  --work-group "my_workgroup" \
  --engine-configuration '{
    "Classifications": [ {
        "Name": "athena-query-engine-properties",
            "Properties": {
                "max-dpu-count" : "32",
                "min-dpu-count" : "8"
                }
            }
        ]}'
```

The relationship between query-level and workgroup-level DPU settings depends on your workgroup configuration:

- When **Override client-side settings** is enabled, workgroup-level DPU controls take precedence over any query-level settings. This ensures consistent resource usage for all queries in the specified workgroup.
- When **Override client-side settings** is not enabled, query-level DPU controls take precedence over workgroup-level settings. This allows flexibility for optimizing individual queries.

If you don't specify DPU controls at either level, Athena automatically allocates capacity based on query complexity.

###### Note

For DDL queries, the maximum value for minimum DPUs is 4. Setting a higher minimum for DDL queries results in an error.

## Monitor DPU usage

After your queries complete, you can view its DPU usage. Athena provides DPU usage metrics through the console, API operations, and CloudWatch.

###### To view DPU consumption in the console

1. Open the Athena console at
   [https://console.aws.amazon.com/athena/](https://console.aws.amazon.com/athena/home "https://console.aws.amazon.com/athena/home").
2. In the navigation pane, choose **Query editor**.
3. After a query completes, view its **Consumed DPU** value in the query results container.
4. To view DPU consumption for past queries:
   1. Choose **Recent queries** in the navigation pane.
   2. Select the settings icon to add the **Consumed DPU** column to the table if not already displayed.
   3. Review the DPU consumption for each completed query.

5. Optionally, from the **Query editor**, choose the **Query stats** tab and review the **Consumed DPU**.

###### To retrieve DPU consumption using the API

1. Use the following API operations to retrieve DPU consumption programmatically:
   - `GetQueryExecution` - Returns execution details for a specific query
   - `BatchGetQueryExecution` - Returns execution details for multiple queries

2. Example using the AWS CLI:

```
aws athena get-query-execution \
  --query-execution-id "123e4567-e89b-12d3-a456-426614174000"
```

The response includes the `DpuCount` field in the `Statistics` object:

```
{
  "QueryExecution": {
    "Statistics": {
      "DpuCount": 8
    }
  }
}
```

###### To monitor DPU usage with CloudWatch

- Athena publishes query-related metrics to CloudWatch that help you monitor capacity utilization and other performance data. To learn more, see [Monitor Athena query metrics with CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md").

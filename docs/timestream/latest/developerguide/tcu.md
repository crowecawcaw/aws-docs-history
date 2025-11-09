For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Timestream Compute Unit (TCU)

Amazon Timestream for Live Analytics measures the compute capacity allocated to you for your query needs in Timestream compute unit (TCU). One TCU comprises of 4 vCPUs and 16 GB of memory. When you run queries in Timestream for Live Analytics, the service allocates TCUs on-demand based on the complexity of your queries and the amount of data being processed. The number of TCUs that a query consumes determines the associated cost.

###### Note

All AWS accounts that onboard to the service after April 29, 2024 will default to using TCUs for query pricing.

###### In this topic:

- [Provisioned Timestream Compute Units](provisioned-tcu.md "provisioned-tcu.md")
- [MaxQuery TCU](#maxquery-tcu "#maxquery-tcu")
- [Billing for TCU](#billing-tcus "#billing-tcus")
- [Configuring TCU](#config-tcus "#config-tcus")
- [Estimating required compute units](#estimate-compute-units "#estimate-compute-units")
- [When to increase MaxQueryTCU](#increase-maxquery-tcu "#increase-maxquery-tcu")
- [When to decrease MaxQueryTCU](#decrease-maxquery-tcu "#decrease-maxquery-tcu")
- [Monitoring usage with CloudWatch metrics](#cw-metrics-monitor-usage "#cw-metrics-monitor-usage")
- [Understanding variations in compute units usage](#variations-compute-units-usage "#variations-compute-units-usage")

## MaxQuery TCU

This setting specifies the maximum number of compute units the service will use at any point in time to serve your queries. To run queries, you must set the minimum capacity to 4 TCUs. You can set the maximum number of TCUs in multiples of 4, for example, 4, 8, 16, 32, and so on. You're charged only for the compute resources you use for your workload. For example, if you set the maximum TCUs to 128, but consistently use only 8 TCUs. You'll be charged only for the duration during which you used the 8 TCUs. The default `MaxQueryTCU` in your account is set to 200. You can adjust `MaxQueryTCU` from 4 to 1000, using the AWS Management Console or [UpdateAccountSettings](API_query_UpdateAccountSettings.md "API_query_UpdateAccountSettings.md") API operation with the AWS SDK or AWS CLI.

We recommend setting the `MaxQueryTCU` for your account. Setting a maximum TCU limit helps control costs by restricting the number of compute units the service can use for your query workload. This allows you to better predict and manage your query spending.

## Billing for TCU

Each TCU is billed on an hourly basis with per-second granularity and for a minimum of 30 seconds. The usage unit of these compute units is TCU-hour.

When you run queries, you're billed for the TCUs used during the query execution time, measured in TCU-hours. For example:

- Your workload uses 20 TCUs for 3 hours. You're billed for 60 TCU-hours (20 TCUs x 3 hours).
- Your workload uses 10 TCUs for 30 minutes, and then 20 TCUs for the next 30 minutes. You're billed for 15 TCU-hours (10 TCUs x 0.5 hours + 20 TCUs x 0.5 hours).

The pricing per TCU-hour varies by AWS Region. Refer to [Amazon Timestream pricing](https://aws.amazon.com/timestream/pricing/ "https://aws.amazon.com/timestream/pricing/") for additional details. As your workload grows, the service automatically scales the compute capacity up to the specified maximum TCU limit (`MaxQueryTCU`) to maintain consistent performance. The `MaxQueryTCU` setting acts as a ceiling for the compute capacity that the service can scale to. This setting helps you to control the number of compute resources and as a result their cost.

## Configuring TCU

When you onboard the service, each AWS account has a default `MaxQueryTCU` limit of 200. You can update this limit as required at any point in time using the AWS Management Console or [UpdateAccountSettings](API_query_UpdateAccountSettings.md "API_query_UpdateAccountSettings.md") API operation with the AWS SDK or AWS CLI.

If you're unsure about the values to configure, monitor the `QueryTCU` metric for your account. This metric is available in the AWS Management Console and Amazon CloudWatch. This metric provides insight into the maximum number of TCUs used at a minute granularity. Based on historical data and your estimation of future growth, set the `MaxQueryTCU` to accommodate the spikes in your usage. We recommend having a headroom of at least 4-16 TCUs above your peak usage. For example, if your peak `QueryTCU` in the last 30 days was 128, we recommend setting `MaxQueryTCU` between 132 to 144.

## Estimating required compute units

Compute units can process queries concurrently. To determine the number of compute units required, consider the general guidelines in the following table:

| Concurrent queries | TCUs |
| ------------------ | ---- |
| 7                  | 4    |
| 14                 | 8    |
| 21                 | 12   |

###### Note

- These are general guidelines and the actual number of compute units required depends on several factors, such as:
  - The effective concurrency of queries.
  - Query patterns.
  - The number of partitions scanned.
  - Other workload-specific characteristics.

- This guideline pertains to queries that scan for the last few minutes to an hour of data and adhere to the [Timestream query best practices](queries-bp.md "queries-bp.md") and [Data modeling guidelines](data-modeling.md "data-modeling.md").
- Monitor your application's performance and the `QueryTCU` metric to adjust the compute units, as required.

## When to increase MaxQueryTCU

You should consider increasing the `MaxQueryTCU` in the following scenarios:

- Your peak query consumption is approaching or reaching the current configured maximum query TCU. We recommend setting the maximum query TCU at least 4-16 TCUs higher than your peak consumption.
- Your queries are returning a 4xx error with the message MaxQueryTCU exceeded. If you anticipate a planned increase in your workload, revisit and adjust the configured maximum query TCU accordingly.

## When to decrease MaxQueryTCU

You should consider decreasing the `MaxQueryTCU` in the following scenarios:

- Your workload has a predictable and stable usage pattern, and you have a good understanding of your compute usage requirements. Lowering the maximum query TCU to within 4-16 TCU above your peak consumption can help prevent unintentional usage and costs. You can modify the value using the [UpdateAccountSettings](API_query_UpdateAccountSettings.md "API_query_UpdateAccountSettings.md") API operation.
- Your workload's peak usage has decreased over time, either due to changes in your application or user behavior patterns. Lowering the maximum TCU can help mitigate unintentional costs.

###### Note

Depending on your current usage, reducing the maximum TCU limit change might take up to 24 hours to be effective. You're billed only for the TCUs that your queries actually consume. Having a higher maximum query TCU limit does not impact your costs unless those TCUs are used by your workload.

## Monitoring usage with CloudWatch metrics

To monitor your TCU usage, Timestream for Live Analytics provides the following CloudWatch metric: `QueryTCU`. This metric specifies the number of compute units used in a minute and is emitted every minute. You can choose to monitor the maximum and minimum TCUs used in a minute. You can also set alarms on this metric to track your query costs in real-time.

## Understanding variations in compute units usage

The number of compute resources required for your queries can either increase or decrease based on several parameters. For example, data volume, data ingestion patterns, query latency, query shape, query efficiency, and query combinations that use real-time and analytical queries. These parameters can lead to either higher or lower TCU units required for your workload. In a steady state where these parameters don't change, you might observe that the number of compute units required for your workload decrease. Consequently, this can lower your monthly cost.

Additionally, if any of these parameters in your workload or data change, the number of compute units required might increase. When Timestream receives a query, depending upon the data partitions the query accesses, Timestream decides the number of compute resources to performantly address the query.

At periodic intervals, based on your ingest and query access patterns, Timestream optimizes the data layout. Timestream performs the optimization by clubbing less accessed partitions into a single partition or splitting a hot partition into multiple partitions for performance. Consequently, the compute capacity used by the same query might vary slightly at different points in time.

###### Opting-in to use TCU pricing for your queries

As an existing user, you can do a one-time opt-in to use TCUs for better cost management and removal of per query minimum bytes metered. You can opt-in using the AWS Management Console or [UpdateAccountSettings](API_query_UpdateAccountSettings.md "API_query_UpdateAccountSettings.md") API operation with the AWS SDK or AWS CLI. In the API operation, set the `QueryPricingModel` parameter to `COMPUTE_UNITS`.

Opting into the compute-based pricing model is an irreversible change.

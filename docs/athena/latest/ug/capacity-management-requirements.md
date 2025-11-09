# Determine capacity requirements

Before you create a capacity reservation, you can estimate the capacity required so that
you can assign it the correct number of DPUs. And, after a reservation is in use, you might
want to check the reservation for insufficient or excess capacity. This topic describes
techniques that you can use to make these estimates and also describes some AWS tools for
assessing usage and cost.

###### Topics

- [Estimate required
  capacity](#capacity-management-requirements-estimating "#capacity-management-requirements-estimating")
- [Signs that more
  capacity is required](#capacity-management-requirements-insufficient-capacity "#capacity-management-requirements-insufficient-capacity")
- [Check for idle
  capacity](#capacity-management-requirements-idle-capacity "#capacity-management-requirements-idle-capacity")

## Estimate required

capacity

When estimating capacity requirements, it is useful to consider two perspectives: how
much capacity a particular query might require, and how much capacity you might need in
general.

### Estimate

per-query capacity requirements

To determine the number of DPUs that a query might would require, you can use the
following guidelines:

- DDL queries consume 4 DPUs.
- DML queries consume between 4 and 124 DPUs.

Athena determines the number of DPUs required by a DML query when the query is
submitted. The number varies based on data size, storage format, query construction,
and other factors. Generally, Athena tries to select the lowest, most efficient DPU
number. If Athena determines that more computational power is required for the query
to complete successfully, it increases the number of DPUs assigned to the
query.

### Estimate

workload specific capacity requirements

To determine how much capacity you might require to run multiple queries at the
same time, consider the general guidelines in the following table:

| Concurrent queries | DPUs required |
| ------------------ | ------------- |
| 10                 | 40 or more    |
| 20                 | 96 or more    |
| 30 or more         | 240 or more   |

Note that the actual number of DPUs that you need depends on your goals and
analysis patterns. For example, if you want queries to start immediately without
queuing, determine your peak concurrent query demand, and then provision the number
of DPUs accordingly.

You can provision fewer DPUs than your peak demand, but queuing may result when
peak demand occurs. When queuing occurs, Athena holds your queries in a queue and
runs them when capacity becomes available.

If your goal is to run queries within a fixed budget, you can use the [AWS Pricing Calculator](https://calculator.aws/#/addService/Athena "https://calculator.aws/#/addService/Athena")
to determine the number of DPUs
that fit your
budget.

Lastly, remember that data size, storage format, and how a query is written
influence the DPUs that a query requires. To increase query performance, you can
compress or partition your data or convert it into columnar formats. For more
information, see [Optimize Athena performance](performance-tuning.md "performance-tuning.md").

## Signs that more

capacity is required

Insufficient capacity error messages and query queuing are two indications that your
assigned capacity is inadequate.

If your queries fail with an insufficient capacity error message, your capacity
reservation's DPU count is too low for your query. For example, if you have a
reservation with 24 DPUs and run a query that requires more than 24 DPUs, the query will
fail. To monitor for this query error, you can use Athena's [EventBridge events](athena-events.md "athena-events.md"). Try adding more DPUs and
re-running your query.

If many queries are queued, it means your capacity is fully utilized by other queries.
To reduce the queuing, do one of the following:

- Add DPUs to your reservation to increase query concurrency.
- Remove workgroups from your reservation to free up capacity for other
  queries.

To check for excessive query queuing, use the Athena query queue time [CloudWatch
metric](query-metrics-viewing.md "query-metrics-viewing.md") for the workgroups in your capacity reservation. If the value is above
your preferred threshold, you can add DPUs to the capacity reservation.

## Check for idle

capacity

To check for idle capacity, you can either decrease the number of DPUs in the
reservation or increase its workload, and then observe the results.

###### To check for idle capacity

1. Do one of the following:
   - Reduce the number of DPUs in your reservation (reduce the resources
     available)
   - Add workgroups to your reservation (increase the workload)

2. Use [CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md") to measure the query queue time.
3. If the queue time increases beyond a desirable level, do one of the
   following
   - Remove workgroups
   - Add DPUs to your capacity reservation

4. After each change, check the performance and query queue time.
5. Continue to adjust the workload and/or DPU count to attain the desired
   balance.

If you do not want to maintain capacity outside a preferred time period, you can [cancel](capacity-management-cancelling-a-capacity-reservation.md "capacity-management-cancelling-a-capacity-reservation.md")
the reservation and create another reservation later. However, even if you recently
cancelled capacity from another reservation, requests for new capacity are not
guaranteed, and new reservations take time to create.

You can use the following services and features in AWS to measure your Athena
usage and costs.

### CloudWatch

metrics

You can configure Athena to publish query-related metrics to Amazon CloudWatch at the
workgroup level. After you enable metrics for the workgroup, the metrics for the
workgroup's queries are displayed in the Athena console on the workgroup's
details page.

For information about the Athena metrics published to CloudWatch and their
dimensions, see [Monitor Athena query metrics with CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md").

### CloudWatch usage metrics

You can use CloudWatch usage metrics to provide visibility into your how your
account uses resources by displaying your current service usage on CloudWatch graphs
and dashboards. For Athena, usage availability metrics correspond to AWS [service
quotas](service-limits.md "service-limits.md") for Athena. You can configure alarms that alert you when your
usage approaches a service quota.

For more information, see [Monitor Athena usage metrics with
CloudWatch](monitoring-athena-usage-metrics.md "monitoring-athena-usage-metrics.md").

### Amazon EventBridge events

You can use Amazon Athena with Amazon EventBridge to receive real-time notifications
regarding the state of your queries. When a query you have submitted changes
states, Athena publishes an event to EventBridge that contains information about the
query state transition. You can write simple rules for events that are of
interest to you and take automated actions when an event matches a rule.

For more information, see the following resources.

- [Monitor Athena query events with EventBridge](athena-events.md "athena-events.md")
- [What Is
  Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
- [Amazon EventBridge
  events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md")

### Tags

In Athena, capacity reservations support tags. A tag consists of a key and a
value. To track your costs in Athena, you can use AWS-generated cost allocation
tags. AWS uses the cost allocation tags to organize your resource costs on
your [Cost and Usage Report](../../../cur/latest/userguide/what-is-cur.md "../../../cur/latest/userguide/what-is-cur.md"). This makes it easier for you to categorize
and track your AWS costs. To activate cost allocation tags for Athena, you use
the [AWS Billing and Cost Management console](https://console.aws.amazon.com/billing/ "https://console.aws.amazon.com/billing/").

For more information, see the following resources.

- [Tag Athena resources](tags.md "tags.md")
- [Activating the AWS-generated cost allocation tags](../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md "../../../awsaccountbilling/latest/aboutv2/activate-built-in-tags.md")
- [Using
  AWS cost allocation tags](../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md "../../../awsaccountbilling/latest/aboutv2/cost-alloc-tags.md")

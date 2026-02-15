# Manage query processing capacity

You can use capacity reservations to get dedicated serverless processing capacity for the queries you
run in Athena. With capacity reservations, you can take advantage of workload management
capabilities that help you prioritize, control, and scale your most important
workloads. For example, you can add capacity to control the number of queries
you can run at the same time, choose which workloads can use the capacity, and share capacity
among workloads. Capacity is serverless and fully-managed by Athena and held for you as long as you need it.
Setup is easy and no changes to your SQL queries are required.

To get processing capacity for your queries, you create a capacity reservation, specify
the number of Data Processing Units (DPUs) that you require, and assign one or more
workgroups to the reservation.

Workgroups play an important role when you use capacity reservations. Workgroups allow you
to organize queries into logical groupings or use cases. With capacity reservations, you selectively
assign capacity to workgroups so that you control how the queries for each workgroup behave
and how they are billed. For more information about workgroups, see [Use workgroups to control query
access and costs](workgroups-manage-queries-control-costs.md "workgroups-manage-queries-control-costs.md").

Assigning workgroups to capacity reservations lets you give priority to these queries because they run on your reserved capacity and do not count
towards your DDL and DML query quota. For example, you can allocate capacity to a workgroup used for
time-sensitive financial reporting queries to isolate those queries from less critical
queries in another workgroup. This gives you predictable query execution for critical workloads
while allowing other workloads to run independently.

You can use capacity reservations and workgroups together to meet different requirements.
The following are some example scenarios:

- Isolate important queries – To ensure that an important
  workload has the capacity it needs when you need it, create a capacity reservation and assign its workgroup to the reservation.
  Only queries from the assigned workgroup use the processing capacity from your
  reservation. For example, to ensure reliable
  execution of queries that support a production application, assign the production workgroup
  for those queries to a capacity reservation. When developing queries, use a separate
  workgroup that is not associated with a reservation and move the queries to the production workgroup when ready.
- Share capacity across similar workloads – Multiple workloads can
  share capacity from one reservation. This allows you to achieve a predictable cost for these workloads and control their concurrency. For example,
  if you have scheduled workloads that are tolerant to delayed query execution start times, you can assign their
  workgroups to a single reservation. This frees up your DDL and DML query quota for interactive queries that run in the same account,
  ensuring these queries start with minimal delay.

## Understand DPUs

Capacity is measured in Data Processing Units (DPUs). DPUs represent the serverless compute and
memory resources used by Athena to access and process data on your behalf. One DPU
typically provides 4 vCPUs and 16 GB of memory. The number of DPUs that you hold influences
the number of queries that you can run concurrently. For example, a reservation with 256
DPUs can support approximately twice the number of concurrent queries than a
reservation with 128 DPUs.

For information about estimating your capacity requirements, see [Determine capacity requirements](capacity-management-requirements.md "capacity-management-requirements.md"). For pricing information, see
[Amazon Athena pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").

## Considerations and

limitations

- You can use capacity reservations and per-query billing, based on data scanned, at the same time in the same account.
- Queries run on capacity reservations do not count towards your DDL and DML query quota.
- If your capacity is busy serving other queries, newly submitted queries are queued until capacity is available. The maximum allowed time in queue is 10 hours.
- A workgroup can be assigned to one capacity reservation at a time. You can assign a total of 20 workgroups to a single reservation. When you assign multiple workgroups to a reservation, capacity is shared across workgroups and allocated to queries based on their submission order. There may be variation in execution order due to how Athena dynamically allocates capacity to queries.
- Athena automatically allocates between 4 and 124 DPUs to DML queries based on their complexity. DDL queries consume 4 DPUs each. Refer to the following topics for more information:
  - [Determine capacity requirements](capacity-management-requirements.md "capacity-management-requirements.md")
  - [Control capacity usage](capacity-management-control-capacity-usage.md "capacity-management-control-capacity-usage.md")

- The minimum number of DPUs required with each capacity reservation is 4. For pricing information, see [Amazon Athena pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").
- You can create up to 100 capacity reservations with up to 1,000 total DPUs per account and region. If you require more than 1,000 DPUs for your use case, please reach out to [athena-feedback@amazon.com](mailto:athena-feedback@amazon.com?subject=Athena Provisioned Capacity DPU Limit Request "mailto:athena-feedback@amazon.com?subject=Athena Provisioned Capacity DPU Limit Request").
- Requests for capacity are not guaranteed and can take up to 30 minutes to complete. Capacity is not transferable to another capacity reservation, AWS account, or AWS Region.
- The `DPUConsumed` CloudWatch metric is per-workgroup rather than
  per-reservation. Thus, if you move a workgroup from one reservation to another,
  the `DPUConsumed` metric includes data from the time when the
  workgroup belonged to the first reservation. For more information about using
  CloudWatch metrics in Athena, see [Monitor Athena query metrics with CloudWatch](query-metrics-viewing.md "query-metrics-viewing.md").
- To delete a workgroup that has been assigned to a reservation, remove the
  workgroup from the reservation first.
- Workgroups configured to use Apache Spark are not supported.
- Capacity reservations is available in the following AWS Regions:
  - US East (N. Virginia)
  - US East (Ohio)
  - US West (Oregon)
  - Asia Pacific (Mumbai)
  - Asia Pacific (Singapore)
  - Asia Pacific (Sydney)
  - Asia Pacific (Tokyo)
  - Europe (Ireland)
  - Europe (Spain)
  - Europe (Stockholm)
  - South America (São Paulo)

###### Topics

- [Determine capacity requirements](capacity-management-requirements.md "capacity-management-requirements.md")
- [Create capacity
  reservations](capacity-management-creating-capacity-reservations.md "capacity-management-creating-capacity-reservations.md")
- [Control capacity usage](capacity-management-control-capacity-usage.md "capacity-management-control-capacity-usage.md")
- [Automatically adjust capacity](capacity-management-automatically-adjust-capacity.md "capacity-management-automatically-adjust-capacity.md")
- [Manage reservations](capacity-management-managing-reservations.md "capacity-management-managing-reservations.md")
- [IAM policies for capacity
  reservations](capacity-reservations-iam-policy.md "capacity-reservations-iam-policy.md")
- [Athena capacity reservation APIs](capacity-management-api-list.md "capacity-management-api-list.md")

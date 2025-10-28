Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Workload management

This section describes workload management (WLM), which helps you understand how Amazon Redshift prepares
and runs queries.

Amazon Redshift workload management (WLM) enables flexible management priorities within workloads so that short, fast-running queries don't get stuck in
queues behind long-running queries. Amazon Redshift creates query queues at runtime according to _service
classes_, which define the configuration parameters for various types of
queues, including internal system queues and user-accessible queues. From a user
perspective, a user-accessible service class and a queue are functionally equivalent.
For consistency, this documentation uses the term _queue_ to mean a
user-accessible service class as well as a runtime queue.

Redshift offers automatic workload management, called **automatic WLM**, which is tuned to handle varying workloads and is the recommended
default. With automatic WLM, Redshift determines resource utilization as queries arrive and dynamically determines whether to run them on the main cluster,
on a concurrency scaling cluster, or to send each to a queue. (When queries are queued, automatic WLM
prioritizes shorter-duration queries.) Automatic WLM maximizes total
throughput and enables you to maintain efficient data-warehouse resources. You run workloads without having to be concerned with their size or how they're
scheduled. Automatic WLM is the default
for provisioned clusters. For more information, see [Implementing automatic WLM](automatic-wlm.md "automatic-wlm.md").

###### Note

Amazon Redshift Serverless workgroups always use automatic WLM.

In times where a lot of queries or resource-intensive queries are running, workload management can scale to additional
compute resources when workloads queue on local resources. Concurrency scaling with automatic WLM supports consistent performance
for virtually unlimited concurrent users and queries.

Redshift provisioned clusters offer **manual WLM** if you need fine-grained manual optimization. Here, the customer manages resource
allocation, query concurrency and queuing. When a query runs, WLM assigns the query to a queue according to the user's
user group or by matching a query group that is listed in the queue configuration. This is configured with a query-group
label that the user sets. For more information, see [Implementing manual WLM](cm-c-defining-query-queues.md "cm-c-defining-query-queues.md").

Though Manual WLM can be fine tuned over time to match your workload patterns, in most cases we discourage its use because its static nature
can make it more difficult for you to adapt to changing workloads through the course of a day or over an extended period. It requires more monitoring
and ongoing tuning. In addition, Manual WLM in many cases doesn't use compute resources as efficiently as automatic WLM, such as for example
if queues are set manually to limit memory allocated to them.

An important metric to measure the success of workload management configuration is system throughput, which in other words is how many queries are completed
successfully. System throughput is measured in queries per second. For more information about system metrics,
see [Monitoring Amazon Redshift cluster performance](../mgmt/metrics.md "../mgmt/metrics.md").

The easiest way to manage your WLM configuration is by using the Amazon Redshift Management console. You can also use
the [Amazon Redshift command line interface](../../../cli/latest/reference/redshift.md "../../../cli/latest/reference/redshift.md") (CLI) or the [Amazon Redshift API](../APIReference/API_Operations.md "../APIReference/API_Operations.md"). For more information
about implementing and using workload management, see [Implementing workload management](cm-c-implementing-workload-management.md "cm-c-implementing-workload-management.md").

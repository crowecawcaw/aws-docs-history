# Troubleshooting AWS Glue for Ray errors from logs

AWS Glue provides access to logs that are emitted by Ray processes during the job run. If you encounter errors or
unexpected behavior in Ray jobs, first gather information from the logs to determine the cause of failure. We
also provide similar logs for interactive sessions. Sessions logs are provided with the
`/aws-glue/ray/sessions` prefix.

Log lines are sent to CloudWatch in real time, as your job is run. Print statements are appended to the CloudWatch logs
after the run completes. Logs are retained for two weeks after a job is run.

## Inspecting Ray job logs

When a job fails, gather your job name and job run ID. You can find these in the AWS Glue console. Navigate
to the job page, and then navigate to the **Runs** tab. Ray job logs are stored in the
following dedicated CloudWatch log groups.

- `/aws-glue/ray/jobs/script-log/` – Stores logs emitted by your main Ray
  script.
- `/aws-glue/ray/jobs/ray-monitor-log/` – Stores logs emitted by the Ray
  autoscaler process. These logs are generated for the head node and not for other worker
  nodes.
- `/aws-glue/ray/jobs/ray-gcs-logs/` – Stores logs emitted by the GCS (global
  control store) process. These logs are generated for the head node and not for other worker
  nodes.
- `/aws-glue/ray/jobs/ray-process-logs/` – Stores logs emitted by other Ray
  processes (primarily the dashboard agent) running on the head node. These logs are generated for the
  head node and not for other worker nodes.
- `/aws-glue/ray/jobs/ray-raylet-logs/` – Stores logs emitted by each raylet
  process. These logs are collected in a single stream for each worker node, including the head
  node.
- `/aws-glue/ray/jobs/ray-worker-out-logs/` – Stores `stdout` logs for
  each worker in the cluster. These logs are generated for each worker node, including the head
  node.
- `/aws-glue/ray/jobs/ray-worker-err-logs/` – Stores `stderr` logs for
  each worker in the cluster. These logs are generated for each worker node, including the head
  node.
- `/aws-glue/ray/jobs/ray-runtime-env-log/` – Stores logs about the Ray setup
  process. These logs are generated for each worker node, including the head
  node.

## Troubleshooting Ray job errors

To understand the organization of Ray log groups, and to find the log groups that will help you
troubleshoot your errors, it helps to have background information about Ray architecture.

In AWS Glue ETL, a worker corresponds to an instance. When you configure workers for an AWS Glue job, you're
setting the type and quantity of instances that are dedicated to the job. Ray uses the term
_worker_ in different ways.

Ray uses _head node_ and _worker node_ to distinguish the
responsibilities of an instance within a Ray cluster. A Ray worker node can host multiple
_actor_ processes that perform computations to achieve the result of your distributed
computation. Actors that run a replica of a function are called _replicas_. Replica
actors can also be called worker processes. Replicas can also run on the head node, which is known as the head
because it runs additional processes to coordinate the cluster.

Each actor that contributes to your computation generates its own log stream. This provides us with some
insights:

- The number of processes that emit logs might be larger than the number of workers that are
  allocated to the job. Often, each core on each instance has an actor.
- Ray head nodes emit cluster management and startup logs. In contrast, Ray worker nodes only emit
  logs for the work performed on them.

For more information about Ray architecture, see [Architecture Whitepapers](https://docs.ray.io/en/latest/ray-contribute/whitepaper.html " https://docs.ray.io/en/latest/ray-contribute/whitepaper.html") in the
Ray documentation.

### Problem area: Amazon S3 access

Check the failure message of the job run. If that doesn't provide enough information, check
`/aws-glue/ray/jobs/script-log/`.

### Problem area: PIP dependency

management

Check `/aws-glue/ray/jobs/ray-runtime-env-log/`.

### Problem area: Inspecting intermediate values

in main process

Write to `stderr` or `stdout` from your main script, and retrieve logs from
`/aws-glue/ray/jobs/script-log/`.

### Problem area: Inspecting intermediate values

in a child process

Write to `stderr` or `stdout` from your `remote` function. Then,
retrieve logs from `/aws-glue/ray/jobs/ray-worker-out-logs/` or
`/aws-glue/ray/jobs/ray-worker-err-logs/`. Your function might have run on any replica, so
you might have to examine multiple logs to find your intended output.

### Problem area: Interpreting IP addresses in error messages

In certain error situations, your job might emit an error message that contains an IP address. These
IP addresses are ephemeral, and are used by the cluster to identify and communicate between nodes. Logs
for a node will be published to a log stream with a unique suffix based on the IP address.

In CloudWatch, you can filter down your logs to inspect those specific to this IP address by identifying
this suffix. For example, given `FAILED_IP` and
`JOB_RUN_ID`, you can identify the suffix with:

````
filter @logStream like /`JOB_RUN_ID`/
| filter @message like /IP-/
| parse @message "IP-[*]" as ip
| filter ip like /`FAILED_IP`/
| fields replace(ip, ":", "_") as uIP
| stats count_distinct by uIP as logStreamSuffix
| display logStreamSuffix ```
````



# Managing virtual clusters
<a name="virtual-cluster"></a>

A virtual cluster is a Kubernetes namespace that Amazon EMR is registered with. You can create, describe, list, and delete virtual clusters. They do not consume any additional resource in your system. A single virtual cluster maps to a single Kubernetes namespace. Given this relationship, you can model virtual clusters the same way you model Kubernetes namespaces to meet your requirements. See possible use cases in the [Kubernetes Concepts Overview](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) documentation. 

To register Amazon EMR with a Kubernetes namespace on an Amazon EKS cluster, you need the name of the EKS cluster and the namespace that has been set up for running your workload. These registered clusters in Amazon EMR are called virtual clusters because they do not manage physical compute or storage but point to a Kubernetes namespace where your workload is scheduled.

**Note**  
Before creating a virtual cluster, you must first complete the steps 1-8 in [Setting up Amazon EMR on EKS](setting-up.md).

**Topics**
+ [Create a virtual cluster](#create-virtul-cluster)
+ [List virtual clusters](#list-virtual-cluster)
+ [Describe a virtual cluster](#describe-virtual-cluster)
+ [Delete a virtual cluster](#delete-virtual-cluster)
+ [Virtual cluster states](#virtual-cluster-states)
+ [Concurrent job limits for virtual clusters](#virtual-cluster-job-concurrency-limits)

## Create a virtual cluster
<a name="create-virtul-cluster"></a>

Run the following command to create a virtual cluster by registering Amazon EMR with a namespace on an EKS cluster. Replace {{virtual\_cluster\_name}} with a name that you provide for your virtual cluster. Replace {{eks\_cluster\_name}} with the name of the EKS cluster. Replace the {{namespace\_name}} with the namespace that you want to register Amazon EMR with.

```
aws emr-containers create-virtual-cluster \
--name {{virtual_cluster_name}} \
--container-provider '{
    "id": "{{eks_cluster_name}}",
    "type": "EKS",
    "info": {
        "eksInfo": {
            "namespace": "{{namespace_name}}"
        }
    }
}'
```

Alternatively, you can create a JSON file that includes the required parameters for the virtual cluster, as the following example demonstrates.

```
{
    "name": "{{virtual_cluster_name}}", 
    "containerProvider": {
        "type": "EKS", 
        "id": "{{eks_cluster_name}}", 
        "info": {
            "eksInfo": {
                "namespace": "{{namespace_name}}"
            }
        }
    }
}
```

Then run the following `create-virtual-cluster` command with the path to the JSON file.

```
aws emr-containers create-virtual-cluster \
--cli-input-json {{file://./create-virtual-cluster-request.json}}
```

**Note**  
To validate the successful creation of a virtual cluster, view the status of virtual clusters by running the `list-virtual-clusters` command or by going to the **Virtual clusters** page in the Amazon EMR console.

## List virtual clusters
<a name="list-virtual-cluster"></a>

Run the following command to view the status of virtual clusters. 

```
aws emr-containers list-virtual-clusters
```

## Describe a virtual cluster
<a name="describe-virtual-cluster"></a>

Run the following command to get more details about a virtual cluster, such as namespace, status, and date registered. Replace {{123456}} with your virtual cluster ID. 

```
aws emr-containers describe-virtual-cluster --id {{123456}}
```

## Delete a virtual cluster
<a name="delete-virtual-cluster"></a>

Run the following command to delete a virtual cluster. Replace {{123456}} with your virtual cluster ID.

```
aws emr-containers delete-virtual-cluster --id {{123456}}
```

## Virtual cluster states
<a name="virtual-cluster-states"></a>

The following table describes the four possible states of a virtual cluster.


| `State` | Description | 
| --- | --- | 
| `RUNNING` | Virtual cluster is in RUNNING state.  | 
| `TERMINATING` | The requested termination of the virtual cluster is in progress. | 
| `TERMINATED` | The requested termination is complete. | 
| `ARRESTED` | The requested termination failed because of insufficient permissions. | 

## Concurrent job limits for virtual clusters
<a name="virtual-cluster-job-concurrency-limits"></a>

You can configure concurrent job limits on an Amazon EMR on EKS virtual cluster to control how many job runs execute simultaneously and how many can wait in queue. You set the concurrency limit (`maxConcurrentJobRuns`) and the queue depth (`maxInQueueJobRuns`) independently, so you can cap running job runs, queued job runs, or both. When you set these limits, the `StartJobRun` API provides backpressure at the virtual cluster level. Job runs beyond the running limit wait in the queue in the `SUBMITTED` or `PENDING` state instead of starting immediately, and once the queue is full, `StartJobRun` rejects further submissions. For example, if you set a virtual cluster to allow 500 concurrent job runs and 100 queued job runs, the 101st queued submission is rejected, and you can rebalance that workload across other virtual clusters on the same EKS cluster or add capacity. When you have not set a concurrency limit and queue depth keeps growing, so that job runs stay in the `SUBMITTED` or `PENDING` state longer before they start, it can signal that the underlying EKS cluster is running low on compute resources and cannot schedule new pods fast enough. In that case, route the workload to another cluster or add capacity.

Concurrent job limits add a control layer in front of the Kubernetes scheduler and the [ResourceQuota](https://kubernetes.io/docs/concepts/policy/resource-quotas/) feature on the Kubernetes website. Because they are enforced at `StartJobRun`, before any pods are created, excess load is queued or rejected at the API, which protects the underlying cluster before jobs ever reach it. Kubernetes still enforces the actual CPU and memory ceiling underneath.

### Key benefits of concurrent job limits
<a name="virtual-cluster-job-concurrency-benefits"></a>
+ **Prevents noisy-neighbor overload** — Limits the number of running and queued job runs per virtual cluster, so that a single virtual cluster cannot monopolize the shared EKS cluster and cause noisy-neighbor scheduling failures for other virtual clusters.
+ **Enables traffic shaping** — Returns an immediate rejection when a virtual cluster's queue is full, so that you can redirect submissions to other virtual clusters instead of overwhelming a single virtual cluster.
+ **Provides visibility** — Emits the per-virtual-cluster `JobsRunning` and `JobsInQueue` CloudWatch metrics in the `AWS/EMRContainers` namespace for active and in-queue job run counts every 5 minutes, which gives you a health signal for scheduling.

### Getting started with concurrent job limits
<a name="virtual-cluster-job-concurrency-getting-started"></a>

You configure concurrent job limits with the `schedulerConfiguration` field on a virtual cluster. This field accepts two parameters:

`maxConcurrentJobRuns`  
The maximum number of job runs that can be in the `RUNNING` state at any time.

`maxInQueueJobRuns`  
The maximum number of job runs that can be in the `PENDING` or `SUBMITTED` state (queue depth) at any time.

#### AWS CLI
<a name="virtual-cluster-job-concurrency-cli"></a>

To set limits when you create a virtual cluster, specify `schedulerConfiguration` in your request.

```
aws emr-containers create-virtual-cluster \
  --name {{my-virtual-cluster}} \
  --container-provider '{ ... }' \
  --scheduler-configuration '{
      "maxConcurrentJobRuns": 500,
      "maxInQueueJobRuns": 100
  }'
```

To change limits on an existing virtual cluster, use the `update-virtual-cluster` command.

```
aws emr-containers update-virtual-cluster \
  --id {{virtual-cluster-id}} \
  --scheduler-configuration '{
      "maxConcurrentJobRuns": 500,
      "maxInQueueJobRuns": 100
  }'
```

To remove the limits from a virtual cluster, pass an empty `schedulerConfiguration`. This clears the configuration, so no limits apply and the virtual cluster returns to default (unlimited) behavior. Note that *omitting* `schedulerConfiguration` from the request instead leaves the existing limits unchanged — you must pass an empty object to clear them.

```
aws emr-containers update-virtual-cluster \
  --id {{virtual-cluster-id}} \
  --scheduler-configuration '{}'
```

To view the current limits and live job counts, use the `describe-virtual-cluster` command. The response includes both your `schedulerConfiguration` and a `SchedulerStatus` object with the current `activeJobRunCount` and `inQueueJobRunCount`.

**Note**  
When you submit a job run to a virtual cluster whose queue is full, `StartJobRun` returns a `ValidationException`.

### Choosing values for maxConcurrentJobRuns and maxInQueueJobRuns
<a name="virtual-cluster-job-concurrency-choosing-values"></a>

The right limits depend on three things: how much work your Amazon EKS cluster can run at once, how bursty your submissions are, and how you want the virtual cluster to behave when it is full. Use the following guidance to pick a starting point, and then refine it from the live counters.

#### Setting maxConcurrentJobRuns (running slots)
<a name="virtual-cluster-job-concurrency-running-slots"></a>

`maxConcurrentJobRuns` is a job-granularity, count-based guardrail. A rough estimate here can protect the underlying Amazon EKS cluster from being degraded due to load and can improve availability.
+ **Start from capacity divided by per-job footprint.** Base it on what each job *requests* (driver, executors, and memory overhead), and target approximately 70–80 percent of your namespace capacity to leave headroom for driver overhead, node scale-up, and bursts.
+ **Cap the size of each job (T-shirt sizing).** Bound every job with `spark.dynamicAllocation.maxExecutors` and standardize on a few sizes — for example, Small (20 executors), Medium (100), and Large (approximately 500) — so that `maxConcurrentJobRuns` multiplied by the cap maps predictably to capacity instead of over-provisioning or under-provisioning for a variable average. For the cleanest math, route each size class to its own virtual cluster.
+ **Tune from live counters.** Start conservative and raise the value gradually while you watch `activeJobRunCount` and the `JobsRunning` metric in the `AWS/EMRContainers` namespace.

#### Setting maxInQueueJobRuns (queue depth)
<a name="virtual-cluster-job-concurrency-queue-depth"></a>

`maxInQueueJobRuns` controls how large a backlog the virtual cluster accepts before it starts rejecting submissions. It is a burst-absorption buffer. Consider the following factors.
+ **Burst profile** — Size the queue to absorb the submission bursts that you expect above your running rate. If scheduled pipelines fire many jobs at once, a deeper queue prevents spurious rejections. Base the depth on your expected burst size rather than on a fixed multiple of `maxConcurrentJobRuns`, and validate it against the drain-time limit that follows.
+ **Acceptable wait time** — Queued jobs wait for a running slot to free up. The job at the back of a full queue waits approximately the queue depth divided by the completion throughput. For example, if jobs finish at N per minute and the queue holds Q, the tail waits about Q divided by N minutes. Keep this within your SLA. Because buffered jobs fail after 30 minutes if no slot frees up, keep `maxInQueueJobRuns` small enough that a full queue drains well within 30 minutes at your steady completion rate. Otherwise, queued jobs time out.
+ **Backpressure compared to buffering** — A deeper queue smooths bursts, but it delays the queue-full rejection that you use for traffic shaping and increases tail latency. A shallower queue fails fast, which gives clients an early, actionable signal to retry or route elsewhere. Choose based on whether you prefer to buffer load or shed and redirect it.
+ **Client retry behavior** — When the queue is full, `StartJobRun` returns a `ValidationException`. Make sure that your submitters handle this exception — retry with backoff, or route the workload to another virtual cluster. Set the depth so that rejections occur only during genuine overload, not during routine operation.

### Considerations for concurrent job limits
<a name="virtual-cluster-job-concurrency-considerations"></a>
+ No limits are applied by default. Existing virtual clusters and workloads are unaffected unless you explicitly set `schedulerConfiguration`.
+ Because the counters are maintained across a distributed system, you can sometimes expect a small transient delta from the true value. Internal reconciliation corrects any drift.
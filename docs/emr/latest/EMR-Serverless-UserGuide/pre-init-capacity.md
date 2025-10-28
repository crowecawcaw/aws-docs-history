# Pre-initialized capacity for working with an application in EMR Serverless

EMR Serverless provides an optional feature that keeps driver and workers pre-initialized
and ready to respond in seconds. This effectively creates a warm pool of workers for an
application. This feature is called _pre-initialized capacity_. To
configure this feature, set the `initialCapacity` parameter of an
application to the number of workers you want to pre-initialize. With pre-initialized worker
capacity, jobs start immediately. This is ideal when you want to implement iterative
applications and time-sensitive jobs.

Pre-initialized capacity keeps a warm pool of workers ready for jobs and sessions to startup in seconds. You will be paying
for provisioned pre-initialized workers even when the application is idle, hence we suggest enabling it for use cases
that benefit from the fast start-up time and sizing it for optimal utilization of resources. EMR Serverless applications automatically shut down
when idle. We suggest keeping this feature on when using pre-initialized workers to avoid unexpected charges.

When you submit a job, if workers from `initialCapacity` are available, the job
uses those resources to start its run. If those workers are already in use by other jobs, or
if the job needs more resources than available from `initialCapacity`, then the
application requests and gets additional workers, up to the maximum limits on resources set
for the application. When a job finishes its run, it releases the workers that it used, and
the number of resources available for the application returns to `initialCapacity`.
An application maintains the `initialCapacity` of resources even after jobs finish
their runs. The application releases excess resources beyond `initialCapacity` when
the jobs no longer need them to run.

Pre-initialized capacity is available and ready to use when the application has started.
The pre-initialized capacity becomes inactive when the application is stopped. An application
moves to the `STARTED` state only if the requested pre-initialized capacity has
been created and is ready to use. The whole time that the application is in the
`STARTED` state, EMR Serverless keeps the pre-initialized capacity available for
use or in use by jobs or interactive workloads. The feature restores capacity for released or
failed containers. This maintains the number of workers that the `InitialCapacity`
parameter specifies. The state of an application with no pre-initialized capacity can
immediately change from `CREATED` to `STARTED`.

You can configure the application to release pre-initialized capacity if it isn't used
for a certain period of time, with a default of 15 minutes. A stopped application starts
automatically when you submit a new job. You can set these automatic start and stop
configurations when you create the application, or change them when the application is
in a `CREATED` or `STOPPED` state.

You can change the `InitialCapacity` counts, and specify compute configurations
such as CPU, memory, and disk, for each worker. Because you can't make partial modifications,
specify all compute configurations when you change values. You can only change
configurations when the application is in the `CREATED` or `STOPPED`
state.

###### Note

To optimize your application’s use of resources, we suggest aligning your container
sizes with your pre-initialized capacity worker sizes. For example, if you configure your
Spark executor size to 2 CPUs and your memory to 8 GB, but your pre-initialized
capacity worker size is 4 CPUs with 16 GB of memory, then the Spark executors only
use half of the workers’ resources when they are assigned to this job.

## Customizing pre-initialized capacity for Spark and

Hive

You can further customize pre-initialized capacity for workloads that run on specific
big data frameworks. For example, when a workload runs on Apache Spark, specify how
many workers start as drivers and how many start as executors. Similarly, when you use
Apache Hive, specify how many workers start as Hive drivers, and how many should run
Tez tasks.

**Configuring an application running Apache Hive with pre-initialized
capacity**

The following API request creates an application running Apache Hive based on Amazon EMR
release emr-6.6.0. The application starts with 5 pre-initialized Hive drivers, each with
2 vCPU and 4 GB of memory, and 50 pre-initialized Tez task workers, each with
4 vCPU and 8 GB of memory. When Hive queries run on this application, they first
use the pre-initialized workers and start executing immediately. If all of the
pre-initialized workers are busy and more Hive jobs are submitted, the application can scale
to a total of 400 vCPU and 1024 GB of memory. You can optionally omit capacity for
either the `DRIVER` or the `TEZ_TASK` worker.

```
aws emr-serverless create-application \
  --type "HIVE" \
  --name `my-application-name` \
  --release-label emr-6.6.0 \
  --initial-capacity '{
    "DRIVER": {
        "workerCount": 5,
        "workerConfiguration": {
            "cpu": "2vCPU",
            "memory": "4GB"
        }
    },
    "TEZ_TASK": {
        "workerCount": 50,
        "workerConfiguration": {
            "cpu": "4vCPU",
            "memory": "8GB"
        }
    }
  }' \
  --maximum-capacity '{
    "cpu": "400vCPU",
    "memory": "1024GB"
  }'
```

**Configuring an application running Apache Spark with pre-initialized capacity**

The following API request creates an application that runs Apache Spark 3.2.0 based on
Amazon EMR release 6.6.0. The application starts with 5 pre-initialized Spark drivers, each with
2 vCPU and 4 GB of memory, and 50 pre-initialized executors, each with
4 vCPU and 8 GB of memory. When Spark jobs run on this application, they first use
the pre-initialized workers and start to execute immediately. If all of the pre-initialized
workers are busy and more Spark jobs are submitted, the application can scale to a total of
400 vCPU and 1024 GB of memory. You can optionally omit capacity for either the
`DRIVER` or the `EXECUTOR`.

###### Note

Spark adds a configurable memory overhead, with a 10% default value, to the memory
requested for driver and executors. For jobs to use pre-initialized workers, the initial
capacity memory configuration should be greater than the memory that the job and the
overhead request.

```
aws emr-serverless create-application \
  --type "SPARK" \
  --name `my-application-name` \
  --release-label emr-6.6.0 \
  --initial-capacity '{
    "DRIVER": {
        "workerCount": 5,
        "workerConfiguration": {
            "cpu": "2vCPU",
            "memory": "4GB"
        }
    },
    "EXECUTOR": {
        "workerCount": 50,
        "workerConfiguration": {
            "cpu": "4vCPU",
            "memory": "8GB"
        }
    }
  }' \
  --maximum-capacity '{
    "cpu": "400vCPU",
    "memory": "1024GB"
  }'
```

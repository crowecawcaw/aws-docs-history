# Job concurrency and queuing for an EMR Serverless application

Starting with Amazon EMR version 7.0.0 and later, specify job run queue timeout and concurrency configuration
for your application. When you specify this configuration, Amazon EMR Serverless starts by queuing your job and begins execution
based on concurrency utilization on your application. For example, if your job run concurrency is 10, only ten jobs are
run at a time on your application. Remaining jobs are queued until one of the running jobs terminates. If queue timeout is reached
earlier, your job times out. For more information, refer to [Job run states](job-states.md "job-states.md").

## Key benefits of concurrency and queuing

Job concurrency and queuing provides the following benefits when many job submissions
are required:

- It helps control concurrent executing jobs to efficiently use your application level capacity limits.
- The queue can contain a sudden burst of job submissions, with a configurable timeout setting.

## Getting started with concurrency and queuing

The following procedures demonstrate a couple different ways to implement concurrency and queuing.

**Using the AWS CLI**

1. Create an Amazon EMR Serverless application with queue timeout and concurrent job runs:

```
aws emr-serverless create-application \
--release-label emr-7.0.0 \
--type SPARK \
--scheduler-configuration '{"maxConcurrentRuns": 1, "queueTimeoutMinutes": 30}'
```

2. Update an application to change the job queue timeout and concurrency:

```
aws emr-serverless update-application \
--application-id `application-id` \
--scheduler-configuration '{"maxConcurrentRuns": 5, "queueTimeoutMinutes": 30}'
```

###### Note

You can update your existing application to enable job concurrency and queuing. To do this, the application must have a release label _emr-7.0.0_ or later.

**Using the AWS Management Console**

The following steps demonstrate how to get started with job concurrency and queuing, using the AWS Management Console:

1. Go to EMR Studio and choose to create an application with release label EMR-7.0.0 or higher.
2. Under **Application setup options**, select the option **Use custom settings**.
3. Under **Additional configurations** there is a section for **Job Run Settings**. Select the option **Enable job concurrency** to
   enable the feature.
4. After selection, select **Concurrent job runs** and **Queue timeout** to configure the number of concurrent
   job runs and queue timeout, respectively. If you do not enter values for these settings, the default values are used.
5. Choose **Create Application** and the application will be created with this feature enabled. To verify, go to the dashboard,
   select your application and check under properties tab to determine if the feature is enabled.

Following configuration, submit jobs with this feature enabled.

## Considerations for concurrency and queuing

Take the following into consideration when you implement concurrency and queuing:

- Job concurrency and queuing is supported on Amazon EMR release 7.0.0 and higher.
- Job concurrency and queuing is enabled by default on Amazon EMR release 7.3.0 and higher.
- You cannot update concurrency for an application in the **STARTED** state.
- The valid range for `maxConcurrentRuns` is 1 to 1000, and for `queueTimeoutMinutes` it is 15 to 720.
- A maximum of 2000 jobs can be in the **QUEUED** state for an account.
- Concurrency and queuing applies to batch and streaming jobs. It cannot be used for interactive jobs. For more information,
  refer to [Run interactive workloads with EMR Serverless through EMR Studio](interactive-workloads.md "interactive-workloads.md").

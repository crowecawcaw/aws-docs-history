# Search AWS Batch for jobs in a job queue

You can search and filter your jobs in AWS Batch using Job search. This feature provides an
option to search within an existing job queue and filter its jobs.

Search and filter are able to retrieve jobs that are not in a terminal state
(`SUCCEEDED` or `FAILED`). Once a job's state is `SUCCEEDED`
or `FAILED` you should be able to retrieve the job for up to seven days. You are
still able to view a job's CloudWatch or Amazon EventBridge logs.

To search using multiple criteria simultaneously, use the **Advanced
search** feature. For example, you can include any or all of the following filters:
**Status**, **Date range**, and **Additional
criteria** (such as, a job name, job definition, or job ID).

## Search AWS Batch jobs (AWS Console)

Use this procedure to search the jobs in a job queue in the AWS Batch console.

1. Navigate to the [AWS Batch console](https://console.aws.amazon.com/batch/home "https://console.aws.amazon.com/batch/home").
2. In the Navigation pane, choose **Jobs**.
3. Turn on **Advanced search**.
4. Expand the **Job queue** dropdown list and choose the job queue that
   you want to search within.

###### Note

You can search for jobs within only one job queue at a time. 5. For **Search options**:

    1. For the **Status** dropdown list you can choose one or more
     statuses to filter on. For more information, see [Job states](job_states.md "job_states.md") and [Service job status](service-job-status.md "service-job-status.md").


    ###### Note

    Array job parents are updated to `PENDING` when any child job is updated to `RUNNABLE` and remain in `PENDING` status while child jobs are running. To view these jobs, filter by `PENDING` status until all child jobs reach a terminal state.
    2. Choose **Date range** to filter the results based on a date and
     time range.




    	* Choose **Relative mode** to search for jobs that have a
    	 created date within a time range counting backwards from the current date and
    	 time.
    	* Choose **Absolute mode** to search for jobs that have a
    	 created date within a date and time range that you specify.
    3. In the **Additional criteria** field, enter keywords to include
     in the search results. For example, you can use this field to search by **Job
     name**, **Job definition**, or **Job
     ID**. Depending on the property, there may be additional operators, such as
     equals (=) or contains (:) that you must define.


    ###### Note

    SageMaker Training job queues only support filtering by **Job
     name** and **Job ID**

6. Choose **Search**.

## Search and filter AWS Batch jobs (AWS CLI)

Use this procedure to list all the jobs in a job queue with the AWS CLI. Optionally, use the
**-filters** parameter to narrow the results based on the criteria you
specify.

Search job queue (AWS CLI)
You can use the [list-jobs](../../../cli/latest/reference/batch/list-jobs.md "../../../cli/latest/reference/batch/list-jobs.md") command to search
and filter a job queue.

For example you can search a job queue based on the job name:

```
aws batch list-jobs \
    --job-queue `my-job-queue` \
    --filters name=JOB_NAME,values="`my-job`"
```

In the preceding command, make the following changes:

- Replace `my-job-queue` with the name of your job queue.
- Replace `my-job` with the name of your job.

Search service job queue (AWS CLI)
You can use the [list-service-jobs](../../../cli/latest/reference/batch/list-service-jobs.md "../../../cli/latest/reference/batch/list-service-jobs.md")
command to search and filter a service job queue.

For example you can search a service job queue based on the job name:

```
aws batch list-service-jobs \
    --job-queue `my-sm-queue` \
    --filters name=JOB_NAME,values="`my-sm-job`"
```

In the preceding command, make the following changes:

- Replace `my-sm-queue` with the name of your service job queue.
- Replace `my-sm-job` with the name of your service job.

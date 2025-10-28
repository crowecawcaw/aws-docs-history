# Setting job priority

Within a queue, AWS Elemental MediaConvert processes jobs in parallel until all the resources
available to the queue are used. After a job finishes and the resources are again
available in the queue, MediaConvert selects the next job to process based on the job's
_priority_.

You specify priority when you create a job. MediaConvert processes jobs in each queue
according to each job's priority, starting with the highest number. If more than one job
has the highest value for priority, MediaConvert chooses among them by selecting the
one that you submitted first.

MediaConvert doesn't stop the current job when you submit a job with a higher
priority. When the running job is finished, MediaConvert starts the next job based
on its relative priority in the queue.

After you create a job, you cannot change or update its priority. However, you can specify
a new priority for jobs that hop queues. For additional information, see [Setting priority for hopped jobs](job-priority-and-queue-hopping.md "job-priority-and-queue-hopping.md"). The following tabs show different
options for setting a job's priority.

Console
To set a job's priority in the MediaConvert console:

1. On the **Create job** page, choose **Job
   management**.
2. For **Priority**, enter a number from -50 to 50. MediaConvert
   processes jobs with the highest value for
   **Priority** first. If you don't specify a
   value, MediaConvert assigns the default value of 0.

API, SDK, or the AWS CLI
To set a job's priority in the API, SDK, or the AWS CLI, specify the
`priority` property. This property is a direct child of
`Jobs`, which is in the top level of the JSON job
specification. Set the value of `Priority` to an integer in the
range from -50 to 50, inclusive. The default value is 0.

The following is an excerpt of a job settings JSON with `Priority` set to 10.

```
{
    "Settings": {
        "OutputGroups": `[...]`,
        "Inputs": `[...]`
    },
    "Priority": `10`
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-prop-createjobrequest-priority "../apireference/jobs.md#jobs-prop-createjobrequest-priority").

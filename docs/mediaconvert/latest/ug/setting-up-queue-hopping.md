# Setting up queue hopping

When you set up queue hopping, you specify the _submission
queue_, the _wait time_, and the
_destination queue_. Typically, the submission
queue is a reserved queue and the destination queue is an on-demand queue. The
following tabs show different options for setting up queue hopping.

Console
To set up queue hopping in the MediaConvert console:

1. On the **Create job** page, choose **Job
   management**.
2. Enable **Queue hopping**.
3. Enter the amount of time until your job can hop with **Wait
   minutes**.
4. For **Destination queue**, choose the queue that you want your job
   to hop to if it stays in the submission queue beyond its wait
   time.
5. Optionally, specify a new **Job priority** if your job hops to its
   destination queue. For more information, see [Setting priority for hopped jobs](job-priority-and-queue-hopping.md "job-priority-and-queue-hopping.md").

API, SDK, or the AWS CLI
To set up queue hopping in the API, SDK, or the AWS CLI, configure the
settings for queue hopping under `HopDestinations`. This
property is a direct child of `Jobs`, which is in the top
level of the JSON job specification.

The following is an excerpt of a job settings JSON that hops to an on-demand queue after
10 minutes.

```
{
    "Settings": {
        "OutputGroups": `[...]`,
        "Inputs": `[...]`
    },
    "HopDestinations": [
        {
        "WaitMinutes": `10`,
        "Queue": `"arn:aws:mediaconvert:us-west-2:111122223333:queues/ondemandqueue"`,
        "Priority": `0`
        }
    ]
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-model-hopdestination "../apireference/jobs.md#jobs-model-hopdestination").

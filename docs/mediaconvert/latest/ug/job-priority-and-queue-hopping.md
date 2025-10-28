# Setting priority for hopped jobs

When you set up a job for queue hopping, you can specify the priority for the job
in the new queue. If you don't specify a new priority, the job keeps the priority
number from its submission queue.

If you use different guidelines for choosing the values for `priority`
between the two queues, make sure to specify a new priority value for the job in the
destination queue.

For information about setting the job's priority within the submission queue, see
[Setting job priority](setting-the-priority-of-a-job.md "setting-the-priority-of-a-job.md").

The following tabs provide different options for setting the priority of a hopped
job.

Console
To set the priority of a hopped job in the MediaConvert
console:

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page
   in the MediaConvert console.
2. Choose **Job management** from the
   **Job settings** menu.
3. Enable **Queue hopping**.
4. Enter the **Job priority** for when your job
   hops to its destination queue.
5. Enter both **Wait minutes** and
   **Destination queue**. For more
   information, see [Moving a job to a different queue](setting-up-queue-hopping-to-avoid-long-waits.md "setting-up-queue-hopping-to-avoid-long-waits.md").

API, SDK, or the AWS CLI
You can set up a hopped jobs new priority by using the API, SDK, or
the AWS CLI. To set it up, configure `Priority` under
`HopDestinations`. This property is a direct child of
`Jobs`, which is in the top level of the JSON job
specification.

The following is an excerpt of a job settings JSON that sets a hopped
job's priority to 25.

```
{
	"Settings": {
		"OutputGroups": [...],
		"Inputs": [...]
	},
	"HopDestinations": [
		{
			"WaitMinutes": 10,
			"Queue": "arn:aws:mediaconvert:us-west-2:111122223333:queues/ondemandqueue",
			"Priority": 25
		}
	]
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-model-hopdestination "../apireference/jobs.md#jobs-model-hopdestination").

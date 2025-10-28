# Viewing hopped job history

When a job hops queues, the values for the settings `queue` and
`priority` remain how you set them when you created the job. You
can see the values for the job's post-hop destination and queue priority. The
following tabs provide two options for viewing a job's history and queue
priority.

Console
To see if your job hopped queues by using the MediaConvert
console:

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in the
   MediaConvert console.
2. Select a **Job ID**.
3. Find the **Queue transition** section that
   shows the job priority before and after hopping. That section
   also shows the epoch **Timestamp** for when the
   job hopped, the **Source queue**, and the
   **Destination queue**.

AWS CLI
The following `get-job` example returns a JSON response
with information about your job.

```
aws mediaconvert get-job \
	--id `1234567890123-efg456`
```

The following is an excerpt showing `QueueTransitions` in
the JSON response when you run this command. The response shows your
job's submission queue and destination queue.

```
"QueueTransitions": [
	{
		"Timestamp": 1672662636,
		"SourceQueue": arn:aws:mediaconvert:us-west-2:111122223333:queues/submissionqueue,
		"DestinationQueue": arn:aws:mediaconvert:us-west-2:111122223333:queues/destinationqueue
	}
]
```

For more information about how to use the `get-job`
command, see the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/get-job.html").

###### Billing tags for hopped jobs

If you use billing tags on your jobs and set your billing tags source to
**Queue**, the charges for your jobs are always listed
under the tags for the submission queue. To track how much you were billed for a
job that hops queues, you can set the billing tags source to
**Job**. For more information about using tags to sort your
AWS bill, see [Setting up AWS Elemental MediaConvert resources
for cost allocation through tagging](setting-up-resources-for-catt.md "setting-up-resources-for-catt.md").

###### Note

Cost allocation based on queue only applies to jobs that run in on-demand queues. When
your submission queue is a reserved queue and your job hops to an on-demand
queue, the charges for that on-demand job appear in your cost allocation report.
If you don't put tags on your reserved queue, those charges appear in the report
unsorted.

###### Listing hopped jobs

When you view your job, MediaConvert displays the queue that you submitted
your job. For example, if you submit a job to `Queue1`, and it hops
to `Queue2`, that job appears in lists that are filtered for
`Queue1`. It doesn't appear in lists filtered for
`Queue2`.

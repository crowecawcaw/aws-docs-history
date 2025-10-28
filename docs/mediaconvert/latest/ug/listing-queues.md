# Viewing on-demand queue details

You can list the queues that are associated with your AWS account and get details about
those queues.

These details include ARN, name, status, description, job count information, and
more. The following tabs show different options for viewing queue details.

Console
To view details about your on-demand queues by using the MediaConvert console, open the
[Queues](https://console.aws.amazon.com/mediaconvert/home#/queues/list "https://console.aws.amazon.com/mediaconvert/home#/queues/list") page. Select a queue to view its ARN.

AWS CLI
The following `list-queues` example lists all of your
queues.

```
aws mediaconvert list-queues
```

The following JSON is an example list-queues response.

```
{
	"Queues": [
		{
			"Arn": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Example",
			"CreatedAt": "2023-06-19T09:34:25-07:00",
			"LastUpdated": "2023-06-19T09:34:25-07:00",
			"Name": "Example",
			"PricingPlan": "ON_DEMAND",
			"ProgressingJobsCount": 0,
			"Status": "ACTIVE",
			"SubmittedJobsCount": 0,
			"ConcurrentJobs" 700,
			"TotalConcurrentJobs" 1000,
			"unallocatedConcurrentJobs" 100,
			"Type": "CUSTOM"
		},
		{
			"Arn": "arn:aws:mediaconvert:us-west-2:111122223333:queues/Default",
			"CreatedAt": "2018-05-16T09:13:08-07:00",
			"LastUpdated": "2021-05-14T15:39:23-07:00",
			"Name": "Default",
			"PricingPlan": "ON_DEMAND",
			"ProgressingJobsCount": 0,
			"Status": "ACTIVE",
			"SubmittedJobsCount": 0,
			"ConcurrentJobs" 200,
			"TotalConcurrentJobs" 1000,
			"unallocatedConcurrentJobs" 100,
			"Type": "SYSTEM"
		}
	]
}
```

For more information about how to list queues by using the AWS CLI, see
the [AWS CLI Command Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/list-queues.html").

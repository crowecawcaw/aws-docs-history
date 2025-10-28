# Using accelerated transcoding with

hopped jobs

To reduce the transcoding time for certain jobs, use accelerated transcoding. In most
cases, you submit accelerated jobs to on-demand queues, because reserved queues
cannot run accelerated jobs. However, you can submit a job with
**Accelerated transcoding** set **Preferred**
to a reserved queue. When you do, if the job hops to an on-demand queue, it will run
with acceleration enabled. For more information about accelerated transcoding, see
[Accelerated transcoding](accelerated-transcoding.md "accelerated-transcoding.md") in the
MediaConvert User Guide.

The following tabs provide different options for setting accelerated
transcoding.

Console
To set **Acceleration** to
**Preferred** in MediaConvert console:

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page
   in the MediaConvert console.
2. Choose **Job management** from the
   **Job settings** menu.
3. Under **Acceleration**, choose
   **Preferred** by using the dropdown
   list.

API, SDK, or the AWS CLI
To specify preferred acceleration by using the API, SDK, or the AWS CLI,
configure `Mode` under `AccelerationSettings`.
This property is a direct child of `Jobs`, which is in the
top level of the JSON job specification.

The following is an excerpt of a job settings JSON that specifies
queue hopping to an on-demand queue with accelerated transcoding.

```
{
	"Settings": {
		"OutputGroups": `[...]`,
		"Inputs": `[...]`
	},
	"AccelerationSettings": {
		"Mode": "`PREFERRED`"
	},
	"HopDestinations": [
		{
			"WaitMinutes": `10`,
			"Queue": `"arn:aws:mediaconvert:us-west-2:111122223333:queues/ondemandqueue"`,
			"Priority": `25`
		}
	]
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-model-accelerationsettings "../apireference/jobs.md#jobs-model-accelerationsettings").

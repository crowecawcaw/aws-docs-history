# Simulating a reserved queue

You can run a job in a _simulated_ reserved queue to test its performance. When you do, MediaConvert runs your job from an on-demand queue with similar performance to what you will see with one RTS in a reserved queue. Take note of how long you job takes to complete and use this job completion time when calculating how many RTS you need.

Console
To simulate a job's reserved queue performance using the MediaConvert
console:

1. Open the [Create job](https://console.aws.amazon.com/mediaconvert/home#/jobs/create "https://console.aws.amazon.com/mediaconvert/home#/jobs/create") page
   in the MediaConvert console.
2. Choose **Job management** on the left menu
   under **Job settings**.
3. Set **Simulate reserved queue** to
   **Enabled**.

API, SDK, or the AWS CLI
To simulate a job's reserved queue performance using the API, SDK, or
AWS Command Line Interface (AWS CLI), set
`SimulateReservedQueue` to `ENABLED`. This
property is a direct child of `Jobs`, which is in the top
level of the JSON job specification. The default value is
`DISABLED`.

The following is an excerpt of a job settings JSON with
`SimulateReservedQueue` set to
`ENABLED`.

```
{
    "Settings": {
        "OutputGroups": `[...]`,
        "Inputs": `[...]`
    },
	"SimulateReservedQueue": `"ENABLED"`
}
```

For more information, see the MediaConvert [API Reference](../apireference/jobs.md#jobs-model-simulatereservedqueue "../apireference/jobs.md#jobs-model-simulatereservedqueue").

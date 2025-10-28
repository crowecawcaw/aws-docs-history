# Submit an AWS Batch array job

After you registered your job definition, you can submit an AWS Batch array job that uses your new container
image.

###### To submit an AWS Batch array job

1. Create a file named `print-color-job.json` in your workspace directory and paste the
   following into it.

###### Note

This example uses the job queue mentioned in the [Prerequisites](array-tutorial-prereqs.md "array-tutorial-prereqs.md")
section.

```
{
  "jobName": "print-color",
  "jobQueue": "``existing-job-queue``",
  "arrayProperties": {
    "size": 7
  },
  "jobDefinition": "print-color"
}
```

2. Submit the job to your AWS Batch job queue. Note the job ID that's returned in the output.

```
`$` `aws batch submit-job --cli-input-json file://print-color-job.json`
```

3. Describe the job's status and wait for the job to move to `SUCCEEDED`.

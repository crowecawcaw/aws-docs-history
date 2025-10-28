# Tutorial: Test your rule

To test your rule, submit a job that exits shortly after it starts with a non-zero exit code. If your event
rule is configured correctly, you should receive an email message within a few minutes with the event text.

###### To test a rule

1. Open the AWS Batch console at
   [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. Submit a new AWS Batch job. For more information, see [Tutorial: submit a job](submit_job.md "submit_job.md").
   For the job's command, substitute this command to exit the container with an exit code of 1.

```
`/bin/sh, -c, 'exit 1'`
```

3. Check your email to confirm that you received an email alert for the failed job notification.

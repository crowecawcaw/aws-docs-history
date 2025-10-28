# Submit an Amazon EKS MNP job

To submit a job using the registered job definition, enter the following command. Replace
the value of <EKS_JOB_QUEUE_NAME> with the name or ARN of a pre-existing job queue
associated with an Amazon EKS compute environment.

```
aws batch submit-job --job-queue `<EKS_JOB_QUEUE_NAME>` \
    --job-definition MyEksMnpJobDefinition \
    --job-name myFirstEksMnpJob
```

You will receive the following JSON response.

```
{
    "jobArn": "arn:aws:batch:`region`:`account`:job/9b979cce-9da0-446d-90e2-ffa16d52af68",
    "jobName": "myFirstEksMnpJob",
    "jobId": "`<JOB_ID>`"
}
```

You can check the status of the job using the returned jobId with the following
command.

```
aws batch describe-jobs --jobs `<JOB_ID>`
```

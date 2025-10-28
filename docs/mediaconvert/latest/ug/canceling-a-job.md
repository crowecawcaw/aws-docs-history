# Canceling a job

The following procedure explains how to cancel a job using the AWS Elemental MediaConvert console.

Console
To cancel a job using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in
   the MediaConvert console.
2. Select the **Job ID** of the job that you want to
   cancel by choosing the option (
   ![Empty circle outline representing a placeholder or selection option.](images/circle-icon.png)
   ) next to it.
3. Choose **Cancel job**.

CLI
The following `cancel-job` example cancels a job.

```
aws mediaconvert cancel-job \
	--id `1234567890123-efg456`
```

For more information about how to cancel a job using the AWS CLI, see
the [AWS CLI command reference](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediaconvert/cancel-job.html").

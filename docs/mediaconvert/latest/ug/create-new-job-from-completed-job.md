# Duplicating a job

To create a job that is similar to one that you ran before, you can duplicate a job from
your job history. You can also modify any settings if you want to change them.

###### To create a job based on a recent job using the MediaConvert console

1. Open the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in the MediaConvert console.
2. Choose the **Job ID** of the job that you want to duplicate.
3. Choose **Duplicate**.
4. Optionally modify any job settings.

Settings that are likely to change from job to job include the following: input file
location, output destination locations, and output name modifiers. If you run
transcoding jobs for your customers who have different AWS accounts from your
account, you also must change the **IAM role** under
**Job settings**. 5. Choose **Create** at the bottom of the page.

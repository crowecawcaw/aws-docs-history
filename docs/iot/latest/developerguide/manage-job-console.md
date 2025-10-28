# Create and manage jobs by using the

AWS Management Console

This section describes how you can create and manage jobs from the AWS IoT console. After
you've created a job, you can view information about the job on the details page, and manage
the job.

###### Note

If you want to perform code signing for AWS IoT jobs, use the AWS CLI. For more
information, see [Create and manage jobs by using the AWS CLI](manage-job-cli.md "manage-job-cli.md").

###### Topics

- [Create manage jobs by using the
  AWS Management Console](#create-job-console "#create-job-console")
- [View and manage jobs by using the
  AWS Management Console](#view-manage-job-console "#view-manage-job-console")

## Create manage jobs by using the

AWS Management Console

To create a job, log in to the AWS IoT console, and go to the [Jobs hub](https://console.aws.amazon.com/iot/home#/jobhub "https://console.aws.amazon.com/iot/home#/jobhub") in the **Remote
Actions** section. Then, perform the following steps.

1. On the **Jobs** page, in the **Jobs** dialog
   box, choose **Create job**.
2. Depending on the device that you're using, you can create a custom job, a
   FreeRTOS OTA update job, or an AWS IoT Greengrass job. For this
   example, choose **Create a custom job**. Choose
   **Next**.
3. On the **Custom job properties** page, in the **Job
   properties** dialog box, enter your information for the following
   fields:
   - **Name**: Enter a unique, alphanumeric job
     name.
   - **Description - optional**: Enter an optional
     description about your Job.
   - **Tags - optional**:

###### Note

We recommend that you don't use personally identifiable information in
your job IDs and description.

Choose
**Next**. 4. On the **File configuration** page in the **Job
targets** dialog box, select the **Things** or
**Thing groups** that you want to run this job.

In the **Job document** dialog box, select one of the
following options:

    * **From file**: A JSON job file you previously
     uploaded to an Amazon S3 bucket




    	+ **Code signing**


    	In the job document located in your Amazon S3 URL,
    	 `${aws:iot:code-sign-signature:s3://region.bucket/code-file@code-file-version-id}`
    	 is required as a placeholder until it is replaced with the
    	 signed code file path using your **Code signing
    	 profile**. The new signed code file will initially
    	 appear in a `SignedImages` folder in your Amazon S3 source
    	 bucket. A new job document containing a `Codesigned_`
    	 prefix will be created with the signed code file path replacing
    	 the code-sign placeholder and placed in your Amazon S3 URL for
    	 creating a new job.
    	+ **Pre-sign resource URLs**


    	In the **Pre-signing role** drop down, choose
    	 the IAM role you created in [Presigned URLs](create-manage-jobs.md#create-manage-jobs-presigned-URLs "create-manage-jobs.md#create-manage-jobs-presigned-URLs"). Using
    	 `${aws:iot:s3-presigned-url:` to presign URLs for
    	 objects located in Amazon S3 is a best security practice for devices
    	 downloading objects from Amazon S3.


    	If you want to use presigned URLs for a code signing
    	 placeholder, use the following example template:



    	```
    	    ${aws:iot:s3-presigned-url:${aws:iot:code-sign-signature:<S3 URL>}
    	```
    * **From template**: A job template containing a job
     document and job configurations. The job template can be a custom job
     template you created or an AWS managed template.


     If you're creating a job for performing frequently used remote
     actions such as rebooting your device, you can use an AWS managed
     template. These templates have already been preconfigured for use. For
     more information, see [Create a custom job
     template](job-templates-console.md#job-templates-console-create "job-templates-console.md#job-templates-console-create") and [Create custom job
     templates from managed templates](job-template-manage-console-create.md#job-template-manage-create-template "job-template-manage-console-create.md#job-template-manage-create-template").

5.  On the **Job configuration** page in the **Job
    configuration** dialog box, select one of the following job
    types:
    - **Snapshot job**: A snapshot job is complete when
      it's finished its run on the target devices and groups.
    - **Continuous job**: A continuous job applies to thing
      groups and runs on any device that you later add to a specified target
      group.

6.  In the **Additional configurations - optional** dialog
    box, review the following optional Job configurations and make your selections
    accordingly:

        * **Rollout configuration**
        * **Scheduling configuration**
        * **Job executions timeout configuration**
        * **Job executions retry configuration - new**
        * **Abort configuration**

    Refer to the following sections for additional information on Job
    configurations:

        * [Job rollout, scheduling, and abort
         configurations](jobs-configurations-details.md#job-rollout-abort-scheduling "jobs-configurations-details.md#job-rollout-abort-scheduling")
        * [Job execution timeout and retry
         configurations](jobs-configurations-details.md#job-timeout-retry "jobs-configurations-details.md#job-timeout-retry")

    Review all of your job selections and then choose **Submit**
    to create your job.

## View and manage jobs by using the

AWS Management Console

After you create the job, the console generates a JSON signature and places it in
your job document. You can use the [AWS IoT console](https://console.aws.amazon.com/iot/ "https://console.aws.amazon.com/iot/")
to view the status, cancel, or delete a job.

If you choose the job that you created, you can find:

- General job details, such as the job name, description, type, the time when it was
  created, last updated, and the estimated start time.
- Any job configurations that you specified and their status.
- The job document.
- The job executions and any optional tags that you specified.

To manage jobs, go to the
[Job hub of the console](https://console.aws.amazon.com/iot/home#/jobhub "https://console.aws.amazon.com/iot/home#/jobhub") and
choose whether you want to edit, delete, or cancel the job.

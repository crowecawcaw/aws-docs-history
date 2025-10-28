# Create custom job templates by using the

AWS Management Console

This topic explains how to create, delete, and view details about job templates by
using the AWS IoT console.

## Create a custom job

template

You can either create
an
original custom job template or create a job template from an
existing job. You can also create a custom job template from an existing job
that was created using an AWS managed template. For more information, see
[Create custom job
templates from managed templates](job-template-manage-console-create.md#job-template-manage-create-template "job-template-manage-console-create.md#job-template-manage-create-template").

1. ###### Start creating your job template
   1. Go to the [Job templates hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobtemplatehub "https://console.aws.amazon.com/iot/home#/jobtemplatehub") and
      choose the **Custom templates**
      tab.
   2. Choose **Create job
      template**.

###### Note

You can also navigate to the **Job
templates** page from the **Related
services** page under **Fleet
Hub**. 2. ###### Specify job template properties

In the **Create job template** page, enter an
alphanumeric identifier for your job name and an alphanumeric
description to provide additional details about the
template.

###### Note

We don't recommend using personally identifiable
information in your job IDs or descriptions. 3. ###### Provide job document

Provide a JSON job file that is either stored in an S3 bucket
or as an inline job document that is specified within the job.
This job file will become the job document when you create a job
using this template.

If the job file is stored in an S3 bucket, enter the S3 URL or
choose **Browse S3**, and then navigate to your
job document and select it.

###### Note

You can select only S3 buckets in your current
Region. 4. Continue to add any additional configurations for your job and
then review and create your job. For information about the
additional, optional configurations, refer to the following
links:

    * [Job rollout, scheduling, and abort
     configurations](jobs-configurations-details.md#job-rollout-abort-scheduling "jobs-configurations-details.md#job-rollout-abort-scheduling")
    * [Job execution timeout and retry
     configurations](jobs-configurations-details.md#job-timeout-retry "jobs-configurations-details.md#job-timeout-retry")

1. ###### Choose your job
   1. Go to the [Job
      hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobhub "https://console.aws.amazon.com/iot/home#/jobhub") and choose the job
      that you want to use as the basis for your job
      template.
   2. Choose **Save as a job
      template**.

###### Note

Optionally, you can choose a different job document or
edit the advanced configurations from the original job, and
then choose **Create job template**. Your
new job template appears on the **Job
templates** page. 2. ###### Specify job template properties

In the **Create job template** page, enter an
alphanumeric identifier for your job name and an alphanumeric
description to provide additional details about the
template.

###### Note

The job document is the job file that you specified when
creating the template. If the job document is specified
within the job instead of an S3 location, you can see the
job document in the details page of this job. 3. Continue to add any additional configurations for your job and
then review and create your job. For information about the
additional configurations, see:

    * [Job rollout, scheduling, and abort
     configurations](jobs-configurations-details.md#job-rollout-abort-scheduling "jobs-configurations-details.md#job-rollout-abort-scheduling")
    * [Job execution timeout and retry
     configurations](jobs-configurations-details.md#job-timeout-retry "jobs-configurations-details.md#job-timeout-retry")

## Create a job from a

custom job template

You can create a job from a custom job template by going to the details page
of your job template as described in this topic. You can also create a job or by
choosing the job template you want to use when running the job creation
workflow. For more information, see [Create and manage jobs by using the
AWS Management Console](manage-job-console.md "manage-job-console.md").

This topic shows how to create a job from the details page of a custom job
template. You can also create a job from an AWS managed template. For more
information, see [Create a job using managed
templates](job-template-manage-console-create.md#job-template-manage-create-job "job-template-manage-console-create.md#job-template-manage-create-job").

1. ###### Choose your custom job template

Go to the [Job
templates hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobtemplatehub "https://console.aws.amazon.com/iot/home#/jobtemplatehub") and choose the
**Custom templates** tab, and then choose your
template. 2. ###### Create a job using your custom template

To create a job:

    1. In the details page of your template, choose **Create
     job**.


    The console switches to the **Custom job
     properties** step of the **Create
     job** workflow where your template configuration
     has been added.
    2. Enter a unique alphanumeric job name, and optional description
     and tags, and then choose **Next**.
    3. Choose the things or thing groups as job targets that you want
     to run in this job.


    In the **Job document** section, your
     template is displayed with its configuration settings. If you
     want to use a different job document, choose
     **Browse** and select a different bucket
     and document. Choose **Next**.
    4. On the **Job configuration** page, choose the
     job type as
     continuous
     or a snapshot job. A snapshot job is complete when it finishes
     its run on the target devices and groups. A continuous job
     applies to thing groups and runs on any device that you add to a
     specified target group.
    5. Continue to add any additional configurations for your job and
     then review and create your job. For information about the
     additional configurations, see:




    	* [Job rollout, scheduling, and abort
    	 configurations](jobs-configurations-details.md#job-rollout-abort-scheduling "jobs-configurations-details.md#job-rollout-abort-scheduling")
    	* [Job execution timeout and retry
    	 configurations](jobs-configurations-details.md#job-timeout-retry "jobs-configurations-details.md#job-timeout-retry")

###### Note

When
a job created from a job template updates the existing parameters provided
by the job template, those updated parameters will override the existing
parameters provided by the job template for that
job.

You can also create jobs from job templates with Fleet Hub web
applications. For information about creating jobs in Fleet Hub, see [Working
with job templates in Fleet Hub for AWS IoT Device Management](../fleethubuserguide/aws-iot-monitor-technician-job-templates.md "../fleethubuserguide/aws-iot-monitor-technician-job-templates.md").

## Delete a job template

To delete a job template, first go to the [Job templates hub of
the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobtemplatehub "https://console.aws.amazon.com/iot/home#/jobtemplatehub") and choose the **Custom
templates** tab. Then, choose the job template you want to delete
and choose **Next**.

###### Note

A deletion is permanent and the job template no longer appears on the
**Custom templates** tab.

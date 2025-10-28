# Create a job from AWS managed

templates by using the AWS Management Console

Use the AWS Management Console to get information about AWS managed templates and create a
job by using these templates. You can then save the job you create as your own
custom template.

## Get details about managed

templates

You can get information about the different managed templates that are available to
use from the AWS IoT console.

1. To see your available managed templates, go to the [Job
   templates hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobtemplatehub "https://console.aws.amazon.com/iot/home#/jobtemplatehub") and choose the
   **Managed templates** tab.
2. To view details, choose a managed
   template.

The details page contains the following information:

- Name, description, and Amazon Resource Name (ARN) of the managed
  template.
- The environment on which the remote operations can be performed, such
  as Linux.
- The JSON job document that specifies the path to the job handler and
  the commands to run on the device. For example, the following shows an
  example job document for the **AWS-Reboot** template.
  The template shows the path to the job handler and the shell script,
  `reboot.sh`, that the job handler must run to reboot the
  device.

```
{
  "version": "1.0",
  "steps": [
    {
      "action": {
        "name": "Reboot",
        "type": "runHandler",
        "input": {
          "handler": "reboot.sh",
          "path": "${aws:iot:parameter:pathToHandler}"
        },
        "runAsUser": "${aws:iot:parameter:runAsUser}"
      }
    }
  ]
}
```

For more information about the job document and its parameters for
various remote actions, see [Managed template remote actions and
job documents](job-templates-managed.md#job-template-manage-actions "job-templates-managed.md#job-template-manage-actions").

- The latest version of the job document.

## Create a job using managed

templates

You can use the AWS Management console to choose an AWS managed template
to use to create a job. This section shows you how.

You can also start the job creation workflow and then choose the AWS managed
template that you want to use while creating the job. For more information about
this workflow, see [Create and manage jobs by using the
AWS Management Console](manage-job-console.md "manage-job-console.md").

1. ###### Choose your AWS managed template

Go to the [Job
templates hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobtemplatehub "https://console.aws.amazon.com/iot/home#/jobtemplatehub"), choose the
**Managed templates** tab, and then choose your
template. 2. ###### Create a job using your managed template

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
    4. In the **Job document** section, your
     template is displayed with its configuration settings and input
     parameters. Enter values for the input parameters of your chosen
     template. For example, if you chose the
     **AWS-Download-File** template:




    	* For **downloadUrl**, enter the URL of
    	 the file to download, for example:
    	 `https://`example.com/index`.html`.
    	* For **filePath**, enter the path on
    	 the device to store the downloaded file, for example:
    	 ``path/to/file``.
    You can also optionally enter values for the parameters
     `runAsUser` and `pathToHandler`. For
     more information about the input parameters of each template,
     see [Managed template remote actions and
     job documents](job-templates-managed.md#job-template-manage-actions "job-templates-managed.md#job-template-manage-actions").
    5. On the **Job configuration** page, choose the
     job type as
     continuous
     or a snapshot job. A snapshot job is complete when it finishes
     its run on the target devices and groups. A continuous job
     applies to thing groups and runs on any device that you add to a
     specified target group.
    6. Continue to add any additional configurations for your job and
     then review and create your job. For information about the
     additional configurations, see:




    	* [Job rollout, scheduling, and abort
    	 configurations](jobs-configurations-details.md#job-rollout-abort-scheduling "jobs-configurations-details.md#job-rollout-abort-scheduling")
    	* [Job execution timeout and retry
    	 configurations](jobs-configurations-details.md#job-timeout-retry "jobs-configurations-details.md#job-timeout-retry")

## Create custom job

templates from managed templates

You can use an AWS managed template and a custom job as a starting point to
create your own custom job template. To create a custom job template, first
create a job from your AWS managed template as described in the previous
section.

You can then save the custom job as a template to create your own custom job
template. To save as template:

1. Go to the [Job
   hub of the AWS IoT console](https://console.aws.amazon.com/iot/home#/jobhub "https://console.aws.amazon.com/iot/home#/jobhub") and choose the job containing your
   managed template.
2. Choose **Save as a job template** and then create
   your custom job template. For more information about creating a custom
   job template, see [Create a job
   template from an existing job](job-templates-console.md#job-templates-console-create-exist-job "job-templates-console.md#job-templates-console-create-exist-job").

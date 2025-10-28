# Getting started with MediaConvert

MediaConvert takes in an input file and turns it into one or more output files, based on the
instructions and transcoding settings that you provide.

To get started using the MediaConvert console, this tutorial shows how to create a job to
transcode media files. To access MediaConvert programmatically, see the following topics in the API
Reference:

- If you are using one of the AWS SDKs, see [Getting started with the SDKs](../apireference/custom-endpoints.md "../apireference/custom-endpoints.md").
- If you are using the MediaConvert API directly, see [Getting started with the
  API](../apireference/getting-started.md "../apireference/getting-started.md").

###### Note

If you aren't familiar with MediaConvert basics like jobs, queues, presets, and job
templates, read [What is AWS Elemental MediaConvert?](what-is.md "what-is.md").

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Creating a job](#create-a-job "#create-a-job")

## Prerequisites

Follow the steps in the [Prerequisites to start using MediaConvert](setting-up.md "setting-up.md")
chapter so that your input files are accessible and MediaConvert has permissions to run your job.

Start by noting the location of your input files.
This will be a URI like _s3://amzn-s3-demo-bucket/input.mp4_
or a URL like *https://example.amazon.com/input.mp4*.
Then, note the location of your Amazon S3 destination for your output files.
You will use this input and output information when you create your job.

For more information about which input and output formats MediaConvert supports,
see [Supported inputs and outputs](supported-inputs-outputs.md "supported-inputs-outputs.md").

## Creating a job

A job does the work of transcoding one or more media files. When you create a job, you
specify the input files and settings, the output files and settings, and any other
related job settings.

MediaConvert gets the input from the Amazon S3, HTTP, or HTTPS location that you specify. Then MediaConvert
transcodes and writes to the output location that you specify in the job's output group
settings.

###### To create a job

1. Go to the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list "https://console.aws.amazon.com/mediaconvert/home#/jobs/list") page in
   the MediaConvert console.
2. Choose **Create job**.
3. On the **Create job** page, specify your job settings. Include at least
   one input file and at least one output group. For detailed information, see
   [Tutorial: Configuring job settings](setting-up-a-job.md "setting-up-a-job.md").

Note: Make sure that you select the same AWS Region for your job and your file storage. 4. Specify your IAM role that you created as part of the [Setting up IAM permissions](iam-role.md "iam-role.md") process
earlier under **Job settings**, **AWS integration**. 5. Choose **Create**.

For information about tracking the status of your job, see [Using EventBridge with AWS Elemental MediaConvert](eventbridge_events.md "eventbridge_events.md").

For information about the file names and paths for your job outputs, see [Output file names and
paths](output-file-names-and-paths.md "output-file-names-and-paths.md"). 6. Optionally, if you don't want to keep the transcoded files that you generate during this
tutorial, delete them from Amazon S3 to avoid incurring storage charges. For more
information, see [Deleting objects
_Amazon S3 User Guide_](../../../AmazonS3/latest/userguide/DeletingObjects.md "../../../AmazonS3/latest/userguide/DeletingObjects.md").

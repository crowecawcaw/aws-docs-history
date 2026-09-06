

# Getting started with MediaConvert
<a name="getting-started"></a>

MediaConvert takes in an input file and turns it into one or more output files, based on the instructions and transcoding settings that you provide. 

To get started using the MediaConvert console, this tutorial shows how to create a job to transcode media files. To access MediaConvert programmatically, see the following topics in the API Reference:
+ If you are using one of the AWS SDKs, see [Getting started with the SDKs](https://docs.aws.amazon.com/mediaconvert/latest/apireference/custom-endpoints.html).
+ If you are using the MediaConvert API directly, see [Getting started with the API](https://docs.aws.amazon.com/mediaconvert/latest/apireference/getting-started.html).

**Note**  
If you aren't familiar with MediaConvert basics like jobs, queues, presets, and job templates, read [What is AWS Elemental MediaConvert?](what-is.md).

**Topics**
+ [Prerequisites](#getting-started-prerequisites)
+ [Creating a job](#create-a-job)

## Prerequisites
<a name="getting-started-prerequisites"></a>

Follow the steps in the [Prerequisites to start using MediaConvert](setting-up.md) chapter so that your input files are accessible and MediaConvert has permissions to run your job.

Start by noting the location of your input files. This will be a URI like *s3://amzn-s3-demo-bucket/input.mp4* or a URL like *https://example.amazon.com/input.mp4*. Then, note the location of your Amazon S3 destination for your output files. You will use this input and output information when you create your job.

For more information about which input and output formats MediaConvert supports, see [Supported inputs and outputs](supported-inputs-outputs.md). 

## Creating a job
<a name="create-a-job"></a>

A job does the work of transcoding one or more media files. When you create a job, you specify the input files and settings, the output files and settings, and any other related job settings.

MediaConvert gets the input from the Amazon S3, HTTP, or HTTPS location that you specify. Then MediaConvert transcodes and writes to the output location that you specify in the job's output group settings.

**To create a job**

1. Go to the [Jobs](https://console.aws.amazon.com/mediaconvert/home#/jobs/list) page in the MediaConvert console.

1. Choose **Create job**.

1. On the **Create job** page, specify your job settings. Include at least one input file and at least one output group. For detailed information, see [Tutorial: Configuring job settings](setting-up-a-job.md).

   Note: Make sure that you select the same AWS Region for your job and your file storage. 

1. Specify your IAM role that you created as part of the [Setting up IAM permissions](iam-role.md) process earlier under **Job settings**, **AWS integration**.

1. Choose **Create**.

   For information about tracking the status of your job, see [Using EventBridge with AWS Elemental MediaConvert](eventbridge_events.md).

   For information about the file names and paths for your job outputs, see [Output file names and paths](output-file-names-and-paths.md).

1. Optionally, if you don't want to keep the transcoded files that you generate during this tutorial, delete them from Amazon S3 to avoid incurring storage charges. For more information, see [Deleting objects *Amazon S3 User Guide*](https://docs.aws.amazon.com/AmazonS3/latest/userguide/DeletingObjects.html).
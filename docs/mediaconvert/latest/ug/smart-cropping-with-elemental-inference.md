

# Smart Cropping with Elemental Inference
<a name="smart-cropping-with-elemental-inference"></a>

## Introduction
<a name="smart-cropping-introduction"></a>

[AWS Elemental Inference](https://aws.amazon.com/elemental-inference/) is a managed media service that utilizes AI to analyze media content to allow AI-enabled workflows. The Smart Cropping feature uses AI to infer the region of interest in the input video, and crops the video to the specified aspect ratio while keeping the region of interest in the center of the output.

A typical use case for Smart Cropping is to create a vertical video from a landscape video. For example, in a landscape video of a soccer game, Smart Cropping infers a region containing the soccer ball and active players as the region of interest. The video is cropped (verticalized) to keep the ball and the players in the output video frame.

This guide describes enabling the Smart Cropping feature in a MediaConvert job.

## Elemental Inference integration
<a name="smart-cropping-elemental-inference-integration"></a>

When Smart Cropping is enabled in a job, MediaConvert manages the integration with Elemental Inference. While the job is progressing, MediaConvert performs the following:

1. MediaConvert creates an Elemental Inference feed in the account in which the job is run.

1. MediaConvert sends the input to Elemental Inference for analysis.

1. MediaConvert creates a transcoding job utilizing the analysis metadata from Elemental Inference.

1. MediaConvert deletes the feed once the job completes.

Note: MediaConvert adds an AWS tag to the feed with the key `ManagedByService` and the value `AWSElementalMediaConvert`.

## IAM role permissions
<a name="smart-cropping-iam-role-permissions"></a>

The [Setting up IAM permissions](iam-role.md) guide describes setting up an IAM role with the permissions to run a MediaConvert transcoding job. The following policy lists the additional permissions that are required to be added to the transcode IAM role for the Smart Cropping feature:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elemental-inference:CreateFeed",
        "elemental-inference:AssociateFeed",
        "elemental-inference:PutMedia",
        "elemental-inference:GetMetadata",
        "elemental-inference:DeleteFeed",
        "elemental-inference:TagResource"
      ],
      "Resource": "*"
    }
  ]
}
```

## Maximum concurrent feeds
<a name="smart-cropping-maximum-concurrent-feeds"></a>

Each MediaConvert job that has Smart Cropping enabled consumes one Elemental Inference feed while the job is running. MediaConvert allows the user to specify the maximum number of feeds to be used to run MediaConvert jobs through the **Maximum concurrent feeds** settings of a MediaConvert queue, which must be greater than 0 to allow running Smart Cropping jobs. To update the **Maximum concurrent feeds** setting in the MediaConvert console:

1. In the MediaConvert console, select **Queues** and the name of the queue you wish to update.

1. In the queue details page, select **Edit queue**.

1. Update the **Maximum concurrent feeds** field and select **Save queue**.

Note: The maximum concurrent feeds of all queues cannot exceed the Elemental Inference total feeds limit within the account.

If a queue has more Smart Cropping jobs than the maximum concurrent feeds value, the jobs will be queued until feed capacity becomes available (through job completion or updating the maximum feeds of the queue).

## Setting up the Smart Cropping job
<a name="smart-cropping-setting-up-job"></a>

The following are steps to enable Smart Cropping in a MediaConvert output:

1. In the MediaConvert console, add an output group and an output.

1. In the output video description settings, set the desired width and height, where the width must be less than or equal to the height.

1. In the video description settings, expand **Scaling** and set the **Scaling behavior** to **Smart Cropping using Elemental Inference**.

For details about setting up a MediaConvert job, see [Tutorial: Configuring job settings](setting-up-a-job.md).

Smart Cropping is not supported with the following features:
+ [Accelerated transcoding](accelerated-transcoding.md)
+ [HTTP inputs](http-input-requirements.md)
+ [Reserved queues](working-with-reserved-queues.md)

## Pricing
<a name="smart-cropping-pricing"></a>

The pricing of a Smart Cropping job is divided into 2 parts: the pricing for Elemental Inference and the pricing for the transcode. The charges for the services only apply when the job completes successfully. There are no charges when a job errors.

Smart Cropping is a Professional Tier feature and enabled per output.

## Region availability
<a name="smart-cropping-region-availability"></a>

Smart Cropping enabled jobs are available where Elemental Inference is available in the following regions:
+ US East (North Virginia) us-east-1
+ US West (Oregon) us-west-2
+ Europe (Ireland) eu-west-1
+ Asia Pacific (Mumbai) ap-south-1
+ Asia Pacific (Sydney) ap-southeast-2
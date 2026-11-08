

# AWS Elemental MediaConvert features that use AWS Elemental Inference
<a name="elemental-inference"></a>

 AWS Elemental Inference is a managed media service that uses AI to generate metadata from media files. For more information, see [Elemental Inference](https://aws.amazon.com/elemental-inference/) on the AWS website. 

 This guide shows you how MediaConvert integrates with Elemental Inference to enable Smart features. For more information about enabling a specific Smart feature, see the corresponding feature guide. 

**Topics**
+ [How MediaConvert integrates with Elemental Inference](#elemental-inference-integration)
+ [Configuring IAM role permissions for Smart features](#elemental-inference-iam-role-permissions)
+ [Set the maximum concurrent feeds](#elemental-inference-maximum-concurrent-feeds)
+ [Pricing](#elemental-inference-pricing)
+ [Feature compatibility](#elemental-inference-unsupported-features)
+ [Region availability](#elemental-inference-region-availability)
+ [Smart cropping](smart-cropping-with-elemental-inference.md)
+ [Smart subtitling](smart-subtitling-with-elemental-inference.md)

## How MediaConvert integrates with Elemental Inference
<a name="elemental-inference-integration"></a>

 When you enable a Smart feature in a job, MediaConvert manages multiple interactions with Elemental Inference. While the job is progressing, MediaConvert performs the following actions: 

1. MediaConvert creates an Elemental Inference feed in the account and region from which the job is run.

1. MediaConvert sends the relevant input files to the Elemental Inference feed for inferencing.

1. MediaConvert creates a transcoding job using the metadata returned from the Elemental Inference feed.

1. MediaConvert deletes the Elemental Inference feed after the job transitions to a terminal state.

 To configure optional Elemental Inference feed feature parameters, such as a subtitling profanity filter, you can create and configure a source feed and then specify the ARN in the **AWS Elemental Inference feed configuration source ARN** field. MediaConvert then copies the supported feature parameters from the source feed to the MediaConvert-managed feed created while the job is progressing. You must create the source feed in the same account and region as your MediaConvert job. You must also enable the corresponding Smart features in your job. 

 To configure the **AWS Elemental Inference feed configuration source ARN** value in the MediaConvert console, perform the following steps: 

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. In the navigation pane, choose **Jobs**.

1. Choose **Create job**.

1. Choose **AWS integration**.

1.  For **AWS Elemental Inference feed configuration source ARN**, enter the ARN of your source feed you want MediaConvert to copy the configuration from. 

 Note: We add an AWS tag to the Elemental Inference feed with the key `ManagedByService` and the value `AWSElementalMediaConvert`. 

## Configuring IAM role permissions for Smart features
<a name="elemental-inference-iam-role-permissions"></a>

 The following IAM policy outlines the additional permissions required to use Smart features. For more information about creating a MediaConvert IAM role, see the [Setting up IAM permissions](iam-role.md) guide. 

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

 If you provide an Elemental Inference feed configuration source ARN in your MediaConvert job settings, then you must also include the `elemental-inference:GetFeed` action in your IAM policy. 

## Set the maximum concurrent feeds
<a name="elemental-inference-maximum-concurrent-feeds"></a>

 Each MediaConvert job configured with one or more Smart features creates one Elemental Inference feed while the job is progressing. You can configure the maximum number of concurrent feeds MediaConvert can create via the **Maximum concurrent feeds** setting of a MediaConvert queue. Set this value greater than zero to allow MediaConvert to process jobs that use Smart features. 

 If the number of jobs using Smart features exceeds the **Maximum concurrent feeds** value, then MediaConvert enqueues the extra jobs. MediaConvert processes them when feed capacity becomes available. 

To configure the **Maximum concurrent feeds** value in the MediaConvert console, perform the following steps:

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert](https://console.aws.amazon.com/mediaconvert).

1. In the navigation pane, choose **Queues** and then select the on-demand queue you want to update.

1. On the queue details page, choose **Edit queue**.

1. Update the **Maximum concurrent feeds** field.

1. Choose **Save queue**.

 Note: the total number of concurrent feeds configured across all queues cannot exceed the Elemental Inference **Active feeds per account** quota. To increase this quota, please contact AWS Support. 

## Pricing
<a name="elemental-inference-pricing"></a>

 When using Smart features, you are charged for the Elemental Inference inferencing and the MediaConvert transcoding. Each AWS service charges you only when the job completes successfully. Neither AWS service charges you for errored or canceled jobs. 

All Smart features are in the Professional Tier and are enabled per output.

For more information, see the Pricing pages for AWS Elemental MediaConvert and AWS Elemental Inference.

## Feature compatibility
<a name="elemental-inference-unsupported-features"></a>

Smart features work with most features except the following:
+ [Accelerated transcoding](accelerated-transcoding.md)
+ [HTTP inputs](http-input-requirements.md)
+ [Reserved queues](working-with-reserved-queues.md)

## Region availability
<a name="elemental-inference-region-availability"></a>

Smart features are available in the following regions:
+ US East (North Virginia)
+ US West (Oregon)
+ Europe (Ireland)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Sydney)
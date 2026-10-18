

# Use enhanced AMI distribution capabilities
<a name="distribution-enhanced_functionality"></a>

Image Builder gives you advanced distribution capabilities that separate distribution from the build process. You can distribute an image that you already built, retry an AMI image that failed during its test or distribution phase without rebuilding it, and define multi-stage distribution processes with custom workflows.

## Distribute an existing image
<a name="decoupled-distribution"></a>

The **DistributeImage** operation distributes an image that Image Builder (or you) already created, without rerunning the build and test phases. Image Builder runs only the distribution phase, using the targets and settings in a distribution configuration that you reference by ARN.

You identify the source image in one of three ways:
+ **AMI ID** – A standard AMI identifier, such as `ami-0abcdef1234567890`. The AMI must exist and be accessible in the Region where you call the operation.
+ **SSM parameter** – An Systems Manager Parameter Store reference in the form `ssm:{{/path/to/parameter}}`, where the text after `ssm:` is the parameter name or ARN. The parameter must be a `String` parameter whose value is a valid AMI ID.
+ **Image Builder image version ARN** – The ARN of an Image Builder image in the Region where you call the operation. The image's output resources must include an AMI in that Region. You can specify a build version ARN that ends with the build number, such as `image/{{my-image}}/1.0.0/1`, or a version ARN without the build number, such as `image/{{my-image}}/1.0.0`. Image Builder resolves a version ARN to its latest build in the `AVAILABLE` state.

**Note**  
The source image must be an AMI ID, an SSM parameter, or an Image Builder image ARN, and Image Builder doesn't accept an AWS Marketplace product code. The distribution configuration must be in the same Region where you call **DistributeImage**. You can't pass inline distribution settings to this operation.

**Prerequisites**  
Unlike a pipeline build, **DistributeImage** takes an execution role at call time. Make sure the following are in place:
+ An Image Builder execution role that Image Builder can assume to perform the distribution. We recommend that you create a custom role with the [EC2ImageBuilderExecutionPolicy](security-iam-awsmanpol.md#sec-iam-manpol-EC2ImageBuilderExecutionPolicy) AWS managed policy attached. That policy allows `ec2:ModifyImageAttribute`, `ec2:ModifySnapshotAttribute`, and `ec2:EnableFastLaunch` only on resources that are tagged `CreatedBy: EC2 Image Builder`, and allows `ssm:PutParameter` only on parameters under `/imagebuilder/`. If your distribution acts on other resources, add the required permissions to the role. To configure EC2 Fast Launch without a launch template, also attach the EC2FastLaunchFullAccess policy. To configure EC2 Fast Launch with a launch template, the launch template must have the `CreatedBy: EC2 Image Builder` tag. Image Builder adds this tag only to launch templates that the distribution configuration updates in `launchTemplateConfigurations`. For any other launch template, add the tag yourself or attach the EC2FastLaunchFullAccess policy.
+ Permission to call `imagebuilder:DistributeImage`, `imagebuilder:GetDistributionConfiguration`, and `iam:PassRole` for the execution role. Image Builder also describes the source AMI with your credentials to validate it, so you need `ec2:DescribeImages` for every source type. If the source is an SSM parameter, you also need `ssm:GetParameter` for that parameter. If the source is an Image Builder image ARN, you also need `imagebuilder:GetImage` on that image. If you include tags in the request, you also need `imagebuilder:TagResource`.
+ If the distribution configuration copies the AMI to other accounts (`targetAccountIds`), or updates launch templates or SSM parameters in other accounts, the `EC2ImageBuilderDistributionCrossAccountRole` in each of those accounts, with the [Ec2ImageBuilderCrossAccountDistributionAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess) managed policy attached. The managed policy doesn't cover launch templates or SSM parameters. To update them, also add the policies that [Set up cross-account AMI distribution with Image Builder](cross-account-dist.md) lists for `launchTemplateConfigurations` and Parameter Store parameters.

------
#### [ AWS Management Console ]

To distribute an existing image in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Distribution settings** from the navigation pane.

1. Select the distribution configuration that defines your targets, then choose **Distribute image** from the **Actions** menu. You can select only one distribution configuration at a time for this action.

1. In the **Image to distribute** section, choose the source image type – **AMI ID**, **SSM parameter**, or **Image Builder image ARN** – and specify the image to distribute.

1. Choose the IAM role that Image Builder uses to perform the distribution.

1. Choose **Distribute image**.

------
#### [ AWS CLI ]

The following examples show how to distribute an existing image with the [distribute-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/distribute-image.html) command. You can specify the `--execution-role` by role name or by full ARN; the following examples show both forms.

**Distribute from an AMI ID**  


```
aws imagebuilder distribute-image \
    --source-image ami-0abcdef1234567890 \
    --distribution-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-distribution}} \
    --execution-role arn:aws:iam::{{123456789012}}:role/{{MyImageBuilderDistributionRole}}
```

**Distribute from an SSM parameter**  


```
aws imagebuilder distribute-image \
    --source-image ssm:{{/golden/latest-ami}} \
    --distribution-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-distribution}} \
    --execution-role {{MyImageBuilderDistributionRole}}
```

**Distribute from an Image Builder image version ARN**  
This example uses a build version ARN. You can also omit the trailing build number (`/1`) to distribute the latest build of that image version.

```
aws imagebuilder distribute-image \
    --source-image arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-image}}/1.0.0/1 \
    --distribution-configuration-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:distribution-configuration/{{my-distribution}} \
    --execution-role {{MyImageBuilderDistributionRole}}
```

The command returns the `imageBuildVersionArn` for the distribution. Track its progress the same way you track a build – see [List images and build versions](image-details-list.md).

------

## Retry a failed image
<a name="distribution-retry"></a>

If an image fails during its test or distribution phase, use the [retry-image](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/imagebuilder/retry-image.html) command (the **RetryImage** API) to rerun the image from the start of the phase that failed. Steps in that phase run again. If an AMI copy from the earlier attempt is still available in a target Region and account, Image Builder reuses it instead of copying the AMI again. Image Builder reuses the original execution role, distribution configuration, and settings, so you don't rebuild the image. The retry assumes the same execution role, so any permission fixes that you make to that role apply to the retry.

**Prerequisites**  
Before you retry a failed image, verify the following. A retry counts against your concurrent image build quota, and Image Builder rejects the retry if you've already reached that quota.
+ The image is in a `FAILED` or `CANCELLED` state, and it failed or was canceled during its test or distribution phase. You can't retry an image that succeeded or is still in progress, or an image that failed or was canceled in any other phase.
+ The image was created within the last 30 days.
+ The image is an AMI-based image. You can't retry a container image.
+ The image hasn't already been retried the maximum number of times. Image Builder allows up to 10 retries per image.
+ You have identified and resolved the root cause of the failure. Review the image's logs in CloudWatch Logs for error details.
+ You have permission to call `imagebuilder:RetryImage` on the image build version that you want to retry.
+ For cross-account distribution failures, verify that the `EC2ImageBuilderDistributionCrossAccountRole` in the destination account has the [Ec2ImageBuilderCrossAccountDistributionAccess policy](security-iam-awsmanpol.md#sec-iam-manpol-Ec2ImageBuilderCrossAccountDistributionAccess) managed policy attached. For more information, see [Set up cross-account AMI distribution with Image Builder](cross-account-dist.md).

------
#### [ AWS Management Console ]

To retry a failed image in the Image Builder console, follow these steps:

1. Open the EC2 Image Builder console at [https://console.aws.amazon.com/imagebuilder/](https://console.aws.amazon.com/imagebuilder/).

1. Choose **Images** from the navigation pane, and then choose the image build version that failed.

1. Choose **Retry image**. This action is available only when the image is in a failed or canceled state.

------
#### [ AWS CLI ]

Provide the image build version ARN of the failed image:

```
aws imagebuilder retry-image \
    --image-build-version-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{my-image}}/1.0.0/1
```

------

## Distribution workflows
<a name="distribution-workflows"></a>

Distribution workflows are a workflow type that complements build and test workflows. A distribution workflow defines the distribution phase as a sequence of steps, which gives you step-level visibility and control over how Image Builder distributes an AMI. The steps that this section describes apply to AMI output images.

In a distribution workflow, you can include steps that do the following:
+ Copy and share the AMI across Regions and accounts.
+ Modify image attributes, such as launch permissions, on the distributed AMIs.
+ Apply additional image configurations.
+ Pause for a manual approval or an external callback with a *wait-for-action* step. This lets you build staged or gated rollouts – for example, distribute to a test Region, wait for approval, then continue to production Regions.

Each step reports its own status – `PENDING`, `RUNNING`, `WAITING` (wait-for-action steps only), `COMPLETED`, `FAILED`, `SKIPPED`, or `CANCELLED` – and Image Builder sends step-level details to your CloudWatch log group. A step that runs longer than its `timeoutSeconds` value reports `FAILED`. Image Builder also emits EventBridge events at key points – for example, when the image changes state, and when a wait-for-action step pauses for input. For the full list of events, see [Event messages that Image Builder sends](integ-eventbridge.md#integ-eb-event-summary).

To learn how to create and customize workflows, including the YAML document format and the available step actions, see [Manage build, test, and distribution workflows for Image Builder images](manage-image-workflows.md).
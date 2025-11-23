# Use enhanced AMI distribution capabilities

Image Builder offers advanced distribution capabilities that give you flexibility and control over
how your AMIs are distributed across regions and accounts. These capabilities separate distribution from the
build process, allowing you to distribute existing images on demand, recover from distribution failures efficiently,
and implement controlled, multi-stage distribution strategies through customizable workflows.

You can use enhanced AMI distribution capabilities in Image Builder to directly perform distribution
activities without the need to re-run a complete image build.

## Decoupled Distribution

The DistributeImage API accepts three types of source image references:

- **AMI ID**
  – A standard AMI identifier (for example, `ami-0abcdef1234567890`)
- **SSM Parameter**
  – An SSM parameter that stores an AMI ID (for example, `ssm:/my/ami/parameter`)
- **Image Builder version ARN**
  – An Image Builder image version ARN

## Distribution Retry

If an image distribution fails, use the `RetryImage` API to retry distribution. This reduces time to troubleshoot the cause of the failure by avoiding a complete image rebuild.
Use `RetryImage` after resolving the underlying cause of the distribution failure.

The RetryImage API accepts an image build version ARN (for example, `arn:aws:imagebuilder:us-west-2:123456789012:image/my-image/1.0.0/1`).
When you invoke the API, Image Builder automatically resumes the distribution process from the point of failure using the original distribution configuration and settings.
The `RetryImage` API can retry distributions that failed during the distribution phase, test phase, or integration phase. It works with AMIs in the following states: pending, failed, deleted, or available.

**Prerequisites**

Before retrying a distribution, ensure the following:

- You have identified and resolved the root cause of the failure. Review distribution logs in CloudWatch Logs for error details.
- You have the necessary IAM permissions to retry the image build.
- For cross-account distribution failures, verify that the `EC2ImageBuilderDistributionCrossAccountRole` in the destination account
  has the `Ec2ImageBuilderCrossAccountDistributionAccess` policy attached.

**Important:** Retrying without fixing the underlying issue will result in repeated failures.

## Distribution Workflows

Distribution workflows are a new workflow type that complement build and test workflows, enabling you to define
and control the distribution process with sequential steps. With distribution workflows, you can create custom distribution
processes that include AMI copy operations, wait-for-action checkpoints, image attribute modifications, and other
distribution-related steps. This provides structured control over how your AMIs are distributed, with step-level visibility,
parallel distribution capabilities, and granular error reporting.

To learn more about creating and customizing workflows, see [Manage Image Workflows](manage-image-workflows.md "manage-image-workflows.md").

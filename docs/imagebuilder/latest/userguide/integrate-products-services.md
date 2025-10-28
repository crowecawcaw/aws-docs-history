# Integrate products and services in Image Builder

EC2 Image Builder integrates with AWS Marketplace and other AWS services and applications to help you
create robust, secure custom machine images.

**Products**

Image Builder recipes can incorporate image products from AWS Marketplace and Image Builder managed components to
provide specialized build and test functionality, as follows.

- **AWS Marketplace image products** –
  Use an image product from AWS Marketplace as the base image in your
  recipe to meet organizational standards, such as CIS Hardening.
  When you create a recipe from the Image Builder console, you can choose from your existing
  subscriptions, or
  search for a specific product from AWS Marketplace. When you create a recipe from the Image Builder API,
  CLI, or SDK, you can specify an image product Amazon Resource Name (ARN) to use as your
  base image.
- **Image Builder components** – Components that you specify in
  your recipes can perform build and test actions, for example, to install software or
  perform compliance validation. Some image products that you subscribe to from AWS Marketplace
  might include a companion component that you can use in your recipes. The CIS Hardened images include a matching AWSTOE component
  that you can use in your recipe to enforce CIS Benchmarks Level 1 guidelines for your
  configuration.

###### Note

For more information about compliance-related products, see [Compliance products for your Image Builder images](integ-compliance-products.md "integ-compliance-products.md").

**Services**

Image Builder integrates with the following AWS services to provide detailed event metrics,
logging, and monitoring. This information helps you track your activity, troubleshoot image
build issues, and create automations based on event notifications.

- **AWS Organizations** – AWS Organizations allows you to apply
  Service Control Policies (SCP) on accounts in your
  organization. You can create, manage, enable, and disable individual policies.
  Similar to all other AWS artifacts and services, Image Builder honors the policies defined
  in AWS Organizations. AWS provides template SCPs for common scenarios, such as enforcing
  constraints on member accounts to launch instances with only approved AMIs.
- **AWS CloudTrail** – Monitor Image Builder events that are
  sent to CloudTrail. For more information about CloudTrail integration with Image Builder, see
  [Log Image Builder API calls using CloudTrail](log-cloudtrail.md "log-cloudtrail.md").

To learn more about CloudTrail, including how to turn it on and find your log files, see the
[AWS CloudTrail User Guide](../../../awscloudtrail/latest/userguide.md "../../../awscloudtrail/latest/userguide.md").

- **Amazon CloudWatch Logs** – Monitor, store, and access
  your Image Builder log files with CloudWatch. Optionally, you can save your logs to an S3 bucket. To
  learn more about CloudWatch integration with Image Builder, see [Monitor Image Builder logs with Amazon CloudWatch Logs](monitor-cwlogs.md "monitor-cwlogs.md").

For more information about CloudWatch Logs, see [What is Amazon CloudWatch Logs?](../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.md")
in the _Amazon CloudWatch Logs User Guide_.

- **Amazon Elastic Container Registry (Amazon ECR)** – Amazon ECR is a managed AWS
  container image registry service that is secure, scalable, and reliable. Container
  images that you create with Image Builder are stored in Amazon ECR in your source Region (where
  your build runs), and in any Regions where you distribute the container image. For
  more information about Amazon ECR, see the [Amazon Elastic Container Registry User Guide](../../../AmazonECR/latest/userguide.md "../../../AmazonECR/latest/userguide.md").
- **Amazon EventBridge** – Connect to a stream of
  real-time event data from Image Builder activities in your account. For more information
  about EventBridge, see [What Is Amazon EventBridge?](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md")
  in the _Amazon EventBridge User Guide_.
- **Amazon Inspector** – Discover vulnerabilities in your
  software and network settings with automatic scans for the EC2 test instance that Image Builder
  launches create a new image. Image Builder saves findings for your output image resource
  so that you can investigate and remediate after your test instance terminates.
  For more information about scans and pricing, see [What is Amazon Inspector?](../../../inspector/v1/userguide/inspector_introduction.md "../../../inspector/v1/userguide/inspector_introduction.md")
  in the _Amazon Inspector User Guide_.

Amazon Inspector can also scan your ECR repositories if you configure enhanced scanning. For more
information, see [Scanning
Amazon ECR container images](../../../inspector/latest/user/scanning-ecr.md "../../../inspector/latest/user/scanning-ecr.md") in the _Amazon Inspector User Guide_.

###### Note

Amazon Inspector is a paid feature.

- **AWS License Manager** – You can attach a
  License Manager self-managed license to an output AMI during the distribution process. The
  license that you specify for the destination Region must already exist in that
  Region. For more information about self-managed licenses, see [Self-managed
  licenses in License Manager](../../../license-manager/latest/userguide/license-configurations.md "../../../license-manager/latest/userguide/license-configurations.md").
- **AWS Marketplace** – See a list of your current AWS Marketplace
  product subscriptions, and search for image products directly from Image Builder. You can also
  use an image product that you’ve subscribed to as the base image for an Image Builder recipe.
  For more information about managing AWS Marketplace subscriptions, see [Buying products](../../../marketplace/latest/buyerguide/buyer-subscribing-to-products.md "../../../marketplace/latest/buyerguide/buyer-subscribing-to-products.md")
  in the _AWS Marketplace Buyer Guide_.
- **AWS Resource Access Manager (AWS RAM)** – With AWS RAM, you can
  share resources with any AWS account or through AWS Organizations. If you have multiple
  AWS accounts, you can create resources centrally and use AWS RAM to share those
  resources with other accounts. EC2 Image Builder allows sharing for the following resources:
  components, images, and image recipes. For more information about AWS RAM, see the [AWS Resource Access Manager User
  Guide](../../../ram/latest/userguide/what-is.md "../../../ram/latest/userguide/what-is.md"). For information about sharing Image Builder resources, see
  [Share Image Builder resources with AWS RAM](manage-shared-resources.md "manage-shared-resources.md").
- **Amazon Simple Notification Service (Amazon SNS)** – If configured, publish
  detailed messages about your image status to an SNS topic that you subscribe to. For
  more information about Amazon SNS, see [What is
  Amazon SNS?](../../../sns/latest/dg/welcome.md "../../../sns/latest/dg/welcome.md") in the _Amazon Simple Notification Service Developer Guide_.

###### Product and service integration topics

- [Amazon EventBridge integration in Image Builder](integ-eventbridge.md "integ-eventbridge.md")
- [Amazon Inspector integration in Image Builder](integ-inspector.md "integ-inspector.md")
- [AWS Marketplace integration in Image Builder](integ-marketplace.md "integ-marketplace.md")
- [Amazon SNS integration in Image Builder](integ-sns.md "integ-sns.md")
- [Compliance products for your Image Builder images](integ-compliance-products.md "integ-compliance-products.md")

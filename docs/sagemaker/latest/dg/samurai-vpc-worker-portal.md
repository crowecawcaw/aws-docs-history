# Use Amazon VPC Mode from a Private Worker Portal

To restrict worker portal access to labelers working inside of your Amazon VPC,
you can add a VPC configuration when you create a Ground Truth private workforce.
You can also add a VPC configuration to an existing private workforce. Ground Truth
automatically creates VPC interface endpoints in your VPC and sets up AWS PrivateLink
between your VPC endpoint and the Ground Truth services. The worker portal URL
associated with the workforce can be accessed from your VPC. The worker portal URL
can also be accessed from public internet until you set the restriction on the public internet.
When you delete the workforce or remove the VPC configuration from your workforce,
Ground Truth automatically deletes the VPC endpoints associated with the workforce.

###### Note

There can be only one VPC supported for a workforce.

[Point Cloud](sms-point-cloud.md "sms-point-cloud.md") and [video](sms-video.md "sms-video.md") tasks do not support loading through a VPC.

The guide demonstrates how to complete the necessary steps
to add and delete an Amazon VPC configuration to your workforce, and satisfy the prerequisites.

## Prerequisites

To run a Ground Truth labeling job in Amazon VPC, review the following prerequisites.

- You have an Amazon VPC configured that you can use. If you have not configured a VPC, follow these instructions for [creating a VPC](../../../vpc/latest/privatelink/create-interface-endpoint.md#interface-endpoint-shared-subnets "../../../vpc/latest/privatelink/create-interface-endpoint.md#interface-endpoint-shared-subnets").
- Depending on how a [Worker Task Template](a2i-instructions-overview.md "a2i-instructions-overview.md") is written, labeling data
  stored in an Amazon S3 bucket may be accessed directly from Amazon S3 during labeling tasks. In these cases, the VPC network
  must be configured to allow traffic from the device used by the human labeler to the S3 bucket containing labeling data.
- Follow [View and update DNS attributes for your VPC](../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating "../../../vpc/latest/userguide/vpc-dns.md#vpc-dns-updating") to enable DNS hostnames and DNS resolution for your VPC.

###### Note

There are two ways to configure your VPC for your workforce. You can do this through the [console](https://console.aws.amazon.com/sagemaker "https://console.aws.amazon.com/sagemaker") or
the AWS SageMaker AI [CLI](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").

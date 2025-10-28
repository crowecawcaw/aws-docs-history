# Launching a DLAMI instance

After you [find the ID](find-dlami-id.md "find-dlami-id.md") of the DLAMI that you want to use
to launch a DLAMI instance, you're ready to launch the instance. To launch it, you can
use either the Amazon EC2 console or the AWS Command Line Interface (AWS CLI).

###### Note

For this walkthrough, we might make references specific to the
Deep Learning Base OSS Nvidia Driver GPU AMI (Ubuntu 22.04). Even if you select a different DLAMI, you should be able
to follow this guide.

EC2 console

###### Note

To accelerate high-performance computing (HPC) and machine learning applications, you can launch your DLAMI instance with an Elastic Fabric Adapter (EFA). For specific instructions, see [Launching a AWS Deep Learning AMIs Instance With EFA](tutorial-efa-launching.md "tutorial-efa-launching.md").

1. Open the [EC2 Console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2").
2. Note your current AWS Region in the top-most navigation. If this isn't your desired
   Region, then change this option before you continue. For more
   information, see [Amazon EC2 service endpoints](../../../general/latest/gr/ec2-service.md#ec2_region "../../../general/latest/gr/ec2-service.md#ec2_region") in the _Amazon Web Services General Reference_.
3. Choose **Launch Instance**.
4. Enter a name for your instance and select the DLAMI that is right for you.
   1. Find an existing DLAMI in **My AMIs** or choose **Quick Start.**
   2. Search by DLAMI ID. Browse the options then select your choice.

5. Choose an instance type. You can find the recommended instance families for your DLAMI in [Deep Learning AMIs Release Notes](appendix-ami-release-notes.md "appendix-ami-release-notes.md"). For general recommendations on DLAMI instance types, see
   [Choosing a DLAMI instance type](instance-select.md "instance-select.md").
6. Choose **Launch Instance**.

AWS CLI

- To use the AWS CLI, you must have the ID of the DLAMI that you want to use, the
  AWS Region and EC2 instance type, and your security token
  information. Then, you can launch the instance using the [**ec2 run-instances**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/run-instances.html") AWS CLI command.

For instructions on installing and configuring the AWS CLI, see [Get started
with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
_AWS Command Line Interface User Guide_. For more information,
including command examples, see [Launch, list, and close Amazon EC2 instances for the
AWS CLI](../../../cli/latest/userguide/cli-services-ec2-instances.md "../../../cli/latest/userguide/cli-services-ec2-instances.md").

After you launch your instance using either the Amazon EC2 console or AWS CLI, wait for the instance
to be ready. This usually takes only a few minutes. You can verify the status of the
instance in the [Amazon EC2 console](https://console.aws.amazon.com/ec2 "https://console.aws.amazon.com/ec2"). For more information, see [Status checks for Amazon EC2 instances](../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md "../../../AWSEC2/latest/UserGuide/monitoring-system-instance-status-check.md") in the _Amazon EC2 User Guide_.

###### Next step

[Connecting to a DLAMI instance](setup-connect.md "setup-connect.md")

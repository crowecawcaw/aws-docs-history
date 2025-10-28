# `AWSEC2-PatchLoadBalancerInstance`

**Description**

Upgrade and patch minor version of an Amazon EC2 instance (Windows or Linux) attached to any
load balancer (classic, ALB, or NLB). The default connection draining time is applied before
the instance is patched. You can override the wait time by entering your custom draining
time in minutes (`1`-`59`) for the **ConnectionDrainTime** parameter.

The automation workflow is as follows:

1. The load balancer or target group to which the instance is attached is determined,
   and the instance is verified as healthy.
2. The instance is removed from the load balancer or target group.
3. The automation waits for the period of time specified for the connection draining time.
4. The [AWS-RunPatchBaseline](../../../systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.md "../../../systems-manager/latest/userguide/patch-manager-about-aws-runpatchbaseline.md") automation is
   called to patch the instance.
5. The instance is reattached to the load balancer or target group.
   [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSEC2-PatchLoadBalancerInstance "https://console.aws.amazon.com/systems-manager/automation/execute/AWSEC2-PatchLoadBalancerInstance")

**Document Type**

Automation

**Owner**

Amazon

**Prerequisites**

- Verify that SSM Agent is installed on your instance. For more information, see
  [Working with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/sysman-install-ssm-win.md "../../../systems-manager/latest/userguide/sysman-install-ssm-win.md").

**Parameters**

- **InstanceId**

Type: String

Description: (Required) ID of the instance to patch that is associated with a load
balancer (classic, ALB, or NLB).

- **ConnectionDrainTime**

Type: String

Description: (Optional) The connection draining time of the load balancer, in
minutes (`1`-`59`).

- **S3BucketLog**

Type: String

Description: (Optional) The name of the Amazon S3 bucket to use to store the command output
responses. You can specify a bucket that you own or a bucket that is shared with you.
If you provide this parameter, you must also provide **runCommandAssumeRole**.

- **runCommandAssumeRole**

Type: String

Description: (Optional) The ARN of the IAM role to use to run the command on the
instance. The role must have a trust relationship with the `ssm.amazonaws.com`
service principal, it must have the **AmazonSSMManagedInstanceCore**
policy attached, and it must have write permissions for the Amazon S3 bucket specified for
**S3BucketLog**.

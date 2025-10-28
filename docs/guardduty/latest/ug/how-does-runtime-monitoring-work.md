# How it works

To use Runtime Monitoring, you must enable Runtime Monitoring and then manage the GuardDuty security agent. The
following list explains this two-step process:

1.  **Enable Runtime Monitoring** for your account so that GuardDuty can accept
    the runtime events that it receives from your Amazon EC2 instances, Amazon ECS clusters, and Amazon EKS
    workloads.
2.  **Manage GuardDuty agent** for the individual resources for which you
    want to monitor the runtime behavior. Based on the resource type, you can choose to:

        * Use automated agent configuration, where GuardDuty manages the agent deployment and automatically an Amazon Virtual Private Cloud (Amazon VPC)
         endpoint.
        * Install agent manually, which requires you to create the VPC endpoint as a prerequisite.

    The security agent uses VPC endpoint to deliver events to GuardDuty, ensuring that the data remains
    within the AWS network. This approach enhances security and allows GuardDuty to monitor and analyze runtime behavior
    across your resources (Amazon EKS, Amazon EC2, and AWS Fargate-Amazon ECS). GuardDuty uses [Instance identity roles](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-identity-roles "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-identity-roles") that authenticates the security agent for each resource type
    to send the associated runtime events to the VPC endpoint.

###### Note

GuardDuty doesn't make the runtime events accessible to you.

When you manage the security agent (either manually or through GuardDuty) in EKS Runtime Monitoring
or Runtime Monitoring for EC2 instances, and
GuardDuty is presently deployed on an Amazon EC2 instance and receives
the [Collected runtime event
types](runtime-monitoring-collected-events.md "runtime-monitoring-collected-events.md") from this instance, GuardDuty will not charge
your AWS account for the analysis of VPC flow logs from this Amazon EC2 instance. This helps GuardDuty avoid double usage cost in the account.

The following topics explain how enabling Runtime Monitoring and managing GuardDuty security agent works
differently for each resource type.

###### Contents

- [How Runtime Monitoring works with Amazon EKS
  clusters](how-runtime-monitoring-works-eks.md "how-runtime-monitoring-works-eks.md")
- [How Runtime Monitoring works with Amazon EC2
  instances](how-runtime-monitoring-works-ec2.md "how-runtime-monitoring-works-ec2.md")
- [How Runtime Monitoring works with Fargate
  (Amazon ECS only)](how-runtime-monitoring-works-ecs-fargate.md "how-runtime-monitoring-works-ecs-fargate.md")
- [After you enable Runtime Monitoring](runtime-monitoring-after-configuration.md "runtime-monitoring-after-configuration.md")

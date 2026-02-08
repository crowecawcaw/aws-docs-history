# MSFTPERF02-BP02 Consider the use for EC2 Fast Launch to

accelerate launching your Microsoft workload instances

EC2 Fast Launch will speed up the Windows EC2 instance launch
process. When you configure a Windows Server AMI for EC2 Fast
Launch, Amazon EC2 creates a set of pre-provisioned snapshots to use
for faster launching. It completes steps such as Sysprep specialize,
Windows Out of Box Experience (OOBE), and rebooting as required.
Especially useful when you need to scale fast.

**Desired outcome:** Significantly
reduce Windows instance launch times and improve scaling
responsiveness for Microsoft workloads by leveraging EC2 Fast Launch
to pre-provision snapshots and complete initialization steps,
enabling rapid deployment and auto-scaling capabilities for
time-sensitive applications.

**Common anti-patterns:**

- Accepting standard Windows instance launch times without
  evaluating Fast Launch benefits, missing opportunities to
  improve application availability and user experience during
  scaling events.
- Implementing Fast Launch without considering the additional
  costs of pre-provisioned snapshots and temporary instances,
  potentially increasing expenses without adequate benefit
  analysis.
- Using Fast Launch for infrequently launched instances where the
  preparation overhead exceeds the benefits, leading to
  unnecessary complexity and costs.

**Benefits of establishing this best
practice:**

- Dramatically reduced instance launch times through
  pre-provisioned snapshots that eliminate Windows initialization
  steps like Sysprep and OOBE during actual instance launches.
- Improved application availability and scaling responsiveness
  during traffic spikes or auto-scaling events, enhancing user
  experience and system reliability.
- Enhanced disaster recovery capabilities through faster instance
  replacement and environment restoration when rapid recovery is
  critical for business continuity.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Implementing EC2 Fast Launch requires careful evaluation of your
scaling patterns and cost-benefit analysis. Focus on AMIs that are
frequently launched and where launch time significantly impacts
application performance or user experience.

### Implementation steps

1. Identify Windows AMIs that are frequently launched or
   require rapid scaling capabilities for your Microsoft
   workloads.
2. Analyze current instance launch times and scaling patterns
   to determine potential benefits of Fast Launch
   implementation.
3. Configure Fast Launch for selected AMIs through the EC2
   console or AWS CLI, specifying the number of pre-provisioned
   snapshots to maintain.
4. Monitor Fast Launch metrics including launch time
   improvements and associated costs for pre-provisioned
   resources.
5. Evaluate cost-benefit ratio considering snapshot storage
   costs, temporary instance costs, and performance
   improvements.
6. Integrate Fast Launch-enabled AMIs into auto-scaling groups
   and deployment processes to maximize scaling responsiveness.
7. Establish monitoring and alerting for Fast Launch resource
   utilization to optimize the number of pre-provisioned
   snapshots.
8. Document Fast Launch configuration and regularly review
   effectiveness based on actual scaling patterns and
   requirements.

## Resources

**Related documents:**

- [Configuring
  your Windows AMI for faster launching](../../../AWSEC2/latest/UserGuide/win-ami-config-fast-launch.md "../../../AWSEC2/latest/UserGuide/win-ami-config-fast-launch.md")
- [Launch
  Microsoft Windows Server instances on Amazon EC2 up to 65%
  faster than before](https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/ "https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/")

**Related tools:**

- [Launch
  Microsoft Windows Server instances on Amazon EC2 up to 65%
  faster than before](https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/ "https://aws.amazon.com/blogs/modernizing-with-aws/launch-windows-faster-on-ec2/")

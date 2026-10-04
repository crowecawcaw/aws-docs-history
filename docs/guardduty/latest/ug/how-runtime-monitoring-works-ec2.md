

# Deploying the security agent to Amazon EC2
<a name="how-runtime-monitoring-works-ec2"></a>

GuardDuty Runtime Monitoring monitors your Amazon EC2 instances for threats by deploying the GuardDuty security agent to them.

**Note**  
Runtime Monitoring also collects runtime events from Amazon ECS tasks running on your Amazon EC2 instances.

You can let GuardDuty manage the agent automatically (recommended) or manage it manually.

## Automated agent configuration (recommended)
<a name="use-automated-agent-config-ec2"></a>

GuardDuty manages deployment and updates to the security agent for your Amazon EC2 instances. In the GuardDuty console, this configuration appears as *Runtime Monitoring (EC2)*.

For how the security agent connects to GuardDuty, see [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md).

**Impact of enabling the security agent**

With automated agent configuration, GuardDuty creates one SSM association for your SSM-managed Amazon EC2 instances (shown under **Fleet Manager** in the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/) console) and uses it to install and update the agent.

**Monitoring scope**

By default, GuardDuty manages the security agent for all Amazon EC2 instances in your account. To stop GuardDuty from managing the agent on a specific instance, add the tag `GuardDutyManaged`:`false` to that instance.

**Considerations**
+ When automated agent configuration is off, GuardDuty manages the security agent only on the Amazon EC2 instances that you tag with `GuardDutyManaged`:`true`.
+ Adding the `GuardDutyManaged`:`false` tag stops GuardDuty from managing the security agent, but doesn't uninstall an agent that is already installed.
+ Protect the `GuardDutyManaged` tag by controlling who can modify it, using service control policies or IAM policies. For more information, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *AWS Organizations User Guide* or [Control access to AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *IAM User Guide*.

## Manual agent configuration
<a name="ec2-security-agent-option2-manual"></a>

There are two ways to manage the security agent for Amazon EC2 manually:
+ For SSM-managed Amazon EC2 instances, you can use GuardDuty managed documents in AWS Systems Manager to install the security agent.
**Note**  
To use this option, ensure that each new Amazon EC2 instance you launch is SSM enabled.
+ Use RPM package manager (RPM) scripts to install the security agent on your Amazon EC2 instances, whether or not they are SSM managed.

## Related topics
<a name="ec2runmon-related"></a>
+ [How the security agent connects to GuardDuty](runtime-monitoring-agent-connectivity.md)
+ [Tracking Runtime Monitoring coverage](runtime-monitoring-after-configuration.md)
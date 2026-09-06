

# Prerequisites for Amazon EC2 instance support
<a name="prereq-runtime-monitoring-ec2-support"></a>

This section includes the prerequisites for monitoring runtime behavior of your Amazon EC2 instances. After these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md).

**Topics**
+ [Make EC2 instances SSM managed (for automated agent configuration only)](#ssm-managed-prereq-ec2)
+ [Validate architectural requirements](#validating-architecture-req-ec2)
+ [Validating your organization service control policy in a multi-account environment](#validate-organization-scp-ec2)
+ [When using automated agent configuration](#runtime-ec2-prereq-automated-agent)
+ [CPU and memory limit for GuardDuty agent](#ec2-cpu-memory-limits-gdu-agent)
+ [Next step](#next-step-after-prereq-ec2)

## Make EC2 instances SSM managed (for automated agent configuration only)
<a name="ssm-managed-prereq-ec2"></a>

GuardDuty uses AWS Systems Manager (SSM) to automatically deploy, install, and manage the security agent on your instances. If you plan to manually install and manage the GuardDuty agent, SSM is not required. 

To manage your Amazon EC2 instances with Systems Manager, see [Setting up Systems Manager for Amazon EC2 instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-setting-up-ec2.html) in the *AWS Systems Manager User Guide*.

## Validate architectural requirements
<a name="validating-architecture-req-ec2"></a>

The architecture of your OS distribution might impact how the GuardDuty security agent will behave. You must meet the following requirements before using Runtime Monitoring for Amazon EC2 instances:
+ Kernel support includes `eBPF`, `Tracepoints` and `Kprobe`. For CPU architectures, Runtime Monitoring supports AMD64 (`x64`) and ARM64 (Graviton2 and above)[1](#runtime-monitoring-ec2-graviton-2-support).

  The following table shows the OS distribution that has been verified to support the GuardDuty security agent for Amazon EC2 instances.    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html)

  1. <a name="runtime-monitoring-ec2-graviton-2-support"></a>Runtime Monitoring for Amazon EC2 resources doesn't support the first generation Graviton instance such as A1 instance types.

  1. <a name="runtime-monitoring-ec2-os-support"></a>Support for various operating systems - GuardDuty has verified Runtime Monitoring support for the operating distribution listed in the preceding table. While the GuardDuty security agent may run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the expected security value.

  1. <a name="runtime-monitoring-ec2-kernel-version-required-flag"></a>For any kernel version, you must set the `CONFIG_DEBUG_INFO_BTF` flag to `y` (meaning *true*). This is required so that the GuardDuty security agent can run as expected.

  1. <a name="runtime-monitoring-ec2-kernel-5-10"></a>For kernel versions 5.10 and earlier, the GuardDuty security agent uses locked memory in RAM (`RLIMIT_MEMLOCK`) to function as expected. If your system's `RLIMIT_MEMLOCK` value is set too low, GuardDuty recommends setting both hard and soft limits to at least 32 MB. For information about verifying and modifying the default `RLIMIT_MEMLOCK` value, see [Viewing and updating `RLIMIT_MEMLOCK` values](#runtime-monitoring-ec2-modify-rlimit-memlock).
+ Additional requirements - Only if you have Amazon ECS/Amazon EC2

  For Amazon ECS/Amazon EC2, we recommend that you use the latest Amazon ECS-optimized AMIs (dated September 29, 2023 or later), or use Amazon ECS agent version v1.77.0. 

### Viewing and updating `RLIMIT_MEMLOCK` values
<a name="runtime-monitoring-ec2-modify-rlimit-memlock"></a>

When your system's `RLIMIT_MEMLOCK` limit is set too low, GuardDuty security agent may not perform as designed. GuardDuty recommends that both hard and soft limits must be at least 32 MB. If you don't update the limits, GuardDuty will be unable to monitor the runtime events for your resource. When `RLIMIT_MEMLOCK` is above the minimum stated limits, it becomes optional for you to update these limits.

You can modify the default `RLIMIT_MEMLOCK` value either before or after installing the GuardDuty security agent. 

**To view `RLIMIT_MEMLOCK` values**

1. Run `ps aux | grep guardduty`. This will output the process ID (`pid`).

1. Copy the process ID (`pid`) from the output of the previous command.

1. Run `grep "Max locked memory" /proc/{{pid}}/limits` after replacing the `pid` with the process ID copied from the previous step.

   This will display the maximum locked memory for running the GuardDuty security agent.

**To update `RLIMIT_MEMLOCK` values**

1. If the `/etc/systemd/system.conf.d/{{NUMBER}}-limits.conf` file exists, then comment out the line of `DefaultLimitMEMLOCK` from this file. This file sets a default `RLIMIT_MEMLOCK` with high priority, which overwrites your settings in the `/etc/systemd/system.conf` file.

1. Open the `/etc/systemd/system.conf` file and uncomment the line that has `#DefaultLimitMEMLOCK=`.

1. Update the default value by providing both hard and soft `RLIMIT_MEMLOCK` limits to at least 32MB. The update should look like this: `DefaultLimitMEMLOCK=32M:32M`. The format is `soft-limit:hard-limit`.

1. Run `sudo reboot`.

## Validating your organization service control policy in a multi-account environment
<a name="validate-organization-scp-ec2"></a>

If you have set up a service control policy (SCP) to manage permissions in your organization, validate that permissions boundary allows the `guardduty:SendSecurityTelemetry` action. GuardDuty requires this permission to support Runtime Monitoring across different resource types.

If your account is a member account, contact the associated delegated administrator. For information about managing SCPs for your organization, see [Service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html).

## When using automated agent configuration
<a name="runtime-ec2-prereq-automated-agent"></a>

To [Use automated agent configuration (recommended)](how-runtime-monitoring-works-ec2.md#use-automated-agent-config-ec2), your AWS account must meet the following prerequisites:
+ When using inclusion tags with automated agent configuration, for GuardDuty to create an SSM association for a new instance, make sure that the new instance is SSM managed and shows up under **Fleet Manager** in the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/) console.
+ When using exclusion tags with automated agent configuration:
  + Add the `GuardDutyManaged`:`false` tag before configuring the GuardDuty automated agent for your account.

    Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent configuration for Amazon EC2, any EC2 instance that launches without an exclusion tag will be covered under GuardDuty automated agent configuration.
  + Enable **Allow tags in metadata** setting for your instances. This setting is required because GuardDuty needs to read the exclusion tag from the instance metadata service (IMDS) to determine whether it should exclude the instance from agent installation. For more information, see [Enable access to tags in instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.html#allow-access-to-tags-in-IMDS) in the *Amazon EC2 User Guide*.

## CPU and memory limit for GuardDuty agent
<a name="ec2-cpu-memory-limits-gdu-agent"></a>

**CPU limit**  
GuardDuty limits the security agent to 10 percent of the total vCPU capacity on the instance. For example, on an instance with 4 vCPU cores, the agent can use at most 0.4 vCPU.

**Memory limit**  
From the memory associated with your Amazon EC2 instance, there is a limited memory that the GuardDuty security agent can use.   
The following table shows the memory limit.      
[See the AWS documentation website for more details](http://docs.aws.amazon.com/guardduty/latest/ug/prereq-runtime-monitoring-ec2-support.html)

## Next step
<a name="next-step-after-prereq-ec2"></a>

The next step is to configure Runtime Monitoring and also manage the security agent (automatically or manually).
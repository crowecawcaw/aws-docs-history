# Prerequisites for Amazon EC2 instance

support

This section includes the prerequisites for monitoring runtime behavior of your Amazon EC2
instances. After these prerequisites are met, see [Enabling GuardDuty Runtime Monitoring](runtime-monitoring-configuration.md "runtime-monitoring-configuration.md").

###### Topics

- [Make EC2 instances SSM managed (for automated agent
  configuration only)](#ssm-managed-prereq-ec2 "#ssm-managed-prereq-ec2")
- [Validate architectural requirements](#validating-architecture-req-ec2 "#validating-architecture-req-ec2")
- [Validating your organization service control
  policy in a multi-account environment](#validate-organization-scp-ec2 "#validate-organization-scp-ec2")
- [When using automated agent
  configuration](#runtime-ec2-prereq-automated-agent "#runtime-ec2-prereq-automated-agent")
- [CPU and memory limit for GuardDuty agent](#ec2-cpu-memory-limits-gdu-agent "#ec2-cpu-memory-limits-gdu-agent")
- [Next step](#next-step-after-prereq-ec2 "#next-step-after-prereq-ec2")

## Make EC2 instances SSM managed (for automated agent

configuration only)

GuardDuty uses AWS Systems Manager (SSM) to automatically deploy, install, and manage the security agent
on your instances. If you plan to manually install and manage the GuardDuty agent, SSM is not
required.

To manage your Amazon EC2 instances with Systems Manager, see [Setting up Systems Manager for
Amazon EC2 instances](../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md "../../../systems-manager/latest/userguide/systems-manager-setting-up-ec2.md") in the _AWS Systems Manager User Guide_.

## Validate architectural requirements

The architecture of your OS distribution might impact how the GuardDuty security agent will
behave. You must meet the following requirements before using Runtime Monitoring for Amazon EC2
instances:

- Kernel support includes `eBPF`, `Tracepoints` and
  `Kprobe`. For CPU architectures, Runtime Monitoring supports AMD64 (`x64`) and
  ARM64 (Graviton2 and above)[1](#runtime-monitoring-ec2-graviton-2-support "#runtime-monitoring-ec2-graviton-2-support").

The following table shows the OS distribution that has been verified to support the GuardDuty
security agent for Amazon EC2 instances.

| OS distribution[2](#runtime-monitoring-ec2-os-support "#runtime-monitoring-ec2-os-support") | Kernel version[3](#runtime-monitoring-ec2-kernel-version-required-flag "#runtime-monitoring-ec2-kernel-version-required-flag")                                                                                                            |
| ------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon Linux 2                                                                              | 5.4[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.10[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.15                                                               |
| Amazon Linux 2023                                                                           | 5.4[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.10[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.15, 6.1, 6.5, 6.8, 6.12                                          |
| Ubuntu 20.04 and Ubuntu 22.04                                                               | 5.4[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.10[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.15, 6.1, 6.5, 6.8                                                |
| Debian 11 and Debian 12                                                                     | 5.4[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.10[4](#runtime-monitoring-ec2-kernel-5-10 "#runtime-monitoring-ec2-kernel-5-10"), 5.15, 6.1, 6.5, 6.8                                                |
| Ubuntu 24.04                                                                                | 6.8<br>6.13[5](#runtime-monitoring-ec2-ubuntu-noble-agent-version "#runtime-monitoring-ec2-ubuntu-noble-agent-version"), 6.14[5](#runtime-monitoring-ec2-ubuntu-noble-agent-version "#runtime-monitoring-ec2-ubuntu-noble-agent-version") |
| RedHat 9.4                                                                                  | 5.14                                                                                                                                                                                                                                      |
| Fedora 34.0                                                                                 | 5.11, 5.17                                                                                                                                                                                                                                |
| Fedora 40                                                                                   | 6.8                                                                                                                                                                                                                                       |
| Fedora 41                                                                                   | 6.12                                                                                                                                                                                                                                      |
| CentOS Stream 9                                                                             | 5.14                                                                                                                                                                                                                                      |
| Oracle Linux 8.9                                                                            | 5.15                                                                                                                                                                                                                                      |
| Oracle Linux 9.3                                                                            | 5.15                                                                                                                                                                                                                                      |
| Rocky Linux 9.5                                                                             | 5.14                                                                                                                                                                                                                                      |

    1. Runtime Monitoring for Amazon EC2 resources doesn't support the first generation Graviton
     instance such as A1 instance types.
    2. Support for various operating systems - GuardDuty has verified Runtime Monitoring
     support for the operating distribution listed in the preceding table. While the GuardDuty security agent may
     run on operating systems not listed in the preceding table, the GuardDuty team cannot guarantee the
     expected security value.
    3. For any kernel version, you must set the `CONFIG_DEBUG_INFO_BTF` flag to `y` (meaning *true*). This is required so that
     the GuardDuty security agent can run as expected.
    4. For kernel versions 5.10 and earlier, the GuardDuty security agent uses locked memory in
     RAM (`RLIMIT_MEMLOCK`) to function as expected. If your system's
     `RLIMIT_MEMLOCK` value is set too low, GuardDuty recommends setting both hard and
     soft limits to at least 32 MB. For information about verifying and modifying the default
     `RLIMIT_MEMLOCK` value, see [Viewing and updating
     RLIMIT\_MEMLOCK values](#runtime-monitoring-ec2-modify-rlimit-memlock "#runtime-monitoring-ec2-modify-rlimit-memlock").
    5. For Ubuntu 24.04, the kernel versions 6.13 and 6.14 support EC2 agent versions only 1.9.1 and above.

- Additional requirements - Only if you have Amazon ECS/Amazon EC2

For Amazon ECS/Amazon EC2, we recommend that you use the latest Amazon ECS-optimized AMIs (dated
September 29, 2023 or later), or use Amazon ECS agent version v1.77.0.

### Viewing and updating

`RLIMIT_MEMLOCK` values

When your system's `RLIMIT_MEMLOCK` limit is set too low, GuardDuty security agent
may not perform as designed. GuardDuty recommends that both hard and soft limits must be at least
32 MB. If you don't update the limits, GuardDuty will be unable to monitor the runtime events for
your resource. When `RLIMIT_MEMLOCK` is above the minimum stated limits, it becomes
optional for you to update these limits.

You can modify the default `RLIMIT_MEMLOCK` value either before or after
installing the GuardDuty security agent.

###### To view `RLIMIT_MEMLOCK` values

1. Run `ps aux | grep guardduty`. This will output the process ID
   (`pid`).
2. Copy the process ID (`pid`) from the output of the previous command.
3. Run `grep "Max locked memory" /proc/`pid`/limits`
   after replacing the `pid` with the process ID copied from the previous
   step.

This will display the maximum locked memory for running the GuardDuty security agent.

###### To update `RLIMIT_MEMLOCK` values

1. If the
   `/etc/systemd/system.conf.d/`NUMBER`-limits.conf`
   file exists, then comment out the line of `DefaultLimitMEMLOCK` from this file.
   This file sets a default `RLIMIT_MEMLOCK` with high priority, which overwrites
   your settings in the `/etc/systemd/system.conf` file.
2. Open the `/etc/systemd/system.conf` file and uncomment the line that
   has `#DefaultLimitMEMLOCK=`.
3. Update the default value by providing both hard and soft `RLIMIT_MEMLOCK`
   limits to at least 32MB. The update should look like this:
   `DefaultLimitMEMLOCK=32M:32M`. The format is
   `soft-limit:hard-limit`.
4. Run `sudo reboot`.

## Validating your organization service control

policy in a multi-account environment

If you have set up a service control policy (SCP) to manage permissions in your
organization, validate that permissions boundary allows the
`guardduty:SendSecurityTelemetry` action. It is required for GuardDuty to support
Runtime Monitoring across different resource types.

If you are a member account, connect with the associated delegated administrator. For
information about managing SCPs for your organization, see [Service control policies
(SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md").

## When using automated agent

configuration

To [Use automated agent configuration
(recommended)](how-runtime-monitoring-works-ec2.md#use-automated-agent-config-ec2 "how-runtime-monitoring-works-ec2.md#use-automated-agent-config-ec2"), your AWS account must meet the
following prerequisites:

- When using inclusion tags with automated agent configuration, for GuardDuty to create an SSM
  association for a new instance, ensure that the new instance is SSM managed and shows up under
  **Fleet Manager** in the [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/") console.
- When using exclusion tags with automated agent configuration:
  - Add the `GuardDutyManaged`:`false` tag before configuring the
    GuardDuty automated agent for your account.

  Ensure that you add the exclusion tag to your Amazon EC2 instances before you launch them. Once you have enabled automated agent
  configuration for Amazon EC2, any EC2 instance that launches
  without an exclusion tag will be covered under GuardDuty automated agent configuration.
  - Enable **Allow tags in metadata** setting for your instances. This
    setting is required because GuardDuty needs to read the exclusion tag from the
    instance metadata service (IMDS) to determine whether it should exclude
    the instance from agent installation. For
    more information, see [Enable
    access to tags in instance metadata](../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "../../../AWSEC2/latest/UserGuide/work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS") in the _Amazon EC2 User Guide_.

## CPU and memory limit for GuardDuty agent

**CPU limit**

The maximum CPU limit for the GuardDuty security agent associated with Amazon EC2 instances is 10
percent of the total vCPU cores. For example, if your EC2 instance has 4 vCPU cores, then the
security agent can use a maximum of 40 percent out of the total available 400 percent.

**Memory limit**

From the memory associated with your Amazon EC2 instance, there is a limited memory that the
GuardDuty security agent can use.

The following table shows the memory limit.

| Memory of the Amazon EC2 instance | Maximum memory for GuardDuty agent |
| --------------------------------- | ---------------------------------- |
| Less than 8 GB                    | 128 MB                             |
| Less than 32 GB                   | 256 MB                             |
| More than or equal to 32 GB       | 1 GB                               |

## Next step

The next step is to configure Runtime Monitoring and also manage the security agent (automatically or
manually).

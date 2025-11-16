# Use Systems Manager SSM documents with AWS FIS

AWS FIS supports custom fault types through the AWS Systems Manager SSM Agent and the AWS FIS action
[aws:ssm:send-command](fis-actions-reference.md#ssm-send-command "fis-actions-reference.md#ssm-send-command"). Pre-configured
Systems Manager SSM documents (SSM documents) that can be used to create common fault injection
actions are available as public AWS documents that begin with the AWSFIS- prefix.

SSM Agent is Amazon software that can be installed and configured on Amazon EC2 instances,
on-premises servers, or virtual machines (VMs). This makes it possible for Systems Manager to manage
these resources. The agent processes requests from Systems Manager, and then runs them as specified in
the request. You can include your own SSM document to inject custom faults, or reference
one of the public Amazon-owned documents.

###### Requirements

For actions that require SSM Agent to run the action on the target, you must ensure
the following:

- The agent is installed on the target. SSM Agent is installed by default on some
  Amazon Machine Images (AMIs). Otherwise, you can install the SSM Agent on your
  instances. For more information, see [Manually install SSM
  Agent for EC2 instances](../../../systems-manager/latest/userguide/sysman-manual-agent-install.md "../../../systems-manager/latest/userguide/sysman-manual-agent-install.md") in the
  _AWS Systems Manager User Guide_.
- Systems Manager has permission to perform actions on your instances. You grant access using
  an IAM instance profile. For more information, see [Create an IAM instance profile
  for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-profile.md "../../../systems-manager/latest/userguide/setup-instance-profile.md") and [Attach an IAM instance
  profile to an EC2 instance](../../../systems-manager/latest/userguide/setup-launch-managed-instance.md "../../../systems-manager/latest/userguide/setup-launch-managed-instance.md") in the
  _AWS Systems Manager User Guide_.

## Use the aws:ssm:send-command

action

An SSM document defines the actions that Systems Manager performs on your managed instances.
Systems Manager includes a number of pre-configured documents, or you can create your own. For
more information about creating your own SSM document, see [Creating Systems Manager
documents](../../../systems-manager/latest/userguide/create-ssm-doc.md "../../../systems-manager/latest/userguide/create-ssm-doc.md") in the _AWS Systems Manager User Guide_. For more information
about SSM documents in general, see [AWS Systems Manager
documents](../../../systems-manager/latest/userguide/sysman-ssm-docs.md "../../../systems-manager/latest/userguide/sysman-ssm-docs.md") in the _AWS Systems Manager User Guide_.

AWS FIS provides pre-configured SSM documents. You can view the pre-configured SSM
documents under **Documents** in the AWS Systems Manager console: [https://console.aws.amazon.com/systems-manager/documents](https://console.aws.amazon.com/systems-manager/documents "https://console.aws.amazon.com/systems-manager/documents"). You can also choose from a
selection of pre-configured documents in the AWS FIS console. For more information, see
[Pre-configured AWS FIS SSM documents](#fis-ssm-docs "#fis-ssm-docs").

To use an SSM document in your AWS FIS experiments, you can use the [aws:ssm:send-command](fis-actions-reference.md#ssm-send-command "fis-actions-reference.md#ssm-send-command") action. This action
fetches and runs the specified SSM document on your target instances.

When you use the `aws:ssm:send-command` action in your experiment template,
you must specify additional parameters for the action, including the following:

- **documentArn** – Required. The Amazon
  Resource Name (ARN) of the SSM document.
- **documentParameters** – Conditional.
  The required and optional parameters that the SSM document accepts. The format
  is a JSON object with keys that are strings and values that are either strings
  or arrays of strings.
- **documentVersion** – Optional. The
  version of the SSM document to run.

You can view the information for an SSM document (including the parameters for the
document) by using the Systems Manager console or the command line.

###### To view information about an SSM document using the console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Documents**.
3. Select the document, and choose the **Details** tab.

###### To view information about an SSM document using the command line

Use the SSM [describe-document](../../../cli/latest/reference/ssm/describe-document.md "../../../cli/latest/reference/ssm/describe-document.md") command.

###### Learn more about action state

SSM action state is determined by [SSM command statuses](../../../systems-manager/latest/userguide/monitor-commands.md "../../../systems-manager/latest/userguide/monitor-commands.md").

## Pre-configured AWS FIS SSM documents

You can use pre-configured AWS FIS SSM documents with the
`aws:ssm:send-command` action in your experiment templates.

###### Requirements

- The pre-configured SSM documents provided by AWS FIS are supported only on the
  following operating systems:
  - Amazon Linux 2023, Amazon Linux 2
  - Ubuntu
  - RHEL 8, 9
  - CentOS 9

- The pre-configured SSM documents provided by AWS FIS are supported only on EC2
  instances. They are not supported on other types of managed nodes, such as
  on-premises servers.

To use these SSM documents in experiments on ECS tasks, use the corresponding
[Amazon ECS actions](fis-actions-reference.md#ecs-actions-reference "fis-actions-reference.md#ecs-actions-reference"). For example, the **aws:ecs:task-cpu-stress**
action uses the AWSFIS-Run-CPU-Stress document.

###### Documents

- [AWSFIS-Run-CPU-Stress](#awsfis-run-cpu-stress "#awsfis-run-cpu-stress")
- [AWSFIS-Run-Disk-Fill](#awsfis-run-disk-fill "#awsfis-run-disk-fill")
- [AWSFIS-Run-IO-Stress](#awsfis-run-io-stress "#awsfis-run-io-stress")
- [AWSFIS-Run-Kill-Process](#awsfis-run-kill-process "#awsfis-run-kill-process")
- [AWSFIS-Run-Memory-Stress](#awsfis-run-memory-stress "#awsfis-run-memory-stress")
- [AWSFIS-Run-Network-Blackhole-Port](#awsfis-run-network-blackhole-port "#awsfis-run-network-blackhole-port")
- [AWSFIS-Run-Network-Latency](#awsfis-run-network-latency "#awsfis-run-network-latency")
- [AWSFIS-Run-Network-Latency-Sources](#awsfis-run-network-latency-sources "#awsfis-run-network-latency-sources")
- [AWSFIS-Run-Network-Packet-Loss](#awsfis-run-network-packet-loss "#awsfis-run-network-packet-loss")
- [AWSFIS-Run-Network-Packet-Loss-Sources](#awsfis-run-network-packet-loss-sources "#awsfis-run-network-packet-loss-sources")

######

Difference between action duration and DurationSeconds in AWS FIS SSM documents

Some SSM documents limit their own execution time, for example the DurationSeconds
parameter is used by some of the pre-configured AWS FIS SSM documents. As a result you need to specify
two independent durations in the AWS FIS action definition:

- **Action duration**: For experiments with a single action, the action duration
  is equivalent to the experiment duration. With multiple actions, the experiment duration
  depends on individual action durations and the order in which they are run. AWS FIS monitors
  each action until its action duration elapsed.
- Document parameter **DurationSeconds**: The duration, specified in seconds,
  for which the SSM document will execute.

You can choose different values for the two types of duration:

- **Action duration exceeds DurationSeconds**: The
  SSM document execution finishes before the action is complete. AWS FIS waits until the action
  duration elapsed before subsequent actions are started.
- **Action duration is shorter than DurationSeconds**: The SSM document continues the
  execution after the action is complete. If the SSM document execution is still in progress and the
  action duration elapsed then the action status is set to Completed. AWS FIS only monitors the execution
  until the action duration elapsed.

Note that some SSM documents have variable durations. For example AWS FIS SSM documents have the option
to install prerequisites, which can extend the overall execution duration beyond the specified
DurationSeconds parameter. Thus, if you set the action duration and DurationSeconds to the same value,
it is possible that the SSM script may run longer than the action duration.

### AWSFIS-Run-CPU-Stress

Runs CPU stress on an instance using the **stress-ng** tool. Uses
the [AWSFIS-Run-CPU-Stress](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-CPU-Stress/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-CPU-Stress/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-CPU-Stress

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-CPU-Stress

###### Document parameters

- **DurationSeconds** –
  Required. The duration of the CPU stress test, in seconds.
- **CPU** – Optional. The
  number of CPU stressors to use. The default is 0, which uses all CPU
  stressors.
- **LoadPercent** –
  Optional. The target CPU load percentage, from 0 (no load) to 100 (full
  load). The default is 100.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependency is
  **stress-ng**.

The following is an example of the string you can enter in the console.

```
{"DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Disk-Fill

Allocates disk space on the root volume of an instance to simulate a disk full
fault. Uses the [AWSFIS-Run-Disk-Fill](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Disk-Fill/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Disk-Fill/description") SSM document.

If the experiment injecting this fault is stopped, either manually or through a
stop condition, AWS FIS attempts to roll back by canceling the running SSM document.
However, if the disk is 100% full, either due to the fault or the fault plus
application activity, Systems Manager might be unable to complete the cancel operation.
Therefore, if you might need to stop the experiment, ensure that the disk will not
become 100% full.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Disk-Fill

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Disk-Fill

###### Document parameters

- **DurationSeconds** –
  Required. The duration of the disk fill test, in seconds.
- **Percent** – Optional.
  The percentage of the disk to allocate during the disk fill test.
  The default is 95%.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependencies are
  **atd**, **kmod** and **fallocate**.

The following is an example of the string you can enter in the console.

```
{"DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-IO-Stress

Runs IO stress on an instance using the **stress-ng** tool. Uses
the [AWSFIS-Run-IO-Stress](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-IO-Stress/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-IO-Stress/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-IO-Stress

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-IO-Stress

###### Document parameters

- **DurationSeconds** –
  Required. The duration of the IO stress test, in seconds.
- **Workers** – Optional.
  The number of workers that perform a mix of sequential, random, and
  memory-mapped read/write operations, forced synchronizing, and cache
  dropping. Multiple child processes perform different I/O operations on the
  same file. The default is 1.
- **Percent** – Optional.
  The percentage of free space on the file system to use during the IO stress
  test. The default is 80%.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependency is
  **stress-ng**.

The following is an example of the string you can enter in the console.

```
{"Workers":"1", "Percent":"80", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Kill-Process

Stops the specified process in the instance, using the **killall**
command. Uses the [AWSFIS-Run-Kill-Process](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Kill-Process/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Kill-Process/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Kill-Process

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Kill-Process

###### Document parameters

- **ProcessName** –
  Required. The name of the process to stop.
- **Signal** – Optional.
  The signal to send along with the command. The possible values are
  `SIGTERM` (which the receiver can choose to ignore) and
  `SIGKILL` (which cannot be ignored). The default is
  `SIGTERM`.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependency is
  **killall**.

The following is an example of the string you can enter in the console.

```
{"ProcessName":"myapplication", "Signal":"SIGTERM"}
```

### AWSFIS-Run-Memory-Stress

Runs memory stress on an instance using the **stress-ng** tool.
Uses the [AWSFIS-Run-Memory-Stress](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Memory-Stress/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Memory-Stress/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Memory-Stress

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Memory-Stress

###### Document parameters

- **DurationSeconds** –
  Required. The duration of the memory stress test, in seconds.
- **Workers** – Optional.
  The number of virtual memory stressors. The default is 1.
- **Percent** – Required.
  The percentage of virtual memory to use during the memory stress
  test.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependency is
  **stress-ng**.

The following is an example of the string you can enter in the console.

```
{"Percent":"80", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Network-Blackhole-Port

Drops inbound or outbound traffic for the protocol and port using the
**iptables** tool. Uses the [AWSFIS-Run-Network-Blackhole-Port](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Blackhole-Port/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Blackhole-Port/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Network-Blackhole-Port

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Network-Blackhole-Port

###### Document parameters

- **Protocol** –
  Required. The protocol. The possible values are `tcp` and
  `udp`.
- **Port** – Required.
  The port number.
- **TrafficType** –
  Optional. The type of traffic. The possible values are `ingress`
  and `egress`. The default is `ingress`.
- **DurationSeconds** –
  Required. The duration of the network blackhole test, in seconds.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependencies are
  **atd**, **dig**, **lsof**, and
  **iptables**.

The following is an example of the string you can enter in the console.

```
{"Protocol":"tcp", "Port":"8080", "TrafficType":"egress", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Network-Latency

Adds latency to the network interface using the **tc** tool. Uses
the [AWSFIS-Run-Network-Latency](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Network-Latency

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Network-Latency

###### Document parameters

- **Interface** –
  Optional. The network interface. The default is `eth0`.
- **DelayMilliseconds** –
  Optional. The delay, in milliseconds. The default is 200.
- **DurationSeconds** –
  Required. The duration of the network latency test, in seconds.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependencies are
  **atd**, **dig**, and
  **tc**.

The following is an example of the string you can enter in the console.

```
{"DelayMilliseconds":"200", "Interface":"eth0", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Network-Latency-Sources

Adds latency and jitter to the network interface using the **tc**
tool for traffic to or from specific sources. Uses the [AWSFIS-Run-Network-Latency-Sources](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency-Sources/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency-Sources/description") SSM document.

Use the `FlowsPercent` parameter to add latency on a percentage of the connections.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Network-Latency-Sources

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Network-Latency-Sources

###### Document parameters

- **Interface** –
  Optional. The network interfaces, separated by commas. ALL and DEFAULT values are supported. The default is `DEFAULT`, which will target the primary network interface for the Operating System.
- **DelayMilliseconds** –
  Optional. The delay, in milliseconds. The default is 200.
- **JitterMilliseconds**
  – Optional. The jitter, in milliseconds. The default is 10.
- **FlowsPercent**
  – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
- **Sources** – Required.
  The sources, separated by commas, without spaces. The possible values are: an IPv4 address,
  an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and
  `S3`. If you specify `DYNAMODB` or
  `S3`, this applies only to the Regional endpoint in the current
  Region.
- **TrafficType** –
  Optional. The type of traffic. The possible values are `ingress`
  and `egress`. The default is `ingress`.
- **DurationSeconds** –
  Required. The duration of the network latency test, in seconds.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances if they are not already
  installed. The default is `True`. The dependencies are
  **atd**, **dig**, **jq**, **lsof**,
  and **tc**.

When using this document, the experiment role requires the following permissions:

- `ec2:DescribeInstances`
- `ec2:DescribeSubnets`

The following is an example of the string you can enter in the console.

```
{"DelayMilliseconds":"200", "JitterMilliseconds":"15", "Sources":"S3,www.example.com,72.21.198.67", "Interface":"eth0", "TrafficType":"egress", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Network-Packet-Loss

Adds packet loss to the network interface using the **tc** tool.
Uses the [AWSFIS-Run-Network-Packet-Loss](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss/description") SSM document.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Network-Packet-Loss

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Network-Packet-Loss

###### Document parameters

- **Interface** –
  Optional. The network interface. The default is `eth0`.
- **LossPercent** –
  Optional. The percentage of packet loss. The default is 7%.
- **DurationSeconds** –
  Required. The duration of the network packet loss test, in seconds.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances. The default is
  `True`. The dependencies are **atd**, **lsof**,
  **dig**, and **tc**.

The following is an example of the string you can enter in the console.

```
{"LossPercent":"15", "Interface":"eth0", "DurationSeconds":"60", "InstallDependencies":"True"}
```

### AWSFIS-Run-Network-Packet-Loss-Sources

Adds packet loss to the network interface using the **tc** tool for
traffic to or from specific sources. Uses the [AWSFIS-Run-Network-Packet-Loss-Sources](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss-Sources/description "https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss-Sources/description") SSM document.

Use the `FlowsPercent` parameter to inject packet loss on a percentage of the connections.

###### Action type (console only)

aws:ssm:send-command/AWSFIS-Run-Network-Packet-Loss-Sources

###### ARN

arn:aws:ssm:region::document/AWSFIS-Run-Network-Packet-Loss-Sources

###### Document parameters

- **Interface** –
  Optional. The network interfaces, separated by commas. ALL and DEFAULT values are supported. The default is `DEFAULT`, which will target the primary network interface for the Operating System.
- **LossPercent** –
  Optional. The percentage of packet loss. The default is 7%.
- **FlowsPercent**
  – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
- **Sources** – Required.
  The sources, separated by commas, without spaces. The possible values are: an IPv4 address,
  an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and
  `S3`. If you specify `DYNAMODB` or
  `S3`, this applies only to the Regional endpoint in the current
  Region.
- **TrafficType** –
  Optional. The type of traffic. The possible values are `ingress`
  and `egress`. The default is `ingress`.
- **DurationSeconds** –
  Required. The duration of the network packet loss test, in seconds.
- **InstallDependencies**
  – Optional. If the value is `True`, Systems Manager installs the
  required dependencies on the target instances. The default is
  `True`. The dependencies are **atd**,
  **dig**, **jq**, **lsof**, and
  **tc**.

When using this document, the experiment role requires the following permissions:

- `ec2:DescribeInstances`
- `ec2:DescribeSubnets`

The following is an example of the string you can enter in the console.

```
{"LossPercent":"15", "Sources":"S3,www.example.com,72.21.198.67", "Interface":"eth0", "TrafficType":"egress", "DurationSeconds":"60", "InstallDependencies":"True"}
```

## Examples

For an example experiment template, see [Run a pre-configured AWS FIS SSM document](experiment-template-example.md#cpu-fault-injection "experiment-template-example.md#cpu-fault-injection").

For an example tutorial, see [Run CPU stress on an
instance](fis-tutorial-run-cpu-stress.md "fis-tutorial-run-cpu-stress.md").

## Limitations

- The following documents cannot run in parallel:
  - AWSFIS-Run-Network-Blackhole-Port
  - AWSFIS-Run-Network-Latency
  - AWSFIS-Run-Network-Latency-Sources
  - AWSFIS-Run-Network-Packet-Loss
  - AWSFIS-Run-Network-Packet-Loss-Sources

## Rollback scripts

AWS FIS SSM documents automatically create rollback scripts as a safety mechanism to restore system state after fault injection experiments. These scripts ensure that injected faults are removed, even if the action fails or is terminated unexpectedly.

### Rollback script creation

Rollback scripts are created automatically when fault injection experiments begin.

###### Creation details

- **Location** – Scripts are created in the `/var/lib/amazon/ssm/` directory.
- **Naming pattern** – ``FAULT_NAME`-`FAULT_IDENTIFIER`-Rollback.sh`where`FAULT_IDENTIFIER` is a randomly generated 32-character string
- **Timing** – Created at the beginning of each fault injection experiment, before fault injection starts.
- **Content** – Contains all necessary environment variables and commands to reverse the specific fault.

For example, a network latency experiment might create a rollback script at `/var/lib/amazon/ssm/NetworkLatency-abc123-Rollback.sh`.

### Rollback logging

Rollback scripts implement dual logging to capture all rollback activities for troubleshooting and audit purposes.

###### Log file locations

When a rollback script executes, it creates logs in two locations:

- **Temporary files** – `/tmp/aws-fis-rollback-`TIMESTAMP`-`PID`.log`
- **System logs** – Sent to syslog with facility `local0.info`

###### Log file naming

Temporary log files use the following naming convention:

```
/tmp/aws-fis-rollback-`YYYY-MM-DDTHH:MM:SSZ`-`PID`.log
```

Where `YYYY-MM-DDTHH:MM:SSZ` is the UTC timestamp and `PID` is the process ID of the rollback script.

###### Syslog configuration

Rollback logs are sent to syslog with the following configuration:

- **Tag** – `aws-fis-rollback`
- **Priority** – `local0.info`
- **Format** – `[YYYY-MM-DDTHH:MM:SSZ] `log_message``

###### To view rollback logs

Use the following command to view all rollback logs from the systemd journal:

```
sudo journalctl -t aws-fis-rollback
```

## Troubleshooting

Use the following procedure to troubleshoot issues.

###### To troubleshoot issues with SSM documents

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Node Management**,
   **Run Command**.
3. On the **Command history** tab, use the filters to locate
   the run of the document.
4. Choose the ID of the command to open its details page.
5. Choose the ID of the instance. Review the output and errors for each step.

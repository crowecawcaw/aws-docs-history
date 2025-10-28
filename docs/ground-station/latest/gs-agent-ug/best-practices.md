# Best practices

## Amazon EC2 best practices

Follow current EC2 best practices and ensure sufficient data storage availability.

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-best-practices.html](../../../AWSEC2/latest/UserGuide/ec2-best-practices.md "../../../AWSEC2/latest/UserGuide/ec2-best-practices.md")

## Linux scheduler

The Linux scheduler can re-order packets on UDP sockets if the corresponding processes are not pinned to a specific core.
Any thread sending or receiving UDP data should pin itself to a specific core for the duration of data transmission.

## AWS Ground Station managed prefix list

It is recommended to utilize the `com.amazonaws.global.groundstation` AWS-managed prefix list when specifying the network rules to allow communication from the Antenna. See [Working with AWS Managed Prefix Lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") for more information about AWS Managed Prefix Lists.

## Single contact limitation

The AWS Ground Station Agent supports multiple streams per contact, but only supports a single contact at a time.
To prevent scheduling issues, do not share an instance across multiple dataflow endpoint groups. If a single agent configuration is associated with multiple different DFEG ARNs, it will fail to register.

## Running services and processes alongside the AWS Ground Station Agent

When launching services and processes on the same EC2 Instance as the AWS Ground Station Agent, it is
important to bind them to vCPUs not in use by the AWS Ground Station Agent and Linux
kernel as this can cause bottlenecks and even data loss during contacts. This concept of binding
to specific vCPUs is known as affinity.

Cores to avoid:

- `agentCpuCores` from [Agent config file](configuring-agent.md#agent-config-file "configuring-agent.md#agent-config-file")
- `interrupt_core_list` from [Tune hardware interrupts and receive queues - impacts CPU and network](ec2-instance-performance-tuning.md#tune-hardware-interrupts "ec2-instance-performance-tuning.md#tune-hardware-interrupts").
  - Default values can be found from [Appendix: Recommended parameters for interrupt/RPS tune](ec2-instance-performance-tuning.md#recommended-parameters "ec2-instance-performance-tuning.md#recommended-parameters")

### As an example using a `c5.24xlarge` instance

If you specified

`"agentCpuCores": [24,25,26,27,72,73,74,75]"`

and ran

`echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '0,1,48,49' 'ffffffff,ffffffff,ffffffff' >> /var/log/user-data.log 2>&1" >>/var/spool/cron/root`

then avoid the following cores:

`0,1,24,25,26,27,48,49,72,73,74,75`

### Affinitizing services (systemd)

Newly launched services will automatically affinitize to the `interrupt_core_list`
mentioned previously. If your launched services' use-case requires additional cores, or
needs less congested cores, follow this section.

Check what affinity your service is currently configured to with command:

```

systemctl show --property CPUAffinity <service name>

```

If you see an empty value like `CPUAffinity=`, that means it will likely use the default cores from the above command
`...bin/set_irq_affinity.sh <using the cores here> ...`

To override and set a specific affinity find the location of the service file by running:

```

systemctl show -p FragmentPath <service name>

```

Open and modify the file (using `vi`, `nano`, etc.) and put the
`CPUAffinity=<core list>` in the `[Service]` section like:

```

[Unit]
...

[Service]
...
CPUAffinity=2,3

[Install]
...

```

Save the file and restart the service to apply the affinity with:

```

systemctl daemon-reload
systemctl restart <service name>

# Additionally confirm by re-running
systemctl show --property CPUAffinity <service name>

```

For more information visit:
[Red Hat Enterprise Linux 8 - Managing, monitoring, and updating the kernel - Chapter 27. Configuring CPU Affinity and NUMA policies using systemd](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/assembly_configuring-cpu-affinity-and-numa-policies-using-systemd_managing-monitoring-and-updating-the-kernel "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/managing_monitoring_and_updating_the_kernel/assembly_configuring-cpu-affinity-and-numa-policies-using-systemd_managing-monitoring-and-updating-the-kernel").

### Affinitizing processes (scripts)

It is highly recommended for newly launched scripts and processes to be manually affinitized as the
default Linux behavior will allow them to use any core on the machine.

To avoid core conflicts for any running processes (such as python, bash scripts, etc.), launch the process with:

```

taskset -c <core list> <command>
# Example: taskset -c 8 ./bashScript.sh

```

If the process is already running, use commands such as `pidof`, `top`, or `ps` to find the Process ID (PID) of the specific process. With the PID you can see current affinity with:

```

taskset -p <pid>

```

and can modify it with:

```

taskset -p <core mask> <pid>
# Example: taskset -p c 32392 (which sets it to cores 0xc -> 0b1100 -> cores 2,3)

```

For more information on taskset see [taskset - Linux man page](https://linux.die.net/man/1/taskset "https://linux.die.net/man/1/taskset")

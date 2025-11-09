# Methods for stopping an instance

There are four ways to perform a user-initiated stop: default stop, stop with skip OS
shutdown, force stop, and force stop with skip OS shutdown. The following table compares
the key differences between the stop methods:

| Stop method                      | Key purpose                                                                                                             | Use case                                                           | CLI command                                                                                                      |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- |
| Default stop                     | Normal instance shutdown with attempted graceful OS shutdown.                                                           | Typical instance stop.                                             | ``<br>aws ec2 stop-instances \<br>--instance-id `i-1234567890abcdef0`<br>``                                      |
| Stop with skip OS shutdown       | Bypasses the graceful OS shutdown when stopping an instance.                                                            | When bypassing graceful OS shutdown is required.                   | ``<br>aws ec2 stop-instances \<br>--instance-id `i-1234567890abcdef0` \<br>--skip-os-shutdown<br>``              |
| Force stop                       | Handles stuck instances. Attempts a default stop first; if instance fails to stop, then<br>forcibly stops the instance. | When instance is stuck in `stopping` state.                        | ``<br>aws ec2 stop-instances \<br>--instance-id `i-1234567890abcdef0` \<br>--force<br>``                         |
| Force stop with skip OS shutdown | Force stops and bypasses the graceful OS shutdown when stopping an<br>instance.                                         | When force stop and bypassing graceful OS shutdown is<br>required. | ``<br>aws ec2 stop-instances \<br>--instance-id `i-1234567890abcdef0` \<br>--force \<br>--skip-os-shutdown<br>`` |

For instructions on how to use each method, see the following:

- [Stop an instance with a
  graceful OS shutdown](Stop_Start.md#stop-instance-with-graceful-os-shutdown "Stop_Start.md#stop-instance-with-graceful-os-shutdown")
- [Stop an instance and
  bypass the graceful OS shutdown](Stop_Start.md#stop-instance-bypass-graceful-os-shutdown "Stop_Start.md#stop-instance-bypass-graceful-os-shutdown")
- [Force stop an instance](TroubleshootingInstancesStopping.md#force-stop-instance "TroubleshootingInstancesStopping.md#force-stop-instance")

###### Stop methods:

- [Default stop](#ec2-instance-default-stop "#ec2-instance-default-stop")
- [Stop with skip OS
  shutdown](#ec2-instance-stop-with-skip-os-shutdown "#ec2-instance-stop-with-skip-os-shutdown")
- [Force stop](#ec2-instance-force-stop "#ec2-instance-force-stop")
- [Force stop with skip
  OS shutdown](#ec2-instance-force-stop-with-skip-os-shutdown "#ec2-instance-force-stop-with-skip-os-shutdown")
  The following sections provide more detailed information about the four different
  user-initiated stop methods.

## Default stop

The default stop method is the standard way to stop an instance. When you issue
the StopInstances command, the instance transitions from the `running`
state, to `stopping`, and finally to `stopped`, as illustrated
by the following diagram:

![Default stop flow](images/stop-instance-flow-1.png)

**Purpose:** Normal instance shutdown with attempted
graceful OS shutdown.

**Data impact:** Preserves data on the EBS root volume and
data volumes. Loses data on the instance store volume.

**When to use:** First stop attempt for typical
stops.

###### Note

If you've already attempted a stop with skip OS shutdown, a subsequent default stop
attempt during the same state transition session will not perform a graceful OS
shutdown. Bypassing the graceful OS shutdown is irreversible for the instance's
current session.

## Stop with skip OS

shutdown

When bypassing the graceful OS shutdown is required, the stop with skip OS
shutdown method can be used to stop an instance and bypass the graceful OS shutdown,
as illustrated by the following diagram:

![Stop with skip OS shutdown flow](images/stop-instance-flow-3.png)

###### Warning

Bypassing the graceful OS shutdown might result in data loss or corruption
(for example, memory contents not flushed to disk or loss of in-flight IOs) or
skipped shutdown scripts.

**Purpose:** Bypass the graceful OS shutdown when
stopping an instance.

**Data impact:** Might result in data loss or
corruption. Contents of memory might not be flushed to disk and in-flight IOs might
be lost. Might skip shutdown scripts.

**When to use:** When bypassing the graceful OS shutdown is
required. If used while a default stop with graceful OS shutdown is in progress, the
graceful OS shutdown will be bypassed.

###### Note

Bypassing the graceful OS shutdown is irreversible for the instance's current state
transition session. A subsequent default stop attempt during this session will
not attempt a graceful OS shutdown.

## Force stop

The force stop method is used to handle instances that are stuck in the
`stopping` state. An instance typically becomes stuck due to an
underlying hardware issue (indicated by a failed [system status check](monitoring-system-instance-status-check.md#system-status-checks "monitoring-system-instance-status-check.md#system-status-checks")).

The force stop method first attempts a default stop. If the instance remains stuck in the
`stopping` state, the `force` parameter forcibly shuts
down the instance and transitions the instance to the `stopped` state, as
indicated by the following diagram:

![Force stop flow](images/stop-instance-flow-2.png)

**Purpose:** Handles instances stuck in the
`stopping` state. Attempts a default stop first. If the instance
fails to stop, then forcibly shuts down the instance.

**Data impact:** Attempts a default stop first, but if force
stop goes ahead, then might cause data loss or corruption. In rare cases, results in
post-stop writes to EBS volumes or other shared resources.

**When to use:** Second stop attempt when an instance remains
stuck after a default stop. For more information, see [Troubleshoot Amazon EC2 instance stop issues](TroubleshootingInstancesStopping.md "TroubleshootingInstancesStopping.md").

## Force stop with skip

OS shutdown

When force stopping and bypassing the graceful OS shutdown is required, the force
stop with skip OS shutdown method can be used to bring an instance to the
`stopped` state, as illustrated in the following diagram:

![Force stop with skip OS shutdown flow](images/stop-instance-flow-4.png)

**Purpose:** Combines force stop with bypassing a graceful OS
shutdown when stopping an instance.

**Data impact:** Skip OS shutdown might result in
data loss or corruption. Contents of memory might not be flushed to disk and
in-flight IOs might be lost. Might skip shutdown scripts. If force stop goes ahead,
then might cause additional data loss or corruption. In rare cases, results in
post-stop writes to the EBS volumes or other shared resources.

**When to use:** When you want to be sure that your
instance will stop and you want to bypass the graceful OS shutdown. If used while a
default stop with graceful OS shutdown is in progress, the graceful OS shutdown will
be bypassed.

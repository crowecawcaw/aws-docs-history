# Troubleshoot the ENA kernel driver on Linux

The Elastic Network Adapter (ENA) is designed to improve operating system health and
reduce the chances of long-term disruption because of unexpected hardware behavior and or
failures. The ENA architecture keeps device or driver failures as transparent to the system
as possible. This topic provides troubleshooting information for ENA.

If you are unable to connect to your instance, start with the
[Troubleshoot connectivity issues](#ena-connectivity-issues "#ena-connectivity-issues")
section.

If you experience performance degradation after migrating to a sixth generation instance
type, see the article [What do I need to do
before I migrate my EC2 instance to a sixth generation instance to make sure that I get
maximum network performance?](https://repost.aws/knowledge-center/migrate-to-gen6-ec2-instance "https://repost.aws/knowledge-center/migrate-to-gen6-ec2-instance")

If you are able to connect to your instance, you can gather diagnostic information by
using the failure detection and recovery mechanisms that are covered in the later sections
of this topic.

###### Contents

- [Troubleshoot connectivity issues](#ena-connectivity-issues "#ena-connectivity-issues")
- [Keep-alive mechanism](#ena-keep-alive "#ena-keep-alive")
- [Register read timeout](#register-read-timeout-ena "#register-read-timeout-ena")
- [Statistics](#statistics-ena "#statistics-ena")
- [Driver error logs in syslog](#driver-error-logs-ena "#driver-error-logs-ena")
- [Sub-optimal configuration notifications](#ts-ena-sub-opt-config-notification "#ts-ena-sub-opt-config-notification")

## Troubleshoot connectivity issues

If you lose connectivity while enabling enhanced networking, the
`ena` module might be incompatible with your instance's current
running kernel. This can happen if you install the module for a specific kernel version
(without **dkms**, or with an improperly configured
**dkms.conf** file) and then your instance kernel is updated. If the
instance kernel that is loaded at boot time does not have the `ena`
module properly installed, your instance will not recognize the network adapter and your
instance becomes unreachable.

If you enable enhanced networking for a PV instance or AMI, this can also
make your instance unreachable.

If your instance becomes unreachable after enabling enhanced networking with ENA, you
can disable the `enaSupport` attribute for your instance and it will
fall back to the stock network adapter.

###### To disable enhanced networking with ENA (EBS-backed instances)

1. From your local computer, stop the instance by using the Amazon EC2 console, the
   [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") command (AWS CLI), or the
   [Stop-EC2Instance](../../../powershell/latest/reference/items/Stop-EC2Instance.md "../../../powershell/latest/reference/items/Stop-EC2Instance.md") cmdlet (AWS Tools for PowerShell).
2. From your local computer, disable the enhanced networking attribute by using the
   [modify-instance-attribute](../../../cli/latest/reference/ec2/modify-instance-attribute.md "../../../cli/latest/reference/ec2/modify-instance-attribute.md")
   command with the `--no-ena-support` option or the
   [Edit-EC2InstanceAttribute](../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md "../../../powershell/latest/reference/items/Edit-EC2InstanceAttribute.md")
   cmdlet with the `-EnaSupport $false` parameter.
3. From your local computer, start the instance using the Amazon EC2 console, the
   [start-instances](../../../cli/latest/reference/ec2/start-instances.md "../../../cli/latest/reference/ec2/start-instances.md") command, or the
   [Start-EC2Instance](../../../powershell/latest/reference/items/Start-EC2Instance.md "../../../powershell/latest/reference/items/Start-EC2Instance.md") cmdlet.
4. (Optional) Connect to your instance and try reinstalling the
   `ena` module with your current kernel version by following
   the steps in [Enable enhanced networking with ENA on your EC2 instances](enhanced-networking-ena.md "enhanced-networking-ena.md").

###### To disable enhanced networking with ENA (instance store-backed instances)

1. Create a new AMI as described in [Create an Amazon S3-backed AMI](creating-an-ami-instance-store.md "creating-an-ami-instance-store.md").
2. When you register the AMI, be sure to include the `--no-ena-support` option in the
   [stop-instances](../../../cli/latest/reference/ec2/stop-instances.md "../../../cli/latest/reference/ec2/stop-instances.md") command (AWS CLI) or the
   `-EnaSupport $false` parameter in the
   [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") cmdlet.

## Keep-alive mechanism

The ENA device posts keep-alive events at a fixed rate (usually once every second).
The ENA driver implements a watchdog mechanism, which checks for the presence of
these keep-alive messages. If a message or messages are present, the watchdog is
rearmed, otherwise the driver concludes that the device experienced a failure and then
does the following:

- Dumps its current statistics to syslog
- Resets the ENA device
- Resets the ENA driver state

The above reset procedure may result in some traffic loss for a short
period of time (TCP connections should be able to recover), but should not otherwise
affect the user.

The ENA device may also indirectly request a device reset procedure, by not sending a
keep-alive notification, for example, if the ENA device reaches an unknown state after
loading an irrecoverable configuration.

The following is an example of the reset procedure:

```
`[18509.800135] ena 0000:00:07.0 eth1: Keep alive watchdog timeout. `// The watchdog process initiates a reset`
[18509.815244] ena 0000:00:07.0 eth1: Trigger reset is on
[18509.825589] ena 0000:00:07.0 eth1: tx_timeout: 0 `// The driver logs the current statistics`
[18509.834253] ena 0000:00:07.0 eth1: io_suspend: 0
[18509.842674] ena 0000:00:07.0 eth1: io_resume: 0
[18509.850275] ena 0000:00:07.0 eth1: wd_expired: 1
[18509.857855] ena 0000:00:07.0 eth1: interface_up: 1
[18509.865415] ena 0000:00:07.0 eth1: interface_down: 0
[18509.873468] ena 0000:00:07.0 eth1: admin_q_pause: 0
[18509.881075] ena 0000:00:07.0 eth1: queue_0_tx_cnt: 0
[18509.888629] ena 0000:00:07.0 eth1: queue_0_tx_bytes: 0
[18509.895286] ena 0000:00:07.0 eth1: queue_0_tx_queue_stop: 0
.......
........
[18511.280972] ena 0000:00:07.0 eth1: free uncompleted tx skb qid 3 idx 0x7 `// At the end of the down process, the driver discards incomplete packets.`
[18511.420112] [ENA_COM: ena_com_validate_version] ena device version: 0.10 `//The driver begins its up process`
[18511.420119] [ENA_COM: ena_com_validate_version] ena controller version: 0.0.1 implementation version 1
[18511.420127] [ENA_COM: ena_com_admin_init] ena_defs : Version:[b9692e8] Build date [Wed Apr 6 09:54:21 IDT 2016]
[18512.252108] ena 0000:00:07.0: Device watchdog is Enabled
[18512.674877] ena 0000:00:07.0: irq 46 for MSI/MSI-X
[18512.674933] ena 0000:00:07.0: irq 47 for MSI/MSI-X
[18512.674990] ena 0000:00:07.0: irq 48 for MSI/MSI-X
[18512.675037] ena 0000:00:07.0: irq 49 for MSI/MSI-X
[18512.675085] ena 0000:00:07.0: irq 50 for MSI/MSI-X
[18512.675141] ena 0000:00:07.0: irq 51 for MSI/MSI-X
[18512.675188] ena 0000:00:07.0: irq 52 for MSI/MSI-X
[18512.675233] ena 0000:00:07.0: irq 53 for MSI/MSI-X
[18512.675279] ena 0000:00:07.0: irq 54 for MSI/MSI-X
[18512.772641] [ENA_COM: ena_com_set_hash_function] Feature 10 isn't supported
[18512.772647] [ENA_COM: ena_com_set_hash_ctrl] Feature 18 isn't supported
[18512.775945] ena 0000:00:07.0: Device reset completed successfully `// The reset process is complete``
```

## Register read timeout

The ENA architecture suggests a limited usage of memory mapped I/O (MMIO) read
operations. MMIO registers are accessed by the ENA device driver only during its
initialization procedure.

If the driver logs (available in **dmesg** output) indicate failures of
read operations, this may be caused by an incompatible or incorrectly compiled driver, a
busy hardware device, or hardware failure.

Intermittent log entries that indicate failures on read operations should not be
considered an issue; the driver will retry them in this case. However, a sequence of log
entries containing read failures indicate a driver or hardware problem.

Below is an example of driver log entry indicating a read operation failure due to a
timeout:

```
`[ 47.113698] [ENA_COM: ena_com_reg_bar_read32] reading reg failed for timeout. expected: req id[1] offset[88] actual: req id[57006] offset[0] 
[ 47.333715] [ENA_COM: ena_com_reg_bar_read32] reading reg failed for timeout. expected: req id[2] offset[8] actual: req id[57007] offset[0] 
[ 47.346221] [ENA_COM: ena_com_dev_reset] Reg read32 timeout occurred`
```

## Statistics

If you experience insufficient network performance or latency issues, you should
retrieve the device statistics and examine them. These statistics can be obtained using
**ethtool** as follows.

````
`[ec2-user ~]$` `ethtool -S eth`N```NIC statistics:
 tx_timeout: 0
 suspend: 0
 resume: 0
 wd_expired: 0
 interface_up: 1
 interface_down: 0
 admin_q_pause: 0
 bw_in_allowance_exceeded: 0
 bw_out_allowance_exceeded: 0
 pps_allowance_exceeded: 0
 conntrack_allowance_available: 450878
 conntrack_allowance_exceeded: 0
 linklocal_allowance_exceeded: 0
 queue_0_tx_cnt: 4329
 queue_0_tx_bytes: 1075749
 queue_0_tx_queue_stop: 0
 ...`
````

The following command output parameters are described below:

`tx_timeout`: `N`

The number of times that the Netdev watchdog was activated.

`suspend`: `N`

The number of times the driver performed a suspend operation.

`resume`: `N`

The number of times the driver performed a resume operation.

`wd_expired`: `N`

The number of times that the driver did not receive the keep-alive
event in the preceding three seconds.

`interface_up`: `N`

The number of times that the ENA interface was brought up.

`interface_down`: `N`

The number of times that the ENA interface was brought down.

`admin_q_pause`: `N`

The number of times the admin queue was not found in a running
state.

`bw_in_allowance_exceeded`: `N`
The number of packets queued or dropped because the
inbound aggregate bandwidth exceeded the maximum for the instance.

`bw_out_allowance_exceeded`: `N`
The number of packets queued or dropped because the outbound
aggregate bandwidth exceeded the maximum for the instance.

`pps_allowance_exceeded`: `N`
The number of packets queued or dropped because the bidirectional
PPS exceeded the maximum for the instance. \*

`conntrack_allowance_available`:
`N`
The number of tracked connections that can be established
by the instance before hitting the Connections Tracked allowance of that instance type. Only available for Nitro-based
instances. Not supported with FreeBSD instances or DPDK environments.

`conntrack_allowance_exceeded`:
`N`
The number of packets dropped because connection tracking
exceeded the maximum for the instance and new connections could not be established. This can
result in packet loss for traffic to or from the instance.

`linklocal_allowance_exceeded`: `N`
The number of packets dropped because the PPS of the traffic
to local proxy services exceeded the maximum for the network interface. This impacts traffic to the
Amazon DNS service, the Instance Metadata Service, and the Amazon Time Sync Service, but does
not impact traffic to custom DNS resolvers.

`queue_`N`_tx_cnt`: `N`

The number of transmitted packets for this queue.

`queue_`N`_tx_bytes`: `N`

The number of transmitted bytes for this queue.

`queue_`N`_tx_queue_stop`: `N`

The number of times that queue `N` was full and stopped.

`queue_`N`_tx_queue_wakeup`: `N`

The number of times that queue `N` resumed after being stopped.

`queue_`N`_tx_dma_mapping_err`: `N`

Direct memory access error count. If this value is not 0, it indicates low system resources.

`queue_`N`_tx_linearize`: `N`

The number of times SKB linearization was attempted for this queue.

`queue_`N`_tx_linearize_failed`: `N`

The number of times SKB linearization failed for this queue.

`queue_`N`_tx_napi_comp`: `N`

The number of times the `napi` handler called `napi_complete` for this queue.

`queue_`N`_tx_tx_poll`:
`N`

The number of times the `napi` handler was scheduled for this queue.

`queue_`N`_tx_doorbells`: `N`

The number of transmission doorbells for this queue.

`queue_`N`_tx_prepare_ctx_err`: `N`

The number of times `ena_com_prepare_tx` failed for this
queue.

`queue_`N`_tx_bad_req_id`: `N`

Invalid `req_id` for this queue. The valid `req_id` is
zero, minus the `queue_size`, minus 1.

`queue_`N`_tx_llq_buffer_copy`: `N`

The number of packets whose headers size are larger than llq entry for
this queue.

`queue_`N`_tx_missed_tx`:
`N`

The number of packets that were left uncompleted for this queue.

`queue_`N`_tx_unmask_interrupt`: `N`

The number of times the tx interrupt was unmasked for this queue.

`queue_`N`_rx_cnt`: `N`

The number of received packets for this queue.

`queue_`N`_rx_bytes`: `N`

The number of received bytes for this queue.

`queue_`N`_rx_rx_copybreak_pkt`: `N`

The number of times the rx queue received a packet that is less than the rx_copybreak
packet size for this queue.

`queue_`N`_rx_csum_good`: `N`

The number of times the rx queue received a packet where the checksum was checked and
was correct for this queue.

`queue_`N`_rx_refil_partial`: `N`

The number of times the driver did not succeed in refilling the empty
portion of the rx queue with the buffers for this queue. If this value is
not zero, it indicates low memory resources.

`queue_`N`_rx_bad_csum`: `N`

The number of times the `rx` queue had a bad checksum for this
queue (only if rx checksum offload is supported).

`queue_`N`_rx_page_alloc_fail`: `N`

The number of time that page allocation failed for this queue. If this
value is not zero, it indicates low memory resources.

`queue_`N`_rx_skb_alloc_fail`: `N`

The number of time that SKB allocation failed for this queue. If this
value is not zero, it indicates low system resources.

`queue_`N`_rx_dma_mapping_err`: `N`

Direct memory access error count. If this value is not 0, it indicates low system resources.

`queue_`N`_rx_bad_desc_num`: `N`

Too many buffers per packet. If this value is not 0, it indicates the use of very small buffers.

`queue_`N`_rx_bad_req_id`: `N`

The req_id for this queue is not valid. The valid req_id is from [0, queue\_size - 1 ].

`queue_`N`_rx_empty_rx_ring`: `N`

The number of times the rx queue was empty for this queue.

`queue_`N`_rx_csum_unchecked`: `N`

The number of times the rx queue received a packet whose checksum wasn't checked for this queue.

`queue_`N`_rx_xdp_aborted`: `N`

The number of times that an XDP packet was classified as XDP_ABORT.

`queue_`N`_rx_xdp_drop`: `N`

The number of times that an XDP packet was classified as XDP_DROP.

`queue_`N`_rx_xdp_pass`: `N`

The number of times that an XDP packet was classified as XDP_PASS.

`queue_`N`_rx_xdp_tx`: `N`

The number of times that an XDP packet was classified as XDP_TX.

`queue_`N`_rx_xdp_invalid`: `N`

The number of times that the XDP return code for the packet was not valid.

`queue_`N`_rx_xdp_redirect`: `N`

The number of times that an XDP packet was classified as XDP_REDIRECT.

`queue_`N`_xdp_tx_cnt`: `N`

The number of transmitted packets for this queue.

`queue_`N`_xdp_tx_bytes`: `N`

The number of transmitted bytes for this queue.

`queue_`N`_xdp_tx_queue_stop`: `N`

The number of times that this queue was full and stopped.

`queue_`N`_xdp_tx_queue_wakeup`: `N`

The number of times that this queue resumed after being stopped.

`queue_`N`_xdp_tx_dma_mapping_err`: `N`

Direct memory access error count. If this value is not 0, it indicates low
system resources.

`queue_`N`_xdp_tx_linearize`: `N`

The number of times XDP buffer linearization was attempted for this
queue.

`queue_`N`_xdp_tx_linearize_failed`: `N`

The number of times XDP buffer linearization failed for this queue.

`queue_`N`_xdp_tx_napi_comp`: `N`

The number of times the napi handler called napi_complete for this
queue.

`queue_`N`_xdp_tx_tx_poll`: `N`

The number of times the napi handler was scheduled for this queue.

`queue_`N`_xdp_tx_doorbells`: `N`

The number of transmission doorbells for this queue.

`queue_`N`_xdp_tx_prepare_ctx_err`: `N`

The number of times ena_com_prepare_tx failed for this queue. This value
should always be zero; if not, see the driver logs.

`queue_`N`_xdp_tx_bad_req_id`: `N`

The req_id for this queue is not valid. The valid req_id is from [0,
queue\_size - 1 ].

`queue_`N`_xdp_tx_llq_buffer_copy`: `N`

The number of packets that had their headers copied using llq buffer copy
for this queue.

`queue_`N`_xdp_tx_missed_tx`: `N`

The number of times a tx queue entry missed a completion timeout for this
queue.

`queue_`N`_xdp_tx_unmask_interrupt`: `N`

The number of times the tx interrupt was unmasked for this queue.

`ena_admin_q_aborted_cmd`: `N`

The number of admin commands that were aborted. This usually happens
during the auto-recovery procedure.

`ena_admin_q_submitted_cmd`: `N`

The number of admin queue doorbells.

`ena_admin_q_completed_cmd`: `N`

The number of admin queue completions.

`ena_admin_q_out_of_space`: `N`

The number of times that the driver tried to submit new admin command,
but the queue was full.

`ena_admin_q_no_completion`: `N`

The number of times that the driver did not get an admin completion for a command.

## Driver error logs in syslog

The ENA driver writes log messages to **syslog** during system boot.
You can examine these logs to look for errors if you are experiencing issues. Below is
an example of information logged by the ENA driver in **syslog** during
system boot, along with some annotations for select messages.

```
`Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 478.416939] [ENA_COM: ena_com_validate_version] ena device version: 0.10
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 478.420915] [ENA_COM: ena_com_validate_version] ena controller version: 0.0.1 implementation version 1
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.256831] ena 0000:00:03.0: Device watchdog is Enabled
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.672947] ena 0000:00:03.0: creating 8 io queues. queue size: 1024
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.680885] [ENA_COM: ena_com_init_interrupt_moderation] Feature 20 isn't supported `// Interrupt moderation is not supported by the device`
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.691609] [ENA_COM: ena_com_get_feature_ex] Feature 10 isn't supported `// RSS HASH function configuration is not supported by the device`Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.694583] [ENA_COM: ena_com_get_feature_ex] Feature 18 isn't supported `//RSS HASH input source configuration is not supported by the device`
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.697433] [ENA_COM: ena_com_set_host_attributes] Set host attribute isn't supported
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.701064] ena 0000:00:03.0 (unnamed net_device) (uninitialized): Cannot set host attributes
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 479.704917] ena 0000:00:03.0: Elastic Network Adapter (ENA) found at mem f3000000, mac addr 02:8a:3c:1e:13:b5 Queues 8
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 480.805037] EXT4-fs (xvda1): re-mounted. Opts: (null)
Jun 3 22:37:46 ip-172-31-2-186 kernel: [ 481.025842] NET: Registered protocol family 10`
```

###### Which errors can I ignore?

The following warnings that may appear in your system's error logs can be ignored
for the Elastic Network Adapter:

**`Set host attribute isn't supported`**

Host attributes are not supported for this device.

**`failed to alloc buffer for rx queue`**

This is a recoverable error, and it indicates that there may have
been a memory pressure issue when the error was thrown.

**`Feature `X` isn't
 supported`**

The referenced feature is not supported by the Elastic Network
Adapter. Possible values for `X` include:

- 10: RSS Hash function configuration
  is not supported for this device.
- 12: RSS Indirection table
  configuration is not supported for this device.
- 18: RSS Hash Input configuration is
  not supported for this device.
- 20: Interrupt moderation is not
  supported for this device.
- 27: The Elastic Network Adapter driver
  does not support polling the Ethernet capabilities from snmpd.

**`Failed to config AENQ`**

The Elastic Network Adapter does not support AENQ
configuration.

**`Trying to set unsupported AENQ events`**

This error indicates an attempt to set an AENQ events group that
is not supported by the Elastic Network Adapter.

## Sub-optimal configuration notifications

The ENA device detects sub-optimal configuration settings in the driver
that you can change. The device notifies the ENA driver and logs a warning to
the console. The following example shows the format of the warning message.

```
`Sub-optimal configuration notification code: `1`. Refer to AWS ENA documentation for additional details and mitigation options.`
```

The following list shows notification code details and recommended actions for sub-optimal
configuration findings.

- **Code 1: ENA Express with wide LLQ configuration is not recommended**

ENA Express ENI is configured with wide LLQ. This configuration is
sub-optimal and could impact performance for ENA Express. We recommend that
you disable wide LLQ settings when you use ENA Express ENIs as follows.

```
sudo rmmod ena && sudo modprobe ena force_large_llq_header=0
```

For more information about optimal configuration for ENA Express, see
[Improve network performance between EC2 instances with ENA
Express](ena-express.md "ena-express.md").

- **Code 2: ENA Express ENI with sub-optimal Tx queue
  depth is not recommended**

ENA Express ENI is configured with sub-optimal Tx queue depth. This configuration
could impact performance for ENA Express. We recommend that you enlarge all Tx
queues to the maximum value for the network interface when you use ENA Express
ENIs as follows.

You can run the following **ethtool** commands to adjust
LLQ size. To learn more about how to control, query, and enable wide-LLQ, see the [Large Low-Latency Queue (Large LLQ)](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq") topic of the Linux kernel driver for
ENA documentation in the _Amazon Drivers GitHub repository_.

```
ethtool -g `interface`
```

Set your Tx queues to the maximum depth:

```
ethtool -G `interface` tx `depth`
```

For more information about optimal configuration for ENA Express, see
[Improve network performance between EC2 instances with ENA
Express](ena-express.md "ena-express.md").

- **Code 3: ENA with regular LLQ size and Tx packet
  traffic exceeds the maximum header supported size**

By default, ENA LLQ supports Tx packet header size up to 96 bytes. If the packet
header size is larger than 96 bytes, the packet is dropped. To mitigate this issue,
we recommend that you enable wide-LLQ, which increases the supported Tx packet
header size to a maximum of 224 bytes.

However, when you enable wide-LLQ, the maximum Tx ring size is reduced from 1000 to 512
entries. Wide-LLQ is enabled by default for all Nitro v4 and later instance types.

    + Nitro v4 instance types have a default maximum wide-LLQ Tx ring size of 512 entries,
     which can't be changed.
    + Nitro v5 instance types have a default wide-LLQ Tx ring size of 512 entries, which you
     can increase up to 1000 entries.

You can run the following **ethtool** commands to adjust
LLQ size. To learn more about how to control, query, and enable wide-LLQ, see the [Large Low-Latency Queue (Large LLQ)](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#large-low-latency-queue-large-llq") topic of the Linux kernel driver for
ENA documentation in the _Amazon Drivers GitHub repository_.

Find the maximum depth for your Tx queues:

```
ethtool -g `interface`
```

Set your Tx queues to the maximum depth:

```
ethtool -G `interface` tx `depth`
```

# Optimize network performance on EC2 Windows instances

To achieve the maximum network performance on your Windows instances with enhanced networking,
you might need to modify the default operating system configuration. We recommend the following
configuration changes for applications that require high network performance. Other
optimizations (such as turning on checksum offloading and enabling RSS, for example) are already
configured on official Windows AMIs.

###### Note

TCP chimney offloading should be disabled in most use cases, and has been deprecated
as of Windows Server 2016.

In addition to these operating system optimizations, you should also consider the maximum
transmission unit (MTU) of your network traffic, and adjust according to your workload and
network architecture. For more information, see [Network maximum transmission unit (MTU) for your EC2 instance](network_mtu.md "network_mtu.md").

AWS regularly measures average round trip latencies between instances launched in a
cluster placement group of 50us and tail latencies of 200us at the 99.9 percentile.
If your applications require consistently low latencies, we recommend using the latest
version of the ENA drivers on fixed performance instances built on the Nitro System.

## Configure Receive side scaling CPU affinity

Receive side scaling (RSS) is used to distribute network traffic CPU load across
multiple processors. By default, the official Amazon Windows AMIs are configured with
RSS enabled. ENA elastic network interfaces provide up to eight RSS queues. By defining CPU affinity for RSS
queues, as well as for other system processes, it is possible to spread the CPU load out
over multi-core systems, enabling more network traffic to be processed. On instance
types with more than 16 vCPUs, we recommend that you use the `Set-NetAdapterRSS`
PowerShell cmdlet, which manually excludes the boot processor (logical processor 0 and 1
when hyper-threading is enabled) from the RSS configuration for all elastic network interfaces, in order to prevent
contention with various system components.

Windows is hyper-thread aware and ensures that the RSS queues of a single network interface card (NIC) are
always placed on different physical cores. Therefore, unless hyper-threading is
disabled, in order to completely prevent contention with other NICs, spread the RSS
configuration of each NIC among a range of 16 logical processors. The
`Set-NetAdapterRss` cmdlet allows you to define the per-NIC range of
valid logical processors by defining the values of BaseProcessorGroup,
BaseProcessorNumber, MaxProcessingGroup, MaxProcessorNumber, and NumaNode (optional). If
there are not enough physical cores to completely eliminate inter-NIC contention,
minimize the overlapping ranges or reduce the number of logical processors in the elastic network interface
ranges depending on the expected workload of the interface (in other words, a low volume administrative
network interface may not need as many RSS queues assigned). Also, as previously noted,
various components must run on CPU 0, and therefore we recommend excluding it from all
RSS configurations when sufficient vCPUs are available.

For example, when there are three elastic network interfaces on a 72 vCPU instance with 2 NUMA nodes with
hyper-threading enabled, the following commands spread the network load between the two
CPUs without overlap and prevent the use of core 0 completely.

```
Set-NetAdapterRss -Name NIC1 -BaseProcessorGroup 0 -BaseProcessorNumber 2 -MaxProcessorNumber 16
Set-NetAdapterRss -Name NIC2 -BaseProcessorGroup 1 -BaseProcessorNumber 0 -MaxProcessorNumber 14
Set-NetAdapterRss -Name NIC3 -BaseProcessorGroup 1 -BaseProcessorNumber 16 -MaxProcessorNumber 30
```

Note that these settings are persistent for each network adapter. If an instance is
resized to one with a different number of vCPUs, you should reevaluate the RSS
configuration for each enabled elastic network interface. The complete Microsoft documentation for the
cmdlet can be found here: [Set-NetAdapterRss](https://learn.microsoft.com/en-us/powershell/module/netadapter/set-netadapterrss "https://learn.microsoft.com/en-us/powershell/module/netadapter/set-netadapterrss").

Special note for SQL workloads: We also recommend that you review your I/O thread
affinity settings along with your elastic network interface RSS configuration to minimize I/O and network
contention for the same CPUs. See [Server configuration: affinity mask](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-mask-server-configuration-option "https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/affinity-mask-server-configuration-option").

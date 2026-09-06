

# Tune your EC2 instance for performance
<a name="ec2-instance-performance-tuning"></a>

**Note**  
If you provisioned your AWS resources using CloudFormation templates these tunings are automatically applied. If you used an AMI or manually created your EC2 instance then these performance tunings must be applied to achieve the most reliable performance.

Remember to reboot your instance after applying any tuning(s).

**Topics**
+ [Tune hardware interrupts and receive queues - impacts CPU and network](#tune-hardware-interrupts)
+ [Tune Rx interrupt coalescing - impacts network](#tune-rx-interrupts)
+ [Tune Rx ring buffer - impacts network](#tune-rx-ring-buffer)
+ [Set kernel boot parameters (CPU C-State and interface naming) - impacts CPU and network](#tune-cpu-c-state)
+ [Reserve ingress ports - impacts network](#reserve-ingress-ports)
+ [Reboot](#reboot)

## Tune hardware interrupts and receive queues - impacts CPU and network
<a name="tune-hardware-interrupts"></a>

This section configures CPU core usage of systemd, SMP IRQs, Receive Packet Steering (RPS) and Receive Flow Steering (RFS). See [Appendix: Recommended parameters for interrupt/RPS tune](#recommended-parameters) for a set of recommended settings based on the instance type you are using.

**Important**  
 **Amazon Linux 2023 only:** Install and enable the cron daemon before continuing.   

```
sudo dnf install -y cronie
sudo systemctl enable --now crond
```
 This section and the two that follow it add `@reboot` crontab entries, which require a running cron daemon to take effect on each boot. On Amazon Linux 2023, the cron daemon is **not** installed by default, so without the commands above these entries are written but never run. On Amazon Linux 2, the cron daemon is already installed and enabled; no action is needed. 

1. Pin systemd processes away from agent CPU cores.

1. Route hardware interrupt requests away from agent CPU cores.

1. Configure RPS to prevent the hardware queue of a single network interface card from becoming a bottleneck in network traffic.

1. Configure RFS to increase the CPU cache hit rate and thereby reduce network latency.

The `set_irq_affinity.sh` script provided by the RPM configures all the above for you. Add to crontab, so it is applied on each boot:

```
echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '${interrupt_core_list}' '${rps_core_mask}' >> /var/log/user-data.log 2>&1" >>/var/spool/cron/root
```
+ Replace `interrupt_core_list` with cores reserved for the kernel and OS - typically the first and second along with hyper-threaded core pairs. This should not overlap with the cores selected above. (Ex: ‘0,1,48,49’ for a hyper-threaded, 96-CPU instance).
+ `rps_core_mask` is a hexadecimal bit mask specifying which CPUs should be processing incoming packets, with each digit representing 4 CPUs. It must also be comma separated every 8 characters starting from the right. It is recommended to allow all CPUs and let caching handle the balancing.
  + To see the list of recommended parameters for each instance type, refer to [Appendix: Recommended parameters for interrupt/RPS tune](#recommended-parameters).
+  Example for 96-CPU instance: 

  ```
  echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '0,1,48,49' 'ffffffff,ffffffff,ffffffff' >> /var/log/user-data.log 2>&1" >>/var/spool/cron/root
  ```

## Tune Rx interrupt coalescing - impacts network
<a name="tune-rx-interrupts"></a>

 Interrupt coalescing helps prevent flooding the host system with too many interrupts and helps increase network throughput. With this configuration, packets are collected and one single interrupt is generated every 128 microseconds. Add to crontab, so it is applied on each boot: 

```
echo "@reboot sudo ethtool -C ${interface} rx-usecs 128 tx-usecs 128 >>/var/log/user-data.log 2>&1" >>/var/spool/cron/root
```
+ Replace `interface` with the network interface (ethernet adapter) configured to receive data. Typically, this is `eth0` as that's the default network interface assigned for an EC2 instance.

## Tune Rx ring buffer - impacts network
<a name="tune-rx-ring-buffer"></a>

 Increase the number of ring entries for the Rx ring buffer to prevent packet drops or overruns during bursty connections. Add to the crontab, so it is correctly set on each boot: 

```
echo "@reboot sudo ethtool -G ${interface} rx 16384 >>/var/log/user-data.log 2>&1" >>/var/spool/cron/root
```
+ Replace `interface` with the network interface (ethernet adapter) configured to receive data. Typically, this is `eth0` as that's the default network interface assigned for an EC2 instance.
+ If setting up a `c6i` family instance, command needs to be modified to set the ring buffer to `8192`, instead of `16384`.

## Set kernel boot parameters (CPU C-State and interface naming) - impacts CPU and network
<a name="tune-cpu-c-state"></a>

 These kernel boot parameters prevent CPU idling by setting `intel_idle.max_cstate=1 processor.max_cstate=1 max_cstate=1`. CPU idling can cause lost packets at the start of a contact. The parameters also include `net.ifnames=0 biosdevname=0`, which rename the receiver's network interface to `eth0`. Like the other tuning steps in this chapter, these parameters take effect at the reboot described in [Reboot](#reboot). You can apply them in any order relative to the other sections. 

 Use `grubby` to set the kernel arguments. This works on both Amazon Linux 2023 (UEFI) and Amazon Linux 2 because `grubby` manages the bootloader configuration directly on both. 

```
sudo grubby --update-kernel=ALL --args="console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 intel_idle.max_cstate=1 processor.max_cstate=1 max_cstate=1"
```

**Note**  
 The `net.ifnames=0` argument renames the network interface to `eth0` on the next boot. The other tuning sections and the agent configuration target `eth0`, so applying these parameters and rebooting is the recommended path. If you choose not to apply these parameters, the interface keeps its default name (for example, `ens5` on Amazon Linux 2023). In that case, substitute the actual interface name — found by running `ip link show` — everywhere this guide uses `eth0`. 

## Reserve ingress ports - impacts network
<a name="reserve-ingress-ports"></a>

 Reserve all ports in your `AwsGroundStationAgentEndpoint`’s ingress address port range to prevent conflicts with kernel usage. Port usage conflict will lead to contact and data delivery failure. 

```
echo "net.ipv4.ip_local_reserved_ports=${port_range_min}-${port_range_max}" >> /etc/sysctl.conf
```
+ Example: `echo "net.ipv4.ip_local_reserved_ports=42000-43500" >> /etc/sysctl.conf`.

## Reboot
<a name="reboot"></a>

After all tunings are applied successfully, reboot the instance for the tunings to take effect.

```
sudo reboot
```

## Appendix: Recommended parameters for interrupt/RPS tune
<a name="recommended-parameters"></a>

 This section determines the recommended parameter values for use in tuning section Tune Hardware Interrupts and Receive Queues - Impacts CPU and Network. 


| Family | Instance Type | ${interrupt\_core\_list} | ${rps\_core\_mask} | 
| --- | --- | --- | --- | 
| c7i |  + c7i.24xlarge<br />+ c7i.12xlarge  |  + 0,1,48,49<br />+ 0,1,24,25  |  + ffffffff,ffffffff,ffffffff<br />+ ffff,ffffffff  | 
| c6i |  + c6i.32xlarge  |  + 0,1,64,65  |  + ffffffff,ffffffff,ffffffff,ffffffff  | 
| c5 |  + c5.24xlarge<br />+ c5.18xlarge<br />+ c5.12xlarge  |  + 0,1,48,49<br />+ 0,1,36,37<br />+ 0,1,24,25  |  + ffffffff,ffffffff,ffffffff<br />+ ff,ffffffff,ffffffff<br />+ ffff,ffffffff  | 
| c5n |  + c5n.metal<br />+ c5n.18xlarge  |  + 0,1,36,37<br />+ 0,1,36,37  |  + ff,ffffffff,ffffffff<br />+ ff,ffffffff,ffffffff  | 
| m5 |  + m5.24xlarge<br />+ m5.12xlarge  |  + 0,1,48,49<br />+ 0,1,24,25  |  + ffffffff,ffffffff,ffffffff<br />+ ffff,ffffffff  | 
| r5 |  + r5.metal<br />+ r5.24xlarge  |  + 0,1,48,49<br />+ 0,1,48,49  |  + ffffffff,ffffffff,ffffffff<br />+ ffffffff,ffffffff,ffffffff  | 
| r5n |  + r5n.metal<br />+ r5n.24xlarge  |  + 0,1,48,49<br />+ 0,1,48,49  |  + ffffffff,ffffffff,ffffffff<br />+ ffffffff,ffffffff,ffffffff  | 
| g4dn |  + g4dn.metal<br />+ g4dn.16xlarge<br />+ g4dn.12xlarge  |  + 0,1,48,49<br />+ 0,1,32,33<br />+ 0,1,24,25  |  + ffffffff,ffffffff,ffffffff<br />+ ffffffff,ffffffff<br />+ ffff,ffffffff  | 
| p4d |  + p4d.24xlarge  |  + 0,1,48,49  |  + ffffffff,ffffffff,ffffffff  | 
| p3dn |  + p3dn.24xlarge  |  + 0,1,48,49  |  + ffffffff,ffffffff,ffffffff  | 
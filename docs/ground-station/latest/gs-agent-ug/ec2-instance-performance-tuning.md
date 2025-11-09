# Tune your EC2 instance for performance

###### Note

If you provisioned your AWS resources using CloudFormation templates these tunings are automatically applied.
If you used an AMI or manually created your EC2 instance then these performance tunings must be applied to achieve the most reliable performance.

Remember to reboot your instance after applying any tuning(s).

**Topics**

- [Tune hardware interrupts and receive queues - impacts CPU and network](#tune-hardware-interrupts "#tune-hardware-interrupts")
- [Tune Rx interrupt coalescing - impacts network](#tune-rx-interrupts "#tune-rx-interrupts")
- [Tune Rx ring buffer - impacts network](#tune-rx-ring-buffer "#tune-rx-ring-buffer")
- [Tune CPU C-State - impacts CPU](#tune-cpu-c-state "#tune-cpu-c-state")
- [Reserve ingress ports - impacts network](#reserve-ingress-ports "#reserve-ingress-ports")
- [Reboot](#reboot "#reboot")

## Tune hardware interrupts and receive queues - impacts CPU and network

This section configures CPU core usage of systemd, SMP IRQs, Receive Packet Steering (RPS) and Receive Flow Steering (RFS). See [Appendix: Recommended parameters for interrupt/RPS tune](#recommended-parameters "#recommended-parameters") for a set of recommended settings based on the instance type you are using.

1. Pin systemd processes away from agent CPU cores.
2. Route hardware interrupt requests away from agent CPU cores.
3. Configure RPS to prevent the hardware queue of a single network interface card from becoming a bottleneck in network traffic.
4. Configure RFS to increase the CPU cache hit rate and thereby reduce network latency.

The `set_irq_affinity.sh` script provided by the RPM configures all the above for you.
Add to crontab, so it is applied on each boot:

```

echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '${interrupt_core_list}' '${rps_core_mask}' >> /var/log/user-data.log 2>&1" >>/var/spool/cron/root

```

- Replace `interrupt_core_list` with cores reserved for the kernel and OS - typically the first and second along with hyper-threaded core pairs.
  This should not overlap with the cores selected above. (Ex: ‘0,1,48,49’ for a hyper-threaded, 96-CPU instance).
- `rps_core_mask` is a hexadecimal bit mask specifying which CPUs should be processing incoming packets, with each digit representing 4 CPUs.
  It must also be comma separated every 8 characters starting from the right. It is recommended to allow all CPUs and let caching handle the balancing.
  - To see the list of recommended parameters for each instance type, refer to [Appendix: Recommended parameters for interrupt/RPS tune](#recommended-parameters "#recommended-parameters").

- Example for 96-CPU instance:

```

echo "@reboot sudo /opt/aws/groundstation/bin/set_irq_affinity.sh '0,1,48,49' 'ffffffff,ffffffff,ffffffff' >> /var/log/user-data.log 2>&1" >>/var/spool/cron/root

```

## Tune Rx interrupt coalescing - impacts network

Interrupt coalescing helps prevent flooding the host system with too many interrupts and helps increase network throughput.
With this configuration, packets are collected and one single interrupt is generated every 128 microseconds.
Add to crontab, so it is applied on each boot:

```

echo "@reboot sudo ethtool -C ${interface} rx-usecs 128 tx-usecs 128 >>/var/log/user-data.log 2>&1" >>/var/spool/cron/root

```

- Replace `interface` with the network interface (ethernet adapter) configured to receive data.
  Typically, this is `eth0` as that's the default network interface assigned for an EC2 instance.

## Tune Rx ring buffer - impacts network

Increase the number of ring entries for the Rx ring buffer to prevent packet drops or overruns during bursty connections.
Add to the crontab, so it is correctly set on each boot:

```

echo "@reboot sudo ethtool -G ${interface} rx 16384 >>/var/log/user-data.log 2>&1" >>/var/spool/cron/root

```

- Replace `interface` with the network interface (ethernet adapter) configured to receive data.
  Typically, this is `eth0` as that's the default network interface assigned for an EC2 instance.
- If setting up a `c6i` family instance, command needs to be modified to set the ring buffer to `8192`,
  instead of `16384`.

## Tune CPU C-State - impacts CPU

Set the CPU C-state to prevent idling which can cause lost packets during the start of a contact. Requires instance reboot.

```

echo "GRUB_CMDLINE_LINUX_DEFAULT=\"console=tty0 console=ttyS0,115200n8 net.ifnames=0 biosdevname=0 nvme_core.io_timeout=4294967295 intel_idle.max_cstate=1 processor.max_cstate=1 max_cstate=1\"" >/etc/default/grub
echo "GRUB_TIMEOUT=0" >>/etc/default/grub
grub2-mkconfig -o /boot/grub2/grub.cfg

```

## Reserve ingress ports - impacts network

Reserve all ports in your `AwsGroundStationAgentEndpoint`’s ingress address port range to prevent conflicts with kernel usage.
Port usage conflict will lead to contact and data delivery failure.

```

echo "net.ipv4.ip_local_reserved_ports=${port_range_min}-${port_range_max}" >> /etc/sysctl.conf

```

- Example: `echo "net.ipv4.ip_local_reserved_ports=42000-43500" >> /etc/sysctl.conf`.

## Reboot

After all tunings are applied successfully, reboot the instance for the tunings to take effect.

```

sudo reboot

```

## Appendix: Recommended parameters for interrupt/RPS tune

This section determines the recommended parameter values for use in tuning section Tune Hardware Interrupts and Receive Queues - Impacts CPU and Network.

| Family | Instance Type                                      | ${interrupt_core_list}                    | ${rps_core_mask}                                                          |
| ------ | -------------------------------------------------- | ----------------------------------------- | ------------------------------------------------------------------------- |
| c6i    | • c6i.32xlarge                                     | • 0,1,64,65                               | • ffffffff,ffffffff,ffffffff,ffffffff                                     |
| c5     | • c5.24xlarge<br>• c5.18xlarge<br>• c5.12xlarge    | • 0,1,48,49<br>• 0,1,36,37<br>• 0,1,24,25 | • ffffffff,ffffffff,ffffffff<br>• ff,ffffffff,ffffffff<br>• ffff,ffffffff |
| c5n    | • c5n.metal<br>• c5n.18xlarge                      | • 0,1,36,37<br>• 0,1,36,37                | • ff,ffffffff,ffffffff<br>• ff,ffffffff,ffffffff                          |
| m5     | • m5.24xlarge<br>• m5.12xlarge                     | • 0,1,48,49<br>• 0,1,24,25                | • ffffffff,ffffffff,ffffffff<br>• ffff,ffffffff                           |
| r5     | • r5.metal<br>• r5.24xlarge                        | • 0,1,48,49<br>• 0,1,48,49                | • ffffffff,ffffffff,ffffffff<br>• ffffffff,ffffffff,ffffffff              |
| r5n    | • r5n.metal<br>• r5n.24xlarge                      | • 0,1,48,49<br>• 0,1,48,49                | • ffffffff,ffffffff,ffffffff<br>• ffffffff,ffffffff,ffffffff              |
| g4dn   | • g4dn.metal<br>• g4dn.16xlarge<br>• g4dn.12xlarge | • 0,1,48,49<br>• 0,1,32,33<br>• 0,1,24,25 | • ffffffff,ffffffff,ffffffff<br>• ffffffff,ffffffff<br>• ffff,ffffffff    |
| p4d    | • p4d.24xlarge                                     | • 0,1,48,49                               | • ffffffff,ffffffff,ffffffff                                              |
| p3dn   | • p3dn.24xlarge                                    | • 0,1,48,49                               | • ffffffff,ffffffff,ffffffff                                              |

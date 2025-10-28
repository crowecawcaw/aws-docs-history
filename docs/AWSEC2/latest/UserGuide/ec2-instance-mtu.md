# Set the MTU for your Amazon EC2 instances

The maximum transmission unit (MTU) of a network connection is the size, in bytes,
of the largest permissible packet that can be passed over the connection. All Amazon EC2
instances support standard frames (1500 MTU) and all current generation instance
types support jumbo frames (9001 MTU).

You can view the MTU for your Amazon EC2 instances, view the path MTU between
your instance and another host, and configure your instances to use either
standard or jumbo frames.

###### Tasks

- [Check the path MTU between two hosts](#check_path_mtu "#check_path_mtu")
- [Check the MTU for your instance](#check_mtu "#check_mtu")
- [Set the MTU for your instance](#set_mtu "#set_mtu")

## Check the path MTU between two hosts

You can check the path MTU between your EC2 instance and another host. You can specify
a DNS name or an IP address as the destination. If the destination is another EC2 instance,
verify that its security group allows inbound UDP traffic.

The procedure that you use depends on the operating system of the instance.

Run the **tracepath** command on your instance to check the path MTU
between your EC2 instance and the specified destination. This command is part of the
`iputils` package, which is available by default in many Linux
distributions.

This example checks the path MTU between the EC2 instance and `amazon.com`.

```
`[ec2-user ~]$` tracepath `amazon.com`
```

In this example output, the path MTU is 1500.

```
 1?: [LOCALHOST]     pmtu 9001
 1:  ip-172-31-16-1.us-west-1.compute.internal (172.31.16.1)   0.187ms pmtu 1500
 1:  no reply
 2:  no reply
 3:  no reply
 4:  100.64.16.241 (100.64.16.241)                          0.574ms
 5:  72.21.222.221 (72.21.222.221)                         84.447ms asymm 21
 6:  205.251.229.97 (205.251.229.97)                       79.970ms asymm 19
 7:  72.21.222.194 (72.21.222.194)                         96.546ms asymm 16
 8:  72.21.222.239 (72.21.222.239)                         79.244ms asymm 15
 9:  205.251.225.73 (205.251.225.73)                       91.867ms asymm 16
...
31:  no reply
     Too many hops: pmtu 1500
     Resume: pmtu 1500
```

###### To check path MTU using mturoute

1. Download **mturoute.exe** to your EC2 instance from [https://elifulkerson.com/projects/mturoute.php](https://elifulkerson.com/projects/mturoute.php "https://elifulkerson.com/projects/mturoute.php").
2. Open a Command Prompt window and change to the directory where you downloaded
   **mturoute.exe**.
3. Use the following command to check the path MTU between your EC2 instance
   and the specified destination. This example checks the path MTU between the
   EC2 instance and `www.elifulkerson.com`.

```
.\mturoute.exe `www.elifulkerson.com`
```

In this example output, the path MTU is 1500.

```
* ICMP Fragmentation is not permitted. *
* Speed optimization is enabled. *
* Maximum payload is 10000 bytes. *
+ ICMP payload of 1472 bytes succeeded.
- ICMP payload of 1473 bytes is too big.
Path MTU: 1500 bytes.
```

## Check the MTU for your instance

You can check the MTU value for your instance. Some instances are configured to use jumbo
frames, and others are configured to use standard frame sizes.

The procedure that you use depends on the operating system of the instance.

###### To check the MTU setting on a Linux instance

Run the following **ip** command on your EC2 instance. If the
primary network interface is not `eth0`, replace `eth0`
with your network interface.

```
`[ec2-user ~]$` ip link show `eth0`
```

In this example output, `mtu 9001` indicates that the
instance uses jumbo frames.

```
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> `mtu 9001` qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 02:90:c0:b7:9e:d1 brd ff:ff:ff:ff:ff:ff
```

The procedure that you use depends on the driver on your instance.

ENA driver

###### Version 2.1.0 and later

To get the MTU value, use the following
**Get-NetAdapterAdvancedProperty** command on
your EC2 instance. Use the wildcard (asterisk) to get all
Ethernet names. Check the output for the interface name
`*JumboPacket`. A value of 9015 indicates that
Jumbo frames are enabled. Jumbo frames are disabled by
default.

```
Get-NetAdapterAdvancedProperty -Name "Ethernet*"
```

###### Version 1.5 and earlier

To get the MTU value, use the following
**Get-NetAdapterAdvancedProperty** command on
your EC2 instance. Check the output for the interface name
`MTU`. A value of 9001 indicates that Jumbo
frames are enabled. Jumbo frames are disabled by default.

```
Get-NetAdapterAdvancedProperty -Name "Ethernet"
```

Intel SRIOV 82599 driver
To get the MTU value, use the following
**Get-NetAdapterAdvancedProperty** command on
your EC2 instance. Check the entry for the interface name
`*JumboPacket`. A value of 9014 indicates that Jumbo
frames are enabled. (Note that the MTU size includes the header and
the payload.) Jumbo frames are disabled by default.

```
Get-NetAdapterAdvancedProperty -Name "Ethernet"
```

AWS PV driver
To get the MTU value, use the following command on your EC2
instance. The name of the interface can vary. In the output, look
for an entry with the name "Ethernet," "Ethernet 2," or "Local Area
Connection". You'll need the interface name to enable or disable
jumbo frames. A value of 9001 indicates that Jumbo frames are
enabled.

```
netsh interface ipv4 show subinterface
```

## Set the MTU for your instance

You might want to use jumbo frames for network traffic within your
VPC and standard frames for internet traffic. Whatever your use case, we recommend
that you verify that your instance behaves as expected.

The procedure that you use depends on the operating system of the instance.

###### To set the MTU value on a Linux instance

1. Run the following **ip** command on your instance. It
   sets the desired MTU value to 1500, but you could use 9001 instead.
   If the primary network interface is not `eth0`, replace `eth0`
   with the actual network interface.

```
`[ec2-user ~]$` sudo ip link set dev `eth0` mtu `1500`
```

2. (Optional) To persist your network MTU setting after a reboot, modify the
   following configuration files, based on your operating system type.
   - Amazon Linux 2023 – Modify the `[Link]` section of the config file.
     The default config file is `/usr/lib/systemd/network/80-ec2.network`,
     or you can update any custom config file created in /run/systemd/network/, where the
     file name is `priority`-`interface`.network.
     For more information, see [Networking service](../../../linux/al2023/ug/networking-service.md "../../../linux/al2023/ug/networking-service.md") in the Amazon Linux documentation.

   ```
   MTUBytes=`1500`
   ```

   - Amazon Linux 2 – Add the following line to the
     `/etc/sysconfig/network-scripts/ifcfg-`eth0``
     file:

   ```
   MTU=`1500`
   ```

   Add the following line to the
   `/etc/dhcp/dhclient.conf` file:

   ```
   request subnet-mask, broadcast-address, time-offset, routers, domain-name, domain-search, domain-name-servers, host-name, nis-domain, nis-servers, ntp-servers;
   ```

   - Other Linux distributions – Consult their specific
     documentation.

3. (Optional) Reboot your instance and verify that the MTU setting is correct.
   The procedure that you use depends on the driver on your instance.

ENA driver
You can change the MTU using Device Manager or the
**Set-NetAdapterAdvancedProperty** command on
your instance.

###### Version 2.1.0 and later

Use the following command to enable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" -RegistryValue 9015
```

Use the following command to disable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" -RegistryValue 1514
```

###### Version 1.5 and earlier

Use the following command to enable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "MTU" -RegistryValue 9001
```

Use the following command to disable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "MTU" -RegistryValue 1500
```

Intel SRIOV 82599 driver
You can change the MTU using Device Manager or the
**Set-NetAdapterAdvancedProperty** command on
your instance.

Use the following command to enable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" -RegistryValue 9014
```

Use the following command to disable jumbo frames.

```
Set-NetAdapterAdvancedProperty -Name "Ethernet" -RegistryKeyword "*JumboPacket" -RegistryValue 1514
```

AWS PV driver
You can change the MTU using the **netsh** command
on your instance. You can't change the MTU using Device
Manager.

Use the following command to enable jumbo frames.

```
netsh interface ipv4 set subinterface "`Ethernet`" mtu=9001
```

Use the following command to disable jumbo frames.

```
netsh interface ipv4 set subinterface "`Ethernet`" mtu=1500
```

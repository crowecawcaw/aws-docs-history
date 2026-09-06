

# Set the time reference on your EC2 instance to use the local Amazon Time Sync Service
<a name="configure-ec2-ntp"></a>

 The Amazon Time Sync Service provides several methods for your Amazon EC2 instance to synchronize to a local time source. First, any Amazon EC2 instance can reach a local time source over the Network Time Protocol (NTP). In addition, the enhanced Amazon Time Sync Service offers higher-accuracy local time sources to [supported Amazon EC2 instances](#ptp-hardware-clock-requirements). Launch your supported instance in a placement group with the `precision-time` strategy to reach a higher-accuracy NTP source. Finally, Linux instances launched in a precision time placement group have access to a PTP Hardware Clock (PHC) device and the ability to retrieve hardware packet timestamps. 

 Any Amazon EC2 instance has access to the local NTP source. You can reach the NTP source over a link-local IP address, which restricts this traffic to within your VPC without the need for specific VPC configuration changes. Your AMI might already have configured your clock synchronization daemon to use the local NTP source by default. This NTP source is available over the following IP addresses: 
+ IPv4: `169.254.169.123`
+ IPv6: `fd00:ec2::123` (Only accessible on [Nitro-based instances](instance-types.md#instance-hypervisor-type).)

 [Supported Amazon EC2 instances](#ptp-hardware-clock-requirements) have access to the enhanced Amazon Time Sync Service. To access the enhanced Amazon Time Sync Service, launch a supported instance in a placement group with the `precision-time` strategy. You do not need to configure your instance to benefit from this improvement if you use the NTP link-local IP addresses. Any operating system can use this enhancement. You can verify that you benefit from the enhanced NTP source by using your NTP client of choice. 

Linux-based AMIs, running on supported instance families, have the additional option to source time from a PHC device. The ENA driver makes this device available. Both enhanced NTP source and PHC device use the same highly accurate time source. Access to the PHC time source is optimized, leading to a more accurate synchronization of your Amazon EC2 instance.

**Considerations**
+ The NTP time source offers a leap smearing view of the UTC timescale, while the PHC does not smear time. For more information, see [Leap seconds](set-time.md#leap-seconds).
+ Only Linux instances have access to the local PTP hardware clock. Windows instances must use NTP to access the enhanced Amazon Time Sync Service.
+ There is a 1024 packet per second (PPS) limit to services that use [link-local](using-instance-addressing.md#link-local-addresses) addresses. This limit includes the aggregate of [Route 53 Resolver DNS Queries](https://docs.aws.amazon.com/vpc/latest/userguide/AmazonDNS-concepts.html#vpc-dns-limits), [Instance Metadata Service (IMDS)](instancedata-data-retrieval.md) requests, Amazon Time Sync Service Network Time Protocol (NTP) requests, and [Windows Licensing Service (for Microsoft Windows based instances)](https://aws.amazon.com/windows/resources/licensing/) requests. 

**Topics**
+ [Access the IPv4 endpoint of the Amazon Time Sync Service](#configure-amazon-time-service-IPv4)
+ [Access the IPv6 endpoint of the Amazon Time Sync Service](#configure-amazon-time-service-IPv6)
+ [Access the enhanced Amazon Time Sync Service](#enhanced-amazon-time-sync-service)
+ [Access the PTP Hardware Clock (PHC)](#connect-to-the-ptp-hardware-clock)

## Access the IPv4 endpoint of the Amazon Time Sync Service
<a name="configure-amazon-time-service-IPv4"></a>

Your AMI might already have configured the Amazon Time Sync Service by default. Otherwise, use the following procedures to configure your instance to use the local Amazon Time Sync Service through the IPv4 endpoint.

For help troubleshooting issues, see [Troubleshoot NTP synchronization issues on Linux instances](https://repost.aws/knowledge-center/linux-troubleshoot-ntp-synchronization) or [Troubleshoot time issues on Windows instances](https://repost.aws/knowledge-center/ec2-windows-time-service).

------
#### [ Amazon Linux ]

AL2023 and recent versions of Amazon Linux 2 are configured to use the Amazon Time Sync Service IPv4 endpoint by default. If you confirm that your instance is already configured, you can skip the following procedure.

**To verify that chrony is configured to use the IPv4 endpoint**  
Run the following command. In the output, the line that starts with `^*` indicates the preferred time source.

```
[ec2-user ~]$ chronyc sources -v | grep -F ^*
```

```
^* 169.254.169.123               3   4   377    13  -4325ns[-9201ns] +/-  401us
```

**To configure chrony to connect to the IPv4 endpoint on older versions of Amazon Linux 2**

1. Connect to your instance and uninstall the NTP service.

   ```
   [ec2-user ~]$ sudo yum erase 'ntp*'
   ```

1. Install the `chrony` package.

   ```
   [ec2-user ~]$ sudo yum install chrony
   ```

1. Open the `/etc/chrony.conf` file using a text editor (such as **vim** or **nano**). Add the following line before any other `server` or `pool` statements that may be present in the file, and save your changes:

   ```
   server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
   ```

1. Restart the `chrony` daemon (`chronyd`).

   ```
   [ec2-user ~]$ sudo service chronyd restart
   ```

   ```
   Starting chronyd:                                          [  OK  ]
   ```
**Note**  
On RHEL and CentOS (up to version 6), the service name is `chrony` instead of `chronyd`.

1. To configure `chronyd` to start at each system boot, use the `chkconfig` command.

   ```
   [ec2-user ~]$ sudo chkconfig chronyd on
   ```

1. Verify that `chrony` is using the `169.254.169.123` IPv4 endpoint to synchronize the time.

   ```
   [ec2-user ~]$ chronyc sources -v | grep -F ^*
   ```

   In the output, `^*` indicates the preferred time source.

   ```
   ^* 169.254.169.123               3   6    17    43    -30us[ -226us] +/-  287us
   ```

1. Verify the time synchronization metrics that are reported by `chrony`.

   ```
   [ec2-user ~]$ chronyc tracking
   ```

   ```
   Reference ID    : A9FEA97B (169.254.169.123)
   Stratum         : 4
   Ref time (UTC)  : Wed May 06 00:39:14 2026
   System time     : 0.000002191 seconds fast of NTP time
   Last offset     : +0.000002164 seconds
   RMS offset      : 0.000082968 seconds
   Frequency       : 3.710 ppm slow
   Residual freq   : +0.002 ppm
   Skew            : 0.504 ppm
   Root delay      : 0.000362541 seconds
   Root dispersion : 0.000225028 seconds
   Update interval : 16.1 seconds
   Leap status     : Normal
   ```

------
#### [ Ubuntu ]

**To configure chrony to connect to the IPv4 endpoint on Ubuntu**

1. Connect to your instance and use `apt` to install the `chrony` package.

   ```
   ubuntu:~$ sudo apt install chrony
   ```
**Note**  
If necessary, update your instance first by running `sudo apt update`.

1. Open the `/etc/chrony/chrony.conf` file using a text editor (such as **vim** or **nano**). Add the following line before any other `server` or `pool` statements that are already present in the file, and save your changes:

   ```
   server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
   ```

1. Restart the `chrony` service.

   ```
   ubuntu:~$ sudo /etc/init.d/chrony restart
   ```

   ```
   Restarting chrony (via systemctl): chrony.service.
   ```

1. Verify that `chrony` is using the `169.254.169.123` IPv4 endpoint to synchronize the time.

   ```
   ubuntu:~$ chronyc sources -v | grep -F ^*
   ```

   In the output, the line starting with `^*` indicates the preferred time source.

   ```
   ^* 169.254.169.123               3   6    17    12    +15us[  +57us] +/-  320us
   ```

1. Verify the time synchronization metrics that are reported by `chrony`.

   ```
   ubuntu:~$ chronyc tracking
   ```

   ```
   Reference ID    : A9FEA97B (169.254.169.123)
   Stratum         : 4
   Ref time (UTC)  : Wed May 06 00:39:14 2026
   System time     : 0.000002191 seconds fast of NTP time
   Last offset     : +0.000002164 seconds
   RMS offset      : 0.000082968 seconds
   Frequency       : 3.710 ppm slow
   Residual freq   : +0.002 ppm
   Skew            : 0.504 ppm
   Root delay      : 0.000362541 seconds
   Root dispersion : 0.000225028 seconds
   Update interval : 16.1 seconds
   Leap status     : Normal
   ```

------
#### [ SUSE Linux ]

Starting with SUSE Linux Enterprise Server 15, `chrony` is the default implementation of NTP.

**To configure chrony to connect to IPv4 endpoint on SUSE Linux**

1. Open the `/etc/chrony.conf` file using a text editor (such as **vim** or **nano**).

1. Verify that the file contains the following line:

   ```
   server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
   ```

   If this line is not present, add it.

1. Comment out any other server or pool lines.

1. Open YaST and enable the chrony service.

------
#### [ Windows ]

Starting with the August 2018 release, Windows AMIs use the Amazon Time Sync Service by default. No further configuration is required for instances launched from these AMIs and you can skip the following procedures.

If you're using an AMI that doesn't have the Amazon Time Sync Service configured by default, first verify your current NTP configuration. If your instance is already using the IPv4 endpoint of the Amazon Time Sync Service, no further configuration is required. If your instance is not using the Amazon Time Sync Service, then complete the procedure to change the NTP server to use the Amazon Time Sync Service.

**To verify the NTP configuration**

1. From your instance, open a Command Prompt window.

1. Get the current NTP configuration by typing the following command:

   ```
   w32tm /query /configuration
   ```

   This command returns the current configuration settings for the Windows instance and will show if you're connected to the Amazon Time Sync Service.

1. (Optional) Get the status of the current configuration by typing the following command:

   ```
   w32tm /query /status
   ```

   This command returns information such as the last time the instance synced with the NTP server and the poll interval.

**To change the NTP server to use the Amazon Time Sync Service**

1. From the Command Prompt window, run the following command:

   ```
   w32tm /config /manualpeerlist:169.254.169.123 /syncfromflags:manual /update
   ```

1. Verify your new settings by using the following command:

   ```
   w32tm /query /configuration
   ```

   In the output that's returned, verify that `NtpServer` displays the `169.254.169.123` IPv4 endpoint.

**Default NTP settings for Amazon Windows AMIs**

Amazon Machine Images (AMIs) generally adhere to the out-of-the-box defaults except in cases where changes are required to function on EC2 infrastructure. The following settings have been determined to work well in a virtual environment, as well as to keep any clock drift to within one second of accuracy: 
+ **Update Interval** – Governs how frequently the time service will adjust system time towards accuracy. AWS configures the update interval to occur once every two minutes.
+ **NTP Server** – Starting with the August 2018 release, AMIs use the Amazon Time Sync Service by default. This time service is accessible from any AWS Region at the 169.254.169.123 IPv4 endpoint. Additionally, the 0x9 flag indicates that the time service is acting as a client, and to use `SpecialPollInterval` to determine how frequently to check in with the configured time server.
+ **Type** – "NTP" means that the service acts as a standalone NTP client instead of acting as part of a domain.
+ **Enabled and InputProvider** – The time service is enabled and provides time to the operating system.
+ **Special Poll Interval** – Checks against the configured NTP Server every 900 seconds (15 minutes).
**Note**  
For Windows Server 2025 AMIs, the `SpecialPollInterval` value is 1024 seconds instead of 900 seconds.


| Registry path | Key name | Data | 
| --- | --- | --- | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\Config | UpdateInterval | 120 | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\Parameters | NtpServer | 169.254.169.123,0x9 | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\Parameters | Type | NTP | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\TimeProviders\\NtpClient | Enabled | 1 | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\TimeProviders\\NtpClient | InputProvider | 1 | 
| HKLM:\\System\\CurrentControlSet\\services\\w32time\\TimeProviders\\NtpClient | SpecialPollInterval | 900 (Windows Server 2016, 2019, and 2022) or 1024 (Windows Server 2025) | 

------

## Access the IPv6 endpoint of the Amazon Time Sync Service
<a name="configure-amazon-time-service-IPv6"></a>

This section explains how the steps described in [Access the IPv4 endpoint of the Amazon Time Sync Service](#configure-amazon-time-service-IPv4) differ if you are configuring your instance to use the local Amazon Time Sync Service through the IPv6 endpoint. It doesn't explain the entire Amazon Time Sync Service configuration process.

The IPv6 endpoint is only accessible on [Nitro-based instances](instance-types.md#instance-hypervisor-type).

We don't recommend using both the IPv4 and IPv6 endpoint entries together. The IPv4 and IPv6 NTP packets come from the same local server for your instance. Configuring both IPv4 and IPv6 endpoints is unnecessary and will not improve the accuracy of the time on your instance.

------
#### [ Linux ]

Depending on the Linux distribution you're using, when you reach the step to edit the `chrony.conf` file, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (`fd00:ec2::123`) rather than the IPv4 endpoint (`169.254.169.123`):

```
server fd00:ec2::123 prefer iburst minpoll 4 maxpoll 4
```

Save the file and verify that chrony is using the `fd00:ec2::123` IPv6 endpoint to synchronize time: 

```
[ec2-user ~]$ chronyc sources -v
```

In the output, if you see the `fd00:ec2::123` IPv6 endpoint, the configuration is complete.

------
#### [ Windows ]

When you reach the step to change the NTP server to use the Amazon Time Sync Service, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (`fd00:ec2::123`) rather than the IPv4 endpoint (`169.254.169.123`):

```
w32tm /config /manualpeerlist:fd00:ec2::123 /syncfromflags:manual /update
```

Verify that your new settings are using the `fd00:ec2::123` IPv6 endpoint to synchronize time:

```
w32tm /query /configuration
```

In the output, verify that `NtpServer` displays the `fd00:ec2::123` IPv6 endpoint.

------

## Access the enhanced Amazon Time Sync Service
<a name="enhanced-amazon-time-sync-service"></a>

 The enhanced Amazon Time Sync Service offers higher accuracy local time sources to supported Amazon EC2 instances. Instances launched in a placement group with a `precision-time` strategy can access these local sources. We recommend precision time placement groups for applications that require more accurate time from either the link-local NTP source, or a PTP Hardware Clock (PHC) device on a Linux instance. When you launch instances into a precision time placement group, AWS places them on supported hardware with direct access to high-precision time sources in AWS infrastructure. 

**Key benefits**
+  **Improved NTP source by default** — Your instance has immediate access to an enhanced local NTP time source, if you use the NTP link-local IP addresses as described in the preceding section. 
+  **Microsecond-accurate clock synchronization** — Configure your Amazon EC2 Linux instance to use a PTP Hardware Clock device and achieve microsecond-accurate clock synchronization. 
+  **Simplified deployment** — Single placement strategy ensures all instances have precision time capabilities. 
+  **Hardware packet timestamping** — Access low-level packet timestamps for network measurements. 
+  **No additional cost** — Precision time placement groups are available at no extra charge. 

**Rules and limitations**
+  Precision time placement groups are available in all AWS Commercial Regions. 
+  Precision time placement groups support the following Gen7 and later Amazon EC2 instance families: 
  +  **General purpose**: M7a, M7g, M7gd, M7i, M7i-flex, M8a, M8g 
  +  **Compute optimized**: C7a, C7gd, C7i, C7i-flex, C8g, C8gd 
  +  **Memory optimized**: R7a, R7g, R7i, R8g, X8g 
  +  **Storage optimized**: I8g, I8ge 
+  If you start or launch an instance in a precision time placement group and there is insufficient hardware to give access to the enhanced Amazon Time Sync Service, the request fails. 
+  If you stop an instance in a precision time placement group and then start it again, it still runs in the placement group. However, the start might fail if there is insufficient hardware to give access to the enhanced Amazon Time Sync Service. 
+  Amazon EC2 continuously adds hardware that supports the enhanced Amazon Time Sync Service. If your request fails due to insufficient capacity, try again later or try a different Availability Zone. For more information, see [Troubleshoot Amazon EC2 instance launch issues](troubleshooting-launch.md). 
+ Rules and limitations of placement groups apply. For more information, see [Placement groups for your Amazon EC2 instances](placement-groups.md) 

### Create a precision time placement group
<a name="create-precision-time-placement-group"></a>

You can create a precision time placement group using the AWS CLI, AWS Management Console, or AWS SDKs, by specifying the `precision-time` strategy.

**Using AWS CLI**  
Run the following command:

```
aws ec2 create-placement-group \
    --group-name {{my-precision-time-pg}} \
    --strategy precision-time
```

The command returns a placement group ARN that you use when creating capacity reservations, and a group name or group ID that you use when launching instances and linking placement groups.

### Launch an instance
<a name="launch-instance-precision-time"></a>

After you create a precision time placement group, specify it when launching instances to access the enhanced Amazon Time Sync Service:

```
aws ec2 run-instances \
    --image-id {{ami-0abcdef1234567890}} \
    --instance-type {{r7g.2xlarge}} \
    --placement GroupId={{pg-0aaa1111111111111}}
```

### Verify access to the enhanced Amazon Time Sync Service
<a name="verify-enhanced-local-ntp-time-source"></a>

After you launch your instance in a precision time placement group, you benefit from an enhanced NTP time source.

For example, if you use the chronyd daemon on your instance, you can verify that the NTP time source is now referred to as a Stratum 1 and has improved clock accuracy metrics:

```
[ec2-user ~]$ chronyc sources
```

```
MS Name/IP address         Stratum Poll Reach LastRx Last sample
===============================================================================
^* 169.254.169.123               1   4   377     3  +3477ns[+4689ns] +/-   91us
```

Verify the time synchronization metrics that are reported by `chrony`.

```
[ec2-user ~]$ chronyc tracking
```

```
Reference ID    : A9FEA97B (169.254.169.123)
Stratum         : 2
Ref time (UTC)  : Wed May 06 01:33:43 2026
System time     : 0.000000276 seconds fast of NTP time
Last offset     : +0.000000331 seconds
RMS offset      : 0.000001929 seconds
Frequency       : 2.870 ppm fast
Residual freq   : +0.000 ppm
Skew            : 0.031 ppm
Root delay      : 0.000107584 seconds
Root dispersion : 0.000036476 seconds
Update interval : 16.2 seconds
Leap status     : Normal
```

## Access the PTP Hardware Clock (PHC)
<a name="connect-to-the-ptp-hardware-clock"></a>

 The PTP Hardware Clock (PHC) is part of the [AWS Nitro System](https://docs.aws.amazon.com/ec2/latest/instancetypes/ec2-nitro-instances.html). It is directly accessible on [supported bare metal and virtualized Amazon EC2 instances](#ptp-hardware-clock-requirements) launched in a precision time placement group. The PHC device is currently accessible on Linux instances only. The following sections describe how to set up and verify the PHC device on your Linux instance. 

### Requirements
<a name="ptp-hardware-clock-requirements"></a>
+  ENA driver version 2.10.0 or later installed on a supported operating system. 
+  An Amazon EC2 instance running Linux. For more information about supported operating systems, see the driver [prerequisites](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#prerequisites) on *GitHub*. 
+  An Amazon EC2 instance launched in a precision time placement group (see [Access the enhanced Amazon Time Sync Service](#enhanced-amazon-time-sync-service)). 

**Note**  
 The enhanced Amazon Time Sync Service and the PHC device remain accessible without a precision time placement group in the following regions and for the specific instance families. For the best experience, we recommend launching Amazon EC2 instances in precision placement groups instead.   
Legacy access supported AWS Regions: US East (N. Virginia), US East (Ohio), Asia Pacific (Malaysia), Asia Pacific (Thailand), Asia Pacific (Tokyo), and Europe (Stockholm)
Legacy access supported Local Zones: US East (New York City)
Legacy access supported instance families:  
**General purpose: **M7a, M7g, M7i
**Memory optimized: **R7a, R7g, R7i
**Storage optimized: **I8g, I8ge

### Compile and enable the ENA driver with PHC support
<a name="compile-enable-ena-driver-phc"></a>

 Always review the most recent instructions from the latest Elastic Network Adapter (ENA) driver version in the [ENA driver documentation](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#ptp-hardware-clock-phc) on *GitHub* for information specific to your operating system. The following is an overview of steps for Amazon Linux. 

Before you begin, ensure your instance meets the [Requirements](#ptp-hardware-clock-requirements).

**To compile and enable the ENA driver with PHC support**

1. Install prerequisites.

   ```
   [ec2-user ~]$ sudo yum update
   [ec2-user ~]$ sudo yum install kernel-devel-$(uname -r) git
   [ec2-user ~]$ sudo reboot
   ```

1. Load the required ptp module.

   ```
   [ec2-user ~]$ sudo modprobe ptp
   ```

1. Retrieve the latest ENA driver version (version 2.10.0 or later).

   ```
   [ec2-user ~]$ git clone https://github.com/amzn/amzn-drivers.git /tmp/amzn-drivers
   ```

1. Build the ENA driver `ena.ko` with PHC support.

   ```
   [ec2-user ~]$ cd /tmp/amzn-drivers/kernel/linux/ena
   [ec2-user ~]$ ENA_PHC_INCLUDE=1 make
   ```

1. Reload the ENA driver and enable the PHC device.

   ```
   [ec2-user ~]$ sudo rmmod ena && sudo insmod ena.ko phc_enable=1
   ```

1. Validate the loaded ENA driver has PHC support.

   ```
   [ec2-user ~]$ modinfo ena | grep -E "phc_enable"
   ```

   ```
   parm:           phc_enable:Enable PHC.
   ```

1. Validate the PHC support is enabled with the ENA driver.

   ```
   [ec2-user ~]$ cat /sys/module/ena/parameters/phc_enable
   ```

   ```
   1
   ```

For instructions to install the driver and activate the phc\_enable option upon reboot, see the [ENA driver README](https://github.com/amzn/amzn-drivers/blob/master/kernel/linux/ena/README.rst) on *GitHub*.

### Verify the PTP device configuration
<a name="verify-ptp-device-configuration"></a>

Verify that the ENA PTP hardware clock device shows up on your instance.

```
[ec2-user ~]$ for file in /sys/class/ptp/*; do echo -n "$file: "; cat "$file/clock_name"; done
```

Expected output

```
/sys/class/ptp/ptp{{<index>}}: ena-ptp-{{<PCI slot>}}
```

Where:
+ `{{index}}` is the kernel-registered PTP hardware clock index.
+ `{{PCI slot}}` is the ENA ethernet controller PCI slot. This is the same slot as shown in `lspci | grep ENA`.

Example output

```
/sys/class/ptp/{{ptp0}}: ena-ptp-{{05}}
```

If `ena-ptp-{{<PCI slot>}}` is not in the output, the ENA driver was not correctly installed. Review the steps in [Compile and enable the ENA driver with PHC support](#compile-enable-ena-driver-phc).

### Configure PTP symlink
<a name="configure-ptp-symlink"></a>

PTP devices are typically named `/dev/ptp0`, `/dev/ptp1`, and so on, with their index depending on the hardware initialization order. Creating a symlink ensures that applications like chrony consistently reference the correct device, regardless of index changes.

The latest Amazon Linux 2023 AMIs include a `udev` rule that creates the `/dev/ptp_ena` symlink, pointing to the correct `/dev/ptp` entry associated with the ENA host.

First, check if the symlink is present by running the following command.

```
[ec2-user ~]$ ls -l /dev/ptp*
```

Example output

```
crw------- 1 root root 245, 0 Jan 31 2025 /dev/ptp0
lrwxrwxrwx 1 root root      4 Jan 31 2025 /dev/ptp_ena -> ptp0
```

Where:
+ `/dev/ptp{{<index>}}` is the path to the PTP device.
+ `/dev/ptp_ena` is the constant symlink, which points to the same PTP device.

If the `/dev/ptp_ena` symlink is present, skip to [Configure the chronyd daemon to use the PHC device](#configure-chronyd-phc). If it's missing, do the following:

**To create the PTP symlink**

1. Add the following `udev` rule.

   ```
   [ec2-user ~]$ echo "SUBSYSTEM==\"ptp\", ATTR{clock_name}==\"ena-ptp-*\", SYMLINK += \"ptp_ena\"" | sudo tee -a /etc/udev/rules.d/53-ec2-network-interfaces.rules
   ```

1. Reload the `udev` rule, either by rebooting the instance, or by running the following command.

   ```
   [ec2-user ~]$ sudo udevadm control --reload-rules && sudo udevadm trigger
   ```

### Configure the chronyd daemon to use the PHC device
<a name="configure-chronyd-phc"></a>

The chronyd clock synchronization daemon must be configured to use the PHC device as an additional time source, using the `/dev/ptp_ena` symlink to identify the device.

**To configure the chronyd daemon to use the PHC device**

1. Edit `/etc/chrony.conf` using a text editor and add the following line:

   ```
   refclock PHC /dev/ptp_ena poll 0 delay 0.000010 prefer
   ```

1. Restart chrony.

   ```
   [ec2-user ~]$ sudo systemctl restart chronyd
   ```

1. Verify that chrony is using the PTP hardware clock. The PHC0 device must be the preferred time source with a Stratum 0 value. The local NTP time source (if configured) must have a Stratum 1 value.

   ```
   [ec2-user ~]$ chronyc sources
   ```

   ```
   MS Name/IP address         Stratum Poll Reach LastRx Last sample
   ===============================================================================
   #* PHC0                          0   0   377     0   +184ns[ +198ns] +/- 5032ns
   ^- 169.254.169.123               1   4   377     8    -18us[  -18us] +/-  115us
   ```

### Verify hardware packet timestamping
<a name="verify-hardware-packet-timestamping"></a>

The ENA driver loaded with the PHC support provides access to hardware packet timestamping. You can verify support for this functionality by using the `ethtool -T {{interface}}` command.

For more information about using hardware packet timestamping, see the [packet timestamping Linux documentation](https://www.kernel.org/doc/html/latest/networking/timestamping.html).

```
[ec2-user ~]$ sudo ethtool -T {{ens5}}
```

```
Time stamping parameters for ens5:
Capabilities:
        software-transmit
        hardware-receive
        software-receive
        software-system-clock
PTP Hardware Clock: 0
Hardware Transmit Timestamp Modes: none
Hardware Receive Filter Modes:
        none
        all
```

If the output shows `hardware-receive` in the Capabilities list, hardware packet timestamping is available on your instance.
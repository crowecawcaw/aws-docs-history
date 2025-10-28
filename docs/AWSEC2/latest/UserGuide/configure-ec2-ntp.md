# Set the time reference on your EC2 instance to use

the local Amazon Time Sync Service

The local Amazon Time Sync Service either uses the Network Time Protocol (NTP), or provides a local
Precision Time Protocol (PTP) hardware clock on [supported instances](#ptp-hardware-clock-requirements "#ptp-hardware-clock-requirements"). The PTP
hardware clock supports either an NTP connection (Linux and Windows instances), or a
direct PTP connection (Linux instances only). The NTP and direct PTP connections use the
same highly accurate time source, but the direct PTP connection is more accurate than
the NTP connection. The NTP connection to the Amazon Time Sync Service supports leap smearing while the
PTP connection to the PTP hardware clock does not smear time. For more information, see
[Leap seconds](set-time.md#leap-seconds "set-time.md#leap-seconds").

Your instances can access the local Amazon Time Sync Service as follows:

- Through NTP at the following IP address endpoints:
  - IPv4: `169.254.169.123`
  - IPv6: `fd00:ec2::123` (Only accessible on [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").)

- (Linux only) Through a direct PTP connection to connect to a local PTP
  hardware clock:

      + `PHC0`

  Amazon Linux AMIs, Windows AMIs, and most partner AMIs configure your instance to use the NTP
  IPv4 endpoint by default. This is the recommended setting for most customer workloads.
  No further configuration is required for instances launched from these AMIs unless you
  want to use the IPv6 endpoint or connect directly to the PTP hardware clock.

NTP and PTP connections do not require any VPC configuration changes, and your
instance does not require access to the internet.

###### Considerations

- There is a 1024 packet per second (PPS) limit to services that use [link-local](using-instance-addressing.md#link-local-addresses "using-instance-addressing.md#link-local-addresses") addresses. This limit includes the aggregate of [Route 53 Resolver DNS Queries](../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-limits "../../../vpc/latest/userguide/AmazonDNS-concepts.md#vpc-dns-limits"), [Instance Metadata Service (IMDS)](instancedata-data-retrieval.md "instancedata-data-retrieval.md") requests, Amazon Time Service Network Time Protocol (NTP) requests, and [Windows Licensing Service (for Microsoft Windows based instances)](https://aws.amazon.com/windows/resources/licensing/ "https://aws.amazon.com/windows/resources/licensing/") requests.
- Only Linux instances can use a _direct PTP
  connection_ to connect to the local PTP hardware clock. Windows
  instances use NTP to connect to the local PTP hardware clock.

###### Contents

- [Connect to the IPv4 endpoint of the Amazon Time Sync Service](#configure-amazon-time-service-IPv4 "#configure-amazon-time-service-IPv4")
- [Connect to the IPv6 endpoint of
  the Amazon Time Sync Service](#configure-amazon-time-service-IPv6 "#configure-amazon-time-service-IPv6")
- [Connect to the PTP hardware clock](#connect-to-the-ptp-hardware-clock "#connect-to-the-ptp-hardware-clock")

## Connect to the IPv4 endpoint of the Amazon Time Sync Service

Your AMI might already have configured the Amazon Time Sync Service by default. Otherwise, use
the following procedures to configure your instance to use the local Amazon Time Sync Service
through the IPv4 endpoint.

For help troubleshooting issues, see [Troubleshoot NTP synchronization issues on Linux instances](https://repost.aws/knowledge-center/linux-troubleshoot-ntp-synchronization "https://repost.aws/knowledge-center/linux-troubleshoot-ntp-synchronization") or
[Troubleshoot time issues on Windows instances](https://repost.aws/knowledge-center/ec2-windows-time-service "https://repost.aws/knowledge-center/ec2-windows-time-service").

Amazon Linux
AL2023 and recent versions of Amazon Linux 2 are configured to use the
Amazon Time Sync Service IPv4 endpoint by default. If you confirm that your instance
is already configured, you can skip the following procedure.

###### To verify that chrony is configured to use the IPv4 endpoint

Run the following command. In the output, the line that starts with
`^*` indicates the preferred time source.

```
`chronyc sources -v | grep -F ^*`
^* 169.254.169.123               3   4   377    14    +12us[+9653ns] +/-  290us
```

###### To configure chrony to connect to the IPv4 endpoint on older versions of Amazon Linux 2

1. Connect to your instance and uninstall the NTP
   service.

```
`[ec2-user ~]$` `sudo yum erase 'ntp*'`
```

2. Install the `chrony` package.

```
`[ec2-user ~]$` `sudo yum install chrony`
```

3. Open the `/etc/chrony.conf` file using a
   text editor (such as **vim** or
   **nano**). Add the following line before any other `server` or `pool`
   statements that may be present in the file, and
   save your changes:

```
server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
```

4. Restart the `chrony` daemon
   (`chronyd`).

```
`[ec2-user ~]$` `sudo service chronyd restart`
```

```
Starting chronyd:                                          [  OK  ]
```

###### Note

On
RHEL
and CentOS (up to version 6), the
service name is `chrony` instead of
`chronyd`. 5. To configure `chronyd` to start at each
system boot, use the `chkconfig`
command.

```
`[ec2-user ~]$` `sudo chkconfig chronyd on`
```

6. Verify that `chrony` is using the
   `169.254.169.123` IPv4 endpoint to
   synchronize the time.

```
`[ec2-user ~]$` `chronyc sources -v | grep -F ^*`
```

In the output, `^*` indicates the preferred time source.

```
^* 169.254.169.123               3   6    17    43    -30us[ -226us] +/-  287us
```

7. Verify the time synchronization metrics that are
   reported by `chrony`.

```
`[ec2-user ~]$` `chronyc tracking`
```

```
Reference ID    : A9FEA97B (169.254.169.123)
Stratum         : 4
Ref time (UTC)  : Wed Nov 22 13:18:34 2017
System time     : 0.000000626 seconds slow of NTP time
Last offset     : +0.002852759 seconds
RMS offset      : 0.002852759 seconds
Frequency       : 1.187 ppm fast
Residual freq   : +0.020 ppm
Skew            : 24.388 ppm
Root delay      : 0.000504752 seconds
Root dispersion : 0.001112565 seconds
Update interval : 64.4 seconds
Leap status     : Normal
```

Ubuntu

###### To configure chrony to connect to the IPv4 endpoint on Ubuntu

1. Connect to your instance and use `apt` to
   install the `chrony` package.

```
`ubuntu:~$` `sudo apt install chrony`
```

###### Note

If necessary, update your instance first by
running `sudo apt update`. 2. Open the `/etc/chrony/chrony.conf` file
using a text editor (such as **vim** or
**nano**). Add the following line
before any other `server` or
`pool` statements that are already
present in the file, and save your changes:

```
server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
```

3. Restart the `chrony` service.

```
`ubuntu:~$` `sudo /etc/init.d/chrony restart`
```

```
Restarting chrony (via systemctl): chrony.service.
```

4. Verify that `chrony` is using the
   `169.254.169.123` IPv4 endpoint to
   synchronize the time.

```
`ubuntu:~$` `chronyc sources -v | grep -F ^*`
```

In the output, the line starting with `^*` indicates the preferred time source.

```
^* 169.254.169.123               3   6    17    12    +15us[  +57us] +/-  320us
```

5. Verify the time synchronization metrics that are
   reported by `chrony`.

```
`ubuntu:~$` `chronyc tracking`
```

```
Reference ID    : 169.254.169.123 (169.254.169.123)
Stratum         : 4
Ref time (UTC)  : Wed Nov 29 07:41:57 2017
System time     : 0.000000011 seconds slow of NTP time
Last offset     : +0.000041659 seconds
RMS offset      : 0.000041659 seconds
Frequency       : 10.141 ppm slow
Residual freq   : +7.557 ppm
Skew            : 2.329 ppm
Root delay      : 0.000544 seconds
Root dispersion : 0.000631 seconds
Update interval : 2.0 seconds
Leap status     : Normal
```

SUSE Linux
Starting with SUSE Linux Enterprise Server 15, `chrony`
is the default implementation of NTP.

###### To configure chrony to connect to IPv4 endpoint on SUSE Linux

1. Open the `/etc/chrony.conf` file using a
   text editor (such as **vim** or
   **nano**).
2. Verify that the file contains the following
   line:

```
server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
```

If this line is not present, add it. 3. Comment out any other server or pool lines. 4. Open YaST and enable the chrony service.

Windows
Starting with the August 2018 release, Windows AMIs use the Amazon Time Sync Service by
default. No further configuration is required for instances launched from
these AMIs and you can skip the following procedures.

If you're using an AMI that doesn't have the Amazon Time Sync Service configured by default,
first verify your current NTP configuration. If your instance is already
using the IPv4 endpoint of the Amazon Time Sync Service, no further configuration is required.
If your instance is not using the Amazon Time Sync Service, then complete the procedure to
change the NTP server to use the Amazon Time Sync Service.

###### To verify the NTP configuration

1. From your instance, open a Command Prompt window.
2. Get the current NTP configuration by typing the following
   command:

```
w32tm /query /configuration
```

This command returns the current configuration settings for the
Windows instance and will show if you're connected to the
Amazon Time Sync Service. 3. (Optional) Get the status of the current configuration by typing
the following command:

```
w32tm /query /status
```

This command returns information such as the last time the
instance synced with the NTP server and the poll interval.

###### To change the NTP server to use the Amazon Time Sync Service

1. From the Command Prompt window, run the following command:

```
w32tm /config /manualpeerlist:169.254.169.123 /syncfromflags:manual /update
```

2. Verify your new settings by using the following command:

```
w32tm /query /configuration
```

In the output that's returned, verify that `NtpServer`
displays the `169.254.169.123` IPv4 endpoint.

###### Default NTP settings for Amazon Windows AMIs

Amazon Machine Images (AMIs) generally adhere to the out-of-the-box
defaults except in cases where changes are required to function on EC2
infrastructure. The following settings have been determined to work well
in a virtual environment, as well as to keep any clock drift to within
one second of accuracy:

- Update Interval –
  Governs how frequently the time service will adjust system time
  towards accuracy. AWS configures the update interval to occur
  once every two minutes.
- NTP Server – Starting
  with the August 2018 release, AMIs use the Amazon Time Sync Service by default.
  This time service is accessible from any AWS Region at the
  169.254.169.123 IPv4 endpoint. Additionally, the 0x9 flag
  indicates that the time service is acting as a client, and to
  use `SpecialPollInterval` to determine how frequently
  to check in with the configured time server.
- Type – "NTP" means that
  the service acts as a standalone NTP client instead of acting as
  part of a domain.
- Enabled and InputProvider
  – The time service is enabled and provides time to the
  operating system.
- Special Poll Interval –
  Checks against the configured NTP Server every 900 seconds (15
  minutes).

| Registry path                                                           | Key name            | Data                |
| ----------------------------------------------------------------------- | ------------------- | ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HKLM:\System\CurrentControlSet\services\w32time\Config                  | UpdateInterval      | 120                 |
| HKLM:\System\CurrentControlSet\services\w32time\Parameters              | NtpServer           | 169.254.169.123,0x9 |
| HKLM:\System\CurrentControlSet\services\w32time\Parameters              | Type                | NTP                 |
| HKLM:\System\CurrentControlSet\services\w32time\TimeProviders\NtpClient | Enabled             | 1                   |
| HKLM:\System\CurrentControlSet\services\w32time\TimeProviders\NtpClient | InputProvider       | 1                   |
| HKLM:\System\CurrentControlSet\services\w32time\TimeProviders\NtpClient | SpecialPollInterval | 900                 | ## Connect to the IPv6 endpoint of the Amazon Time Sync Service This section explains how the steps described in [Connect to the IPv4 endpoint of the Amazon Time Sync Service](#configure-amazon-time-service-IPv4 "#configure-amazon-time-service-IPv4") differ if you are configuring your instance to use the local Amazon Time Sync Service through the IPv6 endpoint. It doesn't explain the entire Amazon Time Sync Service configuration process. The IPv6 endpoint is only accessible on [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"). We don't recommend using both the IPv4 and IPv6 endpoint entries together. The IPv4 and IPv6 NTP packets come from the same local server for your instance. Configuring both IPv4 and IPv6 endpoints is unnecessary and will not improve the accuracy of the time on your instance. Linux Depending on the Linux distribution you're using, when you reach the step to edit the `chrony.conf` file, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (`fd00:ec2::123`) rather than the IPv4 endpoint (`169.254.169.123`): `server fd00:ec2::123 prefer iburst minpoll 4 maxpoll 4` Save the file and verify that chrony is using the `fd00:ec2::123` IPv6 endpoint to synchronize time: `` `[ec2-user ~]$` `chronyc sources -v` `` In the output, if you see the `fd00:ec2::123` IPv6 endpoint, the configuration is complete. Windows When you reach the step to change the NTP server to use the Amazon Time Sync Service, you'll be using the IPv6 endpoint of the Amazon Time Sync Service (`fd00:ec2::123`) rather than the IPv4 endpoint (`169.254.169.123`): `w32tm /config /manualpeerlist:fd00:ec2::123 /syncfromflags:manual /update` Verify that your new settings are using the `fd00:ec2::123` IPv6 endpoint to synchronize time: `w32tm /query /configuration` In the output, verify that `NtpServer` displays the `fd00:ec2::123` IPv6 endpoint. ## Connect to the PTP hardware clock The PTP hardware clock is part of the [AWS Nitro System](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md"), so it is directly accessible on [supported bare metal and virtualized EC2 instances](#ptp-hardware-clock-requirements "#ptp-hardware-clock-requirements") without using any customer resources. The NTP endpoints for the PTP hardware clock are the same as those for the regular Amazon Time Sync Service. If your instance has a PTP hardware clock and you configured the NTP connection (to either the IPv4 or IPv6 endpoint), your instance time is automatically sourced from the PTP hardware clock over NTP. For Linux instances, you can configure a _direct_ PTP connection, which will give you more accurate time than the NTP connection. Windows instances only support an NTP connection to the PTP hardware clock. ### Requirements The PTP hardware clock is available on an instance when the following requirements are met: <br>• Supported AWS Regions: US East (N. Virginia), US East (Ohio), Asia Pacific (Malaysia), Asia Pacific (Thailand), Asia Pacific (Tokyo), and Europe (Stockholm) <br>• Supported Local Zones: US East (New York City) <br>• Supported instance families: + **General purpose:** M7a, M7g, M7i + **Memory optimized:** R7a, R7g, R7i + **Storage optimized:** I8g, I8ge <br>• (Linux only) ENA driver version 2.10.0 or later installed on a supported operating system. For more information about supported operating systems, see the driver [prerequisites](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#prerequisites "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#prerequisites") on _GitHub_. This section describes how to configure your Linux instance to use the local Amazon Time Sync Service through the PTP hardware clock using a direct PTP connection. It requires adding a server entry for the PTP hardware clock in the `chrony` configuration file. ###### To configure a direct PTP connection to the PTP hardware clock (Linux instances only) 1. **Install prerequisites** Connect to your Linux instance and do the following: 1. Install the Linux kernel driver for Elastic Network Adapter (ENA) version 2.10.0 or later. 2. Enable the PTP hardware clock.For the installation instructions, see [Linux kernel driver for Elastic Network Adapter (ENA) family](https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#linux-kernel-driver-for-elastic-network-adapter-ena-family "https://github.com/amzn/amzn-drivers/tree/master/kernel/linux/ena#linux-kernel-driver-for-elastic-network-adapter-ena-family") on _GitHub_. 2. **Verify ENA PTP device** Verify that the ENA PTP hardware clock device shows up on your instance. `` `[ec2-user ~]$` `for file in /sys/class/ptp/*; do echo -n "$file: "; cat "$file/clock_name"; done` `` Expected output `` /sys/class/ptp/ptp`<index>`: ena-ptp-`<PCI slot>` `` Where: <br>• `index` is the kernel-registered PTP hardware clock index. <br>• `PCI slot` is the ENA ethernet controller PCI slot. This is the same slot as shown in `lspci | grep ENA`. Example output ``` /sys/class/ptp/`ptp0`: ena-ptp-`05` ``` If `ena-ptp-`<PCI slot>`` is not in the output, the ENA driver was not correctly installed. Review step 1 in this procedure for installing the driver. 3. **Configure PTP symlink** PTP devices are typically named `/dev/ptp0`, `/dev/ptp1`, and so on, with their index depending on the hardware initialization order. Creating a symlink ensures that applications like chrony consistently reference the correct device, regardless of index changes. The latest Amazon Linux 2023 AMIs include a `udev`rule that creates the`/dev/ptp_ena`symlink, pointing to the correct`/dev/ptp` entry associated with the ENA host. First check if the symlink is present by running the following command. ``` `[ec2-user ~]$` `ls -l /dev/ptp*` ``` Example output ``` crw------- 1 root root 245, 0 Jan 31 2025 /dev/ptp0 lrwxrwxrwx 1 root root      4 Jan 31 2025 /dev/ptp_ena -> ptp0 ``` Where: <br>• `/dev/ptp`<index>`` is the path to the PTP device. <br>• `/dev/ptp_ena` is the constant symlink, which points to the same PTP device. If the `/dev/ptp_ena` symlink is present, skip to Step 4 in this procedure. If it's missing, do the following: 1. Add the following `udev` rule. ``` `[ec2-user ~]$` `echo "SUBSYSTEM==\"ptp\", ATTR{clock_name}==\"ena-ptp-\*\", SYMLINK += \"ptp_ena\"" | sudo tee -a /etc/udev/rules.d/53-ec2-network-interfaces.rules` ``` 2. Reload the `udev` rule, either by rebooting the instance, or by running the following command. ``` `[ec2-user ~]$` `sudo udevadm control --reload-rules && udevadm trigger` ``` 4. **Configure chrony** chrony must be configured to use the `/dev/ptp_ena` symlink instead of directly referencing /`dev/ptp`<index>``. 1. Edit `/etc/chrony.conf` using a text editor and add the following line anywhere in the file. ``` refclock PHC /dev/ptp_ena poll 0 delay 0.000010 prefer ``` 2. Restart chrony. ``` `[ec2-user ~]$` `sudo systemctl restart chronyd` ``` 5. **Verify chrony configuration** Verify that chrony is using the PTP hardware clock to synchronize the time on this instance. ``` `[ec2-user ~]$` `chronyc sources` ``` Expected output ``` MS Name/IP address         Stratum Poll Reach LastRx Last sample =============================================================================== #* PHC0                          0   0    377    1   +2ns[ +1ns] +/-   5031ns ``` In the output that's returned, `\*`indicates the preferred time source.`PHC0` corresponds to the PTP hardware clock. You might need to wait a few seconds after restarting chrony for the asterisk to appear. |

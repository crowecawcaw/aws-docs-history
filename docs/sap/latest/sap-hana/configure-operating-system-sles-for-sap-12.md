# Configure SLES 12/15 for SAP

###### Important

In the following steps, you need to update several configuration files. We recommend taking a backup of the files before you modify them. This will help you to revert to the previous configuration if needed.

1. After your instance is up and running, connect to the instance by using Secure Shell (SSH) and the key pair that you used to launch the instance.

###### Note

Depending on your network and security settings, you might have to first connect by using SSH to a bastion host before accessing your SAP HANA instance, or you might have to add IP addresses or ports to the security group to allow SSH access. 2. Switch to root user.

Alternatively, you can use `sudo` to execute the following commands as ec2-user. 3. Set a hostname and fully qualified domain name (FQDN) for your instance by executing the `hostnamectl` command and updating the `/etc/hostname` file.

```
   hostnamectl set-hostname --static <your_hostname>
   echo <your_hostname.example.com> > /etc/hostname
```

Open a new session to verify the hostname change. 4. Ensure that the `DHCLIENT_SET_HOSTNAME` parameter is set to **no** to prevent DHCP from changing the hostname during restart.

```
   grep DHCLIENT_SET_HOSTNAME /etc/sysconfig/network/dhcp
```

5. Set the `preserve_hostname` parameter to true to ensure your hostname is preserved during restart.

```
   sed -i '/preserve_hostname/ c\preserve_hostname: true' /etc/cloud/cloud.cfg
```

6. Add an entry to the `/etc/hosts` file with the new hostname and IP address.

```
  <ip_address> <hostname.example.com> <hostname>
```

7. If you are using a BYOS SLES for SAP image, register your instance with SUSE. Ensure that your subscription is for SLES for SAP.

```
   SUSEConnect -r <Your_Registration_Code>
   SUSEConnect -s
```

8. Ensure that the following packages are installed:

`systemd`, `tuned`, `saptune`, `libgcc_s1`, `libstdc++6`, `cpupower`, `autofs`, `nvme-cli`, `libssh2-1`, `libopenssl1_0_0`

You can use the `rpm` command to check whether a package is installed.

```
   rpm -qi <package_name>
```

You can then use the zypper install command to install the missing packages.

```
   zypper install <package_name>
```

###### Note

If you are importing your own SLES image, additional packages might be required to ensure that your instance is optimally setup. For the latest information, refer to the Package List section in the SLES for SAP Application Configuration Guide for SAP HANA, which is attached to SAP OSS Note [1944799](https://launchpad.support.sap.com/#/notes/1944799 "https://launchpad.support.sap.com/#/notes/1944799") 9. Ensure that your instance is running on a kernel version that is recommended in SAP OSS Note [2205917](https://launchpad.support.sap.com/#/notes/2205917 "https://launchpad.support.sap.com/#/notes/2205917") or [2684254](https://launchpad.support.sap.com/#/notes/2684254 "https://launchpad.support.sap.com/#/notes/2684254") depending on your version. If needed, update your system to meet the minimum kernel version. You can check the version of the kernel and other packages by using the following command:

```
   rpm -qi kernel*
```

10. Start `saptune daemon` and use the following command to set it to automatically start when the system reboots.

```
   saptune daemon start
```

11. Check whether the `force_latency` parameter is set in the `saptune` configuration file.

```
   grep force_latency /usr/lib/tuned/saptune/tuned.conf
```

If the parameter is set, skip the next step and proceed with activating the HANA profile with `saptune`. 12. Update the `saptune HANA` profile according to SAP OSS Note [2205917](https://launchpad.support.sap.com/#/notes/2205917 "https://launchpad.support.sap.com/#/notes/2205917"), and then run the following commands to create a custom profile for SAP HANA. This step is not required if the `force_latency` parameter is already set.

```
   mkdir /etc/tuned/saptune
   cp /usr/lib/tuned/saptune/tuned.conf /etc/tuned/saptune/tuned.conf
   sed -i "/\[cpu\]/ a force_latency=70" /etc/tuned/saptune/tuned.conf
   sed -i "s/script.sh/\/usr\/lib\/tuned\/saptune\/script.sh/"
```

13. Switch the `tuned` profile to HANA and verify that all settings are configured appropriately.

```
   saptune solution apply HANA
   saptune solution verify HANA
```

14. Configure and start the Network Time Protocol (NTP) service. You can adjust the NTP server pool based on your requirements; for example:

###### Note

Remove any existing invalid NTP server pools from `/etc/ntp.conf` before adding the following.

```
   echo "server 0.pool.ntp.org" >> /etc/ntp.conf
   echo "server 1.pool.ntp.org" >> /etc/ntp.conf
   echo "server 2.pool.ntp.org" >> /etc/ntp.conf
   echo "server 3.pool.ntp.org" >> /etc/ntp.conf
   systemctl enable ntpd.service
   systemctl start ntpd.service
```

###### Tip

Instead of connecting to the global NTP server pool, you can connect to your internal NTP server if needed. Or you can use [Amazon Time Sync Service](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") to keep your system time in sync. 15. Set the clocksource to `tsc` by updating the `current_clocksource` file and the GRUB2 boot loader.

```
   echo "tsc" > /sys/devices/system/clocksource/*/current_clocksource
   cp /etc/default/grub /etc/default/grub.backup
   sed -i '/GRUB_CMDLINE_LINUX/ s|"| clocksource=tsc"|2' /etc/default/grub
   grub2-mkconfig -o /boot/grub2/grub.cfg
```

16. Reboot your system for the changes to take effect.
17. Continue with [storage configuration for SAP HANA](configure-storage-for-sap-hana.md "configure-storage-for-sap-hana.md").

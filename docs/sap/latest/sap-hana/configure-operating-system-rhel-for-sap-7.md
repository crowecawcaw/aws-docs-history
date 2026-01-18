# Configure RHEL 7/8/9 for SAP

###### Important

In the following steps, you need to update several configuration files. We recommend taking a backup of the files before you modify them. This will help you to revert to the previous configuration if needed.

1. After your instance is up and running, connect to the instance by using Secure Shell (SSH) and the key pair that you used to launch the instance.

###### Note

Depending on your network and security settings, you might have to first connect by using SSH to a bastion host before accessing your SAP HANA instance, or you might have to add IP addresses or ports to the security group to allow SSH access. 2. Switch to root user.

Alternatively, you can use sudo to execute the following commands as ec2-user. 3. Set a hostname for your instance by executing the `hostnamectl` command and update the `/etc/cloud/cloud.cfg` file to ensure that your hostname is preserved during system reboots.

```
    hostnamectl set-hostname --static <your_hostname>
   echo "preserve_hostname: true" >> /etc/cloud/cloud.cfg
```

Open a new session to verify the hostname change. 4. Add an entry to the `/etc/hosts` file with the new hostname and IP address.

```
  <ip address> <hostname.example.com> <hostname>
```

Ensure that the packages listed in the following SAP Notes (SAP portal access required) are installed:

    * [SAP Note 2002167 - Red Hat Enterprise Linux 7.x: Installation and Upgrade](https://launchpad.support.sap.com/#/notes/2002167 "https://launchpad.support.sap.com/#/notes/2002167")
    * [SAP Note 2772999 - Red Hat Enterprise Linux 8.x: Installation and Configuration](https://launchpad.support.sap.com/#/notes/2772999 "https://launchpad.support.sap.com/#/notes/2772999")
    * [SAP Note 3108316 - Red Hat Enterprise Linux 9.x: Installation and Configuration](https://launchpad.support.sap.com/#/notes/3108316 "https://launchpad.support.sap.com/#/notes/3108316")



    Note that your instance should have access to the SAP HANA channel to install libraries requires for SAP HANA installations.


    You can use the `rpm` command to check whether a package is installed:



    ```
      rpm -qi <package_name>
    ```

    You can then install any missing packages by using the `yum –y install` command.



    ```
      yum -y install <package name>
    ```

    ###### Note

    Depending on your base RHEL image, additional packages might be required to ensure that your instance is optimally setup. (You can skip this step if you are using the RHEL for SAP with HA & US image.) For the latest information, refer to the RHEL configuration guide that is attached to SAP OSS Note [2009879](https://launchpad.support.sap.com/#/notes/2009879 "https://launchpad.support.sap.com/#/notes/2009879"). Review the packages in the Install Additional Required Packages section and the Appendix–Required Packages for SAP HANA on RHEL 7 section.

5. Ensure that your instance is running on a kernel version that is recommended in SAP OSS Note [2292690](https://launchpad.support.sap.com/#/notes/2292690 "https://launchpad.support.sap.com/#/notes/2292690"), [2777782](https://launchpad.support.sap.com/#/notes/2777782 "https://launchpad.support.sap.com/#/notes/2777782"), and [3108302](https://launchpad.support.sap.com/#/notes/3108302 "https://launchpad.support.sap.com/#/notes/3108302"). If needed, update your system to meet the minimum kernel version. You can check the version of the kernel and other packages using the following command.

```
 rpm -qi kernel*
```

6. Start `tuned daemon` and use the following commands to set it to automatically start when the system reboots.

```
 systemctl start tuned

systemctl enable tuned
```

7. Configure the `tuned HANA` profile to optimize your instance for SAP HANA workloads.

Check whether the `force_latency` parameter is already set in the `/usr/lib/tuned/sap-hana/tuned.conf` file. If the parameter is set, execute the following commands to apply and activate the `sap-hana` profile.

```
 tuned-adm profile sap-hana
tuned-adm active
```

If the `force_latency` parameter is not set, execute the following steps to modify and activate the `sap-hana` profile.

```
 mkdir /etc/tuned/sap-hana
cp /usr/lib/tuned/sap-hana/tuned.conf /etc/tuned/sap-hana/tuned.conf
sed -i '/force_latency/ c\force_latency=70' /etc/tuned/sap-hana/tuned.conf
tuned-adm profile sap-hana
tuned-adm active
```

8. Disable Security-Enhanced Linux (SELinux) by running the following command. (Skip this step if you are using the RHEL for SAP with HA & US image.)

```
    sed -i 's/\(SELINUX=enforcing\|SELINUX=permissive\)/SELINUX=disabled/g' \/etc/selinux/config
```

9. Disable Transparent Hugepages (THP) at boot time by adding the following to the line that starts with GRUB_CMDLINE_LINUX in the `/etc/default/grub` file. Execute the following commands to add the required parameter and to re-configure grub (Skip this step if you are using the RHEL for SAP with HA & US image.)

```
    sed -i '/GRUB_CMDLINE_LINUX/ s|"| transparent_hugepage=never"|2' /etc/default/grub
   cat /etc/default/grub
   grub2-mkconfig -o /boot/grub2/grub.cfg
```

10. Add symbolic links by executing following commands. (Skip this step if you are using the RHEL for SAP with HA & US image.)

```
    ln -s /usr/lib64/libssl.so.10 /usr/lib64/libssl.so.1.0.1
   ln -s /usr/lib64/libcrypto.so.10 /usr/lib64/libcrypto.so.1.0.1
```

11. Configure and start the Network Time Protocol (NTP) service. You can adjust the NTP server pool based on your requirements. The following is just an example.

###### Note

Remove any existing invalid NTP server pools from `/etc/ntp.conf` before adding the following.

```
    echo "server 0.pool.ntp.org" >> /etc/ntp.conf
   echo "server 1.pool.ntp.org" >> /etc/ntp.conf
   echo "server 2.pool.ntp.org" >> /etc/ntp.conf
   echo "server 3.pool.ntp.org" >> /etc/ntp.conf
   systemctl enable ntpd.service
   systemctl start ntpd.service
   systemctl restart systemd-timedated.service
```

###### Tip

Instead of connecting to the global NTP server pool, you can connect to your internal NTP server if needed. Alternatively, you can also use [Amazon Time Sync Service](../../../AWSEC2/latest/UserGuide/set-time.md "../../../AWSEC2/latest/UserGuide/set-time.md") to keep your system time in sync. 12. Set clocksource to `tsc` by the updating the `current_clocksource` file and the GRUB2 boot loader.

```
    echo "tsc" > /sys/devices/system/clocksource/*/current_clocksource
   cp /etc/default/grub /etc/default/grub.backup
   sed -i '/GRUB_CMDLINE_LINUX/ s|"| clocksource=tsc"|2' /etc/default/grub
   grub2-mkconfig -o /boot/grub2/grub.cfg
```

13. For RHEL9 only, disable the LVM device persistence using the following commands.

```
 sed -i'.bkp' -e 's/ use_devicesfile = 0/use_devicesfile = 1/g' /etc/lvm/lvm.conf
mv /etc/lvm/devices/system.devices /etc/lvm/devices/system.devices.bkp
```

14. Reboot your system for the changes to take effect.
15. After the reboot, log in as root and execute the `tuned-adm` command to verify that all SAP recommended settings are in place.

```
    tuned-adm verify

  “tuned-adm verify” creates a log file under /var/log/tuned/tuned.log Review this log file and ensure that  all checks have passed.
```

16. Continue with storage configuration.

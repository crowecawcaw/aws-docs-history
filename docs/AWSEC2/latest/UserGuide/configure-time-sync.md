# Set the time reference on your EC2 instance or any

internet-connected device to use the public Amazon Time Sync Service

You can set your instance, or any internet-connected device such as your local
computer or an on-prem server, to use the public Amazon Time Sync Service, which is accessible over the
internet at `time.aws.com`. You can use the public Amazon Time Sync Service as a backup for the
local Amazon Time Sync Service and to connect resources outside of AWS to the Amazon Time Sync Service.

###### Note

For the best performance, we recommend using the _local_ Amazon Time Sync Service on your instances, and only using the _public_ Amazon Time Sync Service as a backup.

Use the instructions for the operating system of your instance or device.

###### To set your Linux instance or device to use the public Amazon Time Sync Service using

chrony or ntpd

1. Edit `/etc/chrony.conf` (if you use chrony) or
   `/etc/ntp.conf` (if you use ntpd) using a text editor as
   follows:
   1. To prevent your instance or device from trying to mix smeared
      and non-smeared servers, remove or comment out lines starting
      with `server` except any existing connection to the
      local Amazon Time Sync Service.

   ###### Important

   If you're setting your EC2 instance to connect to the
   public Amazon Time Sync Service, do not remove the following line which sets
   your instance to connect to the local Amazon Time Sync Service. The local
   Amazon Time Sync Service is a more direct connection and will provide better
   clock accuracy. The public Amazon Time Sync Service should only be used as a
   backup.

   ```
   server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4
   ```

   2. Add the following line to connect to the public Amazon Time Sync Service.

   ```
   pool time.aws.com iburst
   ```

2. Restart the daemon using one of the following commands.
   - chrony

   ```
   sudo service chronyd force-reload
   ```

   - ntpd

   ```
   sudo service ntp reload
   ```

###### To set your macOS instance or device to use the public Amazon Time Sync Service

1. Open **System Preferences**.
2. Choose **Date & Time**, and then choose the
   **Date & Time** tab.
3. To make changes, choose the lock icon, and enter your password when
   prompted.
4. For **Set date and time automatically**, enter
   `time.aws.com`.

###### To set your Windows instance or device to use the public Amazon Time Sync Service

1. Open the **Control Panel**.
2. Choose the **Date and Time** icon.
3. Choose the **Internet Time** tab. This tab is not be
   available if your PC is part of a domain. In this case, it will
   synchronize time with the domain controller. You can configure the
   controller to use the public Amazon Time Sync Service.
4. Choose **Change settings**.
5. Select the checkbox for **Synchronize with an Internet time
   server**.
6. Next to **Server**, enter `time.aws.com`.

###### To set your Windows Server instance or device to use the public

Amazon Time Sync Service

- Follow [Microsoft's instructions](https://support.microsoft.com/en-us/kb/816042 "https://support.microsoft.com/en-us/kb/816042") to update your registry.

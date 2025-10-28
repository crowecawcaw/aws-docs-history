# Set EC2Config service properties from the system dialog on your EC2 Windows instance

The following procedure describes how to use the **EC2 Service Properties**
system dialog to enable or disable settings.

1. Launch and connect to your Windows instance.
2. From the **Start** menu, click **All
   Programs**, and then click **EC2ConfigService
   Settings**.

![EC2Config service properties shown in the General tab.](images/EC2ConfigProperties_General.png) 3. On the **General** tab of the **EC2 Service Properties**
system dialog, you can enable or disable the following settings.

**Set Computer Name**

If this setting is enabled (it is disabled by default), the host
name is compared to the current internal IP address at each boot; if
the host name and internal IP address do not match, the host name is
reset to contain the internal IP address and then the system reboots
to pick up the new host name. To set your own host name, or to
prevent your existing host name from being modified, do not enable
this setting.

**User Data**

User data execution enables you to specify scripts in the instance metadata.
By default, these scripts are run during the initial launch.
You can also configure them to run the next time you reboot or start the instance,
or every time you reboot or start the instance.

If you have a large script, we recommend that you use user data to
download the script, and then run it.

For more information, see [User data execution](user-data.md#user-data-execution "user-data.md#user-data-execution").

**Event Log**

Use this setting to display event log entries on the console
during boot for easy monitoring and debugging.

Click **Settings** to specify filters for the log entries sent to the
console. The default filter sends the three most recent error
entries from the system event log to the console.

**Wallpaper Information**

Use this setting to display system information on the desktop
background. The following is an example of the information displayed
on the desktop background.

![Wallpaper Information displayed on the desktop background.](images/EC2ConfigProperties_Wallpaper.png)

The information displayed on the desktop background is controlled
by the settings file
`EC2ConfigService\Settings\WallpaperSettings.xml`.

**Enable Hibernation**

Use this setting to allow EC2 to signal the operating system to perform hibernation. 4. Click the **Storage** tab. You can enable or disable the
following settings.

![Storage tab within EC2 Service Properties.](images/EC2ConfigProperties_Storage.png)

**Root Volume**

This setting dynamically extends Disk 0/Volume 0 to include any unpartitioned space.
This can be useful when the instance is booted from a root volume
that has a custom size.

**Initialize Drives**

This setting formats and mounts all volumes attached to the
instance during start.

**Drive Letter Mapping**

The system maps the volumes attached to an instance to drive
letters. For Amazon EBS volumes, the default is to assign drive letters
going from D: to Z:. For instance store volumes, the default depends
on the driver. AWS PV drivers and Citrix PV drivers assign instance
store volumes drive letters going from Z: to A:. Red Hat drivers
assign instance store volumes drive letters going from D: to Z:.

To choose the drive letters for your volumes, click
**Mappings**. In the
**DriveLetterSetting** dialog box, specify the
**Volume Name** and **Drive
Letter** values for each volume, click **Apply**, and then click
**OK**. We recommend that you select drive
letters that avoid conflicts with drive letters that are likely to
be in use, such as drive letters in the middle of the
alphabet.

![DriveLetterSetting dialog box.](images/EC2ConfigProperties_driver_letter_mapping.png)

After you specify a drive letter mapping and attach a volume with
same label as one of the volume names that you specified, EC2Config
automatically assigns your specified drive letter to that volume.
However, the drive letter mapping fails if the drive letter is
already in use. Note that EC2Config doesn't change the drive letters
of volumes that were already mounted when you specified the drive
letter mapping. 5. To save your settings and continue working on them later, click **OK** to
close the **EC2 Service Properties** system dialog. If you have
finished customizing your instance and want to create an AMI from that instance,
see [Create an Amazon EC2 AMI using Windows Sysprep](ami-create-win-sysprep.md "ami-create-win-sysprep.md").

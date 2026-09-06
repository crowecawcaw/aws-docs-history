

# Configuring shadow copies to use the default storage and schedule
<a name="setting-up-fsx-shadow-copies"></a>

You can quickly set up shadow copies on your file system by using the default shadow copy storage setting and schedule. The default shadow copy storage setting lets shadow copies consume a maximum of 10 percent of your file system storage capacity. If you increase your file system's storage capacity, the amount of the currently allocated shadow copy storage is not similarly increased.

The default schedule automatically takes shadow copies every Monday, Tuesday, Wednesday, Thursday, and Friday, at 7:00 AM and 12:00 PM UTC.

**To set the default level of shadow copy storage**

1. Connect to a Windows compute instance that has network connectivity with your file system. 

1. Log in to the Windows compute instance as a member of the file system administrators group. In AWS Managed Microsoft AD, that group is **AWS Delegated FSx Administrators**. In your self-managed Microsoft AD, that group is **Domain Admins** or the custom group that you specified for administration when you created your file system. For more information, see [Connecting to Your Windows Instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) in the *Amazon EC2 User Guide*. 

1.  Set the default amount of shadow storage using the following command. Replace `{{FSxFileSystem-Remote-PowerShell-Endpoint}}` with the Windows Remote PowerShell endpoint of file system that you want to administer. You can find the Windows Remote PowerShell endpoint in the Amazon FSx console, in the **Network & Security** section of the file system details screen, or in the response of the `DescribeFileSystem` API operation. 

   ```
   PS C:\Users\delegateadmin> Invoke-Command -ComputerName {{FSxFileSystem-Remote-PowerShell-Endpoint}} -ConfigurationName FSxRemoteAdmin -scriptblock {Set-FsxShadowStorage -Default}
   ```

   The response looks like the following.

   ```
   FSx Shadow Storage Configuration 
   
   AllocatedSpace UsedSpace    MaxSpace MaxShadowCopyNumber
   -------------- ---------    -------- -------------------
                0         0 10737418240                  20
   ```

**To set the default shadow copy schedule**

1. Connect to a Windows compute instance that has network connectivity with your file system.

1. Log in to the Windows compute instance as a member of the file system administrators group. In AWS Managed Microsoft AD, that group is **AWS Delegated FSx Administrators**. In your self-managed Microsoft AD, that group is **Domain Admins** or the custom group that you specified for administration when you created your file system. For more information, see [Connecting to Your Windows Instance](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) in the *Amazon EC2 User Guide*. 

1.  Set the default shadow copy schedule by using the following command. 

   ```
   PS C:\Users\delegateadmin> Invoke-Command -ComputerName {{FSxFileSystem-Remote-PowerShell-Endpoint}} -ConfigurationName FSxRemoteAdmin -scriptblock {Set-FsxShadowCopySchedule -Default}
   ```

    The response displays the default schedule that is now set. 

   ```
   FSx Shadow Copy Schedule
   
   Start Time                Days of week                             WeeksInterval
   ----------                ------------                             -------------
   2019-07-16T07:00:00+00:00 Monday,Tuesday,Wednesday,Thursday,Friday             1
   2019-07-16T12:00:00+00:00 Monday,Tuesday,Wednesday,Thursday,Friday             1
   ```

 To learn about additional options and creating a custom shadow copy schedule, see [Creating a custom shadow copy schedule](shadow-schedules.md). 
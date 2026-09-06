

# Host setup for MSSQL
<a name="mssql"></a>

Use the following procedure to create volumes and LUNs for MSSQL server.

1. Connect to your FSx for ONTAP system using SSH. For more information, see [Managing FSx for ONTAP resources using NetApp applications](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-resources-ontap-apps.html).

1. Use the following SSH command to create the required volumes:

   ```
   vol create -vserver <SvmName> -volume <VolumeName> -aggregate aggr1 -size <VolumeSize> -state online -tiering-policy snapshot-only -percent-snapshot-space 0 -autosize-mode grow -snapshot-policy none -security-style ntfs
   volume modify -vserver <SvmName> -volume <VolumeName> -fractional-reserve 0
   volume modify -vserver <SvmName> -volume <VolumeName> -space-mgmt-try-first vol_grow
   volume snapshot autodelete modify -vserver <SvmName> -volume <VolumeName> -delete-order oldest_first
   ```

1. Start the `iSCSI` service with PowerShell using elevated privileges in Windows servers, and set the startup type to *Automatic*.

   ```
   Start-service -Name msiscsi
   Set-Service -Name msiscsi -StartupType Automatic
   ```

1. Install Multipath-IO with PowerShell using elevated privileges in Windows servers.

   ```
   Install-WindowsFeature -name Multipath-IO -Restart
   ```

1. Find the Windows initiator name with PowerShell using elevated privileges in Windows servers.

   ```
   Get-InitiatorPort | select NodeAddress
   ```

1. Connect to Storage virtual machines (SVM) using putty, and create an `iGroup`.

   ```
   igroup create -igroup <iGroupName> -protocol iscsi -ostype windows -initiator <InitiatorName>
   ```

1. Use the following SSH command to create LUNs inside each volume. To achieve I/O alignment with the operating system partitioning scheme, use `windows_2008` as the recommended LUN type.

   ```
   lun create -path /vol/<VolumeName>/<LUNName> -size <LUNSize> -ostype windows_2008 -space-allocation enabled
   ```

1. Use the following SSH command to map the `igroup` to the LUNs that you just created:

   ```
   lun show
   lun map -path <LUNPath> -igroup <iGroupName>
   ```

1. Get the iSCSI endpoint IP addresses (preferred subnet and standby subnet) from the FSx for ONTAP console. Choose your SVM on the Storage Virtual Machines page.

   The iSCSI endpoint IP addresses are used as iSCSI targets in the next step. For more information, see [Provisioning iSCSI for Windows](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/mount-iscsi-windows.html). .. On the Windows server, go to iSCSI initiator settings, and connect to your iSCSI targets (FSx for ONTAP iSCSI endpoints). Go to **Discovery** > **Discover Portal**. Enter the iSCSI IP address from previous step, and select **Advanced**. From Local Adapter, select **Microsoft iSCSI Initiator**. From Initiator IP, select **IP of the server**. .. From iSCSI Initiator Settings, select **Targets** and choose **Connect** and **Enable muti-path**. .. For best performance, add more sessions. NetApp recommends creating five iSCSI sessions. Select **Properties** > **Add session** > **Advanced**, and repeat the previous step. For further details, see [SQL Server on Amazon EC2 using Amazon FSx for NetApp ONTAP](https://docs.netapp.com/us-en/netapp-solutions/databases/sql-aws-ec2.html#introduction).

1. Initialize disks with the following PowerShell command:

   ```
   $disks = Get-Disk | where PartitionStyle -eq raw
   foreach ($disk in $disks) {Initialize-Disk $disk.Number}
   ```

1. Run the partition and format commands with PowerShell.

   ```
   New-Partition -DiskNumber 1 -DriveLetter F -UseMaximumSize
   Format-Volume -DriveLetter F -FileSystem NTFS -AllocationUnitSize 65536
   ```

LUNs can also be created using SnapCenter.

You can also automate volume and LUN creation using the PowerShell script provided in the Appendix B of [SQL Server on Amazon EC2 using Amazon FSx for NetApp ONTAP](https://docs.netapp.com/us-en/netapp-solutions/databases/sql-aws-ec2.html#introduction).
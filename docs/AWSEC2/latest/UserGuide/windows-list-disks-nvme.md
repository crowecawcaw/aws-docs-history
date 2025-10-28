# Map NVMe disks on Amazon EC2 Windows instance to

volumes

With [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"), EBS volumes are exposed as NVMe devices. This topic
explains how to view the **NVMe disks** that are available
to the Windows operating system on your instance. It also shows how to map those NVMe
disks to the underlying Amazon EBS volumes and the device names specified for the block
device mappings used by Amazon EC2.

###### Topics

- [List NVMe disks](#windows-disks-nvme "#windows-disks-nvme")
- [Map NVMe disks to volumes](#ebs-nvme-volume-map "#ebs-nvme-volume-map")

## List NVMe disks

You can find the disks on your Windows instance using Disk Management or
Powershell.

Disk Management

###### To find the disks on your Windows instance

1. Log in to your Windows instance using Remote Desktop. For more
   information, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
2. Start the Disk Management utility.
3. Review the disks. The root volume is an EBS volume mounted as
   `C:\`. If there are no other disks shown, then you
   didn't specify additional volumes when you created the AMI or launched the
   instance.

The following is an example that shows the disks that are available if you
launch an `r5d.4xlarge` instance with two additional EBS
volumes.

![Disk Management with a root volume, two instance store volumes, and two EBS volumes.](images/disk_management_nvme.png)

PowerShell
The following PowerShell script lists each disk and its corresponding device name
and volume. It is intended for use with [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type"), which use NVMe EBS and
instance store volumes.

Connect to your Windows instance and run the following command to enable
PowerShell script execution.

```
Set-ExecutionPolicy RemoteSigned
```

Copy the following script and save it as `mapping.ps1` on your
Windows instance.

```
# List the disks for NVMe volumes

function Get-EC2InstanceMetadata {
    param([string]$Path)
    (Invoke-WebRequest -Uri "http://169.254.169.254/latest/$Path").Content
}

function GetEBSVolumeId {
    param($Path)
    $SerialNumber = (Get-Disk -Path $Path).SerialNumber
    if($SerialNumber -clike 'vol*'){
        $EbsVolumeId = $SerialNumber.Substring(0,20).Replace("vol","vol-")
    }
    else {
       $EbsVolumeId = $SerialNumber.Substring(0,20).Replace("AWS","AWS-")
    }
    return $EbsVolumeId
}

function GetDeviceName{
    param($EbsVolumeId)
    if($EbsVolumeId -clike 'vol*'){

        $Device  = ((Get-EC2Volume -VolumeId $EbsVolumeId ).Attachment).Device
        $VolumeName = ""
    }
     else {
        $Device = "Ephemeral"
        $VolumeName = "Temporary Storage"
    }
    Return $Device,$VolumeName
}

function GetDriveLetter{
    param($Path)
    $DiskNumber =  (Get-Disk -Path $Path).Number
    if($DiskNumber -eq 0){
        $VirtualDevice = "root"
        $DriveLetter = "C"
        $PartitionNumber = (Get-Partition -DriveLetter C).PartitionNumber
    }
    else
    {
        $VirtualDevice = "N/A"
        $DriveLetter = (Get-Partition -DiskNumber $DiskNumber).DriveLetter
        if(!$DriveLetter)
        {
            $DriveLetter = ((Get-Partition -DiskId $Path).AccessPaths).Split(",")[0]
        }
        $PartitionNumber = (Get-Partition -DiskId $Path).PartitionNumber
    }

    return $DriveLetter,$VirtualDevice,$PartitionNumber

}

$Report = @()
foreach($Path in (Get-Disk).Path)
{
    $Disk_ID = ( Get-Partition -DiskId $Path).DiskId
    $Disk = ( Get-Disk -Path $Path).Number
    $EbsVolumeId  = GetEBSVolumeId($Path)
    $Size =(Get-Disk -Path $Path).Size
    $DriveLetter,$VirtualDevice, $Partition = (GetDriveLetter($Path))
    $Device,$VolumeName = GetDeviceName($EbsVolumeId)
    $Disk = New-Object PSObject -Property @{
      Disk          = $Disk
      Partitions    = $Partition
      DriveLetter   = $DriveLetter
      EbsVolumeId   = $EbsVolumeId
      Device        = $Device
      VirtualDevice = $VirtualDevice
      VolumeName= $VolumeName
    }
	$Report += $Disk
}

$Report | Sort-Object Disk | Format-Table -AutoSize -Property Disk, Partitions, DriveLetter, EbsVolumeId, Device, VirtualDevice, VolumeName
```

Run the script as follows:

```
`PS C:\>` .\mapping.ps1
```

The following is example output for an instance with a root volume, two EBS
volumes, and two instance store volumes.

```
Disk Partitions DriveLetter EbsVolumeId           Device    VirtualDevice VolumeName
---- ---------- ----------- -----------           ------    ------------- ----------
   0          1 C           vol-03683f1d861744bc7 /dev/sda1 root
   1          1 D           vol-082b07051043174b9 xvdb      N/A
   2          1 E           vol-0a4064b39e5f534a2 xvdc      N/A
   3          1 F           AWS-6AAD8C2AEEE1193F0 Ephemeral N/A           Temporary Storage
   4          1 G           AWS-13E7299C2BD031A28 Ephemeral N/A           Temporary Storage
```

If you did not configure your credentials for Tools for Windows PowerShell on the Windows instance, the script cannot
get the EBS volume ID and uses N/A in the `EbsVolumeId` column.

## Map NVMe disks to volumes

You can use the [Get-Disk](https://learn.microsoft.com/en-us/powershell/module/storage/get-disk "https://learn.microsoft.com/en-us/powershell/module/storage/get-disk") command to map Windows disk numbers to Amazon EBS volumes and Amazon EC2 instance store volumes.

```
`PS C:\>` `Get-Disk``Number Friendly Name Serial Number HealthStatus OperationalStatus Total Size Partition
 Style
------ ------------- ------------- ------------ ----------------- ---------- ----------
3 NVMe Amazo... AWS6AAD8C2AEEE1193F0_00000001. Healthy Online 279.4 GB MBR
4 NVMe Amazo... AWS13E7299C2BD031A28_00000001. Healthy Online 279.4 GB MBR
2 NVMe Amazo... vol0a4064b39e5f534a2_00000001. Healthy Online 8 GB MBR
0 NVMe Amazo... vol03683f1d861744bc7_00000001. Healthy Online 30 GB MBR
1 NVMe Amazo... vol082b07051043174b9_00000001. Healthy Online 8 GB MBR`
```

You can also run the **ebsnvme-id** command to map NVMe disk
numbers to EBS volume IDs and device names.

```
`PS C:\>` `C:\PROGRAMDATA\Amazon\Tools\ebsnvme-id.exe``Disk Number: 0
Volume ID: vol-03683f1d861744bc7
Device Name: sda1

Disk Number: 1
Volume ID: vol-082b07051043174b9
Device Name: xvdb

Disk Number: 2
Volume ID: vol-0a4064b39e5f534a2
Device Name: xvdc`
```

# Map non-NVMe disks on Amazon EC2 Windows instance

to volumes

For instances launched from a Windows AMI that uses AWS PV or Citrix PV drivers,
you can use the relationships described on this page to map your Windows disks to your
instance store and EBS volumes. This topic explains how to view the **non-NVMe disks** that
are available to the Windows operating system on your instance. It also shows how to map
those non-NVMe disks to the underlying Amazon EBS volumes and the device names specified for
the block device mappings used by Amazon EC2.

###### Note

If you launch an instance If your Windows AMI uses Red Hat PV drivers, you can
update your instance to use the Citrix drivers. For more information, see [Upgrade PV drivers on EC2 Windows
instances](Upgrading_PV_drivers.md "Upgrading_PV_drivers.md").

###### Topics

- [List non-NVMe disks](#windows-disks "#windows-disks")
- [Map non-NVMe disks to volumes](#windows-volume-mapping "#windows-volume-mapping")

## List non-NVMe disks

You can find the disks on your Windows instance using Disk Management or
PowerShell.

Disk Management

###### To find the disks on your Windows instance

1. Log in to your Windows instance using Remote Desktop. For more
   information, see [Connect to your Windows instance using RDP](connecting_to_windows_instance.md "connecting_to_windows_instance.md").
2. Start the Disk Management utility.

On the taskbar, right-click the Windows
logo, and then choose **Disk Management**. 3. Review the disks. The root volume is an EBS volume mounted as
`C:\`. If there are no other disks shown, then you
didn't specify additional volumes when you created the AMI or launched the
instance.

The following is an example that shows the disks that are available if you
launch an `m3.medium` instance with an instance store volume
(Disk 2) and an additional EBS volume (Disk 1).

![Disk Management with a root volume, one instance store volume, and one EBS volume.](images/disk_management.png) 4. Right-click the gray pane labeled Disk 1, and then select
**Properties**. Note the value of
**Location** and look it up in the tables in [Map non-NVMe disks to volumes](#windows-volume-mapping "#windows-volume-mapping"). For example, the following disk has the location Bus Number 0, Target Id
9, LUN 0. According to the table for EBS volumes, the device name for this
location is `xvdj`.

![The location of an EBS volume.](images/disk_1_location.png)

PowerShell
The following PowerShell script lists each disk and its corresponding device name
and volume.

###### Requirements and limitations

- Requires Windows Server 2012 or later.
- Requires credentials to get the EBS volume ID. You can configure a profile
  using the Tools for PowerShell, or attach an IAM role to the instance.
- Does not support NVMe volumes.
- Does not support dynamic disks.

Connect to your Windows instance and run the following command to enable
PowerShell script execution.

```
Set-ExecutionPolicy RemoteSigned
```

Copy the following script and save it as `mapping.ps1` on your
Windows instance.

```
# List the disks
function Convert-SCSITargetIdToDeviceName {
  param([int]$SCSITargetId)
  If ($SCSITargetId -eq 0) {
    return "sda1"
  }
  $deviceName = "xvd"
  If ($SCSITargetId -gt 25) {
    $deviceName += [char](0x60 + [int]($SCSITargetId / 26))
  }
  $deviceName += [char](0x61 + $SCSITargetId % 26)
  return $deviceName
}

[string[]]$array1 = @()
[string[]]$array2 = @()
[string[]]$array3 = @()
[string[]]$array4 = @()

Get-WmiObject Win32_Volume | Select-Object Name, DeviceID | ForEach-Object {
  $array1 += $_.Name
  $array2 += $_.DeviceID
}

$i = 0
While ($i -ne ($array2.Count)) {
  $array3 += ((Get-Volume -Path $array2[$i] | Get-Partition | Get-Disk).SerialNumber) -replace "_[^ ]*$" -replace "vol", "vol-"
  $array4 += ((Get-Volume -Path $array2[$i] | Get-Partition | Get-Disk).FriendlyName)
  $i ++
}

[array[]]$array = $array1, $array2, $array3, $array4

Try {
  $InstanceId = Get-EC2InstanceMetadata -Category "InstanceId"
  $Region = Get-EC2InstanceMetadata -Category "Region" | Select-Object -ExpandProperty SystemName
}
Catch {
  Write-Host "Could not access the instance Metadata using AWS Get-EC2InstanceMetadata CMDLet.
Verify you have AWSPowershell SDK version '3.1.73.0' or greater installed and Metadata is enabled for this instance." -ForegroundColor Yellow
}
Try {
  $BlockDeviceMappings = (Get-EC2Instance -Region $Region -Instance $InstanceId).Instances.BlockDeviceMappings
  $VirtualDeviceMap = (Get-EC2InstanceMetadata -Category "BlockDeviceMapping").GetEnumerator() | Where-Object { $_.Key -ne "ami" }
}
Catch {
  Write-Host "Could not access the AWS API, therefore, VolumeId is not available.
Verify that you provided your access keys or assigned an IAM role with adequate permissions." -ForegroundColor Yellow
}

Get-disk | ForEach-Object {
  $DriveLetter = $null
  $VolumeName = $null
  $VirtualDevice = $null
  $DeviceName = $_.FriendlyName

  $DiskDrive = $_
  $Disk = $_.Number
  $Partitions = $_.NumberOfPartitions
  $EbsVolumeID = $_.SerialNumber -replace "_[^ ]*$" -replace "vol", "vol-"
  if ($Partitions -ge 1) {
    $PartitionsData = Get-Partition -DiskId $_.Path
    $DriveLetter = $PartitionsData.DriveLetter | Where-object { $_ -notin @("", $null) }
    $VolumeName = (Get-PSDrive | Where-Object { $_.Name -in @($DriveLetter) }).Description | Where-object { $_ -notin @("", $null) }
  }
  If ($DiskDrive.path -like "*PROD_PVDISK*") {
    $BlockDeviceName = Convert-SCSITargetIdToDeviceName((Get-WmiObject -Class Win32_Diskdrive | Where-Object { $_.DeviceID -eq ("\\.\PHYSICALDRIVE" + $DiskDrive.Number) }).SCSITargetId)
    $BlockDeviceName = "/dev/" + $BlockDeviceName
    $BlockDevice = $BlockDeviceMappings | Where-Object { $BlockDeviceName -like "*" + $_.DeviceName + "*" }
    $EbsVolumeID = $BlockDevice.Ebs.VolumeId
    $VirtualDevice = ($VirtualDeviceMap.GetEnumerator() | Where-Object { $_.Value -eq $BlockDeviceName }).Key | Select-Object -First 1
  }
  ElseIf ($DiskDrive.path -like "*PROD_AMAZON_EC2_NVME*") {
    $BlockDeviceName = (Get-EC2InstanceMetadata -Category "BlockDeviceMapping")."ephemeral$((Get-WmiObject -Class Win32_Diskdrive | Where-Object { $_.DeviceID -eq ("\\.\PHYSICALDRIVE" + $DiskDrive.Number) }).SCSIPort - 2)"
    $BlockDevice = $null
    $VirtualDevice = ($VirtualDeviceMap.GetEnumerator() | Where-Object { $_.Value -eq $BlockDeviceName }).Key | Select-Object -First 1
  }
  ElseIf ($DiskDrive.path -like "*PROD_AMAZON*") {
    if ($DriveLetter -match '[^a-zA-Z0-9]') {
      $i = 0
      While ($i -ne ($array3.Count)) {
        if ($array[2][$i] -eq $EbsVolumeID) {
          $DriveLetter = $array[0][$i]
          $DeviceName = $array[3][$i]
        }
        $i ++
      }
    }
    $BlockDevice = ""
    $BlockDeviceName = ($BlockDeviceMappings | Where-Object { $_.ebs.VolumeId -eq $EbsVolumeID }).DeviceName
  }
  ElseIf ($DiskDrive.path -like "*NETAPP*") {
    if ($DriveLetter -match '[^a-zA-Z0-9]') {
      $i = 0
      While ($i -ne ($array3.Count)) {
        if ($array[2][$i] -eq $EbsVolumeID) {
          $DriveLetter = $array[0][$i]
          $DeviceName = $array[3][$i]
        }
        $i ++
      }
    }
    $EbsVolumeID = "FSxN Volume"
    $BlockDevice = ""
    $BlockDeviceName = ($BlockDeviceMappings | Where-Object { $_.ebs.VolumeId -eq $EbsVolumeID }).DeviceName
  }
  Else {
    $BlockDeviceName = $null
    $BlockDevice = $null
  }
  New-Object PSObject -Property @{
    Disk          = $Disk;
    Partitions    = $Partitions;
    DriveLetter   = If ($DriveLetter -eq $null) { "N/A" } Else { $DriveLetter };
    EbsVolumeId   = If ($EbsVolumeID -eq $null) { "N/A" } Else { $EbsVolumeID };
    Device        = If ($BlockDeviceName -eq $null) { "N/A" } Else { $BlockDeviceName };
    VirtualDevice = If ($VirtualDevice -eq $null) { "N/A" } Else { $VirtualDevice };
    VolumeName    = If ($VolumeName -eq $null) { "N/A" } Else { $VolumeName };
    DeviceName    = If ($DeviceName -eq $null) { "N/A" } Else { $DeviceName };
  }
} | Sort-Object Disk | Format-Table -AutoSize -Property Disk, Partitions, DriveLetter, EbsVolumeId, Device, VirtualDevice, DeviceName, VolumeName


```

Run the script as follows:

```
`PS C:\>` .\mapping.ps1
```

The following is example output.

```
Disk  Partitions  DriveLetter   EbsVolumeId             Device      VirtualDevice   DeviceName              VolumeName
----  ----------  -----------   -----------             ------      -------------   ----------              ----------
   0           1            C   vol-0561f1783298efedd   /dev/sda1   N/A             NVMe Amazon Elastic B   N/A
   1           1            D   vol-002a9488504c5e35a   xvdb        N/A             NVMe Amazon Elastic B   N/A
   2           1            E   vol-0de9d46fcc907925d   xvdc        N/A             NVMe Amazon Elastic B   N/A
```

If you did not provide your credentials on the Windows instance, the script cannot
get the EBS volume ID and uses N/A in the `EbsVolumeId` column.

## Map non-NVMe disks to volumes

The block device driver for the instance assigns the actual volume names when
mounting volumes.

###### Mappings

- [Instance store volumes](#instance-store-volume-map "#instance-store-volume-map")
- [EBS volumes](#ebs-volume-map "#ebs-volume-map")

### Instance store volumes

The following table describes how the Citrix PV and AWS PV drivers map
non-NVMe instance store volumes to Windows volumes. The number of available
instance store volumes is determined by the instance type. For more information,
see [Instance store volume limits for EC2 instances](instance-store-volumes.md "instance-store-volumes.md").

| Location                          | Device name |
| --------------------------------- | ----------- |
| Bus Number 0, Target ID 78, LUN 0 | xvdca       |
| Bus Number 0, Target ID 79, LUN 0 | xvdcb       |
| Bus Number 0, Target ID 80, LUN 0 | xvdcc       |
| Bus Number 0, Target ID 81, LUN 0 | xvdcd       |
| Bus Number 0, Target ID 82, LUN 0 | xvdce       |
| Bus Number 0, Target ID 83, LUN 0 | xvdcf       |
| Bus Number 0, Target ID 84, LUN 0 | xvdcg       |
| Bus Number 0, Target ID 85, LUN 0 | xvdch       |
| Bus Number 0, Target ID 86, LUN 0 | xvdci       |
| Bus Number 0, Target ID 87, LUN 0 | xvdcj       |
| Bus Number 0, Target ID 88, LUN 0 | xvdck       |
| Bus Number 0, Target ID 89, LUN 0 | xvdcl       |

### EBS volumes

The following table describes how the Citrix PV and AWS PV drivers map
non-NVME EBS volumes to Windows volumes.

| Location                          | Device name |
| --------------------------------- | ----------- |
| Bus Number 0, Target ID 0, LUN 0  | /dev/sda1   |
| Bus Number 0, Target ID 1, LUN 0  | xvdb        |
| Bus Number 0, Target ID 2, LUN 0  | xvdc        |
| Bus Number 0, Target ID 3, LUN 0  | xvdd        |
| Bus Number 0, Target ID 4, LUN 0  | xvde        |
| Bus Number 0, Target ID 5, LUN 0  | xvdf        |
| Bus Number 0, Target ID 6, LUN 0  | xvdg        |
| Bus Number 0, Target ID 7, LUN 0  | xvdh        |
| Bus Number 0, Target ID 8, LUN 0  | xvdi        |
| Bus Number 0, Target ID 9, LUN 0  | xvdj        |
| Bus Number 0, Target ID 10, LUN 0 | xvdk        |
| Bus Number 0, Target ID 11, LUN 0 | xvdl        |
| Bus Number 0, Target ID 12, LUN 0 | xvdm        |
| Bus Number 0, Target ID 13, LUN 0 | xvdn        |
| Bus Number 0, Target ID 14, LUN 0 | xvdo        |
| Bus Number 0, Target ID 15, LUN 0 | xvdp        |
| Bus Number 0, Target ID 16, LUN 0 | xvdq        |
| Bus Number 0, Target ID 17, LUN 0 | xvdr        |
| Bus Number 0, Target ID 18, LUN 0 | xvds        |
| Bus Number 0, Target ID 19, LUN 0 | xvdt        |
| Bus Number 0, Target ID 20, LUN 0 | xvdu        |
| Bus Number 0, Target ID 21, LUN 0 | xvdv        |
| Bus Number 0, Target ID 22, LUN 0 | xvdw        |
| Bus Number 0, Target ID 23, LUN 0 | xvdx        |
| Bus Number 0, Target ID 24, LUN 0 | xvdy        |
| Bus Number 0, Target ID 25, LUN 0 | xvdz        |

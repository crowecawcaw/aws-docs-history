# Increase the size of an EBS volume on your Mac

instance

You can increase the size of your Amazon EBS volumes on your Mac instance. For more information, see
[Amazon EBS Elastic Volumes](../../../ebs/latest/userguide/ebs-modify-volume.md "../../../ebs/latest/userguide/ebs-modify-volume.md")
in the _Amazon EBS User Guide_.

After you increase the size of the volume, you must increase the size of your APFS container
as follows.

###### Make increased disk space available for use

1. Determine if a restart is required. If you resized an existing EBS volume on a running Mac instance, you must
   [reboot](ec2-instance-reboot.md "ec2-instance-reboot.md") the instance to make the new size available.
   If disk space modification was done during launch time, a reboot will not be required.

View current status of disk sizes:

```
`[ec2-user ~]$`  diskutil list external physical
/dev/disk0 (external, physical):
   #:                       TYPE NAME                    SIZE       IDENTIFIER
   0:                 GUID_partition_scheme            *322.1 GB     disk0
   1:                 EFI EFI                           209.7 MB     disk0s1
   2:                 Apple_APFS Container disk2        321.9 GB     disk0s2
```

2. Copy and paste the following command.

```
`[ec2-user ~]$` PDISK=$(diskutil list physical external | head -n1 | cut -d" " -f1)
APFSCONT=$(diskutil list physical external | grep "Apple_APFS" | tr -s " " | cut -d" " -f8)
yes | sudo diskutil repairDisk $PDISK
```

3. Copy and paste the following command.

```
`[ec2-user ~]$` sudo diskutil apfs resizeContainer $APFSCONT 0
```

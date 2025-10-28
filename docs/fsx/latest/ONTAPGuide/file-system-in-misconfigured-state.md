# Your file system is in a `MISCONFIGURED` state

There are a number of potential causes for a file system to be in a `MISCONFIGURED` state,
each with their own resolution, as follows.

###### Topics

- [The VPC owner account has disabled Multi-AZ VPC sharing](#maz-file-system "#maz-file-system")
- [You can't create a new SVM on a Multi-AZ file system](#unable-to-create-svm-on-maz "#unable-to-create-svm-on-maz")
- [Your file system’s SSD storage tier is more than 90% full](#ssd-tier-gt-90-percent "#ssd-tier-gt-90-percent")

## The VPC owner account has disabled Multi-AZ VPC sharing

Multi-AZ file systems created by a participant AWS account in a shared VPC subnet will go into
a `MISCONFIGURED` state for one of the following reasons:

- The owner account that shared the VPC subnet has disabled Multi-AZ VPC sharing support for FSx for ONTAP file systems.
- The owner account has stopped sharing the VPC subnet.

If the owner account has stopped sharing the VPC subnet, you will see the following message in the console for that file system:

```
The vpc ID `vpc-012345abcde` does not exist
```

To resolve the issue, you must contact the owner account that shared the VPC subnet with you. For more information see
[Creating FSx for ONTAP file systems in shared subnets](creating-file-systems.md#fsxn-vpc-shared-subnets "creating-file-systems.md#fsxn-vpc-shared-subnets") for more information.

## You can't create a new SVM on a Multi-AZ file system

For Multi-AZ file systems created by a participant AWS account in a shared VPC, you will be unable to create a new SVM
for one of the following reasons:

- The owner account that shared the VPC subnet has disabled Multi-AZ VPC sharing support for FSx for ONTAP file systems.
- The owner account has stopped sharing the VPC subnet.

To resolve the issue, you must contact the owner account that shared the VPC subnet with you. For more information see
[Creating FSx for ONTAP file systems in shared subnets](creating-file-systems.md#fsxn-vpc-shared-subnets "creating-file-systems.md#fsxn-vpc-shared-subnets") for more information.

## Your file system’s SSD storage tier is more than 90% full

Your Single-AZ or Multi-AZ file system’s SSD storage tier is currently more than 90% full. We recommend that you do not exceed 80% utilization of your SSD storage tier
on an ongoing basis. If you do not free up space in the SSD storage tier before your file system’s next maintenance window, FSx for ONTAP will temporarily throttle
down your file system’s throughput for the duration of the patching operation. This is done to ensure that the background maintenance processes can complete within
a reasonable time period. To avoid this, please reduce the utilization of your SSD storage tier to below 90%. You can reduce SSD utilization several ways, including:

- Increasing your file system's SSD storage capacity.
- By deleting unneeded data.
- By deleting unneeded volume snapshots.

For more information, see [Managing storage capacity](managing-storage-capacity.md "managing-storage-capacity.md").

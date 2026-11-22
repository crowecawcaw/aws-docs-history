

# Step 2: Validate and confirm inventory

Before loading your server data into MGN, AWS Transform prepares the migration inventory file for your review. You must confirm the migration inventory file data and content as this sets the migration configuration. You can review the data in the file and update it using either of these methods:
+ **Edit the migration inventory file directly** – Download the file in CSV or XLSX format and modify it locally in your preferred spreadsheet application. You can adjust any of the fields in the file, except for the read-only ones.
+ **Use the chat interface** – Make targeted changes for specific columns on individual source servers without downloading the entire file.

The migration inventory file includes details such as server names, operating systems, Amazon EC2 instance type recommendations, storage configuration, target subnets, security groups, IP assignments, and licensing options. Required fields include:
+ **Server information** – Server name, VMID, and source specifications.
+ **Wave assignment** – Migration wave grouping.
+ **Application grouping** – Logical application associations.
+ **Target configuration** – Target account, Region, and Amazon EC2 instance type. You can control the operating system licensing options (BYOL or License Included) and tenancy by specifying the configuration in the inventory file columns `mgn:launch:placement:operating-system-licensing` and `mgn:launch:placement:tenancy`.
+ **Network configuration** – Target subnet and security groups. To migrate to an AWS Local Zone or an Outpost, specify a target subnet on the Local Zone or Outpost.
+ **Storage configuration** – The storage settings for each source server, in the `mgn:launch:default:ebs:*` fields. The settings are defined per source server, and you update them per source server. By default, these fields contain the server's storage settings defaults. MGN uses these settings for every Amazon EBS volume that it creates for the server, including when a new disk appears on the source server or when a disk grows. The storage settings defaults include:
  + **Amazon EBS volume type** – For example, gp2, gp3, io1, io2, st1, or sc1.
  + **IOPS** – The provisioned IOPS for the volumes. The allowed range depends on the volume type.
  + **Throughput** – The provisioned throughput, in MiB/s. Applies to gp3 volumes only.
  + **Volume initialization rate** – The rate, in MiB/s, at which snapshot data is downloaded to the volume, so that volumes are fully initialized in a predictable amount of time. Additional costs apply.
  + **Delete on termination** – Whether the volumes are deleted when the instance is terminated. If you turn this off, you must delete the volumes manually when you no longer need them.

  If a setting has no value, MGN uses its own default. With no volume type, MGN uses gp3 with 3,000 IOPS and 125 MiB/s throughput. With a volume type but no IOPS or throughput, MGN uses the highest IOPS and throughput that the volume type and size allow. For the limits of each volume type, see [Amazon EBS volume types](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-volume-types.html) in the *Amazon EBS User Guide*.

  If you use storage recommendations, AWS Transform fills these fields with the recommended values instead of the defaults. For Amazon EBS, these are the volume type, IOPS, and throughput. MGN sets the volume size automatically, based on the size of the source disk. For Amazon FSx for NetApp ONTAP, AWS Transform adds the SVM IDs mapped to your source storage arrays. If a storage value is missing, validation shows a warning that doesn't block the migration. For more information, see [Storage recommendations](transform-vmware-ms-migration-defaults.md#transform-vmware-ms-storage-recommendations).

For more information about the fields, see [Import parameters](https://docs.aws.amazon.com/mgn/latest/ug/import-parameters.html) in the *MGN User Guide*.

After you review the migration inventory file, you can either accept it as shown or upload a modified version. AWS Transform then loads the data into MGN, which creates source server records for each server in the wave.

**Note**  
Do not remove columns or change column headers in the inventory file. AWS Transform requires the original file structure to process the data correctly.

**Note**  
AWS Transform allows one import to a given target AWS account and target AWS Region at a time. If you work on more than one wave simultaneously, or if there is more than one migration job running with the same target account, you must wait for an import to finish before you can perform another import in a different wave or job.
# Specify a licensing option for your

import

You can specify either a license type or a usage operation for the VMs that you
migrate. Specifying a license option ensures your operating system is licensed
appropriately and your billing is optimized. If you choose a license type that is
incompatible with your VM, the VM Import task fails with an error message. For more
information on troubleshooting errors, see [Troubleshooting VM Import/Export](vmimport-troubleshooting.md "vmimport-troubleshooting.md").

###### Topics

- [Specify a license
  type](#licensing-specify-option-license-type "#licensing-specify-option-license-type")
- [Specify a usage operation](#licensing-specify-option-usage-operation "#licensing-specify-option-usage-operation")

## Specify a license

type

**Specify license type**

You can specify the following values for the `--license-type`
parameter:

- `AWS` (license included) – Replaces the
  source-system license with an AWS license on the migrated VM.
- `BYOL` – Retains the source-system license on the
  migrated VM.

###### Note

Leaving the `--license-type` parameter undefined while
importing a Windows Server OS is the same as choosing `AWS`
and the same as choosing `BYOL` when importing a Windows
client OS (such as Windows 10) or a Linux OS.

For example, to specify the license type as an AWS license, run the following
command:

```
aws ec2 import-image \
    --license-type `aws` \
    --disk-containers Format=`OVA`,Url=S3://`bucket_name`/`sql_std_image.ova`
```

## Specify a usage operation

###### Important

AWS stamps the software edition with the information that you provide. You
are responsible for entering the correct software edition information for any
licenses that you bring to AWS.

You can specify the following values for the `--usage-operation`
parameter:

| Platform details                                                            | Usage operation \* |
| --------------------------------------------------------------------------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Windows Server License Included without SQL Server                          | RunInstances:0002  |
| Windows Server License Included with SQL Server (any edition) BYOL          | RunInstances:0002  |
| Windows Server License Included with SQL Server Standard License Included   | RunInstances:0006  |
| Windows Server License Included with SQL Server Enterprise License Included | RunInstances:0102  |
| Windows Server License Included with SQL Server Web License Included        | RunInstances:0202  |
| Windows Server BYOL without SQL Server                                      | RunInstances:0800  |
| Windows Server BYOL with SQL (any edition) BYOL                             | RunInstances:0800  |
| Linux/UNIX without SQL Server                                               | RunInstances       |
| Linux/UNIX with SQL Server (any edition) BYOL                               | RunInstances       |
| Linux/UNIX with SQL Server Enterprise License Included                      | RunInstances:0100  |
| Linux/UNIX with SQL Server Standard License Included                        | RunInstances:0004  |
| Linux/UNIX with SQL Server Web License Included                             | RunInstances:0200  |
| Red Hat Enterprise Linux                                                    | RunInstances:0010  |
| SUSE Linux                                                                  | RunInstances:000g  | \* If you are running Spot Instances, the `lineup/Operation` on your AWS Cost and Usage Report might be different from the **Usage operation** value that is listed here. For example, to specify the usage operation for Windows with SQL Server Standard, run the following command: `` aws ec2 import-image \ --usage-operation `RunInstances:0006` \ --disk-containers Format=`OVA`,Url=S3://`bucket_name`/`sql_std_image.ova` `` For more information about billing codes, see [AMI billing information fields](../../../AWSEC2/latest/UserGuide/billing-info-fields.md "../../../AWSEC2/latest/UserGuide/billing-info-fields.md"). |

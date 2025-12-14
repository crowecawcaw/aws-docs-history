# Where can I transfer my data with

AWS DataSync?

Where you can transfer your data with AWS DataSync depends on the following factors:

- Your transfer's source and destination [locations](how-datasync-transfer-works.md#sync-locations "how-datasync-transfer-works.md#sync-locations")
- If your locations are in different AWS accounts
- If your locations are in different AWS Regions
- If your are using Basic mode or Enhanced mode

## Supported transfers in the same

AWS account

DataSync supports transfers between the following storage resources that are associated
with the same AWS account.

| Source                       | Destination                                 | Requires an agent?  | Supported task mode |
| ---------------------------- | ------------------------------------------- | ------------------- | ------------------- |
| • NFS<br>• SMB               | • Amazon S3                                 | Yes                 | Basic, Enhanced     |
| • NFS<br>• SMB               | • Amazon EFS<br>• Amazon FSx                | Yes                 | Basic only          |
| • HDFS<br>• Object Storage   | • Amazon S3<br>• Amazon EFS<br>• Amazon FSx | Yes                 | Basic only          |
| • Other cloud storage        | • Amazon S3                                 | Only for Basic mode | Basic, Enhanced     |
| • Other cloud storage        | • Amazon EFS<br>• Amazon FSx                | Yes                 | Basic only          |
| • Amazon S3                  | • Amazon S3                                 | No                  | Basic, Enhanced     |
| • Amazon S3                  | • Amazon EFS<br>• Amazon FSx                | No                  | Basic only          |
| • Amazon S3                  | • NFS<br>• SMB                              | Yes                 | Basic, Enhanced     |
| • Amazon S3                  | • HDFS<br>• Object Storage                  | Yes                 | Basic only          |
| • Amazon S3                  | • Other cloud storage                       | Only for Basic mode | Basic, Enhanced     |
| • Amazon EFS<br>• Amazon FSx | • NFS<br>• SMB                              | Yes                 | Basic only          |
| • Amazon EFS<br>• Amazon FSx | • HDFS<br>• Object Storage                  | Yes                 | Basic only          |
| • Amazon EFS<br>• Amazon FSx | • Other cloud storage                       | Yes                 | Basic only          |
| • Amazon EFS<br>• Amazon FSx | • Amazon S3                                 | No                  | Basic only          |
| • Amazon EFS<br>• Amazon FSx | • Amazon EFS<br>• Amazon FSx                | No                  | Basic only          |
| • S3 on Outposts             | • S3 (in AWS Regions)                       | Yes                 | Basic only          |
| • Amazon S3 (in AWS Regions) | • S3 on Outposts                            | Yes                 | Basic only          |

## Supported transfers across

AWS accounts

DataSync supports some transfers between storage resources that are associated with
different AWS accounts.

| Source                                                                                                                | Destination                  | Requires an agent?                     | Supported task mode |
| --------------------------------------------------------------------------------------------------------------------- | ---------------------------- | -------------------------------------- | ------------------- |
| • NFS<br>• SMB                                                                                                        | • Amazon S3                  | Yes                                    | Basic, Enhanced     |
| • HDFS<br>• Object Storage                                                                                            | • Amazon S3                  | Yes                                    | Basic only          |
| • Amazon S3                                                                                                           | • Amazon S3                  | No                                     | Basic, Enhanced     |
| • Amazon S3                                                                                                           | • Amazon EFS<br>• Amazon FSx | No                                     | Basic only          |
| • Amazon S3                                                                                                           | • NFS<br>• SMB               | Yes                                    | Basic, Enhanced     |
| • Amazon S3                                                                                                           | • HDFS<br>• Object Storage   | Yes                                    | Basic only          |
| • Amazon EFS<br>• Amazon FSx                                                                                          | • Amazon S3                  | No                                     | Basic only          |
| • Amazon EFS1<br>• Amazon FSx for OpenZFS1<br>• Amazon FSx for Windows File Server2<br>• Amazon FSx for NetApp ONTAP3 | • Amazon EFS<br>• Amazon FSx | Yes (when used as an NFS/SMB location) | Basic only          |

1 Configured as an [NFS
location](create-nfs-location.md "create-nfs-location.md").

2 Configured as an [SMB
location](create-smb-location.md "create-smb-location.md").

3 Configured as an NFS or SMB location.

## Supported transfers in the same

AWS Region

There are no restrictions when transferring data within the same AWS Region
(including [opt-in Regions](../../../accounts/latest/reference/manage-acct-regions.md "../../../accounts/latest/reference/manage-acct-regions.md")).
For more information, see [AWS Regions supported by
DataSync](../../../general/latest/gr/datasync.md "../../../general/latest/gr/datasync.md").

## Supported transfers between

AWS Regions

Note the following when transferring data between [AWS Regions supported by
DataSync](../../../general/latest/gr/datasync.md "../../../general/latest/gr/datasync.md"):

- When transferring between AWS storage services in different AWS Regions,
  one of the two locations must be in the Region where you're using DataSync.
- You can't transfer across Regions with an NFS, SMB, HDFS, or object storage
  location. In these situations, both of your transfer locations must be in the
  same Region where you [activate your DataSync
  agent](activate-agent.md "activate-agent.md").
- With AWS GovCloud (US) Regions, you can:
  - Transfer between the AWS GovCloud (US-East) and AWS GovCloud (US-West)
    Regions.
  - Transfer between an AWS GovCloud (US) Region and commercial AWS Region,
    such as US East (N. Virginia). This type of transfer requires an [agent](agent-requirements.md "agent-requirements.md") when transferring between
    Amazon EFS or Amazon FSx file systems.

###### Important

You pay for data transferred between AWS Regions. This transfer is billed as
data transfer out from the source to destination Region. For more information, see
[AWS DataSync
Pricing](https://aws.amazon.com/datasync/pricing/ "https://aws.amazon.com/datasync/pricing/").

## Determining if your transfer requires a

DataSync agent

Depending on your transfer scenario, you might need a DataSync agent. For more
information, see [Do I need an AWS DataSync agent?](do-i-need-datasync-agent.md "do-i-need-datasync-agent.md")

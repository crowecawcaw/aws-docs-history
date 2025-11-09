# Where can I transfer my data with

AWS DataSync?

Where you can transfer your data with AWS DataSync depends on the following factors:

- Your transfer's source and destination [locations](how-datasync-transfer-works.md#sync-locations "how-datasync-transfer-works.md#sync-locations")
- If your locations are in different AWS accounts
- If your locations are in different AWS Regions

## Supported transfers in the same

AWS account

DataSync supports transfers between the following storage resources that are associated
with the same AWS account.

| Source (from)                                                                                                                                                                                                                                                                                                                                                                        | Destination (to)                                                                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| • NFS<br>• SMB<br>• HDFS<br>• Object storage                                                                                                                                                                                                                                                                                                                                         | • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• Amazon FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                     |
| • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                            | • NFS<br>• SMB<br>• HDFS<br>• Object storage                                                                                                                                                                                                                                                                                                                                         |
| • Google Cloud Storage<br>• Microsoft Azure Blob Storage<br>• Microsoft Azure Files<br>• Wasabi Cloud Storage<br>• DigitalOcean Spaces<br>• Oracle Cloud Infrastructure Object<br>Storage<br>• Cloudflare R2 Storage<br>• Backblaze B2 Cloud Storage<br>• NAVER Cloud Object Storage<br>• Alibaba Cloud Object Storage Service<br>• IBM Cloud Object Storage<br>• Seagate Lyve Cloud | • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• Amazon FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                     |
| • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• Amazon FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                     | • Google Cloud Storage<br>• Microsoft Azure Blob Storage<br>• Microsoft Azure Files<br>• Wasabi Cloud Storage<br>• DigitalOcean Spaces<br>• Oracle Cloud Infrastructure Object<br>Storage<br>• Cloudflare R2 Storage<br>• Backblaze B2 Cloud Storage<br>• NAVER Cloud Object Storage<br>• Alibaba Cloud Object Storage Service<br>• IBM Cloud Object Storage<br>• Seagate Lyve Cloud |
| • Amazon S3 compatible storage on AWS Snowball Edge                                                                                                                                                                                                                                                                                                                                  | • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• Amazon FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                     |
| • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                            | • Amazon S3 compatible storage on Snowball Edge                                                                                                                                                                                                                                                                                                                                      |
| • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                            | • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                                                                                                                                                                                                                            |
| • Amazon S3 (in AWS Regions)                                                                                                                                                                                                                                                                                                                                                         | • Amazon S3 on AWS Outposts                                                                                                                                                                                                                                                                                                                                                          |
| • Amazon S3 on AWS Outposts                                                                                                                                                                                                                                                                                                                                                          | • Amazon S3 (in AWS Regions)                                                                                                                                                                                                                                                                                                                                                         |

## Supported transfers across

AWS accounts

DataSync supports some transfers between storage resources that are associated with
different AWS accounts.

| Source (from)                                                                                                                             | Destination (to)                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| • Amazon EFS1<br>• FSx for Windows File Server2                                                                                           | • Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP                                 |
| • Amazon S3 (in AWS Regions)                                                                                                              | • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP |
| • Amazon S3 (in AWS Regions)<br>• Amazon EFS<br>• FSx for Windows File Server<br>• FSx for Lustre<br>• FSx for OpenZFS<br>• FSx for ONTAP | • Amazon S3 (in AWS Regions)                                                                                                              |
| • NFS<br>• SMB<br>• HDFS<br>• Object storage                                                                                              | • Amazon S3 (in AWS Regions)                                                                                                              |

1 Configured as an [NFS
location](create-nfs-location.md "create-nfs-location.md").

2 Configured as an [SMB
location](create-smb-location.md "create-smb-location.md").

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

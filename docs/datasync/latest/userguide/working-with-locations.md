

# Where can I transfer my data with AWS DataSync?
<a name="working-with-locations"></a>

Where you can transfer your data with AWS DataSync depends on the following factors:
+ Your transfer's source and destination [locations](how-datasync-transfer-works.md#sync-locations)
+ Whether your locations are in different AWS accounts
+ Whether your locations are in different AWS Regions
+ Whether you are using Basic or Enhanced mode

## Supported transfers in the same AWS account
<a name="working-with-locations-same-account"></a>

DataSync supports transfers between the following storage resources that are associated with the same AWS account. You can use Basic or Enhanced mode for all of these transfers except those that use S3 on Outposts, which require Basic mode.


| Source | Destination | Requires an agent? | 
| --- | --- | --- | 
|  + NFS<br />+ SMB<br />+ HDFS<br />+ Object Storage  |  + Amazon S3<br />+ Amazon EFS<br />+ Amazon FSx  | Yes | 
|  + Amazon S3<br />+ Amazon EFS<br />+ Amazon FSx  |  + NFS<br />+ SMB<br />+ HDFS<br />+ Object Storage  | Yes | 
|  + Other cloud storage  |  + Amazon S3  | Only for Basic mode | 
|  + Amazon S3  |  + Other cloud storage  | Only for Basic mode | 
|  + Other cloud storage  |  + Amazon EFS<br />+ Amazon FSx  | Yes | 
|  + Amazon EFS<br />+ Amazon FSx  |  + Other cloud storage  | Yes | 
|  + Amazon S3<br />+ Amazon EFS<br />+ Amazon FSx  |  + Amazon S3<br />+ Amazon EFS<br />+ Amazon FSx  | No | 
|  + S3 on Outposts  |  + S3 (in AWS Regions)  | Yes | 
|  + Amazon S3 (in AWS Regions)  |  + S3 on Outposts  | Yes | 

## Supported transfers across AWS accounts
<a name="working-with-locations-across-accounts"></a>

DataSync supports some transfers between storage resources that are associated with different AWS accounts. You can use Basic or Enhanced mode for all of these transfers.


| Source | Destination | Requires an agent? | 
| --- | --- | --- | 
|  + NFS<br />+ SMB<br />+ HDFS<br />+ Object Storage  |  + Amazon S3  | Yes | 
|  + Amazon S3  |  + NFS<br />+ SMB<br />+ HDFS<br />+ Object Storage  | Yes | 
|  + Amazon S3  |  + Amazon S3<br />+ Amazon EFS<br />+ Amazon FSx  | No | 
|  + Amazon EFS<br />+ Amazon FSx  |  + Amazon S3  | No | 
|  + Amazon EFS1<br />+ Amazon FSx for OpenZFS1<br />+ Amazon FSx for Windows File Server2<br />+ Amazon FSx for NetApp ONTAP3  |  + Amazon EFS<br />+ Amazon FSx  | Yes (when used as an NFS/SMB location) | 

1 Configured as an [NFS location](create-nfs-location.md).

2 Configured as an [SMB location](create-smb-location.md).

3 Configured as an NFS or SMB location.

## Supported transfers in the same AWS Region
<a name="working-with-locations-same-region"></a>

There are no restrictions when transferring data within the same AWS Region (including [opt-in Regions](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html)). For more information, see [AWS Regions supported by DataSync](https://docs.aws.amazon.com/general/latest/gr/datasync.html).

## Supported transfers between AWS Regions
<a name="working-with-locations-cross-regions"></a>

Note the following when transferring data between [AWS Regions supported by DataSync](https://docs.aws.amazon.com/general/latest/gr/datasync.html):
+ When transferring between AWS storage services in different AWS Regions, one of the two locations must be in the Region where you're using DataSync.
+ You can't transfer across Regions with an NFS, SMB, HDFS, or object storage location. In these situations, both of your transfer locations must be in the same Region where you [activate your DataSync agent](activate-agent.md).
+ With AWS GovCloud (US) Regions, you can:
  + Transfer between the AWS GovCloud (US-East) and AWS GovCloud (US-West) Regions.
  + Transfer between an AWS GovCloud (US) Region and commercial AWS Region, such as US East (N. Virginia). This type of transfer requires an [agent](agent-requirements.md) when transferring between Amazon EFS or Amazon FSx file systems.

**Important**  
You pay for data transferred between AWS Regions. This transfer is billed as data transfer out from the source to destination Region. For more information, see [AWS DataSync Pricing](https://aws.amazon.com/datasync/pricing/).

## Determining if your transfer requires a DataSync agent
<a name="datasync-transfer-requirements"></a>

Depending on your transfer scenario, you might need a DataSync agent. For more information, see [Do I need an AWS DataSync agent?](do-i-need-datasync-agent.md)
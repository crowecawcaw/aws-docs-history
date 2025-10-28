# Amazon EBS volumes

Set the default Amazon EBS volume type used by the replication servers,
whether to use Amazon EBS encryption, and whether to automatically replicate newly added disks.

## Amazon EBS volume type

Each disk has minimum and maximum sizes and varying performance metrics and
pricing. Learn more about Amazon EBS volume types in [this Amazon EBS article](../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md "../../../AWSEC2/latest/UserGuide/EBSVolumeTypes.md"). The best practice is to not change the
default **Auto volume type selection** volume
type, unless there is a business need for doing so.

Choose the default **Amazon EBS volume type** to
be used by the replication servers for large disks:

- With **Auto volume type selection** the service
  dynamically switches between
  performance/cost optimized volume type according to the replicated disk write throughput.

###### Note

This option only affects disks over 125 GiB (by default, smaller disks always use
Magnetic HDD volumes).

- The default
  **Lower cost, Throughput Optimized HDD (st1)**
  option utilizes slower, less expensive disks.

You may want to use this option if:

    + You want to keep costs low
    + Your large disks do not change frequently
    + You are not concerned with how long the Initial Sync process
     takes

- The **Faster, General Purpose SSD (gp2)** and
  Faster, **General Purpose SSD (gp3)** options
  utilizes faster, but more expensive disks.

You may want to use this option if:

    + Your source server has disks with a high write rate or if you want faster performance in
     general
    + You want to speed up the initial sync process
    + You are willing to pay more for speed

###### Note

You can customize the Amazon EBS volume type used by each disk within each source server
in that source server's settings. [Learn more about changing
individual source server volume types](disk-settings.md "disk-settings.md").

## Amazon EBS encryption

Choose your encryption approach:

- When you choose **Default**, the default key is
  used. This can be an EBS-managed key or a customer-managed key. This option encrypts
  your replicated data at rest on the staging area subnet disks and the replicated disks.
- Choose **Custom** and then enter the ARN or
  key ID of a customer-managed key from your account or another AWS account in the **EBS encryption key** field. Enter
  the key, such as a cross-account KMS key, in standard key ID
  format. For example, KMS key format is `123abcd-12ab-34cd-56ef-1234567890ab)`. This option encrypts
  your replicated data at rest on the staging area subnet disks and the replicated disks.
- Choose **Create an AWS KMS
  key** to be redirected to the Key Management Service (KMS)
  Console where you can create a new key to use.

Learn more about EBS Volume Encryption in [Amazon EBS
encyption](../../../AWSEC2/latest/UserGuide/EBSEncryption.md "../../../AWSEC2/latest/UserGuide/EBSEncryption.md").

###### Important

Changing the encryption option after data replication has started causes
data replication to start from the beginning.

## Automatic replication of new disks

AWS Elastic Disaster Recovery (AWS DRS) allows you to automatically replicate newly added disks.
When you add new disks to your source environment AWS DRS initiates data replication
to the staging area subnet in your AWS account.

Automating replication of new disks assists you in maintaining continuous data
replication, saves time and resources, and reduces the risk of data loss in the
event of a disruption.

This feature is activated automatically for newly added servers.

To deactivate or reactivate this feature for newly added servers:

- Under **Settings** on the left-hand
  navigation menu, choose **Default replication
  settings**.
- select **Edit**.
- Under **Volumes**, uncheck the
  **Automatically replicate new
  disks** checkbox.

To activate or deactivate or reactivate this feature for a specific
server:

- Go to the replication settings.
- select **Edit**.
- Under **Volumes**, uncheck the
  **Automatically replicate new
  disks** checkbox.

###### Note

- This feature is only supported for new agent versions (version 4.6
  or higher). For older versions, you must reinstall your agent to activate
  automatic replication of new disks.
- Auto replication of new disks is not supported with
  --force-volumes.
- It might take up to 10 minutes for new disks to start
  replicating.
- New disks are only replicated once the feature is activated and
  are not replicated retroactively.

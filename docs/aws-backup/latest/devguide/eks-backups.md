# Amazon EKS backups

An Amazon Elastic Kubernetes Service (Amazon EKS) cluster consists of multiple resources that you can back up as a single unit. When you back up an Amazon EKS cluster, AWS Backup creates a composite recovery point that includes both EKS cluster state and persistent volume backups.

When an Amazon EKS cluster is backed up, recovery points are created for the Amazon EKS cluster state and persistent volumes supported by AWS Backup. These recovery points are grouped together within an overarching recovery point called a **composite**.

There are two distinct components of an Amazon EKS backup:

- _Amazon EKS Cluster State:_ This is a backup of the Amazon EKS cluster state. See Amazon EKS backup terminology below for what is included.
- _Persistent Storage:_ This is a backup of persistent storage (Amazon EBS, Amazon S3, Amazon Elastic File System) attached to the Amazon EKS cluster via Persistent Volume Claims and [supported by EKS Add Ons CSI Driver](../../../eks/latest/userguide/storage.md "../../../eks/latest/userguide/storage.md").

## Amazon EKS backup terminology

The following terms are used throughout the Amazon EKS backup documentation. For Amazon EKS Specific terminology, please refer to [Amazon EKS Documentation](../../../eks/latest/userguide/getting-started.md "../../../eks/latest/userguide/getting-started.md").

- **Composite recovery point** – A recovery point used to group nested recovery points together for an Amazon EKS cluster backup.
- **Nested recovery point** – A recovery point of a resource that is part of an Amazon EKS cluster and is backed up as part of the composite recovery point.
- **EKS Cluster State** – The Kubernetes manifests (YAML or JSON files) that define the desired state of Kubernetes resources in your cluster. This includes Kubernetes resources and deployments such as: secrets, config maps, stateful sets, DaemonSets, storage classes, storage maps, replica sets, persistent volume claims, custom resource definitions, roles, and role bindings.
- **Amazon EKS Cluster Configuration Child Recovery Point** – Contains Amazon EKS cluster state.
- **Persistent Volume Child Recovery Points** – Contains persistent volume backups for supported storage types (EBS, S3, EFS) [supported by EKS Add Ons CSI Driver](../../../eks/latest/userguide/storage.md "../../../eks/latest/userguide/storage.md").

## Amazon EKS backup structure

**Amazon EKS backups include the following components:**

- Amazon EKS Cluster State
- Persistent Storage: Backups of supported storage types including Amazon EBS, Amazon EFS, and Amazon S3

**Amazon EKS Backups will not include the following components:**

- Container images from external repositories (ECR, Docker)
- EKS cluster infrastructure components (e.g. VPCs, Subnets)
- Auto-generated EKS resources like nodes, auto-generated pods, events, leases, and jobs.

**EKS backup setup and prerequisites ("Before you backup")**

- **EKS Cluster Settings:**
  - EKS Cluster [authorization mode](../../../eks/latest/userguide/setting-up-access-entries.md "../../../eks/latest/userguide/setting-up-access-entries.md") set to API or API_AND_CONFIG_MAP for AWS Backup to create [Access Entries](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md") to access the EKS cluster.

- **Permissions:**
  - AWS Backup's managed policy [AWSBackupServiceRolePolicyForBackup](security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForBackup "security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForBackup") contains the required permissions to backup your Amazon EKS cluster and EBS and EFS persistent storage
  - If your EKS Cluster contains an S3 bucket you will need to ensure the following policies and prerequisites for your S3 bucket are added and enabled as documented:
    - [AWSBackupServiceRolePolicyForS3Backup](security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForS3Backup "security-iam-awsmanpol.md#AWSBackupServiceRolePolicyForS3Backup")
    - [Prerequisites for S3 Backups](s3-backups.md#s3-backup-prerequisites "s3-backups.md#s3-backup-prerequisites")

- **Encryption:**
  - Amazon EKS child recovery points will be encrypted with the Amazon KMS key set of the target Backup Vault
  - Persistent Storage recovery points will be encrypted as per the current support for each storage class: EBS Snapshots, S3 Backups, EFS Backups. [See Encryption for backups in AWS Backup](encryption.md "encryption.md")

## Create an Amazon EKS backup

The process of a backup creation is called a backup job. An Amazon EKS cluster backup job has a
status. When a backup job has finished, it has the status of Completed.
This signifies a recovery point (a backup) has been created.

### Creating an on-demand Amazon EKS backup

Console
To create an on-demand backup of your Amazon EKS cluster:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com//backup "https://console.aws.amazon.com//backup").
2. In the navigation pane, choose **Protected resources**.
3. Under **Resource type**, select **Amazon EKS**.
4. Select the checkbox next to the Amazon EKS cluster you want to back up.
5. Choose **Create on-demand backup**.
6. Configure your backup settings, including backup window, transition to cold storage, and retention period.
7. Choose **Create on-demand backup**.

AWS CLI
To create an on-demand backup of your Amazon EKS cluster using the AWS CLI:

Use the **start-backup-job** command:

```
aws backup start-backup-job \
                                  --backup-vault-name my-backup-vault \
                                  --resource-arn arn:aws:eks:us-west-2:123456789012:cluster/my-cluster \
                                  --iam-role-arn arn:aws:iam::123456789012:role/service-role \
                                  --region us-west-2
```

Optionally, specify additional parameters such as lifecycle settings:

```
aws backup start-backup-job \
                                  --backup-vault-name my-backup-vault \
                                  --resource-arn arn:aws:eks:us-west-2:123456789012:cluster/my-cluster \
                                  --iam-role-arn arn:aws:iam::123456789012:role/service-role \
                                  --lifecycle MoveToColdStorageAfterDays=30,DeleteAfterDays=365 \
                                  --region us-west-2
```

Monitor the backup job status:

```
aws backup describe-backup-job \
                                  --backup-job-id backup-job-id \
                                  --region us-west-2
```

## Amazon EKS backup ARN format

Composite Recovery Point arn:`partition`:backup:`region`:`accountId`:recovery-point:composite:eks/`cluster-name`-`timestamp`

Child Recovery Point arn:`partition`:backup:`region`:`accountId`:recovery-point:eks/`cluster-name`-`timestamp`

### Amazon EKS recovery points

#### Recovery point status

When the backup job of an Amazon EKS cluster is finished (the job status is `Completed`), a backup of the cluster has been created. This backup is also known as a composite recovery point. A composite recovery point can have one of the following statuses: `Completed`, `Failed`, or `Partial`.

Each Amazon EKS backup creates a parent backup job for the composite recovery point and child backup jobs for each child recovery point (cluster configuration and persistent volumes).

- A completed backup job means your entire Amazon EKS cluster and the resources within it are protected by AWS Backup.
- A failed status indicates that the backup job was unsuccessful; you should create the backup again once the issue that caused the failure is corrected.
- A `Partial` status means that not all the resources in the cluster were backed up. This may happen if one or more of the backup jobs belonging to resources within the cluster (nested resources) have statuses other than `Completed`. You can manually create an on-demand backup to rerun any resources that resulted in a status other than `Completed`.

Each nested resource within the composite recovery point has its own individual recovery point, each with its own status (either `Completed` or `Failed`). Nested recovery points with a status of `Completed` can be restored.

AWS Backup supports lifecycle transitions to cold storage for persistent volume recovery points. You can subscribe to notifications to receive alerts on backup job status.

## Manage recovery points

Composite recovery points (backups) can be copied; persistent volume child recovery points can be copied, deleted, disassociated, or restored. The Amazon EKS cluster state child recovery point cannot be copied, deleted, or disassociated as it maintains a 1:1 relationship with its parent composite recovery point.

A composite recovery point which contains nested backups cannot be deleted. After the nested recovery points within a composite recovery point have been deleted or disassociated, you can manually delete the composite recovery point manually or let it remain until the backup plan lifecycle deletes it.

### Delete a recovery point

You can delete a recovery point using the console or using the AWS CLI.

To delete recovery points using the console:

Open the AWS Backup console at [https://console.aws.amazon.com/backup/](https://console.aws.amazon.com//backup/home "https://console.aws.amazon.com//backup/home").

1. Click on Protected Resources in the left-hand navigation. In the text box, type EKS to display only your Amazon EKS clusters.
2. Composite recovery points will be displayed in the Recovery points pane. The plus sign (+) to the left of each recovery point ID can be clicked to expand each composite recovery point, showing all nested recovery points contained in the composite. You can check the box to the left of any recovery point to include it in your selection of recovery points you wish to delete.
3. Click the Delete button.

When you use the console to delete one or more composite recovery points, a warning box will pop up. This warning box requires you to confirm your intention to delete the composite recovery points, including nested recovery points within composite stacks.

To delete recovery points using API, use the DeleteRecoveryPoint command.

When you use API with the AWS Command Line Interface you must delete all nested recovery points prior to deleting a composite point.

### Disassociate a nested recovery point from composite recovery point

You can disassociate a nested recovery point from a composite recovery point (for example, you wish to keep the nested recovery point but delete the composite recovery point). Both recovery points will remain, but they will no longer be connected; that is, actions that occur on the composite recovery point will no longer apply to the nested recovery point once it has been disassociated. The Amazon EKS cluster state child recovery point cannot be disassociated as it maintains a 1:1 relationship with its parent composite recovery point.

You can disassociate the recovery point using the console, or you can call the API DisassociateRecoveryPointFromParent.

## Copy a recovery point

You can copy a composite recovery point, or you can copy a nested recovery point if the resource supports [cross-account and cross-Region copy](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").

To copy recovery points using the AWS Backup console:

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com//backup "https://console.aws.amazon.com//backup").
2. Click on **Protected Resources** in the left-hand navigation. In the text box, type `EKS` to display only your Amazon EKS clusters.
3. Composite recovery points will be displayed in the Recovery points pane. The plus sign (+) to the left of each recovery point ID can be clicked to expand each composite recovery point, showing all nested recovery points contained in the composite. You can click the radial circle button to the left of any recovery point to copy it.
4. Once it is selected, click the **Copy** button in the top-right corner of the pane.

Amazon EKS backups support all copy types:

- Same region/account
- Cross account
- Cross region
- Opt-in regions

## Limitations

- Persistent volumes using a CSI Driver via CSI migration, in-tree storage plugins or ACK controllers are not supported.
- Amazon S3 buckets with specific prefixes attached to CSI Driver MountPoints cannot be backed up. Only Amazon S3 buckets as targets are supported, not specific prefixes
- Amazon S3 bucket backups as part of an EKS cluster backup will only support snapshot backups.
- Amazon FSx via CSI driver is not supported via EKS Backups
- Subject to [backup and restore quotas](aws-backup/latest/devguide/aws-backup-limits.md "aws-backup/latest/devguide/aws-backup-limits.md")

## Frequently Asked Questions

1. _"What is included as part of the Amazon EKS backup?"_

As part of each backup of an Amazon EKS cluster, the Amazon EKS cluster state and persistent volumes
supported by AWS Backup are backed up. The Amazon EKS cluster state includes details like cluster name,
IAM role, Amazon VPC configuration, network settings, logging, encryption, add-ons, access entries,
managed node groups, Fargate profiles, pod identity associations, and Kubernetes manifest files. 2. _"Does a `Partial` status mean the creation of my backup failed?"_

No. A partial status indicates that some of the recovery points were backed up, while some were not.
There are two conditions to check if you were expecting a `Completed` backup result:

    1. One or more of the backup jobs belonging to resources within the cluster were not
     successful and the job has to be rerun.
    2. A nested recovery point was deleted or disassociated from the composite recovery point.

3. _"Do I need to have an agent or Amazon EKS Add-on installed on my Amazon EKS cluster before backup?"_

No. AWS Backup does not require any agents or add-ons to be installed on your Amazon EKS cluster. The only
pre-requisite is to have your EKS Cluster's [authorization mode](../../../eks/latest/userguide/setting-up-access-entries.md "../../../eks/latest/userguide/setting-up-access-entries.md")
set to API or API_AND_CONFIG_MAP for AWS Backup to create [Access Entries](../../../eks/latest/userguide/access-entries.md "../../../eks/latest/userguide/access-entries.md")
to access the EKS cluster. 4. _"Does Amazon EKS Backups include Amazon EKS infrastructure components or Amazon ECR images?"_

No. Amazon EKS backups focus on the EKS cluster state and application workloads, not the underlying
infrastructure components or container images. 5. _"Can I lifecycle my EKS Composite Recovery Point to cold storage?"_

You can transition to cold storage for underlying child recovery points that support cold storage tiers.
See the [AWS Backup feature availability matrix](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource")
for full list of support. 6. _"Are my EKS backups incremental?"_

AWS Backup will take incremental backups of each child recovery point where supported today, this includes
EBS volumes, EFS Filesystems and S3 buckets. The EKS cluster state child recovery point will be a full
backup. See the [AWS Backup feature availability matrix](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource"). 7. _"Can I create an index and search my EKS backups?"_

No, however you can create on-demand indexes and search persistent volumes where the underlying
storage type supports this capability through AWS Backup. See the [AWS Backup feature availability matrix](backup-feature-availability.md#features-by-resource "backup-feature-availability.md#features-by-resource").

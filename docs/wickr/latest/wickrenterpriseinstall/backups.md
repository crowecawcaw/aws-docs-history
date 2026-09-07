

This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide/what-is-wickr.html) or [AWS Wickr User Guide](https://docs.aws.amazon.com/wickr/latest/userguide/what-is-wickr.html).

# Backups
<a name="backups"></a>

Wickr Enterprise utilizes Velero for Backup purposes. Velero provides the necessary tools for backing up and restoring Kubernetes cluster resources and persistent volumes, whether operating on a cloud provider or on-premises.

**Velero backups with Minio**: Currently Velero backups are only enabled for Minio in Low Resource Mode. 

![Velero installation image.](http://docs.aws.amazon.com/wickr/latest/wickrenterpriseinstall/images/wickr-enterprise-velero.png)


## Installation using Velero documentation
<a name="installation-using-velero-doc"></a>
+ Install the Velero CLI. For more information, see [Installing the Velero CLI](https://docs.replicated.com/enterprise/snapshots-velero-cli-installing).
+ Install Velero on your cluster and configure storage based on your provider:
  + [AWS](https://velero.io/docs/v1.0.0/aws-config/).
  + [GCP](https://velero.io/docs/v1.0.0/gcp-config/).
  + [Azure](https://velero.io/docs/v1.0.0/azure-config/).
  + [Other providers](https://velero.io/docs/v1.10/supported-providers/).

### Limitation
<a name="limitation"></a>

By default, no volumes are included in the backup. If any pods mount a volume that should be backed up, you must configure the backup with an annotation listing the specific volumes to include in the backup.

For each volume that requires a backup, add the backup.velero.io/backup-volumes annotation. The annotation name is backup.velero.io/backup-volumes and the value is a comma separated list of volumes to include in the backup. For more information, see [Configure Snapshots](https://docs.replicated.com/vendor/snapshots-configuring-backups).
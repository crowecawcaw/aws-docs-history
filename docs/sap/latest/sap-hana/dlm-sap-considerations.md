# Considerations

Only the following configurations are supported.

- SAP HANA 2.0 SPS 05 and later with multi-tenant configuration.
- Single SAP HANA databases. Multiple SAP HANA Systems on One Host (MCOS) is not supported.
- SAP HANA scale-out systems are not supported.

###### Supported Regions

You can automate the creation and retention of application-consistent snapshots of your SAP HANA workloads using Amazon Data Lifecycle Manager in all [AWS Regions where AWS Systems Manager for SAP is available](../../../general/latest/gr/ssm-sap.md "../../../general/latest/gr/ssm-sap.md").

- Ensure that the EBS snapshot you use for the restore has fast snapshot restore in the `enabled` state for the required Availability Zone.
- It takes 60 minutes per TiB to enable a snapshot for fast snapshot restore after the snapshot reaches the `COMPLETED` state.
- Ensure that the snapshot has enough [volume creation credits](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md#volume-creation-credits "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md#volume-creation-credits") to restore volumes with the full performance benefit of fast snapshot restore.
- Ensure that you have sufficient [fast snapshot restore quota](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md#limits "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md#limits") in your account and Region to meet your recovery needs. The total quota required depends on several factors, including the number of volumes supporting the SAP HANA database, the snapshot creation frequency, and the snapshot retention period.
- You can use [Amazon CloudWatch metrics](../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md#fast-snapshot-restore-metrics "../../../AWSEC2/latest/UserGuide/using_cloudwatch_ebs.md#fast-snapshot-restore-metrics") and [Amazon EventBridge events](../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#fast-snapshot-restore-events "../../../AWSEC2/latest/UserGuide/ebs-cloud-watch-events.md#fast-snapshot-restore-events") to monitor the fast snapshot restore state for a snapshot.
- We recommend that you do not use the SSM document for SAP HANA without Amazon Data Lifecycle Manager. Doing this will result in EBS snapshots that are not managed by Amazon Data Lifecycle Manager.
- It is your responsibility to ensure that the SAP HANA database is prepared to create snapshots and that it has at least 2 percent available memory and CPU resources. Otherwise, Amazon Data Lifecycle Manager will not initiate the instructions to freeze I/O and to create the application-consistent EBS snapshots.
- The time required to complete snapshot creation depends on several factors, including the amount of data that has changed since the last snapshot of the EBS volume.
- The time it takes to restore a SAP HANA database from EBS snapshots will be impacted by the [initialization of EBS volumes](../../../AWSEC2/latest/UserGuide/ebs-initialize.md#ebs-initialize-linux "../../../AWSEC2/latest/UserGuide/ebs-initialize.md#ebs-initialize-linux"). You can use [fast snapshot restore](../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md "../../../AWSEC2/latest/UserGuide/ebs-fast-snapshot-restore.md") to ensure that the EBS volumes created from the EBS snapshot are fully-initialized at creation and instantly deliver all of their provisioned performance.
- If you choose to not use fast snapshot restore, you can manually [initialize the EBS volume](../../../AWSEC2/latest/UserGuide/ebs-initialize.md#ebs-initialize-linux "../../../AWSEC2/latest/UserGuide/ebs-initialize.md#ebs-initialize-linux") after creation. However, this can take several minutes or up to several hours, depending on your EC2 instance bandwidth, the IOPS provisioned for the volume, and the size of the volume.
- You can verify that application-consistent EBS snapshots of your SAP HANA workloads were successfully created by reviewing the snapshot tags, the emitted Amazon CloudWatch metrics, and the emitted Amazon EventBridge events. For more information see [Identifying snapshots created with pre and post scripts](../../../AWSEC2/latest/UserGuide/dlm-script-tags.md "../../../AWSEC2/latest/UserGuide/dlm-script-tags.md") and [Monitoring pre and post script execution](../../../AWSEC2/latest/UserGuide/dlm-script-monitoring.md "../../../AWSEC2/latest/UserGuide/dlm-script-monitoring.md").

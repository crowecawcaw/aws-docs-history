

# SageMaker HyperPod cluster events reference
<a name="sagemaker-hyperpod-cluster-events-reference"></a>

This page provides a complete reference of all structured events emitted by Amazon SageMaker HyperPod clusters. Events provide visibility into cluster, instance group, and instance-level operations including provisioning, scaling, patching, and orchestrator-specific lifecycle changes.

Cluster events are available for HyperPod clusters with `NodeProvisioningMode` set to `Continuous`. Events are accessible through the `ListClusterEvents` and `DescribeClusterEvent` APIs, the SageMaker AI console **Events** tab, and Amazon EventBridge.

## Cluster event record
<a name="sagemaker-hyperpod-cluster-events-record"></a>

Each cluster event is represented as a structured record containing identification, timing, scope, severity, and operation-specific metadata. The following example shows a complete event record as delivered through the `DescribeClusterEvent` API and Amazon EventBridge:

```
{
  "version": "0",
  "id": "0bd4a141-0a02-9d8a-f977-3924c3fb259c",
  "detail-type": "SageMaker HyperPod Cluster Event",
  "source": "aws.sagemaker",
  "account": "111122223333",
  "time": "2026-06-01T17:20:25Z",
  "region": "us-west-2",
  "resources": [
    "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster"
  ],
  "detail": {
    "EventDetails": {
      "EventId": "83ea0bb5-be77-45e8-a458-0a87f778a205",
      "ClusterArn": "arn:aws:sagemaker:us-west-2:111122223333:cluster/sample-cluster",
      "ClusterName": "sample-cluster",
      "InstanceGroupName": "p5Inst",
      "InstanceId": "i-0391f86fa0fe0d465",
      "ResourceType": "Instance",
      "EventTime": 1748794825350,
      "EventLevel": "Error",
      "Description": "Instance creation in Cluster sample-cluster and InstanceGroup p5Inst failed",
      "EventDetails": {
        "EventMetadata": {
          "Instance": {
            "FailureMessage": "We currently do not have sufficient capacity to launch new ml.p5.48xlarge instances. Please try again.",
            "NodeLogicalId": "df268d19-f035-4f28-9b80-b956b92ae21e"
          }
        }
      }
    }
  }
}
```

### Event record fields
<a name="sagemaker-hyperpod-cluster-events-record-fields"></a>

The `detail.EventDetails` object contains the following fields:


| Field | Type | Required | Description | 
| --- | --- | --- | --- | 
| EventId | String (UUID) | Yes | Unique identifier for the event. | 
| ClusterArn | String | Yes | ARN of the HyperPod cluster. | 
| ClusterName | String | Yes | Name of the HyperPod cluster. | 
| EventTime | Timestamp | Yes | When the event occurred (epoch milliseconds). | 
| ResourceType | String | Yes | Scope of the event: Cluster, InstanceGroup, or Instance. | 
| EventLevel | String | Yes | Severity classification: Info, Warn, or Error. | 
| Description | String | No | Human-readable summary of the event. | 
| InstanceGroupName | String | No | Instance group name (present when ResourceType is InstanceGroup or Instance). | 
| InstanceId | String | No | EC2 instance ID (present when ResourceType is Instance). | 
| EventDetails | Object | No | Additional metadata specific to the resource type and operation. | 

### Event levels
<a name="sagemaker-hyperpod-cluster-events-levels"></a>


| Level | Meaning | 
| --- | --- | 
| Info | Operation completed successfully or is progressing normally. | 
| Warn | Operation completed with a non-critical issue or a condition that may require future attention. | 
| Error | Operation failed or requires immediate attention. | 

### Resource types
<a name="sagemaker-hyperpod-cluster-events-resource-types"></a>


| ResourceType | Scope | Example events | 
| --- | --- | --- | 
| Cluster | Whole-cluster operations | Cluster creation/update started, cluster operation failed | 
| InstanceGroup | Instance group operations | Scaling started/completed, patching scheduled, FSx lifecycle | 
| Instance | Individual instance operations | EC2 provisioning, lifecycle script execution, ENI management, termination | 

### EventDetails metadata
<a name="sagemaker-hyperpod-cluster-events-metadata"></a>

Cluster events include an `EventMetadata` object within the `EventDetails` field that provides operation-specific context beyond what the event description conveys. The contents of `EventMetadata` vary by resource type and event type. For the complete schema and supported fields, see [EventMetadata](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_EventMetadata.html) in the Amazon SageMaker AI API Reference.

### EventBridge envelope fields
<a name="sagemaker-hyperpod-cluster-events-eventbridge-envelope"></a>

When delivered through Amazon EventBridge, the event record is wrapped in the standard EventBridge envelope:


| Field | Description | 
| --- | --- | 
| version | EventBridge schema version (always "0"). | 
| id | Unique EventBridge event ID. | 
| detail-type | SageMaker HyperPod Cluster Event | 
| source | aws.sagemaker | 
| account | AWS account ID that owns the cluster. | 
| time | ISO 8601 timestamp of the event. | 
| region | AWS Region where the cluster resides. | 
| resources | Array containing the cluster ARN. | 
| detail | Contains the EventDetails object described above. | 

## Common events (EKS and Slurm)
<a name="sagemaker-hyperpod-cluster-events-common"></a>

The following events are emitted for all HyperPod clusters regardless of orchestrator. The **Description** column shows the value of the `Description` field in the event record as it appears in the API response and the console **Events** tab.

### Cluster lifecycle
<a name="sagemaker-hyperpod-cluster-events-common-cluster"></a>


| Event | Description | 
| --- | --- | 
| Cluster operation started | Cluster <cluster-name> <operation> started successfully | 
| Cluster operation start failed | Failed to start Cluster <cluster-name> <operation> | 
| Cluster operation completed | Cluster <cluster-name> <operation> completed successfully | 
| Cluster operation failed | Cluster <cluster-name> <operation> failed | 

### Instance group lifecycle
<a name="sagemaker-hyperpod-cluster-events-common-ig"></a>


| Event | Description | 
| --- | --- | 
| Instance group operation started | InstanceGroup <instance-group-name> <operation> started successfully in Cluster <cluster-name> | 
| Instance group operation start failed | Failed to start InstanceGroup <instance-group-name> <operation> in Cluster <cluster-name> | 
| Instance group operation completed | Instance Group <instance-group-name> <operation> in Cluster <cluster-name> completed successfully | 
| Instance group operation failed | Instance Group <instance-group-name> <operation> in Cluster <cluster-name> failed | 

### Instance group network configuration
<a name="sagemaker-hyperpod-cluster-events-common-network"></a>


| Event | Description | 
| --- | --- | 
| Network configuration found | Found Subnet <subnet-id> in AZ <availability-zone> with SecurityGroupIds <security-group-ids> for IG <instance-group-name> in Cluster <cluster-name> | 
| Network configuration failed | Failed to process Instance Group Network Configuration details for IG <instance-group-name> in Cluster <cluster-name> | 
| Custom AMI override found | Found Custom AMI Override <ami-id> for IG <instance-group-name> in Cluster <cluster-name> | 
| Custom AMI override failed | Failed to process Custom AMI Override details for IG <instance-group-name> in Cluster <cluster-name> | 
| Platform network configuration used | Using HyperPod Platform provided network configuration for IG <instance-group-name> in Cluster <cluster-name> | 
| Network configuration determined | Instance Group network configuration successfully determined for IG <instance-group-name> in Cluster <cluster-name> | 

### Instance creation
<a name="sagemaker-hyperpod-cluster-events-common-instance-creation"></a>


| Event | Description | 
| --- | --- | 
| Instance operation started | Instance <operation> started successfully in Cluster <cluster-name> and IG <instance-group-name> | 
| Instance operation start failed | Failed to start Instance <operation> in Cluster <cluster-name> and IG <instance-group-name> | 
| Capacity reservation found | Found CapacityReservation ID <reservation-id> for Cluster <cluster-name> and IG <instance-group-name>, using reserved capacity | 
| Capacity reservation not found | No CapacityReservation found for Cluster <cluster-name> and IG <instance-group-name>, using on-demand pool | 
| Instance payload setup failed | Failed to process CapacityReservationDetails for Cluster <cluster-name> and IG <instance-group-name> | 
| Customer ENI created | Successfully created Customer ENI for instance in Cluster <cluster-name> and IG <instance-group-name> | 
| Customer ENI creation failed | Failed to create Customer ENI for instance in Cluster <cluster-name> and IG <instance-group-name> | 
| EC2 instance provisioned | EC2 Instance <instance-id> successfully provisioned in Cluster <cluster-name> and IG <instance-group-name> | 
| EC2 instance creation failed | Failed to provision EC2 Instance in Cluster <cluster-name> and IG <instance-group-name> | 
| Lifecycle script status updated | Instance lifecycle script execution for EC2 Instance <instance-id> has <status> | 
| Lifecycle script status update failed | Failed to update Instance lifecycle script execution status for EC2InstanceId <instance-id> | 
| Instance creation failed with lifecycle logs | Instance lifecycle script execution for EC2 Instance <instance-id> has Failed. To view lifecycle script logs, visit log group... | 
| Unused ENI cleanup succeeded | Successfully deleted unused Customer ENIs for EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 
| Unused ENI cleanup failed | Failed to delete unused Customer ENIs for EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 

### Instance deletion
<a name="sagemaker-hyperpod-cluster-events-common-instance-deletion"></a>


| Event | Description | 
| --- | --- | 
| EC2 instance termination in progress | Termination of EC2 Instance <instance-id> is currently in progress in Cluster <cluster-name> and IG <instance-group-name> | 
| EC2 instance termination failed | Failed to terminate EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 
| Customer ENI deleted | Customer ENI successfully deleted for EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 
| Customer ENI deletion failed | Failed to delete Customer ENI for EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 

### Instance reboot
<a name="sagemaker-hyperpod-cluster-events-common-instance-reboot"></a>


| Event | Description | 
| --- | --- | 
| EC2 instance reboot in progress | Reboot of EC2 Instance <instance-id> is currently in progress on Cluster <cluster-name> and IG <instance-group-name> | 
| EC2 instance reboot request failed | Failed to submit reboot request for EC2 Instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 

### Instance operation (generic)
<a name="sagemaker-hyperpod-cluster-events-common-instance-operation"></a>


| Event | Description | 
| --- | --- | 
| Instance operation completed | Instance <operation> <instance-id> in Cluster <cluster-name> and IG <instance-group-name> completed successfully | 
| Instance operation failed | Instance <operation> <instance-id> in Cluster <cluster-name> and IG <instance-group-name> failed | 

### Instance replacement
<a name="sagemaker-hyperpod-cluster-events-common-instance-replacement"></a>


| Event | Description | 
| --- | --- | 
| Instance replacement started | Instance <instance-id> is starting as part of instance replacement in Cluster <cluster-name> and IG <instance-group-name> | 
| Instance replacement start failed | Instance <instance-id> failed to start as part of instance replacement in Cluster <cluster-name> and IG <instance-group-name> | 
| Instance replacement completed | Instance <instance-id> <operation> completed successfully as part of instance replacement in Cluster <cluster-name> and IG <instance-group-name> | 
| Instance replacement failed | Instance <instance-id> <operation> failed as part of instance replacement in Cluster <cluster-name> and IG <instance-group-name> | 

### FSx filesystem lifecycle
<a name="sagemaker-hyperpod-cluster-events-common-fsx"></a>


| Event | Description | 
| --- | --- | 
| FSx creation started | FSx creation started for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx creation failed | Failed to create FSx for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx creation completed | FSx creation successfully completed for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx deletion started | FSx deletion started for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx deletion failed | Failed to delete FSx for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx deletion completed | FSx deletion successfully completed for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx update started | FSx update started for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx update failed | Failed to update FSx for IG <instance-group-name> in Cluster <cluster-name> | 
| FSx update completed | FSx update successfully completed for IG <instance-group-name> in Cluster <cluster-name> | 

### Patching (common steps)
<a name="sagemaker-hyperpod-cluster-events-common-patching"></a>

These patching events are emitted for both EKS and Slurm clusters during `UpdateClusterSoftware` operations.


| Event | Description | 
| --- | --- | 
| Instance group patching scheduled | InstanceGroup <instance-group-name> in Cluster <cluster-name> has been scheduled for UpdateClusterSoftware to latest. | 
| Instance group patching schedule failed | Failed to schedule UpdateClusterSoftware for IG <instance-group-name> in Cluster <cluster-name>. | 
| Instance group patching started | UpdateClusterSoftware initiated for IG <instance-group-name> in Cluster <cluster-name> using <strategy> strategy. | 
| Instance group patching start failed | Failed to initiate UpdateClusterSoftware for IG <instance-group-name> in Cluster <cluster-name>. | 
| Next patching batch selected | Next update batch selected for IG <instance-group-name> in Cluster <cluster-name>. | 
| Next patching batch selection failed | Failed to select the next update batch for IG <instance-group-name> in Cluster <cluster-name>. | 
| Failed instances queued for replacement | Failed instances in IG <instance-group-name> in Cluster <cluster-name> queued for node replacement. | 
| Failed instance replacement queueing failed | Failed to queue instances for node replacement in IG <instance-group-name> in Cluster <cluster-name>. | 
| Instance group patching completed | UpdateClusterSoftware completed successfully for IG <instance-group-name> in Cluster <cluster-name>. | 
| Instance group patching completion failed | Failed to complete UpdateClusterSoftware for IG <instance-group-name> in Cluster <cluster-name>. | 
| Root volume replacement started | Root volume replacement started for Instance <instance-id> in IG <instance-group-name>. | 
| Root volume replacement failed | Failed to start root volume replacement for Instance <instance-id> in IG <instance-group-name>. | 
| Instance patching succeeded | Instance <instance-id> in IG <instance-group-name> updated successfully. | 

## EKS-specific events
<a name="sagemaker-hyperpod-cluster-events-eks"></a>

The following events are emitted only for HyperPod clusters orchestrated with Amazon EKS.

### Access entry management
<a name="sagemaker-hyperpod-cluster-events-eks-access"></a>


| Event | Description | 
| --- | --- | 
| SLR access entry operation succeeded | SLR Access Entry <operation> successful for Cluster <cluster-name> | 
| SLR access entry operation failed | SLR Access Entry <operation> failed for Cluster <cluster-name> | 
| EKS access entries operation succeeded | EKS Access Entries <operation> successful for Cluster <cluster-name> | 
| EKS access entries operation failed | EKS Access Entries <operation> failed for Cluster <cluster-name> | 

### Kubernetes configuration updates
<a name="sagemaker-hyperpod-cluster-events-eks-k8s"></a>


| Event | Description | 
| --- | --- | 
| Kubernetes config update succeeded | Successfully updated Kubernetes config for instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 
| Kubernetes config update failed | Failed to update Kubernetes config for instance <instance-id> in Cluster <cluster-name> and IG <instance-group-name> | 

### Karpenter autoscaling
<a name="sagemaker-hyperpod-cluster-events-eks-karpenter"></a>


| Event | Description | 
| --- | --- | 
| Autoscaling operation succeeded | AutoScaling <operation> <status> successfully in Cluster <cluster-name> | 
| Autoscaling operation failed | Failed to <operation> AutoScaling in Cluster <cluster-name> | 
| Karpenter CRD installation succeeded | CustomResourceDefinition installation completed successfully in EKS Cluster <cluster-name> | 
| Karpenter CRD installation failed | CustomResourceDefinition installation failed for EKS Cluster <cluster-name> | 
| Karpenter SLR access policy update succeeded | <operation> access policies with AmazonSageMakerHyperPodServiceRole access entry in EKS cluster <cluster-name> successfully | 
| Karpenter SLR access policy update failed | Failed to <operation> access policies with AmazonSageMakerHyperPodServiceRole access entry in EKS cluster <cluster-name> | 

### Patching — EKS instance-level
<a name="sagemaker-hyperpod-cluster-events-eks-patching-instance"></a>


| Event | Description | 
| --- | --- | 
| Instance patching preparation succeeded | Instance <instance-id> in IG <instance-group-name> cordoned and pods evicted. | 
| Instance patching skipped (PDB violation) | UpdateClusterSoftware for Instance <instance-id> in IG <instance-group-name> skipped due to PodDisruptionBudget constraint. | 
| Instance patching preparation failed | Failed to prepare instance <instance-id> in IG <instance-group-name> for UpdateClusterSoftware. | 
| Instance restored to schedulable state | Instance <instance-id> in IG <instance-group-name> restored to schedulable state. | 
| Instance restore to schedulable failed | Failed to restore instance <instance-id> in IG <instance-group-name> to schedulable state. | 

### Patching — EKS rollback
<a name="sagemaker-hyperpod-cluster-events-eks-patching-rollback"></a>


| Event | Description | 
| --- | --- | 
| Bake time started | Baking period started for IG <instance-group-name> in Cluster <cluster-name>. Monitoring alarms [<alarm-names>] for <duration> seconds. | 
| Bake time completed | Baking period completed for IG <instance-group-name> in Cluster <cluster-name>. No alarms triggered during the <duration>-second baking period. | 
| Bake time alarm triggered | Baking period failed for IG <instance-group-name> in Cluster <cluster-name>. Alarms [<alarm-names>] entered ALARM state. Initiating auto-rollback. | 
| Bake time evaluation failed | Failed to evaluate alarms during baking period for IG <instance-group-name> in Cluster <cluster-name>. | 
| Instance group patching rollback initiated | UpdateClusterSoftware failed for IG <instance-group-name> in Cluster <cluster-name>. Initiating rollback. | 
| Instance group patching rollback failed | Rollback failed for IG <instance-group-name> in Cluster <cluster-name>. Some instances may be in FailedMaintenance state. | 
| Instance patching rollback initiated | Instance <instance-id> in IG <instance-group-name> failed to update. Rollback initiated. | 
| Instance patching rollback succeeded | Instance <instance-id> in IG <instance-group-name> rolled back successfully to previous AMI. | 
| Instance patching rollback failed | UpdateClusterSoftware rollback failed for instance <instance-id> in IG <instance-group-name>. | 

## Slurm-specific events
<a name="sagemaker-hyperpod-cluster-events-slurm"></a>

The following events are emitted only for HyperPod clusters orchestrated with Slurm.


| Event | Description | 
| --- | --- | 
| Provisioning parameters found | Found provisioning\_parameters.json in LifeCycleScript S3 Path for controller group <instance-group-name> | 
| Provisioning parameters not found | No provisioning\_parameters.json found in LifeCycleScript S3 Path for controller group <instance-group-name> | 
| Slurm munge key created | Successfully created and stored munge key | 
| Slurm drift validation passed | Slurm configuration drift validation passed | 
| Slurm drift detected | Slurm configuration drift detected: <drift-details> | 
| Slurm cluster rollback completed | Cluster creation failed: controller and login nodes did not become ready within the expected time | 
| Slurm reconfiguration succeeded | Slurm was reconfigured successfully. Slurm config updated to match desired state | 

## EventBridge integration
<a name="sagemaker-hyperpod-cluster-events-eventbridge"></a>

HyperPod sends cluster events to Amazon EventBridge using three detail types:


| Detail type | Description | 
| --- | --- | 
| SageMaker HyperPod Cluster Event | Operational events for provisioning, scaling, patching, and orchestrator-specific operations. Includes EventLevel for severity filtering. | 
| SageMaker HyperPod Cluster State Change | Cluster-level status transitions (for example, Creating to InService). Includes full cluster configuration. | 
| SageMaker HyperPod Cluster Node Health Event | Health monitoring events from the HyperPod Health Monitoring Agent (HMA). Includes health status, reason, repair action, and recommendation. | 

### Event pattern examples
<a name="sagemaker-hyperpod-cluster-events-eventbridge-patterns"></a>

**All HyperPod cluster events:**

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker HyperPod Cluster Event"]
}
```

**Error events only (for alerting):**

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker HyperPod Cluster Event"],
  "detail": {
    "EventDetails": {
      "EventLevel": ["Error"]
    }
  }
}
```

**Events for a specific cluster:**

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker HyperPod Cluster Event"],
  "resources": ["arn:aws:sagemaker:us-west-2:111122223333:cluster/my-cluster-id"]
}
```

**Node health events:**

```
{
  "source": ["aws.sagemaker"],
  "detail-type": ["SageMaker HyperPod Cluster Node Health Event"]
}
```

## API reference
<a name="sagemaker-hyperpod-cluster-events-api-reference"></a>
+ [ListClusterEvents](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListClusterEvents.html) — List events with filtering, sorting, and pagination
+ [DescribeClusterEvent](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeClusterEvent.html) — Get full details for a specific event
+ [ClusterEventSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterEventSummary.html) — Event summary data type
+ [ClusterEventDetail](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterEventDetail.html) — Event detail data type

## See also
<a name="sagemaker-hyperpod-cluster-events-see-also"></a>
+ [SageMaker HyperPod Slurm cluster events](sagemaker-hyperpod-cluster-events-slurm-page.md) — Slurm cluster events with CLI usage and common scenarios
+ [SageMaker HyperPod EKS cluster events](sagemaker-hyperpod-cluster-events-eks-page.md) — EKS cluster events with CLI usage and common scenarios
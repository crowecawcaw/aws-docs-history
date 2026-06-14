# SageMaker HyperPod cluster events reference

This page provides a complete reference of all structured events emitted by
Amazon SageMaker HyperPod clusters. Events provide visibility into cluster, instance group, and
instance-level operations including provisioning, scaling, patching, and
orchestrator-specific lifecycle changes.

Cluster events are available for HyperPod clusters with
`NodeProvisioningMode` set to `Continuous`. Events are accessible
through the `ListClusterEvents` and `DescribeClusterEvent` APIs, the
SageMaker AI console **Events** tab, and Amazon EventBridge.

## Cluster event record

Each cluster event is represented as a structured record containing identification,
timing, scope, severity, and operation-specific metadata. The following example shows a
complete event record as delivered through the `DescribeClusterEvent` API and
Amazon EventBridge:

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

The `detail.EventDetails` object contains the following fields:

| Field               | Type          | Required | Description                                                                               |
| ------------------- | ------------- | -------- | ----------------------------------------------------------------------------------------- |
| `EventId`           | String (UUID) | Yes      | Unique identifier for the event.                                                          |
| `ClusterArn`        | String        | Yes      | ARN of the HyperPod cluster.                                                              |
| `ClusterName`       | String        | Yes      | Name of the HyperPod cluster.                                                             |
| `EventTime`         | Timestamp     | Yes      | When the event occurred (epoch milliseconds).                                             |
| `ResourceType`      | String        | Yes      | Scope of the event: `Cluster`,<br>`InstanceGroup`, or<br>`Instance`.                      |
| `EventLevel`        | String        | Yes      | Severity classification: `Info`,<br>`Warn`, or `Error`.                                   |
| `Description`       | String        | No       | Human-readable summary of the event.                                                      |
| `InstanceGroupName` | String        | No       | Instance group name (present when<br>`ResourceType` is `InstanceGroup`<br>or `Instance`). |
| `InstanceId`        | String        | No       | EC2 instance ID (present when `ResourceType`<br>is `Instance`).                           |
| `EventDetails`      | Object        | No       | Additional metadata specific to the resource type and<br>operation.                       |

### Event levels

| Level   | Meaning                                                                                            |
| ------- | -------------------------------------------------------------------------------------------------- |
| `Info`  | Operation completed successfully or is progressing<br>normally.                                    |
| `Warn`  | Operation completed with a non-critical issue or a condition<br>that may require future attention. |
| `Error` | Operation failed or requires immediate attention.                                                  |

### Resource types

| ResourceType    | Scope                          | Example events                                                               |
| --------------- | ------------------------------ | ---------------------------------------------------------------------------- |
| `Cluster`       | Whole-cluster operations       | Cluster creation/update started, cluster operation<br>failed                 |
| `InstanceGroup` | Instance group operations      | Scaling started/completed, patching scheduled, FSx<br>lifecycle              |
| `Instance`      | Individual instance operations | EC2 provisioning, lifecycle script execution, ENI<br>management, termination |

### EventDetails metadata

Cluster events include an `EventMetadata` object within the
`EventDetails` field that provides operation-specific context
beyond what the event description conveys. The contents of
`EventMetadata` vary by resource type and event type. For the
complete schema and supported fields, see [EventMetadata](../APIReference/API_EventMetadata.md "../APIReference/API_EventMetadata.md") in the Amazon SageMaker AI API Reference.

### EventBridge envelope fields

When delivered through Amazon EventBridge, the event record is wrapped in the
standard EventBridge envelope:

| Field         | Description                                            |
| ------------- | ------------------------------------------------------ |
| `version`     | EventBridge schema version (always<br>`"0"`).          |
| `id`          | Unique EventBridge event ID.                           |
| `detail-type` | `SageMaker HyperPod Cluster Event`                     |
| `source`      | `aws.sagemaker`                                        |
| `account`     | AWS account ID that owns the cluster.                  |
| `time`        | ISO 8601 timestamp of the event.                       |
| `region`      | AWS Region where the cluster resides.                  |
| `resources`   | Array containing the cluster ARN.                      |
| `detail`      | Contains the `EventDetails` object described<br>above. |

## Common events (EKS and Slurm)

The following events are emitted for all HyperPod clusters regardless of
orchestrator. The **Description** column shows the value of
the `Description` field in the event record as it appears in the API response
and the console **Events** tab.

### Cluster lifecycle

| Event                          | Description                                                  |
| ------------------------------ | ------------------------------------------------------------ |
| Cluster operation started      | Cluster <cluster-name> <operation> started<br>successfully   |
| Cluster operation start failed | Failed to start Cluster <cluster-name><br><operation>        |
| Cluster operation completed    | Cluster <cluster-name> <operation> completed<br>successfully |
| Cluster operation failed       | Cluster <cluster-name> <operation><br>failed                 |

### Instance group lifecycle

| Event                                 | Description                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| Instance group operation started      | InstanceGroup <instance-group-name> <operation><br>started successfully in Cluster<br><cluster-name>    |
| Instance group operation start failed | Failed to start InstanceGroup <instance-group-name><br><operation> in Cluster <cluster-name>            |
| Instance group operation completed    | Instance Group <instance-group-name> <operation><br>in Cluster <cluster-name> completed<br>successfully |
| Instance group operation failed       | Instance Group <instance-group-name> <operation><br>in Cluster <cluster-name> failed                    |

### Instance group network configuration

| Event                               | Description                                                                                                                                                      |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Network configuration found         | Found Subnet <subnet-id> in AZ<br><availability-zone> with SecurityGroupIds<br><security-group-ids> for IG<br><instance-group-name> in Cluster<br><cluster-name> |
| Network configuration failed        | Failed to process Instance Group Network Configuration<br>details for IG <instance-group-name> in Cluster<br><cluster-name>                                      |
| Custom AMI override found           | Found Custom AMI Override <ami-id> for IG<br><instance-group-name> in Cluster<br><cluster-name>                                                                  |
| Custom AMI override failed          | Failed to process Custom AMI Override details for IG<br><instance-group-name> in Cluster<br><cluster-name>                                                       |
| Platform network configuration used | Using HyperPod Platform provided network<br>configuration for IG <instance-group-name> in Cluster<br><cluster-name>                                              |
| Network configuration determined    | Instance Group network configuration successfully<br>determined for IG <instance-group-name> in Cluster<br><cluster-name>                                        |

### Instance creation

| Event                                        | Description                                                                                                                              |
| -------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| Instance operation started                   | Instance <operation> started successfully in Cluster<br><cluster-name> and IG<br><instance-group-name>                                   |
| Instance operation start failed              | Failed to start Instance <operation> in Cluster<br><cluster-name> and IG<br><instance-group-name>                                        |
| Capacity reservation found                   | Found CapacityReservation ID <reservation-id> for<br>Cluster <cluster-name> and IG<br><instance-group-name>, using reserved<br>capacity  |
| Capacity reservation not found               | No CapacityReservation found for Cluster<br><cluster-name> and IG <instance-group-name>,<br>using on-demand pool                         |
| Instance payload setup failed                | Failed to process CapacityReservationDetails for Cluster<br><cluster-name> and IG<br><instance-group-name>                               |
| Customer ENI created                         | Successfully created Customer ENI for instance in Cluster<br><cluster-name> and IG<br><instance-group-name>                              |
| Customer ENI creation failed                 | Failed to create Customer ENI for instance in Cluster<br><cluster-name> and IG<br><instance-group-name>                                  |
| EC2 instance provisioned                     | EC2 Instance <instance-id> successfully provisioned<br>in Cluster <cluster-name> and IG<br><instance-group-name>                         |
| EC2 instance creation failed                 | Failed to provision EC2 Instance in Cluster<br><cluster-name> and IG<br><instance-group-name>                                            |
| Lifecycle script status updated              | Instance lifecycle script execution for EC2 Instance<br><instance-id> has <status>                                                       |
| Lifecycle script status update failed        | Failed to update Instance lifecycle script execution<br>status for EC2InstanceId <instance-id>                                           |
| Instance creation failed with lifecycle logs | Instance lifecycle script execution for EC2 Instance<br><instance-id> has Failed. To view lifecycle script<br>logs, visit log group...   |
| Unused ENI cleanup succeeded                 | Successfully deleted unused Customer ENIs for EC2<br>Instance <instance-id> in Cluster<br><cluster-name> and IG<br><instance-group-name> |
| Unused ENI cleanup failed                    | Failed to delete unused Customer ENIs for EC2 Instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name>        |

### Instance deletion

| Event                                | Description                                                                                                                     |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| EC2 instance termination in progress | Termination of EC2 Instance <instance-id> is<br>currently in progress in Cluster <cluster-name> and IG<br><instance-group-name> |
| EC2 instance termination failed      | Failed to terminate EC2 Instance <instance-id> in<br>Cluster <cluster-name> and IG<br><instance-group-name>                     |
| Customer ENI deleted                 | Customer ENI successfully deleted for EC2 Instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name>   |
| Customer ENI deletion failed         | Failed to delete Customer ENI for EC2 Instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name>       |

### Instance reboot

| Event                              | Description                                                                                                                 |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| EC2 instance reboot in progress    | Reboot of EC2 Instance <instance-id> is currently in<br>progress on Cluster <cluster-name> and IG<br><instance-group-name>  |
| EC2 instance reboot request failed | Failed to submit reboot request for EC2 Instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name> |

### Instance operation (generic)

| Event                        | Description                                                                                                            |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Instance operation completed | Instance <operation> <instance-id> in Cluster<br><cluster-name> and IG <instance-group-name><br>completed successfully |
| Instance operation failed    | Instance <operation> <instance-id> in Cluster<br><cluster-name> and IG <instance-group-name><br>failed                 |

### Instance replacement

| Event                             | Description                                                                                                                                               |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Instance replacement started      | Instance <instance-id> is starting as part of<br>instance replacement in Cluster <cluster-name> and IG<br><instance-group-name>                           |
| Instance replacement start failed | Instance <instance-id> failed to start as part of<br>instance replacement in Cluster <cluster-name> and IG<br><instance-group-name>                       |
| Instance replacement completed    | Instance <instance-id> <operation> completed<br>successfully as part of instance replacement in Cluster<br><cluster-name> and IG<br><instance-group-name> |
| Instance replacement failed       | Instance <instance-id> <operation> failed as<br>part of instance replacement in Cluster<br><cluster-name> and IG<br><instance-group-name>                 |

### FSx filesystem lifecycle

| Event                  | Description                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------ |
| FSx creation started   | FSx creation started for IG <instance-group-name><br>in Cluster <cluster-name>                   |
| FSx creation failed    | Failed to create FSx for IG<br><instance-group-name> in Cluster<br><cluster-name>                |
| FSx creation completed | FSx creation successfully completed for IG<br><instance-group-name> in Cluster<br><cluster-name> |
| FSx deletion started   | FSx deletion started for IG <instance-group-name><br>in Cluster <cluster-name>                   |
| FSx deletion failed    | Failed to delete FSx for IG<br><instance-group-name> in Cluster<br><cluster-name>                |
| FSx deletion completed | FSx deletion successfully completed for IG<br><instance-group-name> in Cluster<br><cluster-name> |
| FSx update started     | FSx update started for IG <instance-group-name> in<br>Cluster <cluster-name>                     |
| FSx update failed      | Failed to update FSx for IG<br><instance-group-name> in Cluster<br><cluster-name>                |
| FSx update completed   | FSx update successfully completed for IG<br><instance-group-name> in Cluster<br><cluster-name>   |

### Patching (common steps)

These patching events are emitted for both EKS and Slurm clusters during
`UpdateClusterSoftware` operations.

| Event                                       | Description                                                                                                                 |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| Instance group patching scheduled           | InstanceGroup <instance-group-name> in Cluster<br><cluster-name> has been scheduled for<br>UpdateClusterSoftware to latest. |
| Instance group patching schedule failed     | Failed to schedule UpdateClusterSoftware for IG<br><instance-group-name> in Cluster<br><cluster-name>.                      |
| Instance group patching started             | UpdateClusterSoftware initiated for IG<br><instance-group-name> in Cluster<br><cluster-name> using <strategy><br>strategy.  |
| Instance group patching start failed        | Failed to initiate UpdateClusterSoftware for IG<br><instance-group-name> in Cluster<br><cluster-name>.                      |
| Next patching batch selected                | Next update batch selected for IG<br><instance-group-name> in Cluster<br><cluster-name>.                                    |
| Next patching batch selection failed        | Failed to select the next update batch for IG<br><instance-group-name> in Cluster<br><cluster-name>.                        |
| Failed instances queued for replacement     | Failed instances in IG <instance-group-name> in<br>Cluster <cluster-name> queued for node<br>replacement.                   |
| Failed instance replacement queueing failed | Failed to queue instances for node replacement in IG<br><instance-group-name> in Cluster<br><cluster-name>.                 |
| Instance group patching completed           | UpdateClusterSoftware completed successfully for IG<br><instance-group-name> in Cluster<br><cluster-name>.                  |
| Instance group patching completion failed   | Failed to complete UpdateClusterSoftware for IG<br><instance-group-name> in Cluster<br><cluster-name>.                      |
| Root volume replacement started             | Root volume replacement started for Instance<br><instance-id> in IG<br><instance-group-name>.                               |
| Root volume replacement failed              | Failed to start root volume replacement for Instance<br><instance-id> in IG<br><instance-group-name>.                       |
| Instance patching succeeded                 | Instance <instance-id> in IG<br><instance-group-name> updated<br>successfully.                                              |

## EKS-specific events

The following events are emitted only for HyperPod clusters orchestrated with
Amazon EKS.

### Access entry management

| Event                                  | Description                                                             |
| -------------------------------------- | ----------------------------------------------------------------------- |
| SLR access entry operation succeeded   | SLR Access Entry <operation> successful for Cluster<br><cluster-name>   |
| SLR access entry operation failed      | SLR Access Entry <operation> failed for Cluster<br><cluster-name>       |
| EKS access entries operation succeeded | EKS Access Entries <operation> successful for<br>Cluster <cluster-name> |
| EKS access entries operation failed    | EKS Access Entries <operation> failed for Cluster<br><cluster-name>     |

### Kubernetes configuration updates

| Event                              | Description                                                                                                                    |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| Kubernetes config update succeeded | Successfully updated Kubernetes config for instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name> |
| Kubernetes config update failed    | Failed to update Kubernetes config for instance<br><instance-id> in Cluster <cluster-name> and IG<br><instance-group-name>     |

### Karpenter autoscaling

| Event                                        | Description                                                                                                                       |
| -------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Autoscaling operation succeeded              | AutoScaling <operation> <status> successfully<br>in Cluster <cluster-name>                                                        |
| Autoscaling operation failed                 | Failed to <operation> AutoScaling in Cluster<br><cluster-name>                                                                    |
| Karpenter CRD installation succeeded         | CustomResourceDefinition installation completed<br>successfully in EKS Cluster<br><cluster-name>                                  |
| Karpenter CRD installation failed            | CustomResourceDefinition installation failed for EKS<br>Cluster <cluster-name>                                                    |
| Karpenter SLR access policy update succeeded | <operation> access policies with<br>AmazonSageMakerHyperPodServiceRole access entry in EKS<br>cluster <cluster-name> successfully |
| Karpenter SLR access policy update failed    | Failed to <operation> access policies with<br>AmazonSageMakerHyperPodServiceRole access entry in EKS<br>cluster <cluster-name>    |

### Patching — EKS instance-level

| Event                                     | Description                                                                                                                       |
| ----------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Instance patching preparation succeeded   | Instance <instance-id> in IG<br><instance-group-name> cordoned and pods<br>evicted.                                               |
| Instance patching skipped (PDB violation) | UpdateClusterSoftware for Instance <instance-id> in<br>IG <instance-group-name> skipped due to<br>PodDisruptionBudget constraint. |
| Instance patching preparation failed      | Failed to prepare instance <instance-id> in IG<br><instance-group-name> for<br>UpdateClusterSoftware.                             |
| Instance restored to schedulable state    | Instance <instance-id> in IG<br><instance-group-name> restored to schedulable<br>state.                                           |
| Instance restore to schedulable failed    | Failed to restore instance <instance-id> in IG<br><instance-group-name> to schedulable state.                                     |

### Patching — EKS rollback

| Event                                      | Description                                                                                                                                                 |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bake time started                          | Baking period started for IG <instance-group-name><br>in Cluster <cluster-name>. Monitoring alarms<br>[<alarm-names>] for <duration><br>seconds.            |
| Bake time completed                        | Baking period completed for IG<br><instance-group-name> in Cluster<br><cluster-name>. No alarms triggered during the<br><duration>-second baking period.    |
| Bake time alarm triggered                  | Baking period failed for IG <instance-group-name><br>in Cluster <cluster-name>. Alarms<br>[<alarm-names>] entered ALARM state. Initiating<br>auto-rollback. |
| Bake time evaluation failed                | Failed to evaluate alarms during baking period for IG<br><instance-group-name> in Cluster<br><cluster-name>.                                                |
| Instance group patching rollback initiated | UpdateClusterSoftware failed for IG<br><instance-group-name> in Cluster<br><cluster-name>. Initiating rollback.                                             |
| Instance group patching rollback failed    | Rollback failed for IG <instance-group-name> in<br>Cluster <cluster-name>. Some instances may be in<br>FailedMaintenance state.                             |
| Instance patching rollback initiated       | Instance <instance-id> in IG<br><instance-group-name> failed to update. Rollback<br>initiated.                                                              |
| Instance patching rollback succeeded       | Instance <instance-id> in IG<br><instance-group-name> rolled back successfully to<br>previous AMI.                                                          |
| Instance patching rollback failed          | UpdateClusterSoftware rollback failed for instance<br><instance-id> in IG<br><instance-group-name>.                                                         |

## Slurm-specific events

The following events are emitted only for HyperPod clusters orchestrated with
Slurm.

| Event                             | Description                                                                                                       |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Provisioning parameters found     | Found provisioning_parameters.json in LifeCycleScript S3 Path<br>for controller group <instance-group-name>       |
| Provisioning parameters not found | No provisioning_parameters.json found in LifeCycleScript S3<br>Path for controller group<br><instance-group-name> |
| Slurm munge key created           | Successfully created and stored munge key                                                                         |
| Slurm drift validation passed     | Slurm configuration drift validation passed                                                                       |
| Slurm drift detected              | Slurm configuration drift detected:<br><drift-details>                                                            |
| Slurm cluster rollback completed  | Cluster creation failed: controller and login nodes did not<br>become ready within the expected time              |
| Slurm reconfiguration succeeded   | Slurm was reconfigured successfully. Slurm config updated to<br>match desired state                               |

## EventBridge integration

HyperPod sends cluster events to Amazon EventBridge using three detail
types:

| Detail type                                       | Description                                                                                                                                        |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| `SageMaker HyperPod Cluster Event`                | Operational events for provisioning, scaling, patching, and<br>orchestrator-specific operations. Includes<br>`EventLevel` for severity filtering.  |
| `SageMaker HyperPod Cluster State Change`         | Cluster-level status transitions (for example, Creating to<br>InService). Includes full cluster configuration.                                     |
| `SageMaker HyperPod Cluster Node Health<br>Event` | Health monitoring events from the HyperPod Health<br>Monitoring Agent (HMA). Includes health status, reason, repair<br>action, and recommendation. |

### Event pattern examples

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

- [ListClusterEvents](../APIReference/API_ListClusterEvents.md "../APIReference/API_ListClusterEvents.md") — List events with filtering, sorting, and
  pagination
- [DescribeClusterEvent](../APIReference/API_DescribeClusterEvent.md "../APIReference/API_DescribeClusterEvent.md") — Get full details for a specific
  event
- [ClusterEventSummary](../APIReference/API_ClusterEventSummary.md "../APIReference/API_ClusterEventSummary.md") — Event summary data type
- [ClusterEventDetail](../APIReference/API_ClusterEventDetail.md "../APIReference/API_ClusterEventDetail.md") — Event detail data type

## See also

- [SageMaker HyperPod Slurm cluster events](sagemaker-hyperpod-cluster-events-slurm-page.md "sagemaker-hyperpod-cluster-events-slurm-page.md") —
  Slurm cluster events with CLI usage and common scenarios
- [SageMaker HyperPod EKS cluster events](sagemaker-hyperpod-cluster-events-eks-page.md "sagemaker-hyperpod-cluster-events-eks-page.md") — EKS
  cluster events with CLI usage and common scenarios

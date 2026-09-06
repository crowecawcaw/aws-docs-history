

# Compute environments on Amazon ECS Managed Instances
<a name="ecs-managed-instances-compute-environments"></a>

AWS Batch compute environments on Amazon ECS Managed Instances use a `managedInstancesProvider` configuration block inside `computeResources`. This structure aligns with the Amazon ECS capacity provider model and is self-contained. All networking, instance profile, and instance selection configuration lives within this block.

The following list describes the compute environment parameters for Amazon ECS Managed Instances compute environments.

`type` (top-level)  
Must be `MANAGED`.  

```
"type": "MANAGED"
```

`computeResources.type`  
Must be `ECS_MANAGED_INSTANCES`. Unlike Fargate and Amazon EC2 compute environments, Spot capacity is not expressed as a separate type (there is no `ECS_MANAGED_INSTANCES_SPOT` type). Instead, use `capacityOptionType` inside `managedInstancesProvider.instanceLaunchTemplate` to specify On-Demand or Spot capacity.  

```
"type": "ECS_MANAGED_INSTANCES"
```

`computeResources.maxvCpus`  
The maximum number of vCPUs that the compute environment can scale to. Works the same as `maxvCpus` for Fargate compute environments — it caps the total vCPU consumed across all running jobs.  
Currently, AWS Batch evaluates `maxvCpus` based on the total vCPUs requested by running jobs, not the total vCPUs of the underlying Amazon EC2 instances. Amazon ECS Managed Instances uses multi-tenant instance allocation. As a result, the actual instance vCPU capacity provisioned might exceed the job vCPU total. The compute environment might provision more instance capacity than the `maxvCpus` value implies. This behavior might be refined in a future update.

`computeResources.managedInstancesProvider`  
Required for Amazon ECS Managed Instances compute environments. Contains all Amazon ECS Managed Instances-specific configuration. For more information, see [ManagedInstancesProvider](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ManagedInstancesProvider.html) in the *Amazon Elastic Container Service API Reference*. The following fields are available:    
`infrastructureRoleArn`  
Required. The ARN of the IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf. This role must have a trust policy for `ecs.amazonaws.com`. Your IAM principal must have `iam:PassRole` permission for this role with the condition `iam:PassedToService: ecs.amazonaws.com`.  
`propagateTags`  
Optional. Controls whether tags on the capacity provider are propagated to the Amazon EC2 instances it launches. Valid values are `CAPACITY_PROVIDER` and `NONE`.  
`instanceLaunchTemplate`  
Required. Contains the instance launch configuration:    
`ec2InstanceProfileArn`  
Required. The ARN of the Amazon EC2 instance profile for the managed instances. This instance profile must use the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy with a trust policy for `ec2.amazonaws.com`.  
`networkConfiguration`  
Required. Specifies the VPC configuration for the managed instances.  
+ `subnets` — Required. The VPC subnets where instances are launched. Instances need external network access to communicate with the Amazon ECS service endpoint. If your subnets don't provide public IP addresses, they must have a NAT gateway for outbound internet access.
+ `securityGroups` — Required. The VPC security groups to associate with the instances.  
`instanceRequirements`  
Optional. Specifies constraints on which Amazon EC2 instance types Amazon ECS can launch. If not provided, all available instance types are eligible.  
+ `allowedInstanceTypes` — A list of specific instance types or instance families (for example, `m5.large` or `g5`). When specified, only these instance types are used.  
`capacityOptionType`  
Optional. The capacity pricing model. Valid values are `ON_DEMAND` (default) and `SPOT`. With `SPOT`, Amazon ECS launches Spot Instances which can provide significant cost savings for fault-tolerant workloads.  
`storageConfiguration`  
Optional. Configures the root EBS volume for instances.  
+ `storageSizeGiB` — The size of the root volume in GiB.  
`monitoring`  
Optional. The level of CloudWatch monitoring for the instances. Valid values are `BASIC` and `DETAILED`.  
`fipsEnabled`  
Optional. When set to `true`, enables FIPS 140-2 compliance on the managed instances. Not available in all AWS Regions.  
`capacityReservations`  
Optional. Targets On-Demand Capacity Reservations (ODCRs) for predictable capacity availability.  
+ `reservationGroupArn` — The ARN of the capacity reservation group to target.
+ `reservationPreference` — Controls how capacity reservations are used. Valid values are `RESERVATIONS_ONLY` (only launch into reservations), `RESERVATIONS_FIRST` (prefer reservations, fall back to on-demand), and `RESERVATIONS_EXCLUDED` (do not use reservations).  
`instanceMetadataTagsPropagation`  
Optional. Controls whether tags are accessible from the instance metadata service (IMDS) on the managed instances.  
`localStorageConfiguration`  
Optional. Configures local instance store volumes (local NVMe SSDs) for the managed instances.  
+ `useLocalStorage` — Whether instance store volumes are available to containers running on the managed instances.  
`infrastructureOptimization`  
Optional. Controls how Amazon ECS manages idle instances.  
+ `scaleInAfter` — The number of seconds an instance must be idle before Amazon ECS terminates it. Valid values are `-1` (to disable scale-in) or `0`–`3600` (seconds of idle time before termination).

`computeResources.capacityTags`  
Optional. Tags to apply to the Amazon ECS capacity provider and Amazon EC2 instances managed by the compute environment. Only valid for `ECS_MANAGED_INSTANCES` compute environments. Your IAM principal must have `batch:SetCapacityTags` permission on the compute environment resource to specify this field. For more information, see [Control access to capacity tags with `batch:SetCapacityTags`](capacity-tags-access-policy.md).  
These tags are separate from the top-level `tags` on the compute environment resource itself. Use `capacityTags` for cost allocation and organization of the underlying infrastructure resources.

Parameters not applicable to Amazon ECS Managed Instances  
The following `computeResources` parameters are not valid for Amazon ECS Managed Instances compute environments and must not be specified:  
+ `allocationStrategy`
+ `bidPercentage`
+ `desiredvCpus`
+ `minvCpus`
+ `imageId`
+ `instanceTypes`
+ `instanceRole`
+ `ec2Configuration`
+ `ec2KeyPair`
+ `launchTemplate`
+ `placementGroup`
+ `spotIamFleetRole`
+ `subnets` (use `managedInstancesProvider.instanceLaunchTemplate.networkConfiguration.subnets` instead)
+ `securityGroupIds` (use `managedInstancesProvider.instanceLaunchTemplate.networkConfiguration.securityGroups` instead)

## Updating Amazon ECS Managed Instances compute environments
<a name="ecs-managed-instances-compute-environment-updates"></a>

All Amazon ECS Managed Instances compute environment attributes can be updated except the compute environment type, `capacityOptionType`, and `fipsEnabled`. Updates flow through to the underlying Amazon ECS capacity provider. New instances use the updated configuration. Existing instances continue running until their jobs complete and then drain naturally.

The following cannot be changed after creation:
+ The compute environment type (`ECS_MANAGED_INSTANCES` cannot be changed to `FARGATE`, `EC2`, or other types)
+ `capacityOptionType` — You cannot switch between On-Demand and Spot after creation
+ `fipsEnabled` — FIPS mode cannot be changed after creation

## Examples
<a name="ecs-managed-instances-compute-environment-examples"></a>

### Minimal configuration
<a name="ecs-managed-instances-ce-example-minimal"></a>

The following example shows the minimum configuration required to create an Amazon ECS Managed Instances compute environment. Amazon ECS selects instance types automatically from all available types.

```
{
  "computeEnvironmentName": "my-managed-instances-ce",
  "type": "MANAGED",
  "state": "ENABLED",
  "computeResources": {
    "type": "ECS_MANAGED_INSTANCES",
    "maxvCpus": 256,
    "managedInstancesProvider": {
      "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
      "instanceLaunchTemplate": {
        "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
        "networkConfiguration": {
          "subnets": ["subnet-abcde012", "subnet-bcde012a"],
          "securityGroups": ["sg-abcde012"]
        }
      }
    }
  }
}
```

### GPU workload with specific instance types
<a name="ecs-managed-instances-ce-example-gpu"></a>

The following example creates a compute environment constrained to NVIDIA GPU instance types for machine learning workloads.

```
{
  "computeEnvironmentName": "my-gpu-managed-instances-ce",
  "type": "MANAGED",
  "state": "ENABLED",
  "computeResources": {
    "type": "ECS_MANAGED_INSTANCES",
    "maxvCpus": 1000,
    "managedInstancesProvider": {
      "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
      "instanceLaunchTemplate": {
        "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
        "networkConfiguration": {
          "subnets": ["subnet-abcde012", "subnet-bcde012a"],
          "securityGroups": ["sg-abcde012"]
        },
        "instanceRequirements": {
          "allowedInstanceTypes": ["g5.xlarge", "g5.2xlarge", "g5.4xlarge"]
        },
        "capacityOptionType": "ON_DEMAND"
      }
    }
  }
}
```

### Spot capacity for cost-sensitive workloads
<a name="ecs-managed-instances-ce-example-spot"></a>

The following example creates a Spot-backed compute environment for fault-tolerant batch workloads.

```
{
  "computeEnvironmentName": "my-spot-managed-instances-ce",
  "type": "MANAGED",
  "state": "ENABLED",
  "computeResources": {
    "type": "ECS_MANAGED_INSTANCES",
    "maxvCpus": 5000,
    "managedInstancesProvider": {
      "infrastructureRoleArn": "arn:aws:iam::123456789012:role/ecsInfrastructureRole",
      "instanceLaunchTemplate": {
        "ec2InstanceProfileArn": "arn:aws:iam::123456789012:instance-profile/ecsInstanceProfile",
        "networkConfiguration": {
          "subnets": ["subnet-abcde012", "subnet-bcde012a", "subnet-cde012ab"],
          "securityGroups": ["sg-abcde012"]
        },
        "instanceRequirements": {
          "allowedInstanceTypes": ["m5.large", "m5.xlarge", "m6i.large", "m6i.xlarge"]
        },
        "capacityOptionType": "SPOT",
        "storageConfiguration": {
          "storageSizeGiB": 100
        }
      }
    }
  }
}
```
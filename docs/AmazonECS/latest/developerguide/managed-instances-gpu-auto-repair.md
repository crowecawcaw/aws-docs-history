

# GPU auto repair for Amazon ECS managed instances
<a name="managed-instances-gpu-auto-repair"></a>

Amazon ECS monitors NVIDIA GPU health on Amazon ECS Managed Instances that use GPU hardware. When Amazon ECS detects a GPU hardware failure, it can automatically replace the impaired instance. GPU auto repair is enabled by default for Amazon ECS Managed Instances.

## How it works
<a name="managed-instances-gpu-auto-repair-how-it-works"></a>

Amazon ECS uses NVIDIA Data Center GPU Manager (DCGM) to monitor NVIDIA GPU health on managed instances that have GPU hardware. When DCGM reports a critical GPU failure, Amazon ECS marks the instance as impaired.

When GPU auto repair is enabled, Amazon ECS replaces the impaired instance by using a start-before-stop workflow:

1. Amazon ECS sets the impaired instance to DRAINING. New tasks are not placed on the instance.

1. Amazon ECS provisions a replacement instance.

1. Amazon ECS allows existing tasks to stop gracefully. Amazon ECS honors the task stop timeout for tasks on the instance.

1. After the drain period ends, Amazon ECS terminates the impaired instance.

Amazon ECS rate-limits repair actions to prevent cascading replacements. No more than 20% of the instances belonging to the capacity provider can be drained at a time. If there are fewer than 9 instances in the capacity provider, at most one instance is drained at a time.

## Monitoring GPU health
<a name="managed-instances-gpu-auto-repair-monitoring"></a>

You can use the `DescribeContainerInstances` API to check GPU health. For more information, see [Monitor Amazon ECS container instance health](container-instance-health.md). You can also monitor GPU health changes through the [Amazon ECS container instance health change events](ecs_container_instance_health_events.md).

## Monitored XID error codes
<a name="managed-instances-gpu-auto-repair-xid-errors"></a>

Amazon ECS monitors the following NVIDIA Xid error codes. If Amazon ECS detects any of these errors, it marks the instance as impaired and replaces the instance.


| Xid | Description | 
| --- | --- | 
| 46 | GPU stopped processing | 
| 48 | Double Bit ECC Error | 
| 54 | Auxiliary power connector not connected | 
| 62 | Internal micro-controller halt | 
| 64 | GPU memory remapping failure | 
| 74 | NVLink Error | 
| 79 | GPU has fallen off the bus | 
| 95 | Uncontained memory error | 
| 109 | Context switch timeout | 
| 110 | GPU disappeared from the bus | 
| 136 | GPU memory page retirement limit exceeded | 
| 140 | Unrecoverable ECC Error | 
| 142 | GPU memory page retired due to uncorrectable error | 
| 143 | GPU memory page retired due to correctable error threshold | 
| 151 | GPU to CPU interconnect error | 
| 155 | GPU NVLink flit CRC error | 
| 156 | GPU NVLink lane error | 
| 158 | GPU InfoROM corrupted | 

For more information on XID errors, see [Xid Errors](https://docs.nvidia.com/deploy/xid-errors/index.html#topic_5_1) in the *NVIDIA GPU Deployment and Management Documentation*. For more information on the individual XID messages, see [Understanding Xid Messages](https://docs.nvidia.com/deploy/gpu-debug-guidelines/index.html#understanding-xid-messages) in the *NVIDIA GPU Deployment and Management Documentation*.

## Disabling auto repair
<a name="managed-instances-gpu-auto-repair-disable"></a>

GPU auto repair is enabled by default for Amazon ECS Managed Instances. To disable GPU auto repair, set `actionsStatus` to `DISABLED` in `autoRepairConfiguration` when you create or update a capacity provider. You can also disable GPU auto repair in the Amazon ECS console when you create or update a capacity provider.

When GPU auto repair is disabled, Amazon ECS continues to monitor GPU health, but it does not replace impaired instances automatically.

**Note**  
Disabling GPU auto repair also disables Amazon ECS Managed Daemons auto repair. For more information, see [Amazon ECS Managed Daemons auto repair](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/managed-daemons-auto-repair.html).

**To disable GPU auto repair**

```
aws ecs update-capacity-provider \
    --name {{my-gpu-capacity-provider}} \
    --managed-instances-provider '{
        "infrastructureRoleArn": "arn:aws:iam::{{111122223333}}:role/ecsInfrastructureRole",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::{{111122223333}}:instance-profile/ecsInstanceRole",
            "networkConfiguration": {
                "subnets": ["{{subnet-0123456789abcdef0}}"],
                "securityGroups": ["{{sg-0123456789abcdef0}}"]
            }
        },
        "autoRepairConfiguration": {
            "actionsStatus": "DISABLED"
        }
    }'
```

**To enable GPU auto repair**

```
aws ecs update-capacity-provider \
    --name {{my-gpu-capacity-provider}} \
    --managed-instances-provider '{
        "infrastructureRoleArn": "arn:aws:iam::{{111122223333}}:role/ecsInfrastructureRole",
        "instanceLaunchTemplate": {
            "ec2InstanceProfileArn": "arn:aws:iam::{{111122223333}}:instance-profile/ecsInstanceRole",
            "networkConfiguration": {
                "subnets": ["{{subnet-0123456789abcdef0}}"],
                "securityGroups": ["{{sg-0123456789abcdef0}}"]
            }
        },
        "autoRepairConfiguration": {
            "actionsStatus": "ENABLED"
        }
    }'
```

**To verify the configuration**

```
aws ecs describe-capacity-providers \
    --capacity-providers {{my-gpu-capacity-provider}}
```
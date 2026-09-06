

# Tutorial: Create a managed compute environment using Amazon ECS Managed Instances
<a name="create-compute-environment-ecs-managed-instances"></a>

This tutorial walks you through creating an AWS Batch compute environment that uses Amazon ECS Managed Instances. Amazon ECS manages the Amazon EC2 instances on your behalf — you specify the maximum capacity and optional instance constraints, and Amazon ECS handles provisioning, scaling, and termination.

## Prerequisites
<a name="create-ce-ecs-managed-instances-prerequisites"></a>

Before you create an Amazon ECS Managed Instances compute environment, you must have the following:
+ An **Amazon ECS infrastructure role** — an IAM role that Amazon ECS assumes to manage Amazon EC2 instances on your behalf. The role must have a trust policy for `ecs.amazonaws.com`. For more information, see [Amazon ECS infrastructure IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/infrastructure-iam-roles.html) in the *Amazon Elastic Container Service Developer Guide*.
+ An **Amazon EC2 instance profile** — an instance profile that uses the `AmazonECSInstanceRolePolicyForManagedInstances` managed policy. The trust policy must allow `ec2.amazonaws.com` to assume the role.
+ Your IAM principal must have `iam:PassRole` permission for the infrastructure role with the condition `iam:PassedToService: ecs.amazonaws.com`.
+ A VPC with subnets that have outbound internet access (either public IP assignment or a NAT gateway).

## Creating an Amazon ECS Managed Instances compute environment (console)
<a name="create-ce-ecs-managed-instances-console"></a>

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/).

1. From the navigation bar, choose the AWS Region to use.

1. In the left navigation pane, choose **Environments**.

1. Choose **Create environment**, then choose **Create compute environment**.

1. For **Compute environment type**, choose **ECS Managed Instances**.

1. For **Compute environment name**, enter a unique name. The name can be up to 128 characters long and can contain uppercase and lowercase letters, numbers, hyphens (-), and underscores (\_).

1. For **Maximum vCPUs**, enter the maximum number of vCPUs that the compute environment can scale to.

1. For **Infrastructure role**, choose the Amazon ECS infrastructure role that you created as a prerequisite.

1. For **Instance profile**, choose the Amazon EC2 instance profile that you created as a prerequisite.

1. In the **Networking** section:

   1. For **VPC**, choose the VPC where instances will be launched.

   1. For **Subnets**, choose one or more subnets. The subnets must have outbound internet access.

   1. For **Security groups**, choose one or more security groups to associate with the instances.

1. (Optional) For **Capacity type**, choose **Spot** to use Spot Instances for cost savings on fault-tolerant workloads. The default is **On-Demand**.

1. (Optional) For **Allowed instance types**, specify which instance types Amazon ECS can launch. If you don't specify any, all available instance types are eligible.

1. Choose **Create compute environment**.

## Creating an Amazon ECS Managed Instances compute environment (AWS CLI)
<a name="create-ce-ecs-managed-instances-cli"></a>

Use the `create-compute-environment` command to create an Amazon ECS Managed Instances compute environment.

### Basic example
<a name="create-ce-ecs-managed-instances-cli-basic"></a>

The following example creates a compute environment with the minimum required configuration. Amazon ECS can use any available instance type.

```
$ aws batch create-compute-environment \
    --compute-environment-name {{my-managed-instances-ce}} \
    --type MANAGED \
    --state ENABLED \
    --compute-resources '{
      "type": "ECS_MANAGED_INSTANCES",
      "maxvCpus": 256,
      "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsInfrastructureRole}}",
        "instanceLaunchTemplate": {
          "ec2InstanceProfileArn": "arn:aws:iam::{{123456789012}}:instance-profile/{{ecsInstanceProfile}}",
          "networkConfiguration": {
            "subnets": ["{{subnet-abcde012}}", "{{subnet-bcde012a}}"],
            "securityGroups": ["{{sg-abcde012}}"]
          }
        }
      }
    }'
```

### Spot with specific instance types
<a name="create-ce-ecs-managed-instances-cli-spot"></a>

The following example creates a Spot-backed compute environment constrained to specific instance types.

```
$ aws batch create-compute-environment \
    --compute-environment-name {{my-spot-managed-instances-ce}} \
    --type MANAGED \
    --state ENABLED \
    --compute-resources '{
      "type": "ECS_MANAGED_INSTANCES",
      "maxvCpus": 1000,
      "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsInfrastructureRole}}",
        "instanceLaunchTemplate": {
          "ec2InstanceProfileArn": "arn:aws:iam::{{123456789012}}:instance-profile/{{ecsInstanceProfile}}",
          "networkConfiguration": {
            "subnets": ["{{subnet-abcde012}}", "{{subnet-bcde012a}}"],
            "securityGroups": ["{{sg-abcde012}}"]
          },
          "instanceRequirements": {
            "allowedInstanceTypes": ["m5.large", "m5.xlarge", "m6i.large", "m6i.xlarge"]
          },
          "capacityOptionType": "SPOT"
        }
      }
    }'
```

Output:

```
{
    "computeEnvironmentName": "my-spot-managed-instances-ce",
    "computeEnvironmentArn": "arn:aws:batch:us-east-1:123456789012:compute-environment/my-spot-managed-instances-ce"
}
```

### With capacity reservations
<a name="create-ce-ecs-managed-instances-cli-reservations"></a>

The following example creates a compute environment that targets On-Demand Capacity Reservations for predictable capacity.

```
$ aws batch create-compute-environment \
    --compute-environment-name {{my-reserved-managed-instances-ce}} \
    --type MANAGED \
    --state ENABLED \
    --compute-resources '{
      "type": "ECS_MANAGED_INSTANCES",
      "maxvCpus": 512,
      "managedInstancesProvider": {
        "infrastructureRoleArn": "arn:aws:iam::{{123456789012}}:role/{{ecsInfrastructureRole}}",
        "instanceLaunchTemplate": {
          "ec2InstanceProfileArn": "arn:aws:iam::{{123456789012}}:instance-profile/{{ecsInstanceProfile}}",
          "networkConfiguration": {
            "subnets": ["{{subnet-abcde012}}", "{{subnet-bcde012a}}"],
            "securityGroups": ["{{sg-abcde012}}"]
          },
          "instanceRequirements": {
            "allowedInstanceTypes": ["m5.xlarge", "m5.2xlarge"]
          },
          "capacityReservations": {
            "reservationGroupArn": "arn:aws:ec2:{{us-east-1}}:{{123456789012}}:capacity-reservation-group/{{my-reservation-group}}",
            "reservationPreference": "RESERVATIONS_FIRST"
          }
        }
      }
    }'
```

## Next steps
<a name="create-ce-ecs-managed-instances-next-steps"></a>

After creating your compute environment, complete the following steps to run jobs:

1. Create a job queue and associate your Amazon ECS Managed Instances compute environment with it. For more information, see [Create a job queue](create-job-queue.md).

1. Create a job definition with `platformCapabilities` set to `MANAGED_INSTANCES` and using `ecsProperties`. For more information, see [Job definitions on Amazon ECS Managed Instances](ecs-managed-instances-job-definitions.md).

1. Submit a job to the job queue. For more information, see [Tutorial: submit a job](submit_job.md).
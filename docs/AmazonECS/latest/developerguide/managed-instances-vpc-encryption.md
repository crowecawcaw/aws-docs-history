

# Enabling VPC Encryption control for Amazon ECS Managed Instances
<a name="managed-instances-vpc-encryption"></a>

Amazon ECS Managed Instances supports VPC Encryption Controls, a security and compliance feature that provides centralized control to monitor and enforce encryption in transit for all traffic flows within and across your VPCs in a region. When VPC Encryption Controls is enabled on your subnet, you can specify instance types that support encryption in transit in your Amazon ECS Managed Instances custom capacity provider, guaranteeing that Amazon ECS Managed Instances workloads run with encryption in transit.

## Prerequisites
<a name="managed-instances-vpc-encryption-prerequisites"></a>

Before you begin, you need:
+ A VPC with encryption in transit enabled on subnets. For more information, see [VPC encryption controls documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html).
+ An Amazon ECS Managed Instances custom capacity provider. For more information, see [Architect for Amazon ECS Managed Instances](ManagedInstances.md).

## Identify compatible instance types
<a name="managed-instances-vpc-encryption-compatible-types"></a>

Amazon EC2 instance types must meet two requirements:

1. **Support VPC encryption in transit** - Use the following AWS CLI command to list Amazon EC2 instance types that support encryption in transit:

   ```
   aws ec2 describe-instance-types \
       --filters Name=network-info.encryption-in-transit-supported,Values=true \
       --query "InstanceTypes[*].[InstanceType]" \
       --output text | sort
   ```

1. **Supported by Amazon ECS Managed Instances** - All Amazon EC2 instance types supported by Amazon ECS Managed Instances are documented in [Amazon ECS Managed Instances instance types](managed-instances-instance-types.md).

If you have additional requirements (such as specific CPU, memory, or architecture needs), filter the compatible instance types further based on your workload requirements.

## Create a cluster with VPC encryption support
<a name="managed-instances-vpc-encryption-cluster-config"></a>

To configure Amazon ECS Managed Instances for VPC encryption in transit:

1. Create a new cluster and select **Fargate and Managed Instances** for the infrastructure.

1. Select **Use custom – advanced** to access additional configuration parameters.

1. In **Allowed Instance types**, add only the specific instance types that support VPC encryption in transit.

When configured this way, Amazon ECS Managed Instances will launch only Amazon EC2 instance types that support VPC encryption in transit.

## Considerations
<a name="managed-instances-vpc-encryption-considerations"></a>
+ **Burstable performance instances** - T3, T3a, and T4g instance types do not support VPC encryption in transit and cannot be used in subnets with encryption control enabled in Enforced mode.
+ **Mode transitions** - You can transition your VPC subnet from Monitor mode to Enforced mode only if all running instances support VPC encryption in transit.
+ **Task launch failures** - In Enforced mode, tasks will fail to launch if you specify instance types that don't support encryption in transit.

## Troubleshooting
<a name="managed-instances-vpc-encryption-troubleshooting"></a>

Task launch failures in Enforced mode  
If tasks fail to launch, verify that all specified instance types support VPC encryption in transit using the AWS CLI command provided above.

Cannot transition to Enforced mode  
Use the console or `GetVpcResourcesBlockingEncryptionEnforcement` command to identify resources that are not enforcing encryption in transit.

For more information about VPC Encryption Controls, see the [VPC encryption controls documentation](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-encryption-controls.html).
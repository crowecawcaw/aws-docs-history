

# Customize compute node network interfaces with launch template overrides
<a name="tutorial-network-customization-v3"></a>

Starting with AWS ParallelCluster 3.15.0, the `LaunchTemplateOverrides` parameter lets you customize the network interfaces of compute nodes by overriding the default network interface configuration with the configuration in a referenced launch template. The entire network interface section of the compute nodes is overwritten by the network interface section of the launch template used to override.

This tutorial walks through an example of overriding the default network configuration of `p6-b300.48xlarge` compute nodes. This customization is useful when you need a specific network interface configuration that differs from what AWS ParallelCluster configures by default. In this example, we configure use case 2 for P6-B300 instances as outlined in the [Amazon EC2 EFA-supported instance types documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-acc-inst-types.html).

**Note**  
It is recommended to use the AWS CLI to create the launch template instead of the console for maximum flexibility.

**Note**  
The launch template should only contain Network Interfaces overrides. AWS ParallelCluster has a validation preventing overriding other parameters.

**Warning**  
If you use the override to configure network interfaces in a way that is not supported by the instance type being used, then the instances will fail to launch.

**Prerequisites**
+ AWS ParallelCluster version 3.15.0 or later [is installed](install-v3-parallelcluster.md).
+ The AWS CLI [is installed and configured.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ You have an IAM role with the [permissions](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies) that are required to run the [`pcluster`](pcluster-v3.md) CLI.

## Step 1: Create security groups
<a name="tutorial-network-customization-v3-security-groups"></a>

When creating the launch template to use in the override, you must reference a security group. The default AWS ParallelCluster security group for the compute resource does not exist until cluster creation, so you must create a custom security group. This security group must then be referenced by the head node security group to allow traffic between the head node and compute nodes.

If you are updating an existing cluster to customize new capacity, you can use the default AWS ParallelCluster compute node security group in the launch template instead of creating a custom one.

Create the following two security groups:
+ **Head node additional security group** (`sg-1234abcd`):
  + Ingress: all traffic from compute security group
+ **Compute security group** (`sg-abcd1234`):
  + Ingress: all traffic from head node security group
  + Ingress: all traffic from self (compute-to-compute)
  + Egress: default allow-all

## Step 2: Create the launch template
<a name="tutorial-network-customization-v3-launch-template"></a>

Create a launch template that defines the network interface configuration for `p6-b300.48xlarge` compute nodes. For the primary network interface (network card index 0, device index 0), use an ENA (default) network interface. For the remaining network cards, create an EFA-only interface (network card indexes 1-16, device index 0) and an ENA (default) interface (network card indexes 1-16, device index 1).

Run the following AWS CLI command to create the launch template (`lt-123456789`):

```
aws ec2 create-launch-template \
  --region us-east-1 \
  --launch-template-name override-lt \
  --launch-template-data '{
    "NetworkInterfaces": [
      {"NetworkCardIndex":0,  "DeviceIndex":0, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":1,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":1,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":2,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":2,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":3,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":3,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":4,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":4,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":5,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":5,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":6,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":6,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":7,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":7,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":8,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":8,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":9,  "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":9,  "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":10, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":10, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":11, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":11, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":12, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":12, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":13, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":13, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":14, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":14, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":15, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":15, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":16, "DeviceIndex":0, "InterfaceType":"efa-only", "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"},
      {"NetworkCardIndex":16, "DeviceIndex":1, "Groups":["sg-abcd1234"], "SubnetId":"subnet-123456789"}
    ]
  }'
```

## Step 3: Create the cluster with launch template overrides
<a name="tutorial-network-customization-v3-create-cluster"></a>

Create a cluster configuration that uses the `LaunchTemplateOverrides` parameter to reference the launch template you created.

```
Region: us-east-1
HeadNode:
  InstanceType: c5.xlarge
  Networking:
    SubnetId: subnet-abcdefghi
    AdditionalSecurityGroups:
      # Add the head node SG that allows traffic from the compute node SG
      - sg-1234abcd
...

Scheduling:
  Scheduler: slurm
  SlurmQueues:
  - Name: queue0
    Networking:
      SubnetIds:
        - subnet-123456789
    ComputeResources:
      - Name: compute-resource1
        InstanceType: p6-b300.48xlarge
        Efa:
          Enabled: false # The override replaces all network interface configuration, so this setting is ignored
        LaunchTemplateOverrides:
          LaunchTemplateId: lt-123456789
          Version: 1 # If the launch template is updated, then the new version should be specified here.
```
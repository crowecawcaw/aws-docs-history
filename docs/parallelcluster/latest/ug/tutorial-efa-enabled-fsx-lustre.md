# Creating a cluster with an EFA-enabled FSx Lustre

In this tutorial, you will create a cluster that uses an EFA-enabled FSx Lustre file system as shared
storage. Using an FSx Lustre file system with EFA enabled can provide a boost in performance up to 8x.
To verify if an EFA-enabled file system is what you need, look at [Working with EFA-enabled file systems](../../../fsx/latest/LustreGuide/efa-file-systems.md "../../../fsx/latest/LustreGuide/efa-file-systems.md") in the
_FSx for Lustre User Guide_.

When you use AWS ParallelCluster, you only pay for the AWS resources that are created when you create
or update AWS ParallelCluster images and clusters. For more information, see [AWS services used by AWS ParallelCluster](aws-services-v3.md "aws-services-v3.md").

## Requirements

- The AWS CLI is [installed and configured](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- The ParallelCluster CLI is [installed and
  configured](install-v3-parallelcluster.md "install-v3-parallelcluster.md").
- An [Amazon
  EC2 key pair](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") to log into the cluster.
- An IAM role with the [permissions](../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md "../../../AWSEC2/latest/UserGuide/ec2-key-pairs.md") that are required to
  run the ParallelCluster CLI.

## Create Security Groups

Create two security groups in the same VPC where the cluster and the file system will be deployed:
one for the client running on cluster nodes and one for the file system.

```
# Create security group for the FSx client
aws ec2 create-security-group \
    --group-name Fsx-Client-SecurityGroup \
    --description "Allow traffic for the FSx Lustre client" \
    --vpc-id `vpc-cluster` \
    --region `region`

# Create security group for the FSx file system
aws ec2 create-security-group \
    --group-name Fsx-FileSystem-SecurityGroup \
    --description "Allow traffic for the FSx Lustre File System" \
    --vpc-id `vpc-cluster` \
    --region `region`

```

In the remainder of the tutorial, we will assume `sg-client` and `sg-file-system`
are the security group ids of the client and file system, respectively.

Configure the security group for the client to allow all outbound traffic to the file system, as
[required
by EFA](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security").

```
# Allow all outbound traffic from the client to the file system
aws ec2 authorize-security-group-egress \
 --group-id `sg-client` \
 --protocol -1 \
 --port -1 \
 --source-group `sg-file-system` \
 --region `region`
```

Configure the security group for the file system to allow all inbound/outbound traffic within itself
and all inbound traffic from the client, as [required by EFA](../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security "../../../AWSEC2/latest/UserGuide/efa-start.md#efa-start-security").

```
# Allow all inbound traffic within this security group
aws ec2 authorize-security-group-ingress \
    --group-id `sg-file-system` \
    --protocol -1 \
    --port -1 \
    --source-group `sg-file-system` \
    --region region

# Allow all outbound traffic within this security group
aws ec2 authorize-security-group-egress \
    --group-id `sg-file-system` \
    --protocol -1 \
    --port -1 \
    --source-group `sg-file-system` \
    --region `region`

# Allow all inbound traffic from the client
aws ec2 authorize-security-group-ingress \
    --group-id `sg-file-system` \
    --protocol -1 \
    --port -1 \
    --source-group `sg-client` \
    --region `region`

# Allow all outbound traffic to the client
aws ec2 authorize-security-group-egress \
    --group-id `sg-file-system` \
    --protocol -1 \
    --port -1 \
    --source-group `sg-client` \
    --region `region`
```

## Create the file system

Create the file system within the same Availability Zone (AZ) where the compute nodes will be;
and replace `subnet-compute-nodes` with its ID in the following
code. This is required to allow EFA work with your file system. Note that, as part of the file
system creation, we enable EFA using the EfaEnable property.

```
aws fsx create-file-system \
    --file-system-type LUSTRE \
    --storage-capacity 38400 \
    --storage-type SSD \
    --subnet-ids `subnet-compute-nodes` \
    --security-group-ids `sg-file-system` \
    --lustre-configuration DeploymentType=PERSISTENT_2,PerUnitStorageThroughput=125,EfaEnabled=true,MetadataConfiguration={Mode=AUTOMATIC} \
    --region `region`
```

Take note of the file system id returned by the previous command. In the remainder of the
tutorial, replace `fs-id` with this file system id.

## Create the cluster

1. Create the cluster with the following configurations set in the AWS ParallelCluster
   YAML configuration file:
   1. AMI based on a supported OS, such as Ubuntu 22.04.
   2. Compute nodes must use an [EFA supported instance
      type](../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types "../../../AWSEC2/latest/UserGuide/efa.md#efa-instance-types") having [Nitro v4+](../../../ec2/latest/instancetypes/ec2-nitro-instances.md "../../../ec2/latest/instancetypes/ec2-nitro-instances.md"), such as
      g6.16xlarge.
      - Compute nodes must be in the same AZ where the file system is.
      - Compute nodes must have [Efa/Enabled](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-ComputeResources-Efa-Enabled")
        set to true.
      - Compute nodes must run the configuration script `configure-efa-fsx-lustre-client.sh`
        as an [OnNodeStart](Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart "Scheduling-v3.md#yaml-Scheduling-SlurmQueues-CustomActions-OnNodeStart")
        custom action. The script, provided in the [FSx official documentation](../../../fsx/latest/LustreGuide/configure-efa-clients.md "../../../fsx/latest/LustreGuide/configure-efa-clients.md")
        and offered in our public bucket for your convenience, is meant to configure
        the FSx Lustre client on compute nodes to let them use EFA.

2. Create a cluster configuration file `config.yaml`:

```
Region: `region`
Image:
  Os: ubuntu2204
HeadNode:
  InstanceType: c5.xlarge
  Networking:
    SubnetId: `subnet-xxxxxxxxxx`
    AdditionalSecurityGroups:
        - `sg-client`
  Ssh:
    KeyName: `my-ssh-key`
Scheduling:
  Scheduler: slurm
  SlurmQueues:
    - Name: q1
      ComputeResources:
        - Name: cr1
          Instances:
            - InstanceType: g6.16xlarge
          MinCount: 1
          MaxCount: 3
          Efa:
            Enabled: true
      Networking:
        SubnetIds:
          - `subnet-xxxxxxxxxx` # Subnet in the same AZ where the file system is
        AdditionalSecurityGroups:
          - `sg-client`
        PlacementGroup:
          Enabled: false
      CustomActions:
        OnNodeStart:
          Script: https://us-east-1-aws-parallelcluster.s3.us-east-1.amazonaws.com/scripts/fsx-lustre-efa/configure-efa-fsx-lustre-client.sh
SharedStorage:
  - MountDir: /fsx
    Name: my-fsxlustre-efa-external
    StorageType: FsxLustre
    FsxLustreSettings:
      FileSystemId: `fs-id`
```

Then create a cluster using that configuration:

```
pcluster create-cluster \
    --cluster-name fsx-efa-tutorial \
    --cluster-configuration config.yaml \
    --region `region`
```

## Validate FSx with EFA is working

To verify that Lustre network traffic is using EFA, use the Lustre `lnetctl` tool
that can show the network traffic for a given network interface. To this aim, execute the following
commands in a compute node:

```
# Take note of the number of packets flowing through the interface,
# which are specified in statistics:send_count and statistics:recv_count
sudo lnetctl net show --net efa -v

# Generate traffic to the file system
echo 'Hello World' > /fsx/hello-world.txt

# Take note of the number of packets flowing through the interface,
# which are specified in statistics:send_count and statistics:recv_count
sudo lnetctl net show --net efa -v
```

If the feature is working, the number of packets flowing through the interface is expected to
increase.

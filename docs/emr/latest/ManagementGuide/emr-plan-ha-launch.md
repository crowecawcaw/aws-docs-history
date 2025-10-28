# Launch an Amazon EMR Cluster with multiple

primary nodes

This topic provides configuration details and examples for launching an
Amazon EMR cluster with multiple primary nodes.

###### Note

Amazon EMR automatically enables termination protection for all clusters that have
multiple primary nodes, and overrides any auto-termination settings that you
supply when you create the cluster. To shut down a cluster with multiple
primary nodes, you must first modify the cluster attributes to disable
termination protection. For instructions, see [Terminate an Amazon EMR Cluster with
multiple primary nodes](#emr-plan-ha-launch-terminate "#emr-plan-ha-launch-terminate").

## Prerequisites

- You can launch an Amazon EMR cluster with multiple primary nodes in both public and private VPC
  subnets. **EC2-Classic** is not supported. To launch an
  Amazon EMR cluster with multiple primary nodes in a public subnet, you must enable the instances in
  this subnet to receive a public IP address by selecting
  **Auto-assign IPv4** in the console or running the
  following command. Replace `22XXXX01` with your
  subnet ID.

```
aws ec2 modify-subnet-attribute --subnet-id subnet-`22XXXX01` --map-public-ip-on-launch
```

- To run Hive, Hue, or Oozie on an Amazon EMR cluster with multiple primary nodes, you must create an
  external metastore. For more information, see [Configuring an
  external metastore for Hive](../ReleaseGuide/emr-metastore-external-hive.md "../ReleaseGuide/emr-metastore-external-hive.md"), [Using Hue with a remote database in
  Amazon RDS](../ReleaseGuide/hue-rds.md "../ReleaseGuide/hue-rds.md"), or [Apache
  Oozie](../ReleaseGuide/emr-oozie.md "../ReleaseGuide/emr-oozie.md").
- To use Kerberos authentication in your cluster, you must configure an
  external KDC. For more information, see [Configuring Kerberos on
  Amazon Amazon EMR](emr-kerberos-configure.md "emr-kerberos-configure.md").

## Launch an Amazon EMR Cluster with multiple

primary nodes

You can launch a cluster with multiple primary nodes when you use instance groups
or instance fleets. When you use _instance groups_ with multiple
primary nodes, you must specify an instance count value of `3` for the
primary node instance group. When you use _instance fleets_ with
multiple primary nodes, you must specify the `TargetOnDemandCapacity` of
`3`, `TargetSpotCapacity` of `0` for the
primary instance fleet, and `WeightedCapacity` of `1` for each
instance type that you configure for the primary fleet.

The following examples demonstrate how to launch the cluster using the default
AMI or a custom AMI with both instance groups and instance fleets:

###### Note

You must specify the subnet ID when you launch an Amazon EMR cluster with multiple primary nodes using
the AWS CLI. Replace `22XXXX01` and `22XXXX02` with your subnet ID in the following examples.

Default AMI, instance groups

###### Example – Launching an Amazon EMR instance group cluster with

multiple primary nodes using a default AMI

```
aws emr create-cluster \
--name "ha-cluster" \
--release-label emr-6.15.0 \
--instance-groups InstanceGroupType=MASTER,InstanceCount=3,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=4,InstanceType=m5.xlarge \
--ec2-attributes KeyName=ec2_key_pair_name,InstanceProfile=EMR_EC2_DefaultRole,SubnetId=subnet-22XXXX01 \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark
```

Default AMI, instance fleets

###### Example – Launching an Amazon EMR instance fleet cluster with

multiple primary nodes using a default AMI

```
aws emr create-cluster \
--name "ha-cluster" \
--release-label emr-6.15.0 \
--instance-fleets '[
    {
        "InstanceFleetType": "MASTER",
        "TargetOnDemandCapacity": 3,
        "TargetSpotCapacity": 0,
        "LaunchSpecifications": {
            "OnDemandSpecification": {
                "AllocationStrategy": "lowest-price"
            }
        },
        "InstanceTypeConfigs": [
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.xlarge"
            },
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.2xlarge"
            },
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.4xlarge"
            }
        ],
        "Name": "Master - 1"
    },
    {
        "InstanceFleetType": "CORE",
        "TargetOnDemandCapacity": 5,
        "TargetSpotCapacity": 0,
        "LaunchSpecifications": {
            "OnDemandSpecification": {
                "AllocationStrategy": "lowest-price"
            }
        },
        "InstanceTypeConfigs": [
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.xlarge"
            },
            {
                "WeightedCapacity": 2,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.2xlarge"
            },
            {
                "WeightedCapacity": 4,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.4xlarge"
            }
        ],
        "Name": "Core - 2"
    }
]' \
 --ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetIds":["subnet-22XXXX01", "subnet-22XXXX02"]}' \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark
```

Custom AMI, instance groups

###### Example – Launching an Amazon EMR instance group cluster

with multiple primary nodes using a custom AMI

```
aws emr create-cluster \
--name "custom-ami-ha-cluster" \
--release-label emr-6.15.0 \
--instance-groups InstanceGroupType=MASTER,InstanceCount=3,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=4,InstanceType=m5.xlarge \
--ec2-attributes KeyName=ec2_key_pair_name,InstanceProfile=EMR_EC2_DefaultRole,SubnetId=subnet-22XXXX01 \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark \
--custom-ami-id ami-MyAmiID
```

Custom AMI, instance fleets

###### Example – Launching an Amazon EMR instance fleet cluster with

multiple primary nodes using a custom AMI

```
aws emr create-cluster \
--name "ha-cluster" \
--release-label emr-6.15.0 \
--instance-fleets '[
    {
        "InstanceFleetType": "MASTER",
        "TargetOnDemandCapacity": 3,
        "TargetSpotCapacity": 0,
        "LaunchSpecifications": {
            "OnDemandSpecification": {
                "AllocationStrategy": "lowest-price"
            }
        },
        "InstanceTypeConfigs": [
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.xlarge"
            },
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.2xlarge"
            },
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.4xlarge"
            }
        ],
        "Name": "Master - 1"
    },
    {
        "InstanceFleetType": "CORE",
        "TargetOnDemandCapacity": 5,
        "TargetSpotCapacity": 0,
        "LaunchSpecifications": {
            "OnDemandSpecification": {
                "AllocationStrategy": "lowest-price"
            }
        },
        "InstanceTypeConfigs": [
            {
                "WeightedCapacity": 1,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.xlarge"
            },
            {
                "WeightedCapacity": 2,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.2xlarge"
            },
            {
                "WeightedCapacity": 4,
                "BidPriceAsPercentageOfOnDemandPrice": 100,
                "InstanceType": "m5.4xlarge"
            }
        ],
        "Name": "Core - 2"
    }
]' \
--ec2-attributes '{"InstanceProfile":"EMR_EC2_DefaultRole","SubnetIds":["subnet-22XXXX01", "subnet-22XXXX02"]}' \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark \
--custom-ami-id ami-MyAmiID
```

## Terminate an Amazon EMR Cluster with

multiple primary nodes

To terminate an Amazon EMR cluster with multiple primary nodes, you must disable termination protection
before terminating the cluster, as the following example demonstrates. Replace
`j-3KVTXXXXXX7UG` with your cluster ID.

```
aws emr modify-cluster-attributes --cluster-id `j-3KVTXXXXXX7UG` --no-termination-protected
aws emr terminate-clusters --cluster-id `j-3KVTXXXXXX7UG`
```

# Amazon EMR integration with EC2 placement

groups

When you launch an Amazon EMR multiple primary node cluster on Amazon EC2, you have the
option to use placement group strategies to specify how you want the primary node
instances deployed to protect against hardware failure.

Placement group strategies are supported starting with Amazon EMR version 5.23.0 as an
option for multiple primary node clusters. Currently, only primary node types
are supported by the placement group strategy, and the `SPREAD` strategy is
applied to those primary nodes. The `SPREAD` strategy places a small
group of instances across separate underlying hardware to guard against the loss of
multiple primary nodes in the event of a hardware failure. Note that an instance
launch request could fail if there is insufficient unique hardware to fulfill the
request. For more information about EC2 placement strategies and limitations, see [Placement
groups](../../../AWSEC2/latest/UserGuide/placement-groups.md "../../../AWSEC2/latest/UserGuide/placement-groups.md") in the _EC2 User Guide for Linux
Instances_.

There is an initial limit from Amazon EC2 of 500 placement group strategy-enabled
clusters that can be launched per AWS region. Contact AWS support to request an
increase in the number of allowed placement groups. You can identify EC2 placement
groups Amazon EMR creates by tracking the key-value pair that Amazon EMR associates with the Amazon EMR
placement group strategy. For more information about EC2 cluster instance tags, see
[View cluster instances in Amazon EC2](UsingEMR_Tagging.md "UsingEMR_Tagging.md").

## Attach the placement group managed

policy to the Amazon EMRrole

The placement group strategy requires a managed policy called
`AmazonElasticMapReducePlacementGroupPolicy`, which allows Amazon EMR to
create, delete, and describe placement groups on Amazon EC2. You must attach
`AmazonElasticMapReducePlacementGroupPolicy` to the service role for
Amazon EMR before you launch an Amazon EMR cluster with multiple primary nodes.

You can alternatively attach the `AmazonEMRServicePolicy_v2` managed
policy to the Amazon EMR service role instead of the placement group managed policy.
`AmazonEMRServicePolicy_v2` allows the same access to placement
groups on Amazon EC2 as the `AmazonElasticMapReducePlacementGroupPolicy`. For
more information, see [Service role for Amazon EMR (EMR role)](emr-iam-role.md "emr-iam-role.md").

The `AmazonElasticMapReducePlacementGroupPolicy` managed policy is the
following JSON text that is created and administered by Amazon EMR.

###### Note

Because the `AmazonElasticMapReducePlacementGroupPolicy` managed
policy is updated automatically, the policy shown here may be out-of-date. Use
the AWS Management Console to view the current policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Resource": [
 "*"
 ],
 "Effect": "Allow",
 "Action": [
 "ec2:DeletePlacementGroup",
 "ec2:DescribePlacementGroups"
 ],
 "Sid": "AllowEC2Deleteplacementgroup"
 },
 {
 "Resource": [
 "arn:aws:ec2:*:*:placement-group/pg-*"
 ],
 "Effect": "Allow",
 "Action": [
 "ec2:CreatePlacementGroup"
 ],
 "Sid": "AllowEC2Createplacementgroup"
 }
 ]
}`

```

## Launch an Amazon EMR cluster with

multiple primary nodes using placement group strategy

To launch an Amazon EMR cluster that has multiple primary nodes with a placement group
strategy, attach the placement group managed policy
`AmazonElasticMapReducePlacementGroupPolicy` to the Amazon EMR role. For
more information, see [Attach the placement group managed
policy to the Amazon EMRrole](#emr-plan-ha-launch-pg-policy "#emr-plan-ha-launch-pg-policy").

Every time you use this role to start an Amazon EMR cluster with multiple primary
nodes, Amazon EMR attempts to launch a cluster with `SPREAD` strategy applied
to its primary nodes. If you use a role that does not have the placement group
managed policy `AmazonElasticMapReducePlacementGroupPolicy` attached to
it, Amazon EMR attempts to launch an Amazon EMR cluster that has multiple primary nodes
without a placement group strategy.

If you launch an Amazon EMR cluster that has multiple primary nodes with the
`placement-group-configs` parameter using the Amazon EMRAPI or CLI, Amazon EMR
only launches the cluster if the Amazon EMRrole has the placement group managed policy
`AmazonElasticMapReducePlacementGroupPolicy` attached. If the
Amazon EMRrole does not have the policy attached, the Amazon EMR cluster with multiple primary
nodes start fails.

Amazon EMR API

###### Example – Use a placement group strategy to launch an

instance group cluster with multiple primary nodes from the
Amazon EMR API

When you use the RunJobFlow action to create an Amazon EMR cluster with
multiple primary nodes, set the `PlacementGroupConfigs`
property to the following. Currently, the `MASTER`
instance role automatically uses `SPREAD` as the
placement group strategy.

```
{
   "Name":"ha-cluster",
   "PlacementGroupConfigs":[
      {
         "InstanceRole":"MASTER"
      }
   ],
   "ReleaseLabel": emr-6.15.0,
   "Instances":{
      "ec2SubnetId":"subnet-22XXXX01",
      "ec2KeyName":"ec2_key_pair_name",
      "InstanceGroups":[
         {
            "InstanceCount":3,
            "InstanceRole":"MASTER",
            "InstanceType":"m5.xlarge"
         },
         {
            "InstanceCount":4,
            "InstanceRole":"CORE",
            "InstanceType":"m5.xlarge"
         }
      ]
   },
   "JobFlowRole":"EMR_EC2_DefaultRole",
   "ServiceRole":"EMR_DefaultRole"
}
```

- Replace `ha-cluster` with the name of
  your high-availability cluster.
- Replace `subnet-22XXXX01` with your
  subnet ID.
- Replace the `ec2_key_pair_name` with
  the name of your EC2 key pair for this cluster. EC2 key pair is
  optional and only required if you want to use SSH to access your
  cluster.

AWS CLI

###### Example – Use a placement group strategy to launch an

instance fleet cluster with multiple primary nodes from the
AWS Command Line Interface

When you use the RunJobFlow action to create an Amazon EMR cluster with
multiple primary nodes, set the `PlacementGroupConfigs`
property to the following. Currently, the `MASTER`
instance role automatically uses `SPREAD` as the
placement group strategy.

```
aws emr create-cluster \
--name "ha-cluster" \
--placement-group-configs InstanceRole=MASTER \
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
--ec2-attributes '{
    "KeyName": "ec2_key_pair_name",
    "InstanceProfile": "EMR_EC2_DefaultRole",
    "SubnetIds": [
        "subnet-22XXXX01",
        "subnet-22XXXX02"
    ]
}' \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark
```

- Replace `ha-cluster` with the name of
  your high-availability cluster.
- Replace the `ec2_key_pair_name` with
  the name of your EC2 key pair for this cluster. EC2 key pair is
  optional and only required if you want to use SSH to access your
  cluster.
- Replace `subnet-22XXXX01` and
  `subnet-22XXXX02`with your subnet
  IDs.

## Launch a cluster with multiple primary nodes

without a placement group strategy

For a cluster with multiple primary nodes to launch primary nodes without the placement
group strategy, you need to do one of the following:

- Remove the placement group managed policy
  `AmazonElasticMapReducePlacementGroupPolicy`from the
  Amazon EMRrole, or
- Launch a cluster with multiple primary nodes with the `placement-group-configs`
  parameter using the Amazon EMRAPI or CLI choosing `NONE` as the
  placement group strategy.

Amazon EMR API

###### Example – Launching a cluster with multiple primary nodes without placement group

strategy using the Amazon EMRAPI.

When using the RunJobFlow action to create a cluster with multiple primary nodes,
set the `PlacementGroupConfigs` property to the
following.

```
{
   "Name":"ha-cluster",
   "PlacementGroupConfigs":[
      {
         "InstanceRole":"MASTER",
         "PlacementStrategy":"NONE"
      }
   ],
   "ReleaseLabel":"emr-5.30.1",
   "Instances":{
      "ec2SubnetId":"subnet-22XXXX01",
      "ec2KeyName":"ec2_key_pair_name",
      "InstanceGroups":[
         {
            "InstanceCount":3,
            "InstanceRole":"MASTER",
            "InstanceType":"m5.xlarge"
         },
         {
            "InstanceCount":4,
            "InstanceRole":"CORE",
            "InstanceType":"m5.xlarge"
         }
      ]
   },
   "JobFlowRole":"EMR_EC2_DefaultRole",
   "ServiceRole":"EMR_DefaultRole"
}
```

- Replace `ha-cluster` with the name of
  your high-availability cluster.
- Replace `subnet-22XXXX01` with your
  subnet ID.
- Replace the `ec2_key_pair_name` with
  the name of your EC2 key pair for this cluster. EC2 key pair is
  optional and only required if you want to use SSH to access your
  cluster.

Amazon EMR CLI

###### Example – Launching a cluster with multiple primary nodes without a placement group

strategy using the Amazon EMRCLI.

When using the RunJobFlow action to create a cluster with multiple primary nodes,
set the `PlacementGroupConfigs` property to the
following.

```
aws emr create-cluster \
--name "ha-cluster" \
--placement-group-configs InstanceRole=MASTER,PlacementStrategy=NONE \
--release-label emr-5.30.1 \
--instance-groups InstanceGroupType=MASTER,InstanceCount=3,InstanceType=m5.xlarge InstanceGroupType=CORE,InstanceCount=4,InstanceType=m5.xlarge \
--ec2-attributes KeyName=ec2_key_pair_name,InstanceProfile=EMR_EC2_DefaultRole,SubnetId=subnet-22XXXX01 \
--service-role EMR_DefaultRole \
--applications Name=Hadoop Name=Spark
```

- Replace `ha-cluster` with the name of
  your high-availability cluster.
- Replace `subnet-22XXXX01` with your
  subnet ID.
- Replace the `ec2_key_pair_name` with
  the name of your EC2 key pair for this cluster. EC2 key pair is
  optional and only required if you want to use SSH to access your
  cluster.

## Checking placement group strategy

configuration attached to the cluster with multiple primary nodes

You can use the Amazon EMR describe cluster API to see the placement group strategy
configuration attached to the cluster with multiple primary nodes.

```
aws emr describe-cluster --cluster-id "j-xxxxx"
{
   "Cluster":{
      "Id":"j-xxxxx",
      ...
      ...
      "PlacementGroups":[
         {
            "InstanceRole":"MASTER",
            "PlacementStrategy":"SPREAD"
         }
      ]
   }
}
```

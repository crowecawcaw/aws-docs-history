# Targets for AWS FIS

A target is one or more AWS resources on which an action is performed by AWS Fault Injection Service (AWS FIS)
during an experiment. Targets can be in the same AWS account as the experiment, or in a different account
using a multi-account experiment. To learn more about targeting resources in a different account,
see [Working with multi-account experiments for AWS FIS](multi-account.md "multi-account.md").

You define targets when you [create an experiment template](create-template.md "create-template.md").
You can use the same target for multiple actions in your experiment template.

AWS FIS identifies all targets at the start of the experiment, before starting any of the
actions in the actions set. AWS FIS uses the target resources that it selects for the entire
experiment. If no targets are found, the experiment fails.

###### Contents

- [Target syntax](targets.md#target-syntax "targets.md#target-syntax")
- [Resource types](targets.md#resource-types "targets.md#resource-types")
- [Identify target resources](targets.md#target-identification "targets.md#target-identification")
  - [Resource filters](targets.md#target-filters "targets.md#target-filters")
  - [Resource parameters](targets.md#target-parameters "targets.md#target-parameters")

- [Selection mode](targets.md#target-selection-mode "targets.md#target-selection-mode")
- [Example targets](targets.md#target-examples "targets.md#target-examples")
- [Example filters](targets.md#filter-examples "targets.md#filter-examples")

## Target syntax

The following is the syntax for a target.

```
{
    "targets": {
        "`target_name`": {
            "resourceType": "`resource-type`",
            "resourceArns": [
                "`resource-arn`"
            ],
            "resourceTags": {
                "`tag-key`": "`tag-value`"
            },
            "parameters": {
                "`parameter-name`": "`parameter-value`"
            },
            "filters": [
                {
                    "path": "`path-string`",
                    "values": ["`value-string`"]
                }
            ],
            "selectionMode": "`value`"
        }
    }
}
```

When you define a target, you provide the following:

**target_name**

A name for the target.

**resourceType**

The [resource type](#resource-types "#resource-types").

**resourceArns**

The Amazon Resource Names (ARN) of specific resources.

**resourceTags**

The tags applied to specific resources.

**parameters**

The [parameters](#target-parameters "#target-parameters") that identify
targets using specific attributes.

**filters**

The [resource filters](#target-filters "#target-filters") scopes the
identified target resources using specific attributes.

**selectionMode**

The [selection mode](#target-selection-mode "#target-selection-mode")
for the identified resources.

For examples, see [Example targets](#target-examples "#target-examples").

## Resource types

Each AWS FIS action is performed on a specific AWS resource type. When you
define a target, you must specify exactly one resource type. When you specify a target
for an action, the target must be the resource type supported by the action.

The following resource types are supported by AWS FIS:

- **aws:arc:zonal-shift-managed-resource** – An AWS resource that is registered with ARC zonal shift
- **aws:dsql:cluster** – An Amazon Aurora DSQL cluster
- **aws:dynamodb:global-table** – An Amazon DynamoDB
  multi-Region eventually consistent global table
- **aws:ec2:autoscaling-group** – An Amazon EC2 Auto Scaling group
- **aws:ec2:ebs-volume** – An Amazon EBS volume
- **aws:ec2:instance** – An Amazon EC2 instance
- **aws:ec2:spot-instance** – An Amazon EC2 Spot Instance
- **aws:ec2:subnet** – An Amazon VPC subnet
- **aws:ec2:transit-gateway** – A transit gateway
- **aws:ec2:vpc-endpoint** – An Amazon VPC Endpoint
- **aws:ecs:cluster** – An Amazon ECS cluster
- **aws:ecs:task** – An Amazon ECS task
- **aws:eks:cluster** – An Amazon EKS cluster
- **aws:eks:nodegroup** – An Amazon EKS node group
- **aws:eks:pod** – A Kubernetes pod
- **aws:elasticache:replicationgroup** – An ElastiCache Replication Group
- **aws:iam:role** – An IAM role
- **aws:kinesis:stream** – An Amazon Kinesis data
  stream
- **aws:lambda:function** – An AWS Lambda function
- **aws:memorydb:multi-region-cluster** – An Amazon MemoryDB multi-Region cluster
- **aws:rds:cluster** – An Amazon Aurora DB cluster
- **aws:rds:db** – An Amazon RDS DB instance
- **aws:s3:bucket** – An Amazon S3 bucket

## Identify target resources

When you define a target in the AWS FIS console, you can choose specific AWS resources
(of a specific resource type) to target. Or, you can let AWS FIS identify a group of
resources based on the criteria that you provide.

To identify your target resources, you can specify the following:

- **Resource IDs** – The resource IDs of
  specific AWS resources. All resource IDs must represent the same type of
  resource.
- **Resource tags** – The tags applied to
  specific AWS resources.
- **Resource filters** – The path and values
  that represent resources with specific attributes. For more information, see
  [Resource filters](#target-filters "#target-filters").
- **Resource parameters** – The parameters
  that represent resources that meet specific criteria. For more information, see
  [Resource parameters](#target-parameters "#target-parameters").

###### Considerations

- You can't specify both a resource ID and a resource tag for the same target.
- You can't specify both a resource ID and a resource filter for the same target.
- If you specify a resource tag with an empty tag value, it is not equivalent to a
  wildcard. It matches resources that have a tag with the specified tag key and an empty
  tag value.
- If you specify more than one tag, all specified tags have to be present on the target resource for it to be selected (`AND`).

### Resource filters

Resource filters are queries that identify target resources according to specific
attributes. AWS FIS applies the query to the output of an API action that
contains the canonical description of the AWS resource, according to the resource
type that you specify. Resources that have attributes that match the query are
included in the target definition.

Each filter is expressed as an attribute path and possible values. A path is a sequence
of elements, separated by periods, that describe the path to reach an attribute in the
output of the **Describe** action for a resource. Each period stands for the expansion of an element. Each element must be
expressed in Pascal case, even if the output of the **Describe** action for a resource is in camel case.
For example, you should use `AvailabilityZone`, not `availablityZone` as an attribute element.

```
"filters": [
    {
        "path": "`Component`.`Component`.`Component`",
        "values": [
            "`string`"
        ]
    }
],
```

The following logic applies to all resource filters:

- If multiple filters are provided, including filters with the same path, all filters have to be matched for a resource to be selected – `AND`
- If multiple values are provided for a single filter, any one value needs to be matched for a resource to be selected – `OR`
- If multiple values are found at the path location of the describe API call, any one value needs to be matched for a resource to be selected – `OR`
- To match on tag key/value pairs you should select target resources by tags instead (see above).

The following table includes the API actions and AWS CLI commands that you can use
to get the canonical descriptions for each resource type. AWS FIS runs these actions
on your behalf to apply the filters that you specify. The corresponding
documentation describes the resources that are included in the results by default.
For example, the documentation for **DescribeInstances** states that
recently terminated instances might appear in the results.

| Resource type                            | API action                                                                                                                                                                                     | AWS CLI command                                                                                                                                                                       |
| ---------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **aws:arc:zonal-shift-managed-resource** | ListManagedResources                                                                                                                                                                           | list-managed-resources                                                                                                                                                                |
| **aws:ec2:autoscaling-group**            | [DescribeAutoScalingGroups](../../../autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.md "../../../autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.md")                   | [describe-auto-scaling-groups](../../../cli/latest/reference/autoscaling/describe-auto-scaling-groups.md "../../../cli/latest/reference/autoscaling/describe-auto-scaling-groups.md") |
| **aws:ec2:ebs-volume**                   | [DescribeVolumes](../../../AWSEC2/latest/APIReference/API_DescribeVolumes.md "../../../AWSEC2/latest/APIReference/API_DescribeVolumes.md")                                                     | [describe-volumes](../../../cli/latest/reference/ec2/describe-volumes.md "../../../cli/latest/reference/ec2/describe-volumes.md")                                                     |
| **aws:ec2:instance**                     | [DescribeInstances](../../../AWSEC2/latest/APIReference/API_DescribeInstances.md "../../../AWSEC2/latest/APIReference/API_DescribeInstances.md")                                               | [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")                                               |
| **aws:ec2:subnet**                       | [DescribeSubnets](../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md "../../../AWSEC2/latest/APIReference/API_DescribeSubnets.md")                                                     | [describe-subnets](../../../cli/latest/reference/ec2/describe-subnets.md "../../../cli/latest/reference/ec2/describe-subnets.md")                                                     |
| **aws:ec2:transit-gateway**              | [DescribeTransitGateways](../../../AWSEC2/latest/APIReference/API_DescribeTransitGateways.md "../../../AWSEC2/latest/APIReference/API_DescribeTransitGateways.md")                             | [describe-transit-gateways](../../../cli/latest/reference/ec2/describe-transit-gateways.md "../../../cli/latest/reference/ec2/describe-transit-gateways.md")                          |
| **aws:ec2:vpc-endpoint**                 | [DescribeVpcEndpoints](../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md "../../../AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.md")                                      | [describe-vpc-endpoints](../../../cli/latest/reference/ec2/describe-vpc-endpoints.md "../../../cli/latest/reference/ec2/describe-vpc-endpoints.md")                                   |
| **aws:ecs:cluster**                      | [DescribeClusters](../../../AmazonECS/latest/APIReference/API_DescribeClusters.md "../../../AmazonECS/latest/APIReference/API_DescribeClusters.md")                                            | [describe-clusters](../../../cli/latest/reference/ecs/describe-clusters.md "../../../cli/latest/reference/ecs/describe-clusters.md")                                                  |
| **aws:ecs:task**                         | [DescribeTasks](../../../AmazonECS/latest/APIReference/API_DescribeTasks.md "../../../AmazonECS/latest/APIReference/API_DescribeTasks.md")                                                     | [describe-tasks](../../../cli/latest/reference/ecs/describe-tasks.md "../../../cli/latest/reference/ecs/describe-tasks.md")                                                           |
| **aws:eks:cluster**                      | [DescribeClusters](../../../eks/latest/APIReference/API_DescribeClusters.md "../../../eks/latest/APIReference/API_DescribeClusters.md")                                                        | [describe-clusters](../../../cli/latest/reference/eks/describe-clusters.md "../../../cli/latest/reference/eks/describe-clusters.md")                                                  |
| **aws:eks:nodegroup**                    | [DescribeNodegroup](../../../eks/latest/APIReference/API_DescribeNodegroup.md "../../../eks/latest/APIReference/API_DescribeNodegroup.md")                                                     | [describe-nodegroup](../../../cli/latest/reference/eks/describe-nodegroup.md "../../../cli/latest/reference/eks/describe-nodegroup.md")                                               |
| **aws:elasticache:replicationgroup**     | [DescribeReplicationGroups](../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md "../../../AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.md") | [describe-replication-groups](../../../cli/latest/reference/elasticache/describe-replication-groups.md "../../../cli/latest/reference/elasticache/describe-replication-groups.md")    |
| **aws:iam:role**                         | [ListRoles](../../../IAM/latest/APIReference/API_ListRoles.md "../../../IAM/latest/APIReference/API_ListRoles.md")                                                                             | [list-roles](../../../cli/latest/reference/iam/list-roles.md "../../../cli/latest/reference/iam/list-roles.md")                                                                       |
| **aws:kinesis:stream**                   | [DescribeStreamSummary](../../../kinesis/latest/APIReference/API_DescribeStreamSummary.md "../../../kinesis/latest/APIReference/API_DescribeStreamSummary.md")                                 | [describe-stream-summary](../../../cli/latest/reference/kinesis/describe-stream-summary.md "../../../cli/latest/reference/kinesis/describe-stream-summary.md")                        |
| **aws:lambda:function**                  | [ListFunctions](../../../lambda/latest/api/API_ListFunctions.md "../../../lambda/latest/api/API_ListFunctions.md")                                                                             | [list-functions](../../../cli/latest/reference/lambda/list-functions.md "../../../cli/latest/reference/lambda/list-functions.md")                                                     |
| **aws:memorydb:multi-region-clustern**   | [DescribeMultiRegionClusters](../../../memorydb/latest/APIReference/API_DescribeMultiRegionClusters.md "../../../memorydb/latest/APIReference/API_DescribeMultiRegionClusters.md")             | [describe-multi-region-clusters](../../../cli/latest/reference/memorydb/describe-multi-region-clusters.md "../../../cli/latest/reference/memorydb/describe-multi-region-clusters.md") |
| **aws:rds:cluster**                      | [DescribeDBClusters](../../../AmazonRDS/latest/APIReference/API_DescribeDBClusters.md "../../../AmazonRDS/latest/APIReference/API_DescribeDBClusters.md")                                      | [describe-db-clusters](../../../cli/latest/reference/rds/describe-db-clusters.md "../../../cli/latest/reference/rds/describe-db-clusters.md")                                         |
| **aws:rds:db**                           | [DescribeDBInstances](../../../AmazonRDS/latest/APIReference/API_DescribeDBInstances.md "../../../AmazonRDS/latest/APIReference/API_DescribeDBInstances.md")                                   | [describe-db-instances](../../../cli/latest/reference/rds/describe-db-instances.md "../../../cli/latest/reference/rds/describe-db-instances.md")                                      |
| **aws:s3:bucket**                        | [ListBuckets](../../../AmazonS3/latest/API/API_ListBuckets.md "../../../AmazonS3/latest/API/API_ListBuckets.md")                                                                               | [list-buckets](../../../cli/latest/reference/s3api/list-buckets.md "../../../cli/latest/reference/s3api/list-buckets.md")                                                             |
| **aws:dynamodb:global-table**            | [DescribeTable](../../../amazondynamodb/latest/APIReference/API_DescribeTable.md "../../../amazondynamodb/latest/APIReference/API_DescribeTable.md")                                           | [describe-table](../../../cli/latest/reference/dynamodb/describe-table.md "../../../cli/latest/reference/dynamodb/describe-table.md")                                                 |
| **aws:dsql:cluster**                     | [GetCluster](../../../aurora-dsql/latest/APIReference/API_GetCluster.md "../../../aurora-dsql/latest/APIReference/API_GetCluster.md")                                                          | [get-cluster](../../../cli/latest/reference/dsql/get-cluster.md "../../../cli/latest/reference/dsql/get-cluster.md")                                                                  |

For examples, see [Example filters](#filter-examples "#filter-examples").

### Resource parameters

Resource parameters identify target resources according to specific
criteria.

The following resource type supports parameters.

**aws:ec2:ebs-volume**

- `availabilityZoneIdentifier` – The code (for
  example, us-east-1a) of the Availability Zone that contains the
  target volumes.

**aws:ec2:subnet**

- `availabilityZoneIdentifier` – The code (for example, us-east-1a) or AZ
  ID (for example, use1-az1) of the Availability Zone that contains the target subnets.
- `vpc` – The VPC that contains the target subnets. Does not support more than one VPC per account.

**aws:ecs:task**

- `cluster` – The cluster that contains the target tasks.
- `service` – The service that contains the target tasks.

**aws:eks:pod**

- `availabilityZoneIdentifier` – Optional. The
  Availability Zone that contains the target pods. For example,
  `us-east-1d`. We determine the Availability Zone of
  a pod by comparing its hostIP and the CIDR of the cluster subnet.
- `clusterIdentifier` – Required. The name or ARN
  of the target EKS cluster.
- `namespace` – Required. The Kubernetes namespace
  of the target pods.
- `selectorType` – Required. The selector type.
  The possible values are `labelSelector`, `deploymentName`,
  and `podName`.
- `selectorValue` – Required. The selector value.
  This value depends on the value of `selectorType`.
- `targetContainerName` – Optional. The name of
  the target container as defined in the pod spec. The default is the first
  container defined in each target pod spec.

**aws:lambda:function**

- `functionQualifier` –
  Optional. The version or alias of the function to target. If no qualifier is specified all invocations will be considered for targeting.
  If an alias with multiple versions is specified, all versions included in the alias will be considered for targeting as long as they are invoked using an ARN containing the alias.
  If the special alias `$LATEST` is used, invocations to the base function ARN and invocations
  including `$LATEST` in the ARN will be considered for fault injection. For more information on Lambda versions, see
  [Manage Lambda function versions](../../../lambda/latest/dg/configuration-versions.md "../../../lambda/latest/dg/configuration-versions.md") in the _AWS Lambda user guide_.

**aws:rds:cluster**

- `writerAvailabilityZoneIdentifiers` –
  Optional. The Availability Zones of the writer of the DB cluster.
  Possible values are: a comma separated list of Availability Zone
  identifiers, `all`.

**aws:rds:db**

- `availabilityZoneIdentifiers` –
  Optional. The Availability Zones of the DB instance to be affected.
  Possible values are: a comma separated list of Availability Zone
  identifiers, `all`.

**aws:elasticache:replicationgroup**

- `availabilityZoneIdentifier` – Required. The
  code (for example, us-east-1a) or AZ ID (for example, use1-az1)
  of the Availability Zone that contains the target nodes.

## Selection mode

You scope the identified resources by specifying a selection mode. AWS FIS supports the following
selection modes:

- `ALL` – Run the action on all targets.
- `COUNT(n)` – Run the action on the specified number of targets, chosen
  from the identified targets at random. For example, COUNT(1) selects one of the
  identified targets.
- `PERCENT(n)` – Run the action on the specified percentage of targets,
  chosen from the identified targets at random. For example, PERCENT(25)
  selects 25% of the identified targets.

If you have an odd number of resources and specify 50%, AWS FIS rounds down. For
example, if you add five Amazon EC2 instances as targets and scope to 50%, AWS FIS rounds down
to two instances. You can't specify a percentage that is less than one resource. For
example, if you add four Amazon EC2 instances and scope to 5%, AWS FIS can't select an
instance.

If you define multiple targets using the same target resource type, AWS FIS can select the
same resource multiple times.

Regardless of which selection mode you use, if the scope that you specify identifies
no resources, the experiment fails.

## Example targets

The following are example targets.

###### Examples

- [Instances in the specified VPC with the specified tags](#target-instances "#target-instances")
- [Tasks with the specified parameters](#target-tasks "#target-tasks")

###### Example: Instances in the specified VPC with the specified tags

The possible targets for this example are Amazon EC2 instances in the specified VPC
with the tag env=prod. The selection mode specifies that AWS FIS
chooses one of these targets at random.

```
{
    "targets": {
        "`randomInstance`": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "`env`": "`prod`"
            },
            "filters": [
                {
                    "path": "VpcId",
                    "values": [
                        "`vpc-aabbcc11223344556`"
                    ]
                }
            ],
            "selectionMode": "COUNT(1)"
        }
    }
}
```

###### Example: Tasks with the specified parameters

The possible targets for this example are Amazon ECS tasks with the specified cluster
and service. The selection mode specifies that AWS FIS choose one of these targets at
random.

```
{
    "targets": {
        "`randomTask`": {
            "resourceType": "aws:ecs:task",
            "parameters": {
                "cluster": "`myCluster`",
                "service": "`myService`"
            },
            "selectionMode": "COUNT(1)"
        }
    }
}
```

## Example filters

The following are example filters.

###### Examples

- [EC2 instances](#filter-instances "#filter-instances")
- [DB clusters](#filter-db-clusters "#filter-db-clusters")

###### Example: EC2 instances

When you specify a filter for an action that supports the
**aws:ec2:instance** resource type, AWS FIS uses the Amazon EC2
**describe-instances** command and applies the filter to identify
the targets.

The **describe-instances** command returns JSON output where each
instance is a structure under `Instances`. The following is partial
output that includes fields marked with `italics`. We'll
provide examples that use these fields to specify an attribute path from the
structure of the JSON output.

```
{
    "Reservations": [
        {
            "Groups": [],
            "Instances": [
                {
                    "ImageId": "ami-00111111111111111",
                    "InstanceId": "i-00aaaaaaaaaaaaaaa",
                    "InstanceType": "t2.micro",
                    "KeyName": "virginia-kp",
                    "LaunchTime": "2020-09-30T11:38:17.000Z",
                    "Monitoring": {
                        "State": "disabled"
                    },
                    "Placement": {
                        "`AvailabilityZone`": "us-east-1a",
                        "GroupName": "",
                        "Tenancy": "default"
                    },
                    "PrivateDnsName": "ip-10-0-1-240.ec2.internal",
                    "PrivateIpAddress": "10.0.1.240",
                    "ProductCodes": [],
                    "PublicDnsName": "ec2-203-0-113-17.compute-1.amazonaws.com",
                    "PublicIpAddress": "203.0.113.17",
                    "State": {
                        "Code": 16,
                        "`Name`": "running"
                    },
                    "StateTransitionReason": "",
                    "`SubnetId`": "subnet-aabbcc11223344556",
                    "VpcId": "vpc-00bbbbbbbbbbbbbbbbb",
                    ...
                    "NetworkInterfaces": [
                    {
                        ...
                        "Groups": [
                            {
                                "GroupName": "sec-group-1",
                                "`GroupId`": "sg-a0011223344556677"
                            },
                            {
                                "GroupName": "sec-group-1",
                                "`GroupId`": "sg-b9988776655443322"
                            }
                        ],
                        ...
                    },
                    ...
                },
                ...
                {
                    ...
                }
            ],
            "OwnerId": "123456789012",
            "ReservationId": "r-aaaaaabbbbb111111"
        },
        ...
    ]
}
```

To select instances in a specific Availability Zone using a resource filter, specify the
attribute path for `AvailabilityZone` and the code for the Availability Zone as
the value. For example:

```
"filters": [
    {
        "path": "Placement.AvailabilityZone",
        "values": [ "us-east-1a" ]
    }
],
```

To select instances in a specific subnet using a resource filter, specify the
attribute path for `SubnetId` and the ID of the subnet as the value.
For example:

```
"filters": [
    {
        "path": "SubnetId",
        "values": [ "subnet-aabbcc11223344556" ]
    }
],
```

To select instances that are in a specific instance state, specify the attribute path
for `Name` and one of the following state names as the value: `pending` |
`running` | `shutting-down` | `terminated` | `stopping` |
`stopped`. For example:

```
"filters": [
    {
        "path": "State.Name",
        "values": [ "running" ]
    }
],
```

To select instances that have _any_ of a number of security groups attached, specify a single filter with the attribute path for `GroupId` and multiple security group IDs. For example:

```
"filters": [
    {
        "path": "NetworkInterfaces.Groups.GroupId",
        "values": [
                "sg-a0011223344556677",
                "sg-f1100110011001100"
            ]
    }
],
```

To select instances that have _all_ of a number of security groups attached, specify multiple filters with the attribute path for `GroupId` and a single security group ID for each filter. For example:

```
"filters": [
    {
        "path": "NetworkInterfaces.Groups.GroupId",
        "values": [
            "sg-a0011223344556677"
        ]
    },
    {
        "path": "NetworkInterfaces.Groups.GroupId",
        "values": [
            "sg-b9988776655443322"
        ]
    }
],
```

###### Example: Amazon RDS cluster (DB cluster)

When you specify a filter for an action that supports the
**aws:rds:cluster** resource type, AWS FIS runs the Amazon RDS
**describe-db-clusters** command and applies the filter to
identify the targets.

The **describe-db-clusters** command returns JSON output similar to the following
for each DB cluster. The following is partial output that includes fields marked with `italics`.
We'll provide examples that use these fields to specify an attribute path from the structure of the
JSON output.

```
[
    {
        "AllocatedStorage": 1,
        "`AvailabilityZones`": [
            "us-east-2a",
            "us-east-2b",
            "us-east-2c"
        ],
        "BackupRetentionPeriod": 7,
        "DatabaseName": "",
        "DBClusterIdentifier": "database-1",
        "DBClusterParameterGroup": "default.aurora-postgresql11",
        "DBSubnetGroup": "default-vpc-01234567abc123456",
        "Status": "available",
        "EarliestRestorableTime": "2020-11-13T15:08:32.211Z",
        "Endpoint": "database-1.cluster-example.us-east-2.rds.amazonaws.com",
        "ReaderEndpoint": "database-1.cluster-ro-example.us-east-2.rds.amazonaws.com",
        "MultiAZ": false,
        "`Engine`": "aurora-postgresql",
        "EngineVersion": "11.7",
        ...
    }
]
```

To apply a resource filter that returns only the DB clusters that use a specific
DB engine, specify the attribute path as `Engine` and the value as
`aurora-postgresql` as shown in the following example.

```
"filters": [
    {
        "path": "Engine",
        "values": [ "aurora-postgresql" ]
    }
],
```

To apply a resource filter that returns only the DB clusters in a specific
Availability Zone, specify the attribute path and value as shown in the following
example.

```
"filters": [
    {
        "path": "AvailabilityZones",
        "values": [ "us-east-2a" ]
    }
],
```

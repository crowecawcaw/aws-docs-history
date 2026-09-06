

# Targets for AWS FIS
<a name="targets"></a>

A target is one or more AWS resources on which an action is performed by AWS Fault Injection Service (AWS FIS) during an experiment. Targets can be in the same AWS account as the experiment, or in a different account using a multi-account experiment. To learn more about targeting resources in a different account, see [Working with multi-account experiments for AWS FIS](multi-account.md).

You define targets when you [create an experiment template](create-template.md). You can use the same target for multiple actions in your experiment template.

AWS FIS identifies all targets at the start of the experiment, before starting any of the actions in the actions set. AWS FIS uses the target resources that it selects for the entire experiment. If no targets are found, the experiment fails.

**Contents**
+ [Target syntax](#target-syntax)
+ [Resource types](#resource-types)
+ [Identify target resources](#target-identification)
  + [Resource filters](#target-filters)
  + [Resource parameters](#target-parameters)
+ [Selection mode](#target-selection-mode)
+ [Example targets](#target-examples)
+ [Example filters](#filter-examples)

## Target syntax
<a name="target-syntax"></a>

The following is the syntax for a target.

```
{
    "targets": {
        "{{target_name}}": {
            "resourceType": "{{resource-type}}",
            "resourceArns": [
                "{{resource-arn}}"
            ],
            "resourceTags": {
                "{{tag-key}}": "{{tag-value}}"
            },
            "parameters": {
                "{{parameter-name}}": "{{parameter-value}}"
            },
            "filters": [
                {
                    "path": "{{path-string}}",
                    "values": ["{{value-string}}"]
                }
            ],
            "selectionMode": "{{value}}"
        }
    }
}
```

When you define a target, you provide the following:

**target\_name**  
A name for the target.

**resourceType**  
The [resource type](#resource-types).

**resourceArns**  
The Amazon Resource Names (ARN) of specific resources.

**resourceTags**  
The tags applied to specific resources.

**parameters**  
The [parameters](#target-parameters) that identify targets using specific attributes.

**filters**  
The [resource filters](#target-filters) scopes the identified target resources using specific attributes.

**selectionMode**  
The [selection mode](#target-selection-mode) for the identified resources.

For examples, see [Example targets](#target-examples).

## Resource types
<a name="resource-types"></a>

Each AWS FIS action is performed on a specific AWS resource type. When you define a target, you must specify exactly one resource type. When you specify a target for an action, the target must be the resource type supported by the action.

The following resource types are supported by AWS FIS:
+ **aws:arc:zonal-shift-managed-resource** – An AWS resource that is registered with ARC zonal shift
+ **aws:directconnect:virtual-interface** – A Direct Connect Virtual Interface 
+ **aws:dsql:cluster** – An Amazon Aurora DSQL cluster 
+ **aws:dynamodb:global-table** – An Amazon DynamoDB multi-Region global table
+ **aws:ec2:autoscaling-group** – An Amazon EC2 Auto Scaling group
+ **aws:ec2:ebs-volume** – An Amazon EBS volume
+ **aws:ec2:instance** – An Amazon EC2 instance
+ **aws:ec2:spot-instance** – An Amazon EC2 Spot Instance
+ **aws:ec2:subnet** – An Amazon VPC subnet
+ **aws:ec2:transit-gateway** – A transit gateway
+ **aws:ec2:vpc-endpoint** – An Amazon VPC Endpoint
+ **aws:ecs:cluster** – An Amazon ECS cluster
+ **aws:ecs:task** – An Amazon ECS task
+ **aws:eks:cluster** – An Amazon EKS cluster
+ **aws:eks:nodegroup** – An Amazon EKS node group
+ **aws:eks:pod** – A Kubernetes pod
+ **aws:elasticache:replicationgroup** – An ElastiCache Replication Group
+ **aws:iam:role** – An IAM role
+ **aws:kinesis:stream** – An Amazon Kinesis data stream
+ **aws:lambda:function ** – An AWS Lambda function
+ **aws:memorydb:multi-region-cluster ** – An Amazon MemoryDB multi-Region cluster
+ **aws:rds:cluster** – An Amazon Aurora DB cluster
+ **aws:rds:db** – An Amazon RDS DB instance
+ **aws:s3:bucket** – An Amazon S3 bucket

## Identify target resources
<a name="target-identification"></a>

When you define a target in the AWS FIS console, you can choose specific AWS resources (of a specific resource type) to target. Or, you can let AWS FIS identify a group of resources based on the criteria that you provide.

To identify your target resources, you can specify the following:
+ **Resource IDs** – The resource IDs of specific AWS resources. All resource IDs must represent the same type of resource.
+ **Resource tags** – The tags applied to specific AWS resources.
+ **Resource filters** – The path and values that represent resources with specific attributes. For more information, see [Resource filters](#target-filters).
+ **Resource parameters** – The parameters that represent resources that meet specific criteria. For more information, see [Resource parameters](#target-parameters).

**Considerations**
+ You can't specify both a resource ID and a resource tag for the same target.
+ You can't specify both a resource ID and a resource filter for the same target.
+ If you specify a resource tag with an empty tag value, it is not equivalent to a wildcard. It matches resources that have a tag with the specified tag key and an empty tag value.
+ If you specify more than one tag, all specified tags have to be present on the target resource for it to be selected (`AND`).

### Resource filters
<a name="target-filters"></a>

Resource filters are queries that identify target resources according to specific attributes. AWS FIS applies the query to the output of an API action that contains the canonical description of the AWS resource, according to the resource type that you specify. Resources that have attributes that match the query are included in the target definition.

Each filter is expressed as an attribute path and possible values. A path is a sequence of elements, separated by periods, that describe the path to reach an attribute in the output of the **Describe** action for a resource. Each period stands for the expansion of an element. Each element must be expressed in Pascal case, even if the output of the **Describe** action for a resource is in camel case. For example, you should use `AvailabilityZone`, not `availablityZone` as an attribute element.

```
"filters": [
    {
        "path": "{{Component}}.{{Component}}.{{Component}}",
        "values": [ 
            "{{string}}" 
        ]
    }
],
```

The following logic applies to all resource filters:
+ If multiple filters are provided, including filters with the same path, all filters have to be matched for a resource to be selected – `AND`
+ If multiple values are provided for a single filter, any one value needs to be matched for a resource to be selected – `OR`
+ If multiple values are found at the path location of the describe API call, any one value needs to be matched for a resource to be selected – `OR`
+ To match on tag key/value pairs you should select target resources by tags instead (see above).

The following table includes the API actions and AWS CLI commands that you can use to get the canonical descriptions for each resource type. AWS FIS runs these actions on your behalf to apply the filters that you specify. The corresponding documentation describes the resources that are included in the results by default. For example, the documentation for **DescribeInstances** states that recently terminated instances might appear in the results.


| Resource type | API action | AWS CLI command | 
| --- | --- | --- | 
| aws:arc:zonal-shift-managed-resource | ListManagedResources | list-managed-resources | 
| aws:directconnect:virtual-interface | [DescribeVirtualInterfaces](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeVirtualInterfaces.html) | [describe-virtual-interfaces](https://docs.aws.amazon.com/cli/latest/reference/directconnect/describe-virtual-interfaces.html) | 
| aws:ec2:autoscaling-group | [DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) | [describe-auto-scaling-groups](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-auto-scaling-groups.html) | 
| aws:ec2:ebs-volume | [DescribeVolumes](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html) | [describe-volumes](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-volumes.html) | 
| aws:ec2:instance | [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) | [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) | 
| aws:ec2:subnet | [DescribeSubnets](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html) | [describe-subnets](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-subnets.html) | 
| aws:ec2:transit-gateway | [DescribeTransitGateways](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeTransitGateways.html) | [describe-transit-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-transit-gateways.html) | 
| aws:ec2:vpc-endpoint | [DescribeVpcEndpoints](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpoints.html) | [describe-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html) | 
| aws:ecs:cluster | [DescribeClusters](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeClusters.html) | [describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-clusters.html) | 
| aws:ecs:task | [DescribeTasks](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DescribeTasks.html) | [describe-tasks](https://docs.aws.amazon.com/cli/latest/reference/ecs/describe-tasks.html) | 
| aws:eks:cluster | [DescribeClusters](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeClusters.html) | [describe-clusters](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-clusters.html) | 
| aws:eks:nodegroup | [DescribeNodegroup](https://docs.aws.amazon.com/eks/latest/APIReference/API_DescribeNodegroup.html) | [describe-nodegroup](https://docs.aws.amazon.com/cli/latest/reference/eks/describe-nodegroup.html) | 
| aws:elasticache:replicationgroup | [DescribeReplicationGroups](https://docs.aws.amazon.com/AmazonElastiCache/latest/APIReference/API_DescribeReplicationGroups.html) | [describe-replication-groups](https://docs.aws.amazon.com/cli/latest/reference/elasticache/describe-replication-groups.html) | 
| aws:iam:role | [ListRoles](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListRoles.html) | [list-roles](https://docs.aws.amazon.com/cli/latest/reference/iam/list-roles.html) | 
| aws:kinesis:stream | [DescribeStreamSummary](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DescribeStreamSummary.html) | [describe-stream-summary](https://docs.aws.amazon.com/cli/latest/reference/kinesis/describe-stream-summary.html) | 
| aws:lambda:function | [ListFunctions](https://docs.aws.amazon.com/lambda/latest/api/API_ListFunctions.html) | [list-functions](https://docs.aws.amazon.com/cli/latest/reference/lambda/list-functions.html) | 
| aws:memorydb:multi-region-clustern | [DescribeMultiRegionClusters](https://docs.aws.amazon.com/memorydb/latest/APIReference/API_DescribeMultiRegionClusters.html) | [describe-multi-region-clusters](https://docs.aws.amazon.com/cli/latest/reference/memorydb/describe-multi-region-clusters.html) | 
| aws:rds:cluster | [DescribeDBClusters](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBClusters.html) | [describe-db-clusters](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-clusters.html) | 
| aws:rds:db | [DescribeDBInstances](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html) | [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) | 
| aws:s3:bucket | [ListBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html) | [list-buckets](https://docs.aws.amazon.com/cli/latest/reference/s3api/list-buckets.html) | 
| aws:dynamodb:global-table | [DescribeTable](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_DescribeTable.html) | [describe-table](https://docs.aws.amazon.com/cli/latest/reference/dynamodb/describe-table.html) | 
| aws:dsql:cluster | [GetCluster](https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_GetCluster.html) | [get-cluster](https://docs.aws.amazon.com/cli/latest/reference/dsql/get-cluster.html) | 

For examples, see [Example filters](#filter-examples).

### Resource parameters
<a name="target-parameters"></a>

Resource parameters identify target resources according to specific criteria.

The following resource type supports parameters.

**aws:ec2:ebs-volume**  
+ `availabilityZoneIdentifier` – The code (for example, us-east-1a) of the Availability Zone that contains the target volumes.

**aws:ec2:subnet**  
+ `availabilityZoneIdentifier` – The code (for example, us-east-1a) or AZ ID (for example, use1-az1) of the Availability Zone that contains the target subnets.
+ `vpc` – The VPC that contains the target subnets. Does not support more than one VPC per account.

**aws:ecs:task**  
+ `cluster` – The cluster that contains the target tasks.
+ `service` – The service that contains the target tasks.

**aws:eks:pod**  
+ `availabilityZoneIdentifier` – Optional. The Availability Zone that contains the target pods. For example, `us-east-1d`. We determine the Availability Zone of a pod by comparing its hostIP and the CIDR of the cluster subnet.
+ `clusterIdentifier` – Required. The name or ARN of the target EKS cluster.
+ `namespace` – Required. The Kubernetes namespace of the target pods.
+ `selectorType` – Required. The selector type. The possible values are `labelSelector`, `deploymentName`, and `podName`.
+ `selectorValue` – Required. The selector value. This value depends on the value of `selectorType`.
+ `targetContainerName` – Optional. The name of the target container as defined in the pod spec. The default is the first container defined in each target pod spec.

** aws:lambda:function **  
+ `functionQualifier` – Optional. The version or alias of the function to target. If no qualifier is specified all invocations will be considered for targeting. If an alias with multiple versions is specified, all versions included in the alias will be considered for targeting as long as they are invoked using an ARN containing the alias. If the special alias `$LATEST` is used, invocations to the base function ARN and invocations including `$LATEST` in the ARN will be considered for fault injection. For more information on Lambda versions, see [Manage Lambda function versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) in the *AWS Lambda user guide*.

** aws:rds:cluster **  
+ `writerAvailabilityZoneIdentifiers` – Optional. The Availability Zones of the writer of the DB cluster. Possible values are: a comma separated list of Availability Zone identifiers, `all`.

** aws:rds:db **  
+ `availabilityZoneIdentifiers` – Optional. The Availability Zones of the DB instance to be affected. Possible values are: a comma separated list of Availability Zone identifiers, `all`.

**aws:elasticache:replicationgroup**  
+ `availabilityZoneIdentifier` – Required. The code (for example, us-east-1a) or AZ ID (for example, use1-az1) of the Availability Zone that contains the target nodes.

## Selection mode
<a name="target-selection-mode"></a>

You scope the identified resources by specifying a selection mode. AWS FIS supports the following selection modes:
+ `ALL` – Run the action on all targets.
+ `COUNT(n)` – Run the action on the specified number of targets, chosen from the identified targets at random. For example, COUNT(1) selects one of the identified targets.
+ `PERCENT(n)` – Run the action on the specified percentage of targets, chosen from the identified targets at random. For example, PERCENT(25) selects 25% of the identified targets.

If you have an odd number of resources and specify 50%, AWS FIS rounds down. For example, if you add five Amazon EC2 instances as targets and scope to 50%, AWS FIS rounds down to two instances. You can't specify a percentage that is less than one resource. For example, if you add four Amazon EC2 instances and scope to 5%, AWS FIS can't select an instance.

If you define multiple targets using the same target resource type, AWS FIS can select the same resource multiple times.

Regardless of which selection mode you use, if the scope that you specify identifies no resources, the experiment fails.

## Example targets
<a name="target-examples"></a>

The following are example targets.

**Examples**
+ [Instances in the specified VPC with the specified tags](#target-instances)
+ [Tasks with the specified parameters](#target-tasks)<a name="target-instances"></a>

**Example: Instances in the specified VPC with the specified tags**  
The possible targets for this example are Amazon EC2 instances in the specified VPC with the tag env=prod. The selection mode specifies that AWS FIS chooses one of these targets at random.

```
{
    "targets": {
        "{{randomInstance}}": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "{{env}}": "{{prod}}"
            },
            "filters": [
                {
                    "path": "VpcId",
                    "values": [
                        "{{vpc-aabbcc11223344556}}"
                    ]
                }
            ],
            "selectionMode": "COUNT(1)"
        }
    }
}
```<a name="target-tasks"></a>

**Example: Tasks with the specified parameters**  
The possible targets for this example are Amazon ECS tasks with the specified cluster and service. The selection mode specifies that AWS FIS choose one of these targets at random.

```
{
    "targets": {
        "{{randomTask}}": {
            "resourceType": "aws:ecs:task",
            "parameters": {
                "cluster": "{{myCluster}}",
                "service": "{{myService}}"
            },
            "selectionMode": "COUNT(1)"
        }
    }
}
```

## Example filters
<a name="filter-examples"></a>

The following are example filters.

**Examples**
+ [EC2 instances](#filter-instances)
+ [DB clusters](#filter-db-clusters)<a name="filter-instances"></a>

**Example: EC2 instances**  
When you specify a filter for an action that supports the **aws:ec2:instance** resource type, AWS FIS uses the Amazon EC2 **describe-instances** command and applies the filter to identify the targets.

The **describe-instances** command returns JSON output where each instance is a structure under `Instances`. The following is partial output that includes fields marked with {{italics}}. We'll provide examples that use these fields to specify an attribute path from the structure of the JSON output.

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
                        "{{AvailabilityZone}}": "us-east-1a",
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
                        "{{Name}}": "running"
                    },
                    "StateTransitionReason": "",
                    "{{SubnetId}}": "subnet-aabbcc11223344556",
                    "VpcId": "vpc-00bbbbbbbbbbbbbbbbb",
                    ...
                    "NetworkInterfaces": [
                    {
                        ...
                        "Groups": [
                            {
                                "GroupName": "sec-group-1",
                                "{{GroupId}}": "sg-a0011223344556677"
                            },
                            {
                                "GroupName": "sec-group-1",
                                "{{GroupId}}": "sg-b9988776655443322"
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

To select instances in a specific Availability Zone using a resource filter, specify the attribute path for `AvailabilityZone` and the code for the Availability Zone as the value. For example:

```
"filters": [
    {
        "path": "Placement.AvailabilityZone",
        "values": [ "us-east-1a" ]
    }
],
```

To select instances in a specific subnet using a resource filter, specify the attribute path for `SubnetId` and the ID of the subnet as the value. For example:

```
"filters": [
    {
        "path": "SubnetId",
        "values": [ "subnet-aabbcc11223344556" ]
    }
],
```

To select instances that are in a specific instance state, specify the attribute path for `Name` and one of the following state names as the value: `pending` \| `running` \| `shutting-down` \| `terminated` \| `stopping` \| `stopped`. For example:

```
"filters": [
    {
        "path": "State.Name",
        "values": [ "running" ]
    }
],
```

To select instances that have *any* of a number of security groups attached, specify a single filter with the attribute path for `GroupId` and multiple security group IDs. For example:

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

To select instances that have *all* of a number of security groups attached, specify multiple filters with the attribute path for `GroupId` and a single security group ID for each filter. For example:

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
```<a name="filter-db-clusters"></a>

**Example: Amazon RDS cluster (DB cluster)**  
When you specify a filter for an action that supports the **aws:rds:cluster** resource type, AWS FIS runs the Amazon RDS **describe-db-clusters** command and applies the filter to identify the targets.

The **describe-db-clusters** command returns JSON output similar to the following for each DB cluster. The following is partial output that includes fields marked with {{italics}}. We'll provide examples that use these fields to specify an attribute path from the structure of the JSON output.

```
[
    {
        "AllocatedStorage": 1,
        "{{AvailabilityZones}}": [
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
        "{{Engine}}": "aurora-postgresql",
        "EngineVersion": "11.7",
        ...
    }
]
```

To apply a resource filter that returns only the DB clusters that use a specific DB engine, specify the attribute path as `Engine` and the value as `aurora-postgresql` as shown in the following example.

```
"filters": [
    {
        "path": "Engine",
        "values": [ "aurora-postgresql" ]
    }
],
```

To apply a resource filter that returns only the DB clusters in a specific Availability Zone, specify the attribute path and value as shown in the following example.

```
"filters": [
    {
        "path": "AvailabilityZones",
        "values": [ "us-east-2a" ] 
    }
],
```
# Cross-Region: Connectivity

You can use the Cross-Region: Connectivity scenario to block application network traffic from the experiment Region to the destination Region and pause cross-Region replication for Amazon S3 and Amazon DynamoDB multi-Region global tables. Cross Region: Connectivity affects outbound application traffic from the Region in which you run the experiment (_experiment Region_). Stateless inbound traffic from the Region you wish to isolate from the _experiment region_ (_destination Region_) may not be blocked. Traffic from AWS managed services may not be blocked.

This scenario can be used to demonstrate that multi-Region applications operate as expected when resources in the destination Region are not accessible from the experiment Region. It includes blocking network traffic from the experiment Region to the destination Region by targeting transit gateways and route tables. It also pauses cross-Region replication for S3 and DynamoDB global tables. By default, actions for which no targets are found will be skipped.

## Actions

Together, the following actions block cross-Region connectivity for the included AWS services. The actions are run in parallel. By default, the scenario blocks traffic for 3 hours, which you can increase up to a maximum 12 Hour duration.

### Disrupt Transit Gateway Connectivity

Cross Region: Connectivity includes [aws:network:transit-gateway-disrupt-cross-region-connectivity](fis-actions-reference.md#network-actions-reference "fis-actions-reference.md#network-actions-reference") to block cross-Region network traffic from VPCs in the _experiment Region_ to VPCs in the _destination Region_ connected by a transit gateway. This does not affect access to VPC endpoints within the _experiment Region_ but will block traffic from the _experiment Region_ destined for a VPC endpoint in the _destination Region_.

This action targets transit gateways connecting the _experiment Region_ and the _destination Region_. By default, it targets transit gateways with a [tag](../../../vpc/latest/tgw/tgw-transit-gateways.md#tgw-tagging "../../../vpc/latest/tgw/tgw-transit-gateways.md#tgw-tagging") named `DisruptTransitGateway` with a value of `Allowed`. You can add this tag to your transit gateways or replace the default tag with your own tag in the experiment template. By default, if no valid transit gateways are found this action will be skipped.

### Disrupt Subnet Connectivity

Cross Region: Connectivity includes [aws:network:route-table-disrupt-cross-region-connectivity](fis-actions-reference.md#network-actions-reference "fis-actions-reference.md#network-actions-reference") to block cross-Region network traffic from VPCs in the _experiment Region_ to public AWS IP blocks in the _destination Region_. These public IP blocks include AWS service endpoints in the _destination Region_, e.g. the S3 regional endpoint, and AWS IP blocks for managed services, e.g. the IP addresses used for load balancers and Amazon API Gateway. This action also blocks network connectivity over cross-Region VPC Peering connections from the _experiment Region_ to the _destination Region_. It does not affect access to VPC endpoints in the _experiment Region_ but will block traffic from the _experiment Region_ destined for a VPC endpoint in the _destination Region_.

This action targets subnets in the experiment Region. By default, it targets subnets with a [tag](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") named `DisruptSubnet` with a value of `Allowed`. You can add this tag to your subnets or replace the default tag with your own tag in the experiment template. By default, if no valid subnets are found this action will be skipped.

### Disrupt VPC Endpoint Connectivity

Cross Region: Connectivity includes [aws:network:disrupt-vpc-endpoint](fis-actions-reference.md#network-actions-reference "fis-actions-reference.md#network-actions-reference") disrupt connectivity to a service associated with the target VPC endpoints. For example, if a VPC endpoint creates a Private Link to com.amazonaws.us-east-1.ec2, then the connectivity to that service will be disrupted.

This action targets VPC endpoints in the experiment region. By default, it targets interface VPC endpoints with a [tag](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") named DisruptVpcEndpoint with a value `Allowed`. You can add this tag to your VPC endpoints or replace the default tag with your own tag in the experiment template. By default, if no valid VPC endpoints are found this action will be skipped.

### Pause S3 Replication

Cross Region: Connectivity includes [aws:s3:bucket-pause-replication](fis-actions-reference.md#s3-actions-reference-fis "fis-actions-reference.md#s3-actions-reference-fis") to pause S3 replication from the _experiment Region_ to the _destination Region_ for the targeted buckets. Replication from the _destination Region_ to the _experiment Region_ will be unaffected. After the scenario ends, bucket replication will resume from the point it was paused. Note that the time it takes for replication to keep all objects in sync will vary based on the duration of the experiment, and the rate of object upload to the bucket.

This action targets S3 buckets in the experiment Region with [Cross-Region Replication](../../../AmazonS3/latest/userguide/replication.md "../../../AmazonS3/latest/userguide/replication.md") (CRR) enabled to an S3 bucket in the destination Region. By default, it targets buckets with a [tag](../../../AmazonS3/latest/userguide/view-bucket-properties.md "../../../AmazonS3/latest/userguide/view-bucket-properties.md")
named `DisruptS3` with a value of `Allowed`. You can add this tag to your buckets or replace the default tag with your own tag in the experiment template. By default, if no valid buckets are found this action will be skipped.

### Pause DynamoDB Replication

Cross-Region: Connectivity includes [aws:dynamodb:global-table-pause-replication](fis-actions-reference.md#dynamodb-actions-reference "fis-actions-reference.md#dynamodb-actions-reference")
to pause replication between the experiment Region and all other Regions, including the destination Region.
This prevents replication into and out of the _experiment Region_ but does not affect replication between other Regions.
After the scenario ends, table replication will resume from the point it was paused.
Note that the time it takes for replication to keep all data in sync will vary based on the duration of the experiment and the rate of changes to the table.

This action targets both DynamoDB multi-Region strongly and eventually consistent global tables in the experiment Region.
By default, it targets tables with a [tag](../../../amazondynamodb/latest/developerguide/Tagging.md "../../../amazondynamodb/latest/developerguide/Tagging.md") named `DisruptDynamoDb` with a
value of `Allowed`. You can add this tag to your tables or replace the default tag with your own tag in the experiment template.
By default, if no valid global tables are found this action will be skipped.

### Pause MemoryDB multi-Region Replication

Cross-Region: Connectivity includes [aws:memorydb:multi-region-cluster-pause-replication](fis-actions-reference.md#memorydb-actions-reference "fis-actions-reference.md#memorydb-actions-reference")
to pause replication from the regional member cluster in the experiment Region to the rest of the clusters in the targeted multi-Region cluster.
Replication between other regional member clusters will be unaffected. After the scenario ends, replication will resume from the point it was paused.
Note that the time for replication to sync data between the member clusters will vary based on the duration of the experiment,
and the rate of data written to the clusters.

This action targets MemoryDB Multi-Region clusters with a regional member in the experiment Region.
By default, it targets multi-Region clusters with a [tag](../../../amazondynamodb/latest/developerguide/Tagging.md "../../../amazondynamodb/latest/developerguide/Tagging.md") named `DisruptMemoryDB` with a
value of `Allowed`. You can add this tag to your multi-Region clusters or replace the default tag with your own tag in the experiment template.
By default, if no valid clusters are found this action will be skipped.

## Limitations

- This scenario does not include [stop conditions](stop-conditions.md "stop-conditions.md"). The correct stop conditions for your application should be added to the experiment template.

## Requirements

- Add the required permission to the AWS FIS [experiment role](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
- Resource tags must be applied to resources that are to be targeted by the experiment. These can use your own tagging convention or the default tags defined in the scenario.

## Permissions

The following policy grants AWS FIS the necessary permissions to execute an experiment with the Cross-Region: Connectivity scenario. This policy must be attached to the [experiment role](getting-started-iam-service-role.md "getting-started-iam-service-role.md").

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RouteTableDisruptConnectivity1",
            "Effect": "Allow",
            "Action": "ec2:CreateRouteTable",
            "Resource": "arn:aws:ec2:*:*:route-table/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity2",
            "Effect": "Allow",
            "Action": "ec2:CreateRouteTable",
            "Resource": "arn:aws:ec2:*:*:vpc/*"
        },
        {
            "Sid": "RouteTableDisruptConnectivity21",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:route-table/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateRouteTable",
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity3",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateNetworkInterface",
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity4",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:prefix-list/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateManagedPrefixList",
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity5",
            "Effect": "Allow",
            "Action": "ec2:DeleteRouteTable",
            "Resource": [
                "arn:aws:ec2:*:*:route-table/*",
                "arn:aws:ec2:*:*:vpc/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity6",
            "Effect": "Allow",
            "Action": "ec2:CreateRoute",
            "Resource": "arn:aws:ec2:*:*:route-table/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity7",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity8",
            "Effect": "Allow",
            "Action": "ec2:CreateNetworkInterface",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:security-group/*"
            ]
        },
        {
            "Sid": "RouteTableDisruptConnectivity9",
            "Effect": "Allow",
            "Action": "ec2:DeleteNetworkInterface",
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity10",
            "Effect": "Allow",
            "Action": "ec2:CreateManagedPrefixList",
            "Resource": "arn:aws:ec2:*:*:prefix-list/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity11",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteManagedPrefixList",
                "ec2:ModifyManagedPrefixList"
            ],
            "Resource": "arn:aws:ec2:*:*:prefix-list/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "EC2DescribeResources",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeNetworkInterfaces",
                "ec2:DescribeVpcs",
                "ec2:DescribeVpcPeeringConnections",
                "ec2:DescribeManagedPrefixLists",
                "ec2:DescribeSubnets",
                "ec2:DescribeRouteTables",
                "ec2:DescribeVpcEndpoints",
                "ec2:DescribeTransitGatewayPeeringAttachments",
                "ec2:DescribeTransitGatewayAttachments",
                "ec2:DescribeTransitGateways",
                "ec2:DescribeSecurityGroups"
            ],
            "Resource": "*"
        },
        {
            "Sid": "RouteTableDisruptConnectivity14",
            "Effect": "Allow",
            "Action": "ec2:ReplaceRouteTableAssociation",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:route-table/*"
            ]
        },
        {
            "Sid": "RouteTableDisruptConnectivity15",
            "Effect": "Allow",
            "Action": "ec2:GetManagedPrefixListEntries",
            "Resource": "arn:aws:ec2:*:*:prefix-list/*"
        },
        {
            "Sid": "RouteTableDisruptConnectivity16",
            "Effect": "Allow",
            "Action": "ec2:AssociateRouteTable",
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:route-table/*"
            ]
        },
        {
            "Sid": "RouteTableDisruptConnectivity17",
            "Effect": "Allow",
            "Action": "ec2:DisassociateRouteTable",
            "Resource": "arn:aws:ec2:*:*:route-table/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "RouteTableDisruptConnectivity18",
            "Effect": "Allow",
            "Action": "ec2:DisassociateRouteTable",
            "Resource": "arn:aws:ec2:*:*:subnet/*"
        },
        {
            "Sid": "RouteTableDisruptConnectivity19",
            "Effect": "Allow",
            "Action": "ec2:ModifyVpcEndpoint",
            "Resource": "arn:aws:ec2:*:*:route-table/*",
            "Condition": {
                "StringEquals": {
                    "ec2:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "TransitGatewayDisruptConnectivity1",
            "Effect": "Allow",
            "Action": [
                "ec2:DisassociateTransitGatewayRouteTable",
                "ec2:AssociateTransitGatewayRouteTable"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:transit-gateway-route-table/*",
                "arn:aws:ec2:*:*:transit-gateway-attachment/*"
            ]
        },
        {
            "Sid": "S3CrossRegion1",
            "Effect": "Allow",
            "Action": "s3:ListAllMyBuckets",
            "Resource": "*"
        },
        {
            "Sid": "S3CrossRegion3",
            "Effect": "Allow",
            "Action": "s3:PauseReplication",
            "Resource": "arn:aws:s3:::*",
            "Condition": {
                "StringLike": {
                    "s3:DestinationRegion": "*"
                }
            }
        },
        {
            "Sid": "S3CrossRegion4",
            "Effect": "Allow",
            "Action": [
                "s3:GetReplicationConfiguration",
                "s3:PutReplicationConfiguration"
            ],
            "Resource": "arn:aws:s3:::*",
            "Condition": {
                "BoolIfExists": {
                    "s3:isReplicationPauseRequest": "true"
                }
            }
        },
        {
            "Sid": "DynamoDbPauseReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:DescribeTable",
                "dynamodb:PutResourcePolicy",
                "dynamodb:GetResourcePolicy",
                "dynamodb:DeleteResourcePolicy"
            ],
            "Resource": [
                "arn:aws:dynamodb:*:*:table/*"
            ]
        },
        {
            "Sid": "DynamoDbMrscPauseReplication",
            "Effect": "Allow",
            "Action": [
                "dynamodb:InjectError"
            ],
            "Resource": ["*"]
        },
        {
            "Sid": "ResolveResourcesViaTags",
            "Effect": "Allow",
            "Action": "tag:GetResources",
            "Resource": "*"
        },
        {
            "Sid": "MemDbCrossRegion",
            "Effect": "Allow",
            "Action": [
                "memorydb:DescribeMultiRegionClusters",
                "memorydb:PauseMultiRegionClusterReplication"
            ],
            "Resource": [
                "arn:aws:memorydb::*:multiregioncluster/*"
            ]
        },
        {
            "Sid": "DisruptVPCE1",
            "Effect": "Allow",
            "Action": "ec2:CreateSecurityGroup",
            "Resource": [
                "arn:aws:ec2:*:*:vpc/*",
                "arn:aws:ec2:*:*:security-group/*"
            ]
        },
        {
            "Sid": "DisruptVPCE2",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": "arn:aws:ec2:*:*:security-group/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateSecurityGroup",
                    "aws:RequestTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "DisruptVPCE3",
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteSecurityGroup",
                "ec2:RevokeSecurityGroupEgress"
            ],
            "Resource": "arn:aws:ec2:*:*:security-group/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/managedByFIS": "true"
                }
            }
        },
        {
            "Sid": "DisruptVPCE4",
            "Effect": "Allow",
            "Action": "vpce:AllowMultiRegion",
            "Resource": "arn:aws:ec2:*:*:vpc-endpoint/*"
        },
        {
            "Sid": "ModifyVPCE",
            "Effect": "Allow",
            "Action": "ec2:ModifyVpcEndpoint",
            "Resource": [
                "arn:aws:ec2:*:*:vpc-endpoint/*",
                "arn:aws:ec2:*:*:security-group/*"
            ]
        }
    ]
}
```

## Scenario Content

The following content defines the scenario. This JSON can be saved and used to create an [experiment template](experiment-templates.md "experiment-templates.md") using the [create-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html") command from the AWS Command Line Interface (AWS CLI). For the most recent version of the scenario, visit the scenario library in the FIS console.

```
{
        "targets": {
                "Transit-Gateway": {
                        "resourceType": "aws:ec2:transit-gateway",
                        "resourceTags": {
                                "TgwTag": "TgwValue"
                        },
                        "selectionMode": "ALL"
                },
                "Subnet": {
                        "resourceType": "aws:ec2:subnet",
                        "resourceTags": {
                                "SubnetKey": "SubnetValue"
                        },
                        "selectionMode": "ALL",
                        "parameters": {}
                },
                "VPC-Endpoint": {
                    "resourceType": "aws:ec2:vpc-endpoint",
                    "resourceTags": {
                        "DisruptPrivateLink": "Allowed"
                    },
                    "selectionMode": "ALL"
                },
                "S3-Bucket": {
                        "resourceType": "aws:s3:bucket",
                        "resourceTags": {
                                "S3Impact": "Allowed"
                        },
                        "selectionMode": "ALL"
                },
                "DynamoDB-Global-Table": {
                        "resourceType": "aws:dynamodb:global-table",
                        "resourceTags": {
                                "DisruptDynamoDb": "Allowed"
                        },
                        "selectionMode": "ALL"
                },
                "MemoryDB-Multi-Region-Cluster": {
                    "resourceType": "aws:memorydb:multi-region-cluster",
                    "resourceTags": {
                        "DisruptMemoryDb": "Allowed"
                    },
                    "selectionMode": "ALL"
                }
        },
        "actions": {
                "Disrupt-Transit-Gateway-Connectivity": {
                        "actionId": "aws:network:transit-gateway-disrupt-cross-region-connectivity",
                        "parameters": {
                                "duration": "PT3H",
                                "region": "eu-west-1"
                        },
                        "targets": {
                                "TransitGateways": "Transit-Gateway"
                        }
                },
                "Disrupt-Subnet-Connectivity": {
                        "actionId": "aws:network:route-table-disrupt-cross-region-connectivity",
                        "parameters": {
                                "duration": "PT3H",
                                "region": "eu-west-1"
                        },
                        "targets": {
                                "Subnets": "Subnet"
                        }
                },
                "Disrupt-Vpc-Endpoint": {
                        "actionId": "aws:network:disrupt-vpc-endpoint",
                        "parameters": {
                                "duration": "PT3H"
                        },
                        "targets": {
                                "VPCEndpoints": "VPC-Endpoint"
                        }
                },
                "Pause-S3-Replication": {
                        "actionId": "aws:s3:bucket-pause-replication",
                        "parameters": {
                                "duration": "PT3H",
                                "region": "eu-west-1"
                        },
                        "targets": {
                                "Buckets": "S3-Bucket"
                        }
                },
                "Pause-DynamoDB-Replication": {
                        "actionId": "aws:dynamodb:global-table-pause-replication",
                        "parameters": {
                                "duration": "PT3H"
                        },
                        "targets": {
                                "Tables": "DynamoDB-Global-Table"
                        }
                },
                "Pause-MemoryDB-Multi-Region-Cluster-Replication": {
                    "actionId": "aws:memorydb:multi-region-cluster-pause-replication",
                    "parameters": {
                        "duration": "PT3H",
                        "region": "eu-west-1"
                    },
                    "targets": {
                        "MultiRegionClusters": "MemoryDB-Multi-Region-Cluster"
                    }
                }
        },
        "stopConditions": [
                {
                        "source": "none"
                }
        ],
        "roleArn": "",
        "logConfiguration": {
                "logSchemaVersion": 2
        },
        "tags": {
                "Name": "Cross-Region: Connectivity"
        },
        "experimentOptions": {
                "accountTargeting": "single-account",
                "emptyTargetResolutionMode": "skip"
        },
        "description": "Block application network traffic from experiment Region to target Region and pause cross-Region replication"
}

```

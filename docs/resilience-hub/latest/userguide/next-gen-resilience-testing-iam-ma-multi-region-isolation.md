

# Multi-Region: isolation
<a name="next-gen-resilience-testing-iam-ma-multi-region-isolation"></a>

Attach the following permissions policy to the target role for the **Multi-Region: isolation** template.

```
{
  "Version": "2012-10-17"		 	 	 ,
  "Statement": [
    {
      "Sid": "RouteTableDisruptCrossRegion",
      "Effect": "Allow",
      "Action": [
        "ec2:AssociateRouteTable",
        "ec2:DisassociateRouteTable",
        "ec2:ReplaceRouteTableAssociation",
        "ec2:CreateRoute"
      ],
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:route-table/*",
        "arn:aws:ec2:*:{{target-account-id}}:subnet/*"
      ]
    },
    {
      "Sid": "RouteTableManagedCreate",
      "Effect": "Allow",
      "Action": "ec2:CreateRouteTable",
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:route-table/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "RouteTableManagedCreateOnVpc",
      "Effect": "Allow",
      "Action": "ec2:CreateRouteTable",
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:vpc/*"
    },
    {
      "Sid": "RouteTableManagedDelete",
      "Effect": "Allow",
      "Action": "ec2:DeleteRouteTable",
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:route-table/*",
        "arn:aws:ec2:*:{{target-account-id}}:vpc/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "PrefixListManagedCreate",
      "Effect": "Allow",
      "Action": "ec2:CreateManagedPrefixList",
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:prefix-list/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "PrefixListManagedModifyDelete",
      "Effect": "Allow",
      "Action": [
        "ec2:DeleteManagedPrefixList",
        "ec2:ModifyManagedPrefixList"
      ],
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:prefix-list/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "NetworkInterfaceManagedCreate",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterface",
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:network-interface/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "NetworkInterfaceManagedCreateOnSubnetAndSg",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterface",
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:subnet/*",
        "arn:aws:ec2:*:{{target-account-id}}:security-group/*"
      ]
    },
    {
      "Sid": "NetworkInterfaceManagedDelete",
      "Effect": "Allow",
      "Action": "ec2:DeleteNetworkInterface",
      "Resource": "arn:aws:ec2:*:{{target-account-id}}:network-interface/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "FISCreateTags",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:route-table/*",
        "arn:aws:ec2:*:{{target-account-id}}:prefix-list/*",
        "arn:aws:ec2:*:{{target-account-id}}:network-interface/*",
        "arn:aws:ec2:*:{{target-account-id}}:security-group/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "Ec2NetworkDescribeAndRead",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeRouteTables",
        "ec2:DescribeSubnets",
        "ec2:DescribeVpcs",
        "ec2:DescribeVpcPeeringConnections",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeManagedPrefixLists",
        "ec2:DescribeVpcEndpoints",
        "ec2:DescribeSecurityGroups",
        "ec2:GetManagedPrefixListEntries",
        "ec2:DescribeTransitGateways",
        "ec2:DescribeTransitGatewayAttachments",
        "ec2:DescribeTransitGatewayPeeringAttachments",
        "ec2:DescribeInstances"
      ],
      "Resource": "*"
    },
    {
      "Sid": "TgwDisruptCrossRegion",
      "Effect": "Allow",
      "Action": [
        "ec2:AssociateTransitGatewayRouteTable",
        "ec2:DisassociateTransitGatewayRouteTable"
      ],
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:transit-gateway-route-table/*",
        "arn:aws:ec2:*:{{target-account-id}}:transit-gateway-attachment/*"
      ]
    },
    {
      "Sid": "VpcEndpointDisrupt",
      "Effect": "Allow",
      "Action": "ec2:ModifyVpcEndpoint",
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:vpc-endpoint/*",
        "arn:aws:ec2:*:{{target-account-id}}:security-group/*"
      ]
    },
    {
      "Sid": "VpcEndpointSecurityGroupManaged",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateSecurityGroup",
        "ec2:DeleteSecurityGroup",
        "ec2:RevokeSecurityGroupEgress"
      ],
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:security-group/*",
        "arn:aws:ec2:*:{{target-account-id}}:vpc/*"
      ]
    },
    {
      "Sid": "SsmSendCommandOnDocuments",
      "Effect": "Allow",
      "Action": "ssm:SendCommand",
      "Resource": [
        "arn:aws:ssm:*::document/AWSFIS-Run-Network-Packet-Loss-Sources",
        "arn:aws:ssm:*::document/AWSFIS-Run-Network-Packet-Loss-ECS"
      ]
    },
    {
      "Sid": "SsmSendCommandOnInstances",
      "Effect": "Allow",
      "Action": "ssm:SendCommand",
      "Resource": [
        "arn:aws:ec2:*:{{target-account-id}}:instance/*",
        "arn:aws:ssm:*:{{target-account-id}}:managed-instance/*",
        "arn:aws:ecs:*:{{target-account-id}}:task/*/*"
      ]
    },
    {
      "Sid": "SsmListAndCancelCommands",
      "Effect": "Allow",
      "Action": [
        "ssm:ListCommands",
        "ssm:CancelCommand"
      ],
      "Resource": "*"
    },
    {
      "Sid": "EcsDescribeForTargetResolution",
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeTasks",
        "ecs:DescribeContainerInstances",
        "ecs:ListTasks"
      ],
      "Resource": [
        "arn:aws:ecs:*:{{target-account-id}}:task/*/*",
        "arn:aws:ecs:*:{{target-account-id}}:container-instance/*/*",
        "arn:aws:ecs:*:{{target-account-id}}:cluster/*"
      ]
    },
    {
      "Sid": "EksDescribeCluster",
      "Effect": "Allow",
      "Action": "eks:DescribeCluster",
      "Resource": "arn:aws:eks:*:{{target-account-id}}:cluster/*"
    },
    {
      "Sid": "DynamoDbGlobalTablePauseReplication",
      "Effect": "Allow",
      "Action": [
        "dynamodb:PutResourcePolicy",
        "dynamodb:GetResourcePolicy",
        "dynamodb:DeleteResourcePolicy",
        "dynamodb:DescribeTable",
        "dynamodb:InjectError"
      ],
      "Resource": "arn:aws:dynamodb:*:{{target-account-id}}:table/*"
    },
    {
      "Sid": "S3PauseReplicationConfiguration",
      "Effect": "Allow",
      "Action": [
        "s3:PutReplicationConfiguration",
        "s3:GetReplicationConfiguration"
      ],
      "Resource": "arn:aws:s3:::*",
      "Condition": {
        "BoolIfExists": {
          "s3:IsReplicationPauseRequest": "true"
        }
      }
    },
    {
      "Sid": "S3PauseReplication",
      "Effect": "Allow",
      "Action": "s3:PauseReplication",
      "Resource": "arn:aws:s3:::*"
    },
    {
      "Sid": "S3ListAllBuckets",
      "Effect": "Allow",
      "Action": "s3:ListAllMyBuckets",
      "Resource": "*"
    },
    {
      "Sid": "MemoryDbMultiRegionPauseReplication",
      "Effect": "Allow",
      "Action": [
        "memorydb:PauseMultiRegionClusterReplication",
        "memorydb:DescribeMultiRegionClusters"
      ],
      "Resource": "arn:aws:memorydb::{{target-account-id}}:multiregioncluster/*"
    },
    {
      "Sid": "TargetResolutionByTags",
      "Effect": "Allow",
      "Action": "tag:GetResources",
      "Resource": "*"
    }
  ]
}
```
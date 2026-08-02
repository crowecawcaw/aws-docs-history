# Availability Zone: recovery

The **Availability Zone: recovery** template runs AWS FIS actions against the following services: Amazon EC2, Amazon EC2 Auto Scaling, Amazon ElastiCache, Amazon RDS, network ACLs, and AWS Application Recovery Controller zonal shift. Attach the following permissions policy to the execution role.

```

{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "EC2StopAndStartInstances",
      "Effect": "Allow",
      "Action": [
        "ec2:StopInstances",
        "ec2:StartInstances"
      ],
      "Resource": "arn:aws:ec2:*:`account-id`:instance/*"
    },
    {
      "Sid": "EC2DescribeInstances",
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    },
    {
      "Sid": "EC2EncryptedVolumesKmsGrant",
      "Effect": "Allow",
      "Action": "kms:CreateGrant",
      "Resource": "arn:aws:kms:*:`account-id`:key/*",
      "Condition": {
        "StringLike": {
          "kms:ViaService": "ec2.*.amazonaws.com"
        },
        "Bool": {
          "kms:GrantIsForAWSResource": "true"
        },
        "ForAllValues:StringEquals": {
          "kms:GrantOperations": ["Decrypt", "CreateGrant"]
        },
        "Null": {
          "kms:GrantOperations": "false"
        },
        "StringEquals": {
          "kms:GrantConstraintType": "EncryptionContextSubset"
        },
        "ForAnyValue:StringEquals": {
          "kms:EncryptionContextKeys": "aws:ebs:id"
        }
      }
    },
    {
      "Sid": "EC2InjectApiError",
      "Effect": "Allow",
      "Action": "ec2:InjectApiError",
      "Resource": "*",
      "Condition": {
        "ForAnyValue:StringEquals": {
          "ec2:FisActionId": [
            "aws:ec2:api-insufficient-instance-capacity-error",
            "aws:ec2:asg-insufficient-instance-capacity-error"
          ]
        }
      }
    },
    {
      "Sid": "AutoScalingDescribe",
      "Effect": "Allow",
      "Action": [
        "autoscaling:DescribeAutoScalingGroups",
        "autoscaling:DescribeTags"
      ],
      "Resource": "*"
    },
    {
      "Sid": "ElastiCacheInterruptAzPower",
      "Effect": "Allow",
      "Action": [
        "elasticache:InterruptClusterAzPower",
        "elasticache:DescribeReplicationGroups"
      ],
      "Resource": "arn:aws:elasticache:*:`account-id`:replicationgroup:*"
    },
    {
      "Sid": "EBSPauseVolumeIO",
      "Effect": "Allow",
      "Action": "ec2:PauseVolumeIO",
      "Resource": "arn:aws:ec2:*:`account-id`:volume/*"
    },
    {
      "Sid": "EBSDescribeVolumes",
      "Effect": "Allow",
      "Action": "ec2:DescribeVolumes",
      "Resource": "*"
    },
    {
      "Sid": "NetworkTagManagedNacl",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": "arn:aws:ec2:*:`account-id`:network-acl/*",
      "Condition": {
        "StringEquals": {
          "ec2:CreateAction": "CreateNetworkAcl",
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "NetworkCreateManagedNacl",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkAcl",
      "Resource": "arn:aws:ec2:*:`account-id`:network-acl/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "NetworkCreateNaclOnVpc",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkAcl",
      "Resource": "arn:aws:ec2:*:`account-id`:vpc/*"
    },
    {
      "Sid": "NetworkModifyManagedNacl",
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkAclEntry",
        "ec2:DeleteNetworkAcl"
      ],
      "Resource": "arn:aws:ec2:*:`account-id`:network-acl/*",
      "Condition": {
        "StringEquals": {
          "ec2:ResourceTag/managedByFIS": "true"
        }
      }
    },
    {
      "Sid": "NetworkDescribe",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeVpcs",
        "ec2:DescribeSubnets",
        "ec2:DescribeNetworkAcls",
        "ec2:DescribeManagedPrefixLists"
      ],
      "Resource": "*"
    },
    {
      "Sid": "NetworkReplaceNaclAssociation",
      "Effect": "Allow",
      "Action": "ec2:ReplaceNetworkAclAssociation",
      "Resource": [
        "arn:aws:ec2:*:`account-id`:subnet/*",
        "arn:aws:ec2:*:`account-id`:network-acl/*"
      ]
    },
    {
      "Sid": "NetworkPrefixListEntries",
      "Effect": "Allow",
      "Action": "ec2:GetManagedPrefixListEntries",
      "Resource": "arn:aws:ec2:*:`account-id`:prefix-list/*"
    },
    {
      "Sid": "RDSFailoverCluster",
      "Effect": "Allow",
      "Action": [
        "rds:FailoverDBCluster",
        "rds:DescribeDBClusters"
      ],
      "Resource": "arn:aws:rds:*:`account-id`:cluster:*"
    },
    {
      "Sid": "RDSDescribeForTargetResolution",
      "Effect": "Allow",
      "Action": "rds:DescribeDBInstances",
      "Resource": "arn:aws:rds:*:`account-id`:db:*"
    },
    {
      "Sid": "ARCZonalShiftManagedElb",
      "Effect": "Allow",
      "Action": [
        "arc-zonal-shift:StartZonalShift",
        "arc-zonal-shift:GetManagedResource",
        "arc-zonal-shift:UpdateZonalShift",
        "arc-zonal-shift:CancelZonalShift"
      ],
      "Resource": [
        "arn:aws:elasticloadbalancing:*:`account-id`:loadbalancer/app/*",
        "arn:aws:elasticloadbalancing:*:`account-id`:loadbalancer/net/*"
      ]
    },
    {
      "Sid": "ARCZonalShiftManagedAsgEks",
      "Effect": "Allow",
      "Action": [
        "arc-zonal-shift:StartZonalShift",
        "arc-zonal-shift:GetManagedResource",
        "arc-zonal-shift:UpdateZonalShift",
        "arc-zonal-shift:CancelZonalShift"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "arc-zonal-shift:ResourceIdentifier": [
            "arn:aws:autoscaling:*:`account-id`:autoScalingGroup:*",
            "arn:aws:eks:*:`account-id`:cluster/*"
          ]
        }
      }
    },
    {
      "Sid": "ARCZonalShiftList",
      "Effect": "Allow",
      "Action": "arc-zonal-shift:ListManagedResources",
      "Resource": "*"
    },
    {
      "Sid": "TargetResolutionByTags",
      "Effect": "Allow",
      "Action": "tag:GetResources",
      "Resource": "*"
    },
    {
      "Sid": "FISExperimentLogging",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogDelivery",
        "logs:GetLogDelivery",
        "logs:UpdateLogDelivery",
        "logs:DeleteLogDelivery",
        "logs:ListLogDeliveries"
      ],
      "Resource": "*"
    },
    {
      "Sid": "FISExperimentLogGroupAccess",
      "Effect": "Allow",
      "Action": [
        "logs:DescribeResourcePolicies",
        "logs:PutResourcePolicy",
        "logs:DescribeLogGroups"
      ],
      "Resource": "*"
    }
  ]
}

```

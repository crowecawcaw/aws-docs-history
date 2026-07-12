# IAM permissions required to create an MSK Replicator

The IAM principal (user or role) that calls `CreateReplicator` needs the permissions described in this section. Attach this policy to the IAM identity that corresponds to your client. For general guidance on creating authorization policies, see [Create authorization policies](iam-access-control.md#create-iam-access-control-policies "iam-access-control.md#create-iam-access-control-policies").

Start with the **base policy** below. If you also configure log delivery, append the snippet for each destination you use (see [Additional permissions for log delivery](msk-replicator-create-iam-perms-logs.md "msk-replicator-create-iam-perms-logs.md")). For self-managed Apache Kafka migration scenarios, see additional service execution role guidance in [Migrate from non-MSK Apache Kafka clusters to Amazon MSK Provisioned](msk-replicator-migrate-external.md "msk-replicator-migrate-external.md").

## Base IAM policy

Replace the placeholders with your account ID, AWS Region, service execution role name, and source and target cluster ARNs. The action `kafka:TagResource` is only needed if you provide tags during creation.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MSKReplicatorIAMPassRole",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::<accountID>:role/<serviceExecutionRoleName>",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "kafka.amazonaws.com"
                }
            }
        },
        {
            "Sid": "MSKReplicatorServiceLinkedRole",
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::<accountID>:role/aws-service-role/kafka.amazonaws.com/AWSServiceRoleForKafka*"
        },
        {
            "Sid": "MSKReplicatorActions",
            "Effect": "Allow",
            "Action": [
                "kafka:CreateReplicator",
                "kafka:DescribeReplicator",
                "kafka:DeleteReplicator",
                "kafka:ListReplicators",
                "kafka:ListTagsForResource",
                "kafka:UpdateReplicationInfo",
                "kafka:TagResource"
            ],
            "Resource": [
                "arn:aws:kafka:<region>:<accountID>:replicator/*"
            ]
        },
        {
            "Sid": "MSKReplicatorListActions",
            "Effect": "Allow",
            "Action": [
                "kafka:ListReplicators"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "EC2Actions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeSubnets",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs"
            ],
            "Resource": [
                "*"
            ]
        },
        {
            "Sid": "MSKClusterActions",
            "Effect": "Allow",
            "Action": [
                "kafka:GetBootstrapBrokers",
                "kafka:DescribeClusterV2"
            ],
            "Resource": [
                "<sourceClusterArn>",
                "<targetClusterArn>"
            ]
        }
    ]
}
```

###### Note

The `ec2:DescribeSubnets`, `ec2:DescribeSecurityGroups`, and `ec2:DescribeVpcs` actions do not support resource-level permissions, so you must specify `"Resource": "*"`. See the [Actions, resources, and condition keys for Amazon EC2](../../../service-authorization/latest/reference/list_amazonec2.md "../../../service-authorization/latest/reference/list_amazonec2.md") reference.

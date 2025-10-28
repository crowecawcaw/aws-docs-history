# AWS managed

policy: AmazonWorkSpacesWebServiceRolePolicy

You can't attach the `AmazonWorkSpacesWebServiceRolePolicy` policy to your
IAM entities. This policy is attached to a service-linked role that allows WorkSpaces Secure Browser
to perform actions on your behalf. For more information, see [Using service-linked roles for
Amazon WorkSpaces Secure Browser](using-service-linked-roles.md "using-service-linked-roles.md").

This policy grants administrative permissions that allow access to AWS services and
resources used or managed by WorkSpaces Secure Browser.

**Permissions details**

This policy includes the following permissions:

- `workspaces-web` – Allows access to AWS services and resources
  used or managed by WorkSpaces Secure Browser.
- `ec2` – Allows principals to describe VPCs, subnets, and
  availability zones; create, tag, describe, and delete network interfaces; associate
  or disassociate an address; and describe route tables, security groups, and VPC
  endpoints.
- `CloudWatch` – Allows principals to put metric data.
- `Kinesis` - Allows principals to describe a summary of Kinesis data
  streams and put records into Kinesis data streams for user access logging. For more
  information, see [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md").

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeNetworkInterfaces",
                "ec2:AssociateAddress",
                "ec2:DisassociateAddress",
                "ec2:DescribeRouteTables",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcEndpoints"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:subnet/*",
                "arn:aws:ec2:*:*:security-group/*"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateNetworkInterface"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/WorkSpacesWebManaged": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:CreateTags"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": "CreateNetworkInterface"
                },
                "ForAllValues:StringEquals": {
                    "aws:TagKeys": [
                        "WorkSpacesWebManaged"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "arn:aws:ec2:*:*:network-interface/*",
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/WorkSpacesWebManaged": "true"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "cloudwatch:namespace": [
                        "AWS/WorkSpacesWeb",
                        "AWS/Usage"
                    ]
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "kinesis:PutRecord",
                "kinesis:PutRecords",
                "kinesis:DescribeStreamSummary"
            ],
            "Resource": "arn:aws:kinesis:*:*:stream/amazon-workspaces-web-*"
        }
    ]
}

```

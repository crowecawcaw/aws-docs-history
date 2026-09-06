

# Service-linked role for VPC networking
<a name="vpc-service-linked-role"></a>

HealthOmics uses an IAM service-linked role to create and manage elastic network interfaces (ENIs) in your VPC. This role is automatically created when you create your first VPC configuration.

## Service-linked role details
<a name="vpc-slr-details"></a>
+ **Role Name**: `AWSServiceRoleForHealthOmics`
+ **Managed Policy**: `AWSHealthOmicsServiceLinkedRolePolicy`
+ **Service Principal**: `omics.amazonaws.com`

## Permissions granted
<a name="vpc-slr-permissions"></a>

The service-linked role grants HealthOmics the following Amazon EC2 permissions to manage network interfaces in your VPC:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEC2DescribeActions",
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeSubnets",
        "ec2:DescribeTags",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeSecurityGroupRules",
        "ec2:DescribeVpcs",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeAvailabilityZones"
      ],
      "Resource": "*"
    },
    {
      "Sid": "AllowVpcGetActions",
      "Effect": "Allow",
      "Action": [
        "ec2:GetSecurityGroupsForVpc"
      ],
      "Resource": "arn:aws:ec2:*:*:vpc/*"
    },
    {
      "Sid": "AllowCreateNetworkInterfaceWithTag",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterface",
      "Resource": "arn:aws:ec2:*:*:network-interface/*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/Service": "HealthOmics"
        }
      }
    },
    {
      "Sid": "AllowCreateNetworkInterfaceSubnetSecurityGroup",
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterface",
      "Resource": [
        "arn:aws:ec2:*:*:subnet/*",
        "arn:aws:ec2:*:*:security-group/*"
      ]
    },
    {
      "Sid": "AllowCreateTags",
      "Effect": "Allow",
      "Action": "ec2:CreateTags",
      "Resource": "arn:aws:ec2:*:*:network-interface/*",
      "Condition": {
        "StringEquals": {
          "ec2:CreateAction": "CreateNetworkInterface"
        }
      }
    },
    {
      "Sid": "AllowDeleteNetworkInterface",
      "Effect": "Allow",
      "Action": "ec2:DeleteNetworkInterface",
      "Resource": "arn:aws:ec2:*:*:network-interface/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Service": "HealthOmics"
        }
      }
    },
    {
      "Sid": "AllowAssignUnassignPrivateIpAddresses",
      "Effect": "Allow",
      "Action": [
        "ec2:AssignPrivateIpAddresses",
        "ec2:UnassignPrivateIpAddresses"
      ],
      "Resource": "arn:aws:ec2:*:*:network-interface/*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Service": "HealthOmics"
        }
      }
    }
  ]
}
```

## Creating the service-linked role
<a name="vpc-slr-creating"></a>

The service-linked role is automatically created when you create your first VPC configuration using the `CreateConfiguration` API. You must have the following IAM permission:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "iam:CreateServiceLinkedRole",
      "Resource": "arn:aws:iam::*:role/aws-service-role/omics.amazonaws.com/AWSServiceRoleForHealthOmics",
      "Condition": {
        "StringEquals": {
          "iam:AWSServiceName": "omics.amazonaws.com"
        }
      }
    }
  ]
}
```

## Deleting the service-linked role
<a name="vpc-slr-deleting"></a>

You can delete the service-linked role only after deleting all VPC configurations in your account. To delete the role:

```
aws iam delete-service-linked-role \
  --role-name AWSServiceRoleForHealthOmics
```

If you have active VPC configurations, the deletion will fail with a message indicating which configuration resources must be deleted first.
# AWS Infrastructure Setup

This section covers the one-time setup tasks required to prepare your AWS environment for the cluster deployment:

###### Topics

- [Create IAM Roles and Policies for Pacemaker](#iam_roles_rhel "#iam_roles_rhel")
- [Modify Security Groups for Cluster Communication](#sg-rhel "#sg-rhel")
- [Add VPC Route Table Entries for Overlay IPs](#rt-rhel "#rt-rhel")

## Create IAM Roles and Policies for Pacemaker

In addition to the permissions required for standard SAP operations, two IAM policies are required for the cluster to control AWS resources. These policies must be assigned to your Amazon EC2 instance using an IAM role. This enables Amazon EC2 instance, and therefore the cluster to call AWS services.

###### Note

Create policies with least-privilege permissions, granting access to only the specific resources that are required within the cluster. For multiple clusters, you may need to create multiple policies.

For more information, see [IAM roles for Amazon EC2](../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-profile "../../../AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.md#ec2-instance-profile").

### STONITH Policy

The Red Hat STONITH resource agent (`fence_aws`) requires permission to start and stop both the nodes of the cluster. Create a policy as shown in the following example. Attach this policy to the IAM role assigned to both Amazon EC2 instances in the cluster.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:DescribeInstances",
        "ec2:DescribeTags"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:123456789012:instance/arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
        "arn:aws:ec2:us-east-1:123456789012:instance/arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
      ]
    }
  ]
}
```

### AWS Overlay IP Policy

The Red Hat Overlay IP resource agent (`aws-vpc-move-ip`) requires permission to modify a routing entry in route tables. Create a policy as shown in the following example. Attach this policy to the IAM role assigned to both Amazon EC2 instances in the cluster.

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:ReplaceRoute",
            "Resource": [
                 "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-0123456789abcdef0",
                 "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-0123456789abcdef0"
                        ]
        },
        {
            "Effect": "Allow",
            "Action": "ec2:DescribeRouteTables",
            "Resource": "*"
        }
    ]
}
```

### Shared VPC (optional)

###### Note

The following directions are only required for setups which include a Shared VPC.

Amazon VPC sharing enables you to share subnets with other AWS accounts within the same AWS Organizations. Amazon EC2 instances can be deployed using the subnets of the shared Amazon VPC.

In the pacemaker cluster, the aws-vpc-move-ip resource agent has been enhanced to support a shared VPC setup while maintaining backward compatibility with previous existing features.

The following checks and changes are required. We refer to the AWS account that owns Amazon VPC as the sharing VPC account, and to the consumer account where the cluster nodes are going to be deployed as the cluster account.

###### IAM Roles and Policies

Using the Overlay IP agent with a shared Amazon VPC requires a different set of IAM permissions to be granted on both AWS accounts (sharing VPC account and cluster account).

###### Sharing VPC Account

In sharing VPC account, create an IAM role to delegate permissions to the EC2 instances that will be part of the cluster. During the IAM Role creation, select "Another AWS account" as the type of trusted entity, and enter the AWS account ID where the EC2 instances will be deployed/running from.

After the IAM role has been created, create the following IAM policy on the sharing VPC account, and attach it to an IAM role. Add or remove route table entries as needed.

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "ec2:ReplaceRoute",
      "Resource": [
        "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-0123456789abcdef0",
        "arn:aws:ec2:us-east-1:123456789012:route-table/rtb-0123456789abcdef0"
      ]
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": "ec2:DescribeRouteTables",
      "Resource": "*"
    }
  ]
}
```

Next, edit move to the "Trust relationships" tab in the IAM role, and ensure that the AWS account you entered while creating the role has been correctly added.

In cluster account, create the following IAM policy, and attach it to an IAM role. This is the IAM Role that is going to be attached to the EC2 instances.

**STS Policy**

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": "sts:AssumeRole",
      "Resource": "arn:aws:iam::123456789012:role/sharing-vpc-account-cluster-role"
    }
  ]
}
```

**STONITH Policy**

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Sid": "VisualEditor0",
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances"
      ],
      "Resource": [
        "arn:aws:ec2:us-east-1:123456789012:instance/arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0",
        "arn:aws:ec2:us-east-1:123456789012:instance/arn:aws:ec2:us-east-1:123456789012:instance/i-1234567890abcdef0"
      ]
    },
    {
      "Sid": "VisualEditor1",
      "Effect": "Allow",
      "Action": "ec2:DescribeInstances",
      "Resource": "*"
    }
  ]
}
```

## Modify Security Groups for Cluster Communication

A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For more information, see [Control traffic to your AWS resources using security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md").

In addition to the standard ports required to access SAP and administrative functions, the following rules must be applied to the security groups assigned to all Amazon EC2 instances in the cluster.

| Source                                      | Protocol | Port range | Description                                                             |
| ------------------------------------------- | -------- | ---------- | ----------------------------------------------------------------------- |
| The security group ID (its own resource ID) | UDP      | 5405       | Allows UDP traffic between cluster resources for corosync communication |

- Note the use of the `UDP` protocol.
- If you are running a local firewall, such as iptables, ensure that communication on the preceding ports is allowed between two Amazon EC2 instances.

## Add VPC Route Table Entries for Overlay IPs

You need to add initial route table entries for the Overlay IP. For more information on Overlay IP, see [Overlay IP Concept](sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel "sap-hana-pacemaker-rhel-concepts.md#overlay-ip-rhel")

Add entries to the VPC route table or tables associated with the subnets of your Amazon EC2 instance for the cluster. The entries for destination (Overlay IP CIDR) and target (Amazon EC2 instance or ENI) must be added manually for the SAP HANA Primary Database mpde. This ensures that the cluster resource has a route to modify. It also supports the install of SAP using the virtual names associated with the Overlay IP before the configuration of the cluster.

Using either the Amazon VPC console, or an AWS CLI command add a route to the table or tables for the Overlay IP.

AWS Console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Route Tables**, then select the route table associated with your cluster node subnets.
3. Choose **Actions** → **Edit routes**.
4. Choose **Add route** and configure the HANA route:

| Destination           | Target                 |
| --------------------- | ---------------------- |
| `<hana_overlayip>/32` | `i-xxxxinstidforhost1` |

5. (Optional) Add a route for read-enabled access to the secondary:

| Destination                  | Target                 |
| ---------------------------- | ---------------------- |
| `<readenabled_overlayip>/32` | `i-xxxxinstidforhost2` |

6. Choose **Save changes**.

Your route table now includes entries for required Overlay IPs, in addition to the standard routes.

AWS CLI
The preceding steps can also be performed programmatically. We suggest performing the steps using administrative privileges, instead of instance-based privileges to preserve least privilege. CreateRoute API isn’t necessary for ongoing operations.

For example:

```
$ aws ec2 create-route --route-table-id <routetable_id> --destination-cidr-block <hana_overlayip>/32 --instance-id <instance_id_1>
```

If required for read enabled access

```
$ aws ec2 create-route --route-table-id <routetable_id> --destination-cidr-block <readenabled_overlayip>/32 --instance-id <instance_id_2>
```

Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Infrastructure security in

Amazon Redshift

As a managed service, Amazon Redshift is protected by AWS global network security. For
information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/ "https://aws.amazon.com/security/"). To design your AWS
environment using the best practices for infrastructure security, see [Infrastructure
Protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") in _Security Pillar AWS Well‐Architected
Framework_.

You use AWS published API calls to access Amazon Redshift through the network. Clients must
support the following:

- Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
- Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral
  Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems
  such as Java 7 and later support these modes.

## Network isolation

A virtual private cloud (VPC) based on the Amazon VPC service is your private, logically
isolated network in the AWS Cloud. You can deploy an Amazon Redshift cluster or Redshift Serverless workgroup
within a VPC by taking the following steps:

- Create a VPC in an AWS Region. For more information, see [What is
  Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide._
- Create two or more private VPC subnets. For more information, see [VPCs and
  subnets](../../../vpc/latest/userguide/VPC_Subnets.md "../../../vpc/latest/userguide/VPC_Subnets.md") in the _Amazon VPC User Guide._
- Deploy an Amazon Redshift cluster or a Redshift Serverless workgroup. For more information, see [Subnets for Redshift resources](working-with-cluster-subnet-groups.md "working-with-cluster-subnet-groups.md") or [Workgroups and namespaces](serverless-workgroup-namespace.md "serverless-workgroup-namespace.md").

An Amazon Redshift cluster is locked down by default upon provisioning. To allow inbound network
traffic from Amazon Redshift clients, associate a VPC security group with an Amazon Redshift cluster. For more
information, see [Subnets for Redshift resources](working-with-cluster-subnet-groups.md "working-with-cluster-subnet-groups.md").

To allow traffic only to or from specific IP address ranges, update the security
groups with your VPC. An example is allowing traffic only from or to your corporate
network.

While configuring network access control lists associated with the subnet(s) your Amazon Redshift
cluster is tagged with, ensure that the respective AWS Region's S3 CIDR ranges are
added to the allowlist for both ingress and egress rules. Doing so lets you execute
S3-based operations such as Redshift Spectrum, COPY, and UNLOAD without any disruptions.

The following example command parses the JSON response for all IPv4 addresses used in
Amazon S3 in the us-east-1 Region.

```
curl https://ip-ranges.amazonaws.com/ip-ranges.json | jq -r '.prefixes[] | select(.region=="us-east-1") | select(.service=="S3") | .ip_prefix'

54.231.0.0/17

52.92.16.0/20

52.216.0.0/15

```

For instructions on how to get S3 IP ranges for a particular region, see [AWS IP address
ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md").

Amazon Redshift supports deploying clusters into dedicated tenancy VPCs. For more information,
see [Dedicated instances](../../../AWSEC2/latest/UserGuide/dedicated-instance.md "../../../AWSEC2/latest/UserGuide/dedicated-instance.md") in the _Amazon EC2 User
Guide._

## Amazon Redshift security groups

When you provision an Amazon Redshift cluster, it is locked down by default so nobody has
access to it. To grant other users inbound access to an Amazon Redshift cluster, you associate
the cluster with a security group. If you are on the EC2-VPC platform, you can either
use an existing Amazon VPC security group or define a new one and then associate it with a
cluster. For more information on managing a cluster on the EC2-VPC platform, see [Redshift resources in a VPC](managing-clusters-vpc.md "managing-clusters-vpc.md").

## Interface VPC endpoints

You can connect directly to the Amazon Redshift and Amazon Redshift Serverless API services using an interface VPC
endpoint (AWS PrivateLink) in your virtual private cloud (VPC) instead of connecting over the
internet. For information about Amazon Redshift API actions, see [Actions](../APIReference/API_Operations.md "../APIReference/API_Operations.md") in the _Amazon Redshift API Reference_. For information about Redshift Serverless API actions, see
[Actions](../../../redshift-serverless/latest/APIReference/API_Operations.md "../../../redshift-serverless/latest/APIReference/API_Operations.md") in the
_Amazon Redshift Serverless API Reference_. For more information about
AWS PrivateLink, see [Interface VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_. Note
that JDBC/ODBC connection to the cluster or workspace is not part of Amazon Redshift API
service.

When you use an interface VPC endpoint, communication between your VPC and Amazon Redshift or Redshift Serverless
is conducted entirely within the AWS network, which can provide greater security. Each VPC
endpoint is represented by one or more elastic network interfaces with private IP addresses
in your VPC subnets. For more information on elastic network interfaces, see [Elastic network
interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in the _Amazon EC2 User Guide._

An interface VPC endpoint connects your VPC directly to Amazon Redshift. It doesn't use an internet
gateway, network address translation (NAT) device, virtual private network (VPN) connection,
or Direct Connect connection. The instances in your VPC don't need public IP addresses to
communicate with the Amazon Redshift API.

To use Amazon Redshift or Redshift Serverless through your VPC, you have two options. One is to connect from an
instance that is inside your VPC. The other is to connect your private network to your VPC
by using an Site-to-Site VPN option or Direct Connect. For more information about Site-to-Site VPN options, see [VPN
connections](../../../vpc/latest/userguide/vpn-connections.md "../../../vpc/latest/userguide/vpn-connections.md") in the _Amazon VPC User Guide_. For information about
Direct Connect, see [Creating a
Connection](../../../directconnect/latest/UserGuide/create-connection.md "../../../directconnect/latest/UserGuide/create-connection.md") in the _Direct Connect User Guide_.

You can create an interface VPC endpoint to connect to Amazon Redshift using the AWS Management Console or
AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating
an Interface Endpoint](../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint "../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint").

After you create an interface VPC endpoint, you can enable private DNS host names for the
endpoint. When you do, the default endpoint is as follows:

- **Amazon Redshift provisioned**:
  `https://redshift.``Region``.amazonaws.com`
- **Amazon Redshift Serverless**:
  `https://redshift-serverless.``Region``.amazonaws.com`

If you don't enable private DNS host names, Amazon VPC provides a DNS endpoint name
that you can use in the following format.

- **Amazon Redshift provisioned**:
  ``VPC_endpoint_ID`.redshift.`Region`.vpce.amazonaws.com`
- **Amazon Redshift Serverless**:
  ``VPC_endpoint_ID`.redshift-serverless.`Region`.vpce.amazonaws.com`

For more information, see [Interface VPC endpoints
(AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User
Guide_.

Amazon Redshift and Redshift Serverless support making calls to all of the [Amazon Redshift API operations](../APIReference/API_Operations.md "../APIReference/API_Operations.md") and
[Redshift Serverless API
operations](../../../redshift-serverless/latest/APIReference/API_Operations.md "../../../redshift-serverless/latest/APIReference/API_Operations.md") inside your VPC.

You can attach VPC endpoint policies to a VPC endpoint to control access for AWS Identity and Access Management
(IAM) principals. You can also associate security groups with a VPC endpoint to control
inbound and outbound access based on the origin and destination of network traffic. An
example is a range of IP addresses. For more information, see [Controlling Access to Services with
VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

### VPC endpoint

policies for Amazon Redshift

You can create a policy for VPC endpoints for Amazon Redshift to specify the following:

- The principal that can or can't perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling access to services
with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

Following, you can find examples of VPC endpoint policies.

#### Amazon Redshift Provisioned

Endpoint Policy Examples

Following, you can find examples of VPC endpoint policies for Amazon Redshift
Provisioned.

##### Example: VPC endpoint policy

to deny all access from a specified AWS account

The following VPC endpoint policy denies the AWS account
`123456789012` all access to
resources using this endpoint.

```

{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "*",
            "Effect": "Deny",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}

```

##### Example: VPC endpoint policy

to allow VPC access only to a specified IAM role

The following VPC endpoint policy allows full access only to the IAM role
`redshiftrole` in AWS account
`123456789012`. All other IAM principals are denied
access using the endpoint.

```

   {
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:role/redshiftrole"
                ]
            }
        }]
}

```

This is only a sample. In most use cases we recommend attaching permissions
for specific actions to narrow the scope of permissions.

##### Example: VPC endpoint policy

to allow VPC access only to a specified IAM principal (user)

The following VPC endpoint policy allows full access only to the IAM user
`redshiftadmin` in AWS account
`123456789012`. All other IAM principals are denied
access using the endpoint.

```

   {
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::123456789012:user/redshiftadmin"
                ]
            }
        }]
}

```

This is only a sample. In most use cases we recommend attaching permissions to
a role before assigning to a user. Additionally, we recommend using specific
actions to narrow the scope of permissions.

##### Example: VPC endpoint policy

to allow read-only Amazon Redshift operations

The following VPC endpoint policy allows only AWS account
`123456789012` to perform the
specified Amazon Redshift actions.

The actions specified provide the equivalent of read-only access for Amazon Redshift. All
other actions on the VPC are denied for the specified account. Also, all other
accounts are denied any access. For a list of Amazon Redshift actions, see [Actions, Resources, and Condition Keys for Amazon Redshift](../../../IAM/latest/UserGuide/list_amazonredshift.md "../../../IAM/latest/UserGuide/list_amazonredshift.md") in the
_IAM User Guide._

```

  {
    "Statement": [
        {
            "Action": [
                "redshift:DescribeAccountAttributes",
                "redshift:DescribeClusterParameterGroups",
                "redshift:DescribeClusterParameters",
                "redshift:DescribeClusterSecurityGroups",
                "redshift:DescribeClusterSnapshots",
                "redshift:DescribeClusterSubnetGroups",
                "redshift:DescribeClusterVersions",
                "redshift:DescribeDefaultClusterParameters",
                "redshift:DescribeEventCategories",
                "redshift:DescribeEventSubscriptions",
                "redshift:DescribeHsmClientCertificates",
                "redshift:DescribeHsmConfigurations",
                "redshift:DescribeLoggingStatus",
                "redshift:DescribeOrderableClusterOptions",
                "redshift:DescribeQuery",
                "redshift:DescribeReservedNodeOfferings",
                "redshift:DescribeReservedNodes",
                "redshift:DescribeResize",
                "redshift:DescribeSavedQueries",
                "redshift:DescribeScheduledActions",
                "redshift:DescribeSnapshotCopyGrants",
                "redshift:DescribeSnapshotSchedules",
                "redshift:DescribeStorage",
                "redshift:DescribeTable",
                "redshift:DescribeTableRestoreStatus",
                "redshift:DescribeTags",
                "redshift:FetchResults",
                "redshift:GetReservedNodeExchangeOfferings"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}

```

##### Example: VPC endpoint policy

denying access to a specified cluster

The following VPC endpoint policy allows full access for all accounts and
principals. At the same time, it denies any access for AWS account
`123456789012` to actions
performed on the Amazon Redshift cluster with cluster ID
`my-redshift-cluster`. Other Amazon Redshift
actions that don't support resource-level permissions for clusters are
still allowed. For a list of Amazon Redshift actions and their corresponding resource type,
see [Actions, Resources, and
Condition Keys for Amazon Redshift](../../../IAM/latest/UserGuide/list_amazonredshift.md "../../../IAM/latest/UserGuide/list_amazonredshift.md") in the
_IAM User Guide._

```

 {
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "*",
            "Effect": "Deny",
            "Resource": "arn:aws:redshift:us-east-1:123456789012:cluster:my-redshift-cluster",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}


```

#### Amazon Redshift Serverless Endpoint

Policy Examples

Following, you can find examples of VPC endpoint policies for Redshift Serverless.

##### Example: VPC

endpoint policy to allow read-only Redshift Serverless operations

The following VPC endpoint policy allows only AWS account
`123456789012` to perform the
specified Redshift Serverless actions.

The actions specified provide the equivalent of read-only access for Redshift Serverless.
All other actions on the VPC are denied for the specified account. Also, all
other accounts are denied any access. For a list of Redshift Serverless actions, see [Actions,
Resources, and Condition Keys for Redshift Serverless](../../../IAM/latest/UserGuide/list_amazonredshiftserverless.md "../../../IAM/latest/UserGuide/list_amazonredshiftserverless.md") in the
_IAM User Guide._

```

  {
    "Statement": [
        {
            "Action": [
                "redshift-serverless:DescribeOneTimeCredit",
                "redshift-serverless:GetCustomDomainAssociation",
                "redshift-serverless:GetEndpointAccess",
                "redshift-serverless:GetNamespace",
                "redshift-serverless:GetRecoveryPoint",
                "redshift-serverless:GetResourcePolicy",
                "redshift-serverless:GetScheduledAction",
                "redshift-serverless:GetSnapshot",
                "redshift-serverless:GetTableRestoreStatus",
                "redshift-serverless:GetUsageLimit",
                "redshift-serverless:GetWorkgroup"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}

```

##### Example: VPC

endpoint policy denying access to a specified workgroup

The following VPC endpoint policy allows full access for all accounts and
principals. At the same time, it denies any access for AWS account
`123456789012` to actions
performed on the Amazon Redshift workgroup with workgroup ID
`my-redshift-workgroup`. Other
Amazon Redshift actions that don't support resource-level permissions for workgroups
are still allowed. For a list of Redshift Serverless actions and their corresponding resource
type, see [Actions,
Resources, and Condition Keys for Redshift Serverless](../../../IAM/latest/UserGuide/list_amazonredshiftserverless.md "../../../IAM/latest/UserGuide/list_amazonredshiftserverless.md") in the
_IAM User Guide._

```

 {
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": "*"
        },
        {
            "Action": "*",
            "Effect": "Deny",
            "Resource": "arn:aws:redshift-serverless:us-east-1:123456789012:workgroup:my-redshift-workgroup",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}


```

# Connect to Amazon EMR on EKS Using an interface VPC endpoint

You can connect directly to Amazon EMR on EKS using [Interface VPC endpoints (AWS
PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in your Virtual Private Cloud (VPC) instead of connecting over the
internet. When you use an interface VPC endpoint, communication between your VPC and
Amazon EMR on EKS is conducted entirely within the AWS network. Each VPC endpoint is represented by
one or more [Elastic
network interfaces (ENIs)](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") with private IP addresses in your VPC subnets.

The interface VPC endpoint connects your VPC directly to Amazon EMR on EKS without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection. The instances in your VPC don't need public IP addresses to communicate with the Amazon EMR on EKS API.

You can create an interface VPC endpoint to connect to Amazon EMR on EKS using the AWS Management Console or AWS Command Line Interface (AWS CLI) commands. For more information, see [Creating
an Interface
Endpoint](../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint "../../../AmazonVPC/latest/UserGuide/vpce-interface.md#create-interface-endpoint").

After you create an interface VPC endpoint, if you enable private DNS hostnames for the endpoint, the default Amazon EMR on EKS endpoint resolves to your VPC endpoint. The default service name endpoint for Amazon EMR on EKS is in the following format.

```
emr-containers.Region.amazonaws.com
```

If you do not enable private DNS hostnames, Amazon VPC provides a DNS endpoint name that you can use in the following format.

```
VPC_Endpoint_ID.emr-containers.Region.vpce.amazonaws.com
```

For more information, see [Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the Amazon VPC User Guide.
Amazon EMR on EKS supports making calls to all of its [API Actions](../../../emr-on-eks/latest/APIReference/API_Operations.md "../../../emr-on-eks/latest/APIReference/API_Operations.md") inside your VPC.

You can attach VPC endpoint policies to a VPC endpoint to control access for IAM principals. You can also associate security groups with a VPC endpoint to control inbound and outbound access based on the origin and destination of network traffic, such as a range of IP addresses. For more information, see [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md").

## Create a VPC Endpoint Policy for Amazon EMR on EKS

You can create a policy for Amazon VPC endpoints for Amazon EMR on EKS to specify the following:

- The principal that can or cannot perform actions
- The actions that can be performed
- The resources on which actions can be performed

For more information, see [Controlling Access to Services with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the Amazon VPC User Guide.

###### Example VPC Endpoint Policy to Deny All Access From a Specified AWS Account

The following VPC endpoint policy denies AWS account `123456789012` all access to resources using the endpoint.

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
                    "`123456789012`"
                ]
            }
        }
    ]
}
```

###### Example VPC Endpoint Policy to Allow VPC Access Only to a Specified IAM Principal (User)

The following VPC endpoint policy allows full access only to the IAM user `lijuan` in AWS account `123456789012`. All other IAM principals are denied access using the endpoint.

```
{
    "Statement": [
        {
            "Action": "*",
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "arn:aws:iam::`123456789012`:user/`lijuan`"
                ]
            }
        }
    ]
}
```

###### Example VPC Endpoint Policy to Allow Read-Only Amazon EMR on EKS Operations

The following VPC endpoint policy allows only AWS account `123456789012` to perform the specified Amazon EMR on EKS actions.

The actions specified provide the equivalent of read-only access for Amazon EMR on EKS. All other actions on the VPC are denied for the specified account. All other accounts are denied any access. For a list of Amazon EMR on EKS actions, see [Actions, Resources, and Condition Keys for Amazon EMR on EKS](../../../IAM/latest/UserGuide/list_amazonemroneksemrcontainers.md "../../../IAM/latest/UserGuide/list_amazonemroneksemrcontainers.md").

```
{
    "Statement": [
        {
            "Action": [
                "emr-containers:DescribeJobRun",
                "emr-containers:DescribeVirtualCluster",
                "emr-containers:ListJobRuns",
                "emr-containers:ListTagsForResource",
                "emr-containers:ListVirtualClusters"
            ],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": [
                    "`123456789012`"
                ]
            }
        }
    ]
}
```

###### Example VPC Endpoint Policy Denying Access to a Specified Virtual Cluster

The following VPC endpoint policy allows full access for all accounts and principals,
but denies any access for AWS account `123456789012` to actions performed on the virtual
cluster with cluster ID `A1B2CD34EF5G`. Other Amazon EMR on EKS actions that don't support
resource-level permissions for virtual clusters are still allowed. For a list of Amazon EMR on EKS actions
and their corresponding resource type, see [Actions, Resources, and
Condition Keys for Amazon EMR on EKS](../../../IAM/latest/UserGuide/list_amazonemroneksemrcontainers.md "../../../IAM/latest/UserGuide/list_amazonemroneksemrcontainers.md")- in the _AWS Identity and Access Management User Guide_.

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
            "Resource": "arn:aws:emr-containers:us-west-2:`123456789012`:/virtualclusters/`A1B2CD34EF5G`",
            "Principal": {
                "AWS": [
                    "123456789012"
                ]
            }
        }
    ]
}
```

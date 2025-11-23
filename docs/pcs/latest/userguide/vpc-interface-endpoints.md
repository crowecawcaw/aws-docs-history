# Access AWS Parallel Computing Service using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS Parallel Computing Service (AWS PCS). You can access AWS PCS as if it were in your VPC, without the
use of an internet gateway, NAT device, VPN connection, or Direct Connect connection.
Instances in your VPC don't need public IP addresses to access AWS PCS.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface in
each subnet that you enable for the interface endpoint. These are requester-managed network
interfaces that serve as the entry point for traffic destined for AWS PCS.

For more information, see [Access AWS services through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

## Considerations for AWS PCS

Before you set up an interface endpoint for AWS PCS, review [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the
_AWS PrivateLink Guide_.

AWS PCS supports making calls to all of its API actions through the interface
endpoint.

If your VPC doesn't have direct internet access, you must configure a VPC endpoint to enable
your compute node group instances to call the AWS PCS
[`RegisterComputeNodeGroupInstance`](../APIReference/API_RegisterComputeNodeGroupInstance.md "../APIReference/API_RegisterComputeNodeGroupInstance.md")
API action.

## Create an interface endpoint for AWS PCS

You can create an interface endpoint for AWS PCS using either the Amazon VPC
console or the AWS Command Line Interface (AWS CLI). For more information, see [Create an interface endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the _AWS PrivateLink Guide_.

Create an interface endpoint for AWS PCS using the following service name:

```
com.amazonaws.`region`.pcs
```

Replace `region` with the ID of the AWS Region to create the
endpoint in, such as `us-east-1`.

If you enable private DNS for the interface endpoint, you can make API requests to
AWS PCS using its default Regional DNS name. For example,
`pcs.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to AWS PCS through the interface endpoint.
To control the access allowed to AWS PCS from your VPC, attach a custom endpoint policy
to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.
- The resources on which the actions can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policy for AWS PCS actions

The following is an example of a custom endpoint policy. When you attach
this policy to your interface endpoint, it grants access to the listed AWS PCS
actions for all principals to the cluster with the specified `cluster-id`.
Replace `region` with the ID of the AWS Region
of the cluster, such as `us-east-1`. Replace `account-id`
with the AWS account number of the cluster.

```
{
    "Statement": [
            {
                "Action": [
                "pcs:CreateCluster",
                "pcs:ListClusters",
                "pcs:DeleteCluster",
                "pcs:GetCluster",
                ],
                "Effect": "Allow",
                "Principal": "*",
                "Resource": [
                    "arn:aws:pcs:`region`:`account-id`:cluster/`cluster-id`*"
                ]
            }
        ]
}
```

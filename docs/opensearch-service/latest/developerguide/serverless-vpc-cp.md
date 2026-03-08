# Control plane access through AWS PrivateLink

Amazon OpenSearch Serverless supports two types of AWS PrivateLink connections for control plane and data
plane operations. Control plane operations include the creation and deletion of collections
and the management of access policies. Data plane operations are for indexing and querying
data within a collection. This page covers the control plane AWS PrivateLink endpoint. For
information about data plane VPC endpoints, see [Data plane access through AWS PrivateLink](serverless-vpc.md "serverless-vpc.md").

## Creating a control plane AWS PrivateLink endpoint

You can improve the security posture of your VPC by configuring OpenSearch Serverless to use an interface VPC endpoint. Interface endpoints are powered by AWS PrivateLink. This technology enables you to privately access OpenSearch Serverless APIs without an internet gateway, NAT device, VPN connection, or AWS Direct Connect connection.

For more information about AWS PrivateLink and VPC endpoints, see [VPC endpoints](../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints "../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints") in the Amazon VPC User Guide.

### Considerations

- VPC endpoints are supported within the same Region only.
- VPC endpoints only support Amazon-provided DNS through Amazon Route 53.
- VPC endpoints support endpoint policies to control access to OpenSearch Serverless Collections, Policies and VpcEndpoints.
- OpenSearch Serverless supports interface endpoints only. Gateway endpoints are not supported.

### Creating the VPC endpoint

To create the control plane VPC endpoint for Amazon OpenSearch Serverless, use the [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint") procedure in the _Amazon VPC Developer Guide_. Create the following endpoint:

- `com.amazonaws.`region`.aoss`

###### To create a control plane VPC endpoint using the console

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create Endpoint**.
4. For **Service category**, choose **AWS services**.
5. For **Services**, choose `com.amazonaws.`region`.aoss`. For example, `com.amazonaws.us-east-1.aoss`.
6. For **VPC**, choose the VPC in which to create the endpoint.
7. For **Subnets**, choose the subnets (Availability Zones) in which to create the endpoint network interfaces.
8. For **Security groups**, choose the security groups to associate with the endpoint network interfaces. Ensure HTTPS (port 443) is allowed.
9. For **Policy**, choose **Full access** to allow all operations, or choose **Custom** to attach a custom policy.
10. Choose **Create endpoint**.

### Creating an endpoint policy

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon OpenSearch Serverless. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

###### Example VPC endpoint policy for OpenSearch Serverless

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": [
        "aoss:ListCollections",
        "aoss:BatchGetCollection"
      ],
      "Resource": "*"
    }
  ]
}
```

###### Example Restrictive policy allowing only list operations

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": "*",
      "Action": "aoss:ListCollections",
      "Resource": "*"
    }
  ]
}
```

# Interface VPC endpoints

We provide AWS PrivateLink support between Amazon VPC and Amazon Managed Grafana. You can control access to
the Amazon Managed Grafana service from the virtual private cloud (VPC) endpoints by attaching an IAM
resource policy for Amazon VPC endpoints.

Amazon Managed Grafana supports two different kinds of VPC endpoints. You can connect to the Amazon Managed Grafana
service, providing access to the Amazon Managed Grafana APIs to manage workspaces. Or you can create a
VPC endpoint to a specific workspace.

## Using Amazon Managed Grafana with interface VPC

endpoints

There are two ways to use interface VPC endpoints with Amazon Managed Grafana. You can use a VPC
endpoint to allow AWS resources such as Amazon EC2 instances to access the Amazon Managed Grafana
API to manage resources, or you can use a VPC endpoint as part of limiting network
access to your Amazon Managed Grafana workspaces.

- If you are using Amazon VPC to host your AWS resources, you can
  establish a private connection between your VPC and the [Amazon Managed Grafana
  API](../APIReference/API_Operations.md "../APIReference/API_Operations.md") using the
  `com.amazonaws.`region`.grafana` service
  name endpoint.
- If you are trying to use network access control to add security to your
  Amazon Managed Grafana workspace, you can establish a private connection between your VPC
  and the Grafana workspaces endpoint, using the
  `com.amazonaws.`region`.grafana-workspace`
  service name endpoint.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual
network that you define. With a VPC, you have control over your network settings, such
as the IP address range, subnets, route tables, and network gateways. To connect your
VPC to your Amazon Managed Grafana API, you define an _interface VPC endpoint_ . The endpoint provides reliable, scalable connectivity to Amazon Managed Grafana without
requiring an internet gateway, a network address translation (NAT) instance, or a VPN
connection. For more information, see [What is Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the
_Amazon VPC User Guide._

_Interface VPC endpoints_ are powered by
AWS PrivateLink, an AWS technology that enables private communication between
AWS services using an elastic network interface with private IP addresses. For more
information, see [New – AWS PrivateLink for AWS Services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/ "https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/").

For information about how to get started with Amazon VPC, see [Get started](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md") in the
_Amazon VPC User Guide_.

## Creating a VPC endpoint to make an

AWS PrivateLink connection to Amazon Managed Grafana

Create an interface VPC endpoint to Amazon Managed Grafana with one of the following
service name endpoints:

- To connect to the Amazon Managed Grafana API for managing workspaces, choose:

`com.amazonaws.`region`.grafana`.

- To connect to a Amazon Managed Grafana workspace (for example, to use the Grafana API),
  choose:

`com.amazonaws.`region`.grafana-workspace`

For the details about creating an interface VPC endpoint, see [Create an
interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User
Guide._

For calling Grafana APIs, you must also enable private DNS for your VPC endpoint,
by following the instructions in the [Amazon VPC User Guide](../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names "../../../vpc/latest/privatelink/interface-endpoints.md#enable-private-dns-names"). This enables local resolution of URLs in the form
`*.grafana-workspace.`region`.amazonaws.com`

## Using network access control to limit access

to your Grafana workspace

If you want to limit what IP addresses or VPC endpoints can be used to access a
specific Grafana workspace, you can [configure
network access control](AMG-configure-nac.md "AMG-configure-nac.md") to that workspace.

For VPC endpoints that you give access to your workspace, you can further limit their
access by configuring security groups for the endpoints. To learn more, see [Associate security groups](../../../vpc/latest/privatelink/interface-endpoints.md#associate-security-groups "../../../vpc/latest/privatelink/interface-endpoints.md#associate-security-groups") and [Security group
rules](../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules "../../../vpc/latest/userguide/VPC_SecurityGroups.md#SecurityGroupRules") in the _Amazon VPC documentation_.

## Controlling access to your Amazon Managed Grafana API VPC endpoint with an

endpoint policy

For VPC endpoints that are connected the Amazon Managed Grafana API (using
`com.amazonaws.`region`.grafana`), you can add a VPC
endpoint policy to limit access to the service.

###### Note

VPC endpoints connected to workspaces (using
`com.amazonaws.`region`.grafana-workspace`) do
not support VPC endpoint policies.

A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when
you create or modify the endpoint. If you don't attach a policy when you create an
endpoint, Amazon VPC attaches a default policy for you that allows full access to the
service. An endpoint policy doesn't override or replace IAM identity-based policies or
service-specific policies. It's a separate policy for controlling access from the
endpoint to the specified service.

Endpoint policies must be written in JSON format.

For more information, see [Control
access to service with VPC endpoints](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the _Amazon VPC
User Guide._

The following is an example of an endpoint policy for Amazon Managed Grafana. This policy allows users
connecting to Amazon Managed Grafana through the VPC to send data to the Amazon Managed Grafana service. It also prevents
them from performing other Amazon Managed Grafana actions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AWSGrafanaPermissions",
 "Effect": "Allow",
 "Action": [
 "grafana:DescribeWorkspace",
 "grafana:UpdatePermissions",
 "grafana:ListPermissions",
 "grafana:ListWorkspaces"
 ],
 "Resource": "arn:aws:grafana:*:*:/workspaces*",
 "Principal": {
 "AWS": [
 "arn:aws:iam::`111122223333`:root"
 ]
 }
 }
 ]
}`

```

###### To edit the VPC endpoint policy for Grafana

1. Open the Amazon VPC console at [VPC
   console](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created endpoints, choose **Create
   Endpoint**.
4. Select the
   `com.amazonaws.`region`.grafana`
   endpoint, and then choose the **Policy** tab.
5. Choose **Edit Policy**, and then make your changes.

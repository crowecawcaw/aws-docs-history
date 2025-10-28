# Using Amazon Managed Service for Prometheus with interface VPC endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish private
connections between your VPC and Amazon Managed Service for Prometheus. You can use these connections to enable
Amazon Managed Service for Prometheus to communicate with your resources on your VPC without going through the public
internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such the IP
address range, subnets, route tables, and network gateways. To connect your VPC to
Amazon Managed Service for Prometheus, you define an _interface VPC endpoint_ to connect your VPC to
AWS services. The endpoint provides reliable, scalable connectivity to Amazon Managed Service for Prometheus without
requiring an internet gateway, a network address translation (NAT) instance, or a VPN
connection. For more information, see [What Is Amazon VPC](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md") in
the _Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables
private communication between AWS services using an elastic network interface with private
IP addresses. For more information, see the [New – AWS PrivateLink for AWS Services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/ "https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/") blog post.

The following information is for Amazon VPC users. For information about how to get started with Amazon VPC,
see [Getting Started](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md")
in the _Amazon VPC User Guide_.

## Create an interface VPC endpoint for Amazon Managed Service for Prometheus

Create an interface VPC endpoint to begin using Amazon Managed Service for Prometheus.
Choose from the following service name endpoints:

- `com.amazonaws.`region`.aps-workspaces`

Choose this service name to work with Prometheus-compatible APIs.
For more information,
see [Prometheus-compatible APIs](AMP-APIReference.md#AMP-APIReference-Prometheus-Compatible-Apis "AMP-APIReference.md#AMP-APIReference-Prometheus-Compatible-Apis")
in the _Amazon Managed Service for Prometheus User Guide_.

- `com.amazonaws.`region`.aps`

Choose this service name to perform workspace management tasks.
For more information,
see [Amazon Managed Service for Prometheus APIs](AMP-APIReference.md#AMP-APIReference-AMPApis "AMP-APIReference.md#AMP-APIReference-AMPApis")
in the _Amazon Managed Service for Prometheus User Guide_.

###### Note

If you are using remote_write in a VPC without direct internet access, you
must also create an interface VPC endpoint for AWS Security Token Service, to allow sigv4 to work
through the endpoint. For information
about creating a VPC endpoint for AWS STS, see [Using AWS STS
interface VPC endpoints](../../../IAM/latest/UserGuide/id_credentials_sts_vpce.md "../../../IAM/latest/UserGuide/id_credentials_sts_vpce.md") in the _AWS Identity and Access Management
User Guide_. You must set AWS STS to use [regionalized endpoints](../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md "../../../sdkref/latest/guide/feature-sts-regionalized-endpoints.md").

For more information, including step-by-step instructions to create an interface VPC
endpoint, see [Creating an interface endpoint](../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/privatelink/vpce-interface.md#create-interface-endpoint") in the
_Amazon VPC User Guide_.

###### Note

You can use **VPC endpoint policies** to control
access to your Amazon Managed Service for Prometheus interface VPC endpoint. See the next section for more
information.

If you created an interface VPC endpoint for Amazon Managed Service for Prometheus and already have data flowing
to the workspaces located on your VPC, the metrics will flow through the interface VPC
endpoint by default. Amazon Managed Service for Prometheus uses public endpoints or private interface endpoints
(whichever are in use) to perform this task.

### Controlling access to your Amazon Managed Service for Prometheus VPC endpoint

You can use VPC endpoint policies to control
access to your Amazon Managed Service for Prometheus interface VPC endpoint. A VPC endpoint policy is an IAM
resource policy that you attach to an endpoint when you create or modify the
endpoint. If you don't attach a policy when you create an endpoint, Amazon VPC
attaches a default policy for you that allows full access to the service. An
endpoint policy doesn't override or replace IAM identity-based policies or
service-specific policies. It's a separate policy for controlling access from
the endpoint to the specified service.

For more information, see [Controlling Access to Services
with VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of an endpoint policy for Amazon Managed Service for Prometheus. This policy
allows users with the role `PromUser` connecting to Amazon Managed Service for Prometheus through
the VPC to view workspaces and rule groups, but not, for example, to create or
delete workspaces.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "AmazonManagedPrometheusPermissions",
 "Effect": "Allow",
 "Action": [
 "aps:DescribeWorkspace",
 "aps:DescribeRuleGroupsNamespace",
 "aps:ListRuleGroupsNamespaces",
 "aps:ListWorkspaces"
 ],
 "Resource": "arn:aws:aps:*:*:/workspaces*",
 "Principal": {
 "AWS": [
 "arn:aws:iam::111122223333:role/PromUser"
 ]
 }
 }
 ]
}`

```

The following example shows a policy that only allows requests coming from a
specified IP address in the specified VPC to succeed. Requests from other IP
addresses will fail.

```
{
    "Statement": [
        {
            "Action": "aps:*",
            "Effect": "Allow",
            "Principal": "*",
            "Resource": "*",
            "Condition": {
                "IpAddress": {
                    "aws:VpcSourceIp": "192.0.2.123"
                },
        "StringEquals": {
                    "aws:SourceVpc": "vpc-555555555555"
                }
            }
        }
    ]
}
```

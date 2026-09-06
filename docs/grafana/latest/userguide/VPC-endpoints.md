

# Interface VPC endpoints
<a name="VPC-endpoints"></a>

We provide AWS PrivateLink support between Amazon VPC and Amazon Managed Grafana. You can control access to the Amazon Managed Grafana service from the virtual private cloud (VPC) endpoints by attaching an IAM resource policy for Amazon VPC endpoints. 

Amazon Managed Grafana supports two different kinds of VPC endpoints. You can connect to the Amazon Managed Grafana service, providing access to the Amazon Managed Grafana APIs to manage workspaces. Or you can create a VPC endpoint to a specific workspace.

## Using Amazon Managed Grafana with interface VPC endpoints
<a name="Using-grafana-with-VPC-endpoints"></a>

There are two ways to use interface VPC endpoints with Amazon Managed Grafana. You can use a VPC endpoint to allow AWS resources such as Amazon EC2 instances to access the Amazon Managed Grafana API to manage resources, or you can use a VPC endpoint as part of limiting network access to your Amazon Managed Grafana workspaces.
+ If you are using Amazon VPC to host your AWS resources, you can establish a private connection between your VPC and the [Amazon Managed Grafana API](https://docs.aws.amazon.com/grafana/latest/APIReference/API_Operations.html) using the `com.amazonaws.{{region}}.grafana` service name endpoint.
+ If you are trying to use network access control to add security to your Amazon Managed Grafana workspace, you can establish a private connection between your VPC and the Grafana workspaces endpoint, using the `com.amazonaws.{{region}}.grafana-workspace` service name endpoint.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network that you define. With a VPC, you have control over your network settings, such as the IP address range, subnets, route tables, and network gateways. To connect your VPC to your Amazon Managed Grafana API, you define an *interface VPC endpoint *. The endpoint provides reliable, scalable connectivity to Amazon Managed Grafana without requiring an internet gateway, a network address translation (NAT) instance, or a VPN connection. For more information, see [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) in the *Amazon VPC User Guide.*

* Interface VPC endpoints* are powered by AWS PrivateLink, an AWS technology that enables private communication between AWS services using an elastic network interface with private IP addresses. For more information, see [New – AWS PrivateLink for AWS Services](https://aws.amazon.com/blogs/aws/new-aws-privatelink-endpoints-kinesis-ec2-systems-manager-and-elb-apis-in-your-vpc/).

For information about how to get started with Amazon VPC, see [Get started](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-getting-started.html) in the *Amazon VPC User Guide*.

## Creating a VPC endpoint to make an AWS PrivateLink connection to Amazon Managed Grafana
<a name="creating-interface-VPC-endpoints"></a>

 Create an interface VPC endpoint to Amazon Managed Grafana with one of the following service name endpoints: 
+ To connect to the Amazon Managed Grafana API for managing workspaces, choose: 

  `com.amazonaws.{{region}}.grafana`.
+ To connect to a Amazon Managed Grafana workspace (for example, to use the Grafana API), choose: 

  `com.amazonaws.{{region}}.grafana-workspace`



For the details about creating an interface VPC endpoint, see [Create an interface endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/vpce-interface.html#create-interface-endpoint) in the *Amazon VPC User Guide.* 

For calling Grafana APIs, you must also enable private DNS for your VPC endpoint, by following the instructions in the [Amazon VPC User Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html#enable-private-dns-names). This enables local resolution of URLs in the form `*.grafana-workspace.{{region}}.amazonaws.com`

## Using network access control to limit access to your Grafana workspace
<a name="vpc-endpoint-with-nac"></a>

If you want to limit what IP addresses or VPC endpoints can be used to access a specific Grafana workspace, you can [configure network access control](AMG-configure-nac.md) to that workspace.

For VPC endpoints that you give access to your workspace, you can further limit their access by configuring security groups for the endpoints. To learn more, see [Associate security groups](https://docs.aws.amazon.com/vpc/latest/privatelink/interface-endpoints.html#associate-security-groups) and [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the *Amazon VPC documentation*.

## Controlling access to your Amazon Managed Grafana API VPC endpoint with an endpoint policy
<a name="controlling-vpc"></a>

For VPC endpoints that are connected the Amazon Managed Grafana API (using `com.amazonaws.{{region}}.grafana`), you can add a VPC endpoint policy to limit access to the service.

**Note**  
VPC endpoints connected to workspaces (using `com.amazonaws.{{region}}.grafana-workspace`) do not support VPC endpoint policies.

A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you create or modify the endpoint. If you don't attach a policy when you create an endpoint, Amazon VPC attaches a default policy for you that allows full access to the service. An endpoint policy doesn't override or replace IAM identity-based policies or service-specific policies. It's a separate policy for controlling access from the endpoint to the specified service.

Endpoint policies must be written in JSON format.

For more information, see [Control access to service with VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-access.html) in the *Amazon VPC User Guide.*

The following is an example of an endpoint policy for Amazon Managed Grafana. This policy allows users connecting to Amazon Managed Grafana through the VPC to send data to the Amazon Managed Grafana service. It also prevents them from performing other Amazon Managed Grafana actions. 

------
#### [ JSON ]

****  

```
{
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
                    "arn:aws:iam::{{111122223333}}:root"
                ]
            }
        }
    ]
}
```

------

**To edit the VPC endpoint policy for Grafana**

1. Open the Amazon VPC console at [VPC console](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. If you have not already created endpoints, choose **Create Endpoint**.

1. Select the `com.amazonaws.{{region}}.grafana` endpoint, and then choose the **Policy** tab.

1. Choose **Edit Policy**, and then make your changes.
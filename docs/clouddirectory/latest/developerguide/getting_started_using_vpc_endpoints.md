Amazon Cloud Directory is no longer be open to new customers. For alternatives to Cloud Directory, explore [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and [Amazon Neptune](https://aws.amazon.com/neptune/ "https://aws.amazon.com/neptune/"). If you need help choosing the right alternative for your use case, or for any other questions, contact [AWS Support](https://aws.amazon.com/support/ "https://aws.amazon.com/support/").

# Using Cloud Directory Interface VPC

Endpoints

If you use Amazon Virtual Private Cloud (Amazon VPC) to host your AWS resources, you can establish a private
connection between your VPC and Cloud Directory. You can use this connection to enable Cloud Directory to
communicate with your resources on your VPC without going through the public internet.

Amazon VPC is an AWS service that you can use to launch AWS resources in a virtual network
that you define. With a VPC, you have control over your network settings, such as the IP address
range, subnets, route tables, and network gateways. To connect your VPC to Cloud Directory, you define an
_interface VPC endpoint_ for Cloud Directory. The endpoint provides reliable,
scalable connectivity to Cloud Directory without requiring an internet gateway, network address
translation (NAT) instance, or VPN connection. For more information, see [What Is Amazon VPC?](../../../vpc/latest/userguide/VPC_Introduction.md "../../../vpc/latest/userguide/VPC_Introduction.md") in the _Amazon VPC User Guide_.

Interface VPC endpoints are powered by AWS PrivateLink, an AWS technology that enables
private communication between AWS services using an elastic network interface with private IP
addresses. For more information, see [AWS PrivateLink for AWS
Services](../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink "../../../vpc/latest/userguide/VPC_Introduction.md#what-is-privatelink").

The following steps are for users of Amazon VPC. For more information, see [Getting Started with Amazon VPC](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User Guide_.

## Availability

Cloud Directory currently supports VPC endpoints in the following Regions:

- US East (Ohio)
- US East (N. Virginia)
- US West (Oregon)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- AWS GovCloud (US-West)

## Create a VPC for Cloud Directory

To start using Cloud Directory with your VPC, use the Amazon VPC console to create an interface VPC
endpoint for Cloud Directory. For more information, see [Creating an Interface
Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint").

- For **Service Category**, choose **AWS
  services**.
- For **Service Name**, choose
  **`com.amazonaws.`region`.clouddirectory`**.
  This creates a VPC endpoint for Cloud Directory operations.

For general information, see [What is
Amazon VPC?](../../../vpc/latest/userguide/what-is-amazon-vpc.md "../../../vpc/latest/userguide/what-is-amazon-vpc.md") in the _Amazon VPC User Guide_.

### Control Access to Your Cloud Directory VPC

Endpoint

A VPC endpoint policy is an IAM resource policy that you attach to an endpoint when you
create or modify the endpoint. If you don't attach a policy when you create an endpoint, we
attach a default policy for you that allows full access to the service. An endpoint policy
doesn't override or replace IAM user policies or service-specific policies. It's a separate
policy for controlling access from the endpoint to the specified service.

Endpoint policies must be written in JSON format. For more information, see [Controlling Access to Services with VPC
Endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

The following is an example of an endpoint policy for Cloud Directory. This policy enables users
connecting to Cloud Directory through the VPC to list directories and prevents them from performing
other Cloud Directory actions.

```
{
  "Statement": [
    {
      "Sid": "ReadOnly",
      "Principal": "*",
      "Action": [
        "clouddirectory:ListDirectories"
      ],
      "Effect": "Allow",
      "Resource": "*"
    }
  ]
}
```

###### To modify the VPC endpoint policy for Cloud Directory

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. If you have not already created the endpoint for Cloud Directory, choose **Create
   Endpoint**. Then select
   **`com.amazonaws.`region`.clouddirectory`**
   and choose **Create endpoint**.
4. Select the
   **`com.amazonaws.`region`.clouddirectory`**
   endpoint and choose the **Policy** tab in the lower half of the
   screen.
5. Choose **Edit Policy** and make the changes to the policy.

For more information, see [Controlling Access
to Services with VPC Endpoints](../../../vpc/latest/userguide/GetStarted.md "../../../vpc/latest/userguide/GetStarted.md") in the _Amazon VPC User
Guide_.

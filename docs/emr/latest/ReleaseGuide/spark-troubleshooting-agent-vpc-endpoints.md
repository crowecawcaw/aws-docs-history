# Configuring Interface VPC Endpoints for Amazon SageMaker Unified Studio MCP

You can establish a private connection between your VPC and Amazon SageMaker Unified Studio MCP service by creating an _interface VPC endpoint_. Interface endpoints are powered by [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/"), which enables you to privately access the MCP server in your VPC without an internet gateway, NAT device, VPN connection, or connection. Instances in your VPC don't need public IP addresses to communicate with the MCP service and traffic between your VPC and MCP service does not leave the Amazon network.

Each interface endpoint is represented by one or more [Elastic Network Interfaces](../../../AWSEC2/latest/UserGuide/using-eni.md "../../../AWSEC2/latest/UserGuide/using-eni.md") in your VPC subnets. For more information, see [Interface VPC endpoints](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md") in the _Amazon VPC User Guide_.

## Step 1: Creating an interface VPC endpoint for Amazon SageMaker Unified Studio MCP

You can create a VPC endpoint for the Amazon SageMaker Unified Studio MCP service using either the Amazon VPC console or the AWS CLI. For more information, see [Creating an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") in the _Amazon VPC User Guide_.

Create a VPC endpoint for Amazon SageMaker Unified Studio MCP using the following service name:

- com.amazonaws.`<aws-region>`.sagemaker-unified-studio-mcp

If you enable private DNS for the endpoint, you can make API requests to Amazon SageMaker Unified Studio MCP using its default DNS name for the Region, for example, `sagemaker-unified-studio-mcp.us-east-1.api.aws`

For more information, see [Accessing a service through an interface endpoint](../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint "../../../vpc/latest/userguide/vpce-interface.md#access-service-though-endpoint") in the _Amazon VPC User Guide_.

## Step 2: Creating a VPC endpoint Policy for Amazon SageMaker Unified Studio MCP

You can attach an endpoint policy to your VPC endpoint that controls access to Amazon SageMaker Unified Studio MCP. The policy specifies the following information:

- The principal that can perform actions.
- The actions that can be performed.
- The resources on which actions can be performed.

For more information, see [Controlling access to services with VPC endpoints](../../../vpc/latest/userguide/vpc-endpoints-access.md "../../../vpc/latest/userguide/vpc-endpoints-access.md") in the _Amazon VPC User Guide_.

### Example: VPC endpoint policy to allow MCP access to a specific IAM role

The following is an example of an endpoint policy for Amazon SageMaker Unified Studio MCP access. When attached to an endpoint, this policy grants access to the listed Amazon SageMaker Unified Studio MCP actions for a specific IAM role principal on all resources.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::ACCOUNT-ID:role/YourRoleName"
      },
      "Action": [
        "sagemaker-unified-studio-mcp:InvokeMcp",
        "sagemaker-unified-studio-mcp:CallReadOnlyTool",
        "sagemaker-unified-studio-mcp:CallPrivilegedTool"
      ],
      "Resource": "*"
    }
  ]
}
```

## Step 3: Testing your VPC

The `curl` command validates end-to-end network connectivity from your VPC network (EC2) to the VPC endpoint by making an HTTP/HTTPS request. A curl response receiving a Message back from the MCP server confirms that the complete network path is functional.

### Method 1: With Private DNS Enabled (Recommended)

```
curl https://sagemaker-unified-studio-mcp.us-east-1.api.aws/spark-troubleshooting/mcp
```

### Method 2: Without Private DNS Enabled

```
curl -k https://vpce-0069xxxx-ejwhxxx.sagemaker-unified-studio-mcp.us-east-1.vpce.amazonaws.com/spark-troubleshooting/mcp
```

###### Note

The `-k` flag bypasses SSL certificate verification due to hostname mismatch between the VPC endpoint DNS name and the certificate's Common Name (CN).

In both cases, the curl command returns a response: `{"Message":"...."}`. Returning with a Message verifies the successful network path connectivity to the VPC endpoint of the MCP service.

## Step 4: Start using the MCP VPC endpoint

Once you have verified the connection, you can follow the steps to configure the MCP in [Setup for Troubleshooting Agent](spark-troubleshooting-agent-setup.md "spark-troubleshooting-agent-setup.md"). Simply use the private VPC endpoint in your MCP configuration.

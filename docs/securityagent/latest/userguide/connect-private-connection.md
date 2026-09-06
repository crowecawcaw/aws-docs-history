

# Connect to privately hosted source control
<a name="connect-private-connection"></a>

AWS Security Agent can connect to source control systems running in private networks, such as GitLab Self-Managed instances and GitHub Enterprise Server. Private connections use Amazon VPC Lattice to establish secure connectivity between AWS Security Agent and your private infrastructure without exposing your systems to the public internet.

## How private connections work
<a name="_how_private_connections_work"></a>

A private connection creates a secure network path between AWS Security Agent and a target resource in your VPC. Under the hood, AWS Security Agent uses Amazon VPC Lattice to establish this connectivity. VPC Lattice is an AWS application networking service for connecting, securing, and monitoring traffic between services across VPCs and accounts, without you managing the underlying network infrastructure.

When you create a private connection:

1. You provide the VPC, subnets, and (optionally) security groups that have network connectivity to your target service.

1. AWS Security Agent creates a service-managed resource gateway and provisions elastic network interfaces (ENIs) in the subnets you specified.

1. The agent uses the resource gateway to route traffic to your target service’s IP address or DNS name over the private network path.

## Service-managed vs. self-managed private connections
<a name="_service_managed_vs_self_managed_private_connections"></a>

AWS Security Agent supports two modes for private connections:

 **Service-managed** (recommended for simple setups):
+ AWS Security Agent creates and manages the VPC Lattice resource gateway for you.
+ The target service must be running in the **same AWS account** where the Agent Space is created.
+ Cannot span multiple AWS accounts.

 **Self-managed** (for advanced or cross-account setups):
+ You create and manage your own VPC Lattice resource configuration.
+ You provide the Amazon Resource Name (ARN) of your existing resource configuration.
+ Supports cross-account access (customer manages cross-account networking).

## Prerequisites
<a name="_prerequisites"></a>

Before creating a private connection, verify that you have:
+ An active Agent Space
+ A privately reachable target service (GitLab Self-Managed or GitHub Enterprise Server) at a known private IP address or DNS name
+ The target service must serve HTTPS traffic with a minimum TLS version of 1.2
+ Subnets in your VPC (1-20 subnets). We recommend selecting subnets in multiple Availability Zones for high availability.
+ (Optional) Security groups to control traffic to the ENIs (up to 5)

**Note**  
The following Availability Zones are not supported by VPC Lattice: `use1-az3`, `usw1-az2`, `apne1-az3`, `apne2-az2`, `euc1-az2`, `euw1-az4`, `cac1-az3`, `ilc1-az2`.

**Note**  
Private connections are account-level resources. After you create a private connection, you can reuse it across multiple integrations and Agent Spaces that need to reach the same host.

**Note**  
When you select a private connection for a provider that uses OAuth authentication, the private connection applies to both the provider endpoint and the token exchange endpoint. Ensure the private connection is configured with a host address that can route traffic to both endpoints.

## Create a private connection
<a name="create-a-private-connection"></a>

1. In the AWS Security Agent Management Console, navigate to **Integrations**.

1. Choose the **Private connections** tab.

1. Choose **Create private connection**.

1. Under **Connection details**, enter a **Name**. Names can contain lowercase letters, numbers, and hyphens, and must start and end with a letter or number.

1. In the **Connection details** section, choose how AWS Security Agent connects to your target service:
   + To have AWS Security Agent create and manage the connection, leave **Use existing resource configuration** cleared, then complete the **Resource location**, **Access control**, and **Service target details** sections.
   + To route through a VPC Lattice resource configuration that you already created, select **Use existing resource configuration**, then complete the **Existing resource configuration** section. The service-managed sections do not apply.

1. (Service-managed) Under **Resource location**:

   1. Select the **VPC where your resource is located**.

   1. Select one or more **Subnets**. We recommend selecting subnets in at least two Availability Zones.

   1. (Optional) Select an **IP address type** (IPv4, IPv6, or Dual stack).

1. (Service-managed) Under **Access control**:

   1. Select the **Security groups associated with your connected resources**.

   1. (Optional) Under **Advanced configuration**, enter **Port ranges** — up to 11 comma-separated TCP ports or ranges, for example `443, 8080-8090`.

1. (Service-managed) Under **Service target details**:

   1. In the **Host address** field, enter the DNS host name or IP address of your target service.

   1. For **DNS resolution**, select **Public** for a publicly resolvable host address, or **In VPC (private DNS)** for an address resolvable only inside the VPC.

   1. (Optional) In the **Certificate public key** field, enter the PEM-encoded public key if your target uses a self-signed certificate or a private certificate authority. This lets AWS Security Agent trust the TLS connection.

1. (Self-managed) Under **Existing resource configuration**, for **Resource configuration**, select a VPC Lattice resource configuration from the list, or enter a resource configuration ID (beginning with `rcfg-`) or its ARN. The list shows resource configurations in the current Region.

1. (Optional) Under **Tags**, add one or more tags to the private connection. Each tag is a key-value pair that helps you organize and identify your resources.

1. Choose **Create connection**.

   The connection status changes to **Create in progress**. This can take up to 10 minutes. When complete, the status changes to **Available**.

## Use a private connection with an integration
<a name="_use_a_private_connection_with_an_integration"></a>

When you register a GitLab Self-Managed or GitHub Enterprise Server integration, select **Connect to endpoint using a private connection**, then choose your connection from the **Private connection** list. AWS Security Agent routes traffic to the provider through that connection. Only connections with an **Available** status appear in the list.

You can also choose **Create a private connection** during registration. AWS Security Agent preserves your registration draft while you create the connection, then returns you to the registration flow.

## Security
<a name="_security"></a>
+  **No public internet exposure** - All traffic stays on the AWS network.
+  **Customer-controlled security groups** - You manage inbound and outbound traffic rules.
+  **Service-linked role with least privilege** - AWS Security Agent uses a service-linked role scoped to resources tagged with `AWSSecurityAgentManaged`.

**Note**  
If your organization has service control policies (SCPs) that restrict VPC Lattice API actions, the service-managed resource gateway is created through a service-linked role. Ensure your SCPs permit the necessary actions for the service-linked role.

## Verify a private connection
<a name="_verify_a_private_connection"></a>

After the private connection reaches the **Available** status, verify connectivity:
+ Ensure your target service is running and accepting connections on the expected port
+ Verify that security groups attached to the ENIs allow outbound traffic on the target port
+ Verify that your service’s security group allows inbound traffic from VPC Lattice data plane IPs within your VPC CIDR range
+ Confirm that subnet route tables allow traffic between the ENI subnets and your service

## Delete a private connection
<a name="_delete_a_private_connection"></a>

1. In the AWS Security Agent console, navigate to **Integrations**.

1. Choose the **Private connections** tab.

1. Select the private connection you want to delete.

1. Choose **Delete**.

**Important**  
You cannot delete a private connection that is currently in use by an integration. Remove the integration first, then delete the private connection.

## Advanced setup using existing VPC Lattice resources
<a name="_advanced_setup_using_existing_vpc_lattice_resources"></a>

If your organization already uses Amazon VPC Lattice and manages your own resource configurations, you can create a private connection in self-managed mode. You provide the Amazon Resource Name (ARN) of an existing resource configuration that points to your target service. You manage the resource gateway yourself, rather than having AWS Security Agent create one.

Consider self-managed mode when you want to:
+ Control the resource gateway and resource configuration lifecycle yourself.
+ Share a resource configuration across multiple AWS accounts or services.
+ Use VPC Lattice access logs for detailed traffic monitoring.
+ Run a hub-and-spoke network architecture.

To use an existing resource configuration, select **Use existing resource configuration** when you create the private connection, then choose a configuration under **Existing resource configuration**. For the full console steps, see [Create a private connection](#create-a-private-connection) earlier on this page.

The resource configuration picker lists configurations in the current console Region. If the list is empty or access is denied, enter a resource configuration ID (starting with `rcfg-`) or its ARN directly.

**Note**  
To populate the resource configuration picker, AWS Security Agent needs the `vpc-lattice:ListResourceConfigurations` permission. If this call returns an access-denied error, the picker falls back to manual entry. You can paste the resource configuration ID or ARN instead.

In self-managed mode, AWS Security Agent does not collect a certificate public key in the console. Your resource configuration defines the target service and its TLS settings.

For more information about creating VPC Lattice resource gateways and resource configurations, see the [Amazon VPC Lattice User Guide](https://docs.aws.amazon.com/vpc-lattice/latest/ug/).

## Cross-Region connectivity
<a name="_cross_region_connectivity"></a>

You must create a private connection in the same AWS Region as your Agent Space. If your target service runs in a different Region, use self-managed mode with inter-Region Amazon VPC peering or AWS Transit Gateway peering.

Follow this pattern:

1. Establish inter-Region connectivity between a VPC in the Agent Space Region and the target service’s VPC. Use VPC peering or Transit Gateway peering. The VPC CIDR ranges must not overlap.

1. Create a VPC Lattice resource gateway in the Agent Space Region, in a VPC that has the peering connection.

1. Create a VPC Lattice resource configuration in the Agent Space Region that points to the target service’s IP address. The address must be routable through the peering connection.

1. Create a self-managed private connection that uses that resource configuration ARN.

## Next steps
<a name="_next_steps"></a>
+  [Connect AWS Security Agent to GitLab Self-Managed](connect-gitlab-self-managed.md) - Connect a private GitLab instance
+  [Connect AWS Security Agent to GitHub Enterprise](connect-github-enterprise.md) - Connect a private GitHub Enterprise instance
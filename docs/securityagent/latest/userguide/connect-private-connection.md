# Connect to privately hosted source control

AWS Security Agent can connect to source control systems running in private networks, such as GitLab Self-Managed instances and GitHub Enterprise Server. Private connections use Amazon VPC Lattice to establish secure connectivity between AWS Security Agent and your private infrastructure without exposing your systems to the public internet.

## How private connections work

A private connection creates a secure network path between AWS Security Agent and a target resource in your VPC. Under the hood, AWS Security Agent uses Amazon VPC Lattice to establish this connectivity.

When you create a private connection:

1. You provide the VPC, subnets, and (optionally) security groups that have network connectivity to your target service.
2. AWS Security Agent creates a service-managed resource gateway and provisions elastic network interfaces (ENIs) in the subnets you specified.
3. The agent uses the resource gateway to route traffic to your target service’s IP address or DNS name over the private network path.

## Service-managed vs. self-managed private connections

AWS Security Agent supports two modes for private connections:

**Service-managed** (recommended for simple setups):

- AWS Security Agent creates and manages the VPC Lattice resource gateway for you.
- The target service must be running in the **same AWS account** where the Agent Space is created.
- Cannot span multiple AWS accounts.

**Self-managed** (for advanced or cross-account setups):

- You create and manage your own VPC Lattice resource configuration.
- You provide the Amazon Resource Name (ARN) of your existing resource configuration.
- Supports cross-account access (customer manages cross-account networking).

## Prerequisites

Before creating a private connection, verify that you have:

- An active Agent Space
- A privately reachable target service (GitLab Self-Managed or GitHub Enterprise Server) at a known private IP address or DNS name
- The target service must serve HTTPS traffic with a minimum TLS version of 1.2
- Subnets in your VPC (1-20 subnets). We recommend selecting subnets in multiple Availability Zones for high availability.
- (Optional) Security groups to control traffic to the ENIs (up to 5)

###### Note

The following Availability Zones are not supported by VPC Lattice: `use1-az3`, `usw1-az2`, `apne1-az3`, `apne2-az2`, `euc1-az2`, `euw1-az4`, `cac1-az3`, `ilc1-az2`.

###### Note

Private connections are account-level resources. After you create a private connection, you can reuse it across multiple integrations and Agent Spaces that need to reach the same host.

###### Note

When you select a private connection for a provider that uses OAuth authentication, the private connection applies to both the provider endpoint and the token exchange endpoint. Ensure the private connection is configured with a host address that can route traffic to both endpoints.

## Create a private connection

1. In the AWS Security Agent Management Console, navigate to **Integrations**.
2. Choose **Private connections**.
3. Choose **Create private connection**.
4. Configure the following fields:

   1. **Name** - Enter a descriptive name (for example, `gitlab-internal-connection`).
   2. **VPC** - Select the VPC where the resource gateway ENIs will be deployed.
   3. **Subnets** - Select one or more subnets (up to 20). We recommend at least two Availability Zones.
   4. **IP address type** - Select the IP type of your target service (IPv4, IPv6, or Dualstack).
   5. **(Optional) Security groups** - Select existing security groups (up to 5). If omitted, a default security group is created.
   6. **(Optional) Port ranges** - Specify the TCP ports your target service listens on (for example, `443`).
   7. **Host address** - Enter the IP address or DNS name of your target service.
   8. **(Optional) Certificate public key** - If your target uses TLS certificates from a private certificate authority, enter the PEM-encoded public key. This allows AWS Security Agent to trust the TLS connection.

5. Choose **Create connection**.

The connection status changes to **Create in progress**. This can take up to 10 minutes. When complete, the status changes to **Available**.

## Use a private connection with an integration

When registering a GitLab Self-Managed or GitHub Enterprise Server integration, select your private connection in the registration flow:

1. During integration registration, in the **Private connection** field, select your available private connection.
2. AWS Security Agent will route all traffic to the provider through this private connection.

## Security

- **No public internet exposure** - All traffic stays on the AWS network.
- **Customer-controlled security groups** - You manage inbound and outbound traffic rules.
- **Service-linked role with least privilege** - AWS Security Agent uses a service-linked role scoped to resources tagged with `AWSSecurityAgentManaged`.

###### Note

If your organization has service control policies (SCPs) that restrict VPC Lattice API actions, the service-managed resource gateway is created through a service-linked role. Ensure your SCPs permit the necessary actions for the service-linked role.

## Verify a private connection

After the private connection reaches the **Available** status, verify connectivity:

- Ensure your target service is running and accepting connections on the expected port
- Verify that security groups attached to the ENIs allow outbound traffic on the target port
- Verify that your service’s security group allows inbound traffic from VPC Lattice data plane IPs within your VPC CIDR range
- Confirm that subnet route tables allow traffic between the ENI subnets and your service

## Delete a private connection

You can delete unused private connections from the AWS Management Console.

1. In the AWS Security Agent console, navigate to **Integrations**.
2. Choose **Private connections**.
3. Select the private connection you want to delete.
4. Choose **Delete**.

The private connection status changes to **Removing connection** while AWS Security Agent removes the managed resource gateway and ENIs from your VPC.

###### Important

You cannot delete a private connection that is currently in use by an integration. Remove the integration first, then delete the private connection.

## Next steps

- [Connect AWS Security Agent to GitLab Self-Managed](connect-gitlab-self-managed.md "connect-gitlab-self-managed.md") - Connect a private GitLab instance
- [Connect AWS Security Agent to GitHub Enterprise Server](connect-github-enterprise-server.md "connect-github-enterprise-server.md") - Connect a private GitHub Enterprise Server

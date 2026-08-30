# Troubleshooting private connections

This page describes common problems you might encounter when creating or using a [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md") for AWS DevOps Agent, and how to resolve them. Each section describes a symptom, the most likely causes, and the steps to fix it.

For an overview of how private connections work, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").

## A DNS host address doesn't resolve, or traffic reaches the wrong place

**Symptom**

You created a private connection using a DNS name for the host address, but the connection can't reach your service. This is most common when your target service is a self-hosted GitLab instance, an internal Application Load Balancer (ALB), or an MCP server whose hostname only exists inside your VPC.

A DNS resolution failure doesn't produce a message that mentions DNS. Instead, it surfaces as a generic reachability or provider error when you register or use the capability provider. For example, you might see `Could not complete request to provider.`, `Unable to connect to the MCP server at <endpoint>. The connection was interrupted.`, or even an authentication error such as `Authentication with provider failed.` Because the message doesn't point to DNS, use the following check to confirm the cause.

**Cause**

By default, a private connection resolves the host address using **public DNS** (`dnsResolution: PUBLIC`). If your hostname only has a record in a [private hosted zone](../../../Route53/latest/DeveloperGuide/hosted-zones-private.md "../../../Route53/latest/DeveloperGuide/hosted-zones-private.md"), an Amazon Route 53 Resolver rule, or an on-premises DNS server, public resolution fails and the connection never reaches your service.

**How to confirm DNS is the cause**

- Check whether your host address resolves only inside your VPC. From an Amazon EC2 instance or AWS CloudShell session in the same VPC, run `nslookup <your-host-address>`. If it resolves there but not from public DNS, and your private connection uses `dnsResolution: PUBLIC`, DNS resolution is the cause.
- Test with the IP address instead of the name. Temporarily create a private connection that uses the target's private IP address (or a load balancer IP) for the host address instead of the DNS name. If the connection then reaches your service, the earlier failure was DNS resolution, not the network path or the service itself.

**Resolution**

- If your hostname resolves only inside your VPC, set the DNS resolution mode to **In VPC** (`IN_VPC`) when you create the connection. In this mode, the host address is resolved from within your VPC context, so private-only hostnames resolve correctly. See [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").
- The DNS resolution mode is chosen at creation time and applies to the host address you provide. You can't change how the service-managed resource gateway resolves DNS after creation, so choose the correct mode up front. If you selected the wrong mode, delete the connection and recreate it with the correct mode.
- If you specify an **IP address** (rather than a DNS name) for the host address, the DNS resolution mode has no effect, and traffic goes directly to that IP.
- If you can't use `IN_VPC` for your setup, you can instead point the host address at the target's private IP address, or at the DNS name of a load balancer that is publicly resolvable but forwards to a private IP.

## The connection is stuck in Create failed

**Symptom**

After you create a private connection, the console shows the status as **Connection Failed** (and `describe-private-connection` returns a status of `CREATE_FAILED`). The response often doesn't include a detailed reason for the failure, so you're left without an error message to act on.

**Cause**

Create failed most often results from a configuration problem in the request or in your VPC, rather than a service error. Because a detailed failure reason isn't always surfaced, work through the following checklist even when no error message is shown.

**Resolution**

Verify the following, in order:

1. **Port ranges use a valid format.** Specify each port range as either a single port (for example, `443`) or a genuine range with different start and end ports (for example, `8080-8090`). A "range" whose start and end are the same (for example, `443-443`) is rejected. You can specify up to 11 port ranges.
2. **Your subnets have available IP addresses.** The resource gateway provisions elastic network interfaces (ENIs) in the subnets you specify. If those subnets are exhausted, creation fails. Choose subnets with free address space.
3. **Your subnets are in supported Availability Zones.** Amazon VPC Lattice doesn't support every Availability Zone. Run the following and compare against the unsupported zones listed in [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md") :

`aws ec2 describe-subnets \ --subnet-ids <your-subnet-ids> \ --query 'Subnets[*].[SubnetId,AvailabilityZoneId]'`

1. **You haven't reached Amazon VPC Lattice service quotas.** Check your account against the [Amazon VPC Lattice quotas](../../../vpc-lattice/latest/ug/quotas.md "../../../vpc-lattice/latest/ug/quotas.md"), especially resource gateway limits.
2. **No IAM policy or SCP is blocking the service-linked role.** The service-managed resource gateway is created through a [service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md "../../../IAM/latest/UserGuide/using-service-linked-roles.md"). If your organization has [service control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") that restrict Amazon VPC Lattice or Amazon EC2 API actions, ensure they permit the service-linked role to create these resources.

If the connection continues to fail after you verify all of these items, contact AWS Support.

## The connection is Active, but capability registration fails with a reachability error

**Symptom**

The private connection reaches the **Active** state, but when you register a capability provider (for example, an MCP server) that uses it, registration fails. For an MCP server, the error message describes how the reachability check failed. You might see one of the following:

- `The MCP server at '<endpoint>' timed out while initializing the session.` (a similar variant refers to listing resources)
- `Unable to connect to the MCP server at <endpoint>. The connection was interrupted. Verify the server is running and accessible, then try again.`
- `Unable to access tools from the MCP server at '<endpoint>' ...`
- `Could not complete request to provider.` (may also appear as an `API error: 504`)

**Cause**

A private connection reaching **Active** confirms that the network path to your VPC is established. It doesn't confirm that your target service is answering on the expected address and port. When you register a capability provider, AWS DevOps Agent validates that the endpoint is reachable and responding, and this is where a misconfigured target surfaces. The message tells you which layer failed:

- A **timed out** message means the connection never reached a listening service. Most often the host address, port, or DNS resolution is wrong, or a security group is blocking the traffic.
- A **connection was interrupted** message means the connection was reset or dropped, typically by a TLS handshake failure or the service closing the connection.
- An **unable to access tools** message means the endpoint responded but rejected the request. This is usually an authorization or provider-side error rather than a network problem.
- A **Could not complete request to provider** message is a general failure to complete the request to your endpoint through the private connection. Review the resolution steps that follow.

**Resolution**

- **Point DNS at the load balancer, not a task or instance IP.** A frequent cause is a DNS record or host address that resolves to a container task or instance IP on an application port (for example, `8100`) instead of the load balancer that terminates TLS on the port you configured (for example, `443`). Confirm the host address resolves to the endpoint that actually serves HTTPS on the target port.
- **Confirm the service serves HTTPS on the configured port.** The target must serve HTTPS with a minimum TLS version of 1.2 on a port included in the connection's port ranges.
- **Check security group rules in both directions.** Verify that the security group attached to the resource gateway ENIs allows outbound traffic on the target port, and that your service's security group allows inbound traffic on that port. Traffic arrives from Amazon VPC Lattice data plane IPs within your VPC CIDR range. You can use security group referencing (allow the ENI security group as a source) or allow inbound from the VPC CIDR. See [Configuring firewall rules for private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").
- **Verify the full certificate chain for a private CA.** If a private certificate authority issued your service's TLS certificate, provide the full PEM-encoded certificate chain when you create the connection. Place the leaf certificate first, then the intermediates, then the root. If the chain is incomplete, the TLS handshake fails even though the network path is up.
- **Confirm the target is running.** Make sure your service is up and accepting connections on the expected port before you complete registration.

## OAuth token exchange can't be reached

**Symptom**

You registered an OAuth-based MCP server (Client Credentials or 3LO) or a remote agent that uses OAuth Client Credentials through a private connection, but token exchange fails even though the MCP server or remote agent endpoint is reachable.

**Cause**

For OAuth-based capability providers, AWS DevOps Agent calls two endpoints: the **target URL** (the MCP server or remote agent endpoint) and the **exchange URL** (the OAuth token exchange endpoint). When you select a single private connection, it applies to _both_ endpoints. If the two endpoints are reachable only through different network paths, a single private connection can't route to both.

**Resolution**

- If both endpoints are reachable through the same path, ensure the private connection's host address can route to both the MCP server or remote agent endpoint and the token exchange endpoint.
- If the endpoints require different network paths, use the per-endpoint fields instead of a single `privateConnectionName`. Set `targetUrlPrivateConnectionName` for the MCP server or remote agent endpoint and `exchangeUrlPrivateConnectionName` for the token exchange endpoint. If you set only one, the other endpoint is reached over the public internet, and it does not fall back to the other private connection. You can't combine the per-endpoint names with `privateConnectionName` in the same request. See [Routing the endpoint and the OAuth token exchange through different private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md").

## Resource gateway or ENIs remain after you delete a connection

**Symptom**

You expected the managed resource gateway and its ENIs to be removed, but they still appear in your VPC. This can incur ENI charges and can block operations that depend on a clean VPC, such as `terraform destroy`.

**Cause**

The managed resource gateway and ENIs are removed only when you delete the private connection through AWS DevOps Agent. The most common reasons they remain are that `DeletePrivateConnection` was never actually called, or that the `AWSAIDevOpsManaged` tag was removed from the managed resources so deletion can't proceed.

###### Important

**AWS DevOps Agent tags the resources it manages (the resource gateway and its ENIs) with `AWSAIDevOpsManaged`. The service-linked role can act only on resources that carry this tag, so** do not remove or modify the `AWSAIDevOpsManaged` tag . If the tag is missing, `DeletePrivateConnection` can't clean up the resources and deletion fails.

**Resolution**

- **Delete the connection through AWS DevOps Agent.** Use the console (**Capability providers** > **Private connections** > **Actions** > **Remove**) or the CLI:

`aws devops-agent delete-private-connection \ --name my-mcp-tool-connection`

The status changes to `DELETE_IN_PROGRESS` while AWS DevOps Agent removes the managed resource gateway and ENIs from your VPC.

- **If deletion fails, confirm the `AWSAIDevOpsManaged` tag is still present.** If the tag was removed from the resource gateway or its ENIs, re-apply it to those resources, then run the deletion again.
- **Don't try to delete the managed resource gateway directly.** The resource gateway is read-only in your account and is fully managed by AWS DevOps Agent, and you can't delete it yourself through Amazon VPC Lattice. Deleting the private connection is what triggers its removal.
- If you deleted the private connection, the tag is present, and the resource gateway or ENIs still remain after deletion completes, contact AWS Support to reconcile the resources.

## Requesting help

If you work through the relevant section for your issue and the problem persists, contact AWS Support. Include your private connection name, its current status, the AWS Region, and the target host address and port so that support can investigate the network path.

## Related topics

- [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md")
- [Configuring firewall rules for private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md "configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md")
- [VPC Endpoints (AWS PrivateLink)](aws-devops-agent-security-vpc-endpoints-aws-privatelink.md "aws-devops-agent-security-vpc-endpoints-aws-privatelink.md")
- [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md "configuring-integrations-and-knowledge-connecting-mcp-servers.md")
- [AWS DevOps Agent Security](aws-devops-agent-security.md "aws-devops-agent-security.md")



# Troubleshooting private connections
<a name="configuring-integrations-and-knowledge-troubleshooting-private-connections"></a>

This page describes common problems you might encounter when creating or using a [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md) for AWS DevOps Agent, and how to resolve them. Each section describes a symptom, the most likely causes, and the steps to fix it.

For an overview of how private connections work, see [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

## A DNS host address doesn't resolve, or traffic reaches the wrong place
<a name="a-dns-host-address-doesnt-resolve-or-traffic-reaches-the-wrong-place"></a>

**Symptom**

You created a private connection using a DNS name for the host address, but the connection can't reach your service. This is most common when your target service is a self-hosted GitLab instance, an internal Application Load Balancer (ALB), or an MCP server whose hostname only exists inside your VPC.

A DNS resolution failure doesn't produce a message that mentions DNS. Instead, it surfaces as a generic reachability or provider error when you register or use the capability provider. For example, you might see `Could not complete request to provider.`, `Unable to connect to the MCP server at <endpoint>. The connection was interrupted.`, or even an authentication error such as `Authentication with provider failed.` Because the message doesn't point to DNS, use the following check to confirm the cause.

**Cause**

By default, a private connection resolves the host address using **public DNS** (`dnsResolution: PUBLIC`). If your hostname only has a record in a [private hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-private.html), an Amazon Route 53 Resolver rule, or an on-premises DNS server, public resolution fails and the connection never reaches your service.

**How to confirm DNS is the cause**
+ Check whether your host address resolves only inside your VPC. From an Amazon EC2 instance or AWS CloudShell session in the same VPC, run `nslookup <your-host-address>`. If it resolves there but not from public DNS, and your private connection uses `dnsResolution: PUBLIC`, DNS resolution is the cause.
+ Test with the IP address instead of the name. Temporarily create a private connection that uses the target's private IP address (or a load balancer IP) for the host address instead of the DNS name. If the connection then reaches your service, the earlier failure was DNS resolution, not the network path or the service itself.

**Resolution**
+ If your hostname resolves only inside your VPC, set the DNS resolution mode to **In VPC** (`IN_VPC`) when you create the connection. In this mode, the host address is resolved from within your VPC context, so private-only hostnames resolve correctly. See [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).
+ The DNS resolution mode is chosen at creation time and applies to the host address you provide. You can't change how the service-managed resource gateway resolves DNS after creation, so choose the correct mode up front. If you selected the wrong mode, delete the connection and recreate it with the correct mode.
+ If you specify an **IP address** (rather than a DNS name) for the host address, the DNS resolution mode has no effect, and traffic goes directly to that IP.
+ If you can't use `IN_VPC` for your setup, you can instead point the host address at the target's private IP address, or at the DNS name of a load balancer that is publicly resolvable but forwards to a private IP.

## The connection is stuck in Create failed
<a name="the-connection-is-stuck-in-create-failed"></a>

**Symptom**

After you create a private connection, the console shows the status as **Connection Failed** (and `describe-private-connection` returns a status of `CREATE_FAILED`).

**Cause**

Create failed most often results from a configuration problem in the request or in your VPC, rather than a service error. When a connection has a failed status, AWS DevOps Agent describes the reason in the `failureMessage` field, so read that field before you work through the checklist.

**Resolution**

Verify the following, in order:

1. **Read `failureMessage` in the connection's details.** This field describes why a connection has a failed status, and is present when the status is `CREATE_FAILED` or `DELETE_FAILED`:

``` aws devops-agent describe-private-connection \ --name my-mcp-tool-connection ```

`failureMessage` also appears in the output of `list-private-connections`. If the field names the cause, act on it. If the field is absent, no reason was returned, so continue with the remaining checks.

1. **Port ranges use a valid format.** Specify each port range as either a single port (for example, `443`) or a genuine range with different start and end ports (for example, `8080-8090`). A "range" whose start and end are the same (for example, `443-443`) is rejected. You can specify up to 11 port ranges.

1. **Your subnets have available IP addresses.** The resource gateway provisions elastic network interfaces (ENIs) in the subnets you specify. If those subnets are exhausted, creation fails. Choose subnets with free address space.

1. **Your subnets are in supported Availability Zones.** Amazon VPC Lattice doesn't support every Availability Zone. Run the following and compare against the unsupported zones listed in [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md) :

``` aws ec2 describe-subnets \ --subnet-ids <your-subnet-ids> \ --query 'Subnets[*].[SubnetId,AvailabilityZoneId]' ```

1. **You haven't reached Amazon VPC Lattice service quotas.** Check your account against the [Amazon VPC Lattice quotas](https://docs.aws.amazon.com/vpc-lattice/latest/ug/quotas.html), especially resource gateway limits.

1. **No IAM policy or SCP is blocking the service-linked role.** The service-managed resource gateway is created through a [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html). If your organization has [service control policies (SCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) that restrict Amazon VPC Lattice or Amazon EC2 API actions, ensure they permit the service-linked role to create these resources.

If the connection continues to fail after you verify all of these items, contact AWS Support.

## The connection is Active, but capability registration fails with a reachability error
<a name="the-connection-is-active-but-capability-registration-fails-with-a-reachability-error"></a>

**Symptom**

The private connection reaches the **Active** state, but when you register a capability provider (for example, an MCP server) that uses it, registration fails. For an MCP server, the error message describes how the reachability check failed. You might see one of the following:
+ `The MCP server at '<endpoint>' timed out while initializing the session.` (a similar variant refers to listing resources)
+ `Unable to connect to the MCP server at <endpoint>. The connection was interrupted. Verify the server is running and accessible, then try again.`
+ `Unable to access tools from the MCP server at '<endpoint>' ...`
+ `Could not complete request to provider.` (may also appear as an `API error: 504`)

**Cause**

A private connection reaching **Active** confirms that the network path to your VPC is established. It doesn't confirm that your target service is answering on the expected address and port. When you register a capability provider, AWS DevOps Agent validates that the endpoint is reachable and responding, and this is where a misconfigured target surfaces. The message tells you which layer failed:
+ A **timed out** message means the connection never reached a listening service. Most often the connection's port ranges don't include the endpoint's port, the host address or DNS resolution is wrong, or a security group is blocking the traffic.
+ A **connection was interrupted** message means the connection was reset or dropped, typically by a TLS handshake failure or the service closing the connection.
+ An **unable to access tools** message means the endpoint responded but rejected the request. This is usually an authorization or provider-side error rather than a network problem.
+ A **Could not complete request to provider** message is a general failure to complete the request to your endpoint through the private connection. Review the resolution steps that follow.

A successful request from an Amazon EC2 instance or AWS CloudShell session in your VPC confirms that the service is reachable from that test environment. It does not confirm that the resource gateway uses the same endpoint URL, port, DNS target, or TLS configuration.

**How to confirm**

1. Repeat the test with the exact endpoint URL that you registered, including its path and any non-default port.

1. Confirm that the endpoint URL's port is included in the private connection's port ranges.

1. Confirm that the private connection's host address resolves to the load balancer or service that terminates TLS on that port, rather than to a task or instance IP on a different application port.

1. Confirm that the target serves HTTPS with TLS 1.2 or later and presents the expected certificate chain.

1. Confirm that the resource gateway security group allows outbound traffic on the target port and that the target security group allows the corresponding inbound traffic.

**Resolution**
+ **Confirm the connection's port ranges include the endpoint's port.** A private connection only forwards traffic on the port ranges you configure when you create it. **If you didn't specify port ranges, the connection allows only port `443`.** The connection drops traffic to any other port without a descriptive error. The dropped traffic surfaces as a timeout, an `Unable to access tools` error, or a `Could not complete request to provider.` error. This commonly affects endpoints on non-standard ports (for example, `https://tools.example.com:8089/mcp`). A successful `curl` from an EC2 instance in the same VPC does **not** rule this out—that test bypasses the private connection entirely. You can't change port ranges after creation. Delete the private connection, recreate it with port ranges that include every port in your endpoint URL, and register the capability provider again.
+ **Confirm the resource gateway can reach your target at all.** This is the first thing to rule out when the target runs in a different AWS account or on premises. In service-managed mode, the resource gateway is created in the VPC and subnets you specified, in the same account as the private connection, so that VPC needs a route to your target. A connection reaching **Active** only means the gateway's network interfaces were created and are healthy; it doesn't mean they can reach your service. Check the connection's mode and the gateway's VPC, then confirm the route:

``` aws devops-agent list-private-connections aws vpc-lattice list-resource-gateways ```

If the gateway's VPC has no route to the target, either add one through VPC peering, AWS Transit Gateway, or a virtual private network (VPN) connection, or move the gateway to the target's account using self-managed mode. See [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).
+ **Point DNS at the load balancer, not a task or instance IP.** A frequent cause is a DNS record or host address that resolves to a container task or instance IP on an application port (for example, `8100`) instead of the load balancer that terminates TLS on the port you configured (for example, `443`). Confirm the host address resolves to the endpoint that actually serves HTTPS on the target port.
+ **Confirm the service serves HTTPS on the configured port.** The target must serve HTTPS with a minimum TLS version of 1.2 on a port included in the connection's port ranges.
+ **Check security group rules in both directions.** Verify that the security group attached to the resource gateway ENIs allows outbound traffic on the target port, and that your service's security group allows inbound traffic on that port. Traffic arrives from Amazon VPC Lattice data plane IPs within your VPC CIDR range. You can use security group referencing (allow the ENI security group as a source) or allow inbound from the VPC CIDR. See [Configuring firewall rules for private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).
+ **Verify the full certificate chain for a private CA.** If a private certificate authority issued your service's TLS certificate, provide the full PEM-encoded certificate chain when you create the connection. Place the leaf certificate first, then the intermediates, then the root. If the chain is incomplete, the TLS handshake fails even though the network path is up. For the error messages this produces, see [The provider's TLS certificate isn't trusted](#the-providers-tls-certificate-isnt-trusted).
+ **Confirm the target is running.** Make sure your service is up and accepting connections on the expected port before you complete registration.

## The provider's TLS certificate isn't trusted
<a name="the-providers-tls-certificate-isnt-trusted"></a>

**Symptom**

Registering or using a capability provider fails with a certificate error. The wording depends on the capability type, but all of these describe the same class of problem:
+ `Could not establish a trusted TLS connection to the provider host: its certificate could not be validated against a publicly trusted certificate authority.`
+ `The server is using a self-signed TLS certificate. Use a certificate from a publicly trusted certificate authority.`
+ `The server's TLS certificate could not be verified. Ensure the full certificate chain is served and issued by a publicly trusted certificate authority.`
+ `The server's TLS certificate has expired. Renew the certificate.`
+ `The server's TLS certificate does not match the endpoint hostname. Ensure the certificate covers the endpoint's domain.`

**Cause**

AWS DevOps Agent couldn't validate the certificate chain that your service presented. The common causes are a certificate issued by a private or internal certificate authority (CA), a chain that's missing its intermediate certificates, an expired certificate in the chain, or a certificate that doesn't cover the hostname in your endpoint URL.

**Note**  
** These messages ask for a certificate from a publicly trusted CA, but a private CA is supported. Supply the chain on the private connection, as described in the resolution steps.

**How to confirm**

From an Amazon EC2 instance or AWS CloudShell session that can reach your target, inspect the chain your service presents on the port you configured, and check which CA signed the top of it:

```
openssl s_client -connect <your-host-address>:<port> -showcerts
```

If an internal CA signed the certificate, supply the chain on the connection. If a public CA signed it, the chain your service sends is probably incomplete.

**Resolution**
+ **For a certificate from a private CA, supply the full chain on the private connection.** Set **Certificate public key** in the console, or the `certificate` field in `create-private-connection`, to the full PEM-encoded chain: the leaf certificate first, then all intermediate CA certificates, then the root. See [Create a private connection](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).
+ **For a certificate from a public CA, send the complete chain.** Configure your service to send the leaf certificate plus all intermediate certificates, not the leaf alone.
+ **Replace any expired certificate in the chain.**
+ **Confirm the certificate covers the hostname in your endpoint URL.**

## OAuth token exchange can't be reached
<a name="oauth-token-exchange-cant-be-reached"></a>

**Symptom**

You registered an OAuth-based MCP server (Client Credentials or 3LO) or a remote agent that uses OAuth Client Credentials through a private connection, but token exchange fails even though the MCP server or remote agent endpoint is reachable.

**Cause**

For OAuth-based capability providers, AWS DevOps Agent calls two endpoints: the **target URL** (the MCP server or remote agent endpoint) and the **exchange URL** (the OAuth token exchange endpoint). When you select a single private connection, it applies to *both* endpoints. If the two endpoints are reachable only through different network paths, a single private connection can't route to both.

**Resolution**
+ If both endpoints are reachable through the same path, ensure the private connection's host address can route to both the MCP server or remote agent endpoint and the token exchange endpoint.
+ If the endpoints require different network paths, use the per-endpoint fields instead of a single `privateConnectionName`. Set `targetUrlPrivateConnectionName` for the MCP server or remote agent endpoint and `exchangeUrlPrivateConnectionName` for the token exchange endpoint. If you set only one, the other endpoint is reached over the public internet, and it does not fall back to the other private connection. You can't combine the per-endpoint names with `privateConnectionName` in the same request. See [Routing the endpoint and the OAuth token exchange through different private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md).

## A private connection can't be deleted while it's in use
<a name="a-private-connection-cant-be-deleted-while-its-in-use"></a>

**Symptom**

Deleting a private connection fails with `Private connection '<name>' is in use by one or more services. Deregister the services first.`

**Cause**

A private connection can't be deleted while a registered capability provider still references it. AWS DevOps Agent refuses the deletion before it removes any resources, so your connection stays in its current state.

**Resolution**

1. Identify the capability providers that use the connection, and either deregister them or update them so they no longer use it.

1. Delete the private connection.

Removing a capability provider from an Agent Space isn't the same as deregistering it. A registration exists at the account level, so remove it from all Agent Spaces and then delete the registration before you delete the connection.

## Resource gateway or ENIs remain after you delete a connection
<a name="resource-gateway-or-enis-remain-after-you-delete-a-connection"></a>

**Symptom**

You expected the managed resource gateway and its ENIs to be removed, but they still appear in your VPC. This can incur ENI charges and can block operations that depend on a clean VPC, such as `terraform destroy`.

**Cause**

The managed resource gateway and ENIs are removed only when you delete the private connection through AWS DevOps Agent. The most common reasons they remain are that `DeletePrivateConnection` was never actually called, or that the `AWSAIDevOpsManaged` tag was removed from the managed resources so deletion can't proceed.

**Important**  
** AWS DevOps Agent tags the resources it manages (the resource gateway and its ENIs) with `AWSAIDevOpsManaged`. The service-linked role can act only on resources that carry this tag, so ** do not remove or modify the `AWSAIDevOpsManaged` tag **. If the tag is missing, `DeletePrivateConnection` can't clean up the resources and deletion fails.

**Resolution**
+ **Delete the connection through AWS DevOps Agent.** Use the console (**Capability providers** > **Private connections** > **Actions** > **Remove**) or the CLI:

``` aws devops-agent delete-private-connection \ --name my-mcp-tool-connection ```

The status changes to `DELETE_IN_PROGRESS` while AWS DevOps Agent removes the managed resource gateway and ENIs from your VPC.
+ **If deletion fails, confirm the `AWSAIDevOpsManaged` tag is still present.** If the tag was removed from the resource gateway or its ENIs, re-apply it to those resources, then run the deletion again.
+ **Don't try to delete the managed resource gateway directly.** The resource gateway is read-only in your account and is fully managed by AWS DevOps Agent, and you can't delete it yourself through Amazon VPC Lattice. Deleting the private connection is what triggers its removal.
+ If you deleted the private connection, the tag is present, and the resource gateway or ENIs still remain after deletion completes, contact AWS Support to reconcile the resources.

## Requesting help
<a name="requesting-help"></a>

If you work through the relevant section for your issue and the problem persists, contact AWS Support. Include your private connection name, its current status, the AWS Region, and the target host address and port so that support can investigate the network path.

## Related topics
<a name="related-topics"></a>
+ [Connecting to privately hosted tools](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md)
+ [Configuring firewall rules for private connections](configuring-integrations-and-knowledge-connecting-to-privately-hosted-tools.md)
+ [VPC Endpoints (AWS PrivateLink)](aws-devops-agent-security-vpc-endpoints-aws-privatelink.md)
+ [Connecting MCP Servers](configuring-integrations-and-knowledge-connecting-mcp-servers.md)
+ [AWS DevOps Agent Security](aws-devops-agent-security.md)
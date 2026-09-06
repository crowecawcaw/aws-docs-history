

# AWS Network Firewall no-source-preservation mode
<a name="nfw-no-source-preservation"></a>

**Note**  
Network Firewall no-source-preservation mode is in public preview and is available only in the US East (Ohio) Region (us-east-2). Features and behavior are subject to change.

AWS Network Firewall supports a no-source-preservation deployment mode where the firewall functions as an explicit forward proxy. In this mode, the firewall attaches to a NAT gateway, terminates client connections, inspects traffic, and re-establishes connections to destinations using the NAT gateway's IP address. This page covers all aspects of deploying and using Network Firewall in no-source-preservation mode.

## Key concepts
<a name="nfw-nosource-concepts"></a>
+ **Deployment mode** – Network Firewall offers two deployment modes: source-preservation and no-source-preservation. In source-preservation deployment, the firewall receives traffic from the VPC endpoint, filters it, and sends it back to the same VPC endpoint. In no-source-preservation deployment, Network Firewall receives traffic from the VPC endpoint, filters it, and then sends the filtered traffic directly to the destination using its own IP address. You can use the no-source-preservation firewall as an explicit proxy. You choose the deployment mode when you create the firewall and cannot change it afterward.
+ **Source-preservation mode** – A deployment mode in which Network Firewall preserves the original source IP address of the traffic it inspects. This is the default mode. Traffic is routed through firewall endpoints using VPC route tables.
+ **No-source-preservation mode** – A deployment mode in which Network Firewall terminates client connections and re-establishes them to the destination using the IP address of an attached NAT gateway. In this mode, the firewall supports both transparent firewall and explicit proxy functionality. Applications connect to the firewall through VPC endpoint associations.
+ **Explicit proxy** – A mode of operation in which Network Firewall receives HTTP CONNECT requests from clients and establishes connections to destinations on behalf of the client. Clients explicitly configure their environment to send traffic to the proxy, rather than the firewall being transparently inserted in the network path. Available only in no-source-preservation mode.
+ **Firewall FQDN** – A fully qualified domain name assigned to a no-source-preservation mode firewall. Clients use this hostname to direct proxy traffic to the firewall. The hostname resolves to the IP address of the local VPC endpoint through automatically created private hosted zones.

## How no-source-preservation mode works
<a name="nfw-nosource-overview"></a>

In no-source-preservation mode, Network Firewall attaches to a NAT gateway and works as an explicit proxy. It comes with a fully qualified domain name (FQDN). After you create a no-source-preservation Network Firewall, you can access it from applications in any VPC by using the `CreateVPCEndpointAssociation` API to deploy VPC endpoints in those VPCs. The application sends a CONNECT request to the no-source-preservation firewall. The firewall terminates the connection, filters it, and re-establishes the filtered connection to the destination using the IP address of the attached NAT gateway.

**Key differences from source-preservation mode**  
The following are the key differences between no-source-preservation mode and the default source-preservation mode.
+ **Fully qualified domain name (FQDN)** – No-source-preservation mode firewalls are assigned a fully qualified domain name that clients use to connect.
+ **Traffic routing** – No route table changes needed; clients use proxy environment variables.
+ **No stateless rules** – The stateless rules engine does not inspect explicit proxy traffic. Proxy traffic (HTTP CONNECT requests) is processed directly by the stateful rules engine.

**Choosing no-source-preservation mode**  
Use no-source-preservation mode when you need the firewall to act as an explicit proxy that terminates and re-establishes connections on behalf of clients, need client authentication at the firewall, or want to simplify routing for HTTP/HTTPS traffic. You cannot change the deployment mode of an existing firewall.

## High-level steps for implementation
<a name="nfw-nosource-high-level-steps"></a>

To create and use an AWS Network Firewall firewall in no-source-preservation mode, you configure the firewall components in the following high-level steps.
+ **Create a firewall policy** – Define the firewall policy by specifying its rule groups. You can create custom rule groups, use AWS managed rule groups, or use partner managed rule groups. For information, see [Firewall policies](firewall-policies.md).
+ **Create a NAT gateway (if one does not exist)** – The firewall attaches to a NAT gateway and uses its IP address to communicate with destinations. If you do not already have a NAT gateway in the VPC and Availability Zone where you want to deploy the firewall, create one. For information about Amazon VPC NAT gateways, see [NAT gateways](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in the *Amazon Virtual Private Cloud User Guide*.
+ **Create the firewall in no-source-preservation mode** – Create a Network Firewall firewall selecting No source preservation as the deployment mode. Attach a NAT gateway (the firewall uses this NAT gateway's IP for egress), and specify a VPC and subnet to deploy the firewall endpoint. Your applications send traffic to the Network Firewall for inspection using this endpoint. You can only create the endpoint in the Availability Zone that your attached NAT gateway resides in. The endpoint subnet must be a different subnet from the NAT gateway subnet. Next, you associate the firewall policy you created in the previous step and optionally configure advanced settings – delete protection, traffic analysis mode, proxy listener ports (defaults to HTTP/3128 and HTTPS/8443), and logging.
+ **Verify the firewall is ready** – After creation, the firewall details page displays the deployment mode, the attached NAT gateway ID, and the status. After the status transitions from PROVISIONING to READY, the proxy FQDN (`DnsName`) appears in the Endpoints and identity section. This is the hostname your applications use to access the proxy. If the status transitions to FAILED, the firewall did not provision successfully. Delete the firewall and create a new one. For more information, see [Troubleshooting firewall endpoint failures](firewall-troubleshooting-endpoint-failures.md).
+ **Configure your workloads to use the proxy** – Point your application's proxy environment variables (for example, `http_proxy`, `https_proxy`) to the firewall's `DnsName` on the configured listener port. An explicit proxy setting does not require any route changes. The applications send traffic to the proxy hostname, which automatically resolves to the firewall endpoint.

After you implement a firewall, you can extend its protections to additional VPCs by creating VPC endpoint associations. Network Firewall automatically creates private hosted zones so the firewall's hostname resolves in the associated VPC.
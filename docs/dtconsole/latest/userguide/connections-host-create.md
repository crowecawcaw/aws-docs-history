# Create a host

You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to create a connection to a third-party
code repository that is installed on your infrastructure. For example, you might have GitHub
Enterprise Server running as a virtual machine on an
Amazon EC2
instance. Before you create a connection to GitHub Enterprise Server, you create a host to
use for the connection.

For an overview of the host creation workflow for installed providers, see [Workflow to create or update a host](welcome-hosts-workflow.md "welcome-hosts-workflow.md").

Before you begin:

- (Optional)
  If
  you want to create your host with a VPC, you must have already
  created a network or virtual private cloud (VPC).
- You must have already created your instance and, if you plan to connect with your
  VPC, launched your
  host
  into your VPC.

###### Note

Each VPC can only be associated with one
host
at a time.
You can optionally
configure your host with a VPC. For more information about network
and VPC
configuration
for your host resource, see
the VPC prerequisites
in [(Optional) Prerequisites: Network or
Amazon VPC configuration for your connection](#connections-create-host-prereq "#connections-create-host-prereq") and [Troubleshooting VPC configuration for
your host](troubleshooting-connections.md#troubleshooting-connections-host-vpc "troubleshooting-connections.md#troubleshooting-connections-host-vpc").

To use the console to create a
host and a
connection to GitHub Enterprise Server, see [Create your GitHub
Enterprise Server connection (console)](connections-create-gheserver-console.md#connections-create-gheserver-connection "connections-create-gheserver-console.md#connections-create-gheserver-connection"). The console creates your host
for you.

To use the console to create a host and a connection to GitLab self-managed, see [Create a connection to GitLab
self-managed](connections-create-gitlab-managed.md "connections-create-gitlab-managed.md"). The console creates your host for
you.

## (Optional) Prerequisites: Network or

Amazon VPC configuration for your connection

If your infrastructure is configured with a network connection, you can skip this
section.

If your host is only accessible in a VPC, follow these VPC requirements before you
continue.

### VPC requirements

You can optionally choose to create your host with a VPC. The following are
general VPC requirements, depending on the VPC you have set up for your
installation.

- You can configure a _public_ VPC with
  public and private subnets. You can use the default VPC for your
  AWS account if you do not have preferred CIDR blocks or subnets.
- If you have a _private_ VPC configured,
  and you have configured your GitHub Enterprise Server instance to perform
  TLS validation using a non-public certificate authority, you need to provide
  the TLS certificate for your host resource.
- When connections creates your host, the VPC endpoint (PrivateLink)
  for webhooks is created for you. For more information, see [AWS CodeConnections and interface VPC endpoints
  (AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").
- Security group configuration:
  - The security groups used during host creation need inbound and
    outbound rules that allow the network interface to connect to your
    GitHub Enterprise Server instance
  - The security groups attached to your GitHub Enterprise Server
    instance (not part of the host setup) need inbound and outbound
    access from the network interfaces created by connections.

- Your VPC subnets must reside in different Availability Zones in your
  Region. Availability Zones are distinct locations that are isolated from
  failures in other Availability Zones. Each subnet must reside entirely
  within one Availability Zone and cannot span zones.

For more information about working with VPCs and subnets, see [VPC and Subnet Sizing for IPv4](../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4 "../../../vpc/latest/userguide/VPC_Subnets.md#vpc-sizing-ipv4") in the _Amazon
VPC User Guide_.

**VPC information you provide for host setup**

When you create your host resource for your connections in the next step, you need
to provide the following:

- **VPC ID:** The ID of the VPC for the server
  where your GitHub Enterprise Server instance is installed or a VPC which has
  access to your installed GitHub Enterprise Server instance through VPN or
  Direct Connect.
- **Subnet ID or IDs:** The ID of the subnet
  for the server where your GitHub Enterprise Server instance is installed or
  a subnet with access to your installed GitHub Enterprise Server instance
  through VPN or Direct Connect.
- **Security group or groups:** The security
  group for the server where your GitHub Enterprise Server instance is
  installed or a security group with access to your installed GitHub
  Enterprise Server instance through VPN or Direct Connect.
- **Endpoint:** Have your server endpoint ready
  and continue to the next step.

For more information, including troubleshooting VPC or host connections, see [Troubleshooting VPC configuration for
your host](troubleshooting-connections.md#troubleshooting-connections-host-vpc "troubleshooting-connections.md#troubleshooting-connections-host-vpc").

### Permission

requirements

As part of the host creation process, AWS CodeConnections creates network resources
on your behalf to facilitate the VPC connectivity. This includes a network interface
for AWS CodeConnections to query data from your host, and a VPC endpoint or
_PrivateLink_ for the host to send event data via webhooks to
connections. To be able to create these network resources, make sure that the
role used for creating the host has the following permissions:

```
ec2:CreateNetworkInterface
ec2:CreateTags
ec2:DescribeDhcpOptions
ec2:DescribeNetworkInterfaces
ec2:DescribeSubnets
ec2:DeleteNetworkInterface
ec2:DescribeVpcs
ec2:CreateVpcEndpoint
ec2:DeleteVpcEndpoints
ec2:DescribeVpcEndpoints
```

For more information about troubleshooting permissions or host connections in a
VPC, see [Troubleshooting VPC configuration for
your host](troubleshooting-connections.md#troubleshooting-connections-host-vpc "troubleshooting-connections.md#troubleshooting-connections-host-vpc").

For more information about the webhook VPC endpoint, see [AWS CodeConnections and interface VPC endpoints
(AWS PrivateLink)](vpc-interface-endpoints.md "vpc-interface-endpoints.md").

###### Topics

- [Create a host for a connection
  (console)](#connections-host-create-console "#connections-host-create-console")
- [Create a
  host for a
  connection (CLI)](#connections-host-create-cli "#connections-host-create-cli")

## Create a host for a connection

(console)

For connections
for
installations, such as with GitHub Enterprise Server or with GitLab
self-managed,
you use a host to represent the endpoint for the infrastructure where your third-party
provider is installed.

###### Note

Beginning July 1, 2024, the console creates connections with `codeconnections` in the resource ARN. Resources with both service prefixes will continue to display in the console.

To learn about considerations for setting up a host in a VPC, see [Create a connection to GitLab
self-managed](connections-create-gitlab-managed.md "connections-create-gitlab-managed.md").

To use the console to create a host and a connection to GitHub Enterprise Server, see
[Create your GitHub
Enterprise Server connection (console)](connections-create-gheserver-console.md#connections-create-gheserver-connection "connections-create-gheserver-console.md#connections-create-gheserver-connection"). The console creates your
host for you.

To use the console to create a host and a connection to GitLab self-managed, see [Create a connection to GitLab
self-managed](connections-create-gitlab-managed.md "connections-create-gitlab-managed.md"). The console creates your host
for you.

###### Note

You only create a host once per GitHub Enterprise Server or GitLab self-managed
account. All of your connections to a specific GitHub Enterprise Server or GitLab
self-managed account will use the same host.

## Create a

host for a
connection (CLI)

You can use the AWS Command Line Interface (AWS CLI) to create a host for installed connections.

###### Note

You only create a host once per GitHub Enterprise Server account. All of your
connections to a specific GitHub Enterprise Server account will use the same
host.

You use a host to represent the endpoint for the infrastructure where your third-party
provider is installed. To create a host with the CLI, you use the
**create-host** command. After you finish creating the host, the host
is in **Pending** status. You then _set
up_ the host to move it to an **Available** status. After
the host is available, you complete the steps to create a connection.

###### Important

A host created through the AWS CLI is in `Pending` status by default.
After you create a host with the CLI, use the console to set up the host to make its
status `Available`.

To use the console to create a host and a connection to GitHub Enterprise Server, see
[Create your GitHub
Enterprise Server connection (console)](connections-create-gheserver-console.md#connections-create-gheserver-connection "connections-create-gheserver-console.md#connections-create-gheserver-connection"). The console creates your
host for you.

To use the console to create a host and a connection to GitLab self-managed, see [Create a connection to GitLab
self-managed](connections-create-gitlab-managed.md "connections-create-gitlab-managed.md"). The console creates your host
for you.

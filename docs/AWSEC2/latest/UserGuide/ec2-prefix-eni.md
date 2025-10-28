# Prefix delegation for Amazon EC2 network interfaces

You can assign a private IPv4 or IPv6 CIDR range, either automatically or manually, to your
network interfaces. By assigning prefixes, you scale and simplify the management of applications,
including container and networking applications that require multiple IP addresses on an
instance. For more information about IPv4 and IPv6 addresses, see [Amazon EC2 instance IP addressing](using-instance-addressing.md "using-instance-addressing.md").

The following assignment options are available:

- **Automatic assignment** — AWS chooses the
  prefix and assigns it to your network interface. If the subnet for the network interface
  has a subnet CIDR reservation of type `prefix`, we select the prefixes from
  the subnet CIDR reservation. Otherwise, we select them from the subnet CIDR range.
- **Manual assignment** — You specify the prefix
  and AWS verifies that it is not already assigned to other resources before assigning
  it to your network interface.
  Assigning prefixes has the following benefits:

- Increased IP addresses on a network interface — When you use a prefix, you
  assign a block of IP addresses as opposed to individual IP addresses. This increases
  the number of IP addresses for a network interface.
- Simplified VPC management for containers — In container applications, each
  container requires a unique IP address. Assigning prefixes to your instance simplifies
  the management of your VPCs, as you can launch and terminate containers without having to
  call Amazon EC2 APIs for individual IP assignments.

###### Contents

- [Basics](ec2-prefix-eni.md#ec2-prefix-basics "ec2-prefix-eni.md#ec2-prefix-basics")
- [Considerations](ec2-prefix-eni.md#prefix-limit "ec2-prefix-eni.md#prefix-limit")
- [Manage prefixes](work-with-prefixes.md "work-with-prefixes.md")
  - [Assign prefixes during network interface creation](work-with-prefixes.md#assign-auto-creation "work-with-prefixes.md#assign-auto-creation")
  - [Assign prefixes to an existing network interface](work-with-prefixes.md#assign-auto-existing "work-with-prefixes.md#assign-auto-existing")
  - [Remove prefixes from your network interfaces](work-with-prefixes.md#unassign-prefix "work-with-prefixes.md#unassign-prefix")

## Basics

- You can assign a prefix to new or existing network interfaces.
- To use prefixes, you assign a prefix to your network interface, attach the
  network interface to your instance, and then configure your operating
  system.
- When you choose the option to specify a prefix, the prefix must meet the following
  requirements:
  - The IPv4 prefix that you can specify is `/28`.
  - The IPv6 prefix that you can specify is `/80`.
  - The prefix is in the subnet CIDR of the network interface, and does
    not overlap with other prefixes or IP addresses assigned to existing
    resources in the subnet.

- You can assign a prefix to the primary or secondary network interface.
- You can assign an Elastic IP address to a network interface that has a prefix assigned to it.
- You can also assign an Elastic IP address to the IP address part of the assigned prefix.
- We resolve the private DNS host name of an instance to the primary private IPv4 address.
- We assign each private IPv4 address for a network interface, including those from prefixes, using the following format:
  - `us-east-1` Region

  ```
  `ip-private-ipv4-address`.ec2.internal
  ```

  - All other Regions

  ```
  `ip-private-ipv4-address`.`region`.compute.internal
  ```

## Considerations

Take the following into consideration when you use prefixes:

- Network interfaces with prefixes are supported with [Nitro-based instances](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").
- Prefixes for network interfaces must use IPv6 addresses or private IPv4
  addresses.
- The maximum number of IP addresses that you can assign to a network interface
  depends on the instance type. Each prefix that you assign to a network interface
  counts as one IP address. For example, a `c5.large` instance has a
  limit of `10` IPv4 addresses per network interface. Each network
  interface for this instance has a primary IPv4 address. If a network interface
  has no secondary IPv4 addresses, you can assign up to 9 prefixes to the network
  interface. For each additional IPv4 address that you assign to a network
  interface, you can assign one less prefix to the network interface. For more
  information, see [Maximum IP addresses per network interface](AvailableIpPerENI.md "AvailableIpPerENI.md").
- Prefixes are included in source/destination checks.
- You must configure your operating system to work with network interfaces with
  prefixes. Note the following:
  - Some Amazon Linux AMIs contain additional scripts installed by AWS, known as
    `ec2-net-utils`. These scripts optionally automate the configuration of your
    network interfaces. They are for use only on Amazon Linux.
  - For containers, you can use a Container Network Interface (CNI) for the
    Kubernetes plug-in, or `dockerd` if you use Docker to manage your
    containers.

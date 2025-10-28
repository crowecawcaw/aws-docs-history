# Monitor CIDR usage by resource

The **Resources** view in Amazon VPC IP Address Manager provides a centralized overview of IP address utilization across your AWS resources. This enables you to quickly identify which resources are consuming IP addresses, track address allocation trends, and optimize your IP address management to align with your evolving infrastructure and business needs.

In IPAM, a resource is an AWS service entity that is assigned an IP address or CIDR
block. IPAM manages some resources, but only monitors other resources, so it's important to understand the difference between the two:

- **Managed resource**: A managed resource has a CIDR
  allocated from an IPAM pool. IPAM monitors the CIDR for potential IP address overlap
  with other CIDRs in the pool, and monitors the CIDR’s compliance with a pool’s
  allocation rules. IPAM supports managing the following type of resources:
  - Elastic IP addresses
  - Public IPv4 pools

  ###### Note

  Public IPv4 pools and IPAM pools are managed by distinct resources in AWS. Public IPv4 pools are single account resources
  that enable you to convert your publicly-owned CIDRs to Elastic IP addresses. IPAM pools can be used to allocate your public space
  to public IPv4 pools.
  - VPCs

- **Monitored resource**: If a resource is monitored by
  IPAM, the resource has been detected by IPAM and you can view details about the
  resource’s CIDR when you use `get-ipam-resource-cidrs` with the AWS CLI, or
  when you view **Resources** in the navigation pane. IPAM supports
  monitoring the following resources:
  - Elastic IP addresses
  - Public IPv4 pools
  - VPCs
  - VPC subnets

AWS Management Console

###### To monitor CIDR usage by resource

1.  Open the IPAM console at
    [https://console.aws.amazon.com/ipam/](https://console.aws.amazon.com/ipam/ "https://console.aws.amazon.com/ipam/").
2.  In the navigation pane, choose **Resources**.
3.  From the IP dropdown menu at the top of the content pane, choose the
    IP address protocol that you want to use: IPv4 or IPv6.
4.  From the scope dropdown menu at the top of the content pane, choose the
    scope that you want to use. For more information about scopes, see [How IPAM works](how-it-works-ipam.md "how-it-works-ipam.md").
5.  Use the resource CIDR map to view available, allocated, and
    overlapping IP address space in a scope:

        * **Available**: An IP address range is available for allocation.
        * **Compliant and nonoverlapping**: An IP address range is
         allocated to a resource managed by IPAM.
        * **Occupied**: An IP address range is allocated to a resource.
        * **Overlapping**: An IP address range has been allocated to
         multiple resources and is overlapping.
        * **Noncompliant**: An IP address
         range is not compliant. There is a resource using the IP address
         range that is not compliant with the allocation rules set up for
         the pool.

    In the CIDR map, choose an IP address block at the bottom of the map
    to view the resources in smaller CIDR blocks. Choose an IP address block
    at the top of the map to view the resources in larger CIDR
    blocks.

6.  In the table, you can view the following details about resources in the scope:
    - **Name (Resource ID)**: The name
      and resource ID of the resource.
    - **CIDR**: The CIDR associated
      with the resource.
    - **Management state**: The state
      of the resource.
      - **Managed**: The resource
        has a CIDR allocated from an IPAM pool and is being
        monitored by IPAM for potential CIDR overlap and
        compliance with pool allocation rules.
      - **Unmanaged**: The
        resource does not have a CIDR allocated from an IPAM
        pool and is not being monitored by IPAM for potential
        CIDR compliance with pool allocation rules. The CIDR is
        monitored for overlap.
      - **Ignored**: The resource
        has been chosen to be exempt from monitoring. Ignored
        resources are not evaluated for overlap or allocation
        rule compliance. When a resource is chosen to be
        ignored, any space allocated to it from an IPAM pool is
        returned to the pool and the resource will not be
        imported again through automatic import (if the
        automatic import allocation rule is set on the
        pool).
      - **-**: This resource is
        not one of the types of resources that IPAM can manage.

    - **Compliance status**: The
      compliance status of the CIDR.
      - **Compliant**: A managed
        resource complies with the allocation rules of the IPAM
        pool.
      - **Noncompliant**: The
        resource CIDR does not comply with one or more of the
        allocation rules of the IPAM pool.

      If a VPC has a CIDR that does not meet the netmask
      length parameters of the IPAM pool, or if the
      resource is not in the same AWS Region as the IPAM
      pool, it will be flagged as noncompliant.
      - **Unmanaged**: The
        resource does not have a CIDR allocated from an IPAM
        pool and is not being monitored by IPAM for potential
        CIDR compliance with pool allocation rules. The CIDR is
        monitored for overlap.
      - **Ignored**: The resource
        has been chosen to be exempt from monitoring. Ignored
        resources are not evaluated for overlap or allocation
        rule compliance. When a resource is chosen to be
        ignored, any space allocated to it from an IPAM pool is
        returned to the pool and the resource will not be
        imported again through automatic import (if the
        automatic import allocation rule is set on the
        pool).
      - **-**: This resource is
        not one of the types of resources that IPAM can manage.

    - **Overlap status**: The overlap
      status of CIDR.
      - **Nonoverlapping**: The
        resource CIDR does not overlap with another CIDR in the
        same scope.
      - **Overlapping**: The
        resource CIDR overlaps with another CIDR in the same
        scope. Note that if a resource CIDR is overlapping, it
        could be overlapping with a manual allocation.
      - **Ignored**: The resource
        has been chosen to be exempt from monitoring. IPAM does
        not evaluate ignored resources for overlap or allocation
        rule compliance. When a resource is chosen to be
        ignored, any space allocated to it from an IPAM pool is
        returned to the pool and the resource will not be
        imported again through automatic import (if the
        automatic import allocation rule is set on the
        pool).
      - **-**: This resource is
        not one of the types of resources that IPAM can manage.

    - **IPs allocated**: For resources
      that are VPCs, this is the percentage of IP address space in the
      VPC that's taken up by subnet CIDRs. For resources that are
      subnets, if the subnet has an IPv4 CIDR provisioned to it, this
      is the percentage of IPv4 address space in the subnet that's in
      use. If the subnet has an IPv6 CIDR provisioned to it, the
      percentage of IPv6 address space in use is not represented. The
      percentage of IPv6 address space in use cannot currently be
      calculated. For resources that are public IPv4 pools, this is
      the percentage of IP address space in the pool that's been
      allocated to Elastic IP addresses (EIPs).
    - **Region**: The AWS Region of
      the resource.
    - **Owner ID**: The AWS account
      ID of the person that created this resource.
    - **Resource type**: Whether the resource is a VPC, subnet, Elastic
      IP address, or public IPv4 pool.
    - **Pool ID**: The ID of the IPAM
      pool that the resource is in.

7.  Use **Filter resources** to filter the resources table by column property, like VPC ID or compliance status.

Command line
The commands in this section link to the _AWS CLI Command Reference_.
The documentation provides detailed descriptions of the options that you can use
when you run the commands.

Use the following AWS CLI commands to monitor CIDR usage by resource:

1. Get the scope ID: [describe-ipam-scopes](../../../cli/latest/reference/ec2/describe-ipam-scopes.md "../../../cli/latest/reference/ec2/describe-ipam-scopes.md")
2. Request resource information: [get-ipam-resource-cidrs](../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md "../../../cli/latest/reference/ec2/get-ipam-resource-cidrs.md")

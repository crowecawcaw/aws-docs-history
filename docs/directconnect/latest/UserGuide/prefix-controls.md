# Inbound prefix controls for Direct Connect

Inbound prefix controls let you manage how many on-premises route prefixes you can
advertise to AWS on your Direct Connect private and transit virtual interfaces (VIFs). Prefix
controls create capacity pools of prefixes at the dedicated connection level and at the
Direct Connect gateway (DXGW) level. With the new controls, you allocate a specific number of
prefixes to a new private or transit VIF, or edit an existing VIF's allocation. You then
attach that VIF to a DXGW or a virtual private gateway (VGW). That VIF then consumes the
value you allocated from the dedicated connection's pool and from the DXGW's pool. This
allows you to have, on the same dedicated connection, for example, a transit VIF with an
allocation of 1,000 prefixes and a private VIF with an allocation of 50 prefixes. If you
don't select any value, AWS applies the default allocation of 100 prefixes per address
family.

The following table summarizes the key limits for inbound prefix controls.

| Limit                                | Value                                                   |
| ------------------------------------ | ------------------------------------------------------- |
| Prefix pool per dedicated connection | 5,000 (1/10 Gbps), 30,000 (100 Gbps), 50,000 (400 Gbps) |
| Maximum allocation per VIF           | 1,000 per address family (IPv4 and IPv6)                |
| Default allocation per VIF           | 100 per address family (IPv4 and IPv6)                  |
| Total allocations per DXGW           | 10,000 (combined IPv4 + IPv6)                           |
| Maximum VIF attachments per DXGW     | 30                                                      |

Public VIFs are not managed by inbound prefix controls. Public VIFs retain the existing
limit of 1,000 inbound prefixes.

## How prefix controls work

Each Direct Connect dedicated connection has a prefix pool — the total number of
inbound route prefixes allowed across all VIFs on that connection. The
pool size depends on the connection speed. In the case of hosted connections, the
underlying physical connections are owned by a partner, so there is no pool that can
be managed by the end customers of the hosted connections. Private and transit VIFs
created on a hosted connection can be allocated a prefix number by the customer, and
that allocation is not counted against a connection's pool.

The following table shows the prefix pool sizes for each connection speed.

| Connection speed | Prefix pool size (IPv4) | Prefix pool size (IPv6) |
| ---------------- | ----------------------- | ----------------------- |
| 1 Gbps           | 5,000                   | 5,000                   |
| 10 Gbps          | 5,000                   | 5,000                   |
| 100 Gbps         | 30,000                  | 30,000                  |
| 400 Gbps         | 50,000                  | 50,000                  |

When you create or update a VIF, you specify how many prefixes to
allocate to that VIF from the connection's pool. The default allocation is 100
prefixes per VIF for each address family (IPv4 and IPv6). You can increase the
allocation up to 1,000 prefixes per VIF for each address
family. To request a higher limit, contact your Solutions Architect (SA) or Technical
Account Manager (TAM). Manual limit increase requests are reviewed on a case-by-case
basis.

The prefix pool tracks the following four states:

Pool size (Allowed)
The total number of prefixes the connection can support. The
connection speed determines this value, and you cannot change it.

Allocated
The number of prefixes reserved on a specific VIF. You set this
value when you create or update a VIF.

Available (Unallocated)
The remaining prefixes in the pool that you haven't allocated to
any VIF. This value equals the pool size minus the sum of all VIF
allocations.

In use
The actual number of prefixes your on-premises router is currently
advertising on a VIF.

###### Important

If the number of prefixes advertised on a VIF exceeds the allocated count, the
BGP session on that VIF will go down and enter an idle state (BGP DOWN). Ensure
that your allocation is at least as large as the number of prefixes you plan to
advertise.

###### Note

You cannot reduce the allocated prefix count for a VIF below the number of
prefixes currently in use. To reduce the allocation, first reduce the number of
prefixes advertised by your on-premises device.

## DXGW prefix limits

Each DXGW has a total prefix pool limit of 10,000 that is shared between all the VIFs
attached to it. This limit adds all IPv4 and IPv6 prefix allocations across all VIFs
attached to the DXGW. The DXGW also maintains the maximum of 30 VIF attachments.
If attaching a new VIF would exceed either the 10,000 prefix allocation limit or the
30 VIF attachment limit, the attachment request is rejected.

Example 1: You attach 10 VIFs with an IPv4 allocation of 1,000. The sum of all the
allocations is 10,000 (10 VIFs x 1,000 IPv4 prefix allocation). The DXGW allows
it.

Example 2: You attach 20 VIFs with an IPv4 allocation of 200 prefixes and an IPv6
allocation of 200 prefixes. The sum of allocations is 8,000 (20 VIFs x [200 IPv4
prefixes + 200 IPv6 prefixes]). The DXGW allows it.

You can view the current total allocation of all VIFs attached to a DXGW using the
console on the gateway details page, or using the
`totalPrefixPoolAllocations` value for a DXGW by using the
`DescribeDirectConnectGateways` CLI/API call.

###### Note

AWS Interconnect connections consume 2,000 prefixes from the 10,000
per-DXGW allocation limit. Account for this when planning prefix allocations
across VIFs on a DXGW with an AWS Interconnect connection attached.

## Link aggregation groups (LAGs)

For LAGs, the prefix pool scales based on the number of billable member
connections. The pool size equals the per-connection pool size multiplied by the
number of active member connections. For 1 Gbps and 10 Gbps LAGs, the pool includes
resources from up to 4 member connections. For 100 Gbps and 400 Gbps LAGs, the pool
includes resources from up to 2 member connections. Unbilled connections are
connections that have been created and added to the LAG but whose Layer 1 connectivity
has not been completed.

Example: You create a LAG with four 10 Gbps connections. The LAG's pool size is
20,000 prefixes each for IPv4 and IPv6 (4 10 Gbps members x 5,000 prefixes, per address
family). You then remove two members from that LAG, reducing the pool to 10,000
prefixes (2 10 Gbps members x 5,000 prefixes, per address family).

### LAG prefix pool guardrail

You cannot remove a LAG member if doing so would reduce the LAG's pool size
below the current total allocated prefixes across all VIFs on the LAG. To remove
the LAG member, first reduce the allocations of the VIFs on that LAG so that the
sum of all the allocations is less than the LAG's pool size will be after you
remove the member connection.

Example: You have a LAG with three 10 Gbps members. That LAG's pool is 15,000
prefixes per address family (3 10 Gbps members x 5,000, per family). You have 15
VIFs on that LAG with IPv4 allocations of 1,000 each, totaling 15,000 prefixes.
Removing a member of the LAG would take its pool down to 10,000 per address family,
which is less than the 15,000 prefixes you have allocated on IPv4. The system
rejects the removal. You then reduce the IPv4 allocations of the 15 VIFs to 500.
The sum of allocations across all VIFs on that LAG is now 7,500 prefixes (15 x
500). The system now allows the removal of the LAG member, because the new pool
size (10,000) is greater than the sum of allocations across all VIFs on the LAG
(7,500).

## Hosted connections

Hosted connections support a single VIF, so the connection-level
prefix pool is not used. You can set the per-VIF prefix allocation on a hosted
connection. The default allocation is 100 for each address family (IPv4 and IPv6),
and you can increase it up to 1,000 using the
`CreatePrivateVirtualInterface` or
`UpdateVirtualInterfaceAttributes` API.

Connection-level prefix pool information (pool size and unallocated count) is not
displayed in the console for hosted connections.

## Additional resources

For more information, see the following resources:

- [Managing prefix allocations](prefix-allocations.md "prefix-allocations.md")
- [Direct Connect quotas](limits.md "limits.md")
- [Direct Connect gateways](direct-connect-gateways-intro.md "direct-connect-gateways-intro.md")

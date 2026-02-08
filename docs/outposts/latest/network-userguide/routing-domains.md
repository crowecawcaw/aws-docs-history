# Multiple local gateway routing domains

Multiple local gateway (LGW) routing domains is a feature available on second-generation AWS Outposts racks that enables you to create up to 10 isolated routing domains with independent network paths to your on-premises network. This capability enables both customer-owned IP (CoIP) and direct VPC routing (DVR) configurations to coexist on the same Outpost, with each routing domain configured independently for either CoIP or DVR mode.

A Virtual Interface (VIF) represents a network interface connecting your Outpost to your on-premises network. VIFs are grouped into VIF Groups, which are then associated with route tables to create routing domains. An LGW routing domain is the association of an LGW Route Table and LGW VIF Group. Each LGW routing domain operates as an independent network segment with its own route table, VIF Group, associated VPCs, and VLAN configurations.

###### Note

Multiple LGW routing domains feature is not available on first-generation AWS Outposts racks.

## Traffic isolation with routing domains

IP address ranges must not overlap within a routing domain to prevent routing conflicts. Multiple on-premises VLANs can be configured within a single domain. Traffic isolation across routing domains works through multiple layers of separation:

- **Logical level** – Each routing domain maintains its own BGP sessions and independent route tables. VPCs are exclusively associated with one LGW routing domain per Outpost, preventing unintended cross-domain communication. This association is agnostic of the routing domain mode (DVR or CoIP).
- **Data plane level** – Traffic remains confined within assigned `VLAN`s and VIFs, ensuring complete isolation.

Each VIF within a VIF Group requires specific configuration including:

- IP addresses for local and peer endpoints
- `VLAN` tags for traffic segregation
- BGP parameters for route exchange
- Association with the appropriate Link Aggregation Group (LAG)

## Creating routing domains

You can create and manage routing domains through the AWS Management Console or AWS CLI.

To create a routing domain:

1. **Create an LGW route table**

Create an LGW route table in DVR or CoIP routing mode, and associate your VPC with it.

The route table will show as inactive until both a VPC and VIF group are associated. A VPC can be associated with 1 LGW route table per Outpost. 2. **Create a VIF group**

Create a VIF group for your routing domain.

Every LGW routing domain requires a unique VIF group and LGW route table for network traffic isolation. Second-generation Outposts racks require 4 VIFs per VIF group. Each VIF maps to: 1 VLAN → 1 LAG. VIF group and individual VIF status will show as "Pending" for up to 10 minutes. 3. **Configure each VIF**

Configure each VIF within the group with the required network parameters.

Assign each VIF:

    * IP addresses
    * VLAN tags (can be unique or the same as existing VLANs, as long as there's no VIF IP conflict on that LAG)
    * BGP parameters
    * LAG assignment

4. **Create the routing domain**

Create the LGW routing domain by associating the route table and VIF group.

Your VIF group and route table can only be associated to 1 routing domain. This creates the 1:1 mapping between the VIF group and route table. 5. **Add a route to the VIF group**

Add a route in the LGW route table that directs traffic to the VIF group.

This route enables traffic to flow from your Outpost through the local gateway to your on-premises network via the VIF group. Without this route, the routing domain will not forward traffic even though the VIF group and route table are associated. 6. **Update your Customer Networking Devices (CNDs)**

Update your Customer Networking Devices (CNDs) to allow the VIF VLANs to send traffic across the physical uplinks that correspond to each LAG.

**Note:** This step requires configuration on your on-premises CNDs. Each VLAN must be configured as a trunk port on the physical interface(s) that connect to the Outpost Networking Devices (ONDs) to complete BGP peering setup. Consult your network equipment documentation for VLAN trunking configuration specific to your hardware.

## Monitoring routing domains

You can monitor the following:

- VIF status and connectivity
- BGP session health
- Route propagation
- Traffic flow through each routing domain

## Best practices and considerations

### Network planning

- Maintain non-overlapping IP ranges between routing domains.
- Plan for sufficient VIFs per VIF group based on your configuration.
- Verify VIF requirements based on your Outpost generation and rack configuration.

### Documentation and organization

- Use clear naming conventions for VIF groups and routing domains.
- Tag LAG IDs for easier identification.
- Review service link VIF information to select appropriate LAG IDs.

## Configuration restrictions

### Routing domains

- Each VIF Group can be associated with only one routing domain at a time.
- To associate a VIF Group with a different routing domain, you must first delete the existing LGW Route Table and routing domain association.
- Each routing domain must be configured for either CoIP or DVR mode during LGW Route Table creation.

### IP addressing

- Local addresses cannot overlap with peer and local addresses of any local gateway VIF or service link VIF on the same LAG.
- Local addresses cannot overlap with peer and local addresses of any local gateway VIF in the same VIF group.

### VLAN configuration

- `VLAN` IDs cannot overlap with service link VIF on the same LAG.
- `VLAN` IDs can overlap with other local gateway VIFs on the same VIF group/LAG.

### BGP

- Local BGP ASN matches the BGP for the VIF group.
- Peer BGP ASN has no overlapping prevention.

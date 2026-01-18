# Multiple local gateway routing domains

Multiple local gateway (LGW) routing domains is a feature available on second-generation AWS Outposts racks that enables you to create up to 10 isolated routing domains with independent network paths to your on-premises network. This capability enables both customer-owned IP (CoIP) and direct VPC routing (DVR) configurations to coexist on the same Outpost, with each routing domain configured independently for either CoIP or DVR mode.

A Virtual Interface (VIF) represents a network interface connecting your Outpost to your on-premises network. VIFs are grouped into VIF Groups, which are then associated with route tables to create routing domains. An LGW routing domain is the association of an LGW Route Table and LGW VIF Group. Each LGW routing domain operates as an independent network segment with its own route table, VIF Group, associated VPCs, and VLAN configurations.

###### Note

Multiple LGW routing domains feature is not available on first-generation AWS Outposts racks.

## Traffic isolation with routing domains

IP address ranges must not overlap within a routing domain to prevent routing conflicts. Multiple on-premises VLANs can be configured within a single domain. Traffic isolation across routing domains works through multiple layers of separation:

- **Logical level** – Each routing domain maintains its own BGP sessions and independent route tables. VPCs are exclusively associated with one routing domain, preventing unintended cross-domain communication.
- **Data plane level** – Traffic remains confined within assigned `VLAN`s and VIFs, ensuring complete isolation.

Each VIF within a VIF Group requires specific configuration including:

- IP addresses for local and peer endpoints
- `VLAN` tags for traffic segregation
- BGP parameters for route exchange
- Association with the appropriate Link Aggregation Group (LAG)

## Creating routing domains

You can create and manage routing domains through the AWS Management Console or AWS CLI.

To create a routing domain:

1. Create a LGW VIF Group.
2. Retrieve your LAG-ID information.
3. Create and configure the required LGW VIFs within the group, assigning each to the appropriate LAG with IP addresses, `VLAN` tags, and BGP parameters.
4. Create a LGW Route Table and specify either CoIP or DVR mode for the routing domain.
5. Associate the route table with the VIF Group.
6. Attach VPCs to the routing domain.

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

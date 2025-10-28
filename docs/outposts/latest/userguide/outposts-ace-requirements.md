# Site requirements for Outpost ACE racks

###### Note

Applies only if you need an ACE rack.

An Aggregation, Core, Edge (ACE) rack acts as a network aggregation point for multi-rack
Outpost deployments. You must install an ACE rack if you have four or more compute racks. If you
have less than four compute racks but plan to expand to four or more racks in the future, we
recommend that you install an ACE rack.

To install an ACE rack, you must meet the requirements in this section in addition to the
requirements listed in [Site requirements for Outposts racks](outposts-requirements.md "outposts-requirements.md").

###### Note

ACE racks are not fully enclosed and don't include a front door or a rear door.

## Facility

These are the facility requirements for an ACE rack.

- Power – All ACE racks are shipped with 10kVA single
  phase (AA+BB; IEC60309 or L6-30P Whip connector types).
- Weight support – The ACE rack weighs 705 lbs (320
  kg).
- Clearance/Size dimension – The ACE rack is 80 inches
  (203 cm) high, 24 inches (61 cm) wide, and 42 inches (107 cm) deep.

If the ACE rack has cable management arms, then the rack's width is 36 inches (91.5 cm).

## Networking

These are the networking requirements for an ACE rack. To understand how the ACE rack
connects the Outposts networking devices, your on-premises networking devices, and your Outposts racks,
see [ACE rack connectivity](local-rack.md#ace-rack-connectivity "local-rack.md#ace-rack-connectivity").

- Rack network requirements – Ensure that you meet the
  requirements listed in the [Network readiness checklist](outposts-requirements.md#checklist "outposts-requirements.md#checklist") and [Local network connectivity for Outposts racks](local-rack.md "local-rack.md") sections except for the following
  changes:
  - The ACE rack has four networking devices that connect to the upstream devices, not two
    as in the case of a single Outposts rack.
  - ACE racks do not support 1 Gbps uplinks.

- Uplink speed – Provide uplinks with speeds of 10
  Gbps, 40 Gbps, or 100 Gbps. For bandwidth recommendations for the service link connection,
  [Service link bandwidth
  recommendations](service-links.md#sl-bandwidth-recommendations "service-links.md#sl-bandwidth-recommendations").

###### Important

ACE racks do not support 1 Gbps uplinks.

- Fiber – Provide single-mode fiber (SMF) with Lucent
  Connector (LC), or multi-mode fiber (MMF) with Lucent Connector (LC). For the full list of
  supported fiber types and optical standards, see [Uplink speed, ports, and fiber](outposts-requirements.md#uplink-ports-fiber "outposts-requirements.md#uplink-ports-fiber").
- Upstream device – Provide two or four upstream
  devices, which can be switches or routers.
- Service VLAN and a Local Gateway VLAN – For each of
  the four ACE networking device you must provide a Service VLAN and a different Local Gateway
  VLAN. You can choose to provide only two distinct VLANs, one for the Service VLAN and one for
  the Local gateway VLAN, or have different VLANs in each ACE networking device for both Service
  VLAN and LGW VLAN for a total of 8 different VLANs. For more information on how link
  aggregation groups (LAGs) and VLAN are used, see [Link aggregation](local-rack.md#link-aggregation "local-rack.md#link-aggregation") and [Virtual LANs](local-rack.md#vlans "local-rack.md#vlans").
- CIDR and IP address for the service link and local gateway
  VLANs – We recommend allocating a dedicated subnet for each ACE networking
  device with a /30 or /31 CIDR. Alternatively, it is possible to allocate a single /29 subnet in
  each Service and Local Gateway VLAN. In both cases, you must specify the IP addresses for the
  ACE networking devices to use. For more information, see [Network layer connectivity](local-rack.md#network-layer-connectivity "local-rack.md#network-layer-connectivity").
- Customer and Outpost BGP Autonomous System Number (ASN) for service
  link VLAN and a Local Gateway VLAN – The Outpost establishes an external BGP
  (eBGP) peering session between each ACE rack device and your local network device for service
  link connectivity over the service link VLAN. In addition, it establishes an eBGP peering
  session from each ACE networking device to a local network device for connectivity from your
  local network to the local gateway. For more information, see [Service link BGP connectivity](local-rack.md#service-link-bgp-connectivity "local-rack.md#service-link-bgp-connectivity") and
  [Local gateway BGP connectivity](local-rack.md#local-gateway-bgp-connectivity "local-rack.md#local-gateway-bgp-connectivity").

###### Important

Service link infrastructure subnets – A service link
infrastructure subnet (must be /26) is required for each compute rack included in your Outposts
installation.

## Power

These are the power requirements for an ACE rack.

| Requirement                                 | Specification                                                                                                   |
| ------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| **AC line voltage**                         | Single-phase 200 to 240 VAC; 50 or 60 Hz                                                                        |
| **Power consumption**                       | 10 kVA single phase (AA+BB)                                                                                     |
| **AC protection (upstream power breakers)** | For 2N input (redundant) only: C-curve, D-curve, or K-curve circuit breaker. B-curve or lower is not supported. |
| **AC inlet type (receptacle)**              | IEC60309 or L6-30P whip connector types.                                                                        |

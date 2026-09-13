

# Site requirements for second-generation Outposts racks (single-rack configuration)
<a name="outposts-rack2ndgen-requirements-single-rack"></a>

AWS Outposts sites are available in select countries and territories.

The single-rack configuration is a single, self-contained 42U rack that integrates AWS managed compute, storage, and networking. It does not use a separate network rack and cannot be expanded by adding racks (no scale-out). You can add capacity within the rack (scale-up). For the multi-rack configuration, which uses one or more compute racks with a dedicated network rack, see [Site requirements for second-generation Outposts racks (multi-rack configuration)](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-requirements.html).

**Topics**
+ [Facility](#facility-single-rack)
+ [Networking](#networking-single-rack)
+ [Network readiness checklist](#network-readiness-checklist-single-rack)
+ [Power](#power-single-rack)
+ [Order fulfillment](#order-fulfillment-single-rack)

## Facility
<a name="facility-single-rack"></a>

The following are the facility requirements for the single-rack configuration.
+ **Temperature and humidity** – The ambient temperature must be between 41° F (5° C) and 95° F (35° C). The relative humidity must be between 8 percent and 80 percent with no condensation.
+ **Airflow** – Racks draw cold air from the front aisle and exhaust hot air to the back aisle. The rack position must provide at least 145.8 times the kVA of cubic feet per minute (CFM) airflow.
+ **Loading dock** – Your loading dock must accommodate a rack crate that is 94 inches (239 cm) high by 54 inches (138 cm) wide by 51 inches (130 cm) deep.
+ **Weight support** – Weight varies by configuration. You can find the weight for your configuration specified in the order summary at the rack point loads. The location where the rack is installed and the path to that location must support the specified weight. This includes any freight and standard elevators along the path.
+ **Clearance** – The rack is 80 inches (203 cm) high by 24 inches (61 cm) wide by 48 inches (122 cm) deep. Any doorways, hallways, turns, ramps, and elevators must provide sufficient clearance. At the final resting position, there must be a 24 inch (61 cm) wide by 48 inch (122 cm) deep area for the Outpost. Allow an additional 48 inches (122 cm) of front clearance and 24 inches (61 cm) of rear clearance. The total minimum area required for the Outpost is 24 inch (61 cm) wide by 10 feet (305 cm) deep.

  The following diagram shows the total minimum area required for the single-rack Outpost, including clearance.  
![Diagram of the single-rack Outpost clearance area and required front and rear clearance.](https://docs.aws.amazon.com/outposts/latest/network-userguide/images/outpost-rack2ndgen-compute-rack-clearance.png)
+ **Seismic bracing** – To the extent required by regulation or code, you must install and maintain appropriate seismic anchorage and bracing for the rack while it is in your facility. We provide floor brackets that offer protection for up to 2.0G of seismic activity with all Outposts racks.
+ **Bonding point** – We recommend that you provide a bonding wire or point at the rack position so that your electrician can bond the racks during installation. The AWS-certified technician validates the bonding.
+ **Facility access** – Do not change the facility in a way that negatively affects the ability of AWS to access, service, or remove the Outpost.
+ **Elevation** – The elevation of the room where the rack is installed must be below 10,005 feet (3,050 meters).

## Networking
<a name="networking-single-rack"></a>

In the single-rack configuration, networking is integrated into the rack. There is no separate network rack and no aggregation layer. With the single-rack configuration, you connect your local network to two Outpost network devices.
+ **Uplink speed** – Provide uplinks with speeds of 10 Gbps, 40 Gbps, or 100 Gbps. For bandwidth recommendations for the service link connection, see [Service link bandwidth recommendations](https://docs.aws.amazon.com/outposts/latest/network-userguide/service-links.html#sl-bandwidth-recommendations).
+ **Fiber** – Provide either single-mode fiber (SMF) with Lucent Connector (LC), multimode fiber (MMF), or MMF OM4 with LC.
+ **Upstream device** – Provide a minimum of two upstream devices, which can be switches or routers. Connect each upstream device to both Outpost network devices. With two Outpost network devices and two upstream devices, there are four link aggregation groups (LAGs) total, two per Outpost network device.

With the single-rack configuration, you get up to 100 Gbps of local gateway (LGW) bandwidth. If one networking device is impaired, the remaining device continues to operate with reduced LGW bandwidth.

## Network readiness checklist
<a name="network-readiness-checklist-single-rack"></a>

Use this checklist to gather the information for your Outpost configuration. This includes the LAN, WAN, and any devices between the Outpost and local traffic destinations, and the destination in the AWS Region.

The following requirements are for the single-rack configuration:
+ Provide uplinks with speeds of 10 Gbps, 40 Gbps, or 100 Gbps.
+ Provide either single-mode fiber (SMF) with Lucent Connector (LC), multimode fiber (MMF), or MMF OM4 with LC.
+ Provide a minimum of two upstream devices, which can be switches or routers, and connect each upstream device to both Outpost network devices (four LAGs total).

### Physical connectivity
<a name="physical-connectivity-single-rack"></a>

An Outpost in the single-rack configuration has two Outpost network devices that attach to your local network.

For the number of uplinks each LAG supports, based on uplink speed, see [Uplink speed, ports, and fiber](#uplink-ports-fiber-single-rack).

Each Outpost network device connects to both of your upstream devices, using a separate LAG to each. With two Outpost network devices and two upstream devices, there are four LAGs total.

The uplink speed and quantity are symmetrical on each Outpost network device. If you use 100 Gbps as the uplink speed, you must configure the link with forward error correction (FEC CL91).

Provide either a single-mode fiber (SMF) with Lucent Connector (LC), multimode fiber (MMF), or MMF OM4 with LC. We provide the optics that are compatible with the fiber that you provide at the rack position.

The physical demarcation is the fiber patch panel in the Outpost. You provide the fiber cables that are required to connect the Outpost to the patch panel.

### Uplink speed, ports, and fiber
<a name="uplink-ports-fiber-single-rack"></a>

**Uplink speed and ports**  
An Outpost in the single-rack configuration has two Outpost network devices that attach to your local network. The number of uplinks each LAG can support depends on your bandwidth needs and what your router can support.

The following list shows how many uplink ports are supported for each LAG, based on the uplink speed.

**10 Gbps**  
1, 2, 4, 8, 12, or 16 uplinks

**40 Gbps or 100 Gbps**  
1, 2, or 4 uplinks

#### Fiber
<a name="networking-fiber-single-rack"></a>

AWS Outposts requires fibers with Lucent Connectors (LC).

The following table lists the supported optical standards and the corresponding fiber type required. If the optical standard uses the Multi-fiber Push-On (MPO) connector, you need an MPO to 4 x LC Type-B breakout cable where the 4 x LC connectors attach to the Outpost to establish one link.


| Uplink speed | Optical standard | Fiber type | 
| --- | --- | --- | 
| 10 Gbps | – 10GBASE-IR<br />– 10GBASE-LR | SMF (LC) | 
| 10 Gbps | – 10GBASE-SR | MMF (LC) | 
| 40 Gbps | – 40GBASE-IR4 (LR4L)<br />– 40GBASE-LR4 | SMF (LC) | 
| 40 Gbps | – 40GBASE-ESR4<br />– 40GBASE-SR4 | MMF (MPO to 4 x LC Type-B breakout) | 
| 100 Gbps | – 100GBASE-CWDM4<br />– 100GBASE-LR4 | SMF (LC) | 
| 100 Gbps | – 100G PSM4 MSA | SMF (MPO to 4 x LC Type-B breakout) | 
| 100 Gbps | – 100GBASE-SR4 | MMF (MPO to 4 x LC Type-B breakout) | 

### Outpost link aggregation and VLANs
<a name="lacp-vlan-single-rack"></a>

Link aggregation control protocol (LACP) is required between the Outpost and your network. You must use dynamic LAG with LACP.

The following VLANs are required for each LAG. With two Outpost network devices and two upstream devices, there are four LAGs (two per Outpost network device), each with a service link VLAN and a local gateway VLAN. For more information, see [Virtual LANs](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#vlans).


| LAG | Service link VLAN | Local gateway VLAN | 
| --- | --- | --- | 
| Outpost network device 1 to upstream device 1 | Valid values: 1-4094 | Valid values: 1-4094 | 
| Outpost network device 1 to upstream device 2 | Valid values: 1-4094 | Valid values: 1-4094 | 
| Outpost network device 2 to upstream device 1 | Valid values: 1-4094 | Valid values: 1-4094 | 
| Outpost network device 2 to upstream device 2 | Valid values: 1-4094 | Valid values: 1-4094 | 

For each Outpost network device, you can choose whether to use the same VLANs or different VLANs for the service link and local gateway. However, we recommend that each Outpost network device have a different VLAN from the other Outpost network device. For more information, see [Link aggregation](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#link-aggregation) and [Virtual LANs](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#vlans).

We also recommend redundant layer 2 connectivity. LACP is used for link aggregation and is not used for high availability. You cannot span a single LAG across both Outpost network devices (no MLAG or vPC). Each LAG terminates on one Outpost network device and one upstream device.

### Outpost network device IP connectivity
<a name="outpost-device-network-connectivity-single-rack"></a>

Each LAG requires a CIDR and IP address for the service link and local gateway VLANs. With four LAGs, you provide four service link interfaces and four local gateway interfaces. We recommend allocating a dedicated subnet for each network device. Specify a subnet and an IP address from the subnet for the Outpost to use. For more information, see [Network layer connectivity](https://docs.aws.amazon.com/outposts/latest/network-userguide/outposts-rack2ndgen-local-rack.html#network-layer-connectivity).


| LAG | Service link interface requirements | Local gateway interface requirements | 
| --- | --- | --- | 
| Outpost network device 1 to upstream device 1 | – Service link CIDR (/31)<br />– Service link IP address | – Local gateway CIDR (/31)<br />– Local gateway IP address | 
| Outpost network device 1 to upstream device 2 | – Service link CIDR (/31)<br />– Service link IP address | – Local gateway CIDR (/31)<br />– Local gateway IP address | 
| Outpost network device 2 to upstream device 1 | – Service link CIDR (/31)<br />– Service link IP address | – Local gateway CIDR (/31)<br />– Local gateway IP address | 
| Outpost network device 2 to upstream device 2 | – Service link CIDR (/31)<br />– Service link IP address | – Local gateway CIDR (/31)<br />– Local gateway IP address | 

### Service link maximum transmission unit (MTU)
<a name="service-link-mtu-single-rack"></a>

The network must support a 1500-byte MTU between the Outpost and the service link endpoints in the parent AWS Region. For more information about the service link, see [AWS Outposts connectivity to AWS Regions](region-connectivity.md).

### Service link Border Gateway Protocol
<a name="service-link-bgp-single-rack"></a>

The Outpost establishes an external BGP (eBGP) peering session between each Outpost network device and your local network device for service link connectivity over the service link VLAN. For more information, see [Service link BGP connectivity](outposts-rack2ndgen-local-rack.md#service-link-bgp-connectivity).


| Outpost | Service link BGP requirements | 
| --- | --- | 
| Your Outpost | – Outpost BGP Autonomous System Number (ASN). 2-byte (16-bit) or 4-byte (32-bit). From your private ASN range (64512-65534 or 4200000000-4294967294).<br />– Must be the same ASN for both Outpost network devices<br />– Infrastructure CIDR (/31 required) | 


| LAG | Service link BGP requirements | 
| --- | --- | 
| Outpost network device 1 to upstream device 1 | – Service link BGP peer IP address.<br />– Service link BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 1 to upstream device 2 | – Service link BGP peer IP address.<br />– Service link BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 2 to upstream device 1 | – Service link BGP peer IP address.<br />– Service link BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 2 to upstream device 2 | – Service link BGP peer IP address.<br />– Service link BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 

### Service link firewall
<a name="service-link-firewall-single-rack"></a>

You must statefully list UDP and TCP 443 in the firewall.


| Protocol | Source port | Source address | Destination port | Destination address | 
| --- | --- | --- | --- | --- | 
| UDP | 443 | Outpost service link /26 | 443 | Outpost Region's public routes | 
| TCP | 1025-65535 | Outpost service link /26 | 443 | Outpost Region's public routes | 

You can use an Direct Connect connection or a public internet connection to connect the Outpost back to the AWS Region. For Outpost service link connectivity, you can use NAT or PAT (Port Address Translation) at your firewall or edge router. The Outpost always initiates service link establishment.

### Local gateway Border Gateway Protocol
<a name="local-gateway-bgp-single-rack"></a>

The Outpost establishes an eBGP peering session from each Outpost network device to a local network device for connectivity from your local network to the local gateway. For more information, see [Local gateway BGP connectivity](outposts-rack2ndgen-local-rack.md#local-gateway-bgp-connectivity).


| Outpost | Local gateway BGP requirements | 
| --- | --- | 
| Your Outpost | – Outpost BGP Autonomous System Number (ASN). 2-byte (16-bit) or 4-byte (32-bit). From your private ASN range (64512-65534 or 4200000000-4294967294). | 


| LAG | Local gateway BGP requirements | 
| --- | --- | 
| Outpost network device 1 to upstream device 1 | – Local gateway BGP peer IP address.<br />– Local gateway BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 1 to upstream device 2 | – Local gateway BGP peer IP address.<br />– Local gateway BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 2 to upstream device 1 | – Local gateway BGP peer IP address.<br />– Local gateway BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 
| Outpost network device 2 to upstream device 2 | – Local gateway BGP peer IP address.<br />– Local gateway BGP peer ASN. 2-byte (16-bit) or 4-byte (32-bit). | 

## Power
<a name="power-single-rack"></a>

The power shelf supports three power configurations: 10 kVA, 15 kVA, or 30 kVA. Because compute, storage, and networking share one rack, a single power configuration covers the entire Outpost. There is no separate network-rack power draw.

The following table lists the power requirements for the single-rack configuration.


| Requirement | Specification | 
| --- | --- | 
| **AC line voltage** | **Single-phase** 208 to 277 VAC; 50 or 60 Hz<br />**Three-phase**:+  208 to 250 VAC (Delta); 50 to 60 Hz <br />+  346 to 480 VAC (Wye); 50 to 60 Hz  | 
| **Power consumption** | 10 kVA, 15 kVA (13 kW), or 30 kVA (26 kW) | 
| **AC protection (upstream power breakers)** | 30 A, 32 A, or 50 A | 
| **AC inlet type (receptacle)** | Single phase L6-30P (30A) or IEC309 P\+N\+E, 6 hour (32 A), three phase AH530P7W 3P\+N\+E, 7 hour (30A), or three phase AH532P6W 3P\+N\+E 6 hour (32 A), or three phase Non-NEMA twistlock Hubbell CS8365C, 3P\+E, center ground (50A) | 
| **Whip length** | 10.25 ft (3 m) | 
| **Whip - Rack cabling input** | From above or below the rack | 

AC line voltage, breaker, receptacle, whip, and cabling specifications follow the same requirements as other Outposts racks.

If the AC whips that we provide as previously described must be fitted with an alternate power plug, consider the following:
+ Only a certified customer-provided electrician should modify the AC whip to fit a new plug type.
+ The installation must comply with all applicable national, state, and local safety requirements. Have it inspected as required for electrical safety.
+ You must notify your AWS representative of modifications to the AC whip plug. Upon request, you must provide information about the modifications to AWS. You must also include any safety inspection records issued by the authority having jurisdiction. We require this documentation to validate the safety of the installation before AWS employees perform work on the equipment.

## Order fulfillment
<a name="order-fulfillment-single-rack"></a>

To fulfill the order, we schedule a date and time with you. You also receive a checklist of items to verify or provide before the installation.

Our installation team arrives at your site at the scheduled date and time. They place the rack at the identified position. You and your electrician are responsible for performing the electrical connection and installation to the rack.

A certified electrician must perform all electrical installations and any changes to those installations. The work must comply with all applicable laws, codes, and best practices. Before you make any changes to the Outpost hardware or electrical installations, get written approval from us. You must provide us with documentation verifying compliance and the safety of any changes. We are not responsible for risks from the Outpost electrical installation, facility electrical wiring, or any changes to either. You must not make any other changes to the Outposts hardware.

The team establishes network connectivity for the rack over the uplink that you provide and configures the rack capacity.

The installation is complete when you confirm that the Amazon EC2 and Amazon EBS capacity for your rack is available from your AWS account.

You cannot scale out the single-rack configuration. During the ordering process, you acknowledge that the deployment is limited to a single rack. To add capacity later, you scale up within the rack rather than adding racks.
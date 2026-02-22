# AWS Cloud WAN Routing policies

Cloud WAN Routing Policies provide customers fine-grained routing controls to optimize route management and customize network routing behavior per their individual needs. A routing policy is a set of rules that gives you precise control over route propagations in your core network allowing you flexible routes management, optimized performance and greater security by controlling your routing and reachability in your global network. Using this feature, customers can perform advanced routing techniques such as route filtering and summarization to have better control on routes exchanged across Cloud WAN and your external networks connected to Cloud WAN.

This feature allows customers to set advanced Border Gateway Protocol (BGP) attributes to customize network traffic behavior per their individual needs and build highly resilient hybrid-cloud network architectures with multiple connectivity paths to AWS. Furthermore, this feature also provides enhanced visibility into the routing databases to allow rapid troubleshooting of network issues in complex multi-path environments.

## Key use-cases

### Controlled routing environments

While customers benefit from end-to-end dynamic routing across their Cloud WAN, they also want to control which networks and resources (prefixes) can route across their global networks. Controlled routing environments are necessary to:

- Selectively filter or propagate routes to achieve specific connectivity goals
- Minimize routing reachability blast radius
- Prevent sub-optimal or asymmetric connectivity patterns
- Avoid over-running of route tables due to propagation of unnecessary routes in global networks
- Protect against misconfiguration that can cause unintended route propagations such as incorrect VPC CIDRs or on-premises route advertisements

### Optimize connectivity in multi-path environments

Customers build multiple connectivity paths between Cloud WAN and their on-premises networks for network resiliency and high availability. It is also common to run into ad-hoc multi-path scenarios where same destination prefixes are learnt over multiple network paths in large BGP-based dynamic networks. In such scenarios, customers want the ability to dictate what paths the network traffic should take by manipulating BGP path preference attributes. Advanced routing policy capability on Cloud WAN allows customers to manipulate standard BGP attributes for selecting optimal path to route network traffic in multi-pathing environments.

## Key benefits

- **AWS-native advanced routing capability** — Eliminates the need for customers to invest in expensive third-party routing solutions that can be complicated and hard to manage. Providing native advanced routing policy in Cloud WAN removes the need for hard to manage and expensive third-party routing solutions.
- **Advanced visibility** — Visibility into route exchanges in an end-to-end dynamically routed network such as Cloud WAN is mandatory for customers to perform Day N operations such as network planning and troubleshooting. This feature provides visibility into the BGP routes that are dynamically learnt and advertised along with the advanced BGP attributes enabling customers to troubleshoot and resolve complex network issues in their Cloud WAN based global networks.

## Advanced routing capabilities

Cloud WAN Routing Policy supports the following capabilities:

- **Route filtering** — Filter (drop) routes from incoming and outgoing route propagations over Cloud WAN attachments. You can set advanced routing policy rules to match one or more prefixes, prefix lists or BGP communities and drop those routes from inbound or outbound route propagations on an attachment. You can also apply these route filtering rules for routes propagated across segments and across regions on the core network (CNE-to-CNE) peering mesh.
- **Route summarization** — Summarize or aggregate routes outbound on Cloud WAN attachments by specifying the desired summary route. You can set an outbound route policy with rules to match on prefixes or prefix lists and specify a summary route to propagate.
- **Path preferences** — Set path preferences to influence incoming and outgoing traffic paths between your Cloud WAN (core network) and external networks. You can set path preferences by modifying BGP attributes such as local preference, AS-PATHs and MED on inbound and outbound route propagations.
- **BGP communities** — Transitively pass BGP communities in outbound route updates, match on BGP communities that are part of inbound route updates, and perform actions such as route filtering, setting path preference attributes or adding and removing BGP communities in outbound route updates.

## Attachment type support

The Cloud WAN Routing Policy feature is supported on all AWS Cloud WAN attachment types, including AWS Site-to-Site VPN, AWS Direct Connect, Connect attachments, peering attachments (Transit Gateway route table), and VPC attachments, as well as on routes propagated across segments and Regions (CNE-to-CNE).

Route summarization and BGP attribute modification are supported only on BGP-capable attachments—Site-to-Site VPN, Direct Connect, Connect, and peering—as well as on inter-segment and inter-Region (CNE-to-CNE) propagated routes. For VPC attachments, support is limited to route filtering rules (“allow” or “drop” actions) for inbound route propagation from the VPC to the core network. BGP communities are supported on Site-to-site VPN and Connect attachments.

## Key considerations

The following is a list of considerations that should be taken into account before using Cloud WAN Routing Policies:

- VPC attachments don't support BGP attribute modification
- Summarization only works outbound and on BGP-capable attachments
- Routing policies associated across segments and regions are unidirectional
- No BGP community support on Direct Connect and TGW Peering attachments
- ASNs specified in the routing policy (replace/remove ASN, community tags) cannot overlap with the ASN range specified in the core network configuration.
  This also means you cannot advertise communities into a core network that contain an ASN currently in use by the core network.
- Replace ASN is not support cross-region (CNE-to-CNE)
- Prefix list alias's must be unique per prefix list core network association
- Prefix list modifications of entry values to the underlying core network routing state may not align with the prefix list state.
- Routing policies are not supported for NFGs (Service Insertion)
- Segment share policies are applied after attachment policies
- External AWS devices cannot advertise routes with BGP communities containing internal ASNs
- The list-core-network-routing-information API shows the routing information before routing policies have been applied
- Route summarization will remove all matched prefixes and replace them with a single summarized route. The summarized prefix will be advertised at the same time as matched prefixes are withdrawn.

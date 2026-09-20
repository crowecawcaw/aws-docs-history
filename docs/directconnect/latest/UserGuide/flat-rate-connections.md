

# Flat-rate billing for dedicated connections
<a name="flat-rate-connections"></a>

Direct Connect offers flat-rate as a new billing mode for dedicated connections, available alongside the existing pay-as-you-go model. You set the billing mode per connection, and you can switch a connection back to pay-as-you-go at any time. Flat-rate billing introduces **port-pairs**, a recommended setup that builds resiliency into your connection by default.

Flat-rate billing applies to **dedicated** connections only. Hosted connections provisioned by an Direct Connect Partner are not eligible.

**Note**  
For how flat-rate connections are priced — the fixed hourly rate, pricing tiers, and what the flat rate includes — see the [Direct Connect Pricing Guide](https://docs.aws.amazon.com/directconnect/latest/PricingGuide/pricing-flat-rate.html).

## Creating a flat-rate connection
<a name="flat-rate-creating"></a>

When you create a Direct Connect dedicated connection, you choose the following:

1. **Location** – The Direct Connect location where your connection is provisioned.

1. **Bandwidth** – The port speed. Bandwidth can't be changed after the connection is created. To use a different bandwidth, you must create a new connection.

1. **Billing mode** – Either pay-as-you-go or flat-rate.

1. **Pricing tier** – The tier determines which AWS Regions are covered under flat-rate billing for that Direct Connect location. For more information about pricing tiers, see the Direct Connect Pricing Guide.

Direct Connect flat-rate billing is built around port-pairs, which is the recommended setup. It gives you a resilient architecture by default, with the redundant port included at no additional charge. You can also use flat-rate billing on a single connection if you prefer to provide your own redundancy, such as a VPN. For more information, see [Using flat-rate billing on a single connection](#flat-rate-single).

## Port-pairs and resiliency
<a name="flat-rate-port-pairs"></a>

Direct Connect flat-rate billing applies to **port-pairs**. A port-pair builds redundancy into your connection by default, so you get a resilient architecture without having to design it yourself.

### What is a port-pair?
<a name="flat-rate-what-is-port-pair"></a>

A port-pair is two dedicated Direct Connect ports, provisioned on different devices or in different locations, that share the same pricing tier. One port carries your traffic and the other stands by for redundancy. If one port becomes unavailable — for example, during an outage or a maintenance window — your connection stays up through the redundant port. Both ports can carry traffic simultaneously; however, the effective bandwidth of the port-pair is limited to the capacity of a single connection. For more information, see [Effective bandwidth](#flat-rate-effective-bandwidth).

The second port is included at no additional charge.

To create a port-pair, place two qualifying flat-rate connections into a resiliency group, a logical grouping that declares your intended redundancy model. AWS matches the qualifying connections in the group as a port-pair. For more information, see [Resiliency groups](#flat-rate-resiliency-groups).

A connection is part of a port-pair when all of the following are true:
+ The connection is set to flat-rate billing mode.
+ The connection belongs to a resiliency group.
+ The group contains at least one other flat-rate connection on a different device.
+ The qualifying connections share the same port speed and the same pricing tier.

Both connections in a port-pair must use the same pricing tier. Because the second port exists solely for resiliency, differing billing properties within a pair are not supported.

The two connections do not need to be in the same Direct Connect location. You can pair ports across locations as long as they meet the preceding requirements. Pairing across locations protects you against a complete location failure as well as a device failure.

A resiliency group can contain any number of connections. AWS looks for pairs within the group. It pairs any two connections on separate devices that share the same billing mode, pricing tier, and port speed. Connections in the group with no match are treated as single connections. A link aggregation group (LAG) counts as a single connection for resiliency group purposes.

After the connections are matched as a port-pair, the billing mode updates on each connection. The following example shows a resiliency group with two associated connections that are billed as a port-pair.

![The Direct Connect console showing a resiliency group named test-RG with two associated connections, each with a billing mode of PortPairFlatRateTier2, confirming that they are billed together as a port-pair.](https://docs.aws.amazon.com/directconnect/latest/UserGuide/images/flat-rate-port-pair-billing.png)


If you delete a connection or change a property that breaks the pairing requirements, both connections revert to single connections. Because flat-rate billing is calculated per hour, changes are reflected within the next billing hour.

All members of a LAG must use the same billing mode. A LAG can't mix flat-rate and pay-as-you-go connections. A flat-rate connection that leaves a LAG keeps flat-rate as its billing mode. A pay-as-you-go connection added to a LAG that already uses flat-rate billing converts to flat-rate automatically.

### Effective bandwidth
<a name="flat-rate-effective-bandwidth"></a>

The usable capacity that you purchase is the capacity of a **single** port. The second port exists solely for redundancy and does not add throughput. For example, a 10 Gbps port-pair at any Direct Connect location gives you an effective usable capacity of **10 Gbps, not 20 Gbps**. If one port fails, the other maintains your full 10 Gbps of connectivity. Plan your port-pairs based on the total capacity that you need. For example, if your workload requires 20 Gbps, provision two 10 Gbps port-pairs.

By enrolling in flat-rate pricing, you agree to use the service in accordance with the AWS Customer Agreement and AWS Service Terms.

### Using flat-rate billing on a single connection
<a name="flat-rate-single"></a>

A port-pair is the recommended setup, but you can also set a single connection to flat-rate billing mode, assign it a pricing tier, and run it without adding it to a resiliency group. This suits you if you want to run one connection at high utilization and provide redundancy yourself — for example, using AWS Site-to-Site VPN as backup. You can also deploy two full-bandwidth connections independently.

Keep the following in mind:
+ A single flat-rate connection costs the same as a port-pair at the same bandwidth and tier. Running one port instead of two does not reduce your price, so there is no cost saving. What you gain is flat-rate billing on a single connection.
+ Your usable bandwidth equals the capacity of that connection, and you can use its full capacity.
+ You do not receive a redundant port and must design for resiliency yourself.

If resiliency matters for the workload, use a port-pair or provide separate backup connectivity such as a VPN.

## Resiliency groups
<a name="flat-rate-resiliency-groups"></a>

To form a flat-rate port-pair, your connections must belong to a **resiliency group** — a logical grouping of Direct Connect connections that declares your intended redundancy model, so that AWS can pair connections correctly.


| How you order | How connections join a resiliency group | 
| --- | --- | 
| Console (Create connection wizard) | You select a resiliency model and create a new resiliency group or add your connections to an existing group. | 
| API | You create or identify the resiliency group, create your connections, and then associate the connections with the group. | 
| Existing connections | Two existing connections provisioned on different devices can be paired by adding them to a resiliency group. | 

## Switching billing modes
<a name="flat-rate-switching"></a>

Billing mode is a per-connection setting that you can change, so you can switch a connection between pay-as-you-go and flat-rate. Billing mode changes are limited to three per connection in any rolling six-month period.

To convert existing pay-as-you-go connections to flat-rate and create a port-pair, complete the following steps:

1. Update the billing mode for each connection to flat-rate.

1. Associate the connections with a new or existing resiliency group.

If you convert a connection to flat-rate without adding it to a resiliency group, the connection is treated as a single flat-rate connection rather than part of a port-pair.

## Limitations
<a name="flat-rate-limitations"></a>

All Direct Connect connections under a single account at a given Direct Connect location must use the same billing mode, either pay-as-you-go or flat-rate. You cannot mix billing modes within the same account at a location.

To use a mix of billing modes at the same location, create and maintain the connections under separate AWS accounts.

## Frequently asked questions
<a name="flat-rate-faq-ug"></a>

**Does the second port double my bandwidth?**

No. Usable bandwidth equals the capacity of a single port. A 10 Gbps port-pair gives you 10 Gbps of usable capacity, not 20 Gbps. The second port protects your connection; it does not add throughput.

**Can I switch a connection back to pay-as-you-go?**

Yes. Billing mode is a per-connection setting that you can change. Billing mode changes are limited to three per connection in any rolling six-month period.

**Is flat-rate billing available for hosted connections?**

No. Flat-rate billing applies to dedicated connections only.
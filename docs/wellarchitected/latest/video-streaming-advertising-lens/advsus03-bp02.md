

# ADVSUS03-BP02 Route more partner traffic internally to share infrastructure and energy savings

 Traffic exchanged between RTB Fabric customers requires less infrastructure overhead than externally routed traffic. When more partners join RTB Fabric, all participants share the resulting infrastructure and energy savings. 

 **Desired outcome:** 
+  A high and growing proportion of real-time bidding traffic is routed inside RTB Fabric between participating partners. 
+  Your highest-volume AdTech partners are onboarded to RTB Fabric and connect using the internal-to-internal pattern. 
+  The ratio of inside to external traffic is measured continuously and trends toward a greater inside share over time. 

 **Common anti-patterns:** 
+  Routing bid traffic over external paths by default, even when both the requester and responder are already RTB Fabric customers. 
+  Not measuring the split between inside and external traffic. 
+  Treating partner onboarding as a purely commercial decision without making the shared sustainability gains visible. 

 **Benefits of establishing this best practice:** 
+  Reduced infrastructure overhead and associated energy use for traffic exchanged between partners. 
+  Shared sustainability gains realized across participating partners rather than by a single party. 
+  Improved visibility into traffic patterns, enabling continued routing and efficiency optimization. 

 **Level of risk exposed if this best practice is not established:** Low 

## Implementation guidance
<a name="implementation-guidance"></a>

 Real-time bidding produces one of the highest request volumes in an advertising workload. A single impression can fan bid requests out to many demand partners, and those exchanges repeat billions of times a day. When a partner sits outside your network boundary, each request leaves your VPC through a NAT gateway and external egress path before it reaches the partner. The response returns over the same path. That path is a separate layer of address-translation and packet-processing infrastructure, and it draws energy in proportion to the connections and bytes it handles. RTB Fabric's internal-to-internal pattern applies when the requester and the responder are both already fabric customers. The exchange stays on shared internal connectivity and never crosses the external boundary. The NAT and egress layer that would otherwise carry the same bytes is neither provisioned nor powered. 

 Because the volume is so large, per-request overhead on the external path is the main efficiency opportunity. Removing a redundant hop on traffic that flows either way avoids energy without changing the advertising outcome. The gain is bilateral, because the exchange a requester keeps inside the fabric is served more efficiently for the responder as well. The benefit is shared across all participating partners. How much traffic can move inside depends on the composition of your partner base. 

 You cannot move an exchange inside the fabric unilaterally, because the counterparty must also be a fabric customer. Onboarding requires engineering and commercial work from that partner, while the efficiency benefit is shared across both sides. A partner who weighs a concrete cost against a diffuse gain shared across all participants may deprioritize the work. The highest-volume partners, where the addressable savings are largest, are the ones hardest to influence. Even with mutual membership, eligible traffic can still fall back to an external path when the internal route is not the one taken. 

 The volume of traffic shifted inside the fabric and the external egress it avoids are proxies for the efficiency gained. These proxies show where the opportunity is largest, but they are not a direct energy measurement. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prioritize high-volume partners:** Identify your highest-volume AdTech partners and prioritize onboarding them to RTB Fabric to maximize the addressable share of inside traffic. 

1.  **Use internal-to-internal connectivity:** Adopt the connectivity pattern in which both the requester and responder are RTB Fabric customers so eligible traffic stays inside the fabric. 

1.  **Track the inside-to-external ratio:** Measure the ratio of inside to external traffic and set targets to increase the inside percentage over time. 

1.  **Use traffic and egress as efficiency proxies:** Track inside traffic volume and avoided external network egress as proxies for the efficiency benefit. 

1.  **Share benefits with partners:** Communicate the sustainability benefits to partners to encourage broader RTB Fabric adoption. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS03-BP01 Align partner connectivity capacity with bid activity to reduce idle energy draw](advsus03-bp01.md) 
+  [ADVSUS03-BP03 Shed predictably low-value traffic at the network layer to reduce the compute footprint](advsus03-bp03.md) 
+  [ADVSUS03-BP06 Continuously measure fabric utilization and retire unjustified capacity](advsus03-bp06.md) 

 **Related documents:** 
+  [AWS RTB Fabric pricing](https://aws.amazon.com/rtb-fabric/pricing/) 

 **Related services:** 
+  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) 
+  [AWS Sustainability service](https://docs.aws.amazon.com/sustainability/latest/userguide/what-is-sustainability.html) 
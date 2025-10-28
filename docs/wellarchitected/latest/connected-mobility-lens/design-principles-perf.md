# Design principles

Core capabilities

- Vehicle provisioning
- Command and control functions
- Telemetry
- Over-the-air updates (OTA)
- Mobile applications – Remote operations (for example, remote start)

**Edge processing and vehicle shadow service architecture:** The
fundamental idea behind this principal is that the automotive industry is transforming itself
to provide a more software centric mobility experience to their customer through applications
and services for both safety and non-safety critical features. This ranges from safety
features in AV/ADAS space as well non-safety critical features like personalization, content
recommendation, trips, navigation, and more. This pushes the need to have more on-board
vehicle compute and storage with high performance CPUs and GPUs. While this is good, there
will never be enough storage and compute on-board vehicles to meet growing industry needs to
provide these experiences and match them with the necessary safety standards. Therefore, the
need exists to have more hybrid architecture and services in place to offload portions of
non-safety critical workloads to edge locations closer to the vehicles to meet latency
requirements.

**Design for failover:** Failures in connected mobility systems
are inevitable especially when vehicles are traversing in suburbs and terrains where
connectivity is spotty and is critically impacted. Working through all possible "what-if"
scenarios during design phase and also having test cases to validate possible scenarios is a
critical aspect of building these systems. Apart from connectivity, it's also important to
build resilient and highly-available cloud systems with a fallback system in place for worst
case scenarios.

**Auto scaling everywhere:** Running and maintaining a connected
mobility application can be expensive, especially when adhering to specific SLAs and KPIs that
cannot be compromised. By using the appropriate services on AWS and applying best practices
and recommendations, customers can handle variable vehicle-cloud data volume spikes and high
vehicle density in specific geographies. This ensures that systems are automatically scalable
on a needed basis and are not running at full capacity at all times, especially during
low-usage periods.

**Multiple connectivity channels:** Vehicle-cloud connectivity is
an integral part of providing a good connected mobility experience. Relying on a single
connectivity channel is error prone due issues like coverage, quality of service (QoS) and
bandwidth capacity and availability. Therefore, it is recommended to explore more than one
connectivity channel not only as a fallback mechanism in case of fail-over, but also as a
means to use different channels for different workload needs. Options can vary, but could
include using secure Wi-Fi for large OTA upgrades to save data costs, using 5G for high
bandwidth, low latency connectivity needs for edge computer-vision or AI/ML workloads, or
using satellite for vehicle-cloud connectivity for high bandwidth needs where latency is not
critical and 5G connectivity is unreliable.

**Every workload is different:** Connected mobility workloads
have their own set of challenges ranging from collecting data when the vehicle is in motion,
processing them and offloading them. It includes latency and bandwidth requirements for data
transfer, and its own SLAs and KPIs that must be met to function optimally.  This is
especially important for safety critical features which cannot be offloaded to edge locations
but still rely on cloud connectivity for some operations. So rather using a modular
architecture approach for all use cases, using these as guiding principles to design what
would be the optimal location for workload execution (edge or region) and tradeoffs can be
made keeping the user safety in mind. 

**Measuring and improving with growth:** Having mechanisms in
place where critical workloads are monitored for specific KPI's for performance and ensuring
that it meets the desired SLAs is critical. Even with features like auto-scalable systems, as
more and more vehicles are on-boarded to connected mobility systems it's inevitable that
feature level and overall system performance will degrade over time. Therefore, understanding
tradeoffs in latency and cost in order to support continuously evolving systems, architectures
and mechanisms are needed in order to support critical workloads wherever the vehicle is
operating.

**Regulatory compliance tradeoffs:** Adhering to local laws and
regulatory compliance is mandatory. Care must be taken to assess and consider any impact on
performance while adhering to them. Based on data processing compliance requirements design
your workload architecture to process the data closer to the edge whenever possible can offset
some of the performance concerns.

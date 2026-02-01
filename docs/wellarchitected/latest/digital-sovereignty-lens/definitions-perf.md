# Definitions

The following are performance efficiency-specific definitions:

- **Traffic routing:** The process
  of directing network requests and data flows from source to
  destination based on predefined rules, policies, or algorithms,
  implemented at multiple layers including DNS, load balancers,
  and content delivery networks.
- **Geographic routing:** Also
  called geolocation routing, this is a traffic management
  strategy that directs user requests to specific endpoints based
  on the physical or network location from which the request
  originates, using the source IP address to determine geographic
  location and apply predefined routing rules. For sovereign
  workloads, geographic routing is a mandatory compliance control.
- **Geo-fencing:** A security and
  compliance technology that creates virtual geographic boundaries
  and enforces restrictions blocking data, requests, or resources
  from moving beyond defined geographic limits through network
  restrictions, service configurations, IAM policies, and
  monitoring systems. Geo-fencing serves as both a preventative
  and detective control that verifies that sensitive data never
  leaves approved jurisdictions while providing visibility into
  attempts to violate geographic constraints.
- **Edge location:** are
  geographically distributed points of presence containing caching
  servers and compute resources positioned close to end users to
  reduce latency and improve application performance, numbering in
  the hundreds of locations worldwide as part of Amazon CloudFront
  CDN infrastructure. For sovereign workloads, edge locations
  present compliance considerations because cached data
  temporarily resides outside primary AWS Regions potentially
  across jurisdictional boundaries.
- **Cloud-based:** Refers to
  applications and architectures designed specifically to use
  cloud computing capabilities through microservices architecture,
  containerization, dynamic orchestration, and managed cloud
  services rather than simply migrating traditional applications
  to cloud infrastructure. For sovereign workloads, cloud-based
  patterns offer significant advantages including built-in
  compliance features in managed services, regional isolation with
  independently deployed microservices, and containerization that
  facilitates portability across cloud providers to avoid vendor
  lock-in.
- **Multi-layered approach:** Also
  called defense in depth, this is a security and reliability
  strategy that implements multiple independent, complementary
  controls at different architectural layers—including network
  boundaries, identity and access, data protection, application
  security, monitoring, and processes—so that if one control
  fails, others continue to provide protection. For sovereign
  architectures, multi-layered approaches are essential because
  compliance isn't guaranteed by a single technology.
  Organizations must combine geographic controls (Region
  selection, geo-fencing), cryptographic controls (encryption, key
  management), access controls (IAM policies, network
  segmentation), operational controls (monitoring, audit logging),
  and contractual controls.
- **Multi-Region:** Architectural
  pattern where application components, data, and infrastructure
  are distributed across multiple geographically separated AWS Regions to achieve high availability, disaster recovery,
  performance optimization, or compliance with data residency
  requirements, with each Region being completely independent with
  separate control planes and infrastructure.
- **High-availability (HA)
  architecture:** System design approach that provides
  continuous operation and minimal downtime even during component
  failures through redundancy at every layer, removing single
  points of failure with multiple application servers across
  availability Zones, load balancers, database replication, and
  automated failover mechanisms targeting availability of 99.9% or
  higher. For sovereign workloads, achieving high availability
  within geographic constraints is challenging because redundant
  infrastructure must reside within approved regions, requiring
  organizations to balance availability requirements against
  sovereignty constraints.

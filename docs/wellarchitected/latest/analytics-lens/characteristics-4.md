# Characteristics

**Discoverability:** The ability of the system to make
operational data available for consumption. This involves discovering multiple disparate types
of data available within an application that can be used for various ad hoc explorations.

**Connectivity:** Operational data can emanate from a variety of
data sources in different format with disparate volumes. For this reason, the operational
system has to provide the capability to seamlessly integrate all the data with the least
overhead for production application.

**Scalability:** The ability of the system to scale up and out to
adapt to changes in the operational analytics workload in terms of storage or compute
requirements.

**Monitoring:** You should be able to continuously monitor the
operational system performance and get notified about the resource utilization and the overall
health of your system.

**Security:** The access to the operational system must
be secure. With Amazon OpenSearch Service, you can configure the domain to be accessible with an endpoint
within your VPC or a public endpoint accessible to the internet. In addition to network-based
access control, you must set up user authentication and authorization to secure the access to
data based on business requirements. OpenSearch Service supports encryption at rest and in Transit.

**Data durability:** With operational analytics, the use cases
differ as to the retention requirements. You should understand your business requirements in
terms of analyzing historical data. With Amazon OpenSearch Service, you can retain more data with less cost
using the UltraWarm and cold storage tiers.

**Automation:** The data lifecycle in your operational system
should be automated in order to easily onboard new data pipelines and reduce the overhead of
managing the lifecycle of the data. With Index State Management (ISM) in Amazon OpenSearch Service, you can
create your own policies to automate the lifecycle management of indices stored in the
service.

  **Observability:** The ability to understand internal state
from the various signal outputs in the system. By providing a holistic view of these various
signals along with a meaningful inference it becomes easy understand how healthy and well
performant the overall system is.

**User centricity:** Each analytics application should address a
well-defined operational scope and solve a particular problem at hand. Users of the system
often won’t understand or care about the analytics process but only see the value the result.

 

**Agility:** The system must be ﬂexible enough to accommodate
changing needs of an analytics application and offer necessary control to bring in additional
data with low overhead.

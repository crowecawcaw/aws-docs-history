# HNPERF01-BP02 Identify what applications and types of data will

be transmitted over the network

Applications can have their own bandwidth considerations. Some
applications might require deterministic performance over a
high-bandwidth connection, while others can require both
deterministic performance and high bandwidth. An application may
need specific configuration to use multiple traffic flows in
parallel if it is hitting per traffic flow bandwidth limits,
allowing it to use more of the connection's bandwidth.

**Desired outcome:**

- Comprehensive understanding of application network requirements
  and data transfer patterns across the hybrid infrastructure.
- Enables proper sizing of network connections, appropriate
  selection of connectivity options.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Optimize network performance for different application types and
  cost-effective selection of connectivity options
- Right-size network infrastructure, prevent bottlenecks, and
  ensure smooth operations during varying workload conditions.

## Implementation guidance

- Inventory of applications that will utilize the hybrid
  network, categorizing them based on their performance
  requirements and criticality.
- Analyze application's bandwidth needs, sensitivity to latency,
  and data transfer patterns.

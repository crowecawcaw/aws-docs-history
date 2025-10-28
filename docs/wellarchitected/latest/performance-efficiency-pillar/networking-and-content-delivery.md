# Networking and content delivery

The optimal networking solution for a workload varies based on
latency, throughput requirements, jitter, and bandwidth. Physical
constraints, such as user or on-premises resources, determine
location options. These constraints can be offset with edge
locations or resource placement.

On AWS, networking is virtualized and is available in a number of
different types and configurations. This makes it easier to match
your networking needs. AWS offers product features (for example,
Enhanced Networking, Amazon EC2 networking optimized instances,
Amazon S3 transfer acceleration, and dynamic Amazon CloudFront) to
optimize network traffic. AWS also offers networking features (for
example, Amazon Route 53 latency routing, Amazon VPC endpoints, AWS Direct Connect, and AWS Global Accelerator) to reduce network
distance or jitter.

This focus area shares guidance and best practices to design, configure, and operate efficient networking and content delivery solutions in the cloud.

###### Best practices

- [PERF04-BP01 Understand how networking impacts
  performance](perf_networking_understand_how_networking_impacts_performance.md "perf_networking_understand_how_networking_impacts_performance.md")
- [PERF04-BP02 Evaluate available networking features](perf_networking_evaluate_networking_features.md "perf_networking_evaluate_networking_features.md")
- [PERF04-BP03 Choose appropriate dedicated connectivity or VPN
  for your workload](perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.md "perf_networking_choose_appropriate_dedicated_connectivity_or_vpn.md")
- [PERF04-BP04 Use load
  balancing to distribute traffic across multiple resources](perf_networking_load_balancing_distribute_traffic.md "perf_networking_load_balancing_distribute_traffic.md")
- [PERF04-BP05 Choose network protocols to improve
  performance](perf_networking_choose_network_protocols_improve_performance.md "perf_networking_choose_network_protocols_improve_performance.md")
- [PERF04-BP06 Choose your workload's location based on network requirements](perf_networking_choose_workload_location_network_requirements.md "perf_networking_choose_workload_location_network_requirements.md")
- [PERF04-BP07 Optimize network configuration based on
  metrics](perf_networking_optimize_network_configuration_based_on_metrics.md "perf_networking_optimize_network_configuration_based_on_metrics.md")

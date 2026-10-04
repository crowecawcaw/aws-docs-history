

# Applying the pattern beyond CMS
<a name="tpd-applying"></a>

For a consumer in another cloud, the pattern’s default — subscribe rather than copy — means serving that consumer from a Kafka topic on AWS, over a private multicloud interconnect where the consumer’s workloads must remain in the other cloud, rather than egressing telemetry over best-effort peering. The private interconnect replaces an uncontracted path with a contracted one, and removing the egress altogether where consumption can move onto AWS is the stronger option on both cost and availability.

For an autonomous-fleet data layer, the same pattern governs how high-volume vehicle capture is made available to downstream training, analytics, and operations consumers: partition for the most demanding consumer, isolate each downstream by group and quota, hold schemas as versioned contracts, and keep the authoritative data on AWS so training pulls and operational reads draw from one governed source rather than proliferating copies. In both cases, size the cost and set the latency and recovery targets with the consumer rather than assuming them.
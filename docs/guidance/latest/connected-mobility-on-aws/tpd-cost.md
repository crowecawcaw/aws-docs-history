

# Cost: where the money goes
<a name="tpd-cost"></a>

The dominant cost in third-party delivery is data movement. Data transferred within an Availability Zone is cheapest; data crossing Availability Zones inside a Region carries an inter-AZ charge on both sides; data crossing Regions carries inter-Region transfer; and data leaving AWS for the public internet or another cloud carries the highest egress rate. The design consequence is direct: a consumer served from a Kafka topic on AWS, or over a private interconnect, avoids the internet-egress tier entirely, while the same delivery to a cross-cloud destination over best-effort peering pays the top rate on every byte with no reliability commitment in return. Replication adds storage cost for the duplicated copy plus the transfer to move it. Because these rates are account- and Region-specific and change over time, size the cost per consumer once volume, destination, and pattern are known, rather than assuming fixed figures.
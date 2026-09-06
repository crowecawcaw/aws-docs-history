

# Failover to the secondary AWS Region
<a name="msk-replicator-when-failover"></a>

We recommend that you monitor replication latency in the secondary AWS Region using Amazon CloudWatch. During a service event in the primary AWS Region, replication latency may suddenly increase. If the latency keeps increasing, use the [AWS Service Health Dashboard](https://health.aws.amazon.com/health/status) to check for service events in the primary AWS Region. If there is a service event, you can failover to the secondary AWS Region.
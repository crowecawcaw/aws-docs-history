

# Demonstrated in production: CMS’s telemetry pipeline
<a name="tn-cms-reference"></a>

The [connected-mobility-guidance-on-aws](https://github.com/aws-solutions-library-samples/guidance-for-connected-mobility-on-aws) repository contains a production implementation of this exact pattern shape: the `modules/flink/` directory holds Managed Service for Apache Flink processors that perform keyed windowing, deduplication, pattern detection, and multi-destination routing, with an Amazon ElastiCache (Redis) sink for low-latency state access and an Apache Iceberg sink for durable analytics.

This is a reference implementation — not the only implementation, and deploying this ADP foundation does not require deploying CMS. If you want to examine a concrete, working embodiment of the eight-step architecture above before designing your own, the CMS Flink processors are the closest existing proof-of-pattern on AWS.
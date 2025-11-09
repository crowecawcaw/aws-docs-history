# MIDAREL02-BP01 Design resilient industrial integration patterns

Implement redundant and fault-tolerant architectural patterns that maintain operational
continuity during system failures. Your manufacturing data architecture should include local
processing capabilities, data buffering, and automatic recovery mechanisms to verify that
critical production processes continue even when cloud connectivity or key systems fail.

**Desired outcome:** Manufacturing operations continue with
minimal disruption when systems fail, with production data preserved and synchronized once
systems are restored. Critical operational parameters remain accessible to machine operators,
and production workflows continue functioning through degraded modes.

**Benefits of establishing the Best Practice:** By implementing
resilient integration patterns, manufacturers can minimize production downtime, maintain
product quality during system failures, preserve critical operational data, and properly
synchronize systems once they are restored, ultimately helping protect revenue and customer
satisfaction.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

**Implement edge computing solutions**

First, assess your manufacturing systems' criticality, required processing latency, and
local autonomy requirements.

Document which operations must continue during cloud connectivity disruptions.

Design local processing capabilities that can operate independently when disconnected,
with clear rules for autonomous decision-making and data buffering.

Consider implementing AWS IoT Greengrass on factory floor gateways to enable local
processing and autonomous operations during connectivity issues, with rules that determine
which operations can continue locally and which require cloud connectivity.

**Create data buffering mechanisms**

Begin by analyzing your data generation patterns, storage requirements, and acceptable
data latency windows. Document recovery time objectives (RTOs) and recovery point objectives
(RPOs) for different data types.

Implement local storage mechanisms that can retain manufacturing data during outages
and automatically synchronize when connectivity is restored.

Consider using AWS IoT SiteWise Edge to store time-series production data locally
during connectivity interruptions, with automatic synchronization to AWS IoT SiteWise in the
cloud when connectivity returns.

**Design circuit breaker patterns**

Start by mapping dependencies between manufacturing systems and identifying potential
failure points. Define graceful degradation modes for each critical service and establish
fallback mechanisms.

Implement patterns that can detect failures and automatically switch to alternative
processing paths.

Consider implementing circuit breakers using AWS Step Functions to handle failures in
downstream dependencies and automatically switch to predefined fallback mechanisms that
maintain critical manufacturing operations.

**Configure automatic failover systems**

First document your manufacturing system's availability requirements and acceptable
downtime windows. Establish clear failover activations and recovery procedures.

Design redundant connectivity paths with automated switching capabilities to maintain
continuous operations.

Consider deploying redundant AWS IoT Core endpoints with automatic failover
capabilities to provide reliable connectivity between manufacturing systems and cloud
services, with monitoring to verify successful failover operations.

## Key AWS services

- AWS IoT Greengrass
- AWS IoT SiteWise
- AWS Step Functions
- AWS IoT Core
- Amazon Kinesis Data Streams

## Resources

- [Implementing Edge Computing with AWS IoT Greengrass](../../../greengrass/v2/developerguide/edge-runtime.md "../../../greengrass/v2/developerguide/edge-runtime.md")
- [Configuring Data Buffering with AWS IoT SiteWise
  Edge](https://aws.amazon.com/about-aws/whats-new/2023/11/aws-iot-sitewise-buffered-batched-measurement-data/ "https://aws.amazon.com/about-aws/whats-new/2023/11/aws-iot-sitewise-buffered-batched-measurement-data/")
- [Designing Resilient Industrial Applications with AWS Step Functions](../../../step-functions/latest/dg/concepts-error-handling.md "../../../step-functions/latest/dg/concepts-error-handling.md")
- [Building High Availability Industrial IoT Solutions with
  AWS](../../../whitepapers/latest/industrial-iot-architecture-patterns/variant-7-edge-gateway-high-availability.md "../../../whitepapers/latest/industrial-iot-architecture-patterns/variant-7-edge-gateway-high-availability.md")

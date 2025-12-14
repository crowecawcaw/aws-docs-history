# ADVSUS08-BP01 Optimize privacy workload processing

patterns and resource allocation for sustainability

For privacy-enhanced collaboration, advertising workloads have specific sustainability considerations for combining first and third-party customer data directly.

## Implementation guidance

- Schedule intensive privacy computations during periods of
  lower carbon intensity.
- Use batch processing for data cleansing and matching
  operations.
- Implement efficient data compression and formatting using
  formats such as Parquet.
- Leverage AWS Graviton processors for energy-efficient
  computing.
- Use serverless architectures for matching operations where
  possible.
- Implement auto scaling based on actual collaboration
  workload patterns.
- Configure Regional data aggregation before central
  processing to reduce transfer needs.

## Key AWS services

- AWS Lambda
- AWS Graviton Processors
- AWS Auto Scaling

## Resources

- [Hardware and services](../sustainability-pillar/hardware-and-services.md "../sustainability-pillar/hardware-and-services.md")
- [AWS Clean Rooms](../../../clean-rooms/latest/userguide/optimization.md "../../../clean-rooms/latest/userguide/optimization.md")

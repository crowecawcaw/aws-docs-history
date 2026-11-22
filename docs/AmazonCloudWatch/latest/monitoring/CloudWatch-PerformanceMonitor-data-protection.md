

# Data protection in Performance Monitor

Performance Monitor processes network telemetry data from the AWS infrastructure layer. This data includes the following:
+ Network path routing information
+ Latency and packet loss measurements
+ Traffic volume (bytes) between endpoints
+ Subnet, VPC, and account identifiers

Performance Monitor doesn't access the payload of your network traffic. It doesn't read, inspect, or store the content of your data in transit.

## Encryption at rest
<a name="CloudWatch-PerformanceMonitor-data-protection-at-rest"></a>

Performance Monitor encrypts data at rest by using AWS managed keys.

## Encryption in transit
<a name="CloudWatch-PerformanceMonitor-data-protection-in-transit"></a>

Performance Monitor encrypts all data in transit by using Transport Layer Security (TLS).

## Key management
<a name="CloudWatch-PerformanceMonitor-data-protection-key-management"></a>

AWS creates and manages the keys that Performance Monitor uses to encrypt your data at rest. You don't need to create, rotate, or manage these keys.
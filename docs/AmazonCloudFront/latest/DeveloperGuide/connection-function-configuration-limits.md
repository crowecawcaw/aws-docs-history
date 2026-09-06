

# Configuration and limits
<a name="connection-function-configuration-limits"></a>

CloudFront Connection Functions have specific configuration requirements and service limits due to their specialized role in TLS connection validation and the performance requirements of edge computing.

**Topics**
+ [Function code requirements](#connection-function-code-requirements)
+ [Service limits](#connection-function-service-limits)
+ [Function filtering options](#connection-function-filtering-options)

## Function code requirements
<a name="connection-function-code-requirements"></a>

Connection functions require JavaScript code that processes TLS connection events. The function code must:
+ Be written in JavaScript
+ Process connection events and make allow/deny decisions
+ Complete execution within the time limits
+ Handle certificate and connection validation logic

## Service limits
<a name="connection-function-service-limits"></a>

Connection functions are subject to the following limits:
+ **Function size** – Function code and configuration are limited in size
+ **Execution time** – Functions have strict execution time limits for TLS connection processing
+ **Association limits** – Each distribution can have only one Connection Function associated
+ **Stage restrictions** – Only LIVE stage functions can be associated with distributions

## Function filtering options
<a name="connection-function-filtering-options"></a>

When listing Connection Functions, you can use the following filters:
+ **Stage filter** – Filter by DEVELOPMENT or LIVE stage
+ **Association filter** – Filter by distribution ID or key-value store ID associations

These filters help you organize and manage Connection Functions across different environments and use cases.
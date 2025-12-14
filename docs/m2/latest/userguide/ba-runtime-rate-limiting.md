AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Configure rate limiting for AWS Blu Age Runtime

AWS Blu Age Runtime includes built-in rate limiting functionality to protect gapwalk application from excessive requests and potential abuse.
The rate limiting system uses the Token Bucket algorithm to provide both burst capacity and sustained rate limiting.

###### Topics

- [Rate limiting overview](#ba-runtime-rate-limiting-overview "#ba-runtime-rate-limiting-overview")
- [Configuration properties](#ba-runtime-rate-limiting-config "#ba-runtime-rate-limiting-config")
- [Enable rate limiting](#ba-runtime-rate-limiting-enable "#ba-runtime-rate-limiting-enable")
- [Client identification](#ba-runtime-rate-limiting-client-id "#ba-runtime-rate-limiting-client-id")
- [Rate limit headers](#ba-runtime-rate-limiting-headers "#ba-runtime-rate-limiting-headers")
- [Memory management](#ba-runtime-rate-limiting-memory "#ba-runtime-rate-limiting-memory")

## Rate limiting overview

The rate limiting system provides the following features:

**Token Bucket Algorithm**

- Allows burst traffic up to the configured burst capacity
- Refills tokens at a steady rate based on requests per minute
- Provides smooth rate limiting without blocking legitimate traffic spikes

**Client Identification**

- Identifies clients by IP address with proxy support
- Supports X-Forwarded-For and X-Real-IP headers
- Handles load balancer and reverse proxy scenarios

**Automatic Memory Management**

- Automatically cleans up expired rate limit buckets
- Configurable cleanup intervals and expiry times
- Prevents memory leaks in long-running applications

**HTTP Integration**

- Returns HTTP 429 (Too Many Requests) when limits exceeded
- Includes standard rate limit headers in responses
- Provides retry-after information for clients

## Configuration properties

Configure rate limiting in your `application-main.yaml` file:

```
gapwalk:
  ratelimiting:
    enabled: true                                        # Enable/disable rate limiting
    requestsPerMinute: 1000                              # Sustained rate limit per minute
    burstCapacity: 1500                                  # Maximum burst requests allowed
    includeHeaders: true                                 # Include X-RateLimit-* headers
    cleanupIntervalMinutes: 5                            # Cleanup interval for expired buckets
    bucketExpiryHours: 1                                 # Hours after which unused buckets expire
    errorMessage: "Too many requests. Try again later."  # Custom error message
    whitelistIps: ""                                     # Comma-separated IPs to bypass limiting
    perEndpointLimiting: false                           # Apply limits per endpoint (not implemented)
```

### Property descriptions

**enabled**

Master switch to enable or disable rate limiting functionality. Default: `false`

**requestsPerMinute**

Number of requests allowed per minute for sustained rate limiting. This represents the token refill rate. Default: `1000`

**burstCapacity**

Maximum number of requests allowed in a burst before rate limiting applies. Should be higher than `requestsPerMinute` to allow traffic spikes. Default: `1500`

**includeHeaders**

Whether to include standard rate limit headers (`X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`) in HTTP responses. Default: `true`

**cleanupIntervalMinutes**

Interval in minutes between automatic cleanup of expired rate limit buckets. Helps prevent memory leaks. Default: `5`

**bucketExpiryHours**

Time in hours after which unused rate limit buckets are considered expired and eligible for cleanup. Default: `1`

**errorMessage**

Custom error message returned in the JSON response when rate limit is exceeded. Default: `"Too many requests. Try again later."`

**whitelistIps**

Comma-separated list of IP addresses that bypass rate limiting entirely. Useful for health checks or trusted systems. Default: `empty`

**perEndpointLimiting**

Whether to apply separate rate limits per endpoint instead of per client only. Currently not implemented. Default: `false`

## Enable rate limiting

To enable rate limiting with default settings:

```
gapwalk:
  ratelimiting:
    enabled: true
```

## Client identification

The rate limiting system identifies clients using the following priority order:

1. **X-Forwarded-For header** (first IP if comma-separated)
2. **X-Real-IP header**
3. **Remote address** from the HTTP request

This ensures proper client identification when the application is behind:

- Load balancers
- Reverse proxies
- CDNs
- API gateways

### Example client identification

```
# Direct connection
Client IP: 192.168.1.100

# Behind load balancer with X-Forwarded-For
X-Forwarded-For: 203.0.113.45, 192.168.1.100
Client IP: 203.0.113.45 (first IP used)

# Behind reverse proxy with X-Real-IP
X-Real-IP: 203.0.113.45
Client IP: 203.0.113.45
```

## Rate limit headers

When `includeHeaders` is enabled, the following headers are added to HTTP responses:

**X-RateLimit-Limit**

The rate limit ceiling for the client (requests per minute)

**X-RateLimit-Remaining**

The number of requests remaining in the current rate limit window

**X-RateLimit-Reset**

The time at which the rate limit window resets (Unix timestamp)

### Example response headers

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 847
X-RateLimit-Reset: 1640995200
```

### Rate limit exceeded response

When rate limit is exceeded, the system returns:

**HTTP Status**
429 Too Many Requests

**Content-Type**
application/json

**Retry-After**
Number of seconds to wait before retrying

```
{
  "error": "Rate limit exceeded",
  "message": "Too many requests. Try again later.",
  "retryAfter": 60,
  "timestamp": 1640995140000
}
```

## Memory management

The rate limiting system automatically manages memory to prevent leaks in long-running applications:

**Automatic Cleanup**

- Runs every `cleanupIntervalMinutes` minutes
- Removes buckets unused for `bucketExpiryHours` hours
- Logs cleanup activity for monitoring

**Memory Efficiency**

- Uses concurrent data structures for thread safety
- Lazy bucket creation (only when needed)
- Efficient token bucket implementation

### Monitoring cleanup activity

Check logs for cleanup messages:

```
INFO  RateLimitingService - Cleaned up 15 expired rate limiting buckets
```

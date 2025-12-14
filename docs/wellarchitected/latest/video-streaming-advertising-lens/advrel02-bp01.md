# ADVREL02-BP01 To allow fast and graceful failure of latency-sensitive services, avoid exponential backing off and retry

With real-time bidding systems, your workload must handle failures
in latency-sensitive services. Traditional exponential backoff and
retry mechanisms should be avoided. Instead, opt for fast-fail
approaches and appropriate rate-limiting techniques to maintain
service responsiveness.

## Implementation guidance

Operating within 100 ms real-time bidding contracts, a single
throttle and retry of five seconds can result in many failed
bids and potentially insurmountable retry queues. Avoid this by
adapting retries to fail fast.  Regulate request rates using
algorithms, such as token buckets, leaky buckets, or fixed
window counters, or use managed service features, like Amazon API Gateway's request throttling. Rate limiting helps prevent
resource exhaustion and fairly distributes resources among
clients or services. Know the trade-offs: while rate limiting
can be an effective way to protect a service from being
overloaded, it can also potentially make the service less
reliable if not implemented carefully. For example, if the rate
limits are set too low, legitimate requests may be rejected or
delayed, leading to reduced availability or responsiveness of
the service.

## Key AWS services

- [Amazon API Gateway](https://aws.amazon.com/api-gateway/ "https://aws.amazon.com/api-gateway/") implements the token bucket algorithm to throttle requests according to account and region limits
- [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/ "https://aws.amazon.com/sqs/") and Amazon Kinesis can buffer requests to smooth out the request rate
- [AWS WAF](https://aws.amazon.com/waf/ "https://aws.amazon.com/waf/") can also be used to implement rate
  limiting and throttle specific API consumers

## Resources

**Related documentation:**

- [Implementing
  layers of admission control](https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/ "https://aws.amazon.com/builders-library/fairness-in-multi-tenant-systems/")
- [API Gateway Request Throttling](../../../apigateway/latest/developerguide/api-gateway-request-throttling.md "../../../apigateway/latest/developerguide/api-gateway-request-throttling.md")

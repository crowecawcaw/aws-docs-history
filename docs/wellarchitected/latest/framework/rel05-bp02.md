

# REL05-BP02 Throttle requests

 Your workload can only process so many requests before it runs out of resources. Throttling protects that capacity by accepting requests up to a defined rate and rejecting the excess with a response that signals the request was throttled. This keeps your workload processing its supported volume during traffic spikes, flooding attacks, and retry storms instead of collapsing under load. 

 **Desired outcome:** 
+  Your workload continues normal processing of its supported request volume during sudden or sustained spikes. 
+  Requests above your defined limits are rejected with a throttling response the client can detect and retry later. 
+  Your per-client rate limits prevent a single IP address or API consumer from exhausting resources shared by other consumers. 
+  Your throttling limits match the capacity you proved through load testing, and your provisioned resources meet or exceed those tested limits. 

 **Common anti-patterns:** 
+  Teams leave API endpoint throttles unimplemented or at default values without considering expected volume. 
+  Teams do not load test endpoints, or set throttling limits that were never tested. 
+  Throttling considers request rate but ignores request size or complexity. 
+  Testing covers maximum request rate or maximum request size, but not both together. 
+  Provisioned resources fall short of the limits established in testing. 
+  Usage plans are not configured for application-to-application API consumers. 
+  Queue consumers that scale horizontally have no maximum concurrency configured. 
+  Rate limiting on a per-IP-address basis is missing. 
+  Shared infrastructure requires every consuming team to individually configure their own throttling protection, rather than shipping protection on by default. 

 **Benefits of establishing this best practice:** 
+  Your workload processes accepted load successfully under unexpected volume spikes rather than exhausting its resources. 
+  Spikes against APIs and queues are absorbed without starving request-processing capacity. 
+  Per-requestor rate limits contain a single noisy consumer so it does not degrade service for others. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Design your service to process a known volume of requests, and establish that number through load testing. Once you know the threshold, throttling enforces it: requests within the limit are processed, and requests above it receive a throttled response so the consumer can back off and retry. 

 The *token bucket* algorithm is a common way to implement a rate limit. A bucket holds tokens, each request consumes one token, and tokens refill at a fixed rate per second. When the bucket is empty, requests are throttled until it refills. The bucket size sets how large a burst you tolerate, and the refill rate sets the sustained throughput. The following figure shows this relationship. 

![Diagram of the token bucket algorithm: a bucket holds tokens, each request consumes one token, tokens refill at a fixed rate, and requests are throttled when the bucket is empty.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/token-bucket-algorithm.png)

*Token bucket algorithm for rate limiting*


 A throttle protects total capacity across all consumers. A rate limit protects fairness by capping any single requestor, which prevents one consumer or IP address from consuming shared capacity. You usually need both. A global throttle alone still lets one aggressive client crowd out the rest, and per-client limits alone can still be overwhelmed by many clients at once. 

 Buffering is a third option when the work can be handled asynchronously. Instead of rejecting a spike, accept requests into a queue or stream and drain them at a controlled rate. This smooths bursts and lets you tolerate higher inbound rates than the backend could handle directly. Several AWS services support these patterns: [Amazon API Gateway](https://aws.amazon.com/api-gateway/) implements the token bucket per account and Region and per client through usage plans, [Amazon SQS](https://aws.amazon.com/sqs/) and [Amazon Kinesis](https://aws.amazon.com/kinesis/) buffer requests to smooth the rate, and [AWS WAF](https://aws.amazon.com/waf/) applies rate-based rules to throttle specific consumers that generate unusual load. 

 When you operate shared infrastructure that many teams and services depend on, protect it at the source. Enable throttling by default so every consumer inherits protection automatically. When you introduce or change a default on infrastructure that already has live consumers, roll it out in waves with a bake time between each one. This gives you time to confirm each wave keeps serving existing traffic before the change reaches everyone. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Configure API Gateway throttling:** Set [API Gateway throttling limits](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) at the account level per Region, per API stage, and per API key through usage plans. API Gateway returns 429 Too Many Requests when a limit is exceeded, which clients can detect and retry. 

1.  **Enable protection by default on shared infrastructure:** For infrastructure that many teams consume, apply API Gateway throttling and usage plans from the previous step as the default, so every consumer is protected without opting in. When you introduce or change a default, roll it out in waves with a bake time between them, and confirm each wave keeps serving existing consumers before the change reaches all of them. 

1.  **Apply per-IP rate limiting with AWS WAF:** Attach [AWS WAF rate-based rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) to API Gateway and AWS AppSync endpoints to limit requests per IP address and block offending sources. Configure rate limits on AWS AppSync API keys for application-to-application consumers. 

1.  **Add API Gateway in front of AWS AppSync when needed:** If you require more throttling control than rate limiting provides for AWS AppSync APIs, place an API Gateway in front of the AWS AppSync endpoint to gain usage-plan and token-bucket controls. 

1.  **Set maximum concurrency on queue consumers:** When Amazon SQS queues trigger AWS Lambda consumers, set [maximum concurrency](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency) so queue processing does not consume the account concurrency other functions need. Consider reserved concurrency on other functions in the same account and Region. 

1.  **Buffer requests to smooth load:** Use API Gateway native integrations with Amazon SQS or Amazon Kinesis to accept spikes into a queue or stream and process them at a controlled rate where asynchronous handling is acceptable. 

1.  **Implement the token bucket yourself where API Gateway does not fit:** For services that cannot use API Gateway, adopt a language-specific token bucket library rather than writing your own. See the related examples for options across common languages. 

1.  **Test limits and align provisioned resources:** Load test the limits you plan to set or allow to be increased, and document the tested values. Do not raise a limit beyond what testing proved, and confirm provisioned resources meet or exceed the tested scenario before applying any increase. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md) 
+  [REL04-BP03 Do constant work](rel04-bp03.md) 

 **Related documents:** 
+  [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) 
+  [Using rate-based rule statements in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) 
+  [Introducing maximum concurrency of AWS Lambda functions when using Amazon SQS as an event source](https://aws.amazon.com/blogs/compute/introducing-maximum-concurrency-of-aws-lambda-functions-when-using-amazon-sqs-as-an-event-source/) 
+  [Using Lambda with Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency) 
+  [The three most important AWS WAF rate-based rules](https://aws.amazon.com/blogs/security/three-most-important-aws-waf-rate-based-rules/) 
+  [Security best practices for AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/best-practices.html) 

 **Related examples:** 
+  [GitHub - bucket4j/bucket4j: Java rate limiting library based on token-bucket algorithm.](https://github.com/bucket4j/bucket4j) 
+  [Client Challenge](https://pypi.org/project/token-bucket/) 
+  [Node token-bucket](https://www.npmjs.com/package/tokenbucket) 
+  [NuGet Gallery \| System.Threading.RateLimiting 10.0.12](https://www.nuget.org/packages/System.Threading.RateLimiting) 

 **Related tools:** 
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [AWS AppSync](https://aws.amazon.com/appsync/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/) 
+  [AWS WAF](https://aws.amazon.com/waf/) 
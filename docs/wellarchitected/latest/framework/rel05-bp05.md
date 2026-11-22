

# REL05-BP05 Set client timeouts

 A call with no timeout can wait forever and hold resources while a dependency is impaired. Set both connection and request timeouts on every call across a process boundary, verify them, and do not rely on framework defaults. Framework defaults do not reflect your workload and are often infinite or far higher than your service goals allow. 

 **Desired outcome:** 
+  Your service dependency calls have explicit connection and request timeouts based on measured, normal completion times. 
+  Your clients handle timeouts gracefully, backing off and retrying or opening a circuit breaker rather than reissuing calls that worsen an impairment. 
+  Your resources are conserved when a remote call responds abnormally slowly, because the timeout releases them. 
+  Your timeout values are tested for both connection and request scenarios rather than assumed. 

 **Common anti-patterns:** 
+  Teams are unaware of system or default timeout values. 
+  Teams do not know the normal completion time of the requests they make. 
+  Teams do not consider why a request might take abnormally long, or the cost of waiting on it. 
+  Timeout scenarios are not tested for connections or requests. 
+  Timeouts set too high cause long waits and hold resources while the client waits. 
+  Timeouts set too low cause artificial failures and retry-driven traffic increases. 
+  Patterns for handling timeout errors, such as circuit breakers and retries, are overlooked. 
+  Error rates, latency service level objectives, and latency outliers are not monitored, so timeout values cannot be tuned. 

 **Benefits of establishing this best practice:** 
+  Resources are conserved when remote calls respond abnormally slowly, because timeouts release them promptly. 
+  Timeout errors are handled gracefully by clients instead of stalling the workload. 
+  Timeout values can be tuned over time, because monitoring reveals whether they are too aggressive or too permissive. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A timeout shorter than a request's normal completion time manufactures failures out of requests that would have succeeded. The resulting retries add load to the backend and latency to the client, and at worst every slow response becomes a retry and overloads the backend. 

 The right timeout depends on why a request is slow. When a request is expensive by design, time it out without retry to preserve resources on both sides. A localized service impairment usually calls for a timeout followed by a retry, which is cheap and conserves client resources. If the network fails to deliver the request or response, the call fails regardless, so an early timeout releases client resources at no cost. 

 A *circuit breaker* stops issuing calls to a dependency that is timing out and tests periodically for recovery. Retries with exponential backoff and jitter handle transient failures. Together, timeouts, circuit breakers, and bounded retries complement fail-fast. 

 Use the [AWS SDKs](https://docs.aws.amazon.com/) and [AWS CLI](https://aws.amazon.com/cli/) to configure connection and request timeouts alongside retries with backoff and jitter. [AWS Lambda](https://aws.amazon.com/lambda/) functions have a configurable timeout, and [AWS Step Functions](https://aws.amazon.com/step-functions/) provides pre-built service integrations for low-code circuit breakers. For container workloads, [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) provides timeout and retry controls at the service network level. Whichever you use, instrument error rates and latency outliers to tune timeouts over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set connection and request timeouts on remote calls:** Configure both timeout types on every call across a process boundary, using built-in language timeout features or an open-source timeout library. Base the values on measured normal completion times, not defaults. 

1.  **Configure AWS SDK timeouts per language:** When your workload calls an AWS SDK, review the language-specific timeout configuration for [Python](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html), [PHP](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.DefaultsMode.Configuration.html), [.NET](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/retries-timeouts.html), [Ruby](https://docs.aws.amazon.com/sdk-for-ruby/v3/developer-guide/), [Java](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices.html#bestpractice5), [Go](https://docs.aws.amazon.com/sdk-for-go/v2/developer-guide/configure-retries-timeouts.html), [Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/), and [C\+\+](https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/client-config.html). 

1.  **Set SDK and CLI default timeout values:** For AWS SDK and AWS CLI usage, set [configuration defaults](https://docs.aws.amazon.com/sdkref/latest/guide/feature-smart-config-defaults.html) for connectTimeoutInMillis and tlsNegotiationTimeoutInMillis. Apply the [command line options](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html) cli-connect-timeout and cli-read-timeout for one-off CLI commands. 

1.  **Configure timeouts on compute and integration services:** Set timeouts on [Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html#configuration-timeout-console). Account for the API Gateway [50-millisecond to 29-second integration timeout](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html#api-gateway-execution-service-limits-table), and implement client retries because API Gateway does not retry a timed-out integration. 

1.  **Monitor timeouts and tune values:** Set alarms on persistent timeout errors, and use [CloudWatch metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/working_with_metrics.html) and [CloudWatch anomaly detection](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.html) on error rates, latency service level objectives, and latency outliers to tune overly aggressive or permissive timeouts. 

1.  **Implement circuit breakers for timing-out calls:** Apply the [circuit breaker](https://martinfowler.com/bliki/CircuitBreaker.html) pattern to avoid calling a dependency that is timing out, opening the circuit during failures and closing it when calls respond normally. Build low-code circuit breakers with [AWS Step Functions](https://aws.amazon.com/step-functions/), or use [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) timeout and retry features for container and service workloads. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL05-BP01 Implement graceful degradation to transform applicable hard dependencies into soft dependencies](rel05-bp01.md) 
+  [REL06-BP07 Monitor end-to-end tracing of requests through your system](rel06-bp07.md) 

 **Related documents:** 
+  [Retries and timeouts - AWS SDK for .NET (V3)](https://docs.aws.amazon.com/sdk-for-net/v3/developer-guide/retries-timeouts.html) 
+  [The Amazon Builders' Library: Timeouts, retries, and backoff with jitter](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter) 
+  [Amazon API Gateway quotas](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html) 
+  [Command line options in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-options.html) 
+  [Best practices for using the AWS SDK for Java 2.x - AWS SDK for Java 2.x](https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/best-practices.html#bestpractice5) 
+  [Configuration - Boto3 1.43.92 documentation](https://docs.aws.amazon.com/boto3/latest/guide/configuration.html#using-the-config-object) 
+  [Configuring AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/lambda-functions.html) 

 **Related examples:** 
+  [Using the circuit breaker pattern with AWS Step Functions and Amazon DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/) 
+  [Circuit Breaker](https://martinfowler.com/bliki/CircuitBreaker.html?ref=wellarchitected) 

 **Related tools:** 
+  [AWS SDKs](https://docs.aws.amazon.com/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 
+  [AWS Command Line Interface](https://aws.amazon.com/cli/) 


# SUS03-BP02 Flatten demand peaks for consistently high resource utilization

 When demand is unpredictable and spiky, provision enough capacity to meet peak loads. Techniques such as buffering and throttling smooth out the load and maintain a consistently high level of resource utilization, reducing the need for excess capacity to handle peaks and improving overall efficiency. By transforming spiky workload patterns into steadier, more predictable ones, you can provision resources that operate at high utilization and resource efficiency levels most of the time. 

 **Desired outcome:** 
+  You smooth demand patterns so your workload runs efficiently on more consistently utilized infrastructure, reducing the excess capacity that sits idle during normal operations. 
+  You achieve higher average resource utilization and a smaller environmental footprint. 

 **Common anti-patterns:** 
+  Provisioning for peak demand without effective mechanisms to smooth demand. 
+  Processing non-urgent workloads or operations immediately, even when non-functional requirements allow time for buffering. 
+  Provisioning infrastructure for peak load that rarely or never occurs. 
+  Not scaling in or down at times of low demand. 
+  Failing to define limits or implement mechanisms for throttling traffic spikes. 

 **Benefits of establishing this best practice:** 
+  Minimizing idle or underutilized resources to handle the demand lowers the required share on hardware related impacts, from raw material extraction to end of life treatment (Scope 3 emissions). 
+  High utilization of resources reduces the effect of energy overhead spent for operating the infrastructure (Scope 2 emissions). 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing mechanisms to flatten demand peaks requires understanding your workload patterns and applying appropriate techniques to smooth out spikes. This may involve adding queuing mechanisms, buffering, throttling, or redesigning processes to operate in batches during periods of lower demand. 

### Implementation steps
<a name="implementation-steps"></a>

1.  Analyze your workload demand patterns: 
   +  Use [Amazon CloudWatch metrics](https://aws.amazon.com/cloudwatch/) to identify peak periods and their frequency. 
   +  Categorize workload components based on their time-sensitivity requirements. 
   +  Identify opportunities to defer or batch non-critical processing. 
   +  Continuously evaluate the balance between responsiveness and resource efficiency. 
   +  Consider adding caching when receiving consistently high volumes of identical incoming requests that can be serviced with the same response. 

1.  Implement queuing and buffering for asynchronous workloads: 
   +  Use [Amazon SQS](https://aws.amazon.com/sqs/) to decouple components and buffer workload. 
   +  Implement auto-scaling based on queue depth using metric math. 
   +  Implement [Amazon Kinesis](https://aws.amazon.com/kinesis/) with micro-buffering for real-time data streaming with controlled processing. 
   +  Configure appropriate processing rates and concurrency limits for consumers. 

1.  Apply throttling for request-heavy APIs and services: 
   +  Configure [API Gateway](https://aws.amazon.com/api-gateway/) throttling to limit request rates. 
   +  Implement client-side retry mechanisms and leverage the AWS SDKs implementation of exponential backoff and jitter. 
   +  Consider different throttling limits for different client types or operations. 
   +  Use circuit breakers to turn off non-critical features and protect the systems and user experience in periods of high demand. 

1.  Monitor and optimize your flattening mechanisms: 
   +  Monitor performance metrics such as queue depth, processing latency, and throttling events. 
   +  Set thresholds on performance metrics to detect exceptions, and drive automated scaling actions when necessary to maintain SLOs. 
   +  Regularly review and adjust buffer sizes, processing rates, and throttling limits as needed. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SUS02-BP01 Implement elasticity for variable workloads](sus02-bp01.md) 
+  [SUS02-BP03 Match resource use to business need](sus02-bp03.md) 
+  [SUS03-BP01 Optimize workloads for high resource usage efficiency](sus03-bp01.md) 
+  [SUS04-BP03 Implement distributed systems appropriately](sus04-bp03.md) 
+  [COST09-BP02 Continuously review and optimize the workload](cost09-bp02.md) 

 **Related documents:** 
+  [What is Amazon Simple Queue Service?](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) 
+  [Throttle requests to your REST APIs for better throughput in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) 
+  [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) 
+  [Circuit breaker pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/cloud-design-patterns/circuit-breaker.html) 
+  [Resilience lessons from the lunch rush](https://builder.aws.com/content/3Ev17ZWA9QX88MmoaULAKevIR8H/resilience-lessons-from-the-lunch-rush) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Integration patterns for distributed systems (API315)](https://www.youtube.com/watch?v=xc9P6wbhLwE) 
+  [AWS re:Invent 2024 - Try again: The tools and techniques behind resilient systems (ARC403)](https://www.youtube.com/watch?v=rvHd4Y76-fs) 

 **Related examples:** 
+  [Using the circuit breaker pattern with AWS Step Functions and Amazon DynamoDB](https://aws.amazon.com/blogs/compute/using-the-circuit-breaker-pattern-with-aws-step-functions-and-amazon-dynamodb/) 
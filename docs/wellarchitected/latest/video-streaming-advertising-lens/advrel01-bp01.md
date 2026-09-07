

# ADVREL01-BP01 Use loosely-coupled architectures to enable graceful recovery from failures
<a name="advrel01-bp01"></a>

 Use architecture patterns like service-oriented architecture (SOA), microservices, and event-driven architecture (EDA) to recover quickly and efficiently from failure. These architectural patterns enable robust failure recovery through loosely coupled designs and enhance system resilience and component self-sufficiency. 

## Implementation guidance
<a name="implementation-guidance-15"></a>

 Highly scalable and reliable workloads necessitate reusable software components that are accessible through service interfaces like APIs. Microservices take this a step further by breaking down components into smaller, simpler units. EDAs build upon and enhance microservices with an event broker, fostering greater efficiency. 

 Implement EDAs using services like [Amazon EventBridge](https://aws.amazon.com/eventbridge/) and [Amazon Simple Notification Service (SNS)](https://aws.amazon.com/sns/) to decouple components and enable asynchronous communication. This can improve resilience by reducing hard coded dependencies and enabling retries and error handling. 

 Make sure that the data pipelines of the advertising system operate reliably despite unexpected failures, packet loss, or high latency. Design interactions between components in your distributed advertising system in such way that their failure makes minimal impact. 

## Key AWS services
<a name="key-aws-services-2"></a>
+  [Amazon Simple Queue Service (SQS)](https://aws.amazon.com/sqs/) 
+  [AWS Step Functions](https://aws.amazon.com/step-functions/) 

## Resources
<a name="resources-10"></a>
+  [What is EDA? - Event Driven Architecture Explained - AWS](https://aws.amazon.com/what-is/eda/index.html) 
+  [Avoiding insurmountable queue backlogs](https://aws.amazon.com/builders-library/avoiding-insurmountable-queue-backlogs/) 
+  [How can I prevent an increasing backlog of messages in my Amazon SQS queue?](https://repost.aws/knowledge-center/sqs-message-backlog) 
+  [Amazon Simple Notification Service (SNS) \| AWS News Blog](https://aws.amazon.com/blogs/aws/category/messaging/amazon-simple-notification-service-sns/index.html) 
+  [Increasing MTBF - Availability and Beyond: Understanding and Improving the Resilience of Distributed Systems on AWS](https://docs.aws.amazon.com/whitepapers/latest/availability-and-beyond-improving-resilience/increasing-mtbf.html) 


# ADVREL02-BP03 Prevent scale mismatch of both internal services and external partners
<a name="advrel02-bp03"></a>

 It's important to implement proportional scaling across all system components in advertising workloads. Balance service capacities, particularly in DSP to SSP integrations, and use pub/sub patterns to reliably distribute load and prevent service overload in microservices architectures. 

## Implementation guidance
<a name="implementation-guidance-21"></a>

 Providing reliability is paramount for advertising workloads, which can be achieved by proportionally scaling all sub-components. For instance, when you integrate using a PrivateLink between DSP and SSP, your partner's requests may overwhelm your API front-end services, leading to throttling. To mitigate this when using a microservices architecture, the smaller services should drive larger capacity services, preventing them from being overwhelmed. The pub/sub pattern should also be followed wherever possible to enhance reliability through decoupled communication and load distribution across multiple subscribers. By implementing these measures, advertising workloads can maintain high availability and fault tolerance, providing a seamless and reliable experience for all stakeholders. 

## Key AWS services
<a name="key-aws-services-7"></a>
+  [Amazon API Gateway](https://aws.amazon.com/api-gateway/) 
+  [Amazon SQS](https://aws.amazon.com/sqs/) 
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/) 
+  [AWS Lambda](https://aws.amazon.com/lambda/) 

## Resources
<a name="resources-16"></a>
+  [Avoiding overload in distributed systems by putting smaller service in control](https://aws.amazon.com/builders-library/avoiding-overload-in-distributed-systems-by-putting-the-smaller-service-in-control/) 
+  [Pub/sub pattern](https://docs.aws.amazon.com/prescriptive-guidance/latest/modernization-integrating-microservices/pub-sub.html) 
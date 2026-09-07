

# ADVPERF05-BP04 Provide dedicated network connection between your on-premises environment and AWS to offer high bandwidth and low latency
<a name="advperf05-bp04"></a>

 Use dedicated network connections to provide stable and high-speed data communication between the on-premises data center and the AWS Cloud. This model is also applicable for connections between multiple Regions, providing efficient and secure data communication while effectively avoiding public network noise. 

## Implementation guidance
<a name="implementation-guidance-54"></a>

 For workloads that require high throughput or have strict compliance requirements, consider implementing [AWS Direct Connect](https://aws.amazon.com/directconnect/). AWS Direct Connect provides a dedicated network connection between your on-premises environment and AWS, offering high bandwidth, low latency, and enhanced security by bypassing the public internet. 

## Key AWS services
<a name="key-aws-services-30"></a>
+  [AWS PrivateLink](https://aws.amazon.com/privatelink/) 

## Resources
<a name="resources-49"></a>
+  [AWS Direct Connect Resiliency Recommendations](https://aws.amazon.com/directconnect/resiliency-recommendation/) 
+  [Compliance validation for AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/DirectConnect-compliance.html) 
+  [Using the AWS Direct Connect Resiliency Toolkit to get started](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_toolkit.html) 
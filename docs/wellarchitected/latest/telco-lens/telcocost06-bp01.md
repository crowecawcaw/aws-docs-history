

# TELCOCOST06-BP01 Implement load-balancing techniques to achieve better utilization of hybrid network resources

 Establish a comprehensive traffic classification system that identifies different types of network traffic (for example, real-time communications, bulk data transfers, best-effort traffic). Monitor the utilization of your hybrid network connections in real time. Use load-balancing mechanisms to distribute network traffic across multiple hybrid network connections, both on-premises and in the cloud. 

 **Desired outcome:** 
+  Optimize the utilization of networking resources across your hybrid infrastructure. 
+  Verify critical network traffic is prioritized and routed efficiently. 
+  Improve overall network performance and cost-effectiveness. 

 **Common anti-patterns:** 
+  Static routing configurations that don't adapt to changing network conditions. 
+  Lack of visibility into network traffic patterns and resource utilization. 
+  Inability to dynamically adjust traffic flows based on real-time performance metrics. 

 **Benefits of establishing this best practice:** 
+  Improved networking resource utilization and cost-effectiveness. 
+  Enhanced performance and reliability for latency-sensitive network traffic. 
+  Increased agility in managing network capacity and traffic flows. 
+  Better alignment of network capabilities with evolving business requirements. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Implementing effective load-balancing techniques across your hybrid networking infrastructure is crucial for optimizing resource utilization and cost-effectiveness. By leveraging advanced load-balancing capabilities, you can intelligently route network traffic based on real-time conditions, prioritize critical applications and services, and verify efficient use of your networking resources. 

 AWS provides various load-balancing services, such as Network Load Balancer and Application Load Balancer, that can assist you to distribute traffic across your hybrid network connections, both on-premises and in the cloud. These load balancers can use dynamic routing algorithms to route traffic based on performance metrics like latency, jitter, and packet loss, verifying that traffic is directed to the most optimal path. 

 Additionally, AWS Global Accelerator can improve the availability and performance of users' voice traffic by routing it over the AWS global network to the closest healthy endpoint. Global Accelerator adds its own fixed fee and a per-GB data transfer premium on top of standard data transfer charges, so evaluate it as a performance investment rather than a way to reduce data transfer costs. 

### Implementation steps
<a name="implementation-steps"></a>
+  Establish a comprehensive traffic classification system that identifies different types of network traffic (for example, real-time communications, bulk data transfers, best-effort traffic). 
+  Deploy Network Load Balancer or Application Load Balancer to distribute voice traffic across your hybrid network connections, both on-premises and in the cloud. 
+  Configure the load balancers to use dynamic routing based on network metrics, such as latency, jitter, and packet loss, to intelligently route traffic. 
+  Use AWS Global Accelerator where users need improved availability and performance for voice traffic, and account for its fixed fee and data transfer premium in your cost model. 
+  Monitor the utilization of your hybrid network connections in real time using Amazon CloudWatch and set up alarms to trigger load-balancing adjustments. 
+  Continuously review and refine your load-balancing policies to maintain optimal utilization of your hybrid network resources. 

## Resources
<a name="resources"></a>

 **Key AWS services:** 
+  [AWS Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) 
+  [AWS Application Load Balancer](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/) 
+  [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
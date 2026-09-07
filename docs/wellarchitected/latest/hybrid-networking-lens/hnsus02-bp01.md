

# HNSUS02-BP01 Prioritize critical components
<a name="hnsus02-bp01"></a>

 Break down your workload into individual components (for example, microservices, databases, and APIs). Use metrics like CPU utilization, request rates, and business impact to classify them as critical or non-critical. 

 **Desired outcome:** Resource allocation aligned with business value, minimizing waste in low-impact areas. 

 **Level of risk exposed if this best practice is not established:** Medium 

 **Benefits of establishing this best practice:** 
+  Focuses optimization efforts on high-impact components 
+  Reduces energy consumption 
+  Maintains performance for mission-critical workloads 

## Implementation guidance
<a name="implementation-guidance-61"></a>
+  Map component dependencies and usage. For example, you can achieve this using AWS X-Ray. 
+  Apply tags to categorize components (for example, business-critical, dev-test). 
+  Right-size your resources during off-peak hours. For example, you can achieve this using AWS Auto Scaling. 

## Resources
<a name="resources-50"></a>
+  [AWS X-Ray: Service Map Analysis](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html) 
+  [Best Practices for Tagging AWS Resources](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/what-are-tags.html) 
+  [AWS Auto Scaling - application scaling](https://aws.amazon.com/autoscaling/) 
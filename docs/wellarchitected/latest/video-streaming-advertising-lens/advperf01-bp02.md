

# ADVPERF01-BP02 Use appropriate scaling to handle burst traffic with cost considerations
<a name="advperf01-bp02"></a>

 Consider start-up latency and scaling needs to handle burst traffic for networking, compute, and storage resources. 

## Implementation guidance
<a name="implementation-guidance-35"></a>

 Network Load Balancer (NLB) and Application Load Balancer (ALB) scaling parameters depend upon the following parameters: 
+  Overall number of long-lived connections 
+  New TCP/TLS connections per second expected 
+  Data transfer in GB per second expected 

 NLB scaling needs are driven by elastic network interface at the Availability Zone level, whereas ALB scales across Availability Zones. 

 Consider Load balancer Capacity Unit (LCU) reservation, which you can use to proactively set a minimum capacity for your load balancer. This capability complements the load balancer's existing ability to auto scale based on your traffic pattern. Implement load balancers with target groups (like Auto Scaling groups). 

 For container workloads running on Amazon EKS, implement EKS Auto Scaling: 
+  Set up horizontal scaling and node scaling using either Cluster Autoscaler or Karpenter 
+  Set up pod scaling using horizontal pod scaling 

 Integrate with default Kubernetes metrics (like CPU and memory) or extensive metrics (inputs like queue lengths, CPU usage, and business metrics) using [Kubernetes Event-driven Autoscaling (KEDA)](https://keda.sh/). 

 For databases like Amazon Aurora, enable storage auto scaling, which is a managed solution for storage expansion. 

## Key AWS services
<a name="key-aws-services-21"></a>
+  [Amazon Network Load Balancer (NLB) ](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) 
+  [Amazon Elastic Load Balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/) 
+  [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) 
+  [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/) 
+  [Amazon Aurora](https://aws.amazon.com/rds/aurora/) 

## Resources
<a name="resources-30"></a>
+  [Auto Scaling benefits for application architecture](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html) 
+  [Load Balancer Capacity Unit Reservation for Application and Network Load Balancers](https://aws.amazon.com/about-aws/whats-new/2024/11/load-balancer-capacity-unit-reservation-application-balancers/) 
+  [Autoscaling Amazon EKS services based on custom Prometheus metrics using CloudWatch Container Insights](https://aws.amazon.com/blogs/containers/autoscaling-amazon-eks-services-based-on-custom-prometheus-metrics-using-cloudwatch-container-insights/) 
+  [Autoscaling Amazon ECS services based on custom metrics with Application Auto Scaling](https://aws.amazon.com/blogs/containers/autoscaling-amazon-ecs-services-based-on-custom-metrics-with-application-auto-scaling/) 
+  [How ktown4u built a custom auto scaling architecture using an Amazon Aurora mixed-configuration cluster to respond to sudden traffic spikes](https://aws.amazon.com/blogs/database/how-ktown4u-built-a-custom-auto-scaling-architecture-using-an-amazon-aurora-mixed-configuration-cluster-to-respond-to-sudden-traffic-spikes/) 


# ADVREL03-BP01 Use a full Regional deployment for compute resources through Auto Scaling groups and compute container orchestrators
<a name="advrel03-bp01"></a>

 Deploy compute resources across multiple Availability Zones (AZs) and Regions to enhance application resilience. Implement zone-aware architectures to optimize performance and manage costs, and focus on intra-AZ communication and load balancing configurations. 

## Implementation guidance
<a name="implementation-guidance-22"></a>

 Increase resiliency of real-time advertising applications by distributing resources across multiple Availability Zones or Regions, but maintain awareness of cross-AZ and cross-Region data transfer costs. When you use a full Regional deployment, implement zone-aware architectures within each Region to optimize performance and costs. When distributing resources across multiple Availability Zones for resilience, implement logic to prefer intra-AZ communication, when possible, and use features like AZ-aware load balancing to minimize cross-AZ traffic. By being zone-aware, companies can reduce costs and improve performance even when they need to operate in multiple Regions. 

## Key AWS services
<a name="key-aws-services-8"></a>
+  [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) groups can be configured to span multiple AZs 
+  [Amazon Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) clusters can also be deployed across multiple AZs 

## Resources
<a name="resources-17"></a>
+  [Regions and Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) 
+  [Distribute instances across Availability Zones](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#arch-AutoScalingMultiAZ)  
+  [EC2 Instance Meta-Data Retrieval](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html) 
+  [Creating Kubernetes Auto Scaling Groups for Multiple Availability Zones \| Containers ](https://aws.amazon.com/blogs/containers/amazon-eks-cluster-multi-zone-auto-scaling-groups/index.html) 
+  [Add an Availability Zone - Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html) 
+  [Simplify node lifecycle with managed node groups - Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html) 
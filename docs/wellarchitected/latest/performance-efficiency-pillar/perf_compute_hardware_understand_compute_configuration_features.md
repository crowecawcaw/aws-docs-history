

# PERF02-BP02 Understand the available compute configuration and features
<a name="perf_compute_hardware_understand_compute_configuration_features"></a>

 Understand the available configuration options and features for your compute service to help you provision the right amount of resources and improve performance efficiency. 

 **Common anti-patterns:** 
+  You do not evaluate compute options or available instance families against workload characteristics. 
+  You over-provision compute resources to meet peak-demand requirements. 

** Benefits of establishing this best practice:** Be familiar with AWS compute features and configurations so that you can use a compute solution optimized to meet your workload characteristics and needs.

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Each compute solution has unique configurations and features available to support different workload characteristics and requirements. Learn how these options complement your workload, and determine which configuration options are best for your application. Examples of these options include instance family, sizes, features (GPU, I/O), bursting, time-outs, function sizes, container instances, and concurrency. If your workload has been using the same compute option for more than four weeks and you anticipate that the characteristics will remain the same in the future, you can use [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/)  to find out if your current compute option is suitable for the workloads from CPU and memory perspective. 

## Implementation steps
<a name="implementation-steps"></a>
+  Understand workload requirements (like CPU need, memory, and latency). 
+  Review AWS documentation and best practices to learn about recommended configuration options that can help improve compute performance. Here are some key configuration options to consider: 


<table>
<thead>
  <tr><th> Configuration option </th><th> Examples </th></tr>
</thead>
<tbody>
  <tr><td> Instance type </td><td> <ul><li>  <a href="https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&amp;sc_channel=ps&amp;sc_campaign=acquisition&amp;sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&amp;ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Compute_Optimized">Compute-optimized</a> instances are ideal for the workloads that require high higher vCPU to memory ratio.   </li><li>  <a href="https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&amp;sc_channel=ps&amp;sc_campaign=acquisition&amp;sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&amp;ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Memory_Optimized">Memory-optimized</a> instances deliver large amounts of memory to support memory intensive workloads.  </li><li>  <a href="https://aws.amazon.com/ec2/instance-types/?trk=36c6da98-7b20-48fa-8225-4784bced9843&amp;sc_channel=ps&amp;sc_campaign=acquisition&amp;sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Compute|EC2|US|EN|Text&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types&amp;ef_id=CjwKCAjwiuuRBhBvEiwAFXKaNNRXM5FrnFg5H8RGQ4bQKuUuK1rYWmU2iH-5H3VZPqEheB-pEm-GNBoCdD0QAvD_BwE:G:s&amp;s_kwcid=AL!4422!3!536392622533!e!!g!!ec2%20instance%20types#Storage_Optimized">Storage-optimized</a> instances are designed for workloads that require high, sequential read and write access (IOPS) to local storage.  </li></ul> </td></tr>
  <tr><td> Pricing model </td><td> <ul><li>  <a href="https://aws.amazon.com/ec2/pricing/on-demand/">On-Demand Instances</a> let you use the compute capacity by the hour or second with no long-term commitment. These instances are good for bursting above performance baseline needs.  </li><li>  <a href="https://aws.amazon.com/savingsplans/">Savings Plans</a> offer significant savings over On-Demand Instances in exchange for a commitment to use a specific amount of compute power for a one or three-year period.  </li><li>  <a href="https://aws.amazon.com/ec2/spot/">Spot Instances</a> let you take advantage of unused instance capacity at a discount for your stateless, fault-tolerant workloads.   </li></ul> </td></tr>
  <tr><td>Auto Scaling</td><td> Use <a href="https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/capacity-autoscaling.html">Auto Scaling</a> configuration to match compute resources to traffic patterns. </td></tr>
  <tr><td> Sizing </td><td> <ul><li>  Use <a href="https://aws.amazon.com/compute-optimizer/">Compute Optimizer</a> to get a machine-learning powered recommendations on which compute configuration best matches your compute characteristics.  </li><li>  Use <a href="https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html">AWS Lambda Power Tuning</a> to select the best configuration for your Lambda function.  </li></ul> </td></tr>
  <tr><td> Hardware-based compute accelerators </td><td> <ul><li>  <a href="https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/accelerated-computing-instances.html">Accelerated computing instances</a> perform functions like graphics processing or data pattern matching more efficiently than CPU-based alternatives.  </li><li>  For machine learning workloads, take advantage of purpose-built hardware that is specific to your workload, such as <a href="https://aws.amazon.com/machine-learning/trainium/">AWS Trainium</a>, <a href="https://aws.amazon.com/machine-learning/inferentia/">AWS Inferentia</a>, and <a href="https://aws.amazon.com/ec2/instance-types/dl1/">Amazon EC2 DL1</a>  </li></ul> </td></tr>
</tbody>
</table>


## Resources
<a name="resources"></a>

 **Related documents:** 
+  [Cloud Compute with AWS ](https://aws.amazon.com/products/compute/?ref=wellarchitected) 
+  [Amazon EC2 Instance Types ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html?ref=wellarchitected) 
+  [Processor State Control for Your Amazon EC2 Instance ](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/processor_state_control.html?ref=wellarchitected) 
+  [Amazon EKS Containers: Amazon EKS Worker Nodes ](https://docs.aws.amazon.com/eks/latest/userguide/worker.html?ref=wellarchitected) 
+  [Amazon ECS Containers: Amazon ECS Container Instances ](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ECS_instances.html?ref=wellarchitected) 
+  [Functions: Lambda Function Configuration](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html?ref=wellarchitected#function-configuration) 

 **Related videos:** 
+  [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4) 
+  [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA) 
+  [AWS re:Invent 2023 – What's new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g) 
+  [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0) 
+  [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU) 
+  [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0) 
+  [AWS re:Invent 2022 – Optimizing Amazon EKS for performance and cost on AWS](https://www.youtube.com/watch?v=5B4-s_ivn1o) 

 **Related examples:** 
+  [Compute Optimizer demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer) 
+  [Amazon EC2 spot instances workshop](https://ec2spotworkshops.com/) 
+  [Efficient and Resilient Workloads with Amazon EC2 AWS Auto Scaling](https://catalog.us-east-1.prod.workshops.aws/workshops/20c57d32-162e-4ad5-86a6-dff1f8de4b3c/en-US) 
+  [Graviton developer workshop](https://catalog.us-east-1.prod.workshops.aws/workshops/dcab7555-32fc-42d2-97e5-2b7a35cd008f/en-US/) 
+  [AWS for Microsoft workloads immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/d6c7ecdc-c75f-4ad1-910f-fdd994cc4aed/en-US) 
+  [AWS for Linux workloads immersion day](https://catalog.us-east-1.prod.workshops.aws/workshops/a8e9c6a6-0ba9-48a7-a90d-378a440ab8ba/en-US) 
+  [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer) 
+  [Amazon EKS workshop](https://www.eksworkshop.com/) 

  
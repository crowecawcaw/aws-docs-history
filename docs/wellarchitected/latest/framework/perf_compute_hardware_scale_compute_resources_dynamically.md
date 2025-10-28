# PERF02-BP05 Scale your compute resources dynamically

Use the elasticity of the cloud to scale your compute resources up
or down dynamically to match your needs and avoid over- or
under-provisioning capacity for your workload.

**Common anti-patterns:**

- You react to alarms by manually increasing capacity.
- You use the same sizing guidelines (generally static
  infrastructure) as in on-premises.
- You leave increased capacity after a scaling event instead of
  scaling back down.

**Benefits of establishing this best
practice:** Configuring and testing the elasticity of
compute resources can help you save money, maintain performance
benchmarks, and improve reliability as traffic changes.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

AWS provides the flexibility to scale your resources up or down
dynamically through a variety of scaling mechanisms in order to
meet changes in demand. Combined with compute-related metrics, a
dynamic scaling allows workloads to automatically respond to
changes and use the optimal set of compute resources to achieve
its goal.

You can use a number of different approaches to match supply of
resources with demand.

- **Target-tracking approach**: Monitor your scaling metric and
  automatically increase or decrease capacity as you need it.
- **Predictive scaling**: Scale in anticipation of daily and
  weekly trends.
- **Schedule-based approach**: Set your own scaling schedule
  according to predictable load changes.
- **Service scaling**: Choose services (like serverless) that
  that automatically scale by design.

You must ensure that workload deployments can handle both scale-up
and scale-down events.

### Implementation steps

- Compute instances, containers, and functions provide
  mechanisms for elasticity, either in combination with
  autoscaling or as a feature of the service. Here are some
  examples of automatic scaling mechanisms:

| Autoscaling Mechanism
| Where to use
|
| --- | --- |
| [Amazon EC2 Auto Scaling](../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md "../../../autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.md") | To ensure you have the correct number of [Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/") instances available to handle the user load for your application. |
| [Application Auto Scaling](../../../autoscaling/application/userguide/what-is-application-auto-scaling.md "../../../autoscaling/application/userguide/what-is-application-auto-scaling.md") | To automatically scale the resources for individual AWS services beyond Amazon EC2 such as [AWS Lambda](https://aws.amazon.com/lambda/ "https://aws.amazon.com/lambda/") functions or [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/ "https://aws.amazon.com/ecs/") services. |
| [Kubernetes Cluster Autoscaler/Karpenter](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/ "https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/") | To automatically scale Kubernetes clusters. | <br>• Scaling is often discussed related to compute services like Amazon EC2 Instances or AWS Lambda functions. Be sure to also consider the configuration of non-compute services like [AWS Glue](../../../glue/latest/dg/auto-scaling.md "../../../glue/latest/dg/auto-scaling.md") to match the demand. <br>• Verify that the metrics for scaling match the characteristics of the workload being deployed. If you are deploying a video transcoding application, 100% CPU utilization is expected and should not be your primary metric. Use the depth of the transcoding job queue instead. You can use a [customized metric](https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/ "https://aws.amazon.com/blogs/mt/create-amazon-ec2-auto-scaling-policy-memory-utilization-metric-linux/") for your scaling policy if required. To choose the right metrics, consider the following guidance for Amazon EC2: + The metric should be a valid utilization metric and describe how busy an instance is. + The metric value must increase or decrease proportionally to the number of instances in the Auto Scaling group. <br>• Make sure that you use [dynamic scaling](../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md "../../../autoscaling/ec2/userguide/as-scale-based-on-demand.md") instead of [manual scaling](../../../autoscaling/ec2/userguide/as-manual-scaling.md "../../../autoscaling/ec2/userguide/as-manual-scaling.md") for your Auto Scaling group. We also recommend that you use [target tracking scaling policies](../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md "../../../autoscaling/ec2/userguide/as-scaling-target-tracking.md") in your dynamic scaling. <br>• Verify that workload deployments can handle both scaling events (up and down). As an example, you can use [Activity history](../../../autoscaling/ec2/userguide/as-verify-scaling-activity.md "../../../autoscaling/ec2/userguide/as-verify-scaling-activity.md") to verify a scaling activity for an Auto Scaling group. <br>• Evaluate your workload for predictable patterns and proactively scale as you anticipate predicted and planned changes in demand. With predictive scaling, you can eliminate the need to overprovision capacity. For more detail, see [Predictive Scaling with Amazon EC2 Auto Scaling](https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/ "https://aws.amazon.com/blogs/compute/introducing-native-support-for-predictive-scaling-with-amazon-ec2-auto-scaling/"). ## Resources **Related documents:** <br>• [Cloud Compute with AWS](https://aws.amazon.com/products/compute/ "https://aws.amazon.com/products/compute/") <br>• [Amazon EC2 Instance Types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md") <br>• [Amazon ECS Containers: Amazon ECS Container Instances](../../../AmazonECS/latest/developerguide/ECS_instances.md "../../../AmazonECS/latest/developerguide/ECS_instances.md") <br>• [Amazon EKS Containers: Amazon EKS Worker Nodes](../../../eks/latest/userguide/worker.md "../../../eks/latest/userguide/worker.md") <br>• [Functions: Lambda Function Configuration](../../../lambda/latest/dg/best-practices.md#function-configuration "../../../lambda/latest/dg/best-practices.md#function-configuration") <br>• [Processor State Control for Your Amazon EC2 Instance](../../../AWSEC2/latest/UserGuide/processor_state_control.md "../../../AWSEC2/latest/UserGuide/processor_state_control.md") <br>• [Deep Dive on Amazon ECS Cluster Auto Scaling](https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/ "https://aws.amazon.com/blogs/containers/deep-dive-on-amazon-ecs-cluster-auto-scaling/") <br>• [Introducing Karpenter – An Open-Source High-Performance Kubernetes Cluster Autoscaler](https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/ "https://aws.amazon.com/blogs/aws/introducing-karpenter-an-open-source-high-performance-kubernetes-cluster-autoscaler/") **Related videos:** <br>• [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4 "https://www.youtube.com/watch?v=T_hMIjKtSr4") <br>• [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA "https://www.youtube.com/watch?v=sSpJ8tWCEiA") <br>• [AWS re:Invent 2023 – What’s new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g "https://www.youtube.com/watch?v=mjHw_wgJJ5g") <br>• [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0 "https://www.youtube.com/watch?v=_AHPbxzIGV0") <br>• [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU "https://www.youtube.com/watch?v=2uc1vaEsPXU") <br>• [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0 "https://www.youtube.com/watch?v=kMMybKqC2Y0") **Related examples:** <br>• [Amazon EC2 Auto Scaling Group Examples](https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples "https://github.com/aws-samples/amazon-ec2-auto-scaling-group-examples") <br>• [Amazon EKS Workshop](https://www.eksworkshop.com/ "https://www.eksworkshop.com/") <br>• [Scale your Amazon EKS workloads by running on IPv6](https://catalog.us-east-1.prod.workshops.aws/workshops/3b06259f-8e17-4f2f-811a-75c9b06a2807/en-US "https://catalog.us-east-1.prod.workshops.aws/workshops/3b06259f-8e17-4f2f-811a-75c9b06a2807/en-US")

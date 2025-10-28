# PERF02-BP04 Configure and right-size compute resources

Configure and right-size compute resources to match your workload’s
performance requirements and avoid under- or over-utilized
resources.

**Common anti-patterns:**

- You ignore your workload performance requirements resulting in
  over-provisioned or under-provisioned compute resources.
- You only choose the largest or smallest instance available for
  all workloads.
- You only use one instance family for ease of management.
- You ignore recommendations from AWS Cost Explorer or Compute Optimizer for right-sizing.
- You do not re-evaluate the workload for suitability of new
  instance types.
- You certify only a small number of instance configurations for
  your organization.

**Benefits of establishing this best
practice:**
Right-sizing compute resources ensures optimal operation in the
cloud by avoiding over-provisioning and under-provisioning
resources. Properly sizing compute resources typically results in
better performance and enhanced customer experience, while also
lowering cost.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Right-sizing allows organizations to operate their cloud
infrastructure in an efficient and cost-effective manner while
addressing their business needs. Over-provisioning cloud resources
can lead to extra costs, while under-provisioning can result in
poor performance and a negative customer experience. AWS provides
tools such as
[AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") and
[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/") that use historical data to provide
recommendations to right-size your compute resources.

### Implementation steps

- Choose an instance type to best fit your needs:
  - [How
    do I choose the appropriate Amazon EC2 instance type for
    my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/")
  - [Attribute-based
    instance type selection for Amazon EC2 Fleet](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md")
  - [Create
    an Auto Scaling group using attribute-based instance
    type selection](../../../autoscaling/ec2/userguide/create-asg-instance-type-requirements.md "../../../autoscaling/ec2/userguide/create-asg-instance-type-requirements.md")
  - [Optimizing
    your Kubernetes compute costs with Karpenter
    consolidation](https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/ "https://aws.amazon.com/blogs/containers/optimizing-your-kubernetes-compute-costs-with-karpenter-consolidation/")

- Analyze the various performance characteristics of your
  workload and how these characteristics relate to memory,
  network, and CPU usage. Use this data to choose resources
  that best match your workload's profile and performance
  goals.
- Monitor your resource usage using AWS monitoring tools such
  as Amazon CloudWatch.
- Select the right configuration for compute resources.
  - For ephemeral workloads,
    evaluate [instance
    Amazon CloudWatch metrics](../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md "../../../AWSEC2/latest/UserGuide/viewing_metrics_with_cloudwatch.md") such
    as `CPUUtilization` to identify if the instance is
    under-utilized or over-utilized.
  - For stable workloads, check AWS rightsizing tools such
    as AWS Compute Optimizer and AWS Trusted Advisor at
    regular intervals to identify opportunities to optimize
    and right-size the compute resource.

- Test configuration changes in a non-production environment
  before implementing in a live environment.
- Continually re-evaluate new compute offerings and compare
  against your workload’s needs.

## Resources

**Related documents:**

- [Cloud
  Compute with AWS](https://aws.amazon.com/products/compute/ "https://aws.amazon.com/products/compute/")
- [Amazon EC2
  Instance Types](../../../AWSEC2/latest/UserGuide/instance-types.md "../../../AWSEC2/latest/UserGuide/instance-types.md")
- [Amazon ECS
  Containers: Amazon ECS Container Instances](../../../AmazonECS/latest/developerguide/ECS_instances.md "../../../AmazonECS/latest/developerguide/ECS_instances.md")
- [Amazon EKS
  Containers: Amazon EKS Worker Nodes](../../../eks/latest/userguide/worker.md "../../../eks/latest/userguide/worker.md")
- [Functions:
  Lambda Function Configuration](../../../lambda/latest/dg/best-practices.md#function-configuration "../../../lambda/latest/dg/best-practices.md#function-configuration")
- [Processor
  State Control for Your Amazon EC2 Instance](../../../AWSEC2/latest/UserGuide/processor_state_control.md "../../../AWSEC2/latest/UserGuide/processor_state_control.md")

**Related videos:**

- [Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0 "https://www.youtube.com/watch?v=kMMybKqC2Y0")
- [AWS re:Invent 2023 – AWS Graviton: The best price performance for your AWS workloads](https://www.youtube.com/watch?v=T_hMIjKtSr4 "https://www.youtube.com/watch?v=T_hMIjKtSr4")
- [AWS re:Invent 2023 – New Amazon EC2 generative AI capabilities in AWS Management Console](https://www.youtube.com/watch?v=sSpJ8tWCEiA "https://www.youtube.com/watch?v=sSpJ8tWCEiA")
- [AWS re:Invent 2023 – What’s new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g "https://www.youtube.com/watch?v=mjHw_wgJJ5g")
- [AWS re:Invent 2023 – Smart savings: Amazon EC2 cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0 "https://www.youtube.com/watch?v=_AHPbxzIGV0")
- [AWS re:Invent 2021 – Powering next-gen Amazon EC2: Deep dive on the Nitro System](https://www.youtube.com/watch?v=2uc1vaEsPXU "https://www.youtube.com/watch?v=2uc1vaEsPXU")
- [AWS re:Invent 2019 – Amazon EC2 foundations](https://www.youtube.com/watch?v=kMMybKqC2Y0 "https://www.youtube.com/watch?v=kMMybKqC2Y0")

**Related examples:**

- [AWS Compute Optimizer Demo code](https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer "https://github.com/awslabs/ec2-spot-labs/tree/master/aws-compute-optimizer")
- [Amazon EKS workshop](https://www.eksworkshop.com/ "https://www.eksworkshop.com/")
- [Right-sizing recommendations](https://catalog.workshops.aws/well-architected-cost-optimization/en-US/3-cost-effective-resources/40-rightsizing-recommendations-100 "https://catalog.workshops.aws/well-architected-cost-optimization/en-US/3-cost-effective-resources/40-rightsizing-recommendations-100")

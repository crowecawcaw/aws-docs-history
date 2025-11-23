# SUS05-BP01 Use the minimum amount of hardware to meet your

needs

Use the minimum amount of hardware for your workload to efficiently meet your business
needs.

**Common anti-patterns:**

- You do not monitor resource utilization.
- You have resources with a low utilization level in your architecture.
- You do not review the utilization of static hardware to determine if it should be
  resized.
- You do not set hardware utilization goals for your compute infrastructure based on
  business KPIs.

**Benefits of establishing this best practice:** Rightsizing your
cloud resources helps to reduce a workload’s environmental impact, save money, and maintain
performance benchmarks.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Optimally select the total number of hardware required for your workload to improve its
overall efficiency. The AWS Cloud provides the flexibility to expand or reduce the number of
resources dynamically through a variety of mechanisms, such as [AWS Auto Scaling](https://aws.amazon.com/autoscaling/ "https://aws.amazon.com/autoscaling/"), and meet changes in demand. It also provides [APIs and SDKs](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") that allow resources to be
modified with minimal effort. Use these capabilities to make frequent changes to your workload
implementations. Additionally, use rightsizing guidelines from AWS tools to efficiently
operate your cloud resource and meet your business needs.

**Implementation steps**

- **Choose the instances type:** Choose the right instances
  type to best fit your needs. To learn about how to choose Amazon Elastic Compute Cloud instances and use
  mechanisms such as attribute-based instance selection, see the following:
  - [How do
    I choose the appropriate Amazon EC2 instance type for my workload?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-instance-choose-type-for-workload/")
  - [Attribute-based instance type selection for Amazon EC2 Fleet.](../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md "../../../AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.md")
  - [Create
    an Amazon EC2 Auto Scaling group using attribute-based instance type selection.](../../../autoscaling/ec2/userguide/create-asg-instance-type-requirements.md "../../../autoscaling/ec2/userguide/create-asg-instance-type-requirements.md")

- **Scale:** Use small increments to scale variable
  workloads.
- **Use multiple compute purchase options:** Balance
  instance flexibility, scalability, and cost savings with multiple compute purchase
  options.
  - [Amazon EC2 On-Demand Instances](../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md "../../../AWSEC2/latest/UserGuide/ec2-on-demand-instances.md") are best suited for new, stateful, and spiky
    workloads which can’t be instance type, location, or time flexible.
  - [Amazon EC2 Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") are a great way to supplement the other options for
    applications that are fault tolerant and flexible.
  - Leverage [Compute
    Savings Plans](https://aws.amazon.com/savingsplans/compute-pricing/ "https://aws.amazon.com/savingsplans/compute-pricing/") for steady state workloads that allow flexibility if your
    needs (like AZ, Region, instance families, or instance types) change.

- **Use instance and Availability Zone diversity:** Maximize
  application availability and take advantage of excess capacity by diversifying your
  instances and Availability Zones.
- **Rightsize instances:** Use the rightsizing
  recommendations from AWS tools to make adjustments on your workload. For more
  information, see [Optimizing your cost with Rightsizing Recommendations](../../../latest/userguide/ce-rightsizing.md "../../../latest/userguide/ce-rightsizing.md") and [Right
  Sizing: Provisioning Instances to Match Workloads](../../../latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md "../../../latest/cost-optimization-right-sizing/cost-optimization-right-sizing.md")
  - Use rightsizing recommendations in AWS Cost Explorer or [AWS Compute Optimizer](https://aws.amazon.com/compute-optimizer/ "https://aws.amazon.com/compute-optimizer/") to identify rightsizing
    opportunities.

- **Negotiate service-level agreements (SLAs):** Negotiate
  SLAs that permit temporarily reducing capacity while automation deploys replacement
  resources.

## Resources

**Related documents:**

- [Optimizing your AWS Infrastructure for Sustainability, Part I: Compute](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-i-compute/")
- [Attirbute based Instance Type Selection for Amazon EC2 Auto Scaling for Amazon EC2 Fleet](https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/ "https://aws.amazon.com/blogs/aws/new-attribute-based-instance-type-selection-for-ec2-auto-scaling-and-ec2-fleet/")
- [AWS Compute Optimizer Documentation](../../../compute-optimizer/index.md "../../../compute-optimizer/index.md")
- [Operating Lambda:
  Performance optimization](https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/ "https://aws.amazon.com/blogs/compute/operating-lambda-performance-optimization-part-2/")
- [Auto Scaling
  Documentation](../../../autoscaling/index.md "../../../autoscaling/index.md")

**Related videos:**

- [AWS re:Invent 2023 - What's
  new with Amazon EC2](https://www.youtube.com/watch?v=mjHw_wgJJ5g "https://www.youtube.com/watch?v=mjHw_wgJJ5g")
- [AWS re:Invent 2023 - Smart
  savings: Amazon Elastic Compute Cloud cost-optimization strategies](https://www.youtube.com/watch?v=_AHPbxzIGV0 "https://www.youtube.com/watch?v=_AHPbxzIGV0")
- [AWS re:Invent 2022 -
  Optimizing Amazon Elastic Kubernetes Service for performance and cost on AWS](https://www.youtube.com/watch?v=5B4-s_ivn1o "https://www.youtube.com/watch?v=5B4-s_ivn1o")
- [AWS re:Invent 2023 -
  Sustainable compute: reducing costs and carbon emissions with AWS](https://www.youtube.com/watch?v=0Bl1SDU2HxI "https://www.youtube.com/watch?v=0Bl1SDU2HxI")

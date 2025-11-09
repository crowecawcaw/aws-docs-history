# Mobilize

The next step in preparing your workforce and resources to migrate
your enterprise at scale is to break down the
[**mobilize
activities**](../../../prescriptive-guidance/latest/strategy-migration/mobilize-phase.md "../../../prescriptive-guidance/latest/strategy-migration/mobilize-phase.md") into different workstreams. Although
the goal of the mobilize phase is the migration of business
applications, most prescriptive guidance and answers on achieving
your sustainability goals are found here.

| MIG-SUS-03: How do you define and optimize cloud resources during migration so that you become more energy efficient by minimizing idle resources? |
| -------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                    |

As a part of your migration planning, one of the important tasks
is to define the key workload performance matrix based on your
assessment. This plays the significant part in deciding how you
would like to migrate the target workload, instead of
replicating as-is on-premises configuration. Optimizing cloud
resources by removing idle resources helps lower carbon
emissions without compromising business requirements.

## MIG-SUS-BP-3.1: Focus on efficiency across all aspects of infrastructure

For example, during migration, verify that you use only the required resources, instead of trying to match with source on-premises capacity.

This BP applies to the following best practice areas: Alignment to demand

### Implementation guidance

**Suggestion 3.1.1:** Review the on-premises capacity to plan the workload requirements for your target environment.

During migration assessment, define the workload performance metrics for client requests. To optimize cloud resources, take advantage of elasticity in the cloud so you can meet the increasing demand of the migrating workload.

As part of your assessment, review and analyze the following:

- How to respond to the overall demand, rate of change,
  and required response time, which could potentially help
  to minimize the environmental impact. Implement dynamic
  scaling and automation practice aligning to your SLAs to
  remove excess capacity and assign only needed capacity.
- Identify redundancy, underutilization, and potential
  decommission targets, and plan how you can consolidate
  the redundant content, scale down underutilized
  resources, and decommission unused assets.

**Suggestion 3.1.2:** Use proven workflow templates to migrate enterprise applications.

The way you plan your migration can help you identify the automation opportunity to improve the efficiency during migration process. For example:

- You can use
  [Migration
  Hub Orchestrator](../../../migrationhub/latest/ug/gs-orchestrator.md "../../../migrationhub/latest/ug/gs-orchestrator.md") templates to create a
  migration workflow that can be customized to fit your
  unique migration requirements, instead of manually
  performing all the tasks.
- You can leverage services like
  [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") to get started. Control
  Tower helps you set up a multi-account environment and
  automate the creation of AWS accounts with built-in
  governance.

**Suggestion 3.1.3:** Evaluate your migrated workload to consider and configure auto scaling mechanism.

AWS Auto Scaling monitors your applications and automatically adjusts capacity to maintain steady, predictable performance. Define the [metrics](../../../autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.md "../../../autoscaling/ec2/userguide/ec2-auto-scaling-cloudwatch-monitoring.md") that have the most relevance to your application's performance to meet changes in demand, and ensure that workloads can scale down quickly and easily during periods of low user load.

**Suggestion 3.1.4:** Define and update service-level agreements (SLAs).

- Review and optimize your workload service-level
  agreements (SLA) based on your sustainability goals to
  minimize the resources required to support your
  workload, while continuing to meet business needs.
  Consider your SLA requirements as part of your design
  and architecture as well.
- Define and update SLAs of the migrating workload, such
  as:
  - Availability
    or data retention periods, to minimize the number of
    resources required to support your

  workload.
  For more detail, see

  [SUS02-BP02 Align SLAs with sustainability goals](../sustainability-pillar/sus_sus_user_a3.md "../sustainability-pillar/sus_sus_user_a3.md")
  - Power off the workload during non-functional period.
    You can use
    [Instance
    Scheduler on AWS](../../../solutions/latest/instance-scheduler-on-aws/schedules.md "../../../solutions/latest/instance-scheduler-on-aws/schedules.md") to do this, which automates
    the starting and stopping of Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Relational Database Service (Amazon RDS) instances.
  - Identify if use of a messaging component can lead to
    relaxed service-level requirements that can be met
    with fewer resources. Employ batching requests,
    where possible, for optimal use of resources. For
    more detail, see
    [SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs](../sustainability-pillar/sus_sus_software_a2.md "../sustainability-pillar/sus_sus_software_a2.md").

For more detail, see the following:

- [Throttle API requests for better throughput](../../../apigateway/latest/developerguide/api-gateway-request-throttling.md "../../../apigateway/latest/developerguide/api-gateway-request-throttling.md")
- [Working with Service auto scaling](../../../AmazonECS/latest/developerguide/service-auto-scaling.md "../../../AmazonECS/latest/developerguide/service-auto-scaling.md")
- [AWS Summit SF 2022 - Optimizing your AWS infrastructure for sustainability](https://www.youtube.com/watch?v=9WJv2re6hlE "https://www.youtube.com/watch?v=9WJv2re6hlE")
- [Capacity management made easy with Amazon EC2 Auto Scaling](https://www.youtube.com/watch?v=9BlsFNBnKHc "https://www.youtube.com/watch?v=9BlsFNBnKHc")
- [Architecting sustainably and reducing your AWS carbon footprint](https://www.youtube.com/watch?v=jsbamOLpCr8 "https://www.youtube.com/watch?v=jsbamOLpCr8")

| MIG-SUS-04: Do you consider sustainability when selecting and prioritizing applications for migration and modernization? |
| ------------------------------------------------------------------------------------------------------------------------ |
|                                                                                                                          |

Have sustainability in mind when deciding which applications to
migrate and modernize. To do this, first identify metrics that
can act as a stand-in for your application's sustainability.
Then, use these metrics to initiate migration and modernization
projects that improve the application's sustainability.

## MIG-SUS-BP-4.1: Adopt metrics that can signal the sustainability of your application

This BP applies to the following best practice areas: Process and culture

Adopt metrics to understand what you have provisioned and how those resources are consumed. Evaluate potential improvements, and estimate their potential impact, the cost to implement, and the associated risks. Measure improvements over time to study trends and the impacts of any migration and modernization initiatives.

### Implementation guidance

**Suggestion 4.1.1:** Adopt [sustainability metrics](../sustainability-pillar/evaluate-specific-improvements.md "../sustainability-pillar/evaluate-specific-improvements.md") relevant to the application.

Understand the resources provisioned by your application to complete a unit of work. Leverage monitoring tools to define [proxy metrics](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/"), business metrics, and sustainability key performance indicators (KPI) for your workloads. Documenting sustainability impact over time, including after migration and modernization, enables iterative improvement of your application over time.

You can also add other sustainability attributes that signal the efficiency of your application. An example of this is the version of your operating systems, runtimes, middleware, libraries, and applications. Keeping your workloads up-to-date can improve workload efficiency, and capturing this information keeps stakeholder informed. Another example of this is an indicator to note if you are using Graviton-based instances improve the performance efficiency of your application. For more detail, see [AWS Well-Architected Framework - Sustainability Pillar](../sustainability-pillar/sustainability-pillar.md "../sustainability-pillar/sustainability-pillar.md").

For more detail, see

[Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/").

**Suggestion 4.1.2:** Introduce organizational dashboards to share sustainability metrics with stakeholders.

Leverage automation to report, visualize, and enforce sustainability metrics for your application. Introduce organizational dashboards for sustainability that can be shared with application owners and other stakeholders, including key organizational functions such as a Cloud Center of Excellence (CCoE) and Application Review Board (ARB). Make sustainability metrics a part of your architectural decisions.

## MIG-SUS-BP-4.2: Include sustainability metrics in the application portfolio analysis to drive migration and modernization initiatives

This BP applies to the following best practice areas: Process and culture

Include sustainability metrics when scoping and prioritizing applications for migrations. Sustainability may be excluded if alignment from migration goals and organizational goals is missing.

### Implementation guidance

**Suggestion 4.2.1:** Include sustainability metrics in the application portfolio analysis.

Establish a [sustainability improvement process](../sustainability-pillar/improvement-process.md "../sustainability-pillar/improvement-process.md") and adopt methods that can rapidly [introduce sustainability improvements](../sustainability-pillar/sus_sus_dev_a2.md "../sustainability-pillar/sus_sus_dev_a2.md") and [keep your workloads up-to-date](../sustainability-pillar/sus_sus_dev_a3.md "../sustainability-pillar/sus_sus_dev_a3.md").

Including sustainability metrics in the application portfolio analysis assures that relevant data is captured early and is included in architecture and implementation considerations. These metrics capture the business and technical value of retiring applications, and prioritize rightsizing and application scaling to meet infrequent demand.

| MIG-SUS-05: How do you implement efficient workload design to support your sustainability goals? |
| ------------------------------------------------------------------------------------------------ |
|                                                                                                  |

Compute and storage services make up the foundation of many
customers, which brings great potential for workload design
consideration that can improve the energy efficiency of the
migrating workload.

## MIG-SUS-BP-5.1: Implement efficient workload design by leveraging the underlying infrastructure.

For example, right-size the workload for the target state before migrating to minimize idle resources, and to avoid over provisioned capacity.
This BP applies to the following best practice areas: Hardware and services

### Implementation guidance

**Suggestion 5.1.1:** Select the most efficient hardware and services for your workload migration.

Amazon EC2 provides a wide selection of [instance types](https://aws.amazon.com/ec2/instance-types/ "https://aws.amazon.com/ec2/instance-types/") optimized to fit different use cases. Instance types comprise varying combinations of CPU, memory, storage, and networking capacity and give you the flexibility to choose the [appropriate mix of resources](../sustainability-pillar/sus_sus_hardware_a3.md "../sustainability-pillar/sus_sus_hardware_a3.md") for your applications. For example, Graviton3 provides up to 60% less energy for the same performance as non-Graviton EC2 instances.

**Suggestion 5.1.2:** Gain insight into workload performance.

Gain insight into workload performance metrics like CPU utilization, memory utilization, network utilization, and disk and usage patterns to perform the right alignment of the cloud resource.

- Key matrices to consider are the following:
  - If the workload is idle for a long time, it's a good
    sign to investigate if this workload can retire
    instead of migrating it.
  - Understand your average CPU and memory utilization,
    and identify resources that are underutilized.
    Rightsize those instances to reduce your carbon
    footprint.
  - Identify the network and storage performance, such
    as I/OPS, and size for the target workload. Analyze
    the overall demand, rate of change, and required
    response time to rightsize the throttle or buffer
    required.
  - For fault-tolerant, flexible, and stateless
    workloads that can trade-off with minimal
    interruption, adopt Spot Instances in your design.
  - Evaluate your migrated workload continually using
    AWS Compute Optimizer and
    [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/"), and proactively
    make rightsizing adjustments on your workload.

**Suggestion 5.1.3:** Consider managed services in your workload design.

Remove the need for you to run and maintain physical servers, as AWS operates at scale and is responsible for their efficient operation. For example, instead of migrating your virtual machine or container to Amazon ECS running on Amazon EC2, consider using a service like Amazon Fargate, where you can run containers without having to manage the servers, or package and deploy Lambda functions as container images.

Containerize and migrate existing applications using , for migrating and modernizing Java and .NET web applications into container format. Use [managed services](../sustainability-pillar/sus_sus_hardware_a4.md "../sustainability-pillar/sus_sus_hardware_a4.md") to operate more efficiently in the cloud.

**Suggestion
5.1.4:** Configure your
[instance
tenancy](../../../autoscaling/ec2/userguide/auto-scaling-dedicated-instances.md "../../../autoscaling/ec2/userguide/auto-scaling-dedicated-instances.md"), which defines how EC2 instances are
distributed across physical hardware.

Tenancy provides the opportunity to further optimize the
workload. Migrating to shared instances instead of migrating
to dedicated underutilized instances or hosts can be more
beneficial when working towards the sustainability goal.

For more detail, see the following:

- [Right Size Before Migrating](../../../whitepapers/latest/cost-optimization-right-sizing/right-size-before-migrating.md "../../../whitepapers/latest/cost-optimization-right-sizing/right-size-before-migrating.md")
- [Getting started with Graviton](https://aws.amazon.com/ec2/graviton/getting-started/ "https://aws.amazon.com/ec2/graviton/getting-started/")
- [Streamline selection and right size EC2 with AWS Compute Optimizer](https://www.youtube.com/watch?v=flhuwVwYomg "https://www.youtube.com/watch?v=flhuwVwYomg")
- [Effortless migration - Is your app already Graviton-ready?](https://www.youtube.com/watch?v=aa_FjqYCJpY "https://www.youtube.com/watch?v=aa_FjqYCJpY")
- [Design patterns for success in serverless microservices](https://www.youtube.com/watch?v=ReRB_xEtEjY "https://www.youtube.com/watch?v=ReRB_xEtEjY")
- [Lift and shift a web application to serverless](https://www.youtube.com/watch?v=O-hSs7aF7JE "https://www.youtube.com/watch?v=O-hSs7aF7JE")

| MIG-SUS-06: How do you take advantage of software and architecture patterns for workloads you are going to migrate to support your sustainability goals? |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                                                                                                                                          |

Software and architecture patterns can be used to influence
utilization of resources while migrating workloads. The aim is
to use patterns that maximize utilization so that resources
consumed for the workloads are minimized. Idling of resources
due to user behavior or nature of workload can also be minimized
by applying appropriate software and architecture patterns.
on-premises workloads are not designed to take advantage of AWS
cloud features that can optimize utilization of resources, like
autoscaling. These workloads can have multiple instances of
software or services running at multiple locations or are
overprovisioned all the time to cater to peak demand. Some
workloads are running all the time, even when not in use. Using
the 7 Rs can optimize resource usage. Adopt patterns and
architecture to consolidate underutilized components to increase
overall utilization. Retire components that are no longer
required.

## MIG-SUS-BP-6.1: Identify environments and workloads that can be consolidated or retired

This BP applies to the following best practice areas: Software and architecture

### Implementation guidance

**Suggestion 6.1.1:** Consolidate environments and workloads in the AWS Cloud.

When moving workloads from multiple on-premises environments or in merger and acquisition cases, consolidating environments on AWS leads to optimal usage of resources and eliminates duplicate functionality. Identify workloads during the assess stage that can be eliminated or consolidated. Identify multiple instances of services or applications running at multiple locations on-premises.

Retire workloads that are not used. Use automated tools such as [Migration Evaluator](https://aws.amazon.com/migration-evaluator/ "https://aws.amazon.com/migration-evaluator/") to identify workloads that are not being used.

## MIG-SUS-BP-6.2: Identify workloads that can use efficient software and architecture patterns to maintain consistent high utilization of deployed resources

This BP applies to the following best practice areas: Software
and architecture

### Implementation guidance

**Suggestion 6.2.1:** Optimize software and architecture for asynchronous and scheduled jobs.

Identify applications and workloads that can benefit from software and architecture patterns to maintain consistently-high utilization of deployed resources while migrating applications.

While migrating applications, evaluate use of integration patterns to scale the processing independently of the receiving of messages, which reduces resource utilization. Identify if use of a messaging component can lead to relaxed service level requirements that can be met with fewer resources. Employ batching requests where possible for optimal use of resources, as batching provides consistent usage. Scheduling the batch jobs reduces idle time for resources. For detail, see [SUS03-BP01 Optimize software and architecture for asynchronous and scheduled jobs](../sustainability-pillar/sus_sus_software_a2.md "../sustainability-pillar/sus_sus_software_a2.md").

## MIG-SUS-BP-6.3: Analyze your data access patterns and data lifecycle processes, and evaluate how you can become more efficient and sustainable in your data management

This BP applies to the following best practice areas: Software and architecture

### Implementation guidance

Storing and accessing data efficiently, in addition to reducing idle storage resources, results in a more efficient and sustainable architecture. When migrating data, understand how data is used within your workload, consumed by your users, transferred, and stored. Use software patterns and architectures that best support data access and storage to minimize the compute, networking, and storage resources required to support the workload.

**Suggestion 6.3.1:** Define and implement a data lifecycle process for data in your object store.

Design a data lifecycle management process based on your data access patterns, observed in your on-premises facility. That process either removes data that is no longer required or archives data into less resource-intensive storage. While migrating data, implement a data lifecycle policy. For more detail, see [Best practice 15.4 – Implement data retention processes to remove redundant data from your analytics environment](../analytics-lens/best-practice-15.4-implement-data-retention-processes-to-remove-redundant-data-from-your-analytics-environment..md "../analytics-lens/best-practice-15.4-implement-data-retention-processes-to-remove-redundant-data-from-your-analytics-environment..md").

**Suggestion 6.3.2:** Evaluate use of columnar data formats and compression.

While migrating data, evaluate if columnar data formats like Parquet and ORC can be used. These formats [require less storage capacity](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/ "https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-ii-storage/") compared to row-based formats like CSV and JSON.

- Parquet consumes up to
  [six
  times](../../../redshift/latest/dg/r_UNLOAD.md "../../../redshift/latest/dg/r_UNLOAD.md") less storage in Amazon S3
  compared to text formats. This is because of features
  such as
  [column-wise
  compression, different encodings, or compression based
  on data type](https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/ "https://aws.amazon.com/blogs/big-data/top-10-performance-tuning-tips-for-amazon-athena/").
- You can improve performance and reduce query costs of
  [Amazon Athena](https://aws.amazon.com/athena/ "https://aws.amazon.com/athena/") by

[30–90
percent](https://aws.amazon.com/athena/faqs/ "https://aws.amazon.com/athena/faqs/") by compressing, partitioning,
and converting your data into columnar formats. Using
columnar data formats and compressions reduces the
amount of data scanned.

## MIG-SUS-BP-6.4: Understand and influence business requirements, and optimize areas of code to reach your sustainability goals

This BP applies to the following best practice areas: Software and architecture

Understanding your sustainability goals is the first step to focusing on the factors needed to meet those goals. Defining such criteria involves adopting metrics that can be used to measure and evaluate your current sustainability posture, report progress against goals, and accelerate improvements. By analyzing the current environmental impact of the underlying cloud-based infrastructure, you can quantify the tradeoffs and changes required to meet your sustainability objectives.

### Implementation guidance

**Suggestion 6.4.1:** Define criteria to measure and understand your sustainability impact after your migration.

Post-migration, you can use sustainability proxy metrics for your monitoring scenarios. [Proxy metrics](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-i-what-are-proxy-metrics/") allow architecture teams to evaluate correlated improvements made to a workload instead of real-time carbon metrics. Defining proxy metrics across compute, storage, and network infrastructure can help you understand how infrastructure changes can impact sustainability results.

Example proxy metrics include vCPU minutes for compute, GBs provisioned for storage, and GBs transferred for network traffic. Proxy metrics combined with business metrics can define sustainability KPIs, which can be used to drive sustainability optimizations while keeping business needs in focus. One example would be to measure vCPU minutes per transaction and define an improvement goal to minimize this metric. Business stakeholders would have to weigh the cost, as reducing vCPUs could ultimately become detrimental to delivering on business needs. When running workloads in AWS, the change in these measured resources correlates with a similar change in cost (except as noted in the following), making overall infrastructure spend a useful proxy metric.

By agreeing on a set of sustainability metrics, the architect team can evaluate different technical approaches to reduce environmental impact.

For more detail, see the following:

- [Cloud sustainability](../sustainability-pillar/cloud-sustainability.md "../sustainability-pillar/cloud-sustainability.md")
- [Evaluate specific improvements](../sustainability-pillar/evaluate-specific-improvements.md "../sustainability-pillar/evaluate-specific-improvements.md")
- [Measure and track cloud efficiency with sustainability proxy metrics, Part II: Establish a metrics pipeline](https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/ "https://aws.amazon.com/blogs/aws-cloud-financial-management/measure-and-track-cloud-efficiency-with-sustainability-proxy-metrics-part-ii-establish-a-metrics-pipeline/")
- [Best Practices from IBM and AWS for Optimizing SaaS Solutions for Sustainability](https://aws.amazon.com/blogs/apn/best-practices-from-ibm-and-aws-for-optimizing-saas-solutions-for-sustainability/ "https://aws.amazon.com/blogs/apn/best-practices-from-ibm-and-aws-for-optimizing-saas-solutions-for-sustainability/")
- [re:Invent 2022: Delivering sustainable, high-performing architectures](https://www.youtube.com/watch?v=FBc9hXQfat0 "https://www.youtube.com/watch?v=FBc9hXQfat0")

**Suggestion
6.4.2:** Consider using
[Amazon CodeWhisperer](https://aws.amazon.com/codewhisperer/ "https://aws.amazon.com/codewhisperer/") to reduce your cloud costs, improve
your application performance, and

[reduce
your carbon emissions](https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/ "https://aws.amazon.com/blogs/compute/building-sustainable-efficient-and-cost-optimized-applications-on-aws/") attributable to your workload.

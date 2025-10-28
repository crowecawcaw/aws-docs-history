# Reliability

The reliability pillar provides guidance to help customers apply best practices in the design, delivery, and maintenance of AWS environments. The reliability pillar provides best practices on how a system can recover from infrastructure or service disruptions, dynamically acquire computing resources to scale demand, and mitigate disruptions caused by events such as misconfigurations or transient network issues.

The technology systems of financial institutions are complex and highly interconnected to each other, and to non-financial entities. The proper functioning of many industries depends on certain types of workloads, for example, payment processing, trading and settlement, market data, custody and entitlement management, and financial messaging. Regulators continue to focus on the resilience of financial institutions through bodies such as the Basel Committee on Banking Supervision, Board of Governors of the Federal Reserve System, RegSCI, Bank of England and other regulatory bodies, issuing policies and guidance that the financial services institutions need to adhere to.

In this section, we provide in-depth best practices that financial institutions can use with AWS services to construct highly available, resilient, and scalable solutions at lower costs compared to traditional on-premises IT. To discuss these best practices, we use the concept of service availability interchangeably with the Recovery Time Objective (RTO) and Recovery Point Objective (RPO). An introduction to the concept of service availability and its relation to the recovery objectives can be found in the [Well-Architected Reliability Pillar](../reliability-pillar/welcome.md "../reliability-pillar/welcome.md").

## Design principles

Financial institutions can leverage AWS services to provide the
levels of resilience and availability that their workloads need
based on their criticality. The AWS Global infrastructure is built
around Regions, Availability Zones (AZs), Local Zones, and edge locations. Our AWS services are of global, Regional, or zonal
nature. For example, Amazon Elastic Compute Cloud (Amazon EC2)
and Amazon Elastic Block Store (Amazon EBS) are zonal services. A
zonal service is one that provides the ability to specify which
Availability Zone the resources are deployed into.

These services operate independently in each Availability Zone within a Region, and more importantly, fail independently in each Availability Zone as well. This means that components of a service in one Availability Zone don't have dependencies on components in other Availability Zones. We can do this because a zonal service has zonal data planes. Services like Amazon Simple Storage Service (Amazon S3), Amazon Simple Queue Service (Amazon SQS) and Amazon DynamoDB are Regional services.

[Regional services](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/") are services that AWS has built on top of multiple Availability Zones so that customers don't have to figure out how to make the best use of zonal services. We logically group together the service deployed across multiple Availability Zones to present a single Regional endpoint to customers. In addition to Regional and zonal AWS services, there is a small set of AWS services like IAM and Amazon Route 53, that do not have control planes and data planes that exist independently in each Region. Because their resources are not Region-specific, they are commonly referred to as _global_. Global AWS services still follow the conventional AWS design pattern of separating the control plane and data plane in order to achieve [static stability](../../../whitepapers/latest/aws-fault-isolation-boundaries/aws-infrastructure.md#static-stability "../../../whitepapers/latest/aws-fault-isolation-boundaries/aws-infrastructure.md#static-stability"). The significant difference for most global services is that their control plane is hosted in a _single_ AWS Region, while their data plane is globally distributed. Therefore, when building critical workloads on AWS it is important to understand the services [fault isolation boundary](../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md "../../../whitepapers/latest/aws-fault-isolation-boundaries/abstract-and-introduction.md") and how the boundary defines the resilience of your workload.

The global infrastructure outlined gives AWS the ability to provide fault isolation to its customers. The disruption of a zonal resource has no impact on resources in other Availability Zones. The disruption of a Regional service has no impact on services in other AWS Regions. For global services, mitigation techniques such as splitting the control plane and data plane mean that the services core functionality continues to operate when the control plane is disrupted, as they can operate independently of one another.

## Definitions

1. [Foundations](../reliability-pillar/foundations.md "../reliability-pillar/foundations.md"): The scope of foundational requirements extends beyond a
   single workload or project. Before architecting any system, foundational requirements that
   influence reliability should be in place.
2. [Workload
   architecture](../reliability-pillar/workload-architecture.md "../reliability-pillar/workload-architecture.md"): A reliable workload starts with upfront design
   decisions for both software and infrastructure. Your architecture choices impact your
   workload behavior across all six Well-Architected pillars.
3. [Change
   management](../reliability-pillar/change-management.md "../reliability-pillar/change-management.md"): Changes to your workload or its environment must be
   anticipated and accommodated to achieve reliable operation of the workload. Changes
   include those imposed on your workload such as spikes in demand, as well as those from
   within, such as feature deployments and security patches.
4. [Failure
   management](../reliability-pillar/failure-management.md "../reliability-pillar/failure-management.md"): Failures are a given, and everything eventually fails
   over time. This is a given, whether you are using the highest-quality hardware or lowest
   cost components. _“Everything fails all the time. We needed to
   build systems that embrace failure as a natural occurrence.”_ — Werner Vogels
5. [Reliability](../reliability-pillar/reliability.md "../reliability-pillar/reliability.md"): Reliability is the ability of a workload to perform its
   intended function correctly and consistently when it's expected to. This includes the
   ability to operate and test the workload through its total lifecycle.
6. [Resilience](../reliability-pillar/shared-responsibility-model-for-resiliency.md "../reliability-pillar/shared-responsibility-model-for-resiliency.md"): Resilience is the ability of a workload to recover
   from infrastructure or service disruptions, dynamically acquire computing resources to
   meet demand, and mitigate disruptions, such as misconfigurations or transient network
   issues.
7. [Embedded Metric
   Format](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format.md"): EMF is a part of Amazon CloudWatch that helps you
   ingest complex, high-cardinality application data as logs and generate
   actionable metrics from them. By using this format to send logs from resources such as
   Lambda functions and containers, you can create custom metrics without having to
   instrument or maintain separate code, while gaining powerful analytical capabilities on
   your log data.

**Note:** Definitions 1–4 are the domain definitions for the Well-Architected Reliability Pillar.

## Design for resilience

AWS offers capabilities that can be leveraged to provide different levels of resilience in the cloud based on your business requirements. When building a workload in the AWS Cloud, AWS is responsible for the resilience of the cloud. This means, we are responsible for the resilience of the services and infrastructure offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

The implementation, configuration, and operation of your applications on AWS is your responsibility. The AWS Cloud services that you choose to consume, how you configure them, how you manage change and failure, and how you plan for disaster recovery are some of your key responsibilities that contribute to the resilience of your system. As a user of AWS, you are responsible for how you configure the services and resources you build into your systems. For example you can make the decision to deploy an Amazon RDS database with a synchronous replica, or as a standalone instance. You are also responsible for establishing monitoring for your system so you can understand when it is not meeting your customers' expectations or delivering business value.

This responsibility determines the amount of configuration work, testing mechanisms,
recovery mechanisms, operational tooling, and observability logic that you can design into
your workload to make it resilient.

Financial institutions should consider the following when building resilient workloads in the cloud:

- Software development lifecycle
- Resilience requirement planning
- Resilience architecture
- Observability
- Data backup and retention

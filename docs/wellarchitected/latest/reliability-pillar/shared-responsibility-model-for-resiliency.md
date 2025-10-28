# Shared Responsibility Model for

Resiliency

Resiliency is a shared responsibility between AWS and you. It is important that you
understand how disaster recovery (DR) and availability, as part of resiliency, operate under
this shared model.

**AWS responsibility - Resiliency of the cloud**

AWS is responsible for resiliency of the infrastructure that runs all of the services
offered in the AWS Cloud. This infrastructure comprises the hardware, software, networking,
and facilities that run AWS Cloud services. AWS uses commercially reasonable efforts to
make these AWS Cloud services available, ensuring service availability meets or exceeds
[AWS Service Level Agreements
(SLAs)](https://aws.amazon.com/legal/service-level-agreements/ "https://aws.amazon.com/legal/service-level-agreements/").

The [AWS Global Cloud
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/") is designed to allow customers to build highly resilient workload
architectures. Each AWS Region is fully isolated and consists of multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones "https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones"), which are physically isolated partitions of infrastructure.
Availability Zones isolate faults that could impact workload resilience, preventing them from
impacting other zones in the Region. But at the same time, all zones in an AWS Region are
interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated
metro fiber providing high-throughput, low-latency networking between zones. All traffic
between zones is encrypted. The network performance is sufficient to accomplish synchronous
replication between zones. When an application is partitioned across AZs, companies are better
isolated and protected from issues such as power outages, lightning strikes, tornadoes,
hurricanes, and more.

**Customer responsibility - Resiliency in the cloud**

Your responsibility is determined by the AWS Cloud services that you select. This
determines the amount of configuration work you must perform as part of your resiliency
responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) requires the customer to
perform all of the necessary resiliency configuration and management tasks. Customers that
deploy Amazon EC2 instances are responsible for [deploying Amazon EC2 instances across multiple locations](use-fault-isolation-to-protect-your-workload.md "use-fault-isolation-to-protect-your-workload.md") (such as AWS Availability
Zones), [implementing self-healing](design-your-workload-to-withstand-component-failures.md "design-your-workload-to-withstand-component-failures.md") using services like Auto Scaling, and using [resilient
workload architecture best practices](workload-architecture.md "workload-architecture.md") for applications installed on the instances.
For managed services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the
operating system, and platforms, and customers access the endpoints to store and retrieve
data. You are responsible for managing resiliency of your data including backup, versioning,
and replication strategies.

Deploying your workload across multiple Availability Zones in an AWS Region is part of
a high availability strategy designed to protect workloads by isolating issues to one
Availability Zone, which uses the redundancy of the other Availability Zones to continue
serving requests. A Multi-AZ architecture is also part of a DR strategy designed to make
workloads better isolated and protected from issues such as power outages, lightning strikes,
tornadoes, earthquakes, and more. DR strategies may also make use of multiple AWS Regions.
For example, in an active/passive configuration, service for the workload fails over from its
active Region to its DR Region if the active Region can no longer serve requests.

![Chart illustrating the shared resiliency model.](images/shared-model-resiliency.png)
_Responsibility for resilience in and of the cloud for customers and
AWS._

You can use AWS services to achieve your resilience objectives. As a customer, you are
responsible for management of the following aspects of your system to achieve resilience in
the cloud. For more detail on each service in particular, see [AWS documentation](../../../index.md "../../../index.md").

**Networking, quotas, and constraints**

- Best practices for this area of the shared responsibility model are described in
  detail under [Foundations](foundations.md "foundations.md").
- Plan your architecture with adequate room to scale and understand the [service quotas](manage-service-quotas-and-constraints.md "manage-service-quotas-and-constraints.md") and constraints of the services you include, based on expected
  load request increases where applicable.
- Design your [network
  topology](plan-your-network-topology.md "plan-your-network-topology.md") to be highly available, redundant, and scalable.

**Change management and operational resilience**

- [Change
  management](change-management.md "change-management.md") includes how to introduce and manage change in your environment.
  [Implementing
  change](implement-change.md "implement-change.md") requires building and keeping runbooks up to date and deployment
  strategies for your application and infrastructure.
- A resilient strategy for [monitoring workload resources](monitor-workload-resources.md "monitor-workload-resources.md") considers all components, including both
  technical and business metrics, notifications, automation, and analysis.
- Workloads in the cloud must [adapt to changes in demand](design-your-workload-to-adapt-to-changes-in-demand.md "design-your-workload-to-adapt-to-changes-in-demand.md") scaling in reaction to impairments or fluctuations
  in usage.

**Observability and failure management**

- Observing failures through monitoring is required to automate healing so that your
  workloads can [withstand component failures](design-your-workload-to-withstand-component-failures.md "design-your-workload-to-withstand-component-failures.md").
- [Failure
  management](failure-management.md "failure-management.md") requires [backing up
  data](back-up-data.md "back-up-data.md"), applying best practices to allow your workload to withstand component
  failures, and [planning for disaster recovery](plan-for-disaster-recovery-dr.md "plan-for-disaster-recovery-dr.md").

**Workload architecture**

- Your [workload
  architecture](workload-architecture.md "workload-architecture.md") includes how you design services around business domains, apply SOA
  and distributed system design to prevent failures, and build in capabilities like
  throttling, retries, queue management, timeouts, and emergency levers.
- Rely on proven [AWS solutions](https://aws.amazon.com/solutions/ "https://aws.amazon.com/solutions/"), the
  [Amazon Builders Library](https://aws.amazon.com/builders-library/ "https://aws.amazon.com/builders-library/"), and
  [serverless patterns](https://serverlessland.com/patterns "https://serverlessland.com/patterns") to align
  with best practices and jump start implementations.
- Use continuous improvement to decompose your system into distributed services to
  scale and innovate faster. Use [AWS
  microservices](https://aws.amazon.com/microservices/ "https://aws.amazon.com/microservices/") guidance and managed service options to simplify and accelerate
  your ability to introduce change and innovate.

**Continuous testing of critical infrastructure**

- [Testing
  reliability](test-reliability.md "test-reliability.md") means testing at the functional, performance, and chaos levels, as
  well as adopting incident analysis and game day practices to build expertise in resolving
  issues that are not well understood.
- For both cloud all-in and hybrid applications, knowing how your application behaves
  when issues arise or components go down allows you to quickly and reliably recover from
  outages.
- Create and document repeatable experiments to understand how your system behaves when
  things don’t work as expected. These tests will prove effectiveness of your overall
  resilience and provide a feedback loop for your operational procedures before facing real
  failure scenarios.

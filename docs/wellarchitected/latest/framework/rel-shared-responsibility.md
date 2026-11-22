

# The shared responsibility model for resilience

 Resilience is a shared responsibility between AWS and you. It is important that you understand how disaster recovery (DR) and availability, as part of resilience, operate under this shared model. 

 **AWS responsibility - Resilience of the cloud** 

 AWS is responsible for resilience of the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure comprises the hardware, software, networking, and facilities that run AWS Cloud services. AWS uses commercially reasonable efforts to make these AWS Cloud services available, ensuring service availability meets or exceeds [AWS Service Level Agreements (SLAs)](https://aws.amazon.com/legal/service-level-agreements/). 

 The [AWS Global Cloud Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) is designed to allow customers to build highly resilient workload architectures. Each AWS Region is fully isolated and consists of multiple [Availability Zones](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/#Availability_Zones), which are physically isolated partitions of infrastructure. Availability Zones isolate faults that could impact workload resilience, preventing them from impacting other zones in the Region. But at the same time, all zones in an AWS Region are interconnected with high-bandwidth, low-latency networking, over fully redundant, dedicated metro fiber providing high-throughput, low-latency networking between zones. All traffic between zones is encrypted. The network performance is sufficient to accomplish synchronous replication between zones. When an application is partitioned across AZs, companies are better isolated and protected from issues such as power failures, lightning strikes, tornadoes, hurricanes, and more. 

 **Customer responsibility - Resilience in the cloud** 

 Your responsibility is determined by the AWS Cloud services that you select. This determines the amount of configuration work you must perform as part of your resilience responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) requires the customer to perform all of the necessary resilience configuration and management tasks. Customers that deploy Amazon EC2 instances are responsible for [Use fault isolation to protect your workload](rel10.md) (such as AWS Availability Zones), [Design your workload to withstand component failures](rel11.md) using services like Auto Scaling, and using [Design your workload service architecture](rel03.md) for applications installed on the instances. For managed services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. You are responsible for managing resilience of your data including backup, versioning, and replication strategies. 

 Deploying your workload across multiple Availability Zones in an AWS Region is part of a high availability strategy designed to protect workloads by isolating issues to one Availability Zone, which uses the redundancy of the other Availability Zones to continue serving requests. A Multi-AZ architecture is also part of a DR strategy designed to make workloads better isolated and protected from issues such as power failures, lightning strikes, tornadoes, earthquakes, and more. DR strategies may also make use of multiple AWS Regions. For example, in an active/passive configuration, service for the workload fails over from its active Region to its DR Region if the active Region can no longer serve requests. 

![Shared responsibility model for resilience. The customer is responsible for resilience in the cloud: continuous testing of critical infrastructure, workload architecture, change management and resilient operations, observability and failure management, and networking, quotas, and constraints. AWS is responsible for resilience of the cloud: hardware and services (compute, storage, database, networking) and the AWS global infrastructure of Regions, Availability Zones, and edge locations.](https://docs.aws.amazon.com/wellarchitected/latest/framework/images/shared-model-resiliency.png)

*Responsibility for resilience in and of the cloud for customers and AWS*


 You can use AWS services to achieve your resilience objectives. As a customer, you are responsible for management of the following aspects of your system to achieve resilience in the cloud. For more detail on each service in particular, see [AWS documentation](https://docs.aws.amazon.com/index.html). 

 **Networking, quotas, and constraints** 
+  Best practices for this area of the shared responsibility model are described in detail under Foundations. 
+  Plan your architecture with adequate room to scale and understand the [Manage service quotas and constraints](rel01.md) and constraints of the services you include, based on expected load request increases where applicable. 
+  Design your [Plan your network topology](rel02.md) to be highly available, redundant, and scalable. 

 **Change management and operational resilience** 
+  Change management includes how to introduce and manage change in your environment. [Implement change](rel08.md) requires building and keeping runbooks up to date and deployment strategies for your application and infrastructure. 
+  A resilient strategy for [Monitor workload resources](rel06.md) considers all components, including both technical and business metrics, notifications, automation, and analysis. 
+  Workloads in the cloud must [Design your workload to adapt to changes in demand](rel07.md) scaling in reaction to impairments or fluctuations in usage. 

 **Observability and failure management** 
+  Observing failures through monitoring is required to automate healing so that your workloads can [Design your workload to withstand component failures](rel11.md). 
+  Failure management requires [Back up data](rel09.md), applying best practices to allow your workload to withstand component failures, and [Plan for Disaster Recovery (DR)](rel13.md). 

 **Workload architecture** 
+  Your workload architecture includes how you design services around business domains, apply SOA and distributed system design to prevent failures, and build in capabilities like throttling, retries, queue management, timeouts, and emergency levers. 
+  Rely on proven [AWS solutions](https://aws.amazon.com/solutions/), the [Amazon Builders Library](https://builder.aws.com/learn/topics/builders-library), and [serverless patterns](https://serverlessland.com/patterns) to align with best practices and jump start implementations. 
+  Use continuous improvement to decompose your system into distributed services to scale and innovate faster. Use [AWS microservices](https://aws.amazon.com/microservices/) guidance and managed service options to simplify and accelerate your ability to introduce change and innovate. 

 **Continuous testing of critical infrastructure** 
+  [Test reliability](rel12.md) means testing at the functional, performance, and resilience levels, as well as adopting incident analysis and game day practices to build expertise in resolving issues that are not well understood. 
+  For both cloud all-in and hybrid applications, knowing how your application behaves when issues arise or components go down allows you to recover quickly and reliably. 
+  Create and document repeatable experiments to understand how your system behaves when things don't work as expected. These tests will prove effectiveness of your overall resilience and provide a feedback loop for your operational procedures before facing real failure scenarios. 
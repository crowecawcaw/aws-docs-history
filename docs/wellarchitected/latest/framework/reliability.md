

# Reliability

 The reliability pillar covers the ability of a workload to perform its intended function correctly and consistently when it is expected to, across its whole lifecycle, and to operate and test the workload throughout that lifecycle. This guidance applies across the design, delivery, and maintenance of a workload, so that reliability is built in rather than added at the end. 

 Reliability in the cloud depends on several factors, and the primary one is resilience: 
+  **Resilience** is the ability of a workload to recover from infrastructure or service disruptions, acquire computing resources dynamically to meet demand, and mitigate disruptions such as misconfigurations or transient network issues. 

 Resilience is the primary focus of this pillar. Four other factors also affect a workload's reliability, and each is covered in depth by its own pillar of the Well-Architected Framework: 
+  **Operational excellence** automates change, uses playbooks to respond to failures, and runs operational readiness reviews to confirm a workload is ready for production. 
+  **Security** helps protect data and infrastructure from unauthorized access and misuse that could otherwise affect availability. Encrypting backups, for example, keeps recovery data protected. 
+  **Performance efficiency** designs for the required request rates and minimizes latency. 
+  **Cost optimization** weighs reliability trade-offs, such as spending more on capacity for static stability against relying on automatic scaling when more capacity is needed. 

 Many of the best practices in this pillar also strengthen those aspects, but the focus here is resilience. 

 This pillar groups its practices into four areas, each containing one or more capabilities that are made up of individual best practices. 

## Foundations
<a name="foundations"></a>

 Foundational requirements have a scope beyond a single workload or project, and they need to be in place before you architect a system. In an on-premises environment, meeting them can involve long lead times because of dependencies; for example, you need sufficient network bandwidth to your data center. On AWS, most of these requirements are already available or can be provisioned as needed. AWS is responsible for satisfying the requirement for sufficient networking and compute capacity, which leaves you free to change resource size and allocation on demand. This area covers establishing those foundations: managing the service quotas and constraints your workloads run within, and planning a network topology that is highly available, redundant, and ready to grow. 
+  [Manage service quotas and constraints](rel01.md) 
+  [Plan your network topology](rel02.md) 

## Workload architecture
<a name="workload-architecture"></a>

 A reliable workload starts with upfront design decisions for both software and infrastructure. These choices affect how the workload behaves across all six Well-Architected pillars, and for reliability there are specific patterns worth following. This area covers shaping a resilient architecture: designing the workload's service architecture, and designing the interactions between distributed components both to prevent failures and to mitigate or withstand the failures that still occur. 
+  [Design your workload service architecture](rel03.md) 
+  [Design interactions in a distributed system to prevent failures](rel04.md) 
+  [Design interactions in a distributed system to mitigate or withstand failures](rel05.md) 

## Change management
<a name="change-management"></a>

 Changes to a workload or its environment must be anticipated and accommodated for the workload to operate reliably. Changes include those imposed on the workload, such as spikes in demand, as well as those from within, such as feature deployments and security patches. This area covers keeping change from becoming a source of failure: monitoring workload resources to detect problems early, designing the workload to adapt to changes in demand, and implementing change through controlled, tested, and automated processes. 
+  [Monitor workload resources](rel06.md) 
+  [Design your workload to adapt to changes in demand](rel07.md) 
+  [Implement change](rel08.md) 

## Failure management
<a name="failure-management"></a>

 Failures are a given, and everything eventually fails over time: from routers to hard disks, from operating systems to memory units corrupting TCP packets, from transient errors to permanent failures. This holds whether you use the highest-quality hardware or the lowest-cost components. 

 — [Werner Vogels, CTO, Amazon.com](https://www.allthingsdistributed.com/2016/03/10-lessons-from-10-years-of-aws.html) 

 In the cloud you are protected against most low-level failures, because managed services replicate data and isolate faults on your behalf. However, failures can still affect a workload, so you must design for resilience when the workload needs to be reliable. This area covers preparing a workload to survive failure: backing up data, using fault isolation to contain the scope of a failure, designing the workload to withstand component failures, testing reliability, and planning for disaster recovery. 
+  [Back up data](rel09.md) 
+  [Use fault isolation to protect your workload](rel10.md) 
+  [Design your workload to withstand component failures](rel11.md) 
+  [Test reliability](rel12.md) 
+  [Plan for Disaster Recovery (DR)](rel13.md) 

 To achieve reliability, start with the foundations, where service quotas and network topology accommodate the workload. Design the workload architecture of the distributed system to prevent and mitigate failures. Build the workload to handle changes in demand and requirements, and design it to detect failure and heal itself automatically. 

 This guidance is written for the technology roles responsible for designing, delivering, and operating reliable workloads, including chief technology officers (CTOs), architects, developers, DevOps and infrastructure engineers, site reliability engineers (SREs), and operations and on-call teams. After reading it, you will understand the AWS recommendations and strategies to apply when you design cloud architectures for reliability, so you can build workloads with strong foundations, resilient architecture, consistent change management, and proven failure recovery. 
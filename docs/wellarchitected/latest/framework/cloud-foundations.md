

# Cloud Foundations

 AWS Well-Architected Cloud Foundations (WA Cloud Foundations) defines the central capabilities you can employ to govern your overall cloud environment, promote and enforce standards across your workloads, and provide services that your workload teams can consume to accelerate their delivery. These capabilities are often maintained by a dedicated engineering team that is distinct from workload teams, such as a foundation team, cloud engineering team, or devops team. 

 This guidance presents a comprehensive framework of organizational-level best practices for building and maintaining secure, efficient, and scalable enterprise cloud environments. While individual workloads require specific architectural considerations, WA Cloud Foundations focuses on establishing organization-wide controls, standards, and practices that enable consistent implementation of Well-Architected principles across all workloads. 

 WA Cloud Foundations addresses critical challenges modern organizations face: managing complex multi-account environments, maintaining security and compliance at scale, optimizing costs, and establishing effective governance. By providing comprehensive guidance across seven key domains - multi-account strategy, identity management, observability, resource management, security and compliance, financial management, and networking - these best practices enable organizations to accelerate cloud adoption while minimizing risks and technical debt. Organizations implementing these recommendations build strong foundations that support business agility, promote innovation, and help maintain long-term sustainability of cloud infrastructure investments. 

 Customers may be familiar with the term Landing Zone, which refers to a well-architected, multi-account AWS environment. WA Cloud Foundations is the blueprint for creating a sound landing zone. It provides prescriptive guidance on the security, operational, and financial controls that every organization should have in place before running production workloads on AWS. 

 After reading this document, technology leaders and practitioners will be equipped to develop effective multi-account strategies, establish standardized and efficient security, compliance and operational practices across their AWS environments. 

## Relationship to the AWS Well-Architected Framework
<a name="foundations-fw-relation"></a>

 Until the launch of Well-Architected Cloud Foundations, best practices that were foundational were spread across multiple areas of the Well-Architected Framework. This distributed nature made it a challenge to understand what to set up before defining your first workload. Additionally, it made it a challenge to review the foundations of an environment as the foundations were likely owned by another team. Cloud Foundations guidance now serves as your new source of information to define your environment. 

## Capabilities
<a name="capabilities"></a>

 Well-Architected Cloud Foundations is organized into seven capabilities that together cover the organizational controls, standards, and shared services needed to run a secure, efficient cloud environment at scale. 


|  Capability  |  Description  | 
| --- | --- | 
|  [Multi-account environment](fnd01.md)  |  Structure and govern AWS accounts and organizational units to create strong isolation boundaries and apply policy consistently across teams and environments.  | 
|  [Identity and access management](fnd02.md)  |  Centralize identities, protect privileged accounts, and enforce least privilege so the right people and services have the right access to your cloud resources.  | 
|  [Central observability management](fnd03.md)  |  Set organization-wide standards for logs, metrics, and traces, and aggregate telemetry centrally so teams share a reliable view of how the environment is behaving.  | 
|  [Resource and inventory management](fnd04.md)  |  Maintain consistent tagging, a current inventory of resources and dependencies, shared patterns, and automated patching to keep the environment discoverable and in good repair.  | 
|  [Security and compliance](fnd05.md)  |  Provide emergency access, audit logging, threat detection, vulnerability management, and forensic readiness so security teams can prevent, detect, and respond to events.  | 
|  [Cloud financial management](fnd06.md)  |  Deliver detailed cost visibility, standardized attribution, budgets, licensing management, and commitment strategies to track and optimize cloud spend across the organization.  | 
|  [Networking and connectivity](fnd07.md)  |  Design and centrally manage network topology, protection controls, and DNS to connect workloads securely and efficiently across accounts, Regions, and on-premises networks.  | 
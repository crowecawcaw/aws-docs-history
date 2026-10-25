

# AWS Transform
<a name="aws-transform"></a>

AWS Transform is a collaborative enterprise IT transformation workbench powered by specialized AI agents, agentic workflows, and continuous learning that accelerates cloud migration, legacy application modernization, and tech debt reduction. It offers purpose-built transformations for mainframe, VMware, and Windows workloads, and automates code modernization at scale—from version and framework upgrades to fully custom, organization-specific transformations.

By automating complex tasks like assessments, code analysis, refactoring, dependency mapping, and transformation planning, AWS Transform dramatically reduces project timelines and costs. Its shared workspaces and natural language chat experience enable cross-functional teams to collaborate in real time, track progress, and manage transformations from start to finish.

In its first year, AWS Transform has migrated tens of thousands of VMs and processed over 4.5 billion lines of code, saving 1.69 million hours of manual effort across mainframe, Windows/.NET, infrastructure, and custom code modernization.

To get started, see [AWS Transform in the AWS Management Console](https://console.aws.amazon.com/transform). For the latest features, see [AWS Transform](https://aws.amazon.com/transform/). For detailed guidance, see the [AWS Transform User Guide](https://docs.aws.amazon.com/transform/latest/userguide/).

## Services and agents
<a name="aws-transform-services-agents"></a>

AWS Transform provides specialized AI agents for five primary use cases. Each agent is purpose-built on 20 years of AWS migration and modernization experience and is accessible from the web console, CLI, IDE (Kiro, VS Code), or through MCP (Model Context Protocol) integration.

### AWS Transform assessments (migration assessments)
<a name="aws-transform-assessments"></a>

AWS Transform assessments help you evaluate the cost, feasibility, and business value of migrating on-premises infrastructure to AWS. Using AI-powered agents, assessments provide automated right-sizing recommendations, multi-scenario comparison, and interactive refinement through natural language chat.

Key capabilities include:
+ **Cost estimation** – Get cost estimates for Amazon EC2, Amazon RDS for SQL Server, Amazon EBS, Amazon S3, Amazon FSx, Amazon MSK, and end user computing services.
+ **Automated right-sizing** – Analyzes on-premises server specifications and recommends appropriately sized EC2 instances based on CPU, memory, and performance requirements.
+ **Flexible pricing models** – Compare On-Demand, Reserved Instances, and both Compute Savings Plans and EC2 Instance Savings Plans side by side to reflect committed-use discounts in your business case.
+ **SQL Server assessment** – Specialized analysis for SQL Server migrations to Amazon RDS or EC2, including BYOM/LI licensing options and Database Savings Plans (up to 20% savings).
+ **Storage assessment** – Assess on-premises storage for migration to Amazon S3, Amazon EBS, and Amazon FSx for NetApp ONTAP. Upload a storage inventory (such as an RVTools export) and AWS Transform maps each workload to a target service, sizes it, and estimates cost—including Single-AZ and Multi-AZ pricing for FSx for NetApp ONTAP.
+ **Streaming assessment** – Assess self-managed Apache Kafka clusters for migration to Amazon MSK Express, with a recommended broker configuration and a TCO estimate across broker hours, storage, data-in, and cross-AZ transfer.
+ **Business value assessment** – Evaluates staff productivity gains, resilience improvements, and business agility beyond infrastructure cost savings.
+ **Sustainability** – Estimates carbon footprint reduction from migrating to AWS.
+ **Multi-scenario comparison** – Create multiple scenarios with different assumptions (pricing models, regions, instance families, licensing) and compare side by side with what-if analysis.
+ **Chat-based interaction** – Refine assessments interactively through natural language. Supports rough estimation with limited data, adding inventory through chat, and modifying costs on the fly.
+ **Deliverable generation** – Generate executive presentations (PPTX) and detailed reports (PDF) directly from assessment results.

AWS Transform accepts inventory data from multiple sources including the AWS Transform Discovery Tool, RVTools (VMware), CMDB exports, Migration Evaluator, partner discovery tools, and MPA format files.

Use assessments at the start of your migration journey to build the business case, inform planning, and gain executive approval.

To learn more, see [Migration assessments](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-assessments.html) in the AWS Transform User Guide.

### AWS Transform for migrations (including VMware)
<a name="aws-transform-migrations"></a>

AWS Transform for migrations accelerates enterprise cloud migrations with purpose-built AI agents that automate the entire lifecycle—from discovery and wave planning through network conversion and cutover. By unifying teams, tools, and workflows in a single collaborative workbench, migrations that once took years now complete in months.

Originally launched for VMware, the service now migrates virtual and bare metal servers from virtually any source—VMware, Hyper-V, and other platforms—and the web application workflow has been renamed from "VMware Migrations" to "Migrations (including VMware)." Key capabilities include:
+ **Intelligent wave planning** – AI agents analyze application dependencies, business priorities, and technical constraints to group workloads into optimized migration waves. What once required weeks of manual effort now takes minutes.
+ **Migration strategy (7Rs) recommendations** – Analyze discovered inventory to get a migration strategy recommendation for every server and application, following the industry-standard seven migration strategies (7Rs). Each recommendation includes a suggested AWS target service, a confidence score, and the reasoning behind it, with interactive HTML, PDF, or PowerPoint output.
+ **Landing zone creation** – Automates generation of Landing Zone Accelerator (LZA) configurations with secure, multi-account AWS environments, consistent governance, and security controls. Supports CloudFormation, CDK, Terraform, and LZA formats, plus an IaC-only flow and brownfield scenarios (existing AWS Control Tower landing zones and AWS Organizations) via a Delegated Administrator connector.
+ **Automated network conversion** – Converts complex on-premises network configurations into AWS equivalents (VPCs, subnets, transit gateways) up to 80x faster than manual methods. You can import a source network, apply a source security posture to existing VPCs, or design a new AWS network from your requirements, with existing-VPC/CIDR-conflict detection and security group modernization.
+ **Rehost or replatform** – Manages the full rehosting lifecycle (agent deployment, test instances, cutover orchestration) or replatforms applications to containers on Amazon ECS or Amazon EKS in the same workflow. **AWS Transform MGN** (formerly AWS Application Migration Service) is the underlying replication engine—use the AWS Transform MGN console for direct control, or the agentic workflow for end-to-end automation.
+ **Block storage migration** – Migrate block storage directly to Amazon FSx for NetApp ONTAP (now generally available) or Amazon EBS within the same migration wave, removing the need for intermediate storage platforms or separate tools.
+ **Post-launch actions** – Automate modernization and validation tasks on each source server immediately after launch using AWS Systems Manager, with predefined or custom SSM documents defined at the account level or per server.

The service supports first-party AWS agents, third-party partner agents, and custom Bring Your Own Agent workflows.

To learn more, see [AWS Transform for VMware migrations](https://aws.amazon.com/transform/migrations/).

Watch the following video from re:Invent 2025 on how to complete a large-scale migration with agentic AI: [Reimagining large-scale migration planning with agentic AI](https://www.youtube.com/results?search_query=reimagining+large-scale+migration+planning+agentic+ai+reinvent+2025).

### AWS Transform for Windows modernization
<a name="aws-transform-windows"></a>

AWS Transform accelerates full-stack Windows modernization by up to 5x across application, UI framework, database, and deployment layers. Using the specialized Windows modernization agent, teams can modernize .NET applications, SQL Server databases, and deployment processes—reducing operating costs by up to 70% by moving away from costly licenses.

Key capabilities include:
+ **.NET framework modernization** – Upgrades legacy .NET Framework applications to .NET 8\+ (cross-platform), enabling containerization and Linux deployment.
+ **SQL Server migration** – Automates database modernization from SQL Server to open-source engines (PostgreSQL, MySQL) or AWS-managed databases. Supports offline source transformation: modernize SQL Server to Amazon Aurora PostgreSQL from uploaded DDL files, without a live database connection.
+ **UI framework upgrades** – Modernizes legacy UI frameworks (for example, Web Forms to Blazor or React).
+ **Deployment modernization** – Converts traditional IIS deployments to containerized microservices on Amazon ECS or Amazon EKS.

In addition to the AWS Transform web console, a Visual Studio extension (VSIX) provides an integrated IDE experience for .NET modernization.

To learn more, see [AWS Transform for Windows](https://aws.amazon.com/transform/windows/).

### AWS Transform for mainframe modernization
<a name="aws-transform-mainframe"></a>

AWS Transform accelerates mainframe application modernization from years to months. The specialized mainframe agent streamlines the entire transformation process—from initial analysis and planning to code refactoring and application reimagining—reducing risk and costs.

Key capabilities include:
+ **Codebase analysis** – Analyzes COBOL, PL/I, JCL, and other mainframe languages to map dependencies, detect missing artifacts, and assess complexity with visual dependency representations.
+ **Automated refactoring** – Converts mainframe code to modern languages (Java, C\#) while preserving business logic. Works with Claude Code and other agentic IDEs for the forward engineering phase.
+ **Traceable reimagine workflow** – A connected, traceable experience from assessment through code generation: assess a z/OS COBOL and PL/I portfolio to identify discrete business functions, extract business rules, generate development-ready requirements, and produce traceable cloud-native code, with every requirement traced back to the source code.
+ **Data migration** – Migrates mainframe data stores (VSAM, IMS DB, Db2) to cloud-native databases.
+ **Testing and validation** – Automated equivalence testing to ensure functional parity between legacy and modernized applications.

To learn more, see [AWS Transform for mainframe](https://aws.amazon.com/transform/mainframe/).

### AWS Transform custom (code modernization)
<a name="aws-transform-custom"></a>

AWS Transform custom is the agentic AI service for eliminating technical debt at scale. It transforms any code pattern—from any language, framework, or runtime to any other—through both built-in (AWS managed) and custom transformation recipes.

Key capabilities include:
+ **Built-in transformations** – Ready out-of-the-box for common scenarios:
  + Java, Python, Node.js version upgrades (Lambda and non-Lambda)
  + AWS SDK v1 to v2 upgrades
  + Java X86 to Graviton
  + Log4J to SLF4J
  + Angular to React / Angular version upgrades / Vue upgrades
  + Spring Boot upgrades, JBoss to Spring Boot
  + Comprehensive code analysis and tech debt reporting
+ **Custom transformations** – Create your own for any-to-any use cases. Define transformation requirements in natural language, test on sample repositories, then apply at enterprise scale. Supports diverse scenarios from language translations (Progress 4GL to Java, C to Rust, COBOL to Java) to architectural changes (X86 to Graviton, microservices decomposition).
+ **Model-to-model migration** – A custom transformation that assesses generative AI workloads and produces a plan for moving from third-party providers (OpenAI, Google Gemini, Anthropic SDK, open-source models via LiteLLM/Ollama) to Amazon Bedrock, with transparent cost comparisons and production-ready code changes.
+ **Continuous modernization** – Generally available autonomous tech debt analysis and remediation at scale: connect GitHub organizations, GitLab groups, and Bitbucket workspaces, run analyses on demand or on a schedule, prioritize findings, and open pull or merge requests with the fixes.
+ **Continual learning** – The agent learns from each execution, becoming smarter when applied repeatedly to similar repositories.
+ **Scale** – CLI-based interface that acts on one or multiple repositories. Integrates with CI/CD platforms for continuous modernization. Can run from laptop, EC2, ECS/EKS containers, or any pipeline.
+ **IDE integration** – Available through Kiro Power (VS Code extension), as well as agent skills for Claude Code, Cursor, and Codex.
+ **Modernization Analysis (MODA)** – Scans code for cloud-native maturity gaps and maps findings to AWS modernization pathways. Completes in 5–30 minutes per repository.
+ **Agentic Readiness Analysis (ARA)** – Evaluates whether systems are ready to be safely called by AI agents, covering APIs, identity, state management, human-in-the-loop controls, and observability.
+ **Campaign management** – Web experience for managing large-scale transformation campaigns, tracking progress across multiple repositories.

To learn more, see [AWS Transform custom](https://aws.amazon.com/transform/custom/).

## Latest innovations
<a name="aws-transform-innovations"></a>

AWS Transform continues to expand capabilities. Recent launches include:
+ **AWS Transform MGN** – AWS Application Migration Service (MGN) is now AWS Transform MGN, the replication engine powering AWS Transform, available in all commercial Regions and both AWS GovCloud (US) Regions while retaining existing compliance certifications.
+ **Migrations beyond VMware** – Migrate virtual and bare metal servers from virtually any source (VMware, Hyper-V, and other platforms), with the workflow renamed to "Migrations (including VMware)."
+ **Continuous modernization (GA)** – Autonomous, scheduled tech debt analysis and remediation across GitHub, GitLab, and Bitbucket repositories, with automated pull/merge requests.
+ **7Rs migration strategy recommendations** – Per-server and per-application strategy recommendations with confidence scores, exportable as HTML, PDF, or PowerPoint.
+ **BI migration agents** – Partner-built agents (Wavicle Data Solutions) convert Power BI and Tableau dashboards to Amazon Quick (QuickSight) assets within the AWS Transform workflow.
+ **MCP integration** – Invoke transformation capabilities directly from orchestrators, IDEs, and coding environments using Model Context Protocol.
+ **Kiro Power and agent skills** – Pre-built playbooks and individual tasks accessible from Kiro, Claude Code, Cursor, and Codex.
+ **Web-to-IDE handoff** – Start modernization jobs in the web console, then hand off to developer IDEs for human-in-the-loop edits and refinement.
+ **Agent builder toolkit** – Extend AWS Transform with custom agents using Kiro Power combined with the AWS Transform base agent and SDK.
+ **Expanded regions** – Migration capabilities added in Asia Pacific (Singapore) and AWS GovCloud (US-West), supporting all commercial Regions as migration targets (excluding Middle East (Bahrain) and Middle East (UAE)); mainframe modernization added in South America (São Paulo); custom available across eight Regions.
+ **FedRAMP Class C authorization** – AWS Transform is in scope for FedRAMP Class C (formerly Moderate baseline) in US East (N. Virginia), with AWS Transform MGN in scope for FedRAMP Class D.
+ **CloudWatch metrics** – Monitor cost, success/failure rates, and agent minutes.

For the latest updates, see [AWS Transform – Latest Innovations](https://aws.amazon.com/blogs/aws/category/artificial-intelligence/generative-ai/aws-transform/) and the [AWS Transform change log](https://docs.aws.amazon.com/transform/latest/userguide/change-log.html).

## Benefits
<a name="aws-transform-benefits"></a>

The following are the primary benefits of using AWS Transform:
+ **Accelerate modernization** – Modernize Windows, mainframe, and VMware applications up to 5x faster with agentic AI–powered automation of analysis, planning, documentation, and transformation tasks.
+ **Deliver at scale** – Transform hundreds of applications in parallel. AWS Transform automates high-effort, repeatable tasks so teams can deliver larger, more complex projects faster.
+ **Reduce costs** – Remove legacy infrastructure, licensing, and modernization costs. Customers report up to 70% reduction in operating costs by moving away from costly licenses.
+ **Specialized agents built on AWS expertise** – Achieve consistent, reliable outcomes using AI agents built on 20 years of AWS migration and modernization experience.
+ **Unified collaboration** – Shared workspaces and natural language chat enable cross-functional teams (project managers, architects, developers, security engineers) to work together in real time.
+ **Flexible tooling** – Use AWS Transform from the web console, CLI, IDE (Kiro, VS Code), or through MCP integration with your preferred orchestrators and coding environments.

## How to access AWS Transform
<a name="aws-transform-access"></a>

The following table describes the interfaces you can use to access AWS Transform.


| Interface | Description | 
| --- | --- | 
| Web console | AWS Transform console ([https://console.aws.amazon.com/transform](https://console.aws.amazon.com/transform))—collaborative workbench for planning and tracking | 
| CLI | Command-line interface for automation, CI/CD integration, and batch operations | 
| IDE (Kiro Power) | VS Code extension and Kiro IDE for developer-centric workflows | 
| Visual Studio (VSIX) | Visual Studio extension for .NET modernization | 
| Agent skills | Pre-built plugins for Claude Code, Cursor, and Codex | 
| MCP | Model Context Protocol integration for orchestrators and custom toolchains | 

AWS Transform supports IAM role authentication, so you can use your existing AWS credentials to create an environment, workspace, and transformation job from the IDE or web app. You can also configure a customer-owned Amazon S3 artifact store, optionally encrypted with your own AWS KMS key.

## Customer success
<a name="aws-transform-customers"></a>

The following are publicly available case studies of customers using AWS Transform:


| Customer | Use case | Outcome | Reference | 
| --- | --- | --- | --- | 
| IDEMIA | .NET modernization | 4x faster, 30% cost reduction | [Case study](https://aws.amazon.com/solutions/case-studies/idemia-case-study/) | 
| Thomson Reuters | Windows/.NET modernization | 4x faster modernization | [Case study](https://aws.amazon.com/solutions/case-studies/thomson-reuters-case-study/) | 
| Bridgestone | Mainframe modernization | Completed in 7 months, 90% efficiency gains | [Case study](https://aws.amazon.com/solutions/case-studies/bridgestone-case-study/) | 
| CSL | VMware migration (5,000 servers, 29 data centers) | 10x faster planning, 30% operational cost savings | [Case study](https://aws.amazon.com/solutions/case-studies/csl-agenticai/) | 
| ADP | Compliance infrastructure | Reimagined with AWS Transform | [Case study](https://aws.amazon.com/solutions/case-studies/adp-case-study/) | 
| Toyota | Mainframe modernization | Accelerated with generative AI | [Case study](https://aws.amazon.com/solutions/case-studies/toyota-transform-case-study/) | 
| Vector | VMware migration | 34% faster than traditional methods | [Case study](https://aws.amazon.com/solutions/case-studies/vector-limited-case-study/) | 
| Mercedes-Benz | SAP modernization | RISE with SAP on AWS | [Case study](https://aws.amazon.com/solutions/case-studies/mercedes-benz-transform-case-study/) | 

## Getting started
<a name="aws-transform-getting-started"></a>

To get started with AWS Transform, use the following resources:
+ **Web experience** – Access [AWS Transform](https://console.aws.amazon.com/transform) in the AWS Management Console.
+ **User guide** – See the [AWS Transform User Guide](https://docs.aws.amazon.com/transform/latest/userguide/) for detailed instructions.
+ **Blog** – Read [One year. 4.5 billion lines of code. 1.6 million hours saved](https://aws.amazon.com/blogs/migration-and-modernization/aws-transform-one-year-milestone/) for an overview of impact and lessons learned.
+ **Migration Launch Guide** – This guide provides context on the broader migration journey and how AWS Transform fits within it.
+ **Partners** – Explore [AWS Transform Partners](https://aws.amazon.com/transform/partners/) for assistance with your transformation initiative.

For more information, contact your AWS account team.
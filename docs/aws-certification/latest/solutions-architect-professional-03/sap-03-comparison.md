

# Comparison of SAP-C02 and SAP-C03
<a name="sap-03-comparison"></a>

**Topics**
+ [Side-by-side comparison](#sap-03-comparison-side-by-side)
+ [Additions of content for SAP-C03](#sap-03-comparison-additions)
+ [Deletions of content for SAP-C03](#sap-03-comparison-deletions)
+ [Recategorizations of content for SAP-C03](#sap-03-comparison-recategorizations)
+ [Changes to in-scope and out-of-scope services and features](#sap-03-comparison-services-changes)

## Side-by-side comparison
<a name="sap-03-comparison-side-by-side"></a>

The following table shows the content domains and the percentage of scored questions in each content domain for the SAP-C02 exam (in use until November 16, 2026) and the SAP-C03 exam (in use beginning November 17, 2026).


<table>
<thead>
  <tr><th>SAP-C02 Content Domain</th><th>SAP-C02 %</th><th>SAP-C03 Content Domain</th><th>SAP-C03 %</th></tr>
</thead>
<tbody>
  <tr><td>Domain 1: Design Solutions for Organizational Complexity</td><td>26%</td><td>Domain 1: Architecture Design and Implementation Built for the Cloud</td><td>25%</td></tr>
  <tr><td>Domain 2: Design for New Solutions</td><td>29%</td><td>Domain 2: Security, Compliance, and Governance</td><td>25%</td></tr>
  <tr><td>Domain 3: Continuous Improvement for Existing Solutions</td><td>25%</td><td>Domain 3: Cost-Optimized Architecture Design</td><td>15%</td></tr>
  <tr><td>Domain 4: Accelerate Workload Migration and Modernization</td><td>20%</td><td>Domain 4: Resilience, Migration, and Business Continuity</td><td>15%</td></tr>
  <tr><td colspan="2"></td><td>Domain 5: Operational Excellence and Automation</td><td>20%</td></tr>
</tbody>
</table>


## Additions of content for SAP-C03
<a name="sap-03-comparison-additions"></a>

In Task 1.1 (Design architectures built for the cloud), the following content was added:
+ Design serverless data processing and analysis pipelines (for example, by using Amazon Kinesis Data Streams, AWS Glue, Amazon Athena, AWS Lambda).
+ Design multi-step workflows that have durable execution patterns (for example, by using AWS Step Functions, durable Lambda functions).
+ Design service mesh architectures that facilitate microservice communication and observability (for example, by using Amazon VPC Lattice, Amazon ECS Service Connect).
+ Manage container images by configuring security scans and lifecycle policies (for example, by using Amazon ECR).
+ Design ingress patterns and optimize resources for specific usage patterns (for example, Application Load Balancer, Network Load Balancer, AWS Load Balancer Controller, Amazon API Gateway).
+ Design architectures that support real-time data processing by using WebSocket and publish-subscribe patterns (for example, by using API Gateway WebSocket APIs).
+ Design multi-tenant architectures that use tenant isolation patterns (for example, siloed or pooled resources, Amazon Cognito tenant context, row-level security, tenant-specific encryption).

In Task 1.2 (Integrate AI and ML services into architectures), the following content was added:
+ Design generative AI integrations for applications, including for multi-account deployment patterns (for example, by using Amazon Bedrock).
+ Design AI agent architectures that integrate with tools (for example, by using Amazon Bedrock AgentCore, Amazon Bedrock Knowledge Bases).
+ Design ML inference architectures (for example, Amazon SageMaker AI endpoints).
+ Design RAG architectures, including ingestion and retrieval strategies (for example, Amazon Bedrock knowledge bases that use vector stores).

In Task 1.3 (Design hybrid cloud integration patterns), the following content was added:
+ Design hybrid compute patterns (for example, by using Amazon EKS Anywhere, Amazon ECS Anywhere, AWS Outposts, AWS Local Zones).

In Task 1.4 (Design network architectures), the following content was added:
+ Design IPv6 adoption and dual-stack migration strategies.

In Task 1.5 (Design data, storage, and database architectures), the following content was added:
+ Design data lake and lakehouse architectures (for example, by using Amazon S3, AWS Lake Formation, Amazon Redshift Spectrum, Apache Iceberg).
+ Design real-time and batch analytics pipelines (for example, by using Amazon EMR, Amazon Redshift, Amazon Managed Streaming for Apache Kafka [Amazon MSK], Amazon AppFlow).
+ Design data cataloging and cross-account data sharing patterns (for example, AWS Glue Data Catalog, Lake Formation, AWS Clean Rooms).

In Task 2.1 (Design identity security architectures), the following content was added:
+ Design application authentication and authorization solutions (for example, by using Amazon Cognito user pools, identity pools, OAuth 2.0, Amazon EKS Pod Identity).
+ Design workload identities for hybrid and multi-cloud environments (for example, by using IAM Roles Anywhere).

In Task 2.2 (Design solutions to implement encryption and key management strategies), the following content was added:
+ Design post-quantum cryptography strategies (for example, by using AWS KMS with Module-Lattice Digital Signature Algorithm [ML-DSA], Module-Lattice-Based Key-Encapsulation Mechanism [ML-KEM]).

In Task 2.4 (Design architectures to meet compliance requirements), the following content was added:
+ Design data residency controls such as Region-specific deployments and transfer restrictions.
+ Implement compliance evidence collection and reporting solutions (for example, by using AWS Artifact).
+ Implement risk assessment solutions for cloud architectures such as threat modeling and mitigation strategies.

In Task 2.5 (Design security and responsible AI controls), the following content was added:
+ Implement content filtering and compliance controls for generative AI services (for example, by using Amazon Bedrock Guardrails).
+ Implement access controls for generative and agentic AI applications (for example, by using Amazon Bedrock AgentCore Identity).
+ Design human oversight workflows that include approval mechanisms for AI operations (for example, by using AWS Step Functions).

In Task 3.1 (Design architectures based on AWS pricing models), the following content was added:
+ Optimize costs for AI/ML workloads by selecting the appropriate service tier, implementing batching strategies, and designing caching patterns (for example, by using Amazon Bedrock, Amazon SageMaker AI).

In Task 3.2 (Optimize data transfer and network costs), the following content was added:
+ Optimize data transfer costs for AI/ML workloads by using strategies such as cross-Region inference routing.

In Task 3.4 (Optimize storage and database costs), the following content was added:
+ Design cost-effective observability solutions that include features such as log filtering, metric aggregation, and retention optimization.

In Task 4.2 (Design disaster recovery architectures), the following content was added:
+ Implement multi-cluster container strategies to provide high availability and disaster recovery (for example, by using Amazon EKS, Amazon ECS).

In Task 5.2 (Design CI/CD and DevSecOps pipelines), the following content was added:
+ Implement security scanning in pipelines to assess vulnerabilities and sign artifacts (for example, by using Amazon Inspector, Amazon ECR image scanning).
+ Configure multi-account and multi-Region deployment pipelines that include features such as role delegation and artifact promotion (for example, by using CodePipeline cross-account deployments).
+ Evaluate AI/ML applications and validate outputs (for example, by using Amazon Bedrock Evaluations).

In Task 5.3 (Design observability and monitoring solutions), the following content was added:
+ Implement monitoring for containerized applications (for example, by using Amazon ECS, Amazon EKS with Container Insights).
+ Monitor metrics for AI/ML workloads, including model performance, AI agent performance, inference latency, and model drift.
+ Design monitoring solutions for the user experience by using strategies such as synthetic transactions and real user monitoring (for example, by using Amazon CloudWatch Synthetics, Amazon CloudWatch RUM).

In Task 5.4 (Design operational automation and resilient systems), the following content was added:
+ Configure controlled remediation solutions that have safety constraints (for example, circuit breakers, rate limits, bulkhead patterns, retry patterns with exponential backoff).
+ Configure automated runbooks and incident response procedures for operational tasks such as patching, remediation, and scaling.

## Deletions of content for SAP-C03
<a name="sap-03-comparison-deletions"></a>

In C02 Content Domain 2, Task 1, the following content was removed:
+ Application upgrade path
+ Delegating to AWS

In C02 Content Domain 4, Task 2, the following content was removed:
+ Migration-tool security

These concepts might still be implicit in other C03 skills. Being absent from the blueprint text does not mean that these concepts are fully out of scope for the exam.

## Recategorizations of content for SAP-C03
<a name="sap-03-comparison-recategorizations"></a>

SAP-C03 consolidated multiple granular skills from SAP-C02 into more comprehensive tasks in SAP-C03. These consolidations do not result in a decreased emphasis on essential skills. Rather, the exam has been reorganized to reduce repetition and ensure consistency in level of detail across all domains. The following list describes the before/after for these consolidations.

The following tasks from SAP-C02 have been consolidated into Task 1.1 for SAP-C03:
+ Task 1.4: Cross-account and cross-Region event routing patterns
+ Task 2.4:
  + Stateless applications with externalized state management
  + Auto scaling patterns for serverless and containerized workloads
+ Task 3.3: Edge architectures for latency requirements
+ Task 4.4:
  + Event-driven architectures (messaging patterns, idempotency, ordering)
  + Container orchestration for microservices

The following tasks from SAP-C02 have been consolidated into Task 1.3 for SAP-C03:
+ Task 4.2: Data synchronization strategies for hybrid workloads
+ Task 4.4: Integration patterns to modernize legacy systems

The following tasks from SAP-C02 have been consolidated into Task 1.4 for SAP-C03:
+ Task 1.1: VPC architectures with subnet strategies and IP address management
+ Task 1.2: Network security architectures (traffic inspection, filtering)

The following tasks from SAP-C02 have been consolidated into Task 1.5 for SAP-C03:
+ Task 2.4: Database scaling solutions for high availability

The following tasks from SAP-C02 have been consolidated into Task 2.1 for SAP-C03:
+ Task 1.2:
  + Identity federation using standard protocols
  + Least-privilege access controls (cross-account access, temporary credentials)
  + Data perimeter controls and external access validation

The following tasks from SAP-C02 have been consolidated into Task 2.2 for SAP-C03:
+ Task 1.2: Dedicated hardware security modules for compliance

The following tasks from SAP-C02 have been consolidated into Task 2.3 for SAP-C03:
+ Task 1.4:
  + Organizational structures with guardrails and landing zones
  + Centralized logging and configuration management
  + Policy enforcement using SCPs and RCPs
+ Task 3.2: Automated compliance monitoring

The following tasks from SAP-C02 have been consolidated into Task 2.4 for SAP-C03:
+ Task 3.2:
  + Solutions to meet regulatory requirements (data sovereignty)
  + Audit trail management for regulated workloads

The following tasks from SAP-C02 have been consolidated into Task 3.1 for SAP-C03:
+ Task 2.5: Rightsizing and scaling strategies based on performance
+ Task 2.6: Cost-optimized architectures for workload requirements (Graviton, Step Functions, Lambda)

The following tasks from SAP-C02 have been consolidated into Task 3.2 for SAP-C03:
+ Task 2.6:
  + Data transfer cost optimization (private connectivity, Regional patterns)
  + Cost-aware multi-Region data replication
  + Cost-effective network architectures (AWS Transit Gateway, AWS PrivateLink pricing)
+ Task 3.3: Content delivery architectures and caching strategies

The following tasks from SAP-C02 have been consolidated into Task 3.3 for SAP-C03:
+ Task 1.5: Policy-based tagging enforcement for cost allocation
+ Task 3.5:
  + Chargeback and showback capabilities
  + Cost monitoring and alerting solutions (budgets, anomaly detection)

The following tasks from SAP-C02 have been consolidated into Task 3.4 for SAP-C03:
+ Task 1.3: Backup and disaster recovery with cost-optimized retention
+ Task 2.6:
  + Database cost optimization (capacity modes, reserved capacity)
  + Intelligent storage tiering and lifecycle policies
+ Task 3.5: Block storage cost optimization

The following tasks from SAP-C02 have been consolidated into Task 4.1 for SAP-C03:
+ Task 4.2: Rehosting strategies
+ Task 4.4:
  + Refactor strategies (microservices decomposition, serverless adoption)
  + Modernize legacy workloads (mainframes, applications, databases)

The following tasks from SAP-C02 have been consolidated into Task 4.2 for SAP-C03:
+ Task 2.2:
  + Multi-Region disaster recovery solutions
  + Disaster recovery testing and validation procedures
+ Task 3.1: Disaster recovery assessment and recovery procedures

The following tasks from SAP-C02 have been consolidated into Task 4.3 for SAP-C03:
+ Task 1.4: Centralized backup governance and cross-account backup policies
+ Task 3.1:
  + Failover tests and recovery time measurement (AWS Fault Injection Service, Amazon Route 53)
  + Chaos engineering with controlled failure scenarios
+ Task 3.2: Data protection against ransomware and accidental deletion

The following tasks from SAP-C02 have been consolidated into Task 5.1 for SAP-C03:
+ Task 1.4: Multi-account and multi-Region infrastructure deployments
+ Task 2.1: Infrastructure as code (declarative and imperative approaches)
+ Task 3.2:
  + Policy as code for validation, enforcement, and drift remediation
  + Secrets management in infrastructure code

The following tasks from SAP-C02 have been consolidated into Task 5.2 for SAP-C03:
+ Task 2.1: CI/CD solutions for automated build and deployment pipelines

The following tasks from SAP-C02 have been consolidated into Task 5.3 for SAP-C03:
+ Task 1.4: Multi-account log aggregation with cross-account subscriptions
+ Task 3.1: Observability with metrics, logs, and distributed tracing
+ Task 3.3: Service-level objectives (SLOs) with measurable indicators

The following tasks from SAP-C02 have been consolidated into Task 5.4 for SAP-C03:
+ Task 2.4: Auto scaling policies (target tracking, predictive scaling)
+ Task 3.1: Health monitoring, capacity planning, and operational responses

## Changes to in-scope and out-of-scope services and features
<a name="sap-03-comparison-services-changes"></a>

### Services added to the in-scope list
<a name="sap-03-comparison-services-added"></a>

The following services are new to the SAP-C03 in-scope list (not present in SAP-C02):
+ Amazon Bedrock
+ Amazon Data Lifecycle Manager
+ Amazon MemoryDB
+ Amazon Security Lake
+ Amazon Verified Permissions
+ Amazon VPC Lattice
+ AWS Application Auto Scaling
+ AWS CDK
+ AWS Clean Rooms
+ AWS Cloud WAN
+ AWS CodeCommit
+ AWS Cost Categories
+ AWS Data Transfer Terminal
+ AWS Distro for OpenTelemetry
+ AWS Fault Injection Service
+ AWS Local Zones
+ AWS Resilience Hub
+ AWS Transform
+ AWS Verified Access
+ Reserved Instances

### Services removed from the in-scope list
<a name="sap-03-comparison-services-removed"></a>

The following services were explicitly listed in SAP-C02 but are no longer present in the SAP-C03 in-scope list. SAP-C03 lists parent service names with sub-features implicitly included.

Entire categories removed:
+ All AWS IoT services (AWS IoT Core, AWS IoT Device Defender, AWS IoT Device Management, AWS IoT Events, AWS IoT Greengrass, AWS IoT SiteWise, AWS IoT Things Graph, AWS IoT 1-Click)
+ End User Computing (Amazon AppStream 2.0, Amazon WorkSpaces)
+ Media Services (Amazon Elastic Transcoder, Amazon Kinesis Video Streams)

Individual services replaced:
+ Individual AI/ML services were replaced by Amazon Bedrock and Amazon SageMaker AI as parent entries (Amazon Comprehend, Amazon Fraud Detector, Amazon Kendra, Amazon Lex, Amazon Personalize, Amazon Polly, Rekognition, Amazon Textract, Amazon Transcribe, Amazon Translate).

Individual services removed:
+ Amazon CodeGuru
+ Amazon Lightsail
+ Amazon Managed Blockchain (AMB)
+ Amazon Pinpoint
+ Amazon SES
+ AWS Amplify
+ AWS App Runner
+ AWS Batch
+ AWS CodeArtifact
+ AWS Data Exchange
+ AWS Device Farm
+ AWS Health Dashboard
+ AWS License Manager
+ AWS Proton
+ AWS Service Catalog
+ AWS Wavelength

### Services added to the out-of-scope list
<a name="sap-03-comparison-services-out-of-scope-added"></a>

The following services are newly added as out-of-scope in SAP-C03:
+ Amazon Braket
+ Amazon Comprehend Medical
+ Amazon Interactive Video Service (Amazon IVS)
+ Amazon Lightsail
+ Amazon RDS Custom for Oracle
+ Amazon Transcribe Medical
+ AWS DeepComposer
+ AWS DeepRacer
+ AWS Elemental MediaConvert
+ AWS Elemental MediaLive
+ AWS Ground Station
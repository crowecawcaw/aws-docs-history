# Architecture specifications with Kiro

After you configure your Kiro workspace and steering files, the next step is to generate application specifications. You create methodology steering files that guide Kiro through business logic analysis, domain-driven design, and microservices decomposition for your target architecture.

## Step 2: Generate application specifications

### Tailor specifications generation to your architecture design target

The specification generation process can be tailored to align with your target application architecture and organizational requirements. For applications targeting a microservices architecture, we follow a Domain-Driven Design (DDD) approach, as demonstrated in this tutorial, where Kiro analyzes the business logic extracted by AWS Transform to identify bounded contexts, aggregate roots, entities, and domain events, ultimately generating comprehensive microservice specifications with clear service boundaries and integration patterns.

Alternatively, for applications designed with a layered architecture, we can adopt a more traditional Software Requirements Specification (SRS) standard, focusing on functional and non-functional requirements organized by system layers and components.

Additionally, organizations may opt to define a custom approach that reflects their specific methodologies, architectural patterns, or industry standards, ensuring the specification generation process aligns with their unique development practices and governance requirements.

### Methodology steering files for a microservice architecture

In addition to the shared steering files, the specification generation step uses methodology-specific steering files. Place these alongside the other steering files under `.kiro/steering/`.

#### Business logic analysis methodology

This document describes the standardized methodology for analyzing Business Logic Extraction results from mainframe applications.

```
# Business Rules Extraction (BRE) Analysis Methodology
#​# Overview
This document describes the standardized methodology for analyzing Business Logic
Extraction results from mainframe applications, specifically for the CardDemo
application BRE output.
#​# Analysis Process
#​#​# Step 1: Identify the Entry Point
Location: input/bre_output/index.html
- This is the main navigation file for all extracted business logic
- Contains hierarchical structure of business functions and components
- Use this to understand the overall application structure
#​#​# Step 2: Locate Business Function Documentation
Location: input/bre_output/ApplicationLevelAnalysis/[BusinessFunctionName]/
Each business function folder contains:
- [BusinessFunctionName].json - Overview with key capabilities and components list
- [BusinessFunctionName].html - Human-readable overview
- entrypoint-[COMPONENT]/ - Subfolders for each component
#​#​# Step 3: Analyze Component Entry Points
Location: input/bre_output/ApplicationLevelAnalysis/[BusinessFunctionName]/entrypoint-[COMPONENT]/
Each entrypoint folder contains:
- entrypoint-[COMPONENT].json - Component summary with:
  - Business functions performed
  - Program flow (functionality_flow)
  - Datasource summary with access types (READ/WRITE/UPDATE)
  - Environment summary (workload type, database types, integration components)
  - Program paths
- entrypoint-[COMPONENT].html - Human-readable version
Key Information to Extract:
1. Business Functions: List of operations performed
2. Program Flow: Call hierarchy and program relationships
3. Datasources:
   - Name and original name
   - Type (VSAM_KSDS, CICS_FILE, MQ_QUEUE, SEQUENTIAL, etc.)
   - Access mode (READ, WRITE, UPDATE)
   - Business purpose
   - Programs that use it
4. Environment: Workload type (Transaction/Batch), database types, integration components
#​#​# Step 4: Review Detailed Program Documentation
Location: input/bre_output/aws-mainframe-modernization-carddemo-main/app/
Detailed program files are organized by type:
- cbl/[PROGRAM]-cbl.json - COBOL programs
- jcl/[JCL]-jcl.json - JCL jobs
- app-vsam-mq/cbl/[PROGRAM]-cbl.json - MQ-enabled COBOL programs
Each detailed JSON file contains:
1. Description: High-level program purpose
2. Flow Diagram Code: Mermaid diagram showing detailed process flow
3. Rules: Array of business rules with:
   - Rule_Id: Unique identifier
   - Rule_Name: Descriptive name
   - Rule_Description: What the rule does
   - Rule_Type: Process Rules, Validation Rules, Decision Rules, Action Rules,
     Computation Rules, Definitional Rules
   - Acceptance_Criteria: Given/When/Then format
Note: These JSON files are single-line formatted and may appear truncated.
They contain 40-100+ business rules per program.
```

#### Domain Driven Design methodology

This document describes the standardized methodology for applying Domain-Driven Design principles to business functions extracted from mainframe applications. This process transforms technical mainframe analysis into a modern DDD model with bounded contexts, aggregates, entities, value objects, and domain events.

```
# Domain-Driven Design (DDD) Analysis Methodology
#​# Overview
This document describes the standardized methodology for applying Domain-Driven
Design principles to business functions extracted from mainframe applications.
#​# Prerequisites
- Completed BRE (Business Rules Extraction) analysis
- Business function analysis document available
- Understanding of the business domain
- Knowledge of DDD tactical and strategic patterns
#​# DDD Analysis Process
#​#​# Step 1: Identify Bounded Contexts
Input: Business function analysis with components, datasources, and business capabilities
Criteria for Bounded Context Identification:
- Cohesion: Related concepts that change together
- Autonomy: Can be developed and deployed independently
- Business Alignment: Matches business organizational structure
- Data Ownership: Clear ownership of data entities
- Language Consistency: Consistent terminology within context
#​#​# Step 2: Define Ubiquitous Language
Input: Bounded contexts, business function documentation, datasource field definitions
#​#​# Step 3: Identify Aggregates and Aggregate Roots
Input: Bounded contexts, datasources, entity relationships, business rules
#​#​# Step 4: Define Entities
Input: Aggregates, datasource structures, business rules
```

#### Microservices specification methodology

This document describes the standardized methodology for generating comprehensive microservice specifications from DDD (Domain-Driven Design) analysis. This process transforms DDD design artifacts (bounded contexts, aggregates, entities, value objects, domain services, and use cases) into detailed, implementation-ready microservice specifications.

```
# Microservice Specification Generation Methodology
#​# Overview
This document describes the standardized methodology for generating comprehensive
microservice specifications from DDD analysis.
#​# Prerequisites
- Completed BRE (Business Rules Extraction) analysis
- Completed DDD analysis with traceability matrix
- Understanding of microservices architecture patterns
- Knowledge of the target technology stack
#​# Microservice Specification Generation Process
#​#​# Step 1: Identify Microservices from Bounded Contexts
#​#​# Step 2: Define Service Overview
#​#​# Step 3: Define Service Boundaries
#​#​# Step 4: Define Data Ownership
```

### Prompt for specification generation

Kiro specs are structured artifacts that formalize the development process for complex features in your application. They provide a systematic approach to transform high-level ideas into detailed implementation plans with clear tracking and accountability. From the Kiro pane, click the + button under Specs and describe your project idea using prompts.

Below is a sample prompt for Kiro to generate application specifications:

```
Ultimate AWS Microservices Implementation Prompt

Context:
You are tasked with implementing the customer-management-service microservice
architecture based on specifications in the microservices-specs folder. This project
requires both backend microservices development and a frontend implementation. The
system will follow modern microservices best practices on AWS, including proper
service isolation, communication patterns, deployment strategies, and AWS-native
integration.

Role:
You are a Senior AWS Solutions Architect and Full-Stack Developer with over 20
years of experience designing and implementing cloud-native applications. You have
deep expertise in Java Spring microservices, Angular frontend development, AWS
services integration, and microservices design patterns.

Action:
1. Begin by analyzing the provided microservices specifications from the
   microservices-specs folder, identifying each required microservice, its
   responsibilities, data models, and integration points.
2. Design the overall architecture for the customer-management-service microservices
   system, including:
   - Service boundaries and responsibilities
   - Data ownership and sharing approach
   - Communication patterns (synchronous vs asynchronous)
   - AWS service selection for each component
3. For the customer-service microservice identified in the specifications:
   - Create a backend project structure with appropriate configuration
   - Implement the data model mapping the customer DynamoDB table definition
     located under the datamodel folder
   - Develop RESTful API controllers following REST best practices
   - Implement service layer business logic as specified
   - Add appropriate exception handling, validation, and logging
   - Configure AWS service integrations (DynamoDB, SQS, SNS, etc. as appropriate)
   - Write unit tests for the service
```

### Generate specifications

Once you have reviewed the three specs and are satisfied that they accurately reflect the desired output, you have two options for execution:

- **Run tasks individually** – Execute each entry in tasks.md one‑by‑one, allowing you to monitor progress and intervene as needed.
- **Run all tasks at once** – Ask the Kiro agent to "Execute all tasks in the spec." Kiro will then generate the complete specification.

### Next steps before source code generation

The generated specifications provide a solid starting point, but before you generate the source code, a software architect / application subject matter expert should:

- Review and validate the generated specification
- Adapt those specifications according to business requirement changes

Only after this human‑in‑the‑loop verification and validation should you move to the next step which is the code generation.

Next: [Code generation with Kiro](transform-forward-engineering-tutorial-codegen.md "transform-forward-engineering-tutorial-codegen.md")

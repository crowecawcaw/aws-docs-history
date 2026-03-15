# Tutorial: Reimagining mainframe applications with exported artifacts from AWS Transform for mainframe

This tutorial walks you through how to leverage modernization outputs from your AWS Transform and use Kiro or any Spec-Driven IDE to generate modernized applications from mainframe COBOL and JCL code.

The example showcases the modernization of a simplified Customer Account Processing application, transforming COBOL code into equivalent Java microservices, complete with REST APIs, entity mappings, and automatically translated business rules. In this tutorial, we use Kiro as our IDE to demonstrate how to use AWS Transform output for reimagining the application.

## Overview

In this tutorial, you will:

- Prepare your modernization outputs and Kiro workspace
- Generate target application specifications using methodology steering files and prompts
- Generate source code, tests, and optionally boost quality with Kiro Hooks

## Prerequisites

Before beginning this tutorial, ensure you have:

- Mainframe application source code
- Kiro IDE installed locally
- Access to outputs from AWS Transform for mainframe, including:
  - Dependency and data analysis results
  - Technical documentation
  - Business documentation

- Java 17+ and Maven 3.9+ installed (for validating generated code)

## Step 1: Prepare modernization outputs

Upon completion of your mainframe modernization job within AWS Transform, the service generates outputs stored in your designated S3 bucket. Download these artifacts to a local workspace that Kiro can access for the modernization process.

The S3 bucket stores the results of each Transform job in a hierarchical layout that makes it easy to locate the artifacts produced by a particular run. The structure is:

```
/your-s3-bucket/transform-output/your-jobid/
├── 1/
    ├── business-documentation/
    ├── data_analysis/
    ├── decomposition/
    ├── documentation/
├── inputs/
```

- `your-jobid` – A unique identifier that groups together everything generated for a single logical job (e.g., a migration or conversion request).
- `1/` – The first execution of that job. If you need to run the job again, a new numeric folder (2/, 3/, …) will be created alongside the existing one, preserving the output of each execution attempt.
- Sub‑folders under `1/` – These folders hold the outputs from the first run; select only the documents that are relevant to your re‑imagined project, as you may not need every file.
  - `business‑documentation` – contains the extracted business logic for the entire application, in a zip archive.
  - `data_analysis` – provides data‑lineage visibility for data modernization and generates data dictionaries with business meanings.
  - `decomposition` – holds workloads grouped into business domains as identified by the BLE agent.
  - `documentation` – includes technical documents that explain the mainframe application.
  - `inputs` – The inputs folder stores the original source artifacts of the mainframe application—COBOL code, JCL scripts, copybooks, and related configuration files.

Import all these files into the root of your Kiro project workspace.

## Prepare your Kiro workspace

Kiro is an agentic IDE that helps you do your best work by bringing structure to AI coding with spec-driven development with features such as specs, steering, and hooks. Specs or specifications are structured artifacts that formalize the development process for complex features in your application. Steering gives Kiro persistent knowledge about your workspace through markdown files. Agent hooks are powerful automation tools that streamline your development workflow by automatically executing predefined agent actions when specific events occur in your IDE.

Steering files give Kiro persistent knowledge of your forward engineering workspace through markdown files. Instead of explaining your conventions in every chat, these files ensure Kiro consistently follows your established patterns, libraries, and standards throughout your project.

Place the steering files in the root of your workspace under `.kiro/steering/`.

### Product Overview (product.md)

Defines your product's purpose, target users, key features, and business objectives. This helps Kiro understand the "why" behind technical decisions and suggest solutions aligned with your product goals. A sample product.md looks like:

```
Product Requirements — COBOL/JCL Business Rules Only

CRITICAL PRINCIPLE: COBOL/JCL BUSINESS RULES ONLY

ABSOLUTE REQUIREMENT: Implement ONLY the business rules explicitly defined in COBOL/JCL programs for CustomerAccountManagement Business Function ONLY.
- NO industry standards
- NO assumptions about validation logic
- NO inferences from incomplete COBOL/JCL rules
- ONLY explicit COBOL/JCL business rule specifications

COBOL/JCL Business Rule Implementation

Rule Discovery & Implementation
1. Locate Entry Points: ApplicationLevelAnalysis/*/entrypoint-*/
2. Locate Program Paths: Search cbl/ jcl programs mentioned in the Entry point files. cbl/jcl programs are located at program_paths.
3. Locate COBOL Program Rules: Search carddemo-v2-main/app/cbl/*.json
4. Locate JCL Program Rules: Search carddemo-v2-main/app/jcl/*.json
5. Extract Components: Rule_Id, Rule_Name, Rule_Description, Acceptance_Criteria, Rule_Type
6. Implementation: Group related COBOL/JCL rules into single methods with exact specification

MANDATORY Code Documentation:
/**
 * <Rule_Id>COBOL_OR_JCL_RULE_ID_1</Rule_Id>
 * <Rule_Description>Brief description from COBOL/JCL rule</Rule_Description>
 * <Acceptance_Criteria>Given/When/Then criteria from COBOL/JCL rule</Acceptance_Criteria>
 *
 * <Rule_Id>COBOL_OR_JCL_RULE_ID_2</Rule_Id>
 * <Rule_Description>Brief description from related COBOL/JCL rule</Rule_Description>
 * <Acceptance_Criteria>Given/When/Then criteria from related COBOL/JCL rule</Acceptance_Criteria>
 */
```

### Technology Stack (tech.md)

Documents your chosen frameworks, libraries, development tools, and technical constraints. When Kiro suggests implementations, it will prefer your established stack over alternatives. A sample tech.md looks like:

```
Technology Stack & Implementation Standards

Technology Stack

Backend (LTS Only)
- Java: Eclipse Temurin LTS (Java 17)
- Spring Boot: Latest LTS 3.x
- Database: H2 (testing), Aurora PostgreSQL (production)
- Build: Maven wrapper (./mvnw) only

Frontend
- Framework: React + TypeScript
- State Management: Redux Toolkit
- API Client: Axios with error handling
- Styling: AWS Cloudscape Design System

AWS Infrastructure
- Database: Amazon RDS Aurora PostgreSQL
- Compute: ECS Fargate
- Load Balancing: ALB
- Registry: Amazon ECR
- Monitoring: CloudWatch
- CI/CD: AWS CodeBuild
- IaC: AWS CDK (v2)
```

### Project Structure (structure.md)

Outlines file organization, naming conventions, import patterns, and architectural decisions. This ensures generated code fits seamlessly into your existing codebase. A sample structure.md looks like:

```
Project Structure & Data Organization

Project Structure

COBOL Artifact Locations
- Extracted business rules for each COBOL/JCL file: carddemo-v2-main/app/*
- Copybooks: source-code/cpy/
- Entry Points: ApplicationLevelAnalysis/*/entrypoint-*/

Data Loading Strategy
- Use DataInitializationService with CSV parsing
- Match CSV headers to copybook field names
- Active only with appropriate testing profile

COBOL/JCL Business Rule Discovery Process

Step-by-Step Rule Location
1. Locate Entry Points: Navigate to ApplicationLevelAnalysis/*/entrypoint-*/
2. Find Program References: Search cbl/ jcl programs mentioned in the Entry point files
3. Extract COBOL Rules: Search carddemo-v2-main/app/cbl/*.json for business rules
4. Extract JCL Rules: Search carddemo-v2-main/app/jcl/*.json for business rules
5. Parse Rule Components: Extract Rule_Id, Rule_Name, Rule_Description, Acceptance_Criteria, Rule_Type
```

These foundation files are included in every interaction by default, forming the baseline of Kiro's project understanding.

### The Kiro specification workflow

Using the steering files and prompts you provide, Kiro automatically creates three core documents that become the backbone of every specification:

- `requirements.md` - Captures user stories and acceptance criteria in structured EARS notation
- `design.md` - Documents technical architecture, sequence diagrams, and implementation considerations
- `tasks.md` - Provides a detailed implementation plan with discrete, trackable tasks

These specifications are living documents. You can edit any of them at any time—adding, removing, or refining details as your understanding of the project evolves. Kiro's design encourages continuous refinement, so the specs remain synchronized with shifting requirements and design decisions, giving you a reliable foundation for development.

Next: [Architecture specifications with Kiro](transform-forward-engineering-tutorial-specs.md "transform-forward-engineering-tutorial-specs.md")

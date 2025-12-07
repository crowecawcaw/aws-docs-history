# Tutorial: Reimagining mainframe applications with exported artifacts from AWS Transform for mainframe

This tutorial walks you through how to leverage modernization outputs from your AWS Transform and use Kiro or any Spec-Driven IDE to generate modernized applications from mainframe COBOL, and JCL code.

The example showcases the modernization of a simplified Customer Account Processing application, transforming COBOL code into equivalent Java microservices, complete with REST APIs, entity mappings, and automatically translated business rules. In this tutorial, we'll use Kiro as our IDE to demonstrate how to use AWS Transform output for reimagining the application.

## Overview

In this tutorial, you will:

- Prepare your outputs from AWS Transform
- Create steering and prompt files to guide modernized code generation
- Follow the three phase workflow through Requirements → Design → Implementation
- Generate the modernized code and tests
- (Optional): Boost Code and Test Quality with Kiro Hooks

## Prerequisites

Before beginning this tutorial, ensure you have:

- Mainframe application source code
- Kiro IDE installed locally or accessible via web interface
- Access to outputs from AWS Transform, including:
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
  - `inputs` - The inputs folder stores the original source artifacts of the mainframe application—COBOL code, JCL scripts, copybooks, and related configuration files.

Import all these files into the root of your Kiro project workspace.

## Step 2: Create Kiro steering files and a prompt

Kiro is an agentic IDE that helps you do your best work by bringing structure to AI coding with spec-driven development with features such as specs, steering, and hooks. Specs or specifications are structured artifacts that formalize the development process for complex features in your application. Steering gives Kiro persistent knowledge about your workspace through markdown files. Agent hooks are powerful automation tools that streamline your development workflow by automatically executing predefined agent actions when specific events occur in your IDE.

### Kiro steering files

Steering files give Kiro persistent knowledge of your forward engineering workspace through markdown files. Instead of explaining your conventions in every chat, these files ensure Kiro consistently follows your established patterns, libraries, and standards throughout your project.

Place the three steering files in the root of your workspace under `.kiro/steering/`.

#### Product Overview (product.md)

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

#### Technology Stack (tech.md)

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

#### Project Structure (structure.md)

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

### Prompt

Kiro specs are structured artifacts that formalize the development process for complex features in your application. They provide a systematic approach to transform high-level ideas into detailed implementation plans with clear tracking and accountability. From the Kiro pane, click the + button under Specs and describe your project idea using prompts.

Below is a sample prompt for Kiro spec generation:

```
Mainframe-to-AWS Modernization

Context
You are assisting in a comprehensive modernization of the Customer Account Management business function from the CardDemo mainframe application.

Project Structure
- source-code/ — COBOL copybook file definitions
- ApplicationLevelAnalysis/CustomerAccountManagement/ — Business function analysis with entrypoint documentation
- carddemo-v2-main/app/ — Extracted business rules per COBOL/JCL file

Target
Produce a compilable, deployable Java Spring Boot microservice that faithfully implements all mainframe business logic, following the steering guidelines exactly.

Initial Instructions
- Read and strictly follow the steering guidelines at .kiro/steering/mainframe-modernization.md before any code generation or analysis.
- Fully understand business requirements, data flows, and program paths from the provided analysis files.
- Preserve every business rule and data structure exactly as specified — no assumptions or inference allowed.
- Generate code that complies with AWS managed services and architecture principles defined in the steering file.
- Produce a clean project structure with all dependencies declared and ready to build and deploy.
- Follow the AWS Well-Architected Tool Framework best practices for security, reliability, and operational excellence.

Deliverables
- Java Spring Boot microservice source code (fully working and deployable)
- Infrastructure as Code using AWS CDK (v2) with multi-stack architecture
- Granular tasks mapped to business rules and program entrypoints
- Documentation for all generated components

Notes
- If any information is missing or ambiguous, stop and explicitly request clarification before proceeding.
- Do not start code generation until the above steps are fully confirmed.
```

## Step 3: Follow the workflow through Requirements → Design → Implementation

Using the steering files and prompts you provide, Kiro automatically creates three core documents that become the backbone of every specification:

- `requirements.md` - Captures user stories and acceptance criteria in structured EARS notation
- `design.md` - Documents technical architecture, sequence diagrams, and implementation considerations
- `tasks.md` - Provides a detailed implementation plan with discrete, trackable tasks

These specifications are living documents. You can edit any of them at any time—adding, removing, or refining details as your understanding of the project evolves. Kiro's design encourages continuous refinement, so the specs remain synchronized with shifting requirements and design decisions, giving you a reliable foundation for development.

## Step 4: Generate modernized code and tests

Once you have reviewed the three specs and are satisfied that they accurately reflect the desired solution, you have two options for execution:

- **Run tasks individually** – Execute each entry in tasks.md one‑by‑one, allowing you to monitor progress and intervene as needed.
- **Run all tasks at once** – Ask the Kiro agent to "Execute all tasks in the spec." Kiro will then generate the complete codebase, unit tests, and functional tests for your new AWS‑hosted application in a single pass.

### Next steps before deployment

The generated code and test suite provide a solid starting point, but they are not yet production‑ready. Before you ship the application, a developer should:

- Review the generated source code for correctness, security, and style compliance.
- Run the automatically generated unit and functional tests, fixing any failures.
- Perform additional manual testing (e.g., integration, performance, and user‑acceptance testing) to validate the system in real‑world scenarios.

Only after this human‑in‑the‑loop verification should the application be considered ready for deployment.

## Step 5 (Optional): Boost Code and Test Quality with Kiro Hooks

Agent hooks are lightweight automation utilities that let you trigger predefined Kiro actions directly from your IDE whenever a specific event occurs. By wiring these hooks into your workflow you can automatically improve the quality of the code and tests that Kiro generates.

### Why use a Hook for AWS Transform projects?

- **Complex business logic** – AWS Transform extracts and modernises main‑frame business rules.
- **Risk of omissions** – When Kiro produces new code it may miss subtle but critical rules.
- **Continuous feedback** – A hook can detect missing rules, invoke Kiro to regenerate the relevant sections, and automatically update the test suite.

Below is a sample of predefined hook prompt:

```
{
  "enabled": true,
  "name": "Business Rules Coverage Analyzer",
  "description": "Trigger for comprehensive business rules coverage analysis and implementation",
  "version": "1",
  "when": {
    "type": "userTriggered",
    "patterns": [
      "account-management-service/scripts/analyze-business-rules-coverage.py",
      "account-management-service/scripts/analyze-business-rules-coverage.json"
    ]
  },
  "then": {
    "type": "askAgent",
    "prompt": "COMPREHENSIVE BUSINESS RULES COVERAGE ANALYSIS\n\nYou are automatically analyzing and improving business rule coverage for account-management-service. Execute these steps in sequence:\n\n## STEP 1: Run Coverage Analysis\n• Execute: cd account-management-service & python3 scripts/analyze-business-rules-coverage.py\n• Capture the current coverage percentage from console output\n\n## STEP 2: Extract Specific Uncovered Rules\n• Execute: cd account-management-service &  python3 scripts/extract_uncovered_rules.py\n• Do the Deep Analysis of the output File: account-management-service/scripts/uncovered_rules_details.json\n• This section contains ONLY the rules that need implementation - focus exclusively on these\n• Do not implement rules that are already covered or not in this list\n• Prioritize from uncovered_rules_details by:\n  - Missing tagging (business logic exists but not tagged per steering guide)\n  - Missing implementation (business logic entirely missing)\n  - High-impact rules (validation, process rules)\n\n## STEP 3: \n- Check where to implement this missing rule. \n- Scan ALL files under the Backend directories: \n1. account-management-service/src/main/java/com/enterprise/carddemo/controller\n2. account-management-service/src/main/java/com/enterprise/carddemo/service\n3. account-management-service/src/main/java/com/enterprise/carddemo/repository\n - Scan ALL files under the Frontend directories:\n1. account-management-frontend/src\n\n### STEP 4:\n• After analyzing, Focus on 5-10 rules from uncovered_rules_details per automation cycle\n\n## STEP 5: Implement Improvements\n• DO NOT implement business rules without the ACTUAL Logic like using logger.debug without Actual Implemenation. \n• For missing tags: Add proper COBOL/JCL rule documentation to existing methods\n• For missing logic: Implement new methods following the steering guide patterns\n• Ensure all new code is:\n  - Properly integrated into service flows. Your newly Generated Code should be getting invoked from some methods.\n  - Follows existing patterns in Backend files like ValidationService, CobolAccountUpdateRulesService, etc. OR in frontened files.\n  - Includes proper error handling and logging\n  - Has appropriate COBOL/JCL rule documentation headers\n\n## STEP 6: CRITICAL - Verify No Dead Code (Integration Verification)\n• MANDATORY: Verify that ALL newly implemented business rule methods are actually invoked from somewhere in the application\n• For each new method created, trace the call path to ensure it's reachable:\n  - Backend: Check that new validation/service methods are called from Controllers, other Services, or Components\n  - Frontend: Check that new utility functions are called from React components, hooks, or other utilities\n• Examples of proper integration:\n  - New validation methods should be called in Controllers or Services during request processing\n  - New formatting methods should be called when preparing data for display\n  - New business rule methods should be integrated into existing workflows\n  - New UI utilities should be used in actual form fields or components\n• Fix dead code immediately: If any method is not invoked, either:\n  - Add proper integration points (recommended)\n  - Remove the dead code (if not needed)\n• Document the integration points in your summary\n\n## STEP 7: Validate Improvements\n• Re-run: cd account-management-service & python3 scripts/analyze-business-rules-coverage.py`\n• Confirm coverage percentage increased\n• Report the improvement: \"Coverage improved from X% to Y% (+Z rules)\" with specific rule IDs moved from uncovered to covered\n\n## STEP 8: Verify and FIX compilation issues\n• Compile the Backend Code and Frontend Code to verify if the build is successful. If there are compilation issues, Fix the errors, but DO NOT implement quick fix or workarounds.\n\n## SUCCESS CRITERIA:\n✅ Coverage analysis runs successfully\n✅ At least 5-10 new rules implemented or tagged\n✅ Coverage percentage increases\n✅ No compilation errors\n✅ All new code follows COBOL/JCL business rule patterns\n✅ NO DEAD CODE: All new methods have verified call paths\n✅ Integration points documented and tested\n\n## OUTPUT REQUIRED:\n• Summary of changes made\n• Before/after coverage statistics\n• List of newly covered rules\n• Integration verification: Document call paths for each new method\n• Confirmation that all code compiles and integrates properly\n• Verification that no dead code exists“
  }
}

```

## Summary – What You've Accomplished

- Exported the artifacts from AWS Transform and imported them into a Kiro workspace.
- Defined project‑wide conventions with steering files (product, technology, and structure) and a clear prompt to guide the IDE.
- Driven the three‑phase workflow (Requirements → Design → Implementation) to produce living specifications.
- Generated a Java‑Spring‑Boot microservice, infrastructure‑as‑code, and a full test suite, with an optional Hook‑based feedback loop to catch missing business rules.

## Next Steps

- Code Review & Quality Assurance
- Test Execution & Enhancement
- CI/CD Integration
- Production Deployment & Monitoring

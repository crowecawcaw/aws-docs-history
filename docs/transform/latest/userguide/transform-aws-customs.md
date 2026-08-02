# AWS-Managed Transformations

AWS-managed transformations are pre-built, AWS-vetted transformations for common use cases that are ready to use without any additional setup.

## Overview

AWS-managed transformations have the following characteristics:

- **Validated by AWS** - These transformations are vetted by AWS to be high quality
- **Ready to use** - No additional setup required
- **Continuously growing** - Additional transformations are continually being added
- **Customizable** - Pre-built transformations can be customized by providing additional guidance or requirements specific to your organization's needs
  using the `additionalPlanContext` configuration parameter
- **Early access support** - Some transformations may be marked as early access as they undergo further testing and refinement

## Available AWS-Managed Transformations

The following catalog lists the AWS-managed transformations that are currently available, grouped by use case. Each table shows the transformation name, the language or stack it applies to, and its status. To find a transformation quickly, use the search box at the top of this page to search by name, language, or use case.

This catalog is the canonical list of AWS-managed transformations. The Kiro Power, the agent plugin, the VS Code plugin, and the CLI all run the same transformations. To list the transformations available in your registry, run `atx custom def list`.

###### Note

Transformations marked **Early access** are functional but might be updated frequently based on customer feedback.

### Runtime upgrades

Upgrade a language or runtime to a newer version, or change the runtime distribution.

| Transformation                      | Language / stack        | Status              | Description                                                                                                                                                                                                                                                                                                                                                                              |
| ----------------------------------- | ----------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/java-version-upgrade`          | Java                    | Generally available | Upgrade Java applications using any build system from any source JDK version to any target JDK version, with dependency modernization including Jakarta EE migration, database drivers, ORM frameworks, and Spring ecosystem updates. Specify the target JDK version in chat or with the `additionalPlanContext` parameter.                                                              |
| `AWS/python-version-upgrade`        | Python                  | Generally available | Migrate Python projects from Python 3.8 or 3.9 to Python 3.11, 3.12, or 3.13 while maintaining functionality and performance. Specify the target Python version in chat or with the `additionalPlanContext` parameter.                                                                                                                                                                   |
| `AWS/nodejs-version-upgrade`        | Node.js                 | Generally available | Upgrade Node.js applications from any source Node.js version to any target Node.js version. Specify the target version in chat or with the `additionalPlanContext` parameter.                                                                                                                                                                                                            |
| `AWS/lambda-nodejs-runtime-upgrade` | Node.js (Lambda)        | Early access        | Upgrade AWS Lambda functions from older Node.js runtimes (nodejs4.3 through nodejs22.x) to nodejs24.x, addressing breaking changes in the Lambda Runtime Interface Client (RIC) and the Node.js 24 language runtime.                                                                                                                                                                     |
| `AWS/oracle-java-to-corretto`       | Java (JDK distribution) | Early access        | Migrate Java projects from Oracle JDK to Amazon Corretto. Replaces Oracle-specific internal APIs with standard Java equivalents, updates build configurations (Maven and Gradle) and container base images, removes commercial JVM flags, and generates a licensing report.                                                                                                              |
| `AWS/ruby-upgrade`                  | Ruby                    | Early access        | Upgrade Ruby applications from Ruby 2.x to Ruby 4.0, and their frameworks to Rails 8.0 or Sinatra 4.1. You can use this transformation with Rails and ActiveRecord apps, Sinatra apps, and standalone gems. The transformation pairs each Ruby version bump with the matching framework upgrade and runs the test suite. It then isolates failures before advancing to the next version. |

### SDK migrations

Migrate between major versions of an AWS SDK.

| Transformation                | Language / stack | Status              | Description                                                                                                                                                                                     |
| ----------------------------- | ---------------- | ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/java-aws-sdk-v1-to-v2`   | Java             | Generally available | Upgrade the AWS SDK from v1 to v2 for Java projects using Maven or Gradle.                                                                                                                      |
| `AWS/python-boto2-to-boto3`   | Python           | Generally available | Migrate Python applications from boto2 to boto3, based on the official AWS migration documentation.                                                                                             |
| `AWS/nodejs-aws-sdk-v2-to-v3` | Node.js          | Generally available | Upgrade Node.js applications from the AWS SDK for JavaScript v2 to v3 for modular architecture, first-class TypeScript support, and improved performance, without changing the Node.js version. |

### Framework upgrades and migrations

Upgrade a framework to a newer version, or migrate to a different framework.

| Transformation                                | Language / stack                       | Status              | Description                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------- | -------------------------------------- | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/spring-boot-version-upgrade`             | Java / Spring Boot                     | Generally available | Migrate Spring Boot 3.x projects to Spring Boot 4.x (targeting 4.1.0 GA). Covers version upgrades, starter renames, Jackson 3 migration, Spring Security 7 DSL, @MockBean removal, property renames, package relocations, observability consolidation, Spring AI 2.0, Spring Cloud 2025.1, Spring Batch, Kafka, AMQP, gRPC, Native/AOT, Jersey, JSpecify, embedded server changes, third-party compatibility, and verification. |
| `AWS/JBoss-to-Spring-Boot`                    | Java (JBoss or WildFly to Spring Boot) | Early access        | Migrate Java EE or Jakarta EE enterprise applications running on JBoss EAP or WildFly to Spring Boot, eliminating application server dependencies for a cloud-native, containerized deployment model.                                                                                                                                                                                                                           |
| `AWS/early-access-angular-to-react-migration` | Angular to React                       | Early access        | Transform an Angular application to React.                                                                                                                                                                                                                                                                                                                                                                                      |
| `AWS/angular-version-upgrade`                 | Angular                                | Early access        | Upgrade an older Angular application to a target Angular version, including components, services, templates, and routing.                                                                                                                                                                                                                                                                                                       |
| `AWS/vue.js-version-upgrade`                  | Vue.js                                 | Early access        | Perform a major version upgrade from Vue.js 2 to Vue.js 3, modernizing components, state management, routing, and global APIs. Minor and patch updates are outside the scope.                                                                                                                                                                                                                                                   |

### GenAI and model migrations

Migrate generative AI workloads to .

| Transformation                              | Language / stack        | Status       | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------------- | ----------------------- | ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/GenAI-to-Bedrock-Migration-Assessment` | Generative AI workloads | Early access | Assess generative AI workloads for migration from third-party providers (OpenAI, Google Gemini, Anthropic direct, and open-source models) to . Discovers SDK usage and models, clarifies requirements, designs a model mapping, estimates cost and risk, and generates assessment artifacts. Assessment-only; does not modify source code. Also covers agentic frameworks such as CrewAI, LangGraph, and Strands. |

### Language-to-language migrations

Translate a codebase from one programming language to another.

| Transformation                | Language / stack | Status       | Description                                                                                                                                                                                                                                                                            |
| ----------------------------- | ---------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/vba-to-python-migration` | VBA to Python    | Early access | Migrate Excel VBA macros, modules, UserForms, and embedded logic to equivalent Python scripts and modules, using openpyxl, pandas, tkinter or PyQt6, and standard libraries. Target language is Python 3.8 or later. Use when converting .bas, .cls, .frm, or .xlsm-embedded VBA code. |

### Database migrations

No database-specific AWS-managed transformations are currently available. To modernize Microsoft SQL Server databases and their associated .NET applications to Amazon Aurora PostgreSQL, see [SQL Server modernization](sql-server-modernization.md "sql-server-modernization.md").

### Observability

Modernize logging and monitoring to AWS-native services.

| Transformation                              | Language / stack                    | Status       | Description                                                                                                                                                                                                                                  |
| ------------------------------------------- | ----------------------------------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/early-access-log4j-to-slf4j-migration` | Java (logging)                      | Early access | Migrate Java applications from Log4j (1.x or 2.x) to SLF4J with a Logback backend. Handles source code, dependency management (Maven and Gradle), and logging configuration files, and validates by compile, test, and residual import scan. |
| `AWS/datadog-monitors-to-cloudwatch-alarms` | Infrastructure as code / monitoring | Early access | Migrate DataDog metric monitors that track AWS service metrics and custom metrics to native CloudWatch alarms as infrastructure as code. Generates CloudFormation YAML, CDK TypeScript, and Terraform HCL.                                   |

### Architecture

Re-architect, re-platform, or optimize applications for AWS.

| Transformation                                  | Language / stack                       | Status              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ----------------------------------------------- | -------------------------------------- | ------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/java-performance-optimization`             | Java (performance)                     | Generally available | Optimize Java application performance by analyzing JFR profiling data to detect CPU and memory hotspots and anti-patterns, then applying targeted code fixes. For instructions on collecting JFR data, see [the JFR runtime guide](https://docs.oracle.com/javacomponents/jmc-5-4/jfr-runtime-guide/run.htm "https://docs.oracle.com/javacomponents/jmc-5-4/jfr-runtime-guide/run.htm").                                                                                     |
| `AWS/early-access-java-x86-to-graviton`         | Java (Arm64 / Graviton)                | Early access        | Validate Java application compatibility with the Arm64 architecture for AWS Graviton processors, and resolve incompatibilities by updating dependencies, detecting architecture-specific code patterns, and recompiling native libraries when source code is available. Many modern Java applications are already Arm64-compatible.                                                                                                                                          |
| `AWS/oracle-service-bus-to-aws`                 | Java / integration to serverless       | Early access        | Migrate Oracle Service Bus (OSB) and BPEL process configurations to an AWS-native serverless architecture, generating a deployable CDK TypeScript project with Amazon API Gateway, AWS Lambda, and AWS Step Functions.                                                                                                                                                                                                                                                       |
| `AWS/mulesoft-to-aws-native`                    | Java / MuleSoft to serverless          | Early access        | Transform MuleSoft Mule 3.x and 4.x applications into AWS serverless architectures (Amazon API Gateway, AWS Lambda, and AWS Step Functions) targeting Java 17 on AWS Lambda with SnapStart. The transformation maps flow triggers to AWS event sources, converts DataWeave and MEL (MuleSoft Expression Language) expressions to AWS equivalents, and replaces connectors with AWS SDK for Java v2 calls. It produces SAM templates, AWS Lambda handlers, and JUnit 5 tests. |
| `AWS/payshield-hsm-to-aws-payment-cryptography` | Java (HSM to AWS Payment Cryptography) | Generally available | Migrate Java applications from the Thales PayShield hardware security module (HSM) protocol to the AWS Payment Cryptography SDK v2. Migration includes command mapping, key migration, dependency setup, and parity testing.                                                                                                                                                                                                                                                 |

### Codebase analysis

Analyze codebases and portfolios to plan modernization. These transformations produce reports and do not modify your code.

| Transformation                                   | Language / stack   | Status              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------------------------------ | ------------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `AWS/comprehensive-codebase-analysis`            | Multiple languages | Generally available | Perform deep static analysis of a codebase to generate hierarchical, cross-referenced documentation that combines behavioral analysis, architectural documentation, and business intelligence, with emphasis on technical debt insights.                                                                                                                                                                                                                                                                |
| `AWS/agentic-readiness-analysis`                 | Multiple languages | Early access        | Evaluate whether systems are ready to be safely called by AI agents, covering APIs, identity, state management, human-in-the-loop, and observability.                                                                                                                                                                                                                                                                                                                                                   |
| `AWS/modernization-readiness-analysis`           | Multiple languages | Early access        | Scan portfolios for cloud-native maturity gaps and map findings to AWS modernization pathways.                                                                                                                                                                                                                                                                                                                                                                                                          |
| `AWS/portfolio-agentic-readiness-analysis`       | Portfolio          | Early access        | Aggregate individual agentic readiness analysis reports across a portfolio of applications to identify cross-cutting blockers, shared remediation patterns, and prioritized recommendations.                                                                                                                                                                                                                                                                                                            |
| `AWS/portfolio-modernization-readiness-analysis` | Portfolio          | Early access        | Aggregate individual modernization analysis reports across a portfolio into a consolidated roadmap with prioritized migration waves and recommended modernization pathways.                                                                                                                                                                                                                                                                                                                             |
| `AWS/business-rules-extraction`                  | Multiple languages | Early access        | This transformation statically analyzes a monolithic codebase to produce rewrite-ready documentation without requiring a build, a run, or source code modifications. It decomposes the system into bounded domains and extracts per-domain business rules, workflows, cross-cutting concerns, and database structure. The output includes a machine-readable manifest, an interactive dashboard, and language-neutral implementation specifications per domain to guide modernization or full rewrites. |

## Customizing AWS-Managed Transformations

You can customize AWS-managed transformations to meet your organization's specific needs by providing additional context
through the `additionalPlanContext` configuration parameter.

**Example: Customizing Java version upgrade**

```
codeRepositoryPath: ./my-project
transformationName: AWS/java-version-upgrade
buildCommand: mvn clean install
additionalPlanContext: |
  The target Java version to upgrade to is Java 17.
  Update all internal library dependencies to versions compatible with Java 17.
  Ensure compatibility with our custom authentication framework.
```

**Example: Customizing AWS SDK migration**

```
codeRepositoryPath: ./my-project
transformationName: AWS/java-aws-sdk-v1-to-v2
buildCommand: gradle build
additionalPlanContext: |
  Maintain our existing error handling patterns.
  Use our organization's standard credential provider chain.
  Update logging to use our internal logging framework.
```

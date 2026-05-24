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

The following AWS-managed transformations are currently available:

**Language Version Upgrades:**

- `AWS/java-version-upgrade` - Upgrade Java applications using any build system from any source JDK version to any target JDK version with comprehensive dependency modernization including Jakarta EE migration, database drivers,
  ORM frameworks, and Spring ecosystem updates. You can specify your desired target JDK version either through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.
- `AWS/python-version-upgrade` - Migrate Python projects from Python 3.8/3.9 to Python 3.11/3.12/3.13, ensuring compatibility with the latest Python features, security updates, and runtime while maintaining functionality and performance.
  You can specify your desired target Python version either through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.
- `AWS/nodejs-version-upgrade` - Upgrade NodeJS applications from any source NodeJS version to any target NodeJS version. You can specify your desired target NodeJS version either
  through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.

**AWS SDK Migrations:**

- `AWS/java-aws-sdk-v1-to-v2` - Upgrade the AWS SDK from V1 to V2 for Java projects using Maven or Gradle.
- `AWS/python-boto2-to-boto3` - Migrate Python applications from boto2 to boto3, based on the official AWS migration documentation.
- `AWS/nodejs-aws-sdk-v2-to-v3` - Upgrade Node.js applications from AWS SDK for JavaScript v2 to v3 to leverage modular architecture, first-class TypeScript support, middleware stack, and improved performance while ensuring all AWS
  service interactions continue to function correctly, without modifying the underlying Node.js version.

**Analysis:**

- `AWS/comprehensive-codebase-analysis` - This transformation performs deep static analysis of codebases to
  generate hierarchical, cross-referenced documentation covering all aspects of the system. It combines behavioral analysis, architectural
  documentation, and business intelligence extraction to create a comprehensive knowledge base organized for maximum usability and navigation.
  The transformation places special emphasis on technical debt analysis, providing prominent, actionable insights on outdated components and
  maintenance concerns at the root level.
- `AWS/java-performance-optimization` - Optimize Java application performance by analyzing JFR profiling data to detect CPU/memory hotspots and anti-patterns, then applying targeted code fixes to reduce resource usage and improve efficiency. For instructions on collecting JFR data, see [https://docs.oracle.com/javacomponents/jmc-5-4/jfr-runtime-guide/run.htm](https://docs.oracle.com/javacomponents/jmc-5-4/jfr-runtime-guide/run.htm "https://docs.oracle.com/javacomponents/jmc-5-4/jfr-runtime-guide/run.htm").

**Early Access Transformations**

###### Note

Early access transformations are functional but might be frequently updated based on customer
feedback.

- `AWS/early-access-java-x86-to-graviton` - [Early Access] Validates Java application compatibility with Arm64 architecture for running on
  AWS Graviton Processors. Identifies and resolves Arm64 incompatibilities by updating dependencies, detecting architecture-specific code patterns,
  and recompiling native libraries when source code is available. Makes targeted code modifications necessary for Arm64 support, such as architecture detection, and native library loading,
  but does not perform general code refactoring. Maintains current Java version and JDK distribution and validates compatibility through build and test execution.
  For optimal results, run in an Arm64-based environment.

###### Note

Many modern Java applications are already Arm64-compatible.

- `AWS/early-access-angular-to-react-migration` - [Early Access] Transform an Angular application to React.
- `AWS/vue.js-version-upgrade` - [Early Access] An early-access transformation for major version upgrades from Vue.js 2 to Vue.js 3 to modernize components, state management, routing, and global APIs to Vue.js 3 patterns. Minor or patch updates are outside the scope.
- `AWS/angular-version-upgrade` - [Early Access] This is an early-access transformation to transform an older Angular application to a target Angular version by upgrading components, services, templates, and routing to modern Angular patterns.
- `AWS/early-access-log4j-to-slf4j-migration` - [Early Access] This transformation migrates Java applications from Log4j (1.x/2.x) to SLF4J with Logback backend. Handles source code, dependency management (Maven/Gradle), and logging configuration files. Validates via compile, test, and residual import scan.
- `AWS/agentic-readiness-analysis` - [Early Access] This is an early-access transformation that evaluates whether systems are ready to be safely called by AI agents - covering APIs, identity, state management, human-in-the-loop, and observability.
- `AWS/modernization-readiness-analysis` - [Early Access] This is an early-access transformation that scans portfolios for cloud-native maturity gaps and maps findings to AWS modernization pathways.
- `AWS/portfolio-agentic-readiness-analysis` - [Early Access] This is an early-access transformation that aggregates individual Agentic Readiness Analysis reports across a portfolio of applications, identifying cross-cutting blockers, shared remediation patterns, and organizational readiness gaps. Produces prioritized recommendations mapped to AWS programs, workshops, and enablement resources tailored to each portfolio's agentic adoption journey.
- `AWS/portfolio-modernization-readiness-analysis` - [Early Access] This is an early-access transformation that aggregates individual Modernization Analysis reports across a portfolio of applications, producing a consolidated modernization roadmap with prioritized migration waves, recommended modernization pathways, and AWS program recommendations including workshops and enablement resources tailored to each portfolio's modernization needs.
- `AWS/oracle-java-to-corretto` - [Early Access] This is an early-access transformation that migrates Java projects from Oracle JDK to Amazon Corretto. Replaces Oracle-specific internal APIs (sun.\*, com.sun.\*, com.oracle.\*) with standard Java equivalents, updates build configurations (Maven/Gradle), replaces container base images (Oracle, eclipse-temurin, openjdk, adoptopenjdk) with amazoncorretto, updates CI workflow distribution fields, removes commercial JVM flags, fixes annotation-processor JDK incompatibilities (Lombok), handles Alpine-to-Amazon-Linux package translation, and generates a LICENSING_REPORT.md with cost savings.
- `AWS/oracle-service-bus-to-aws` - [Early Access] This is an early-access transformation that migrates Oracle Service Bus (OSB) and BPEL process configurations to AWS-native serverless architecture by generating a deployable CDK TypeScript project with API Gateway, Lambda, and Step Functions from OSB proxy/pipeline/business service XML definitions.
- `AWS/JBoss-to-Spring-Boot` - [Early Access] This is an early-access transformation that migrates Java EE/Jakarta EE enterprise applications running on JBoss EAP or WildFly application servers to Spring Boot, eliminating application server dependencies, modernizing to a cloud-native containerized deployment model, and improving developer productivity, deployment velocity, and resource efficiency.
- `AWS/datadog-monitors-to-cloudwatch-alarms` - [Early Access] This is an early-access transformation that migrates DataDog Metric Monitors (metric alert, query alert) tracking AWS service metrics (aws.\* prefix) and custom metrics (Metric Streams or IAM Role polling integration) to native CloudWatch Alarms as infrastructure-as-code. Classifies monitors into Standard, Metrics Insights (MI), or Metric Math alarms. Generates CloudFormation YAML, CDK TypeScript, and/or Terraform HCL. Supports JSON exports, Terraform config (.tf), state (.tfstate), and plan (.tfplan) inputs. Handles ANOMALY_DETECTION_BAND, arithmetic expressions, MI SQL fleet monitoring, and .as_count() simplification. Detects DataDog integration type (Metric Streams vs IAM Role polling) and resolves custom metric names via CloudWatch list-metrics inventory.
- `AWS/spring-boot-version-upgrade` - [Early Access] This is an early-access transformation to transform an older Spring Boot application to a target Spring Boot version by upgrading build files and starters, properties, Jackson 3 packages, Spring Security 7 DSL, testing infrastructure, and observability dependencies to modern Spring Boot patterns.

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

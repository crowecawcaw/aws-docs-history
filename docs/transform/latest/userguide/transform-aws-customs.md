# AWS-Managed Transformations

AWS-managed transformations are pre-built, AWS-vetted transformations for common use cases that are ready to use without any additional setup.

## Overview

AWS-managed transformations have the following characteristics:

- **Validated by AWS** - These transformations are vetted by AWS to be high quality
- **Ready to use** - No additional setup required
- **Continuously growing** - Additional transformations are continually being added
- **Customizable** - Pre-built transformations can be customized by providing additional guidance or requirements specific to your organization's needs using the `additionalPlanContext` configuration parameter
- **Early access support** - Some transformations may be marked as early access as they undergo further testing and refinement

## Available AWS-Managed Transformations

The following AWS-managed transformations are currently available:

**Language Version Upgrades:**

- `AWS/java-version-upgrade` - Upgrade Java applications using any build system from any source JDK version to any target JDK version with comprehensive dependency modernization including Jakarta EE migration, database drivers, ORM frameworks, and Spring ecosystem updates. You can specify your desired target JDK version either through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.
- `AWS/python-version-upgrade` - Migrate Python projects from Python 3.8/3.9 to Python 3.11/3.12/3.13, ensuring compatibility with the latest Python features, security updates, and runtime while maintaining functionality and performance. You can specify your desired target Python version either through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.
- `AWS/nodejs-version-upgrade` - Upgrade NodeJS applications from any source NodeJS version to any target NodeJS version. You can specify your desired target NodeJS version either through interactive chat with the agent, or by passing an additionalPlanContext configuration parameter.

**AWS SDK Migrations:**

- `AWS/java-aws-sdk-v1-to-v2` - Upgrade the AWS SDK from V1 to V2 for Java projects using Maven or Gradle.
- `AWS/python-boto2-to-boto3` - Migrate Python applications from boto2 to boto3, based on the official AWS migration documentation.
- `AWS/nodejs-aws-sdk-v2-to-v3` - Upgrade Node.js applications from AWS SDK for JavaScript v2 to v3 to leverage modular architecture, first-class TypeScript support, middleware stack, and improved performance while ensuring all AWS service interactions continue to function correctly, without modifying the underlying Node.js version.

**Early Access Transformations**

###### Note

Early access transformations are functional but might be frequently updated based on customer
feedback.

- `AWS/early-access-comprehensive-codebase-analysis` - [Early Access] This transformation performs deep static analysis of codebases to generate hierarchical,
  cross-referenced documentation covering all aspects of the system. It combines behavioral analysis, architectural documentation, and business intelligence extraction
  to create a comprehensive knowledge base organized for maximum usability and navigation. The transformation places special emphasis on technical debt analysis, providing prominent, actionable
  insights on outdated components, security vulnerabilities, and maintenance concerns at the root level.
- `AWS/early-access-java-x86-to-graviton` - [Early Access] Validates Java application compatibility with Arm64 architecture for running on
  AWS Graviton Processors. Identifies and resolves Arm64 incompatibilities by updating dependencies, detecting architecture-specific code patterns,
  and recompiling native libraries when source code is available. Makes targeted code modifications necessary for Arm64 support, such as architecture detection, and native library loading,
  but does not perform general code refactoring. Maintains current Java version and JDK distribution and validates compatibility through build and test execution.
  For optimal results, run in an Arm64-based environment.

###### Note

Many modern Java applications are already Arm64-compatible.

## Customizing AWS-Managed Transformations

You can customize AWS-managed transformations to meet your organization's specific needs by providing additional context through the `additionalPlanContext` configuration parameter.

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

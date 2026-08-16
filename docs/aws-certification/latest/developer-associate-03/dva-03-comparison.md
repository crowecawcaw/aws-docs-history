# Comparison of DVA-C02 and DVA-C03

## Side-by-side comparison

The following table shows the domains and the percentage of scored questions in each domain for the DVA-C02 exam (in use until November 30, 2026) and the DVA-C03 exam (in use beginning December 1, 2026).

| DVA-C02 domain                                   | DVA-C03 domain                                   |
| ------------------------------------------------ | ------------------------------------------------ |
| Domain 1: Development with AWS Services (32%)    | Domain 1: Development with AWS Services (30%)    |
| Domain 2: Security (26%)                         | Domain 2: Security (26%)                         |
| Domain 3: Deployment (24%)                       | Domain 3: Testing and Deployment (22%)           |
| Domain 4: Troubleshooting and Optimization (18%) | Domain 4: Troubleshooting and Optimization (22%) |

## Additions of content for DVA-C03

A new task was introduced in DVA-C03 that addresses five dedicated skills that cover the security aspects of AI service usage.

**Task 2.3: Identify and mitigate security risks associated with using and integrating AI services into application development.**

- Request and manage access to AI services.
- Use data privacy controls to transmit data to AI services (for example, by using VPC endpoints to establish private connectivity, ensuring inputs and outputs are not used to train AI models).
- Filter and control AI model inputs and outputs (for example, by applying content filtering, sensitive information detection, PII/PHI redaction, denied topic policies, prompt injection and manipulation protection).
- Secure AI agent interactions (for example, by using tool-use authorization, session isolation, human-in-the-loop approval flows for sensitive actions).
- Protect sensitive content in monitoring logs during interactions with AI services.

In Task 1.1, the following content was added:

- Use AI-assisted development tools to generate, review, and optimize code (for example, spec-driven code generation, automated code reviews, intelligent code completion, refactoring suggestions, security scanning).
- Integrate managed AWS AI services into applications.

In Task 2.1, the following content was added:

- Use presigned URLs to provide secure, time-limited access (for example, by using Amazon S3 and Amazon CloudFront)

In Task 3.1, the following content was added:

- Build and manage container images for deployment (for example, by using Amazon ECR, Docker files, container image tagging, lifecycle policies).

In Task 3.2, the following content was added:

- Use AWS AI tools to generate tests and automate repetitive testing workflows (for example, automated test execution, test result analysis, regression testing automation, ensuring test coverage)

In Task 3.3, the following content was added:

- Deploy containerized applications by using AWS container orchestration services (for example, Amazon ECS task definitions, Amazon EKS manifests, AWS Fargate launch types, rolling updates).
- Use AWS AI tools to support CI/CD workflows (for example, automated deployment approvals, environment provisioning, post-deployment validation).

In Task 4.1, the following content was added:

- Use AWS AI tools to analyze errors and to generate troubleshooting suggestions.

In Task 4.3, the following content was added:

- Use AWS AI tools to identify optimization opportunities (for example, performance bottleneck detection, resource usage optimization, code efficiency improvement)

## Recategorizations of content for DVA-C03

The following skills and content areas were relocated between domains or tasks. Content retains its scope but is tested in a different location within the exam framework:

| What Moved                                       | From (DVA-C02)     | To (DVA-C03)       |
| ------------------------------------------------ | ------------------ | ------------------ |
| Unit testing by using AWS SAM                    | Domain 1, Task 1.1 | Domain 3, Task 3.2 |
| AWS Lambda function performance tuning           | Domain 1, Task 1.2 | Domain 4, Task 4.3 |
| Serialize and deserialize data                   | Domain 1, Task 1.3 | Domain 1, Task 1.1 |
| Amazon API Gateway stages and custom domains     | Domain 3, Task 3.4 | Domain 3, Task 3.1 |
| IaC templates (CDK, AWS SAM, AWS CloudFormation) | Domain 3, Task 3.3 | Domain 3, Task 3.3 |

## Structural changes for DVA-C03

DVA-C03 consolidated multiple granular skills into single comprehensive action-oriented skills. These consolidations do not result in a decreased emphasis on essential skills. Rather, the exam has been reorganized to reduce repetition and ensure consistency in level of detail across all domains. The following table shows the before/after for each major consolidation area:

| Area                                   | DVA-C02 (Before)                                                                                                          | DVA-C03 (After)                                                             |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Amazon DynamoDB                        | 4 separate skills: Partition keys and design, Consistency models, Query operations and scan operations, Keys and indexing | 1 comprehensive DynamoDB skill that covers all aspects                      |
| Security (Encryption + Sensitive Data) | Task 2.2 + Task 2.3 = 13 skills total. Task 2.2: Encryption (6 skills), Task 2.3: Sensitive data (7 skills)               | Single Task 2.2 = 7 skills (all encryption and data protection in one task) |
| Testing (Test + Automate)              | Task 3.2 + Task 3.3 = 11 skills total. Task 3.2: Test Applications (6 skills), Task 3.3: Automate Testing (5 skills)      | Single Task 3.2 = 5 skills (combined with AI testing tool added)            |
| Observability                          | 8 observability skills across Domain 4                                                                                    | 5 observability skills (3 merged)                                           |
| Optimization                           | 9 optimization skills across Domain 4                                                                                     | 6 optimization skills (3 merged)                                            |

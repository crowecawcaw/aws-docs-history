# How AWS Security Agent works

AWS Security Agent operates across three interfaces to provide proactive application security throughout the development lifecycle. Security configurations are managed in the AWS Management Console, security reviews are conducted in the Security Agent Web Application, and automated code and security finding remediation occur directly in code repository platforms like GitHub.

## Overview

AWS Security Agent consists of three main components:

- **AWS Management Console** - Configure Agent Spaces, define security requirements, configure penetration testing, connect code repositories, and manage user access
- **Security Agent Web Application** - Conduct design reviews, create and run threat models, execute penetration tests, create and run code reviews, and review security findings within your assigned Agent Spaces
- **Code Repository Integration** - Receive automated code reviews on pull requests and penetration test remediation pull requests. Currently AWS Security Agent supports connecting to GitHub.

### Console configuration

Administrators configure AWS Security Agent through the AWS Management Console.

**Agent Spaces** - When you create your first Agent Space in the AWS Management Console, AWS Security Agent creates the Web Application for your account. Each Agent Space you create represents a distinct application or project you want to secure. In the Web Application, users select which Agent Space to work in when conducting security assessments.

**Security requirements** - Define the security requirements that AWS Security Agent evaluates during design and code reviews, organized into security requirement packs. Enable AWS-managed packs based on industry standards, create custom packs for your organization’s policies, or generate requirements by uploading your security documentation. Requirements apply across all Agent Spaces.

**Penetration testing configuration** - Configure penetration testing capabilities for each Agent Space by:

- Verifying target domains for testing through DNS or HTTP verification
- Configuring VPC access for testing private applications
- Setting up CloudWatch logging for penetration test runs
- Configuring AWS Secrets Manager or Lambda functions for test credentials
- Specifying S3 buckets for additional application context

**Code review configuration** - Configure code review capabilities for each Agent Space by:

- Connecting GitHub repositories or S3 buckets containing source code
- Selecting code review settings (security vulnerabilities, custom requirements, or both)
- Enabling pull request comments for automated review of code changes in GitHub
- Setting up CloudWatch logging for code review runs

**Threat modeling configuration** - Configure threat modeling capabilities for each Agent Space by:

- Connecting source code repositories or S3 buckets containing source code
- Adding scope docs (feature design documents) to focus the analysis on a specific feature
- Configuring CloudWatch logging for threat model runs
- Setting up a service role for AWS resource access

**Integrations** - Connect GitHub repositories to each Agent Space to enable key capabilities:

- Provide application context for more accurate penetration testing
- Enable code review for full repository scans and pull request analysis
- Enable automated code remediation through pull requests for code review and penetration test findings

**User access** - Manage how users access the Security Agent Web Application. If you’ve enabled IAM Identity Center (SSO), assign users in the AWS Security Agent console to provide direct SSO access to the Web Application. If you’re using IAM-only access, users with AWS Console access can launch the Web Application through the admin access link in the Console for any Agent Space.

### Web Application activities

Users access the Security Agent Web Application to conduct security assessments within their assigned Agent Spaces.

**Select Agent Space** - When logging into the Web Application, users select which Agent Space to work in. Users can only see and access Agent Spaces they’ve been assigned to.

**Design reviews** - Upload design documents and architecture specifications for analysis against organizational security requirements. Review findings with remediation guidance.

**Threat models** - Create and run threat models by providing source code, technical design documents (scope docs), or both. Scope docs define what the agent focuses its analysis on; source code provides context about your existing system. Each run produces a system overview describing your application’s architecture, trust boundaries, data flows, and security posture, along with a set of threats classified by STRIDE category with severity levels and actionable recommendations.

**Code reviews** - Create and run code reviews that perform comprehensive static analysis across your full source code. Select GitHub repositories or S3 sources, configure scan settings, and review detailed security findings with remediation guidance. AWS Security Agent identifies security vulnerabilities and validates compliance with your organization’s custom security requirements across your entire codebase.

**Penetration tests** - Configure and execute penetration tests by providing target URLs, authentication details, and documentation. AWS Security Agent performs autonomous testing to discover exploitable vulnerabilities through multi-step attack scenarios.

**Review findings** - Examine detailed security findings from design reviews, threat models, code reviews, and penetration tests, including impact analysis, reproducible attack paths, and remediation guidance.

**Validate fixes** - Re-run security assessments after implementing remediations to verify vulnerabilities have been addressed.

### GitHub integration

AWS Security Agent integrates directly with GitHub to provide automated security feedback in developers' workflows.

**Pull request comments** - After administrators install the AWS Security Agent GitHub App and enable code review with Code review comments for an Agent Space, AWS Security Agent automatically analyzes pull requests in connected repositories. Developers receive security findings and remediation guidance directly in pull request comments, validating code changes against organizational security requirements and common vulnerabilities.

**Automatic remediation** - When users enable automatic code remediation for a code review, AWS Security Agent generates fixes for identified vulnerabilities and submits pull requests to the associated GitHub repositories.

**Penetration test remediation** - When administrators enable finding remediation in the Console, users can request automatic remediation for penetration test findings from the Web Application. AWS Security Agent opens a pull request to the associated GitHub repository with code fixes to address the vulnerability.

# How AWS Security Agent works

AWS Security Agent operates across three interfaces to provide proactive application security throughout the development lifecycle. Security configurations are managed in the AWS Management Console, security reviews are conducted in the Security Agent Web Application, and automated code and security finding remediation occur directly in code repository platforms like GitHub.

## Overview

AWS Security Agent consists of three main components:

- **AWS Management Console** - Configure Agent Spaces, define security requirements, configure penetration testing, connect code repositories, and manage user access
- **Security Agent Web Application** - Conduct design reviews, execute penetration tests, and review security findings within your assigned Agent Spaces
- **Code Repository Integration** - Receive automated code reviews on pull requests and penetration test remediation pull requests. Currently AWS Security Agent supports connecting to GitHub.

### Console configuration

Administrators configure AWS Security Agent through the AWS Management Console.

**Agent Spaces** - When you create your first Agent Space in the AWS Management Console, AWS Security Agent creates the Web Application for your account. Each Agent Space you create represents a distinct application or project you want to secure. In the Web Application, users select which Agent Space to work in when conducting security assessments.

**Security requirements** - Define organizational security requirements centrally in the Console, such as approved authorization libraries, logging standards, and data access policies. These requirements apply across all Agent Spaces, and AWS Security Agent automatically validates them during design and code reviews.

**Penetration testing configuration** - Configure penetration testing capabilities for each Agent Space by:

- Verifying target domains for testing through DNS or HTTP verification
- Configuring VPC access for testing private applications
- Setting up CloudWatch logging for penetration test runs
- Configuring AWS Secrets Manager or Lambda functions for test credentials
- Specifying S3 buckets for additional application context

**Integrations** - Connect GitHub repositories to each Agent Space to enable three key capabilities:

- Provide application context for more accurate penetration testing
- Enable automated code review on pull requests
- Enable penetration test finding remediation through automated pull requests

**User access** - Manage how users access the Security Agent Web Application. If you’ve enabled IAM Identity Center (SSO), assign users either in IAM Identity Center or the AWS Security Agent console to provide direct SSO access to the Web Application. If you’re using IAM-only access, users with AWS Console access can launch the Web Application through the admin access link in the Console for any Agent Space.

### Web Application activities

Users access the Security Agent Web Application to conduct security assessments within their assigned Agent Spaces.

**Select Agent Space** - When logging into the Web Application, users select which Agent Space to work in. Users can only see and access Agent Spaces they’ve been assigned to.

**Design reviews** - Upload design documents and architecture specifications for analysis against organizational security requirements. Review findings with remediation guidance.

**Penetration tests** - Configure and execute penetration tests by providing target URLs, authentication details, and documentation. AWS Security Agent performs autonomous testing to discover exploitable vulnerabilities through multi-step attack scenarios.

**Review findings** - Examine detailed security findings from design reviews and penetration tests, including impact analysis, reproducible attack paths, and remediation guidance.

**Validate fixes** - Re-run security assessments after implementing remediations to verify vulnerabilities have been addressed.

### GitHub integration

AWS Security Agent integrates directly with GitHub to provide automated security feedback in developers' workflows.

**Automated code review** - After administrators install the AWS Security Agent GitHub App and enable code review for an Agent Space in the Console, AWS Security Agent automatically analyzes pull requests in connected repositories. Developers receive security findings and remediation guidance directly in pull request comments, validating code changes against organizational security requirements and common vulnerabilities.

**Penetration test remediation** - When administrators enable finding remediation in the Console, users can request automatic remediation for penetration test findings from the Web Application. AWS Security Agent opens a pull request to the associated GitHub repository with code fixes to address the vulnerability.

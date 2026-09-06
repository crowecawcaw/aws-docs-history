

# Understand the resource hierarchy and lifecycle
<a name="understand-lifecycle"></a>

AWS Security Agent organizes security testing resources in a hierarchical structure that determines what’s shared across your organization and what’s scoped per application. Understanding this structure helps you configure AWS Security Agent effectively and know where to find and manage different resources.

## What’s shared across your organization
<a name="_whats_shared_across_your_organization"></a>

Some resources in AWS Security Agent are configured once at the organizational level and apply across all your applications and Agent Spaces. These tenant-level resources provide consistency and reduce duplicate configuration work.


| Resource | What it is | Why it’s shared | 
| --- | --- | --- | 
|  **Security requirements**  | Organizational security standards that define what AWS Security Agent validates during design and code reviews | Your security policies apply to all applications. Define them once and AWS Security Agent enforces them everywhere. | 
|  **GitHub integrations**  | Registered GitHub organizations or user accounts authorized to connect with AWS Security Agent | Register your GitHub organization once, then connect specific repositories to any Agent Space as needed. | 
|  **IAM Identity Center configurations**  | SSO settings that control how users access AWS Security Agent | Centralized identity management applies across all Agent Spaces in your organization. | 

**Important**  
Changes to security requirements affect all future design reviews and code reviews across all Agent Spaces. Existing reviews are not affected.

## What’s scoped per Agent Space
<a name="_whats_scoped_per_agent_space"></a>

Each Agent Space represents a distinct application or project you want to secure. Resources at the Agent Space level are scoped to that specific application, allowing different teams to work independently with their own configurations and assessments.


| Resource | What it is | Why it’s scoped per application | 
| --- | --- | --- | 
|  **Penetration test configurations**  | Test configurations for specific features, API endpoints, or functionality within your application | Each application has unique targets, authentication methods, and scope boundaries specific to that application. | 
|  **Design reviews**  | Individual architectural security assessments of design documents | Each application has its own architecture and design documents that are assessed independently. | 
|  **Threat models**  | Threat modeling assessments that build a system overview and identify threats from source code, design documents, or both | Each application has its own code and design, and is threat modeled independently. Threat models are reusable configurations that you can re-run as your code and design evolve. | 
|  **Integrations**  | Source and documentation providers (GitHub, GitLab, Bitbucket, GitHub Enterprise Server, and Confluence) connected to this Agent Space | Different applications rely on different sources and documentation. Connecting them at the Agent Space level keeps application boundaries clear. | 
|  **Code review settings**  | Configuration of code review capabilities including connected sources, scan settings, and PR comment enablement | Each application has its own repositories and security review needs configured independently. | 
|  **Penetration test remediation settings**  | Configuration of which connected repositories can receive automated fix pull requests for penetration testing findings | Teams control where AWS Security Agent can submit code changes based on their application’s workflow. | 
|  **User assignments**  | Users who have access to this specific Agent Space | Teams only see security assessments for applications they’re responsible for, keeping work organized and focused. | 

**Tip**  
We recommend creating one Agent Space per application or project to maintain clear boundaries between teams and organize security assessments effectively.

## How GitHub repositories fit into the hierarchy
<a name="_how_github_repositories_fit_into_the_hierarchy"></a>

GitHub repositories are integrated through a multi-step process that connects organizational resources to specific applications:

1.  **Register at the tenant level** - Authorize the AWS Security Agent GitHub App for your GitHub organization or user account once

1.  **Connect at the Agent Space level** - Select specific repositories to connect to each Agent Space

1.  **Configure usage per repository** - Enable specific capabilities for each connected repository:
   +  **Code review** - Full source code scanning and automated pull request analysis
   +  **Penetration testing context** - Application understanding from source code during penetration tests
   +  **Automatic code remediation** - Automated pull requests with vulnerability fixes for code review and penetration testing findings

A single repository can be connected to multiple Agent Spaces with different capabilities enabled in each one.

## Key differences between security capabilities
<a name="_key_differences_between_security_capabilities"></a>

Each security capability in AWS Security Agent follows a different workflow model based on how security teams use it.

### Continuum for penetration testing: Reusable configurations with independent executions
<a name="_continuum_for_penetration_testing_reusable_configurations_with_independent_executions"></a>

Penetration tests use a configuration-and-run model that supports iterative security testing:
+  **Create once, execute many times** - Define a configuration for a specific target (API endpoint, feature area) with scope boundaries, authentication, and test parameters
+  **Independent executions** - Execute the same configuration multiple times as you improve security. Each execution is independent and generates new findings

This model supports continuous security validation as you develop and deploy improvements.

### Continuum for design reviews: One-off assessments with cloning
<a name="_continuum_for_design_reviews_one_off_assessments_with_cloning"></a>

Design reviews are independent assessments that don’t follow a reusable configuration model:
+  **Single assessment** - Each design review analyzes uploaded documents once against your organization’s security requirements
+  **Cannot re-run** - Design reviews are not reusable. You cannot re-run the same review
+  **Clone for updates** - Clone an existing design review to create a new review with the original documents pre-loaded, allowing you to update documents and run a new analysis

This model supports point-in-time architectural security assessments.

### Continuum for code reviews: Reusable configurations with on-demand scans and automatic PR analysis
<a name="_continuum_for_code_reviews_reusable_configurations_with_on_demand_scans_and_automatic_pr_analysis"></a>

Code reviews provide two modes of operation for securing your source code:
+  **Full code reviews (web application)** - Create code review configurations that select GitHub repositories or S3 sources, then run comprehensive scans on demand. Each run performs static analysis across your full source code and generates findings with remediation guidance. You can re-run the same code review configuration as your code evolves.
+  **Pull request comments (GitHub)** - Enable automated analysis for connected GitHub repositories. AWS Security Agent automatically reviews pull requests when they are marked as ready for review and posts security findings as comments directly in GitHub.

Both modes use your configured code review settings (security vulnerabilities, custom requirements, or both) and support automated code remediation through pull requests.

### Continuum for threat models: Reusable configurations with on-demand runs
<a name="_continuum_for_threat_models_reusable_configurations_with_on_demand_runs"></a>

Threat models use a configuration-and-run model that supports iterative assessment of your architecture:
+  **Create once, run many times** – Define a threat model by selecting source code as sources, uploading design documents as scope docs, or both. Run it on demand and re-run it as your code and design evolve.
+  **Flexible inputs** – Run a threat model on source code only, design documents only, or both. Scope docs define what the agent focuses its analysis on; source code provides context about your existing system.
+  **System overview and threats** – Each run produces a system overview describing your application’s architecture, trust boundaries, data flows, and security posture, along with a set of threats classified by STRIDE category with severity, evidence, and actionable recommendations.

## Understanding resource relationships
<a name="_understanding_resource_relationships"></a>

The hierarchy determines where each resource lives: the AWS Management Console for tenant-level resources and Agent Space settings, the Security Agent web application for assessments and findings, and GitHub for pull request findings and remediation. For the full breakdown of what you do in each interface and the roles involved, see [How AWS Security Agent works](how-it-works.md).
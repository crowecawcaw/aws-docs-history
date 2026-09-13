

# Governance
<a name="acxd-governance"></a>

Agentic CX designer helps protect your workspace and deployed conversational AI applications through access control, sensitive data handling, secure integrations, runtime guardrails, and auditability.

Governance in agentic CX designer is supported through:


| **Security area** | **What it helps control** | 
| --- | --- | 
| **Access control** | Who can access a workspace and what they can view, create, edit, or manage. | 
| **Data protection** | What sensitive information is stored, logged, masked, or redacted. | 
| **Secure integrations** | How applications connect to external systems, APIs, credentials, and environments. | 
| **Runtime protections** | How user inputs and application outputs are checked during conversations. | 
| **Auditability** | What changed, when it changed, and which user performed the action. | 

Together, these controls help teams build conversational AI applications that are safer, more governed, and easier to monitor across development and production environments.

## Access control
<a name="acxd-governance-access-control"></a>

Access in agentic CX designer is managed through Amazon Connect Customer and controlled at the workspace level.

Account Administrators can add users from the available Connect Customer user profiles, assign those users to one or more workspaces, and grant workspace roles based on what each person needs to do.

Use roles and permissions to control who can:
+ View workspace resources
+ Create or edit applications and flows
+ Configure integrations and Data requests
+ Manage guardrails
+ Review analytics and conversation history
+ Create builds or deploy applications
+ Manage users, roles, and workspace settings

**Common governance goals**
+ Limit who can deploy to Production
+ Restrict who can configure integrations and secrets
+ Allow read-only access for reviewers and stakeholders
+ Separate access by business unit, team, environment, or project
+ Review workspace access regularly

## Sensitive data handling
<a name="acxd-governance-sensitive-data"></a>

Agentic CX designer provides controls that help reduce exposure of sensitive information in conversations, logs, transcripts, and connected systems.

Use sensitive data controls to help prevent protected or restricted values from appearing where they should not.
+ Mark fields as Sensitive in Data request schemas and slots so values are redacted where supported.
+ Use Guardrails to detect and mask sensitive patterns, such as credit card numbers, IDs, email addresses, or other restricted values.
+ Avoid storing sensitive data in conversation messages unless it is required for the experience.
+ Review transcripts and logs to confirm sensitive values are handled according to your organization's policies.
+ Use state modifications carefully when storing or clearing sensitive context.

## Secure integrations and secrets
<a name="acxd-governance-secure-integrations"></a>

Integrations are a critical security boundary between a conversational AI application and external systems.

Agentic CX designer supports secure integration patterns through structured Data requests, schemas, secrets, and environment-specific configuration.

**Best practices**
+ Store API keys, tokens, and credentials as Secrets instead of hardcoding them in headers or payloads.
+ Use separate Development and Production endpoints when possible.
+ Validate request and response payloads with clear schemas.
+ Only send the data required for the external system to complete the task.
+ Mark sensitive request or response fields appropriately.
+ Test integrations in a non-production environment before deployment.
+ Confirm failure, timeout, and fallback paths are handled safely.

## Runtime protections
<a name="acxd-governance-runtime-protections"></a>

Security is not only about workspace access. It also includes what happens while users interact with your conversational AI application.

Guardrails evaluate conversation messages at runtime and can check user inputs before they are processed or application outputs before they are returned to the user.

Guardrails can help with:


| **Protection** | **Guardrail type** | 
| --- | --- | 
| Prompt injection or jailbreak detection | Input | 
| Sensitive data detection or masking | Input or Output | 
| Brand, legal, or compliance checks | Output | 
| Hallucination or unsupported claim detection | Output | 
| Redirecting risky conversations to a controlled flow | Input or Output | 
| Logging policy violations for review | Input or Output | 

Guardrails can enforce behavior using actions such as Override, Mask, Redirect, or Flag, depending on how the application should respond when a rule is triggered.

## Auditability and governance review
<a name="acxd-governance-auditability"></a>

Agentic CX designer includes governance features that help teams review workspace changes and maintain a traceable history of activity.

Use Audit to review write and delete events across workspace resources, including who made a change, when it happened, and where it occurred.

Use Versioning to review previous configurations of supported resources and restore earlier versions when needed.

These features help teams:
+ Investigate unexpected workspace changes
+ Confirm who updated or removed a resource
+ Review activity around production-impacting resources
+ Support internal change-management processes
+ Recover from breaking changes
+ Preserve a record of workspace activity over time

**Topics**
+ [Access control](#acxd-governance-access-control)
+ [Sensitive data handling](#acxd-governance-sensitive-data)
+ [Secure integrations and secrets](#acxd-governance-secure-integrations)
+ [Runtime protections](#acxd-governance-runtime-protections)
+ [Auditability and governance review](#acxd-governance-auditability)
+ [Roles and permissions](acxd-roles-permissions.md)
+ [Versioning](acxd-versioning.md)
+ [Audit](acxd-audit.md)
+ [Guardrails](acxd-guardrails.md)
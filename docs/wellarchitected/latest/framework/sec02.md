

# Identity management

 Identity management establishes who and what can authenticate to a workload, and how that authentication is proven and governed. Every workload serves a mix of principals: employees, external customers, partner systems, devices, and automated processes. Each carries a different trust model, a different lifecycle, and a different tolerance for authentication friction, and each must be identified before authentication methods are chosen. 

 Managing identity well depends on treating people and machines as first-class citizens of the same system. A single source of truth for authentication keeps controls uniform across applications and lets lifecycle events, from onboarding to deactivation, propagate without per-application work. Preferring credentials that expire on their own shrinks the window in which an exposed credential is useful, and the few credentials that must persist are stored securely, scoped tightly, and reviewed on a schedule. 

 AI agents and autonomous workflows are a distinct category to plan for. An agent acts on behalf of a person or system and can make dynamic decisions, invoke tools, and chain actions across services, accounts, and sessions, often carrying the originating principal's identity through a multi-step workflow. Scope an agent's permissions to the intersection of what the originating principal may do and what the task requires, enforce time limits on every delegated session, and log both the agent's actions and the human or system that initiated them. 

 This capability covers identifying principals and their use cases, centralizing authentication, using short-lived credentials, storing the remaining secrets securely, and auditing and rotating what is left. It does not cover the permissions those identities are granted or how access to specific resources is authorized, which the permissions capability addresses. 


|  SEC02: How do you manage identities for people and machines?  | 
| --- | 
|  [SEC02-BP01 Identify principals and identity use-cases](sec02-bp01.md)  | 
|  [SEC02-BP02 Use temporary credentials](sec02-bp02.md)  | 
|  [SEC02-BP03 Store and use secrets securely](sec02-bp03.md)  | 
|  [SEC02-BP04 Rely on a centralized identity provider for users and machines](sec02-bp04.md)  | 
|  [SEC02-BP05 Audit and rotate credentials periodically](sec02-bp05.md)  | 

## Capability intent
<a name="sec02-intent"></a>
+  Every principal that interacts with a workload, including workforce users, external customers, federated users, service accounts, devices, and automated agents, is inventoried, and its identity use cases are mapped before authentication methods are chosen. 
+  Both people and machines authenticate against a central identity provider that serves as the source of truth, so controls stay uniform across applications and lifecycle events propagate automatically. 
+  Access relies on short-lived credentials that expire on their own, and the few long-term credentials that remain are scoped, monitored, and rotated on a defined schedule. 
+  Secrets that must persist are stored encrypted in a managed service, access to them is scoped and audited, and continuous scanning keeps them out of source code. 
+  Identities, permissions, and credentials are audited on a schedule, unused identities and roles are removed, and required controls such as multi-factor authentication are enforced continuously. 
+  Authentication strength matches the sensitivity of each use case, and the identity design absorbs growth in users, tenants, and services without a redesign. 

## Common issues to watch for
<a name="sec02-issues"></a>
+  People, service accounts, and automated processes are handled under one identity scheme, so the resulting controls are too weak for sensitive access and too heavy for routine access. 
+  Long-term access keys sit in source code, configuration files, or shipped applications, where they can circulate for years and stay usable until someone finds and revokes them. 
+  Each application manages its own identities, so users juggle multiple logins and the security team has no single view of who has access. 
+  Secrets are stored without encryption and never rotated, so a single exposure remains there indefinitely. 
+  Credentials are never audited after creation, which leaves orphaned accounts, stale permissions, and required controls that quietly lapse. 
+  Identity decisions are deferred until late in development, which forces rework when authentication, tenancy, and session requirements surface. 


# Identity and access management

 Identity and access management sets who can do what across your cloud environment. Strong identity controls protect accounts and resources while letting the business move at the speed it needs. This capability covers the best practices for protecting privileged accounts, centralizing identity, enforcing least privilege, establishing data perimeters to guard your organization's boundaries, and keeping permissions tuned over time. 


|  FND02: How do you manage identities, enforce least privilege, and protect access to accounts and resources?  | 
| --- | 
|  [FND02-BP01 Protect account root users, and establish alternate contacts](fnd02-bp01.md)  | 
|  [FND02-BP02 Use strong sign-in mechanisms](fnd02-bp02.md)  | 
|  [FND02-BP03 Employ a centralized identity provider](fnd02-bp03.md)  | 
|  [FND02-BP04 Establish controls to manage access based on lifecycle](fnd02-bp04.md)  | 
|  [FND02-BP05 Grant least privilege access](fnd02-bp05.md)  | 
|  [FND02-BP06 Define permission guardrails for your organization](fnd02-bp06.md)  | 
|  [FND02-BP07 Implement data perimeter controls to help prevent unintended access](fnd02-bp07.md)  | 
|  [FND02-BP08 Audit and rotate credentials periodically](fnd02-bp08.md)  | 
|  [FND02-BP09 Establish a process to continually review and refine permissions](fnd02-bp09.md)  | 
|  [FND02-BP10 Establish workload and machine identity federation](fnd02-bp10.md)  | 

## Capability intent
<a name="fnd02-intent"></a>
+  Workforce identity is centralized, and access to AWS flows by federation from a single authoritative source that synchronises joiner, mover, and leaver changes automatically. 
+  The highest-privilege identities — starting with account root users — are protected, monitored, and used only by exception. 
+  Permissions default to least privilege and are refined continuously based on what access is actually used. 
+  Organization-wide guardrails and data perimeter controls act independently of individual permission grants, keeping trusted identities, resources, and networks in scope. 
+  Workloads and machines obtain short-lived credentials through federation, and the long-lived credentials that remain are inventoried, owned, and rotated on a known schedule. 

## Common issues to watch for
<a name="fnd02-issues"></a>
+  Long-lived IAM access keys persist for workloads, CI/CD pipelines, and on-premises systems where federation is available, leaving credentials in systems that rarely rotate them and often have no clear owner. 
+  MFA is not enforced on privileged identity provider users beyond the AWS root user requirement, leaving high-risk identities less protected than the controls that guard them. 
+  Break-glass processes depend on the same identity provider or account they are meant to work around, so the path to recover access fails at exactly the moment it is needed. 
+  Organization-wide guardrails are missing, overly permissive at the root organizational unit, or absent on security and audit accounts, so detective controls can be disabled by an administrator account with unauthorized access. 
+  Permissions are copied from prior projects and reviewed only at audit time, so roles accumulate access well beyond current needs and reviews produce activity rather than reduction. 
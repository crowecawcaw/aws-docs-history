

# Permissions management

 Permissions decide which identities can take which actions on which resources, and under what conditions. They apply to the people who operate a workload and to the machine identities that make up the workload itself. Managing them well means granting only the access a function needs and keeping that grant current as the function changes. 

 Permissions management scales through structure rather than effort. Expressing access as reusable policies, roles, or attributes lets an organization grant and adjust permissions without editing rules one identity at a time. Centralizing where those decisions are made and evaluated keeps them consistent as the number of components and the range of access paths grow. 

 This capability covers scoping permissions to function, managing authorization consistently across a workload, and controlling how resources are shared publicly, across accounts, and with third parties. It does not cover establishing the identities themselves, which the identity management capability addresses. 


|  SEC03: How do you manage permissions for people and machines?  | 
| --- | 
|  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md)  | 
|  [SEC03-BP02 Use scalable and centralized permissions management in your workload](sec03-bp02.md)  | 
|  [SEC03-BP03 Analyze public and cross-account access](sec03-bp03.md)  | 
|  [SEC03-BP04 Share resources securely within your organization](sec03-bp04.md)  | 
|  [SEC03-BP05 Share resources securely with a third party](sec03-bp05.md)  | 

## Capability intent
<a name="sec03-intent"></a>
+  Permissions on every identity, human and machine, are scoped to what the function requires and shrink as functions change, so unauthorized access reaches only the actions that identity was granted. 
+  Each workload component runs under its own distinct identity with temporary credentials rather than a shared long-lived key. 
+  Authorization is evaluated through a centralized, policy-based mechanism driven by an explicit model of principals, actions, resources, and conditions, so decisions stay consistent, versioned, and auditable, and authentication stays separate from authorization. 
+  Public and cross-account access is inventoried, deliberately approved, and monitored continuously, so exposure remains limited to the resources that require it. 
+  Sharing within the organization and with third parties happens through controlled, scoped mechanisms bounded by a trust perimeter, and that access can be audited and revoked on a defined cadence. 

## Common issues to watch for
<a name="sec03-issues"></a>
+  Components share a single identity or role, so audit trails blur and the permission set widens to the union of every consumer's needs. 
+  Authorization logic lives inside application code or a database table, so rules drift apart across components and changing one permission requires a deployment. 
+  Permissions granted to unblock a feature stay in place after the feature is gone, so access accumulates as drift that no one revisits. 
+  Public or cross-account grants are made to unblock a project and never reviewed, so broad access surfaces during an incident rather than before one. 
+  Third parties receive long-term access keys instead of temporary credentials, leaving a standing secret outside the organization's visibility. 
+  Cross-account trust relationships omit a unique external ID, leaving the workload open to the confused deputy problem. 
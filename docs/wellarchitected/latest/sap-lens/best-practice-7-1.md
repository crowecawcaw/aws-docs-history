# Best Practice 7.1 – Understand your

SAP user categories and access mechanisms

The types of users accessing your SAP system will determine the security controls you
need to apply. By examining each use case, you can develop a strategy. This should include
how you manage identities, authentication, tooling and mechanisms to support those
requirements.

**Suggestion 7.1.1 Understand data access permissions and permitted
actions**

SAP systems often contain highly sensitive business data. As you define your user
types, understand the data access permissions. (For example, an administrative database user
does not have the fine-grained controls of an application user, and therefore may be more
critical.) Also refer to [Security]: [Best Practice 5.2 -
Classify the data within your SAP workloads](best-practice-5-2.md "best-practice-5-2.md").

Consider the following questions in relation to your SAP system access:

- Do the actions taken by an administrative or service user need to be traceable to
  a uniquely identifiable individual?
- At which layer of the application will the access be granted?
- Can you restrict access to a subset of functionality via permissions?
- Can you restrict access to a subset of functionality via other controls, for
  example exposing only certain services?
- Is there a requirement to audit the actions taken?

**Suggestion 7.1.2 – Understand the network and/or location from which
users will access the SAP systems**

Network and/or location often contributes to the security risk profile and may
determine whether the user is considered trusted or untrusted. Typically, this is coupled
with the controls to prevent unauthorized access (refer to [Best Practice 6.1 - Ensure that security and auditing are built into the SAP network
design](best-practice-6-1.md "best-practice-6-1.md")).

This can influence your design. For example, an untrusted internet user or device may
require additional factors of authentication to access your SAP workload, when compared
with a trusted user from your corporate network.

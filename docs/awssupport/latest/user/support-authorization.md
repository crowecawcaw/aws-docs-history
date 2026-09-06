

# AWS Support authorization
<a name="support-authorization"></a>

AWS Support authorization gives you auditable control over AWS Support access to information about your services that might contain your data during support case resolution.

A support permit is a customer-managed resource that defines the scope and conditions of authorized access. Each support permit is cryptographically signed by using a customer-managed AWS Key Management Service (AWS KMS) key that you control. AWS CloudTrail logs all actions taken on your resources under your authorization during the granted access period, giving you a complete audit trail.

**Important**  
The information obtained through AWS Support authorization might be accessed from outside the AWS Region where your data is stored.

AWS Support authorization supports two authorization scenarios to fit your operational needs.

Proactive authorization  
You create support permits in advance to pre-authorize access within a defined scope. When AWS Support needs access to resolve an issue, a signed authorization is automatically issued if a matching support permit exists. This reduces resolution time during incidents.

Reactive authorization  
AWS Support submits a support permit request in the Support Center when access to information about your services is needed. You review the request and either approve it by creating a scoped support permit or reject it. If you don't approve the request, AWS Support can't access the requested information. This gives you per-case control over access decisions.

**Topics**
+ [AWS Support authorization concepts](support-authorization-concepts.md)
+ [Getting started with AWS Support authorization](support-authorization-getting-started.md)
+ [Configuring AWS KMS keys for AWS Support authorization](support-authorization-kms.md)
+ [Managing support permits](support-authorization-permits.md)
+ [Managing support permit requests](support-authorization-permit-requests.md)
+ [Discovering support actions](support-authorization-actions.md)
+ [Monitoring AWS Support authorization with AWS CloudTrail](support-authorization-monitoring.md)
+ [AWS Support authorization quotas](support-authorization-quotas.md)
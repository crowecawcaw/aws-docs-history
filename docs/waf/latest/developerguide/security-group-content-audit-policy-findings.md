**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Security group content audit policy Firewall Manager findings

This page explains Firewall Manager findings for security group content audit policies.

For information about security group content audit policies, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md "security-group-policies.md").

###### Security group is not in compliance with content audit security group.

A Firewall Manager security group content audit policy has identified a noncompliant security group.
This is a customer-created security group that's in scope of the content audit
policy and that doesn't comply with the settings defined by the policy and its audit
security group. You can enable Firewall Manager remediation on the policy, which modifies the
noncompliant security group to bring it into compliance.

- Severity – 70
- Status settings – PASSED/FAILED
- Updates – Firewall Manager updates this finding.

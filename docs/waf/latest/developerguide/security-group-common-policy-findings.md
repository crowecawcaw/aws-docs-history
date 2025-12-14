**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Security group common policy Firewall Manager findings

This page explains Firewall Manager findings for security group common policies.

For information about security group common policies, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md "security-group-policies.md").

###### Resource has misconfigured security group.

Firewall Manager has identified a resource that is missing the Firewall Manager managed security group
associations that it should have, according to the Firewall Manager policy. You can enable
Firewall Manager remediation on the policy, which creates the associations according to the
policy settings.

- Severity – 70
- Status settings – PASSED/FAILED
- Updates – Firewall Manager updates this finding.

###### Firewall Manager replica security group is out of sync with primary security group.

A Firewall Manager replica security group is out of sync with its primary security group, according
to their common security group policy. You can enable Firewall Manager remediation on the
policy, which syncs the replica security groups with the primary.

- Severity – 80
- Status settings – PASSED/FAILED
- Updates – Firewall Manager updates this finding.

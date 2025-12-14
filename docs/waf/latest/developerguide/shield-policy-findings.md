**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# AWS Shield Advanced policy Firewall Manager findings

This page explains Firewall Manager findings for AWS Shield Advanced policies.

For information about AWS Shield Advanced policies, see [Using security group policies in Firewall Manager to manage Amazon VPC security groups](security-group-policies.md "security-group-policies.md").

###### Resource lacks Shield Advanced protection.

An AWS resource that should have Shield Advanced protection, according to the Firewall Manager policy,
doesn't have it. You can enable Firewall Manager remediation on the policy, which will enable
the protection for the resource.

- Severity – 60
- Status settings – PASSED/FAILED
- Updates – If Firewall Manager performs the remediation
  action, it will update the finding and the severity will lower from `HIGH` to
  `INFORMATIONAL`. If you perform the remediation, Firewall Manager will not
  update the finding.

###### Shield Advanced detected attack against monitored resource.

Shield Advanced detected an attack on a protected AWS resource. You can enable Firewall Manager
remediation on the policy.

- Severity – 70
- Status settings – None
- Updates – Firewall Manager does not update this finding.

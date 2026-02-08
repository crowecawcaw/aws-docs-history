# HNSEC02-BP04 Limit access to networking APIs

Implement strict controls over network management interfaces and
APIs to prevent unauthorized access and changes to critical network
infrastructure. This includes limiting access based on identity,
role, and network location while maintaining comprehensive audit
trails of all management actions.

**Desired outcome:** Prevent
unauthorized access and modification of sensitive networking
resources by restricting API access to approved personnel and secure
locations.

**Level of risk exposed if this best practice
is not established:** High

**Benefits of establishing this best
practice:**

- Minimizes risk of accidental or malicious changes to critical
  network resources
- Supports enforcement of least privilege and security boundaries
- Reduces attack surface and potential for misconfiguration
- Enables better auditability and compliance

## Implementation guidance

- Grant access to networking APIs only to authorized networking
  teams or accounts. For example, you can achieve this using AWS
  IAM policies and resource-based policies.
- Monitor and audit API call to sensitive networking services,
  using services such as AWS CloudTrail.
- Regularly review permissions and restrict access on a
  least-privilege basis.

## Resources

- [Controlling
  Access to AWS Resources Using Policies](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
- [IAM
  Policy Conditions for Source IP](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md#AvailableKeys "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md#AvailableKeys")
- [AWS CloudTrail Documentation](../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md "../../../awscloudtrail/latest/userguide/cloudtrail-user-guide.md")
- [Best
  Practices for IAM Permissions](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")

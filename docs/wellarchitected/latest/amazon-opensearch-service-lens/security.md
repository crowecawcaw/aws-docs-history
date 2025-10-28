# Security

The security pillar includes the ability to protect information,
systems, and assets while delivering business value. This section
provides in-depth, best practice guidance for architecting secure
OpenSearch domains.

###### Focus areas

- [Design principles](#design-principles-sec "#design-principles-sec")
- [Security foundation](security-foundation.md "security-foundation.md")
- [Detection](detection.md "detection.md")
- [Data protection](data-protection.md "data-protection.md")
- [Key AWS services](key-aws-services-sec.md "key-aws-services-sec.md")
- [Resources](resources-sec.md "resources-sec.md")

## Design principles

In addition to the
[security
principles](../Security%20design%20principles*%0dsecurity-pillar/security.md "../Security%20design%20principles*%0dsecurity-pillar/security.md") of the AWS Well-Architected Framework, the
following design principles can enhance the security posture of
OpenSearch workloads:

- **Maintain traceability of your
  OpenSearch domains:** Monitor configuration changes
  to your domain, track user activity, and audit requests for
  data--including detailed connection attributes. Use AWS CloudTrail logging and OpenSearch audit logs to monitor the
  use of configuration APIs and requests to your data.
- **Maintain perimeter security for your
  domain:** Secure the perimeter to your domain by
  using AWS identity and resource policies to associate
  identities and resources to specific allow/deny actions.
  Create logically isolated networks using an Amazon Virtual Private Cloud (VPC), and Amazon VPC security groups to allow
  traffic only from known entities.
- **Protect access to sensitive
  data:** Secure access to your sensitive or
  confidential data using advanced security controls. Use index,
  document, or field-level security to limit access to specific
  indices, documents, or fields.
- **Implement least privilege access
  controls:** Manage user access and monitor cluster
  configuration by using access control features like IAM
  policies or fine-grained access control.
- **Apply security updates
  regularly:** Protect your data from security
  vulnerabilities. To minimize the need for version upgrades,
  OpenSearch Service provides backward compatible security
  patches and upgrades for all supported versions of OpenSearch
  and OpenSearch.
- **Maintain compliance
  requirements:** OpenSearch Service maintain
  compliance with several industry standards, including SOC, PIC
  and HIPAA. These validations can help you meet your
  organization's compliance and governance requirements.

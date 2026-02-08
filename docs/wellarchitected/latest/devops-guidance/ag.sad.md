# [AG.SAD.1] Centralize and federate access with temporary credential vending

**Category:** FOUNDATIONAL

Implement a centralized subsystem for federated access and temporary credential
vending to maintain secure and controlled access to your environments, workloads, and
resources. By implementing a federated access solution, you can leverage your existing
identity systems, provide single sign-on (SSO) capabilities, and avoid the need to maintain
separate user identities across multiple systems which makes scaling in a DevOps model more
tenable. Centralizing identity onboarding and permission management eliminate the
inefficiencies of manual processes, reduce human error, and enable scalability as your
organization grows.

Grant users and services fine-grained access to help ensure secure, granular control
as they interact with resources and systems. By applying the least privilege principle, you
can minimize the risk of unauthorized access and reduce the potential damage from
compromised keys while retaining full control over access to resources and environments. To
reduce the likelihood of keys being compromised, always vend short-lived, temporary
credentials that are scoped for specific tasks to help ensure that privileges are granted
only for the duration needed.

**Related information:**

- [AWS Well-Architected Cost Optimization Pillar: COST02-BP04
  Implement groups and roles](../cost-optimization-pillar/cost_govern_usage_groups_roles.md "../cost-optimization-pillar/cost_govern_usage_groups_roles.md")
- [Security
  best practices in IAM](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md")
- [AWS Well-Architected Security Pillar: SEC02-BP04 Rely on a
  centralized identity provider](../security-pillar/sec_identities_identity_provider.md "../security-pillar/sec_identities_identity_provider.md")
- [IAM Identity Center](../../../singlesignon/latest/userguide/what-is.md "../../../singlesignon/latest/userguide/what-is.md")
- [What
  is SSO (Single-Sign-On)?](https://aws.amazon.com/what-is/sso/ "https://aws.amazon.com/what-is/sso/")
- [Identity
  providers and federation](../../../IAM/latest/UserGuide/id_roles_providers.md "../../../IAM/latest/UserGuide/id_roles_providers.md")

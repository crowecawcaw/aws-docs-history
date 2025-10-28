# Identity management

As you scale your use of the AWS Cloud, you need robust identity and
permission management processes to help ensure that you follow the
standard security advice of granting least privilege, or granting
only the permissions required to perform a task. Robust identity
management helps ensure that the right systems and people have
access to the right resources under the right conditions. This also
needs to be done while not overburdening operations capabilities
with too many, too granular or too complex permission or identity
constructs. The M&G Guide includes the recommendations of the
[Security
Pillar](../security-pillar/identity-management.md "../security-pillar/identity-management.md") for managing identities and access permissions across
all cloud resources in your multi-account strategy in order to be
migration ready, scale ready, and operating efficiently.

The
[Security
Pillar](../security-pillar/identity-management.md "../security-pillar/identity-management.md") describes the difference between human and machine
identities. It also shows that centralized administration of human
identities and access to your environments with an identity provider
is a critical strategy to managing authentication and authorization
across your enterprise. This is important for managing and
governing, as it makes it easier to manage access across multiple
applications and services because you are creating, managing, and
revoking access from a single location. For example, if someone
joins or leaves your organization, you can add or revoke that
individual’s access for all applications and services (including
AWS) from one location. This aligns with ITIL best practices, and
reduces the need for multiple credentials and provides an
opportunity to integrate with existing human resources (HR)
processes. In AWS, we consider machine identities distinctly from
human identities. Machine identities (like service roles) still
reside within AWS IAM and are designed to uphold the principle of
least privilege, but are not managed by your identity provider.

Define access policies and mechanisms that include granting least
privilege access, sharing resources securely, and reducing
permissions continually (including the removal of unused
permissions) with AWS IAM Access Analyzer. Review how permissions
are actually being authored, validated, and used over time, so that
you can remove unnecessary permissions in accordance with the
principle of least privilege. This would include adding
observability rules for “last accessed” data, such as a timestamp
depicting when an identity policy or principal (such as a user or
role) last used a service or performed an action from supported
services. This enables you to more easily identify unused
permissions and improve your security posture by removing the
permissions that are not necessary for the user, group, or role to
perform a specific task. Both AWS and AWS Partners provide tools for
the creation, review, and revoking of permissions in an automated
manner throughout your software development lifecycle (SDLC) or
development, security and operations (DevSecOps) cycles.

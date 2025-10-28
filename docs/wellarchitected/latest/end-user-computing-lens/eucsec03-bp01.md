# EUCSEC03-BP01 Restrict user permissions to the minimum required to perform their role

To implement the principle of least privilege when configuring
AWS EUC services, define appropriate access controls for role
categories like users, service desk users, first-level
administrators, second-level administrators, and accounts used
for automation.

**Level of risk exposed if this best
practice is not established:** High

## Implementation guidance

- **Limit the use of administrator
  permissions:** Users should not be granted local
  administrator access to Amazon WorkSpaces or AppStream 2.0
  instances unless it is required for them to undertake
  their role. Use tools and products that provide the
  ability to temporarily provide elevated rights in
  preference to granting users long term administrative
  access.
- **Do not provide all support staff
  with administrator permissions:** Grant service
  desk users should the minimal set of access permissions to
  allow them to perform their function. This can vary among
  organizations, but service desk users should not be
  granted full access to the Amazon WorkSpaces and AppStream
  2.0 services.
- **Use administrative toolsets and
  automation to avoid the need to provide administrator
  permissions:** Administrators providing
  first-level support for the users consuming the AWS EUC
  service can use the enhanced administrative toolset that
  AWS offers in the form of the EUC toolkit. For more detail
  on the EUC Toolkit, see
  [Use EUC Toolkit to manage Amazon AppStream 2.0 and Amazon WorkSpaces](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/").
- **Audit and monitor privileged or
  sensitive operations:** Log any privileged or
  sensitive operations associated with the management of AWS
  EUC services. These logs can then be used to generate
  alerts as required.
- **Use temporary elevated access for
  privileged or sensitive operations:** When users
  occasionally require elevated or privileged access to
  support or operate the environment, provide a way for them
  to gain temporary elevated access. For an example of
  temporary elevated access to AWS IAM Identity Center, see
  [Temporary
  elevated access for AWS accounts](../../../singlesignon/latest/userguide/temporary-elevated-access.md "../../../singlesignon/latest/userguide/temporary-elevated-access.md").
- **Restrict the allocation and use of
  IAM permissions providing service access:**
  Administrators providing second or third-level support
  that use the AWS Management console require IAM
  permissions. Grant the minimal set of permissions to
  administrative users providing an enhanced level of
  support to users using
  [Amazon WorkSpaces](../../../workspaces/latest/adminguide/workspaces-access-control.md "../../../workspaces/latest/adminguide/workspaces-access-control.md") and

[AppStream
2.0](../../../appstream2/latest/developerguide/controlling-administrator-access-with-policies-roles.md "../../../appstream2/latest/developerguide/controlling-administrator-access-with-policies-roles.md") for them to fulfill their role.

- **Restrict the scope of access for
  service accounts:** Restrict permissions for
  service accounts for Amazon WorkSpaces (with Active
  Directory Connector) and Amazon AppStream 2.0 (with
  domain-joined fleets) to only allow them to create
  computer objects within their designated Organizational
  Unit (OU). For implementing service accounts, see
  [Amazon
  AppStream 2.0 Active Directory Administration](../../../appstream2/latest/developerguide/active-directory-admin.md#active-directory-permissions "../../../appstream2/latest/developerguide/active-directory-admin.md#active-directory-permissions") and

[AD
Connector prerequisites](../../../directoryservice/latest/admin-guide/prereq_connector.md#connect_delegate_privileges "../../../directoryservice/latest/admin-guide/prereq_connector.md#connect_delegate_privileges").

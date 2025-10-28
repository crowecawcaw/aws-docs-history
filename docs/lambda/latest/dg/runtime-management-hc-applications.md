# Controlling Lambda runtime update permissions for high-compliance applications

To meet patching requirements, Lambda customers typically rely on automatic runtime
updates. If your application is subject to strict patching freshness requirements, you may
want to limit use of earlier runtime versions. You can restrict Lambda's runtime management
controls by using AWS Identity and Access Management (IAM) to deny users in your AWS account access to the
[PutRuntimeManagementConfig](../api/API_PutRuntimeManagementConfig.md "../api/API_PutRuntimeManagementConfig.md") API operation.
This operation is used to choose the runtime update mode for a function. Denying access to
this operation causes all functions to default to the **Auto** mode. You can
apply this restriction across your organization by using a [service control policies
(SCP)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"). If you must roll back a function to an earlier runtime
version, you can grant a policy exception on a case-by-case basis.

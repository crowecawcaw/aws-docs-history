This guide documents the classic version of the AWS Wickr administration console, released before March
13, 2025. For documentation on the new AWS Wickr administration console, see [Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Other policy types

AWS supports additional, less-common policy types. These policy types can set the
maximum permissions granted to you by the more common policy types.

- **Permissions boundaries** – A permissions
  boundary is an advanced feature in which you set the maximum permissions that an
  identity-based policy can grant to an IAM entity (IAM user or role). You can
  set a permissions boundary for an entity. The resulting permissions are the
  intersection of entity's identity-based policies and its permissions
  boundaries. Resource-based policies that specify the user or role in the
  `Principal` field are not limited by the permissions boundary. An
  explicit deny in any of these policies overrides the allow. For more information
  about permissions boundaries, see [Permissions boundaries for
  IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") in the _IAM User Guide_.
- **Session policies** – Session policies are
  advanced policies that you pass as a parameter when you programmatically create a
  temporary session for a role or federated user. The resulting session's
  permissions are the intersection of the user or role's identity-based
  policies and the session policies. Permissions can also come from a resource-based
  policy. An explicit deny in any of these policies overrides the allow. For more
  information, see [Session policies](../../../IAM/latest/UserGuide/access_policies.md#policies_session "../../../IAM/latest/UserGuide/access_policies.md#policies_session") in the _IAM User Guide_.

# Understanding collaborator permissions

AWS Transform uses a workspace-based permission model to control access to resources and actions.
Each user is assigned a specific role within a workspace, which determines what actions they can perform.
A user can have different roles in different workspaces.

## User roles

AWS Transform supports five user roles within each workspace. These roles apply within the context of a workspace, and a user will be assigned roles in each workspace they are a member of. The access permissions defined for each role are workspace agnostic, so user A with the Administrator role in workspace A has the same permissions as user B with the Administrator role in workspace B.

## Role permissions

Detailed permissions for each role:

| Action | ResourceType     | Admin | Approver | Contributor | ReadOnly |
| ------ | ---------------- | ----- | -------- | ----------- | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Create | Workspace        | ✓     | ✓        | ✓           | ✓        |
| List   | Workspace        | ✓     | ✓        | ✓           | ✓        |
| Get    | Workspace        | ✓     | ✓        | ✓           | ✓        |
| Update | Workspace        | ✓     | ✗        | ✗           | ✗        |
| Delete | Workspace        | ✓     | ✗        | ✗           | ✗        |
| Create | ChatMessage      | ✓     | ✓        | ✓           | ✓        |
| Read   | ChatMessage      | ✓     | ✓        | ✓           | ✓        |
| Create | RoleAssociation  | ✓     | ✗        | ✗           | ✗        |
| Read   | RoleAssociation  | ✓     | ✓        | ✓           | ✓        |
| Update | RoleAssociation  | ✓     | ✗        | ✗           | ✗        |
| Delete | RoleAssociation  | ✓     | ✗        | ✗           | ✗        |
| Read   | CriticalHITLTask | ✓     | ✓        | ✓           | ✓        |
| Update | CriticalHITLTask | ✓     | ✓        | ✗           | ✗        |
| Delete | CriticalHITLTask | ✓     | ✓        | ✗           | ✗        |
| Read   | HITLTask         | ✓     | ✓        | ✓           | ✓        |
| Update | HITLTask         | ✓     | ✓        | ✓           | ✗        |
| Delete | HITLTask         | ✓     | ✓        | ✓           | ✗        |
| Create | Job              | ✓     | ✓        | ✓           | ✗        |
| Read   | Job              | ✓     | ✓        | ✓           | ✓        |
| Update | Job              | ✓     | ✓        | ✓           | ✗        |
| Delete | Job              | ✓     | ✓        | ✓           | ✗        |
| Read   | Worklog          | ✓     | ✓        | ✓           | ✓        |
| Create | Artifact         | ✓     | ✓        | ✓           | ✗        |
| Read   | Artifact         | ✓     | ✓        | ✓           | ✓        |
| Update | Artifact         | ✓     | ✓        | ✓           | ✗        |
| Delete | Artifact         | ✓     | ✓        | ✓           | ✗        |
| Create | Connector        | ✓     | ✓        | ✓           | ✗        |
| Read   | Connector        | ✓     | ✓        | ✓           | ✓        |
| Update | Connector        | ✓     | ✓        | ✓           | ✗        |
| Delete | Connector        | ✓     | ✓        | ✓           | ✗        | ## Human-in-the-loop (HITL) actions AWS Transform provides two types of HITL actions - standard and critical: Standard HITL actions These are routine actions that can be performed by users with Contributor, Approver, or Administrator roles. Critical HITL actions These are actions with significant impact, and thus require higher permission levels. Examples include: <br>• Merging code to main branches <br>• Performing graph decomposition <br>• Deploying code to production environments Critical HITL actions can only be performed by users with Approver or Administrator roles. To ensure there's a differentiation between Standard HITL and Critical HITL actions in AuthZ policies, AWS Transform provides two separate HITL APIs, one for completing a standard HITL action, and one for completing a critical HITL action. |

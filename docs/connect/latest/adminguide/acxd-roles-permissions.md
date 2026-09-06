

# User roles and permissions
<a name="acxd-roles-permissions"></a>

Access in agentic CX designer is managed through roles and permissions and controlled at the workspace level.

This means users do not create standalone agentic CX designer accounts manually. Instead, Account Administrators select from the user profiles already available in the connected Connect Customer instance, add those users to the appropriate agentic CX designer workspace, and assign each user a workspace role.

Workspace roles determine what a person can view, create, edit, or manage inside that workspace.

## Access model
<a name="acxd-roles-permissions-model"></a>

Agentic CX designer uses a workspace-based access model.


|  |  | 
| --- |--- |
| **Account-level access** | Determines whether a user can access Connect Customer and, depending on their permissions, launch or administer agentic CX designer. | 
| **Workspace assignment** | Determines which workspace or workspaces a user can open. | 
| **Workspace role** | Determines what the user can do inside a specific workspace. | 

A user may have access to one workspace, multiple workspaces, or no workspaces, depending on how an Account Administrator has configured their access.

Resources and permissions are not shared automatically across workspaces. This means:
+ Applications in one workspace do not appear in another workspace.
+ Flows and resources are managed independently by workspace.
+ User roles are assigned per workspace.
+ Access to one workspace does not automatically grant access to others.

If you are an Account Administrator or have been assigned a role in more than one workspace, you can switch between workspaces from the workspace dropdown in the upper-left corner of agentic CX designer.

## Account Administrators
<a name="acxd-roles-permissions-admin"></a>

Account Administrators manage workspace setup and user access for agentic CX designer.

Account Administrators can:
+ Launch agentic CX designer from the Connect Customer console
+ Access the Admin Hub
+ Create workspaces
+ Select users from available Connect Customer user profiles
+ Add users to one or more workspaces
+ Assign workspace roles & create custom roles
+ Manage workspace access over time

Users are selected from the profiles already available in the connected Connect Customer instance.

## Workspace users
<a name="acxd-roles-permissions-users"></a>

Workspace users are people who have been added to one or more agentic CX designer workspaces by an Account Administrator.

Workspace users can access the workspace or workspaces assigned to them. What they can do inside each workspace depends on their assigned role.

For example, one user may have edit access in a development workspace but read-only access in another workspace used for production review.

**To give a user access to agentic CX designer**

1. Open agentic CX designer from Connect Customer.

1. Go to the Admin Hub.

1. Select **Users**.

1. Add users from the available Connect Customer user profiles.

1. Assign each user a workspace role.

1. Save the changes.

Only users with the appropriate account-level permissions can manage workspace access.

## Workspace roles
<a name="acxd-roles-permissions-roles"></a>

Roles determine what users can do inside a workspace.


|  |  | 
| --- |--- |
| **Account Administrator** | Manages account-level setup, workspaces, user access, and role assignments through the Admin Hub. | 
| **Workspace Manager** | Manages resources inside an assigned workspace, depending on the permissions granted. | 
| **Builder** | Creates and edits conversational AI resources such as applications, flows, prompts, slots, and knowledge bases. | 
| **Developer** | Configures technical resources such as integrations, Data requests, APIs, secrets, and environment-specific settings. | 
| **Analyst** | Reviews analytics, conversation history, dashboards, evaluations, and performance data. | 
| **Viewer** | Views workspace resources without making changes. | 
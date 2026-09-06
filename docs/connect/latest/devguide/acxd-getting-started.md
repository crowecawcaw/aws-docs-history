# Getting Started

This guide walks you through setting up authentication and making your first Agentic
CX Designer SDK API call.

## Prerequisites

- An Agentic CX Designer workspace with an Administrator role
- Access to Agentic CX Designer workspace (Admin Hub)

## Authentication

ACXD SDK uses API key authentication. To get an API key you need a programmatic
user.

## Step 1: Create a Programmatic User

Programmatic users are machine identities that can authenticate with the ACXD SDK.
Only account administrators can create them.

1. In the Agentic CX Designer workspace, navigate to Admin Hub > Programmatic Users
2. Click **Create Programmatic User**
3. Provide a name and an optional description
4. Assign permissions via Role Configuration

### Role Configuration

Each programmatic user has a `roleConfig` that determines their access:

#### Account-level role

Grants full access across all workspaces in the account.

```
{
      "roleConfig": {
        "accountRole": "administrator"
      }
  }
```

#### Workspace-scoped roles

Grants specific permissions per workspace

```
{
    "roleConfig": {
      "workspaceRoles": [
        { "workspaceId": "your-workspace-id", "roleId": "role-uuid" }
      ]
    }
  }
```

Workspace-scoped users can be assigned pre-defined roles (administrator,
developer, content manager, read-only) or a custom role configured under Roles in
Admin Hub.

## Step 2: Generate an API Key

Once a programmatic user exists, generate an API key for it:

1. In Admin Hub → Programmatic Users, select your user
2. Click Generate API Key
3. Copy the full key immediately, it is shown only once

The key format is: `acxd_live_<prefix>.<secret>`

###### Important

Store your API key securely. It cannot be retrieved after creation. You can
generate up to 2 keys per programmatic user.

## Step 3: Install the SDK

```
npm install amazon-connect-acxd-sdk
```

## Step 4: Make your First Call

With your API key and workspace ID, you can make requests to the ACXD SDK.

```
import { AgenticCXDesignerClient, ListContextVariablesCommand } from 'amazon-connect-acxd-sdk';

const client = new AgenticCXDesignerClient({
  apiKey: 'acxd_live_...',
  workspaceId: 'your-workspace-uuid', // required for workspace-scoped operations
});

const response = await client.send(new ListContextVariablesCommand({}));
console.log(response.items);
```

For account-level operations (e.g., managing programmatic users, workspaces),
`workspaceId` is not required.

## Permissions

The API key is just a credential - it carries no permissions itself. Permissions are
resolved at request time from the programmatic user's assigned role. If the role is
updated in Admin Hub, the change takes effect immediately.

## Next Steps

- **API Reference**: Explore all available operations
- **Concepts**: Understand workspaces, applications, and flows
- **Error Handling**: Handle errors and retries gracefully

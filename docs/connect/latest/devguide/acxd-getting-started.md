

# Getting Started
<a name="acxd-getting-started"></a>

This guide walks you through setting up authentication and making your first Agentic CX Designer SDK API call.

## Prerequisites
<a name="acxd-getting-started-prerequisites"></a>
+ An Agentic CX Designer workspace with an Administrator role
+ Access to Agentic CX Designer workspace (Admin Hub)

## Authentication
<a name="acxd-getting-started-authentication"></a>

ACXD SDK uses API key authentication. To get an API key you need a programmatic user.

## Step 1: Create a Programmatic User
<a name="acxd-getting-started-step1"></a>

Programmatic users are machine identities that can authenticate with the ACXD SDK. Only account administrators can create them.

1. In the Agentic CX Designer workspace, navigate to Admin Hub > Programmatic Users

1. Click **Create Programmatic User**

1. Provide a name and an optional description

1. Assign permissions via Role Configuration

### Role Configuration
<a name="acxd-getting-started-step1-roleconfig"></a>

Each programmatic user has a `roleConfig` that determines their access:

#### Account-level role
<a name="acxd-getting-started-step1-account-role"></a>

Grants full access across all workspaces in the account.

```
{
      "roleConfig": {
        "accountRole": "administrator"
      }
  }
```

#### Workspace-scoped roles
<a name="acxd-getting-started-step1-workspace-roles"></a>

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

Workspace-scoped users can be assigned pre-defined roles (administrator, developer, content manager, read-only) or a custom role configured under Roles in Admin Hub.

## Step 2: Generate an API Key
<a name="acxd-getting-started-step2"></a>

Once a programmatic user exists, generate an API key for it:

1. In Admin Hub → Programmatic Users, select your user

1. Click Generate API Key

1. Copy the full key immediately, it is shown only once

The key format is: `acxd_live_<prefix>.<secret>`

**Important**  
Store your API key securely. It cannot be retrieved after creation. You can generate up to 2 keys per programmatic user.

## Step 3: Install the SDK
<a name="acxd-getting-started-step3"></a>

```
npm install amazon-connect-acxd-sdk
```

## Step 4: Make your First Call
<a name="acxd-getting-started-step4"></a>

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

For account-level operations (e.g., managing programmatic users, workspaces), `workspaceId` is not required.

## Permissions
<a name="acxd-getting-started-permissions"></a>

The API key is just a credential - it carries no permissions itself. Permissions are resolved at request time from the programmatic user's assigned role. If the role is updated in Admin Hub, the change takes effect immediately.

## Next Steps
<a name="acxd-getting-started-next-steps"></a>
+ **API Reference**: Explore all available operations
+ **Concepts**: Understand workspaces, applications, and flows
+ **Error Handling**: Handle errors and retries gracefully
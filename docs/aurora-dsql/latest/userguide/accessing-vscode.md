# Use Aurora DSQL driver for SQLTools

The Aurora DSQL Driver for SQLTools is a Visual Studio Code
extension for Amazon Aurora DSQL that integrates with SQLTools. It
enables developers to connect to and query Aurora DSQL databases directly
from VS Code. The driver is available for installation from
[Visual Studio Marketplace](https://marketplace.visualstudio.com "https://marketplace.visualstudio.com")
and [Open VSX Registry](https://open-vsx.org/ "https://open-vsx.org/").
Kiro, Cursor and other VSCode-based IDEs can use the
[Open VSX Registry](https://open-vsx.org/ "https://open-vsx.org/") to install
the driver following the standard installation procedure described in this page.

## Features

- Automatic IAM Authentication
- Standard database operations like browsing schemas, tables,
  and executing SQL queries.

## Installation

1. Open the Extensions view.
2. Search for "Aurora DSQL Driver for SQLTools".
3. Click "Install".

**Note:**

The
[SQLTools
extension](https://vscode-sqltools.mteixeira.dev "https://vscode-sqltools.mteixeira.dev") will be automatically installed if not already
present.

## Authentication

In Aurora DSQL all connections use
**IAM-based authentication** with
time-limited tokens.

The driver automatically handles Aurora DSQL authentication using
the
[Aurora DSQL Connector for node-postgres](https://github.com/awslabs/aurora-dsql-connectors/tree/main/node/node-postgres "https://github.com/awslabs/aurora-dsql-connectors/tree/main/node/node-postgres").

For more information on authentication in Aurora DSQL, see the
[user
guide](authentication-authorization.md "authentication-authorization.md").

## Create an Aurora DSQL Connection

### Prerequisites

- AWS credentials configured (via AWS CLI, environment
  variables, or IAM roles)

### Steps

1. Click the SQLTools icon in the left sidebar.
2. In the SQLTools pane, hover over CONNECTIONS and click the
   Add New Connection icon.
3. In the SQLTools Settings tab select Aurora DSQL Driver from
   the list.
4. Fill in the connection parameters.
   - AWS Region
     - Optional - the region will be parsed from the Aurora DSQL
       cluster endpoint.
     - Required when only a cluster ID is specified in the
       DSQL Cluster field.

   - AWS Profile
     - Used for token generation.
     - Uses the default profile if not specified.

5. Click the "Test Connection button" to test the
   connection.
6. Click Save Connection.

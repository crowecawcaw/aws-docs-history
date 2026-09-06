

# Use Aurora DSQL driver for SQLTools
<a name="accessing-vscode"></a>

 The Aurora DSQL Driver for SQLTools is a Visual Studio Code extension for Amazon Aurora DSQL that integrates with SQLTools. It enables developers to connect to and query Aurora DSQL databases directly from VS Code. The driver is available for installation from [Visual Studio Marketplace](https://marketplace.visualstudio.com) and [Open VSX Registry](https://open-vsx.org/). Kiro, Cursor and other VSCode-based IDEs can use the [Open VSX Registry](https://open-vsx.org/) to install the driver following the standard installation procedure described in this page. 

## Features
<a name="features"></a>
+  Automatic IAM Authentication 
+  Standard database operations like browsing schemas, tables, and executing SQL queries. 

## Installation
<a name="installation"></a>

1.  Open the Extensions view. 

1.  Search for "Aurora DSQL Driver for SQLTools". 

1.  Click "Install". 

 **Note:** 

 The [SQLTools extension](https://vscode-sqltools.mteixeira.dev) will be automatically installed if not already present. 

## Authentication
<a name="authentication"></a>

 In Aurora DSQL all connections use **IAM-based authentication** with time-limited tokens. The driver automatically handles Aurora DSQL authentication using the [Aurora DSQL Connector for node-postgres](https://github.com/awslabs/aurora-dsql-connectors/tree/main/node/node-postgres). 

 For more information on authentication in Aurora DSQL, see the [user guide](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/authentication-authorization.html). 

## Create an Aurora DSQL Connection
<a name="create-an-aurora-dsql-connection"></a>

### Prerequisites
<a name="prerequisites"></a>
+  AWS credentials configured (via AWS CLI, environment variables, or IAM roles) 

### Steps
<a name="steps"></a>

1.  Click the SQLTools icon in the left sidebar. 

1.  In the SQLTools pane, hover over CONNECTIONS and click the Add New Connection icon. 

1.  In the SQLTools Settings tab select Aurora DSQL Driver from the list. 

1.  Fill in the connection parameters. 
   +  AWS Region 
     +  Optional - the region will be parsed from the Aurora DSQL cluster endpoint. 
     +  Required when only a cluster ID is specified in the DSQL Cluster field. 
   +  AWS Profile 
     +  Used for token generation. 
     +  Uses the default profile if not specified. 

1.  Click the "Test Connection button" to test the connection. 

1.  Click Save Connection. 
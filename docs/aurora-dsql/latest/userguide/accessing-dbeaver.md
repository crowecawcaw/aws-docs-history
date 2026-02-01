# Use DBeaver to access Aurora DSQL

DBeaver is a universal SQL client that can be used to manage any database that has a JDBC driver. It is widely used among developers and database administrators because of its robust data viewing, editing, and management capabilities. Using DBeaver's cloud connectivity options, you can connect DBeaver to Aurora DSQL natively.

## DBeaver Pro

DBeaver PRO products offer native integration with Aurora DSQL as of version 25.3. Follow the instructions from [DBeaver Documentation](https://dbeaver.com/docs/dbeaver/Database-driver-Aurora-DSQL/ "https://dbeaver.com/docs/dbeaver/Database-driver-Aurora-DSQL/") to connect to your Aurora DSQL cluster.

## DBeaver Community Edition

DBeaver Community Edition is the free and open-source version. Visit the [download page](https://dbeaver.io/download/ "https://dbeaver.io/download/") for installation instructions. In order to connect to DSQL from DBeaver Community Edition, you need to install the [Aurora DSQL Plugin for DBeaver](https://github.com/awslabs/aurora-dsql-dbeaver-plugin "https://github.com/awslabs/aurora-dsql-dbeaver-plugin").

The [Aurora DSQL Plugin for DBeaver](https://github.com/awslabs/aurora-dsql-dbeaver-plugin "https://github.com/awslabs/aurora-dsql-dbeaver-plugin") is built on top of the [Aurora DSQL Connector for JDBC](https://github.com/awslabs/aurora-dsql-jdbc-connector "https://github.com/awslabs/aurora-dsql-jdbc-connector") and enables IAM authentication to Aurora DSQL clusters. It is conveniently installed through DBeaver UI and eliminates the need to write token generation code or manually supply a valid IAM token, simplifying the authentication while eliminating security risks associated with traditional user-generated passwords.

### Features

- IAM Authentication Support: Connect to Aurora DSQL clusters using AWS IAM credentials for secure, password-free authentication
- Automatic Driver Management: Seamlessly installs and configures the Aurora DSQL Connector for JDBC
- Flexible Connection Options: Choose between Host-based or JDBC URL-based connection configuration

### Aurora DSQL Plugin for DBeaver Installation

1. With DBeaver opened, Go to the Drop down menu **Help** → **Install New Software**
2. Click **Add** to add a new repository
3. Enter:
   - **Name**: `Aurora DSQL Plugin`
   - **Location**: `https://awslabs.github.io/aurora-dsql-dbeaver-plugin/update-site/`

4. Check **Aurora DSQL Connector for JDBC**
5. Click **Next**, accept the license, and complete the installation
6. Restart DBeaver when prompted

### Create an Aurora DSQL Connection

1. Click the **New Database Connection**
2. Select **Aurora DSQL**
3. Under **Server**, select one of the following for the **Connect by** setting
   - **Host**
     - to enable the user interface text inputs for the following fields:
       - **Endpoint:** DSQL Cluster Endpoint
       - **Username:** DSQL username (e.g. admin)
       - **AWS Profile:** e.g. default - The standard profile used when no specific profile is specified
       - **AWS Region (Optional):** must match the region where your DSQL cluster exists, otherwise authentication will fail

   - **URL**
     - JDBC URL in this format:

     ```
     jdbc:aws-dsql:postgresql://{cluster_endpoint}/{database}?user=admin&profile=default&region=us-east-1
     ```

     - Note: In this mode, only the URL input is enabled. In order to add parameters to the JDBC connection string, use the URL query parameters format starting with ? as the first parameter and append an & for subsequent parameters.

4. Click **Test Connection** to verify the Aurora DSQL connection works
5. Click **Finish**

## Troubleshooting

### Windows Trust Store Issue

Windows users may encounter issues downloading the Aurora DSQL Connector for JDBC driver from Maven Central.

**Cause:** Windows Trust Store may not include the certificates required to access Maven Central repository.

**Solution:**

1. Run DBeaver as "Administrator"
2. Uncheck this setting - Windows > Preferences > Connections > "Use Windows Trust store"

### Missing Driver Error

If you see a missing driver icon or connection errors, the Aurora DSQL (Community Plugin) may not be installed in your current DBeaver version. See below some examples of errors and how to fix them:

- Creating a new connection with the missing driver:

![Missing driver icon in DBeaver](images/dbeaver-missing-driver-icon.png)

- Attempting to connect without the driver:

![Error dialog when driver is missing](images/dbeaver-version-error-dialog.png)

**Cause:** When multiple DBeaver versions are installed, connection settings are shared but drivers are installed per application.

**Solution:** Reinstall the Aurora DSQL (Community plugin) by following the installation steps above.

###### Important

The administrative features provided by DBeaver for PostgreSQL databases (such as
**Session Manager** and **Lock
Manager**) don't apply to Aurora DSQL databases due to their unique architecture. While
accessible, these screens don't provide reliable information about database health or
status.

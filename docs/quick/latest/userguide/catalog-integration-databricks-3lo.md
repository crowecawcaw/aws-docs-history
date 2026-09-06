

# Setting up identity enforcement with Databricks 3LO
<a name="catalog-integration-databricks-3lo"></a>

Quick supports three-legged OAuth (3LO) with end-user identities for Databricks. When enabled, 3LO enforces per-user data permissions based on Databricks Unity Catalog access control lists (ACLs). Each end user sees only the data that their Databricks permissions allow.

**Important**  
Identity enforcement works only for DirectQuery datasets. If a dataset is switched to SPICE or has transformations applied, identity enforcement does not apply.

## Administrator setup: Client application configuration
<a name="catalog-integration-databricks-3lo-admin"></a>

The Quick account administrator must configure a client application before authors can create 3LO data sources. Complete the following steps:

1. In the Quick console, choose **Manage Account**. Under **Security**, choose **Manage OAuth Client Applications**.

1. Choose **Add OAuth client application** and provide the following information:
   + Config ID
   + OAuth client application name
   + Authentication type
   + Client ID
   + Client secret
   + Token endpoint URL
   + Authorization endpoint URL
   + OAuth scopes
   + VPC connection ARN (optional)
   + Data source type (select **DATABRICKS**)

1. Choose **Add** to save the client application.

## Author setup: Creating a 3LO data source
<a name="catalog-integration-databricks-3lo-author"></a>

After the administrator configures the client application, authors can create a Databricks data source with 3LO authentication.

1. Navigate to the **Create Data Source** page.

1. Select **Databricks**.

1. Choose **3LO** as the authentication method.

1. Enter the required connection information.

1. Enter your username (the email address associated with your Databricks account).

1. Select the option to enforce trusted identity enforcement (TIP). This ensures that permissions defined in Databricks, including table-level access and data filters, are enforced for end users.
**Important**  
You must select this option if end-user identities must be propagated. Without it, all users share the author's Databricks permissions.

1. Choose **Create data source**.

After the data source is created, use the standard Quick workflow or the agentic experience (**Explore Data**) to create datasets, topics, and dashboards.

## End-user experience: Enforcing data permissions
<a name="catalog-integration-databricks-3lo-enduser"></a>

To enforce per-user data permissions for dashboard consumers, complete the following steps:

1. The author shares both the data source and the dashboard with the end user.

1. The end user signs in to Quick and navigates to the **Data Source** page.

1. The end user enters their own Databricks credentials (their OAuth login) and saves.

1. When the end user accesses the dashboard, they see only the data that their Databricks permissions allow.

## Important considerations
<a name="catalog-integration-databricks-3lo-notes"></a>
+ Identity enforcement works only for DirectQuery datasets.
+ The agentic catalog experience (discover, create, inherit) works with both PAT and 3LO authentication. Identity enforcement through 3LO is optional and additive. It is not a prerequisite for the agentic flow.
+ If you do not opt for 3LO, you can use PAT and manually manage data permissions by using row-level security (RLS) and column-level security (CLS) rules in Quick.
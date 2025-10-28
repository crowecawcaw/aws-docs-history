# Configuring Service Catalog portfolios

in Jira

This section describes how to configure AWS Service Catalog portfolios within
Jira.

Once your account or accounts are set up and connectivity is
successful, use the **AWS Account** page to manage,
for each account, which groups can access each portfolio in each Region.
You can expand and collapse each Region and edit and add groups for each
portfolio. Only users in the designated groups have access to those
products. By default, no groups have access.

###### Note

At least one group must be associated to a Service Catalog portfolio for Jira
Service Management end users to request AWS products.

###### To provision products and portfolios

1. Choose **AWS Accounts**.
2. Choose **Manage** for the AWS account in
   which you want to configure portfolios.
3. Under **Portfolios**, expand the Region
   associated with the account. Portfolios display under each
   Region.
4. In the **Permission to request** column, choose
   **Add groups** for the portfolios that you want
   to make visible in Jira Service Management. Select the group you
   want to see and request Service Catalog products.

###### Note

Because the AWS Service Management Connector for Jira
Service Management allows Jira users to provision AWS products
in the portfolios their groups have access to, and to control
those provisioned products, users should maintain security in
their Jira accounts. 5. If products in this portfolio do not require approvals, choose
**Save**.

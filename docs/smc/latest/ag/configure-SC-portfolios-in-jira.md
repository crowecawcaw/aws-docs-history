# Configuring Service Catalog Portfolios in

Jira

This section describes how to configure AWS Service Catalog portfolios within
Jira.

**AWS product access**

Once your account or accounts are set up and connectivity is
successful, use the **AWS Account** page to manage, for
each account, which groups can access each portfolio in each Region. You
can expand and collapse each Region and edit and add groups for each
portfolio. Only internal customers and Jira agents in the designated
groups have access to those products. By default, no groups have access.

###### Note

At least one group must be associated to a Service Catalog portfolio for Jira
Service Management internal customers and Jira agents to request AWS
products.

###### To provision products and portfolios

1. Choose **AWS Accounts**.
2. Choose **Manage** for the AWS account in which
   you want to configure portfolios.
3. Under **Portfolios**, expand the Region
   associated with the account. Portfolios display under each Region.
4. In the **Permission to request** column, choose
   **Add groups** for the portfolios that you want to
   make visible in Jira Service Management. Select the group you want to
   see and request Service Catalog products.

###### Note

Because the AWS Service Management Connector for Jira Service
Management allows Jira internal customers and Jira agents to
provision AWS products in the portfolios their groups have access
to, and to control those provisioned products, internal customers
and Jira agents should maintain security in their Jira
accounts. 5. If products in this portfolio do not require approvals, choose
**Save**.

## Configuring Jira Service Management approvals

for products in Service Catalog Portfolios

The AWS Service Management Connector for Jira Service Management
enables administrators to configure approvals for products at the
portfolio level. All products in a portfolio that contain approval
permissions require approval, so AWS and Jira administrators might
need to collaborate on the Service Catalog portfolio structure.

###### To configure the approval process

1. Choose **AWS Accounts**.
2. Choose **Manage** on the AWS account for
   which you want to configure portfolio approvals.
3. In the **Permission to approve** column, choose
   **Add groups** for the portfolios that require
   product approvals.
4. Select **Require approval for
   provisioning**.
5. Under **Permission to approve**, choose
   **Add group**.
6. Choose **Save**.

###### Note

If a portfolio only has a group associated with
**Permissions to request**, products in the
portfolio immediately provision when you submit the product request.

## Viewing products and

budgets

The **Available Products** tab lists the products
in the portfolio and budgetary information on each. The
**Budgets** tab gives overall budgetary information
on the portfolio.

###### Note

Find details about additional configurations for the AWS Service Catalog
request form and Automated Tags in the next section Configuring
Connector Settings.

## Configuring Connector

Settings (Jira Project Enablement and Request Type)

In addition to configuring AWS accounts, the AWS Service
Management Connector contains AWS services and UI settings for
enabling and associating Jira projects and configuring integration
behavior.

###### Note

There is no project-account association for AWS Service Catalog.
Project-account visibility is determined by the permissions groups
that are granted permission to provision.

## Connector Features Enabled

by Default

###### To configure the default Connector features for specific AWS

services

For a new installation of Connector, Service Management Connector
enables the default project configuration for all Connector features
(AWS Service Catalog, AWS Systems Manager Incident Manager, and AWS Security Hub CSPM). If you are upgrading an
existing installation, Service Management Connector does not initially
enable new features.

1. In the left navigation menu, under **AWS Service
   Management**, select **Connector
   settings.**
2. At the top, under **Connector features enabled by
   default**, select each feature depending whether you want
   projects using the default configuration to be able to use them or
   not.
3. Choose **Save**.

## UI Settings

(AWS Service Catalog)

Configure the AWS Service Catalog product widget components to make them
viewable to internal customers and Jira agents.

To address the varying personas of internal customers and Jira
agents requesting AWS products, the Connector for Jira Service
Management includes an add-on app setting to enable or disable
components of the AWS product widget. By default, we enable AWS
product components.

###### To modify the AWS product view

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**,
   and then navigate to **Connector settings**.
3. In the **UI settings** (Service
   Catalog) section, deselect any AWS product component such
   as:
   1. Allow the product name to be edited. (If unchecked, we
      provide an autogenerated name the user cannot edit.)
   2. Allows internal customers and Jira agents to select a launch
      option. (If unchecked, we select the default launch option and
      hide it.)
   3. Allows internal customers and Jira agents to select a
      product version. (If unchecked, we select the default product
      version and hide it.)
   4. Allows internal customers and Jira agents to add or edit
      tags. (If unchecked, we select the default values for tag
      options and hide it.)
   5. Allows internal customers and Jira agents to create a plan
      for creation or update of a provisioned product. (If unchecked,
      we hide the plans section.)

4. Choose **Save**.

## Configuring AWS

TagOptions for Provisioned Products

The AWS Service Management Connector enables Jira administrators
to add tags (metadata) to provisioned products globally across the
connector application, or granularly at the portfolio level. These tags
are not visible to internal customers and Jira agents.

Two tag types are available

- Generic tags where the administrator can enter the
  **Key** and **Value**.
- Jira issues metadata tags where the administrator can enter the
  syntax for the **Key** and
  **Value** in the table below.

###### Note

Generic tags from administrators are not visible to internal
customers or Jira agents during provisioning, but are available in the
provisioned product in Service Catalog.

| Key                 | Value           |
| ------------------- | --------------- |
| Requester name      | ${OPENED_BY}    |
| Requester user name | ${USERNAME}     |
| Issue ID            | ${ISSUE_ID}     |
| Project name        | ${PROJECT_NAME} |
| Project code        | ${PROJECT_CODE} |

###### To add TagOptions to Service Catalog integration in Jira Service

Management

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**,
   and then navigate to **Automated Tags**.
3. Enter the **Key** and
   **Value** fields.
4. Select a portfolio option.
   1. **Glocal** if the tag should be available
      in all synced portfolios, or
   2. **Portfolio** to restrict tags to only the
      specified portfolio.

5. Choose **Add**.

## Projects Enabled for the

Connector

The AWS Service Management Connector for Jira Service Management
must be associated with one or more Jira projects and Jira Service
Management request types. You can configure which features are enabled for
each Jira project.

**Configure Jira projects for
AWS Service Catalog,AWS Systems Manager Incident Manager, AWS Security Hub CSPM, Support, AWS Systems Manager Automation,
AWS Systems Manager OpsCenter and AWS Health**

###### To configure the Jira projects for AWS Service Catalog, AWS Systems Manager Incident Manager,

AWS Security Hub CSPM, Support, and AWS Systems Manager Automation

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**,
   and then navigate to **Connector settings**.
3. Under **Projects enabled for
   Connector**, you must enable at least one Jira project. You
   can [create a new Jira Service Management project](https://support.atlassian.com/jira-service-management-cloud/docs/set-up-your-first-jira-service-management-project/ "https://support.atlassian.com/jira-service-management-cloud/docs/set-up-your-first-jira-service-management-project/") or add an
   existing one. Only Jira internal customers and Jira agents with access
   to the associated project can access the Connector. When you apply
   this update, the Connector adds the necessary issue types and other
   Jira items for AWS Service Catalog products to be available in those projects.
   You can return to this screen and add or remove projects at any time.
4. Projects initially take the default configuration for which
   Connector features are enabled. Choose **Edit** in a project row to change the configuration for
   individual projects. We permit projects to use more features than the
   default.
5. Choose **Save.**

###### Note

For internal customers and Jira agents to be able to request
AWS Service Catalog products, one or more projects must be enabled. Internal
customers and Jira agents must have Jira permissions to create
issues in the Jira project and Permission to Request in the Jira
settings for the AWS Account for at least one portfolio with
products.

###### AWS Security Hub CSPM configuration

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**,
   and then navigate to **Connector settings**.
3. Under **Security Hub CSPM configuration**, choose
   **CRITICAL**, **HIGH**,
   **MEDIUM**, **LOW**, or
   **INFORMATIONAL** to configure the findings synched
   to Jira Service Management.

**SQS queue name** is the queue from which Security Hub CSPM
findings are synched. The default value is
`AwsSmcJsmCloudForgeSecurityHubQueue`. The configured
queue is available in all AWS accounts and regions and where you
have configured the integration. 4. (optional) Enable **Recreate Jira Issues** to
indicate if Jira Issues will be created for updated findings where the
original Jira Issue deleted. 5. Assign onboarded AWS accounts to Jira projects. 6. Choose **Save**.

###### AWS Systems Manager Incident Manager configuration

1. Configure incident resolution behavior between AWS and Jira
   Service Management. The default value is
   **Bidirectional**.
2. Assign onboarded AWS accounts to Jira projects.
3. Choose **Save**.

###### Support configuraiton

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**, and then navigate to
   **Connector settings**.
3. In the **Support configuration** pane, choose
   **SQS gueue name** from where you want to sync the
   Support case. The default value is
   **AwsSmcJsmCloudForgeSupportQueue**. The queue must
   be available in `us-east-1` for commercial and
   `us-gov-west-1` for GovCloud accounts.
4. Assign onboarded AWS accounts to Jira projects.
5. Choose **Save**.

###### AWS Systems Manager Automation configuraiton

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**, and then navigate to
   **Connector settings**.
3. In the **AWS Systems Manager Automation configuration**
   pane, select the **Jira groups that can request
   automation** execution.
4. Choose **Save**.

###### AWS Systems Manager OpsCenter configuration

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**, and then navigate to
   **Connector settings**.
3. Under **Systems Manager OpsCenter configuration**, assign
   onboarded AWS accounts to Jira projects.
4. Choose **Save**.

###### AWS Health configuration

1. Navigate to the **Settings** menu, and then
   choose **Apps**.
2. Choose **AWS Service Management Connector**, and then navigate to
   **Connector settings**.
3. Under **AWS Health
   configuration**, provide the SQS queue name from where you
   want to sync health events. The default name is **AwsSmcJsmCloudForgeHealthQueue**.
4. Choose default severity levels for Jira issues for health event
   types (**Issue**, **Account Notification**, **Scheduled
   Change**).
5. Assign onboarded AWS accounts to Jira projects.
6. Choose **Save**.

# ServiceNow permissions for administrators of

the Connector scoped app

The AWS Service Management scoped app has two ServiceNow roles that enable
access to configure the application. This feature enables system admins to grant one
or more user's privileges to administer the application, without having to open full
sysadmin access to them. System admins can assign these roles to either individual
users or to one administrator user.

###### To set up Connector application administrator privileges

1. Enter `Users` in the navigator and select
   **System Security – Users**.
2. Choose a user to grant one or both previous roles (such as admin). You can
   also [Administer the Now Platform](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/general/concept/intro-now-platform-landing.html "https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/general/concept/intro-now-platform-landing.html").
3. Choose **Edit** on the **Roles** tab of the form.
4. Filter the collection of roles by the prefix
   `x_126749_aws_sc`.
5. Choose one or more of the following and add them to the user: **x_126749_aws_sc_account_admin**, **x_126749_aws_sc_portfolio_manager**, **x_126749\_ aws_sc.appregistry_manager,**
   **x_126749\_ aws_sc.automation_manager**,
   **x_126749_aws_sc.finding_manager**,
   **x_126749_aws_sc.opscenter_manager**,
   **x_126749_aws_sc.support_case_manager** ,
   **x_126749_aws_sc.change_manager_manager**,
   **x_126749_aws_sc.productsearchaccess**,
   **x_126749_aws_sc.cloudtrail_event_user**,
   and **x_126749_aws_sc.health_dashboard_viewer.**
6. Choose **Save**.

###### To add Service Catalog to ServiceNow Service Catalog categories

1. Choose **Self Service | Service Catalog** and select the
   **Add content** icon in the upper right.
2. Choose the **AWS Service Catalog Product** entry. To add it to your
   catalog home page, choose the first **Add Here** link on
   the second row of the selection panel at the bottom of the page.

###### To add AWS Systems Manager automation documents (runbook) to ServiceNow Service Catalog

categories

1. Choose **Self Service | Service Catalog** and select the
   **Add content** icon in the upper right.
2. Select the **AWS Systems Manager** entry. To add it to your catalog
   home page, choose the first **Add Here** link on the second
   row of the selection panel at the bottom of the page.

###### Note

This Connector release displays all AWS Systems Manager documents in the AWS account
that has AWS Systems Manager selected.

System administrators can deactivate AWS Systems Manager document requests. To deactivate
requests, choose **AWS Systems Manager**, **Automation Documents**, and deselect **Active**.
After deactivation of the document, you no longer see the document in the ServiceNow
Service Catalog.

The Connector creates closed change requests on post provision actions (such as
update, terminate and self-service) for AWS Service Catalog products visible in ServiceNow.

To achieve a closed change request from post provisioned actions, add a change
request type and configure the `sys_id` for the group assigned to the
closed change records in the Connector AWS Service Catalog system properties.

###### To add a change request type for closed change request from post provisioned

actions

1. If you upgrade from a previous version of the AWS Service Management
   scoped app, you must remove the **AWS Product
   Termination** change request type before you create a new
   change request type.
2. You must add a new change request type called **AWS Provisioned
   Product Event** for the scoped application to trigger an
   automated change request in Change Management. For more information, see
   [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html "https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html").
3. Open an existing change request.
4. Open (right-click) the context menu for **Type** and then
   choose **Show Choice List**.
5. Choose **New** and complete these fields:
   - **Table**: `Change
Request`
   - **Label**: `AWS Provisioned Product
Event`
   - **Value**:
     `AWSProvisionedProductEvent`
   - **Sequence**: pick the next unused value

6. Submit the form.

###### To add a change request type for executing AWS Systems Manager Change Manager change

templates

You must add a new change request type called `AWSChangeRequest`
for the scoped application to view and execute AWS Change Manager change
templates in ServiceNow Change Management. For more information, see [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html "https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html").

1. Open an existing change request.
2. Open (right-click) the context menu for **Type** and then choose **Show Choice
   List**.
3. Choose **New** and complete these
   ﬁelds:
   - Table: `Change Request`
   - Label: `AWS Change Request`
   - Value: `AWSChangeRequest`
   - Sequence: pick the next unused value

4. Submit the form.

###### To enable AWS Systems Manager Change Manager integration Change models

AWS Systems Manager Change Manager integration in ServiceNow requires Change Model
feature in ServiceNow.

1. In the navigator, enter `sys_properties.list`.
2. Enter `*change_model` in the **Search** panel to view and edit the properties.
3. Review the available settings and recommendations in the table
   below.

###### Note

For more information on Change model system properties, see [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html "https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html").

| Available settings                                          | Desired value |
| ----------------------------------------------------------- | ------------- |
| `com.snc.change_management.change_model.hide`               | false         |
| `com.snc.change_management.change_model.type_compatibility` | true          |

| ServiceNow Permissions Recap              | ServiceNow Persona                  | Scoped App Permissions                                                              | ServiceNow Permission Type                               | Description |
| ----------------------------------------- | ----------------------------------- | ----------------------------------------------------------------------------------- | -------------------------------------------------------- | ----------- |
| Admin                                     | `x_126749_aws_sc_portfolio_manager` | Role (scoped app)                                                                   | Manage AWS Service Catalog portfolios and product access |
| `x_126749_aws_sc_account_admin`           | Role (scoped app)                   | Onboard and manage AWS accounts                                                     |
| `x_126749_ aws_sc.appregistry_manager`    | Role (scoped app)                   | View AppRegistry applications and attribute groups                                  |
| `x_126749_aws_sc.automation_manager`      | Role (scoped app)                   | Manage Automation Documents and view Automation<br>executions                       |
| `x_126749_aws_sc.finding_manager`         | Role (scoped app)                   | View AWS Security Hub CSPM findings                                                 |
| `x_126749_aws_sc.opscenter_manager`       | Role (scoped app)                   | Default access control for OpsItem integration.                                     |
| `x_126749_aws_sc.change_manager_manager`  | Role (scoped app)                   | Manage AWS Systems Manager Change Manager change templates                          |
| `x_126749_aws_sc.support_case_manager`    | Role (scoped app)                   | Manage Support services and categories                                              |
| `x_126749_aws_sc.productsearchaccess`     | Role (scoped app)                   | End user role for searching AWS Service Catalog products using the search<br>widget |
| `x_126749_aws_sc.cloudtrail_event_user`   | Role (scoped app)                   | Default ACL for CloudTrail events on AWS Systems Manager Change<br>Manager          |
| `x_126749_aws_sc.health_dashboard_viewer` | Role (scoped app)                   | View AWS Health dashboard                                                           |
| End User (i.e., Abel Tuter)               | `Order_AWS_Products`                | Group                                                                               |                                                          |

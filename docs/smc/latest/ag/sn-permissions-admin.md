

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# ServiceNow permissions for administrators of the Connector scoped app
<a name="sn-permissions-admin"></a>

The AWS Service Management scoped app has two ServiceNow roles that enable access to configure the application. This feature enables system admins to grant one or more user's privileges to administer the application, without having to open full sysadmin access to them. System admins can assign these roles to either individual users or to one administrator user.

**To set up Connector application administrator privileges**

1. Enter **Users** in the navigator and select **System Security – Users**. 

1. Choose a user to grant one or both previous roles (such as admin). You can also [Administer the Now Platform](https://docs.servicenow.com/bundle/washingtondc-platform-administration/page/administer/general/concept/intro-now-platform-landing.html). 

1.  Choose **Edit** on the **Roles** tab of the form. 

1.  Filter the collection of roles by the prefix **x\_126749\_aws\_sc**. 

1. Choose one or more of the following and add them to the user: ** x\_126749\_aws\_sc\_account\_admin**, **x\_126749\_aws\_sc\_portfolio\_manager**,** x\_126749\_ aws\_sc.appregistry\_manager,** **x\_126749\_ aws\_sc.automation\_manager**, **x\_126749\_aws\_sc.finding\_manager**, **x\_126749\_aws\_sc.opscenter\_manager**, **x\_126749\_aws\_sc.support\_case\_manager **, **x\_126749\_aws\_sc.change\_manager\_manager**, **x\_126749\_aws\_sc.productsearchaccess**, **x\_126749\_aws\_sc.cloudtrail\_event\_user**, and **x\_126749\_aws\_sc.health\_dashboard\_viewer.**

1.  Choose **Save**. 

**To add Service Catalog to ServiceNow Service Catalog categories**

1.  Choose **Self Service \| Service Catalog** and select the **Add content** icon in the upper right. 

1. Choose the **AWS Service Catalog Product** entry. To add it to your catalog home page, choose the first **Add Here** link on the second row of the selection panel at the bottom of the page. 

**To add AWS Systems Manager automation documents (runbook) to ServiceNow Service Catalog categories**

1. Choose **Self Service \| Service Catalog** and select the **Add content** icon in the upper right.

1. Select the **AWS Systems Manager** entry. To add it to your catalog home page, choose the first **Add Here** link on the second row of the selection panel at the bottom of the page.

**Note**  
 This Connector release displays all AWS Systems Manager documents in the AWS account that has AWS Systems Manager selected. 

System administrators can deactivate AWS Systems Manager document requests. To deactivate requests, choose **AWS Systems Manager**, **Automation Documents**, and deselect **Active**. After deactivation of the document, you no longer see the document in the ServiceNow Service Catalog. 

The Connector creates closed change requests on post provision actions (such as update, terminate and self-service) for AWS Service Catalog products visible in ServiceNow. 

To achieve a closed change request from post provisioned actions, add a change request type and configure the `sys_id` for the group assigned to the closed change records in the Connector AWS Service Catalog system properties.

**To add a change request type for closed change request from post provisioned actions**

1. If you upgrade from a previous version of the AWS Service Management scoped app, you must remove the **AWS Product Termination** change request type before you create a new change request type. 

1.  You must add a new change request type called **AWS Provisioned Product Event** for the scoped application to trigger an automated change request in Change Management. For more information, see [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html). 

1. Open an existing change request. 

1. Open (right-click) the context menu for **Type** and then choose **Show Choice List**. 

1.  Choose **New** and complete these fields: 
   + **Table**: **Change Request**
   + **Label**: **AWS Provisioned Product Event**
   + **Value**: **AWSProvisionedProductEvent**
   + **Sequence**: pick the next unused value

1. Submit the form.

**To add a change request type for executing AWS Systems Manager Change Manager change templates**

You must add a new change request type called `AWSChangeRequest` for the scoped application to view and execute AWS Change Manager change templates in ServiceNow Change Management. For more information, see [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html).

1. Open an existing change request.

1. Open (right-click) the context menu for **Type** and then choose **Show Choice List**.

1. Choose **New** and complete these ﬁelds:
   + Table: **Change Request**
   + Label: **AWS Change Request**
   + Value: **AWSChangeRequest**
   + Sequence: pick the next unused value

1. Submit the form.

**To enable AWS Systems Manager Change Manager integration Change models**

AWS Systems Manager Change Manager integration in ServiceNow requires Change Model feature in ServiceNow.

1. In the navigator, enter **sys\_properties.list**.

1. Enter **\*change\_model** in the **Search** panel to view and edit the properties. 

1. Review the available settings and recommendations in the table below.

**Note**  
For more information on Change model system properties, see [IT Service Management](https://docs.servicenow.com/bundle/washingtondc-it-service-management/page/product/it-service-management/reference/r_ITServiceManagement.html).


| Available settings | Desired value | 
| --- | --- | 
|  com.snc.change\_management.change\_model.hide | false | 
| com.snc.change\_management.change\_model.type\_compatibility | true | 


**ServiceNow Permissions Recap**  


- **Admin**
  - **Scoped App Permissions:**  x\_126749\_aws\_sc\_portfolio\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Manage AWS Service Catalog portfolios and product access 
  - **Scoped App Permissions:**  x\_126749\_aws\_sc\_account\_admin  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Onboard and manage AWS accounts 
  - **Scoped App Permissions:** x\_126749\_ aws\_sc.appregistry\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** View AppRegistry applications and attribute groups
  - **Scoped App Permissions:** x\_126749\_aws\_sc.automation\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Manage Automation Documents and view Automation executions
  - **Scoped App Permissions:** x\_126749\_aws\_sc.finding\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** View AWS Security Hub CSPM findings
  - **Scoped App Permissions:** x\_126749\_aws\_sc.opscenter\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Default access control for OpsItem integration.
  - **Scoped App Permissions:** x\_126749\_aws\_sc.change\_manager\_manager / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Manage AWS Systems Manager Change Manager change templates
  - **Scoped App Permissions:** x\_126749\_aws\_sc.support\_case\_manager  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Manage Support services and categories
  - **Scoped App Permissions:**  x\_126749\_aws\_sc.productsearchaccess  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** End user role for searching AWS Service Catalog products using the search widget
  - **Scoped App Permissions:** x\_126749\_aws\_sc.cloudtrail\_event\_user  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** Default ACL for CloudTrail events on AWS Systems Manager Change Manager
  - **Scoped App Permissions:** x\_126749\_aws\_sc.health\_dashboard\_viewer  / **ServiceNow Permission Type:** Role (scoped app) / **Description:** View AWS Health dashboard

- **End User (i.e., Abel Tuter) **
  - **Scoped App Permissions:** Order\_AWS\_Products
  - **ServiceNow Permission Type:** Group
  - **Description:** 


# Validating AWS Service Catalog integration in

Jira Service Management Cloud

This section describes how you can use service integration features to validate
AWS Service Management Connector for Jira Service Management Cloud installation.

###### **To order a Service Catalog product using the Jira Customer Portal**

###### Note

You can only order a Service Catalog product using the Jira Customer Portal if you have enabled
Jira projects for the connector and added the Service Catalog request form to the portal. For more information about
the Service Catalog request form, review [Enable the AWS Service Catalog Request Type in Jira Customer Portal](customer-portal.md "customer-portal.md").

1. Log in to your Jira Service Management Customer Portal.
2. Select the portal group that corresponds with the Service Catalog request form.
3. Select the product you want to provision.
4. Enter the product request details, including the **product reference name**,
   **parameters**, and **tags**.
5. Choose **Send** to submit the JSM request and provision the Service Catalog product.
   When the product is ready to provision, users receive a notification that the product
   is launching.

###### **To view provisioned products using the Jira Customer Portal**

1. Log in to your Jira Service Management Customer Portal.
2. Choose **Requests** at the top right corner.
3. Select the desired provisioned product to open the issue.
4. Review the provisioned product details, including the **Status** of the
   product request, **Product events**, **Activities**,
   and any available **Self-service actions**.

###### To perform post-provisioning actions

1. Log in to your Jira Service Management Customer Portal.
2. Choose **Requests** at the top right corner.
3. Select a **service action** from the Self-service actions
   list, and then choose **Execute**.
   When the product is in the `Available` status, internal customers and Jira agents can request
   post-provision operations, including **Request update** and **Request termination**
   from the **Actions** menu at the top right corner of the Issues page.

###### **To order a Service Catalog product using the Jira Agent view**

1. Log in to the Jira Service Management agent view as the internal customer or Jira agent.
2. Open the Jira project and navigate to apps **AWS Service Catalog - Order Product**.
3. Select a product to provision.
4. Fill in the product request details, including the product reference name, parameters, and tags.
5. Choose **Order** to submit the Jira Service Management request and provision the AWS Service Catalog product
6. After the request processes, a message appears indicating that your request was created.
   When the product is ready to provision, the internal customers or Jira agents receives a notification that the product is launching.

###### **To view provisioned products using the Jira Agent view**

1. Log in to your Jira Service Management Agent View as the internal customer or Jira agent.
2. Use [Jira filters](https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/ "https://support.atlassian.com/jira-service-management-cloud/docs/save-your-search-as-a-filter/") to show only issues with the Issue Type **AWS Service Catalog Request**.
3. Open a Jira issue.
4. Choose the **AWS Service Catalog** panel.
5. Review the AWS provisioned product details, including the status of the product request,
   product events, activities, and available Self-Service Actions.
6. If Self-Service Actions are available, you can select a service action from the list, and then
   choose **Execute**.
7. After the product is in the `Available` status, internal customers and Jira agents can
   request post-provision operations including **Request update** and **Request termination**
   from the **Actions** menu at the top right corner of the issue page.

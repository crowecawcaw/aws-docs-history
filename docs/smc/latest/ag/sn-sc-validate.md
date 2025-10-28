# Using service integration features to validate AWS Service Catalog integration in

ServiceNow

This section describes how you can use service integration features to validate
AWS Service Management Connector for ServiceNow installation.

###### **To order a Service Catalog product**

1. Log in to your ServiceNow instance as the end user (for this example,
   Abel Tuter).
2. Enter `Service Catalog` in the navigation filter
   and choose **Service Catalog**.
3. Choose the **AWS Service Catalog S3 Storage** product
   to provision.
4. Enter the product request details, including product name, parameters,
   and tags.
5. Choose **Order Now** to submit the ServiceNow
   request and provision the Service Catalog product.

After approximately one minute, you receive an order status
acknowledging the submission.
**To view provisioned products**

End users can view products in two places on the ServiceNow portal: **request items (Requests)** or **My
AWS Service Catalog Products** widgets.

###### \*\*To view products in Service Portal

Requests\*\*

1. Choose **Requests** in the home page navigation
   bar.
2. Choose the request item with the Service Catalog product and request the item
   number.

###### Note

AWS product events and outputs update the request item. When you
terminate the AWS product, the ServiceNow request
item enters a state of **Closed Complete**.

###### \*\*To view products in the My AWS

Products widget Service Portal Requests\*\*

1. In the **My AWS Products**
   widget, choose the AWS Select product name on the request
   form.
2. View **Status and Product Events**.
3. If you want to perform post-provisioned operational actions, choose
   **Request Update**, **Request Self-Service
   Action**, or **Terminate**.

###### **To override workflows on Portfolios**

1. Log in to your ServiceNow fulfiller view (standard user interface).
2. Enter `AWS Service Catalog` in the navigation ﬁlter and choose **Portfolios**.
3. Choose **Display Name** to open a portfolio.
4. Select the required workflow from the search to set **Workflow
   Override.**
5. Choose **Update**.

###### **To view AppRegistry applications**

1. Log in to your ServiceNow fulfiller view (standard user interface).
2. Enter `AWS Service Catalog` in the navigation
   ﬁlter and choose **AppRegistry
   Applications**.
3. Choose the AppRegistry application.

###### **To view AppRegistry attribute groups**

1. Log in to your ServiceNow fulfiller view (standard user interface).
2. Enter `AWS Service Catalog` in the navigation
   ﬁlter and choose **AppRegistry Attribute
   Groups**.
3. Choose the AppRegistry attribute group.

## Video: Integrate AWS Products into Your ServiceNow Portal with the AWS

Service Management Connector

This video (18:33) describes how to integrate AWS products in your ServiceNow
Portal with the AWS Service Management Connector.

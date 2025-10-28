# Granting access to AWS Service Catalog

portfolios

This release of the Connector does not require you to link AWS identities to
ServiceNow roles. To grant access to Service Catalog products in ServiceNow, you must establish
a link between the Service Catalog portfolios and the ServiceNow group (for example,
**Order_AWS_Products** from an earlier installation
example).

###### To grant access to Service Catalog portfolios in ServiceNow

1. In the AWS Service Management scoped app, choose **Service Catalog**, then the **Portfolios**
   module.
2. Choose the desired Portfolio ARN. You can double-click the Service Catalog portfolio
   name.
3. Choose the **Allowed Groups** tab.
4. Choose **New** and enter the **Group**
   named `Order_AWS_Products`.
5. Choose **Submit**.

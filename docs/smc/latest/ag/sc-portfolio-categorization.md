# Activate AWS Service Catalog portfolio categorization

in ServiceNow Service Portal

AWS Service Management Connector can display portfolios with an additional
categorization of AWS Account and Region names in the ServiceNow Service Portal. This allows
you to identify the account and region a portfolio and its product belongs to if the end user
has access to multiple portfolios with the same name.

###### To activate Portfolio categorization in ServiceNow Portal

1. Log in as system administrator.
2. In the **System Properties** menu, choose **AWS Service Catalog**.
3. In the option **If set to Account/Region/Portfolio, the hierarchy of categories created
   will be set to portfolio, region and account. If set to Portfolio, only portfolio category will
   be created**, choose **Account/Region/Portfolio**.
4. In the **System Definition** menu, choose **Scheduled Jobs**.

###### To activate Portfolio categorization for existing users

1. In the **System Definition** menu, choose **Scheduled Jobs**.
2. Select the scheduled job, and then choose **Synchronize AWS Service Catalog**.
3. In the **Active** field, choose **False**, and then
   choose **Update**.
4. In the **System Definition** menu, choose **Fix Script**.
5. Select the fix script, and then choose **AWS Service Catalog Category Delete**, and
   then choose **Run Fix script**.
6. Follow the steps in _To activate Portfolio categorization in ServiceNow
   Portal_ above.

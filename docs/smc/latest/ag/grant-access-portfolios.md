

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Granting access to AWS Service Catalog portfolios
<a name="grant-access-portfolios"></a>

This release of the Connector does not require you to link AWS identities to ServiceNow roles. To grant access to Service Catalog products in ServiceNow, you must establish a link between the Service Catalog portfolios and the ServiceNow group (for example, **Order\_AWS\_Products** from an earlier installation example).

**To grant access to Service Catalog portfolios in ServiceNow**

1. In the AWS Service Management scoped app, choose **Service Catalog**, then the **Portfolios** module. 

1. Choose the desired Portfolio ARN. You can double-click the Service Catalog portfolio name. 

1. Choose the **Allowed Groups** tab.

1.  Choose **New** and enter the **Group** named **Order\_AWS\_Products**. 

1.  Choose **Submit**. 
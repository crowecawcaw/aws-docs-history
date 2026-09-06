

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Activate AWS Service Catalog portfolio categorization in ServiceNow Service Portal
<a name="sc-portfolio-categorization"></a>

AWS Service Management Connector can display portfolios with an additional categorization of AWS Account and Region names in the ServiceNow Service Portal. This allows you to identify the account and region a portfolio and its product belongs to if the end user has access to multiple portfolios with the same name. 

**To activate Portfolio categorization in ServiceNow Portal**

1. Log in as system administrator.

1. In the **System Properties** menu, choose **AWS Service Catalog**. 

1. In the option **If set to Account/Region/Portfolio, the hierarchy of categories created will be set to portfolio, region and account. If set to Portfolio, only portfolio category will be created**, choose **Account/Region/Portfolio**. 

1. In the **System Definition** menu, choose **Scheduled Jobs**. 

**To activate Portfolio categorization for existing users**

1. In the **System Definition** menu, choose **Scheduled Jobs**. 

1. Select the scheduled job, and then choose **Synchronize AWS Service Catalog**. 

1. In the **Active** field, choose **False**, and then choose **Update**. 

1. In the **System Definition** menu, choose **Fix Script**. 

1. Select the fix script, and then choose **AWS Service Catalog Category Delete**, and then choose **Run Fix script**. 

1. Follow the steps in *To activate Portfolio categorization in ServiceNow Portal* above. 
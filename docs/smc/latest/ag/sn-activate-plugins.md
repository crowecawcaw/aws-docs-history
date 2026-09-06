

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Activating ServiceNow plugins
<a name="sn-activate-plugins"></a>

AWS Service Management Connector uses three ServiceNow plugins to provide useful components to the integration features:
+ User Criteria Scoped API (for AWS Service Catalog integration)
+ Discovery and Service Mapping Patterns (for AWS Config integration)
+ Change Management – Change Model Foundation Data (for AWS Systems Manager Change Manager integration)

**To activate the User Criteria Scoped API plugin**

1.  In your ServiceNow dashboard, enter **plugins** into the navigation panel in the upper left. 

1.  When the **System Plugins** page populates, next to the **Name** dropdown, search for **User Criteria**. 

1.  Choose **User Criteria Scoped API** and then choose **Activate**. 

**To activate the Discovery and Service Mapping Patterns plugin**

1. In your ServiceNow dashboard, enter **plugins** into the navigation panel in the upper left.

1.  When the **System Plugins** page populates, next to the **Name** dropdown, search for **Discovery**. 

1.  Choose **Discovery and Service Mapping Patterns** and then choose **Activate**. 

**Note**  
This plugin is free and aligns to the CMDB tables outside of ServiceNow’s family release CMDB updates. 

**To activate the Change Management – Change Model Foundation Data plugin**

1. In your ServiceNow dashboard, enter **plugins** in the navigation panel in the upper left.

1. When the System Plugins page populates, next to the **Name** dropdown, search for **Change Management**.

1. Choose **Change Management - Change Model Foundation Data** and then choose **Activate**.
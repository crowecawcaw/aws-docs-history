

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring the AWS Service Catalog product widget components and assignment group for closed change records
<a name="configure-sc-widget"></a>

To address the varying personas of end users requesting AWS products, the Connector for ServiceNow includes a scoped app setting to enable or disable components of the AWS product widget. By default, all AWS product components are active. 

**To modify the AWS product view**

1.  In the navigator, enter **System Properties** and select **Service Catalog**. 
**Note**  
Make sure you are in the AWS Service Management Connector scoped application mode. 

1.  Deselect any AWS product component to enable: 
   +  Editing of the Service Catalog product name. 
   +  Selection of launch options for Service Catalog Products. (This component is only visible if the AWS product has more than one launch path.) 
   +  Selection of product versions for Service Catalog. (This component is only visible if the AWS product has more than one product version.) 
   +  Tags for Service Catalog products. 
   +  Plans (ChangeSet) creation for product. (If set to false the plan section is not visible.) 

1.  Choose **Save**. 

The AWS Service Catalog system properties also include a section that identifies an assignment group. This group associates with closed change records from post provision actions of products (such as terminate, update, or self-service actions). 

**To associate the assignment group for change records from AWS Service Catalog post provision actions**

1. In the navigator, enter **System Properties** and choose **AWS Service Catalog**. Make sure you are in the AWS Service Management Connector scoped application mode.

1. Choose the section **Set the ‘assignment group’ sys\_id or name that the connector will use when creating change requests**. 

1. Enter the assignment **group sys\_id**. 

   If you need to find the `group sys_id`, enter **System Security** in the left navigator.

1. Choose **Groups** module.

1. Search for the **Group** name.

1. Choose the group that you want to associate to close changed records and choose **Copy sys\_id**. You are now able to paste the copied `sys_id` into the AWS Service Catalog Properties for the Connector under **Set the ‘assignment group’ sys\_id or name that the connector will use when creating change requests**.

   If the `sys_id` is blank, the change record sends a message that no assignment group exists for the record, which causes change requests created from the Connector to be in an open state. 
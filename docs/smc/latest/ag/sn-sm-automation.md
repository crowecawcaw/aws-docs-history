

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Integrating AWS Systems Manager Automation in ServiceNow
<a name="sn-sm-automation"></a>

To allow the Connector to execute Automation Documents, you must ensure that the Connector Sync and End user has the permissions required to sync and execute Automation Documents. 

For more information, see [Setting up Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html).

This table describes the available settings to configure Support integration system properties.


| Available settings | Description | 
| --- | --- | 
| Name of the Systems Manager category to assign to Automation Documents from AWS Systems Manager | The setting allows the Automation Documents to be created under the specified category.<br />By default, the category sets to AWS Systems Manager Automation. | 
| Name of a workflow that starts the execution of an Automation Document from AWS Systems Manager | The setting allows you to use custom workflow with the AWS Systems Manager Automation integration. | 
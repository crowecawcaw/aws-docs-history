

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring ServiceNow for AWS Systems Manager OpsCenter
<a name="sn-opscenter-integ"></a>

This section shows you how to integrate AWS Systems Manager OpsCenter in ServiceNow.

**To configure the AWS Systems Manager OpsCenter integration system properties**

1. In the navigator, enter **AWS Service Management**.

1. Choose **System Properties**, then **AWS Systems Manager - OpsCenter**. 

1. Review the available settings and recommendations in the table below.


<table>
<thead>
  <tr><th>Available settings </th><th>Description </th></tr>
</thead>
<tbody>
  <tr><td>Synchronizing a new OpsItem with a severity 1</td><td><b>Do Nothing</b>. This action only imports selected OpsItems for the scoped app. Users with scoped app permissions can view and choose to create an Incident or Problem. <br /><b>Create Incident</b>. This action automatically creates Incidents from OpsItems and syncs updates in ServiceNow to AWS Systems Manager - OpsCenter.<br /><b>Default value</b>: Create Incident</td></tr>
  <tr><td>Synchronizing a new OpsItem with a severity 2</td><td><b>Do Nothing</b>. This action only imports selected OpsItems for the scoped app. Users with scoped app permissions can view and choose to create Incident or Problem. <br /><b>Create Incident</b>. This action automatically creates Incidents from OpsItems and syncs updates in ServiceNow to AWS Systems Manager - OpsCenter.<br /><b>Default value</b>: Create Incident</td></tr>
  <tr><td>Synchronizing a new OpsItem with a severity 3</td><td><b>Do Nothing</b>. This action only imports selected OpsItems for the scoped app. Users with scoped app permissions can view and choose to create Incident or Problem. <br /><b>Create Incident</b>. This action automatically creates Incidents from OpsItems and syncs updates in ServiceNow to AWS Systems Manager - OpsCenter.<br /><b>Default value</b>: Do Nothing</td></tr>
  <tr><td>Synchronizing a new OpsItem with a severity 4</td><td><b>Do Nothing</b>. This action only imports selected OpsItems for the scoped app. Users with scoped app permissions can view and choose to create Incident or Problem. <br /><b>Create Incident</b>. This action automatically creates Incidents based on OpsItems and syncs updates in ServiceNow to AWS Systems Manager - OpsCenter.<br /><b>Default value</b>: Do Nothing</td></tr>
  <tr><td>Assignment Group (SYS_ID) for created Incidents</td><td>ServiceNow Incidents from AWS OpsItems need assignment group.<br /><b>To associate the assignment group for ServiceNow Incidents from AWS OpsItems </b><br />1. Choose the section <b>Set the assignment group sys_id</b> or name that the Connector uses when creating Incidents. <br />2. Enter the Assignment group <code>sys_id</code>. <br />If you need to find the group <code>sys_id</code>, enter <b>System Security</b> in the left navigator. <br />3. Choose the <b>Groups</b> module and search for the Group name. <br />5. Choose the group to associate to ServiceNow Incidents generated from AWS OpsItems and choose <b>Copy sys_id</b>. You can now paste the copied <code>sys_id </code>into AWS Systems Manager – OpsCenter System Properties.</td></tr>
</tbody>
</table>

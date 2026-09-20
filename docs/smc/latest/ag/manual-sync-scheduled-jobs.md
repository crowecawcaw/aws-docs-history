

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Manually syncing scheduled jobs
<a name="manual-sync-scheduled-jobs"></a>

The Connector for ServiceNow includes nine sync jobs related to AWS services integrations. During the initial setup, manually execute the sync job for your AWS service integration instead of waiting for Scheduled Jobs to run.

**To sync AWS service integrations or accounts manually**

1.  Log in as system administrator. 

1.  Find **Scheduled Jobs** in the navigator panel. 

1.  Search the following AWS Service Management Connector scheduled jobs (including default sync intervals) in the table below:


<table>
<thead>
  <tr><th>AWS Service Management Scheduled Job Name</th><th>Brief description</th><th>Default Sync Interval</th></tr>
</thead>
<tbody>
  <tr><td>Sync all Automation Execution</td><td>Syncs execution of AWS Systems Manager Automation runbooks (documents)</td><td>5 minutes</td></tr>
  <tr><td>Sync all provisioned AWS Service Catalog products</td><td>Syncs latest status of provisioned AWS Service Catalog products</td><td>5 minutes</td></tr>
  <tr><td>Sync all ServiceNow resources to AWS Config</td><td>Syncs ServiceNow resources mapped to AWS Config custom resources</td><td>6 Hours</td></tr>
  <tr><td>Synchronize changes to all AWS Accounts</td><td>Syncs changes to AWS services opted into each AWS account associated to the Connector</td><td>1 Day</td></tr>
  <tr><td>Synchronize AWS Config</td><td>Syncs resource details or relationships from AWS Config into the ServiceNow CMDB</td><td>31 minutes</td></tr>
  <tr><td>Synchronize AWS Security Hub CSPM</td><td>Syncs bi-directionally security findings from AWS Security Hub CSPM to ServiceNow incidents or problems</td><td>31 minutes</td></tr>
  <tr><td>Synchronize AWS Service Catalog</td><td>Syncs AWS Service Catalog products into ServiceNow Service Catalog request items</td><td>31 minutes</td></tr>
  <tr><td>Synchronize AWS Systems Manager Automation</td><td>Syncs AWS Systems Manager Automation runbooks (documents) into ServiceNow Service Catalog request items</td><td>31 minutes</td></tr>
  <tr><td>Synchronize AWS Systems Manager OpsCenter</td><td>Syncs bi-directionally OpsItems from AWS Systems Manager OpsCenter to ServiceNow incidents</td><td>31 minutes</td></tr>
  <tr><td>Synchronize AWS Support Cases through SQS</td><td>Syncs Support Cases created or updated from AWS into ServiceNow</td><td>1 min</td></tr>
  <tr><td>Synchronize status of synced Support Cases</td><td>Syncs status of Closed Incidents from AWS to ServiceNow</td><td>6 hours</td></tr>
  <tr><td>Synchronize AWS Systems Manager Change Manager</td><td>Syncs pre-approved Change templates and Change Requests from AWS to ServiceNow</td><td>31 min</td></tr>
  <tr><td>Synchronize AWS Systems Manager Incident Manager</td><td>Syncs Incident Manager incidents from AWS to ServiceNow</td><td>1 min</td></tr>
  <tr><td>Synchronize AWS Health</td><td>Syncs Health events and resource information from AWS to ServiceNow</td><td>5 min</td></tr>
  <tr><td>Synchronize Amazon WorkSpaces</td><td>Syncs Amazon WorkSpaces resource type from AWS Config</td><td>31 min</td></tr>
</tbody>
</table>


1. Choose the desired sync job, and choose **Execute Now**.
**Note**  
If you do not see **Execute Now** in the upper left corner, choose **Conﬁgure Job Deﬁnition**. **Execute Now** is visible. ServiceNow Administrator can adjust the Scheduled Job repeat interval as required.

Data is visible in the AWS Service Management scoped app menus after the Connector’s scheduled synchronization job has run.
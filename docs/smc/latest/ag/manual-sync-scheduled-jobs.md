# Manually syncing scheduled jobs

The Connector for ServiceNow includes nine sync jobs related to AWS services
integrations. During the initial setup, manually execute the sync job for your AWS
service integration instead of waiting for Scheduled Jobs to run.

###### To sync AWS service integrations or accounts manually

1. Log in as system administrator.
2. Find **Scheduled Jobs** in the navigator panel.
3. Search the following AWS Service Management Connector scheduled jobs
   (including default sync intervals) in the table below:

| AWS Service Management Scheduled Job Name         | Brief description                                                                                          | Default Sync Interval |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | --------------------- |
| Sync all Automation Execution                     | Syncs execution of AWS Systems Manager Automation runbooks<br>(documents)                                  | 5 minutes             |
| Sync all provisioned AWS Service Catalog products | Syncs latest status of provisioned AWS Service Catalog<br>products                                         | 5 minutes             |
| Sync all ServiceNow resources to AWS Config       | Syncs ServiceNow resources mapped to AWS Config custom<br>resources                                        | 6 Hours               |
| Synchronize changes to all AWS Accounts           | Syncs changes to AWS services opted into each AWS<br>account associated to the Connector                   | 1 Day                 |
| Synchronize AWS Config                            | Syncs resource details or relationships from AWS Config into the ServiceNow CMDB                           | 31 minutes            |
| Synchronize AWS Security Hub                      | Syncs bi-directionally security findings from AWS Security Hub<br>to ServiceNow incidents or problems      | 31 minutes            |
| Synchronize AWS Service Catalog                   | Syncs AWS Service Catalog products into ServiceNow Service Catalog<br>request items                        | 31 minutes            |
| Synchronize AWS Systems Manager Automation        | Syncs AWS Systems Manager Automation runbooks (documents) into<br>ServiceNow Service Catalog request items | 31 minutes            |
| Synchronize AWS Systems Manager OpsCenter         | Syncs bi-directionally OpsItems from AWS Systems Manager OpsCenter<br>to ServiceNow incidents              | 31 minutes            |
| Synchronize AWS Support Cases through SQS         | Syncs Support Cases created or updated from AWS into<br>ServiceNow                                         | 1 min                 |
| Synchronize status of synced Support Cases        | Syncs status of Closed Incidents from AWS to<br>ServiceNow                                                 | 6 hours               |
| Synchronize AWS Systems Manager Change Manager    | Syncs pre-approved Change templates and Change Requests<br>from AWS to ServiceNow                          | 31 min                |
| Synchronize AWS Systems Manager Incident Manager  | Syncs Incident Manager incidents from AWS to<br>ServiceNow                                                 | 1 min                 |
| Synchronize AWS Health                            | Syncs Health events and resource information from AWS<br>to ServiceNow                                     | 5 min                 |
| Synchronize Amazon WorkSpaces                     | Syncs Amazon WorkSpaces resource type from AWS Config                                                      | 31 min                |

4. Choose the desired sync job, and choose **Execute
   Now**.

###### Note

If you do not see **Execute Now** in the
upper left corner, choose **Conﬁgure Job
Deﬁnition**. **Execute Now**
is visible. ServiceNow Administrator can adjust the Scheduled Job repeat
interval as required.
Data is visible in the AWS Service Management scoped app menus after the
Connector’s scheduled synchronization job has run.

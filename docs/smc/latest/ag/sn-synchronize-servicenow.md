# Synchronizing AWS Security Hub CSPM to the Connector in

ServiceNow

This section shows you how to synchronize AWS Security Hub CSPM to the Connector in
ServiceNow.

###### To configure AWS Security Hub CSPM synchronization behavior to the Connector in

ServiceNow

1. In the ServiceNow filter navigator in the fulfiller (stand user interface)
   view, enter `AWS Service Management Connector`.
2. Choose **System Properties**, then **AWS Security Hub CSPM**.
3. Set these configuration items:
   - Choose the types of AWS Security Hub CSPM Findings to sync in ServiceNow:
     **CRITICAL**, **HIGH**, **MEDIUM**, **LOW**, and **INFORMATIONAL**.
   - Choose an action for a newly synced Finding to the Connector in
     ServiceNow:
     - **Do Nothing**. This action only
       imports Security Finding types for the scoped app. Users with
       scoped app permissions can view and choose to create an Incident
       or Problem. **Do Nothing** is the
       default value in the Connector.
     - **Create Incident**. This action
       automatically creates Incidents from Security Findings and syncs
       updates in ServiceNow to AWS Security Hub CSPM.
     - **Create Problem**. This action
       automatically creates Incidents from Security Findings and syncs
       updates in ServiceNow to AWS Security Hub CSPM.
     - **Create Incident and Problem**.
       This action automatically creates Incidents and Problems from
       Security Findings and syncs updates in ServiceNow to
       AWS Security Hub CSPM.

   - Adjust the maximum number of messages to fetch from the SQS queue per
     sync, account, or Region (default 50). By default, the sync process runs
     every five minutes.
   - Change the SQS Queue name if you’re not using the default that the
     Connector created. The CloudFormation template supplies the
     Connector.

   ###### Note

   We recommend you not change the SQS name in the ServiceNow scoped
   app (`AwsServiceManagementConnectorForSecurityHubQueue`)
   unless you change the SQS name in the AWS account.

4. Choose **Save** after any changes.

**Fields synchronized from AWS Security Hub CSPM Findings to the
ServiceNow scoped app AWS Security Hub CSPM Findings module in
ServiceNow**

|                       |                                                                                                                                                                                                               |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Region                | The Region that generated the Finding.                                                                                                                                                                        |
| Account Id            | The account that generated the Finding.                                                                                                                                                                       |
| Company Name          | The company that generated the Finding (e.g. AWS).                                                                                                                                                            |
| Compliance            | Whether a resource passes the configured compliance criteria.<br>Contains status (PASSED, WARNING, FAILED, NOT_AVAILABLE). If the<br>resource does not pass, it will contain information about the<br>reason. |
| Created At            | The creation time of the Finding.                                                                                                                                                                             |
| Description           | A description of the Finding.                                                                                                                                                                                 |
| Criticality           | The level of importance for the resource associated with the<br>Finding.                                                                                                                                      |
| First Observed At     | First observation of when Findings captured any potential security<br>issues.                                                                                                                                 |
| Last Observed at      | The most recent time Findings captured any potential security issues.                                                                                                                                         |
| Product Name          | The name of the product that generates the Finding (such as Security<br>Hub).                                                                                                                                 |
| Product Arn           | The ARN of the product that generates the Finding.                                                                                                                                                            |
| Record State          | Either ACTIVE or ARCHIVED.                                                                                                                                                                                    |
| Severity (normalized) | A value from 0 to 100 that indicates the severity of the problem<br>associated with the Finding.                                                                                                              |
| Status                | PASSED, WARNING, FAILED, or NOT AVAILABLE.                                                                                                                                                                    |
| Title                 | The title of the Finding.                                                                                                                                                                                     |
| Updated At            | When the Finding provider last updated the record.                                                                                                                                                            |
| Workflow Status       | The workflow status can be: NEW, ASSIGNED, IN PROGRESS, RESOLVED,<br>DEFERRED, or DUPLICATE.                                                                                                                  |
| Remediation Text      | A description of suggested action to resolve the discovered issue.                                                                                                                                            |
| Remediation Url       | A link to a resource that can resolve the discovered issue.                                                                                                                                                   |

###### Note

ServiceNow does not duplicate findings. If a Security Hub CSPM finding is sent to ServiceNow
with the same finding ID as one previously sent to ServiceNow, we update the ticket
with the most recent information in the finding.

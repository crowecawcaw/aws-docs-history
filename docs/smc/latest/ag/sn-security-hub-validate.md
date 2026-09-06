

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Security Hub CSPM integration in ServiceNow
<a name="sn-security-hub-validate"></a>

This section describes how to validate AWS Security Hub CSPM integration in ServiceNow.

**To view Findings from AWS Security Hub CSPM**

To view AWS Security Hub CSPM Findings, you must have the role, **x\_126749\_aws\_sc.finding\_manager**, from the Connector scope app. 

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulfiller view (standard user interface view).

1.  In the navigator, enter **AWS Service Management**.

1.  Choose **AWS Security Hub CSPM**.

1. Choose **Findings** to show a list of all synced Findings.

1. Choose a Finding to open the record.

1. The **Incident and Problem** fields show the Incident and Problem related to the Finding if these exist.

1. Choose the ⓘ symbol to the right of the field to preview the Incident or Problem. 

1. Choose **Open Record** on the preview form to open the Incident or Problem.

1. If the Connector does not automatically create a ServiceNow Incident or Problem when a new Finding syncs, choose the link at the bottom of the form to create one manually. 

This table shows how fields map from ServiceNow Findings records to ServiceNow as Incident or Problem records. 


| Finding | Incident | Problem | 
| --- | --- | --- | 
| Created at | Opened at | Opened at | 
| Company Name | Company | Company | 
| Description | Description | Description | 
| Criticality | Impact | Impact | 
| Severity | Urgency | Urgency | 
| Hardcoded to software | Category | Category | 
| Id of record in cmdb\_ci\_service with name AWS Security Hub CSPM | Business service | Business service | 
| Description | Short description | Short description | 
| Reference to related Problem if it exists | problem\_id | n/a | 

This table shows how fields synchronize between AWS Security Findings and ServiceNow Incidents or Problems.


| AWS Security Hub CSPM value | ServiceNow Incident | ServiceNow Problem | 
| --- | --- | --- | 
| Severity Label | Urgency | Urgency | 
| Criticality | Impact | Impact | 

**Fields synchronized between AWS Security Findings, Incidents, and Problems in ServiceNow**
+ Finding severity label → Problem/Incident urgency
  + INFORMATIONAL or LOW → LOW
  + MEDIUM → MEDIUM
  + HIGH or CRITICAL → HIGH
+ Finding criticality → Problem/Incident impact
  + 0 - 29 → LOW
  + 30 - 69 → MEDIUM
  + 70 - 100 → HIGH

**Fields synchronized from Findings to AWS Security Hub CSPM**
+ Severity (Label and Normalized)
+ WorkflowStatus


End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating Support in ServiceNow
<a name="sn-aws-support-validate"></a>

This section describes how to create, view, and manage integration features for Support in order to validate integration.

**To view Cases from Support**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

**To manually sync a Support Case**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose an Incident to open the record.

1. Choose **Sync From AWS**.

**To create a general Support Case**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose **New** from list header.

1. Complete the mandatory fields on the form.
   + **Subject**- Brief summary of the question or issue
   + **Description** – Detailed account of the question or issue
   + **AWS Account** – AWS account against which the support case is initiated
   + **AWS Service** – AWS Service related to the support case
   + **AWS Category** – Category of the case under the related service
   + **Caller** – ServiceNow field that indicates who created the support ticket

1. Choose **Submit**.

1. Choose the Incident you created from the list.

   The **AWS Case Id** and **AWS Case Status** displays.

**For AWS Managed Services Accelerate customer to create AMS Accelerate Service Request**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose **New** from list header.

1. Complete the mandatory fields on the form. 
   + **Subject**- Brief summary of the question or issue
   + **Description** – Detailed account of the question or issue
   + **AWS Account** – AWS account against which the support case is initiated
   + **AWS Service** – AWS Service related to the support case (Select **AMS Operations – Service Request**)
   + **AWS Category** – Category of the case under the related service
   + **Caller** – ServiceNow field that indicates who created the support ticket

1. Choose **Submit**.

1. Choose the Incident you created from the list.

   The **AWS Case Id** and **AWS Case Status** displays.

**For AWS Managed Services Accelerate customer to create AMS Accelerate Report Incident**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose **New** from list header.

1. Complete the mandatory fields on the form. 
   + **Subject**- Brief summary of the question or issue
   + **Description** – Detailed account of the question or issue
   + **AWS Account** – AWS account against which the support case is initiated
   + **AWS Service** – AWS Service related to the support case (Select **AMS Operations – Report Incident**)
   + **AWS Category** – Category of the case under the related service
   + **Caller **– ServiceNow field that indicates who created the support ticket

1. Choose **Submit**.

1. Choose the Incident you created from the list.

   The **AWS Case Id** and **AWS Case Status** displays.

**To add a correspondence to an existing Support Case**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose an Incident to open the record.

1. In the Incident form, scroll to the middle of the page to view and open the **Notes** tab. 

1. Add correspondence on the **Additional Comments **(Customer visible) field. 

1. Choose **Post**.

**To add an attachment to an existing Support Case**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose an Incident to open the record.

1. On the Incident form header, choose paper clip icon to add attachment.

1. Choose the file from your disk to add as an attachment. 

**To resolve a Support Case**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**. 

1. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

1. Choose an Incident to open the record.

1. In the Incident form, scroll to the middle of the page to view and open the Resolution Information tab.

1. Complete the **Resolution Code** and **Resolution Notes** fields.

1. On the Incident form header, choose **Resolve**.

## Fields mapped from Support Case records to ServiceNow Incident records
<a name="fields-incident-records"></a>

This table shows how Support Case map to ServiceNow Incidents.


| Support case | ServiceNow incident | 
| --- | --- | 
| Subject | short\_description | 
| First correspondence | description | 
| Case ID | x\_126749\_aws\_sc\_awssupportcaseid | 
| Status | x\_126749\_aws\_sc\_awscasestatus | 
| Service | x\_126749\_aws\_sc\_awsservice | 
| Category | x\_126749\_aws\_sc\_awscategory | 
| Additional contacts | x\_126749\_aws\_sc\_awscasecommunicationemails | 
| AWS account |  x\_126749\_aws\_sc\_awsaccount  | 

 Incident State is an integer in ServiceNow. We map Support case status values to ServiceNow state. 


| ServiceNow incident Status | Support case status | 
| --- | --- | 
| New | Unassigned | 
| New | Open | 
| In Progress | Work in progress | 
| In Progress | Reopened | 
| On Hold | Pending customer action | 
| Resolved | Resolved | 
| Resolved | Closed | 
| Resolved | Closed | 

**Priority**: In Incident, you can’t set the Priority ﬁeld directly. 

The values of the **Impact** and **Urgency** ﬁelds calculate the **Priority** ﬁeld. When synchronizing from AWS, we set by default the ﬁelds shown in the table below.


| Support Case Severity label | Support Case Severity value | ServiceNow Incident priority label | ServiceNow Incident priority value | 
| --- | --- | --- | --- | 
| Business Critical System Down (Enterprise support plan only) | critical | 1 – Critical | 1 | 
| Production System Down | urgent | 2 – High | 2 | 
| Production System Impaired | high | 3 – Moderate | 3 | 
| System Impaired | normal | 4 – Low | 4 | 
| General Guidance | low | 5 – Planning | 5 | 

Support integration also enables you to customize the priority values, and maps Support Case Severity to ServiceNow Incident Priority.

**To create custom priority mappings**

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).

1. In the navigator, enter **AWS Service Management**.

1. Under **Setup**, choose **Priority Mappings**. Then choose **New**.

1. Choose **AWS Record** **Type** as **Support Case**.

1. For mapping, choose **Support Case Severity** and **ServiceNow Incident Priority**. 

1. Choose **Submit**.
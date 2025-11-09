# Validating Support in ServiceNow

This section describes how to create, view, and manage integration features for
Support in order to validate integration.

###### To view Cases from Support

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.

###### To manually sync a Support Case

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose an Incident to open the record.
5. Choose **Sync From AWS**.

###### To create a general Support Case

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose **New** from list header.
5. Complete the mandatory fields on the form.
   - **Subject**- Brief summary of the
     question or issue
   - **Description** – Detailed account of
     the question or issue
   - **AWS Account** – AWS account against
     which the support case is initiated
   - **AWS Service** – AWS Service related
     to the support case
   - **AWS Category** – Category of the
     case under the related service
   - **Caller** – ServiceNow field that
     indicates who created the support ticket

6. Choose **Submit**.
7. Choose the Incident you created from the list.

The **AWS Case Id** and **AWS Case Status** displays.

###### For AWS Managed Services Accelerate customer to create AMS Accelerate Service

Request

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose **New** from list header.
5. Complete the mandatory fields on the form.
   - **Subject**- Brief summary of the
     question or issue
   - **Description** – Detailed account of
     the question or issue
   - **AWS Account** – AWS account against
     which the support case is initiated
   - **AWS Service** – AWS Service
     related to the support case (Select **AMS Operations
     – Service Request**)
   - **AWS Category** – Category of the
     case under the related service
   - **Caller** – ServiceNow field that
     indicates who created the support ticket

6. Choose **Submit**.
7. Choose the Incident you created from the list.

The **AWS Case Id** and **AWS Case Status** displays.

###### For AWS Managed Services Accelerate customer to create AMS Accelerate Report

Incident

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose **New** from list header.
5. Complete the mandatory fields on the form.
   - **Subject**- Brief summary of the
     question or issue
   - **Description** – Detailed account of
     the question or issue
   - **AWS Account** – AWS account against
     which the support case is initiated
   - **AWS Service** – AWS Service related
     to the support case (Select **AMS Operations –
     Report Incident**)
   - **AWS Category** – Category of the
     case under the related service
   - **Caller** – ServiceNow field that
     indicates who created the support ticket

6. Choose **Submit**.
7. Choose the Incident you created from the list.

The **AWS Case Id** and **AWS Case Status** displays.

###### To add a correspondence to an existing Support Case

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose an Incident to open the record.
5. In the Incident form, scroll to the middle of the page to view and open
   the **Notes** tab.
6. Add correspondence on the **Additional Comments** (Customer visible) field.
7. Choose **Post**.

###### To add an attachment to an existing Support Case

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose an Incident to open the record.
5. On the Incident form header, choose paper clip icon to add
   attachment.
6. Choose the file from your disk to add as an attachment.

###### To resolve a Support Case

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. To show a list of all synched Support Cases, choose **Incidents** under **Support**.
4. Choose an Incident to open the record.
5. In the Incident form, scroll to the middle of the page to view and open
   the Resolution Information tab.
6. Complete the **Resolution Code** and
   **Resolution Notes** fields.
7. On the Incident form header, choose **Resolve**.

## Fields mapped from Support Case records to ServiceNow

Incident records

This table shows how Support Case map to ServiceNow Incidents.

| Support case         | ServiceNow incident                        |
| -------------------- | ------------------------------------------ |
| Subject              | short_description                          |
| First correspondence | description                                |
| Case ID              | x_126749_aws_sc_awssupportcaseid           |
| Status               | x_126749_aws_sc_awscasestatus              |
| Service              | x_126749_aws_sc_awsservice                 |
| Category             | x_126749_aws_sc_awscategory                |
| Additional contacts  | x_126749_aws_sc_awscasecommunicationemails |
| AWS account          | x_126749_aws_sc_awsaccount                 |

Incident State is an integer in ServiceNow. We map Support case status
values to ServiceNow state.

| ServiceNow incident Status | Support case status     |
| -------------------------- | ----------------------- |
| New                        | Unassigned              |
| New                        | Open                    |
| In Progress                | Work in progress        |
| In Progress                | Reopened                |
| On Hold                    | Pending customer action |
| Resolved                   | Resolved                |
| Resolved                   | Closed                  |
| Resolved                   | Closed                  |

**Priority**: In Incident, you can’t set the
Priority ﬁeld directly.

The values of the **Impact** and **Urgency** ﬁelds calculate the **Priority** ﬁeld. When synchronizing from AWS, we set by default
the ﬁelds shown in the table below.

| Support Case Severity label                                     | Support Case Severity value | ServiceNow Incident priority label | ServiceNow Incident priority value |
| --------------------------------------------------------------- | --------------------------- | ---------------------------------- | ---------------------------------- |
| Business Critical System Down (Enterprise support plan<br>only) | critical                    | 1 – Critical                       | 1                                  |
| Production System Down                                          | urgent                      | 2 – High                           | 2                                  |
| Production System Impaired                                      | high                        | 3 – Moderate                       | 3                                  |
| System Impaired                                                 | normal                      | 4 – Low                            | 4                                  |
| General Guidance                                                | low                         | 5 – Planning                       | 5                                  |

Support integration also enables you to customize the priority values, and
maps Support Case Severity to ServiceNow Incident Priority.

###### To create custom priority mappings

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface
   view).
2. In the navigator, enter `AWS Service
Management`.
3. Under **Setup**, choose **Priority Mappings**. Then choose **New**.
4. Choose **AWS Record**
   **Type** as **Support
   Case**.
5. For mapping, choose **Support Case
   Severity** and **ServiceNow Incident
   Priority**.
6. Choose **Submit**.

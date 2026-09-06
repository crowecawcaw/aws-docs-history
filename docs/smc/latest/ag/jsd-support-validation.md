

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating Support integration
<a name="jsd-support-validation"></a>

This section describes how to create, view, and manage integration features for Support.

**To view Support cases from Support as Jira incidents**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent **view, choose the Jira project associated to Support

1. Choose **Incidents** and select the Incident related to the Support case in AWS

**To create a general Support case as a Jira incident**

1. Log in to your Jira Agent view as an end user.

1. In the Jira Service Management Jira Agent view, choose the Jira project associated to Support.

1. Choose **Create **from list header and select Issue Type as **Incident**.

1. Complete the mandatory fields on the form.

   Under the Jira Issue Fields section
   + **Summary**- Brief summary of the question or issue
   + **Description** – Detailed account of the question or issue
   + **Priority **– Severity of the AWS Support case

   Under Support fields section
   + **Create Support case** – Check this box to create support case
   + **Support Service and Category** – AWS Service and Category of the support case
   + **AWS Cc Email Addresses** – Add cc email addresses to the Support case (not mandatory)

1. Choose **Create**.

1. Choose the Incident you created from the list. The **AWS Case Id** and **AWS Case Status **displays.

**For AWS managed services Accelerate customers to create AMS Accelerate Report Incident in Jira**

1. Log in to your **Jira Agent** view as an end user.

1. In the **Jira Service Management Jira Agent **view, choose the Jira project associated to Support.

1. Choose **Create** from list header and select Issue Type as **Incident**.

1. Complete the mandatory fields on the form.

   Under **Jira Issue Fields** section
   + **Summary**- Brief summary of the question or issue
   + **Description** – Detailed account of the question or issue
   + **Priority** – Severity of the Support case

   Under **Support fields** section
   + **Create Support case** – Check this box to create support case
   + **AWS Support Service and Category** – Select AMS Operations – Service Request and choose category
   + **AWS Cc Email Addresses **– Add cc email addresses to the Support case (not mandatory)

1. Choose **Create**.

1. Choose the Incident you created from the list. The **AWS case Id **and **AWS case status** displays.

**To add a correspondence and attachment to an existing Support case in Jira incident**

1. Log in to your **Jira Agent **view as an end user

1. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to Support.

1. Choose **Incidents** and select the Incident related to the Support case in AWS.

1. Use **Add Comment** action or scroll to the bottom of the form and **Click to add comment** to add a correspondence with or without attachments

1. Choose **Share with customer**.

**To resolve an Support case in Jira**

1. Log in to your **Jira Agent **view as an end user.

1. In the **Jira Service Management Jira Agent **view, choose the Jira project associated to Support.

1. Choose **Incidents** and select the Incident related to the Support case in AWS.

1. In the Jira Incident form, choose an action from **Workflow**, **Resolve**.

1. Complete the required mandatory fields.

1. Choose **Resolve**.



**Fields mapped from Support case records to Jira Service Management Incident records**

**Status**: We map Support case status values to JSM state.


| JSM incident status | Support case status | 
| --- | --- | 
| OPEN | Unassigned | 
| OPEN | Opened | 
| WORK IN PROGRESS | Work in progress | 
| WORK IN PROGRESS | Reopened | 
| PENDING | Pending customer action | 
| COMPLETED | Resolved | 

**Priority**: We map Support case severity to JSM Incident Priority


| AWS severity | JSM incident priority | 
| --- | --- | 
| General Guidance | Minor | 
| System Impaired | Low | 
| Production System Impaired | Medium | 
| Production system down | High | 
| Business Critical system down | Blocker | 
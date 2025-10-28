# Validating Support integration

This section describes how to create, view, and manage integration
features for Support.

###### To view Support cases from Support as Jira incidents

1. Log in to your **Jira Agent** view
   as an end user.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to Support
3. Choose **Incidents** and select the
   Incident related to the Support case in AWS

###### To create a general Support case as a Jira incident

1. Log in to your Jira Agent view as an end user.
2. In the Jira Service Management Jira Agent view, choose the Jira
   project associated to Support.
3. Choose **Create** from list header
   and select Issue Type as **Incident**.
4. Complete the mandatory fields on the form.

Under the Jira Issue Fields section

    * **Summary**- Brief summary of
     the question or issue
    * **Description** – Detailed
     account of the question or issue
    * **Priority** – Severity of the
     AWS Support case

Under Support fields section

    * **Create Support case** – Check
     this box to create support case
    * **Support Service and Category**
     – AWS Service and Category of the support case
    * **AWS Cc Email Addresses** –
     Add cc email addresses to the Support case (not mandatory)

5. Choose **Create**.
6. Choose the Incident you created from the list. The **AWS Case Id** and **AWS Case Status** displays.

###### For AWS managed services Accelerate customers to create AMS

Accelerate Report Incident in Jira

1. Log in to your **Jira Agent** view
   as an end user.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to Support.
3. Choose **Create** from list header
   and select Issue Type as **Incident**.
4. Complete the mandatory fields on the form.

Under **Jira Issue Fields**
section

    * **Summary**- Brief summary of
     the question or issue
    * **Description** – Detailed
     account of the question or issue
    * **Priority** – Severity of the
     Support case

Under **Support fields**
section

    * **Create Support case** – Check
     this box to create support case
    * **AWS Support Service and
     Category** – Select AMS Operations – Service Request
     and choose category
    * **AWS Cc Email Addresses** –
     Add cc email addresses to the Support case (not mandatory)

5. Choose **Create**.
6. Choose the Incident you created from the list. The **AWS case Id** and **AWS case status** displays.

###### To add a correspondence and attachment to an existing Support case

in Jira incident

1. Log in to your **Jira Agent** view
   as an end user
2. In the **Jira Service Management Jira
   Agent** view, choose the Jira project associated to
   Support.
3. Choose **Incidents** and select the
   Incident related to the Support case in AWS.
4. Use **Add Comment** action or
   scroll to the bottom of the form and **Click to
   add comment** to add a correspondence with or without
   attachments
5. Choose **Share with
   customer**.

###### To resolve an Support case in Jira

1. Log in to your **Jira Agent** view
   as an end user.
2. In the **Jira Service Management Jira Agent** view, choose the Jira project associated to Support.
3. Choose **Incidents** and select the
   Incident related to the Support case in AWS.
4. In the Jira Incident form, choose an action from **Workflow**, **Resolve**.
5. Complete the required mandatory fields.
6. Choose **Resolve**.
   **Fields mapped from Support case records to Jira
   Service Management Incident records**

**Status**: We map Support case status
values to JSM state.

| JSM incident status           | Support case status     |
| ----------------------------- | ----------------------- | ------------------------------------------------------------------- |
| OPEN                          | Unassigned              |
| OPEN                          | Opened                  |
| WORK IN PROGRESS              | Work in progress        |
| WORK IN PROGRESS              | Reopened                |
| PENDING                       | Pending customer action |
| COMPLETED                     | Resolved                | **Priority**: We map Support case severity to JSM Incident Priority |
| AWS severity                  | JSM incident priority   |
| ---                           | ---                     |
| General Guidance              | Minor                   |
| System Impaired               | Low                     |
| Production System Impaired    | Medium                  |
| Production system down        | High                    |
| Business Critical system down | Blocker                 |

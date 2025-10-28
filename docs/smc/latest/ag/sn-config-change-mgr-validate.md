# Validating AWS Systems Manager Change

Manager integration in ServiceNow

This section describes how to validate AWS Systems Manager Change Manager integration in
ServiceNow.

###### To view AWS Systems Manager Change templates

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management
Connector`.
3. To show a list of all synched Change templates, choose **Change Templates** under **Systems Manager**.

###### To view Systems Manager Change Request

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management
Connector`.
3. To show a list of all synched Change Requests created from ServiceNow,
   choose **Change Requests** under **Systems Manager**.
4. Choose a Change Request to open the record.

###### To view AWS Systems Manager Change Request Ops Items

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `AWS Service Management
Connector`.
3. To show a list of all synched Change Requests created from ServiceNow,
   choose **Change Request Ops Items** under
   **Systems Manager**.
4. Choose an Ops Item to open the record.

###### To create AWS Systems Manager Change Manager change

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter `Change`. Then choose
   **Create New** to view the various Change
   options.
3. Choose **Create AWS Systems Manager Change Manager
   Change: Make changes to AWS resources using Change Manager
   Templates**.
4. Choose the runbook you want to execute and complete all the required
   fields.
5. Choose **Submit** to create a ServiceNow
   Change Request.
6. Choose **Request Approval** to send approval
   requests to members of the Assignment group.

After change approval, it moves to a _Scheduled
state_. 7. Choose **Implement**. 8. Scroll to the bottom and view Change Tasks under related lists to view the
Change task associated with Automation Execution.

After the Change Execution is complete, the change moves to a _Closed state_.

###### To view AWS CloudTrail events for the Change execution

This procedure requires you to create and configure AWS CloudTrail Lake on AWS and
configure the Lake name on the AWS Systems Manager Change Manager system properties in
ServiceNow

1. Log in to your ServiceNow instance as a user (for example, System Administrator) in the fulﬁller view (standard user interface view).
2. In the navigator, enter`AWS Service Management Connector`.
3. To show a list of all synched Change Requests created from ServiceNow, choose **Change Requests** under **AWS Systems Manager**.
4. Choose a Change Request to open the record.
5. Use UI Action, **Sync CloudTrail Events**, to start the
   synchronization of events.
6. Choose the same Change Request to reopen the record.
7. Scroll to the bottom of the Change Request form and use **CloudTrail
   Events** related list to review the events of the Change
   execution.

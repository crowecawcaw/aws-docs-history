# Validating AWS Systems Manager OpsCenter

integration in ServiceNow

This section describes how to validate AWS Systems Manager OpsCenter integration in
ServiceNow.

###### \*\*To view OpsItems from AWS Systems Manager -

OpsCenter\*\*

To view AWS OpsItem, you must have the role,
`x_126749_aws_sc.opscenter_manager`, with the Connector scope
app.

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulfiller view (Standard user interface view).
2. In the navigator, enter `AWS Service Management`.
3. Choose **AWS Systems Manager - OpsCenter**.
4. Choose **OpsItems** to show a list of all
   synced Findings.
5. Choose an OpsItems to open the record.

The **Incident** and **Problem** fields show the Incident for the OpsItems, if these
exist. 6. Choose the ⓘ icon to the right of the field to preview the Incident. 7. Choose **Open Record** on the preview form to
open the Incident.

If the Connector configuration does not to automatically create a
ServiceNow Incident when a new Finding syncs, you can create one manually.
To do so, choose the link at the bottom of the form.

###### \*\*To execute an AWS Systems Manager – Automation Document

from an AWS OpsItems associated to a ServiceNow Incident\*\*

One of the following conditions must be true to view or execute automation
documents (runbooks):

- The user has the role Account Manager or Automation Manager.
- The user has a linked Incident.
- The system parameter **Assignment Group (SYS_ID)
  for created incidents** is set to a valid group and a
  linked Incident whose Assignment group is set to that group, and the
  user is a member of that group.

###### Note

To enable this feature, you must activate AWS Systems Manager Automation
in the AWS Account and opt in to the Connector.

1. Log in to your ServiceNow instance as a user (for example, System
   Administrator) in the fulfiller view (standard user interface view).
2. In the navigator, enter `AWS Service Management`.
   Then choose **AWS Systems Manager -
   OpsCenter**.
3. Choose OpsItems to show a list of all synced Findings. Then choose
   **Execute Automation Document**.
4. Choose your Automation Document.

###### Note

You can configure an OpsItem with Automation Documents and mark it as
_Associated_. 5. Choose **Order Execution** next to the
Automation Document you want to execute. You’ll see the ServiceNow catalog
item associated with the Automation Document. 6. Enter the necessary AWS parameters and choose **Order Now**. 7. In OpsItems in the scoped app, choose the OpsItem in the Automation
Document where you executed it. 8. In **OpsItem Automation Executions**, review
the success or failure status. 9. Follow your organization's Incident management procedures to determine
related Incident resolution actions.

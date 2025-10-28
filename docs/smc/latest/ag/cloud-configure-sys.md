# Validating AWS Systems Manager Automation in Jira Service

Management Cloud

To allow the Connector to execute Automation Documents, you must ensure that the
Connector's sync user and end user have the required permissions. For more information,
review [Setting up Automation](../../../systems-manager/latest/userguide/automation-setup.md "../../../systems-manager/latest/userguide/automation-setup.md") in the _AWS Systems Manager user guide_.

###### \*\*To execute a AWS Systems Manager Automation Document from Jira agent

view\*\*

1. Log in to your Jira Agent view.
2. Open the desired **Jira project** and then navigate to the
   **AWS Service Management Connector** app.
3. Choose the **Systems Manager Automation** tab.
4. Enter the required **automation execution parameters** and
   add optional **Tags**.
5. Choose **Execute** to submit the Jira Service Management
   request and execute the automation document.
   After Jira processes the request, Jira displays a message indicating that the request
   was created. When the automation document execution starts, you are able to view the
   details in the Automation panel within the Jira issue.

###### \*\*To view provisioned products using the Jira Agent

view\*\*

1. Log in to your Jira Agent view.
2. Use Jira filters to display only issues with the **Support Automation
   Request** Issue Type.
3. Open the Jira issue.
4. Choose the **Automation Details** panel.

Review the Automation Execution details, including the status of the
execution, parameters, and step functions.
When the execution is complete, the issue moves to the **Execution
complete** status.

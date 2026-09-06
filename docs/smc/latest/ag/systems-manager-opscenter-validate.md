

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Systems Manager OpsCenter integration
<a name="systems-manager-opscenter-validate"></a>

This section describes how to validate the AWS Systems Manager OpsCenter integration in Jira.

**Run an AWS Systems Manager automation document from an AWS OpsItems associated with a Jira incident**

To view or execute automation documents (runbooks), the user must belong to the Jira permissions group assigned to the AWS Systems Manager automation integration. This group can be set on the **Connector Settings** page.

**Note**  
To enable this feature, you must activate AWS Systems Manager automation in the AWS account and opt in to the connector.

1. Log in to your Jira Agent view.

1. Open your Jira project, and choose an **OpsItem** issue.

1. From the **Actions** menu at the top-right of the **Issues** page, choose **Request runbook execution**.

1. Choose your automation document.

**Create a Jira Incident from AWS OpsItems**

1. Log in to your Jira Agent view.

1. Open the desired Jira project, and choose an OpsItem issue.

1. From the **Actions** menu at the top-right corner of the **Issues** page, choose **Create** Incident

1. Choose a response plan, and then choose **Confirm**.

**View related OpsItems or AWS Incidents from an AWS OpsItems**

**Note**  
There isn’t a field for **RelatedOpsItems** because Jira already offers a native feature that can link Jira issues. Upon synchronization from AWS, AWS Service Management Connector looks up any Jira issues that correspond to the related OpsItems and links them. Similarly, if an end user in Jira links an issue of type *AWS OpsItem* to another issue of type *AWS OpsItem*, then AWS Service Management Connector marks the corresponding AWS OpsItems as related.

1. Log in to Jira Agent view.

1. Open your Jira project, and choose an OpsItem issue.

1. View related OpsItems at the bottom of the form.
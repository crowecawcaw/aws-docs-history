

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Validating AWS Systems Manager Automation in Jira Service Management Cloud
<a name="cloud-configure-sys"></a>

To allow the Connector to execute Automation Documents, you must ensure that the Connector's sync user and end user have the required permissions. For more information, review [Setting up Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html) in the *AWS Systems Manager user guide*. 

****To execute a AWS Systems Manager Automation Document from Jira agent view****

1. Log in to your Jira Agent view. 

1. Open the desired **Jira project** and then navigate to the **AWS Service Management Connector** app. 

1. Choose the **Systems Manager Automation** tab. 

1. Enter the required **automation execution parameters** and add optional **Tags**. 

1. Choose **Execute** to submit the Jira Service Management request and execute the automation document. 

After Jira processes the request, Jira displays a message indicating that the request was created. When the automation document execution starts, you are able to view the details in the Automation panel within the Jira issue. 

****To view provisioned products using the Jira Agent view****

1. Log in to your Jira Agent view. 

1. Use Jira filters to display only issues with the **Support Automation Request** Issue Type. 

1. Open the Jira issue. 

1. Choose the **Automation Details** panel. 

   Review the Automation Execution details, including the status of the execution, parameters, and step functions. 

When the execution is complete, the issue moves to the **Execution complete** status.
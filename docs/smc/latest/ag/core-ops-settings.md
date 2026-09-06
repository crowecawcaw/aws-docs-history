

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Configuring core operational settings
<a name="core-ops-settings"></a>

**To configure operational settings for the AWS Service Management Connector for Jira Service Management**

1. In the left navigation menu, under **AWS Service Management Connector**, choose **Connector settings**.

1. Under **Core operational settings**, in the **Synchronization interval** field, you can change the sync interval if you want.

   This interval determines how often Jira Service Management syncs with AWS. Increasing this number reduces the number of API calls to AWS, but increases the time for updates in AWS portfolios and automation documents to reflect in the Connector. Information on actively provisioning products and ongoing automation executions updates are more frequent.

1. Under **Core operational settings**, in the **JIRA Administrator to run as** field, you can change the admin user assigned to perform automated operations within JIRA.
**Important**  
The Connector performs many actions within Jira, and needs to do those actions as a Jira user. By default, Connector chooses the Jira Admin user with the lowest ID, which works for many environments.

   However, that approach might be the wrong strategy if the initial admin user has been disabled, or if there is a different admin user. For clarity within the Connector, it can be a good idea to create a new user called, for example, "AWS Connector Admin", and select that as the default user.

   We record actions performed automatically by the Connector as being performed by this user, such as synchronizing OpsItems from AWS or adding a comment for changes to an AWS provisioned product. These actions do not affect actions that end users perform, such as requesting a provisioned product or manually creating an OpsItem in Jira, which we record as the end user performing the action.

   This user should have global admin permissions, JSM permissions, and admin access to each of the AWS-enabled projects.

1. Choose **Save**.

**Note**  
We recommend no changes to entities that the plugin created, such as the addition of fields, workflows, issue types, screens, and so on.
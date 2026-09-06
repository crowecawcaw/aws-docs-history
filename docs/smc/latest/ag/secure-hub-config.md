

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Associating Jira projects to the AWS Security Hub CSPM integration
<a name="secure-hub-config"></a>

After you've enabled projects for the Connector, AWS Security Hub CSPM requires Jira admins to associate Jira project(s) to this integration, and configurations to manage the Security Hub integration.

**To associate the Jira projects enabled for the Connector to the AWS Security Hub CSPM integration features**

1. In the left navigation menu under **AWS Service Management Connector**, choose **Connector settings**.

1. Create a [new Jira Service Management Project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html).

   Under **Security Hub Configuration**, you must enable at least one Jira project. You can create a [new Jira Service Management project ](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html) or add an existing project. Only users with access to the associated project can access the Connector.

   When you apply this update, the Connector adds the necessary issue type to associated project(s). You can return to this screen and add or remove projects at any time.

1. Under **AWS Security Hub CSPM Configuration,** in the **Sync Interval **field, you can change the sync interval if you want. **SQS Queue Name **and **Number of messages to pull from SQS** set the Amazon SQS queue and the polling size, respectively. **Synchronize AWS Security Hub CSPM Findings according to their Severity value ** determines the Findings with specific severities that sync to the JSM project. 

1. Choose **Save**.
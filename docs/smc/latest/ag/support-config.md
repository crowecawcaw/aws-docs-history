

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Associate Jira projects to the Support integration
<a name="support-config"></a>

After you enable projects for the Connector, Support integration requires Jira admins to associate Jira project(s) to this integration, as well as determine the SQS Queue Name and sync intervals.

**To associate the Jira projects enabled for the Connector to the AWS Systems Manager OpsCenter integration features**

1. In the left navigation menu, under **AWS Service Management Connector**, choose C**onnector settings**.

1. Create a [new Jira Service Management Project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html).

   Under **Support Configuration**, you must enable at least one Jira project. You can create a [new Jira Service Management project ](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html) or add an existing one. Only users with access to the associated project can access the Connector.

   When you apply this update, the Connector adds the necessary issue type to associated project(s). You can return to this screen and add or remove projects at any time.

1. Under **Support Configuration**, in the **Sync Interval,** you can change the sync interval if you want. The **Sync Interval** determines how often Jira Service Management conducts syncs for all **AWS Services** and **AWS Categories**.** SQS Queue Name **identifies the Amazon SQS queue from which the Support case events sync to JSM

1. Choose **Save**.


End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Associate Jira projects to the AWS Systems Manager OpsCenter integration
<a name="ops-center-config"></a>

Once you've enabled projects for the Connector, AWS Systems Manager OpsCenter requires Jira admins to associate Jira project(s) to this integration, as well as determine the full sync and delta sync intervals.

**To associate the Jira projects enabled for the Connector to the AWS Systems Manager OpsCenter integration features**

1. In the left navigation menu, under **AWS Service Management Connector**, choose **Connector settings**.

1. Create a [new Jira Service Management Project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html). Under **OpsCenter Configuration**, you must enable at least one Jira project. You can create a [new Jira Service Management project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html) or add an existing one. Only users with access to the associated project can access the Connector. When you apply this update, the Connector adds the necessary issue type to associated project(s). You can return to this screen and add or remove projects at any time.

1. Under **AWS Systems Manager OpsCenter Configuration**, in the **Full Sync Interval** and **Delta Sync Interval** fields, you can change the sync interval if you want. The **Full Sync** and** Delta** interval determines how often Jira Service Management conducts syncs all or changes to OpsItems details with AWS Systems Manager OpsCenter respectively. Increasing this number reduces the number of API calls to AWS, but increases the time for OpsItems updates to reflect in the Connector.

1. Choose **Save**.
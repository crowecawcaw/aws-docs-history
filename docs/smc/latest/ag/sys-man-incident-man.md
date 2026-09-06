

End of support notice: On March 31, 2027, AWS will end support for AWS Service Management Connector. After March 31, 2027, you will no longer be able to access the AWS Service Management Connector console or AWS Service Management Connector resources. For more information, see [AWS Service Management Connector end of support](https://docs.aws.amazon.com/smc/latest/ag/smc-end-of-support.html). 

# Associating Jira projects to the AWS Systems Manager Incident Manager integration
<a name="sys-man-incident-man"></a>

Once you've enabled projects for the Connector, AWS Systems Manager Incident Manager integration requires Jira admins to associate Jira project(s) to this integration, as well as determine the full sync and delta sync intervals.

**To associate the Jira projects enabled for the Connector to the AWS Systems Manager Incident Manager integration features**

1. In the left navigation menu, under **AWS Service Management Connector**, choose **Connector settings**.

1. Create a new [Jira Service Management Project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html). Under **Incident Manager Configuration**, you must enable at least one Jira project. You can create a new Jira Service Management project or add an existing one. Only users with access to the associated project can access the Connector. When you apply this update, the Connector adds the necessary issue type to associated project(s). You can return to this screen and add or remove projects at any time.

1. Under **AWS Systems Manager Incident Manager Configuration**, the **Synchronization of the resolved status**, determine whether a resolution of an Incident from AWS should transition the corresponding Jira issue to the **Resolved** Status or the inverse. The default sync interval for this integration is one minute.

1. Choose **Save**.
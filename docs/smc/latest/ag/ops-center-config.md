# Associate Jira projects to the AWS Systems Manager OpsCenter

integration

Once you've enabled projects for the Connector, AWS Systems Manager
OpsCenter requires Jira admins to associate Jira project(s) to this
integration, as well as determine the full sync and delta sync
intervals.

###### To associate the Jira projects enabled for the Connector to the

AWS Systems Manager OpsCenter integration features

1. In the left navigation menu, under **AWS Service
   Management Connector**, choose **Connector
   settings**.
2. Create a [new Jira Service Management Project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html "https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html"). Under **OpsCenter Configuration**, you must enable
   at least one Jira project. You can create a [new Jira Service Management project](https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html "https://confluence.atlassian.com/servicedeskserver043/setting-up-your-service-desk-974367545.html") or add an existing
   one. Only users with access to the associated project can access
   the Connector. When you apply this update, the Connector adds the
   necessary issue type to associated project(s). You can return to
   this screen and add or remove projects at any time.
3. Under **AWS Systems Manager OpsCenter
   Configuration**, in the **Full Sync
   Interval** and **Delta Sync
   Interval** fields, you can change the sync interval if
   you want. The **Full Sync**
   and **Delta** interval determines
   how often Jira Service Management conducts syncs all or changes to
   OpsItems details with AWS Systems Manager OpsCenter respectively. Increasing
   this number reduces the number of API calls to AWS, but
   increases the time for OpsItems updates to reflect in the
   Connector.
4. Choose **Save**.

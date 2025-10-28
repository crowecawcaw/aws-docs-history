# AWS Well-Architected Tool Connector for Jira

You can use the AWS Well-Architected Tool Connector for Jira to link your Jira account with AWS Well-Architected Tool and sync improvement items from your workloads to Jira projects to help you create a closed-loop mechanism in implementing improvements.

The connector provides both Automatic and Manual syncing. For more detail, see [Configuring the connector.](configuring-jira.md "configuring-jira.md")

The connector can be set up at the account level and the workload level, with the option to override your account-level settings per workload. At the workload level, you can also choose to exclude a workload from syncing entirely.

You can choose to have improvement items synced to the default WA Jira project, or specify an existing project key to sync to. At the workload level, you can sync each workload to a unique Jira project if necessary.

###### Note

The connector only supports scrum and kanban projects in Jira.

When improvement items are synced to Jira, they are organized in the following way:

- **Project:** WA (or existing project you specify)
- **Epic:** Workload
- **Task:** Question
- **Sub-task:** Best practice
- **Label:** Pillar

After you set up Jira account syncing in the **Settings** page, you can [configure the Jira connector](configuring-jira.md "configuring-jira.md") and [sync improvement items to your Jira account](syncing-workload.md "syncing-workload.md").

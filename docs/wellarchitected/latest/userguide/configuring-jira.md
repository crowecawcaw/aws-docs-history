# Configuring the connector

With the AWS Well-Architected Tool Connector for Jira, you can configure Jira syncing at the account level, the workload level, or both. You can configure workload-level Jira settings independent of account-level settings, or override your account-level settings on a specific workload to specify the workload's sync behavior. You can also configure Jira settings when [Defining a workload](define-workload.md "define-workload.md").

The connector provides two sync methods: **Automatic** and **Manual** sync. In both sync methods, changes that are made in AWS WA Tool are reflected in your Jira project, and changes made in Jira are synced back to AWS WA Tool.

###### Important

By using Automatic sync, you consent to AWS WA Tool modifying your workload in response to changes in Jira.

If you have sensitive information you do not wish to sync to Jira, do not input this information into the **Notes** field in your workloads.

- **Automatic sync:** The connector automatically updates your Jira project and your workload each time a question is updated, including selecting or deselecting a best practice and completing a question.
- **Manual sync:** You must choose **Sync with Jira** in the workload dashboard when you want to sync improvement items between Jira and the AWS WA Tool. You can also choose which specific pillars and questions you want to sync. For more detail, see [Syncing a workload](syncing-workload.md "syncing-workload.md").

###### To configure the connector at the account level

1. Select **Settings** in the left navigation pane.
2. In the **Jira account syncing** pane, choose **Edit**.
3. For **Sync type**, select one of the following:
   1. To automatically sync workloads when changes are made, select **Automatic**.
   2. To manually choose when to sync workloads, select **Manual**.

4. By default, the connector creates a **WA** Jira project. To specify your own Jira project key, do the following:
   1. Select **Override default Jira project key**.
   2. Enter your **Jira project key**.

   ###### Note

   The specified **Jira project key** is used for all workloads unless you change the project at the workload level.

5. Choose **Save settings**.

###### To configure the connector at the workload level

1. Select **Workloads** in the left navigation pane, and select the name of the
   workload you want to configure.
2. Choose **Properties**.
3. In the **Jira** pane, choose **Edit**.
4. To configure the workload's Jira settings, select **Override account level settings**.

###### Note

**Override account level settings** must be selected in order to apply workload-specific settings. 5. For **Sync override**, select one of the following:

    1. To exclude the workload from Jira sync, select **Do not sync workload**.
    2. To manually choose when to sync the workload, select **Sync workload - Manual**.
    3. To sync workload changes automatically, select **Sync workload - Automatic**.

6. (Optional) For **Jira project key**, enter the project key to sync the workload to. This project key can be different from your account-level project key.

If you don't specify a project key, the connector creates a **WA** Jira project. 7. Choose **Save**.

For detail on performing a manual sync, see [Syncing a workload](syncing-workload.md "syncing-workload.md").

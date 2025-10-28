# Running a workflow

You can run a workflow using the Lake Formation console, the AWS Glue console, or the AWS Glue Command
Line Interface (AWS CLI), or API.

###### To run a workflow (Lake Formation console)

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as the data lake
   administrator or as a user who has data engineer permissions. For more information, see
   [Lake Formation personas and IAM permissions reference](permissions-reference.md "permissions-reference.md").
2. In the navigation pane, choose **Blueprints**.
3. On the
   **Blueprints** page, select the workflow. Then on the
   **Actions** menu, choose **Start**.
4. As the workflow runs, view its progress in the **Last run status**
   column. Choose the refresh button occasionally.

The status goes from **RUNNING**, to
**Discovering**, to **Importing**, to
**COMPLETED**.

When the workflow is complete:

    * The Data Catalog has new metadata tables.
    * Your data is ingested into the data lake.

If the workflow fails, do the following:

    1. Select the workflow. Choose **Actions**, and then choose
     **View graph**.


    The workflow opens in the AWS Glue console.
    2. Ensure that the workflow is selected, and choose the **History**
     tab.
    3. Under **History**, select the most recent run and choose
     **View run details**.
    4. Select a failed job or crawler in the dynamic (runtime) graph, and review the
     error message. Failed nodes are either red or yellow.

###### See also:

- [Blueprints and workflows in Lake Formation](workflows-about.md "workflows-about.md")

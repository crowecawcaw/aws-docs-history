# Connect to a GitLab data source

The GitLab data source allows you to keep track of detailed GitLab statistics,
such as top contributors, commits per day, or deployments per day. You can also use
template variables, such as projects, to set up filters for your dashboards. You can
combine data from the GitLab API with data from other sources.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

## Known limitations

Alerting is not supported yet on this plugin because transformations are not
supported in alert queries and transformations is the only way to obtain
meaningful aggregate metrics from GitLab API raw data.

## Adding the data source

1. Open the Grafana console in the Amazon Managed Grafana workspace and make sure you
   are logged in.
2. In the side menu under **Configuration** (the gear
   icon), choose **Data Sources**.
3. Choose **Add data source**.

###### Note

If you don't see the **Data Sources** link in
your side menu, it means that your current user does not have the
`Admin` role. 4. Select **GitLab** from the list of data sources. 5. Enter the following information:

    * For **Name**, enter a name for this GitLab
     data source.
    * For **URL**, enter the root URL for your
     GitLab instance, such as
     `https://gitlab.com/api/v4`.
    * For **Access token**, enter your GitLab
     personal access token.

## Query the GitLab data source

From the GitLab Query Editor you can select different resource types, such as
commits, issues, or releases.

###### Filter and view projects

1. From the dropdown menu, choose **Projects**.
2. (Optional) Filter by the projects that you own.
3. Use the dropdown and select **Yes** or
   **No** to filter the results.

###### Note

Fetching all the projects **Owned = No** can
take a long time.

###### Filter and view commits

1. From the dropdown menu, choose **Commits**.
2. Use the input field to add the project ID.
3. (Optional) To filter by branch/tag use the input field to add a
   branch/tag reference.

###### Filter and view issues

1. From the dropdown menu, choose **Issues**.
2. Use the input field to add the project ID.
3. (Optional) To filter by title/description, use the input field to
   search issues based on their **title** and
   **description**.

###### View releases

1. From the dropdown menu, choose **Deployments**.
2. Use the input field to add the project ID.
3. (Optional) To filter by environment/status, use the input fields. The
   **status** attribute can be one of the following
   values: `created`, `running`,
   `success`, `failed`, or `canceled`.

###### View labels

1. From the dropdown menu, choose **Labels**.
2. Use the input field to add the project ID.

## Templates and variables

To add a new GitLab query variable, see [Adding a query variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable"). Use your GitLab data source as the
data source. Choose a resource type: **Releases**,
**Projects**, or **Labels**.

To get a dynamic list of projects, labels, and so on to choose from, create a
Query type variable. Query type variables use the GitLab Query Editor to query
and return Projects, Labels, and so on. The following example creates a Project
variable to parameterize your queries

###### Create a Project variable to parameterize your queries

1. Add a variable of type **Query** named
   `project`.
2. Select your GitLab data source and refresh **On Dashboard
   Load**.
3. Select the **Projects** resource type,
   **Yes** for **Owned**,
   **name** for **display field** and
   **id** for **value field** .
4. Choose **Update** to add the variable to the
   dashboard.
5. Add a new panel to the dashboard and use
   `$project` as the project ID.

Now, when choosing from the dropdown, you get the results that belong
to that project.

## Using transformations from Grafana to

answer common questions

Now that you can perform basic GitLab queries to find commits, issues, etc,
you can use Transformations to visualize, aggregate, group, and join datasets,
along with many other types of transformations to transform simple results into
answers for complex questions. Below are a few common questions and how to use
transformations to answer them.

**How many commits/issues/deployments per day in my
project?**

1. Add a query. Select **Commits** for the resource
   type and add the project ID.
2. Add a new **Group by** transformation: for
   **Group by**, select
   **created_at_date** and then calculate
   **(Count)=id**
3. Choose the **Graph** visualization.

**What is the average time to close issues in my
project?**

1. Add a query. Select **Issues** for the resource type
   and add the project ID.
2. Add a new **Add field from calculation**
   transformation: for **Mode**, select **Binary
   Operation**, for **Operation**, select
   **closed_at = created_at** and for
   **Alias** choose
   **resolution_time**.
3. Add a new **Add field from calculation**
   transformation: for **Mode**, select **Binary
   Operation**, for **Operation**, select
   **resolution_time / 86400000** and for
   **Alias** choose
   **resolution_time**.

For **Replace all fields**, choose
**True**. 4. Choose the **Stat** visualization.

    * Show = Calculate
    * Calculation = Mean
    * Fields = **resolution\_time**

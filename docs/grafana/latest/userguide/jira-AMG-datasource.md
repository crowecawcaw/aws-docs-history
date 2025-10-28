# Connect to a Jira data source

Get the whole picture of your development process by combining issue data from
Jira with application performance data from other sources.

###### Note

This data source is for Grafana Enterprise only. For more information,
see [Manage access to Enterprise plugins](upgrade-to-enterprise-plugins.md "upgrade-to-enterprise-plugins.md").

Additionally, in workspaces that support version 9 or newer, this data source might
require you to install the appropriate plugin. For more information, see [Extend your workspace with plugins](grafana-plugins.md "grafana-plugins.md").

- Create annotations based on issue creation or resolution, to see the
  relationship between issues and metrics.
- Track detailed Jira stats, such as mean time to resolution and issue
  throughput.
  In order to use the Jira data source, you need an Atlassian account with access to
  a Jira project.

## Known limitations

Custom field types from Jira addons might not be supported.

## Adding the data source

1. Open the Grafana console in the Amazon Managed Grafana workspace and make sure you
   are logged in.
2. In the side menu under **Configuration** (the gear
   icon), choose **Data Sources**.
3. Choose **Add data source**.

###### Note

If you don't see the **Data Sources** link in
your side menu, it means that your current user does not have the
`Admin` role. 4. Select **Jira** from the list of data sources. 5. Enter the following information:

    * For **Name**, enter a name for this Jira data
     source.
    * For **URL**, enter the root URL for your
     Atlassian instance, such as
     `https://bletchleypark.atlassian.net`.
    * For **User**, enter an email address for the
     user/service account.
    * For **API token**, enter an API token
     generated for the user.

## Query the Jira data source

From the Jira Query Editor you can select fields and query issues.

The Jira data source queries Jira for issues, which can represent bugs, user
stories, support tickets, or other tasks in Jira

###### Filter and view issues

1. Choose **Fields** choose the dropdown and use
   type-ahead to select from any of the fields in your Jira instance,
   including custom fields. Some fields to try:
   - **Summary**— The name of the
     issue
   - **Epic Name**— The epis that an issue
     belongs to
   - **Story Point Estimate**— The number
     of story points that the team has estimated for an issue

2. Filter or sort the issues. To do so, enter any valid JQL expression
   to filter or sort the issues based on any of their fields such as
   **Project**, **Assignee**, or
   **Sprint** with the Atlassian query language JQL.

From here, you can display your data in a table or use Grafana transformations
to manipulate that issue data, run calculations, or turn the data into a time
series graph. For more information, see [Applying a transformation](panel-transformations.md#apply-a-transformation "panel-transformations.md#apply-a-transformation").

## Time series query

To show time series data, choose a **Date** field along with
a numeric field, then switch to graph visualization. For example:
**Sprint Start Date**, **Story point
estimate**.

The preceding example, on its own, is not very useful. The numeric field can
be (and will most likely be) calculated from Transformations. Using the
**Group By** Transformation would allow grouping by
**Sprint Start Date** and summarizing the **Story
point estimate** allowing a visualization of Story Points over time
per Sprint. For more information about transformations, see [Applying a transformation](panel-transformations.md#apply-a-transformation "panel-transformations.md#apply-a-transformation").

## Templates and variables

To add a new Jira query variable, see [Adding a query variable](variables-types.md#add-a-query-variable "variables-types.md#add-a-query-variable"). Use your Jira data source as the
data source.

You can define variables on your dashboards and reference them in JQL
expressions. For example, you can create a project status dashboard and choose
between projects, or an epic status dashboard and choose different epics, or a
task status dashboard and choose different assignees.

To get a dynamic list of projects, epics, assignees, and so on to choose from,
create a Query type variable. Query type variables use JQL to query issues and
return Projects, Epics, Assignees, or anything related to issues. The following
is an example:

###### Create an Assignee variable to get the status of issues by

Assignee

1. Add a variable of type **Query** named
   `assignee`.
2. Select **Field: Assignee**.
3. )Optional) Add a JQL filter **project = 'your
   project'**.
4. Choose **Run** to see a list of Assignees.
5. Choose **Update** to add the variable to the
   dashboard.
6. Add a new panel to the dashboard and edit the JQL to filter using your
   new variable **assignee = $assignee**.

Now, when choosing from the dropdown, you see only the issues assigned
to that user.

Multi-value variables allow selecting multiple options and can be used as part
of the IN clause. For example, **assignee IN
($assignee)**.

## Using transformations from Grafana to answer

common questions

Macros are variables that reference the Dashboard time window so you can
filter issues only within the range of the Dashboard window. There are 2 macros:

- **$\_\_timeFrom**
- **$\_\_timeTo.**

The following example JQL query filters issues created within the dashboard
time window: `createdDate >= $__timeFrom AND createdDate <=
 $__timeTo`

## Get the most out of the data source

Using Grafana's transformations and other built-in features can help you
meaningly view your Jira data.

### Using transformations to

augment JQL

While there are many Transformations in Grafana to choose from, the
following provide a powerful augmentation to give JQL some of the
features/power of SQL.

**Group By** This transformation provides a
key feature that is not part of the standard Jira JQL syntax: Grouping.
Using the **Group By** transformation, you can group by
Sprints or other Issue fields, and aggregate by group to get metrics like
velocity and story point estimates vs actual completed in a Sprint.

**Outer Join** Similar to SQL joins, you can
join 2 or more queries together by common fields. This provides a way to
combine datasets from queries and use other transformations to calculate
values from multiple queries/datasets.

**Add Field from Calculation** Similar to SQL
expressions, this transformation allows adding new fields to your dataset
based on calculations of other fields. The fields used in the calculation
can be from a single query or from queries you've joined together. You can
also chain together calculations and perform calculations from calculated
fields.

### Using transformations from

Grafana to answer common questions

You can use Transformations to visualize, aggregate, group, and join
datasets, along with many other types of transformations to transform simple
results into answers for complex questions.

**How do I show Velocity per Sprint?**

1. Select Fields: **Sprint Name**, **Story
   point estimate**.
2. Add a JQL filter: `project = "Your Project" AND type != epic
AND status = done order by created ASC`
3. Add a **Group By** transformation:
   - Sprint Name | Group By
   - Story Point Estimate | Calculate | Total

4. Choose the **Bar Gauage** visualization.

**How do I show what was Completed vs Estimated in a
Sprint?**

1. Add a query. First, select Fields: **Sprint
   Name**, **Sprint Start Date,**,
   **Story point estimate**.

Then add a JQL filter: `project = 'Your Project' AND type !=
 epic` 2. Add a second query. First, select Fields: **Sprint
Name**, **Sprint Start Date,**,
**Story point estimate**.

Then add a JQL filter: `project = 'Your Project' AND type !=
 epic AND status = done` 3. Add a **Group By** transformation:

    * Sprint Name | Group By
    * Sprint Start Date | Group By
    * Story Point Estimate | Calculate | Total

4. Choose the **Graph** visualization.

**What is the Average time to complete issues in my
project?**

1. Add a query. First, select Fields: **Created**,
   **Status Category Changed**.

Then add a JQL filter: `project = 'Your Project' AND type !=
 epic AND status = done` 2. Add a transformation: **Add field from
calculation**

    * Mode = Reduce Row
    * Calculation = Difference

3. Add a transformation: **Add field from
   calculation**
   - Mode = Binary Operation
   - Operation = Difference / 86000000
   - Alias = Days

4. Add a transformation: **Organize fields**
   - Hide Different field

5. Add a transformation: **Filter data by
   values**
   - Filter Type = Include
   - conditions = Match any
     - Field = Days | Match = Is Greater | Value =
       1

6. Add a transformation: **Reduce**
   - Mode = Series to Rows
   - Calculations = mean

7. Choose the **Stat** visualization.

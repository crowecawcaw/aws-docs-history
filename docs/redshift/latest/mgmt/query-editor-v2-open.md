Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Opening query editor v2

With Amazon Redshift, you can execute SQL queries against your data warehouse cluster using the
query editor v2 in the Amazon Redshift console. The query editor v2 is a web-based tool that provides a user-friendly
interface for running ad-hoc queries, exploring data, and performing data analysis
tasks. The following sections guide you through the process of opening the query editor v2 in the
console and utilizing its functionalities effectively.

###### To open the query editor v2

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. From the navigator menu, choose **Editor**, then
   **Query editor V2**. The query editor v2 opens in a new browser
   tab.

The query editor page has a navigator menu where you choose a view as
follows:

**Editor
![Horizontal lines representing redacted or censored text.](images/qev2-align-left.png)**

You manage and query your data organized as tables and contained in a
database. The database can contain stored data or contain a reference to
data stored elsewhere, such as Amazon S3. You connect to a database contained in
either a cluster or a serverless workgroup.

When working in the **Editor** view, you have the
following controls:

- The **Cluster** or **Workgroup**
  field displays the name you are currently connected to. The
  **Database** field displays the databases
  within the cluster or workgroup. The actions that you perform in the
  **Database** view default to act on the
  database you have selected.
- A tree-view hierarchical view of your clusters or workgroups,
  databases, and schemas. Under schemas, you can work with your
  tables, views, functions, and stored procedures. Each object in the
  tree view supports a context menu to perform associated actions,
  such as **Refresh** or **Drop**,
  for the object.
- A
  ![The create icon used in the AWS Console.](images/qev2-add.png)

**Create** action to create databases, schemas,
tables, and functions.

- A
  ![The upload icon used in the AWS Console.](images/qev2-upload.png)
  **Load data** action to load
  data from Amazon S3 or from a local file into your database.
- A
  ![The floppy disk icon used in the AWS Console.](images/qev2-floppy-disk.png)

**Save** icon to save your query.

- A
  ![The shortcut icon used in the AWS Console.](images/qev2-key-command.png)

**Shortcuts** icon to display keyboard shortcuts
for the editor.

- A
  ![The more actions icon used in the AWS Console.](images/qev2-more.png)

**More** icon to display more actions in the
editor. Such as:

    + **Share with my team** to share the query
     or notebook with your team. For more information, see [Collaborating and sharing as a team](query-editor-v2-team.md "query-editor-v2-team.md").
    + **Shortcuts** to display keyboard
     shortcuts for the editor.
    + **Tab history** to display tab history of
     a tab in the editor.
    + **Refresh autocomplete** to refresh the
     displayed suggestions when authoring SQL.

- An
  ![The editor icon in the AWS Console where can enter and run queries.](images/add-plus.png)

**Editor** area where you can enter and run your
query.

After you run a query, a **Result** tab appears
with the results. Here is where you can turn on
**Chart** to visualize your results. You can
also **Export** your results.

- A
  ![The icon in the AWS Console where you can add sections to enter and run SQL or add Markdown.](images/add-plus.png)

**Notebook** area where you can add sections to
enter and run SQL or add Markdown.

After you run a query, a **Result** tab appears
with the results. Here is where you can **Export**
your results.

**Queries
![A folder icon used in the AWS Console used to query databases.](images/qev2-folder-close.png)**

A query contains the SQL commands to manage and query your data in a
database. When you use query editor v2 to load sample data, it also creates and saves
sample queries for you.

When you choose a saved query, you can open, rename, and delete it using the
context (right-click) menu. You can view attributes such as the
**Query ARN** of a saved query by choosing
**Query details**. You can also view its version
history, edit tags attached to the query, and share it with your
team.

**Notebooks
![A book icon used in the AWS Console used as SQL notebook.](images/qev2-manual.png)**

A SQL notebook contains SQL and Markdown cells. Use notebooks to organize,
annotate, and share multiple SQL commands in a single document.

When you choose a saved notebook, you can open, rename, duplicate, and
delete it using the context (right-click) menu. You can view attributes such
as the **Notebook ARN** of a saved notebook by choosing
**Notebook details**. You can also view its version
history, edit tags attached to the notebook, export it, and share it with
your team. For more information, see [Notebooks in Amazon Redshift](query-editor-v2-notebooks.md "query-editor-v2-notebooks.md").

**Charts
![Icon of a chart used in the AWS Console as visual representation of data.](images/qev2-chart.png)**

A chart is a visual representation of your data. The query editor v2 provides the
tools to create many types of charts and save them.

When you choose a saved chart, you can open, rename, and delete it using the
context (right-click) menu. You can view attributes such as the
**Chart ARN** of a saved chart by choosing
**Chart details**. You can also edit tags attached to
the chart and export it. For more information, see [Visualizing query results](query-editor-v2-charts.md "query-editor-v2-charts.md").

**History
![Icon of a clock used in the AWS Console for query history.](images/qev2-clock.png)**

The query history is a list of queries you ran using Amazon Redshift query editor v2. These
queries either ran as individual queries or as part of a SQL notebook. For
more information, see [Viewing query and tab history](query-editor-v2-history.md "query-editor-v2-history.md").

**Scheduled queries
![Icon of a calendar used in the AWS Console for scheduled queries.](images/qev2-calendar.png)**

A scheduled query is a query that is set up to start at specific
times.

All query editor v2 views have the following icons:

- A
  ![Icon of a quarter moon used in the AWS Console to switch between light and dark modes.](images/qev2-moon.png)

**Visual mode** icon to toggle between light mode and dark
mode.

- A
  ![Icon of a gear used in the AWS Console to show settings.](images/qev2-cog.png)

**Settings** icon to show a menu of the different settings
screens.

    + An
    ![Icon used in the AWS Console to show editor preferences.](images/qev2-properties.png)

    **Editor preferences** icon to edit your preferences
     when you use query editor v2. Here you can **Edit workspace
     settings** to change font size, tab size, and other display
     settings.

     You can also turn on (or off) **Autocomplete** to show
     suggestions as you enter your SQL.
    + A
    ![Icon used in the AWS Console to view connections used in the editor tab.](images/qev2-connection.png)

    **Connections** icon to view the connections used by
     your editor tabs.


    A connection is used to retrieve data from a database. A connection is
     created for a specific database. With an isolated connection, the
     results of a SQL command that changes the database, such as creating a
     temporary table, in one editor tab, are not visible in another editor
     tab. When you open an editor tab in query editor v2, the default is an isolated
     connection. When you create a shared connection, that is, turn off the
     **Isolated session** switch, then the results in
     other shared connections to the same database are visible to each other.
     However, editor tabs using a shared connection to a database don't run
     in parallel. Queries using the same connection must wait until the
     connection is available. A connection to one database can't be shared
     with another database, and thus SQL results are not visible across
     different database connections.


    The number of connections any user in the account can have active is
     controlled by a query editor v2 administrator.
    + An
    ![Icon used in the AWS Console used by administrators to change settings of user accounts.](images/qev2-settings.png)

    **Account settings** icon used by an administrator to
     change certain settings of all users in the account. For more
     information, see [Account settings](#query-editor-v2-settings "#query-editor-v2-settings").

## Considerations when working with

query editor v2

Consider the following when working with query editor v2.

- The maximum duration of a query is 24 hours.
- The maximum query result size is 100 MB. If a call returns more than 100 MB of response data, the first 100 MB is returned with a warning.
- You can run a query up to 300,000 characters long.
- You can save a query up to 30,000 characters long.
- By default, query editor v2 auto-commits each individual SQL command that runs.
  When a BEGIN statement is provided, statements within BEGIN-COMMIT or
  BEGIN-ROLLBACK block are run as a single transaction.
  For more information
  about transactions, see [BEGIN](../dg/r_BEGIN.md "../dg/r_BEGIN.md")
  in the _Amazon Redshift Database Developer Guide._
- The maximum number of warnings that query editor v2 displays while running a SQL
  statement is `10`. For example, when a stored procedure is run,
  no more than 10 RAISE statements are displayed.
- The query editor v2 doesn't support an IAM `RoleSessionName` that
  contains commas (,). You might see an error similar to the following:
  **`Error Message : "'AROA123456789EXAMPLE:mytext,yourtext' is
not a valid value for TagValue - it contains illegal
characters"`** This issue arises when you define an IAM
  `RoleSessionName` that includes a comma and then use query editor v2
  with that IAM role.

For more information about an IAM `RoleSessionName`, see
[RoleSessionName SAML attribute](../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md#saml_role-session-attribute "../../../IAM/latest/UserGuide/id_roles_providers_create_saml_assertions.md#saml_role-session-attribute") in the
_IAM User Guide_.

## Account settings

A user with the right IAM permissions can view and change **Account
settings** for other users in the same AWS account. This
administrator can view or set the following:

- The maximum concurrent database connections per user in the account. This
  includes connections for **Isolated sessions**. When you
  change this value, it can take 10 minutes for the change to take
  effect.
- Allow users in the account to export an entire result set from a SQL
  command to a file.
- Load and display sample databases with some associated saved
  queries.
- Specify an Amazon S3 path used by account users to load data from a local
  file.
- View the KMS key ARN used to encrypt query editor v2 resources.

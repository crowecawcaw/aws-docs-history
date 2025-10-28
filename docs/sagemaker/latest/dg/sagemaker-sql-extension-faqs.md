# Frequently asked questions

The following FAQs answer common general questions for the SQL extension in JupyterLab.

A: The SQL extension writes its log in the general log file of your JupyterLab
application in Studio. You can find those logs at
`/var/log/apps/app_container.log`.

A: Create a new cell and load the extension again using `%load_ext
 amazon_sagemaker_sql_magic`.

A: Use `%%sm_sql?` to get the help content of the command.

A: Ensure that your space uses a SageMaker distribution image version 1.6 or higher. These
SageMaker images come pre-installed with the extension.

If you updated the image of your JupyterLab application space in Studio, refresh
your browser.

A: Try refreshing the right panel using the **Refresh** button in the
bottom right corner of the SQL extension UI in your notebook.

A: Try clearing the cached connections by running the following magic command
`%sm_sql_manage --clear-cached-connections`.

A: The SQL extension only supports running one SQL query at a time.

## Snowflake FAQs

The following FAQs answer common general questions for users of the SQL extension using
Snowflake as their data source.

A: This can happen if the default warehouse for a user is not selected. Run the
command `USE WAREHOUSE `warehouse_name`` for each
session.

A: Ensure that your Snowflake user has access to the given object.

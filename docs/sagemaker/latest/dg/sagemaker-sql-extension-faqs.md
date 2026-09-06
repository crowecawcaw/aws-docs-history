

# Frequently asked questions
<a name="sagemaker-sql-extension-faqs"></a>

The following FAQs answer common general questions for the SQL extension in JupyterLab.

## Q: Where do I find the logs for the SQL extension?
<a name="sagemaker-sql-extension-faqs-0"></a>

A: The SQL extension writes its log in the general log file of your JupyterLab application in Studio. You can find those logs at `/var/log/apps/app_container.log`.

## Q: I am getting an error: “UsageError: Cell magic `%%sm\_sql` not found.”
<a name="sagemaker-sql-extension-faqs-1"></a>

A: Create a new cell and load the extension again using `%load_ext amazon_sagemaker_sql_magic`.

## Q: How do I list the various parameters of my `%%sm_sql` command?
<a name="sagemaker-sql-extension-faqs-2"></a>

A: Use `%%sm_sql?` to get the help content of the command.

## Q: I cannot see the data discovery view on the right side panel.
<a name="sagemaker-sql-extension-faqs-3"></a>

A: Ensure that your space uses a SageMaker distribution image version 1.6 or higher. These SageMaker images come pre-installed with the extension. 

If you updated the image of your JupyterLab application space in Studio, refresh your browser.

## Q: The right panel does not accurately reflect the AWS Glue connections that are configured.
<a name="sagemaker-sql-extension-faqs-4"></a>

A: Try refreshing the right panel using the **Refresh** button in the bottom right corner of the SQL extension UI in your notebook.

## Q: SQL statements do not run as expected or run incorrectly.
<a name="sagemaker-sql-extension-faqs-5"></a>

A: Try clearing the cached connections by running the following magic command `%sm_sql_manage --clear-cached-connections`.

## Q: I am getting an error: "Actual statement count 2 did not match the desired statement count 1."
<a name="sagemaker-sql-extension-faqs-6"></a>

A: The SQL extension only supports running one SQL query at a time.

## Snowflake FAQs
<a name="sagemaker-sql-extension-faqs-snowflake"></a>

The following FAQs answer common general questions for users of the SQL extension using Snowflake as their data source.

### Q: I am getting an error: "No active warehouse selected in the current session." Select an active warehouse with the 'use warehouse' command.
<a name="sagemaker-sql-extension-faqs-snowflake-1"></a>

A: This can happen if the default warehouse for a user is not selected. Run the command `USE WAREHOUSE {{warehouse_name}}` for each session.

### Q: I am getting an error: "object '{{foo}}' does not exist or not authorized."
<a name="sagemaker-sql-extension-faqs-snowflake-2"></a>

A: Ensure that your Snowflake user has access to the given object.
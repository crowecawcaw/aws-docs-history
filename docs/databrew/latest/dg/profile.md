# Creating a profile job using a ruleset

After you create a ruleset as described preceding, you are directed to the
**Data quality rules** page, which displays all rulesets in
your account.

###### To create a profile job including a ruleset

1. Choose the name of the ruleset that you previously created to view its details.
2. Choose **Create profile job with ruleset**.

The **Job name** is automatically filled, but you can
change it as needed. 3. For **Job run sample**, you can choose to run the entire dataset or a limited
number of rows.

If you choose to run a limited sample size, be aware that for certain rules, results might differ compared to the full dataset. 4. For **Job output settings**, choose an **S3** location for
the job output. Choose any folder in a named Amazon S3 bucket that you have
access to. If you enter a folder name for this bucket that doesn't
exist, this folder is created.

Upon successful completion of the profile job, this folder will contain profiles of the data and data quality rules validation report in JSON format. 5. Under **Data quality rules**, note your ruleset is listed under **Data quality ruleset
name**. 6. Under **Permissions**, select or create a role to grant DataBrew access to read
from the input Amazon S3 location and write to the job output location. If
you don't have a role ready, select **Create new IAM
role**. 7. Modify any other optional settings as described in [Creating and working with AWS Glue DataBrew profile jobs](jobs.md "jobs.md"), if needed. 8. Choose **Create and run job**.

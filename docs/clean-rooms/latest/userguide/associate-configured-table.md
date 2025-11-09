# Associating a configured table to a

collaboration

After you have created a configured table and added an analysis rule to it, you can
associate it to a collaboration and give AWS Clean Rooms a service role to access your AWS Glue tables.

###### Note

This service role has permissions to the tables. The service role is assumable only by
AWS Clean Rooms to run allowed queries on behalf of the member who can query. No collaboration
members (other than the data owner) have access to the underlying tables in the collaboration.
The data owner can turn on differential privacy to make their tables available for querying by
other members.

## Data access budget

When you associate a configured table, you can apply a data access budget. A _data access budget_ controls how many times a table can be used for
queries, jobs, and ML input channels in a collaboration. These budgets help organizations manage
resource utilization and control costs by limiting table use.

Each time a table is used in a query, job, or ML input channel, the budget for that table is
reduced by one. When the budget reaches zero, the table can't be used in SQL queries, Pyspark
jobs, nor as part of ML input channels derived from the table.

You can establish a per period budget that refreshes periodically, a lifetime budget for
overall usage, or both. By default, table usage is unlimited.

- Per period budget – A renewable allocation that limits the amount of times this
  table can be used within a specified time period. You can set the period to daily, weekly,
  or monthly. This budget can be set to automatically refresh on a daily, weekly, or monthly
  basis.
- Lifetime budget – A running allocation that limits the total amount of times this
  table can be used.

## Associate a configured table

The following topics describe how to associate a configured table and apply a data access
budget to a collaboration using the AWS Clean Rooms
console.

For information about how to associate your configured tables to the collaboration using
the AWS SDKs, see the [_AWS Clean Rooms API
Reference_](../apireference/Welcome.md "../apireference/Welcome.md").

### Step 1: Complete the prerequisites

To associate a configured table, you must complete the following prerequisites:

- An AWS Glue table that points to an Amazon S3 folder location (not a single file)
- For encrypted AWS Glue tables:
  - A service role with permissions to use AWS KMS keys for decrypting AWS Glue
    tables
  - For AWS KMS-encrypted Amazon S3 datasets: The service role must also have permissions
    to use the AWS KMS key to decrypt Amazon S3 data

For information about configuring encryption, see [Setting up encryption in
AWS Glue](../../../glue/latest/dg/set-up-encryption.md "../../../glue/latest/dg/set-up-encryption.md") in the _AWS Glue Developer Guide_.

To verify your AWS Glue table location:

1. Open the AWS Glue console at [https://console.aws.amazon.com/glue/](https://console.aws.amazon.com/glue/ "https://console.aws.amazon.com/glue/")
2. View your table details and confirm the location points to an S3 folder

### Step 2: Associate a configured table

###### To associate a configured table

1. Sign in to the AWS Management Console and open the AWS Clean Rooms console at [https://console.aws.amazon.com/cleanrooms](https://console.aws.amazon.com/cleanrooms/home "https://console.aws.amazon.com/cleanrooms/home").
2. Choose the method to associate your table:
   1. From the configured table detail page:
      1. In the left navigation pane, choose **Tables**.
      2. Choose the configured table.
      3. On the configured table detail page, choose **Associate to
         collaboration**.
      4. For the **Associate table to collaboration** dialog box,
         choose the **Collaboration** from the dropdown list.

   2. From the collaboration detail page:
      1. In the left navigation pane, choose
         **Collaborations**.
      2. Choose the collaboration.
      3. On the **Tables** tab, choose **Associate
         table**.

3. On the **Associate table** page, do one of the following:
   - Choose an existing configured table – Choose the **Configured
     table name** that you want to associate with the collaboration from the
     dropdown list.
   - Configure a new table – Choose **Configure new table**
     and follow the prompts on the **Configure new table** page.
   - View the schema and analysis rule for the configured table – Turn on
     **View schema and analysis rule**.

4. For **Table association details**,
   1. Enter a **Name** for the associated table.

   You can use the default name or rename this table. 2. (Optional) Enter a **Description** of the table.

   The description helps with writing queries.

5. Specify the **Service access** permissions by selecting either
   **Create and use a new service role** or **Use an existing
   service role**.

###### Note

If you are associating a configured table backed by Amazon Athena, choose an
**Existing service role name** from the dropdown list. Ensure the
service role has IAM and, if needed, Lake Formation permissions to the dataset.

| If you choose...                      | Then ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Create and use a new service role** | • AWS Clean Rooms creates a service role with the required policy for this<br>table.<br>• The default **Service role name** is<br>`cleanrooms-<timestamp>`<br>• You must have permissions to create roles and attach policies.<br>• If your input data is encrypted, you can select **This data is<br>encrypted with a KMS key** and then enter an AWS KMS key<br>that will be used to decrypt your data input.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Use an existing service role**      | 1. Choose an **Existing service role name\*<br>• from the<br>dropdown list.<br>The list of roles are displayed if you have permissions to list<br>roles.<br>If you don't have permissions to list roles, you can enter the Amazon<br>Resource Name (ARN) of the role that you want to use.<br>2. View the service role by choosing the **View in<br>IAM*<br>• external link.<br>If there are no existing service roles, the option to \*\*Use an<br>existing service role*<br>• is unavailable.<br>By default, AWS Clean Rooms doesn't attempt to update the existing role policy<br>to add necessary permissions.<br>3. (Optional) Select the \*_Add a pre-configured policy with<br>necessary permissions to this role_<br>• check box to add attach<br>necessary permissions to the role. You must have permissions to modify<br>roles and create policies. |

###### Note

    * AWS Clean Rooms requires permissions to query according to the analysis rules. For
     more information about permissions for AWS Clean Rooms, see [AWS managed policies for AWS Clean Rooms](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
    * If the role doesn’t have sufficient permissions for AWS Clean Rooms, you receive an
     error message stating that the role doesn't have sufficient permissions for
     AWS Clean Rooms. The role policy must be added before proceeding.
    * If you can’t modify the role policy, you receive an error message stating that
     AWS Clean Rooms couldn't find the policy for the service role.

6. If you want to enable **Configured table association tags** for the
   configured table association resource, choose **Add new tag** and then
   enter the **Key** and **Value** pair.
7. Choose **Next**.
8. On the **Configure collaboration analysis rule** page, choose one
   of the following:
   - **Yes, create a collaboration analysis rule now** –
     Associates your table with this collaboration and creates a collaboration analysis
     rule
   - **No, I will create a collaboration analysis rule later**
     – Associates your table with this collaboration only. You can create a
     collaboration analysis rule later.

9. If you choose **Yes, create a collaboration analysis rule now**,
   for **Results delivery**, choose the **Members allowed to
   receive results for query output** from the dropdown list.
10. Choose **Next**.
11. On the **Add data access budget** page, for **Data access
    budget configuration**, choose one of the following:
    - **Yes, add a data access budget now** – Associates your
      table with this collaboration and adds a data access budget. You can select either a
      period budget, a lifetime budget, or both.
    - **No, I will add a data access budget later** –
      Associates your table with this collaboration only. You can add a data access budget
      later.

    If you select **No, I will add a data access budget later**,
    skip to step 15.

12. If you choose **Yes, add a data access budget now**, choose one of
    the following budget configurations:

| Per period budget only                                                                                                                                                                                                                                                                                                                           | Lifetime budget only                                                                                                                                | Both per period and lifetime budgets                                                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Leave **Add per period budget**<br>selected.<br>2. Enter a **Per period budget amount\*<br>• between 1 and<br>1,000,000.<br>3. For **Period**, choose **Daily**,<br>**Weekly**, or **Monthly**.<br>4. (Optional) Leave **Automatically refresh budget<br>weekly\*<br>• selected to renew the allocation.<br>5. Clear **Add lifetime budget**. | 1. Clear **Add per period budget**.<br>2. Select **Add lifetime budget**.<br>3. Enter a \*_Lifetime budget amount_<br>• between 1 and<br>1,000,000. | 1. Leave **Add per period budget\*<br>• selected.<br>2. Enter a **Per period budget amount*<br>• between 1 and<br>1,000,000.<br>3. For **Period**, choose **Daily**,<br>**Weekly**, or **Monthly**.<br>4. Leave **Automatically refresh budget weekly**<br>selected.<br>5. Select **Add lifetime budget**.<br>6. Enter a \*\*Lifetime budget amount*<br>• between 1 and<br>1,000,000. |

13. Review your selections under **Data access budget summary**.

###### Example

For example, if you've chosen a **Per period budget amount** of
1,000, set the **Period** to **Weekly**, left the
**Automatically refresh budget weekly** checkbox
selected, and set the **Lifetime budget** to 1,000,000, then the
**Access budget summary** will display the following message: Every
week, this table can be used up to 1,000 times for running queries or jobs. This
budget is set to automatically refresh every Sunday at 00:00 UTC, and will continue to
refresh until this table has reached its lifetime budget of 1,000,000 uses. 14. (Optional) If you want to enable **Data access budget tags** for
the access budget resource, choose **Add new tag** and enter a Key and
Value pair. 15. Choose **Next**. 16. Review the information on the **Review and create** page.

    1. If you need to edit any sections, choose **Edit**.
    2. Edit your configurations, and then choose **Next**.

17. Choose **Associate table**.

### Step 3: Next steps

Now that you associated your configured data table to the collaboration, you are ready
to:

- [Add a collaboration analysis
  rule](add-collaboration-analysis-rule.md "add-collaboration-analysis-rule.md") to the configured table
- [Edit the collaboration](edit-collaboration.md "edit-collaboration.md"), if you're the
  collaboration creator
- [Query the data tables](running-sql-queries.md "running-sql-queries.md") (as a member who
  can query)

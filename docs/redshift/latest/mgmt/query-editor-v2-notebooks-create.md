Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a notebook

You can create a notebook to organize, annotate, and share multiple SQL queries in a
single document.

###### To create a notebook

1. From the navigator menu, choose the Editor icon (
   ![Horizontal lines representing redacted or censored text.](images/qev2-align-left.png)
   ).
2. Choose the plus icon (
   ![Plus sign icon representing an addition or new item action.](images/add-plus.png)
   ), and then choose **Notebook**.

By default, a SQL query cell appears in the notebook. 3. In the SQL query cell, do one of the following:

    * Enter a query.
    * Paste a query that you copied.

4. (Optionally) Choose the plus icon (
   ![Plus sign icon representing an addition or new item action.](images/add-plus.png)
   ), then choose **Markdown** to add a
   Markdown cell where you can provide descriptive or explanatory text using
   standard Markdown syntax.
5. (Optionally) Choose the plus icon (
   ![Plus sign icon representing an addition or new item action.](images/add-plus.png)
   ), then choose **SQL** to insert a SQL
   cell.
   You can rename notebooks using the pencil icon (
   ![Pencil icon representing an editing or writing function.](images/qev2-edit.png)
   ).

From the menu icon (
![Three dots arranged horizontally, representing an ellipsis or "more" menu icon.](images/qev2-more.png)
), you can also perform the following operations on a
notebook:

- ![Share](images/qev2-share.png)

**Share with my team** – To share the notebook with your
team as defined by tags. To share a notebook with your team, make sure that you
have the principal tag `sqlworkbench-team` set to the same value as
the rest of your team members in your account. For example, an administrator
might set the value to `accounting-team` for everyone in the
accounting department. For an example, see [Permissions
required to use the query editor v2](redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2 "redshift-iam-access-control-identity-based.md#redshift-policy-resources.required-permissions.query-editor-v2") .

- ![Export](images/qev2-export.png)

**Export** – To export the notebook to a local file with
the `.ipynb` extension.

- ![Import query](images/qev2-import.png)

**Import query** – To import a query from a local file
into a cell in the notebook. You can import files with `.sql` and
`.txt` extensions.

- ![Save](/images/redshift/latest/mgmt/images/qev2-floppy-disk.png)

**Save version** – To create a version of the notebook.
To see versions of a notebook, navigate to your saved notebooks and open
**Version history**.

- ![Duplicate](images/qev2-duplicate.png)

**Duplicate** – To create a copy of the notebook and
open it in a new notebook tab.

- ![Shortcuts](images/qev2-key-command.png)

**Shortcuts** – To display the shortcuts available when
authoring a notebook.

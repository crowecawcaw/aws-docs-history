Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Notebooks in Amazon Redshift

You can use notebooks to organize, annotate, and share multiple SQL queries in a single
document. You can add multiple SQL query and Markdown cells to a notebook. Notebooks provide
a way to group queries and explanations associated with a data analysis in a single document
by using multiple query and Markdown cells. You can add text and format the appearance using
Markdown syntax to provide context and additional information for your data analysis tasks.
You can share your notebooks with team members.

To use notebooks, you must add permission for notebooks to your IAM principal (an IAM
user or IAM role). As a best practice, we recommend attaching permissions policies to an IAM role and then assigning it to users and groups as
needed. For more information, see [Identity and access management in Amazon Redshift](redshift-iam-authentication-access-control.md "redshift-iam-authentication-access-control.md"). You can add the permission to one of the query editor v2
managed policies. For more information, see [Accessing the query editor v2](query-editor-v2-getting-started.md#query-editor-v2-configure "query-editor-v2-getting-started.md#query-editor-v2-configure").

You can run all the cells of a notebook sequentially. The SQL query cell of a notebook has
most of the same capabilities as a query editor tab. For more information, see [Authoring queries with Amazon Redshift](query-editor-v2-query-run.md "query-editor-v2-query-run.md"). The
following are differences between a query editor tab and a SQL cell in a notebook.

- There isn't a control to run `Explain` on a SQL statement in a
  notebook.
- You can create only one chart per SQL cell in a notebook.
  You can export and import notebooks to files created with query editor v2. The file extension is
  `.ipynb` and the file size can be a maximum of 5 MB. The SQL and Markdown
  cells are stored in the file. A cluster or workgroup and database is not stored in the
  exported notebook. When you open an imported notebook you choose the cluster or workgroup
  and the database where to run it. After running SQL cells, you can then choose in the
  results tab whether to display the current page of results as a chart. The result set of a
  query is not stored in the notebook.

For a demo of notebooks, watch the following video.

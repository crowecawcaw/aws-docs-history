# Create a query

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to a project that uses the **SQL analytics** or **Data
   analytics and AI-ML model development** project profile. You can do this by using the
   center menu at the top of the page and choosing **Browse all projects**, then
   choosing the name of the project that you want to navigate to.
3. In the **Build** menu, choose **Query editor**. This
   takes you to the Query editor page.
4. To start writing a query, choose the + icon at the top of the editor window to create a
   new tab. This creates a new querybook with an empty SQL cell.
5. Write the query in the given SQL cell. For a guide to SQL commands you can use, see [SQL
   reference](../../../redshift/latest/dg/cm_chap_SQLCommandRef.md "../../../redshift/latest/dg/cm_chap_SQLCommandRef.md") in the Amazon Redshift Database Developer Guide or the [SQL
   reference](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md") for Amazon Athena.
6. (Optional) To create more space for writing commands, add another SQL or markdown cell to
   the notebook.
   To run a query, choose the **Run** icon to run queries in a specific cell,
   or choose **Run all** at the top of the editor window to run all queries on the
   page. A query runs until it is finished or until you use the **Stop**
   button.

After running a query, save the SQLNB file to the project to share it with other project
members. The steps are as follows:

1. Expand the **Actions** menu and choose **Save to
   project**.
2. Confirm the action by choosing **Save changes**.

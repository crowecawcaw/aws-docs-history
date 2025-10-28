# Work with Athena views

Athena views can be easily created, updated, and managed in the Athena console.

## Create views

You can create a view in the Athena console by using a template or by running an
existing query.

###### To use a template to create a

view

1. In the Athena console, next to **Tables and views**, choose
   **Create**, and then choose **Create
   view**.

![Creating a view.](images/create-view.png)

This action places an editable view template into the query editor. 2. Edit the view template according to your requirements. When you enter a name
for the view in the statement, remember that view names cannot contain special
characters other than underscore `(_)`. See [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md"). Avoid using [Escape reserved keywords in queries](reserved-words.md "reserved-words.md") for naming views.

For more information about creating views, see [CREATE VIEW and CREATE PROTECTED MULTI
DIALECT VIEW](create-view.md "create-view.md") and [Examples of Athena views](views-examples.md "views-examples.md"). 3. Choose **Run** to create the view. The view appears in the
list of views in the Athena console.

###### To create a view from an existing query

1. Use the Athena query editor to run an existing query.
2. Under the query editor window, choose **Create**, and then
   choose **View from query**.

![Choose Create, View from query.](images/create-view-from-query.png) 3. In the **Create View** dialog box, enter a name for the view,
and then choose **Create**. View names cannot contain special
characters other than underscore `(_)`. See [Name databases, tables, and columns](tables-databases-columns-names.md "tables-databases-columns-names.md"). Avoid using [Escape reserved keywords in queries](reserved-words.md "reserved-words.md") for naming
views.

Athena adds the view to the list of views in the console and displays the
`CREATE VIEW` statement for the view in the query editor.

###### Notes

- If you delete a table on which a table is based and then attempt to run the
  view, Athena displays an error message.
- You can create a nested view, which is a view on top of an existing view.
  Athena prevents you from running a recursive view that references itself.

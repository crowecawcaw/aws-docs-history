# Using tree filters in AWS Schema Conversion Tool

To migrate data from a source to a target, AWS SCT loads all metadata
from source and target databases into a tree structure. This structure appears in
AWS SCT as the tree view in the main project window.

Some databases can have a large number of objects in the tree structure. You can use
_tree filters_ in AWS SCT to search for objects in
the source and target tree structures. When you use a tree filter, you don't change
the objects that are converted when you convert your database. The filter changes only
what you see in the tree.

Tree filters work with objects that AWS SCT has preloaded. In other words, AWS SCT
doesn't load objects from the database during searches. This approach means that
the tree structure generally contains fewer objects than are present in the
database.

For tree filters, keep the following in mind:

- The filter default is ANY, which means that the filter uses a name search to
  find objects.
- When you select one or more object types, you see only those types of objects
  in the tree.
- You can use the filter mask to show different types of symbols, including
  Unicode, spaces, and special characters. The “%” character is the wildcard for
  any symbol.
- After you apply a filter, the count shows only the number of filtered
  objects.

###### To create a tree filter

1. Open an existing AWS SCT project.
2. Connect to the database that you want to apply the tree filter to.
3. Choose the filter icon.

![The filter icon for the schema tree](images/filter-source-tree.png)

The undo filter icon is grayed out because no filter is currently
applied. 4. Enter the following information in the **Filter** dialog box. Options in
the dialog box are different for each database engine.

| AWS SCT filter option | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Level**             | Choose **Categories\*<br>• to filter objects by categories.<br>Choose **Statuses\*<br>• to filter objects by statuses.                                                                                                                                                                                                                                                                                                                                                     |
| **Type**              | For **Categories\*<br>• in **Level**, choose the categories of filtered objects.<br>Choose **Any loaded*<br>• to display objects from all categories.<br>For \*\*Statuses*<br>• in<br>**Level**, choose the status of<br>filtered objects. You can choose one of the following<br>options:<br>• **Converted** to display all converted objects<br>• **Has actions** to display all objects that have conversion issues<br>• **Encrypted** to display all encrypted objects |
| **Condition**         | For **Categories\*<br>• in **Level**, choose the filtering condition<br>between **Like*<br>• and **Not like**.<br>For \*\*Statuses*<br>• in **Level**, the filtering condition option<br>isn't available.                                                                                                                                                                                                                                                                  |
| **Value**             | For **Categories\*<br>• in **Level**, enter the<br>**Value*<br>• to filter the tree by<br>this value.<br>Use the percent (`%`) as a wildcard to display all objects.<br>For \*\*Statuses*<br>• in **Level**, choose the **Value**<br>between **True\*<br>• and **False\*\*.                                                                                                                                                                                                |
| **And/Or**            | Choose `AND` or `OR` logical operators to apply multiple filter clauses.                                                                                                                                                                                                                                                                                                                                                                                                   |

![The filter icon for the schema tree](images/filter-tree-db.png) 5. Choose **Add new clause** to add an additional filter clause. AWS SCT can
apply multiple filter clauses using `AND` or `OR`
logical operators. 6. Choose **Apply**. After you choose **Apply**, the undo
filter icon (next to the filter icon) is enabled. Use this icon if you want
to remove the filters you applied. 7. Choose **Close** to close the dialog box.
When you filter the schema that appears in the tree,
you don't change the objects that are converted when you convert your schema.
The filter only changes what you see in the tree.

## Importing a file list for the tree filter

You can import a comma-separated value (CSV) file with semicolon separators
or a JSON file that contains names or values that you want the tree filter to use.
Open an existing AWS SCT project, connect to the database to apply the tree filter to,
and then choose the filter icon.

To download an example of the file, choose **Download
template**. Enter the file name and choose **Save**.

To download your existing filter settings, choose **Export**.
Enter the file name and choose **Save**.

To import a file list for the tree filter, choose **Import**.
Choose a file to import, and then choose **Open**.
Choose **Apply**, and then choose **Close**.

CSV files use semicolon as the separator and have the following format:

- `object_type` is the type of object that you want to find.
- `database_name` is the name of database where this object exists.
- `schema_name` is the name of schema where this object exists.
- `object_name` is the object name.
- `import_type` specifies to `include` or `exclude` this item
  from the filter.

Use JSON files to describe complex filtering cases, such as nested rules. JSON
files have the following format:

- `filterGroupType` is the type of filter rule (`AND` or `OR`
  logical operators) that applies to multiple filter clauses.
- `filterCategory` is the level of the filter (**Categories**
  or **Statuses**).
- `names` is the list of object names that applies for the
  **Categories** filter.
- `filterCondition` is the filtering condition (`LIKE`
  or `NOT LIKE`) that applies for the **Categories** filter.
- `transformName` is the status name that applies for the
  **Status** filter.
- `value` is the value to filter the tree by.
- `transformValue` is the value of the filter (`TRUE` or
  `FALSE`) that applies for the **Status** filter.

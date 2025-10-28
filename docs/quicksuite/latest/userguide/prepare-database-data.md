# Preparing a dataset based on database

data

Use the following procedure to prepare a dataset based on a query to a database. The
data for this dataset can be from an AWS database data source like Amazon Athena, Amazon RDS,
or Amazon Redshift, or from an external database instance. You can choose whether to import a copy
of your data into [SPICE](spice.md "spice.md"), or to query the
data directly.

###### To prepare a dataset based on a query to a database

1. Open a database dataset for preparation by choosing one of the following
   options:
   - Create a new database dataset and choose **Edit/Preview
     data**. For more information about creating a new dataset
     using a new database data source, see [Creating a dataset from a database](../../../quicksight/latest/user/create-a-database-data-set.md "../../../quicksight/latest/user/create-a-database-data-set.md"). For
     more information about creating a new dataset using an existing database
     data source, see [Creating a dataset using an existing database
     data source](../../../quicksight/latest/user/create-a-data-set-existing-database.md "../../../quicksight/latest/user/create-a-data-set-existing-database.md").
   - Open an existing database dataset for editing from either the analysis
     page or the **Your Datasets** page. For more
     information about opening an existing dataset for data preparation, see
     [Editing datasets](../../../quicksight/latest/user/edit-a-data-set.md "../../../quicksight/latest/user/edit-a-data-set.md").

2. (Optional) On the data preparation page, enter a name into the dataset name
   box on the application bar.

This name defaults to the table name if you selected one before data
preparation. Otherwise, it's `Untitled data
 source`. 3. Decide how your data is selected by choosing one of the following:

    * To use a single table to provide data, choose a table or change the
     table selection.


    If you have a long table list in the **Tables** pane,
     you can search for a specific table by typing a search term for
     **Search tables**.


    Any table whose name contains the search term is shown. Search is
     case-insensitive and wildcards are not supported. Choose the cancel icon
     (**X**) to the right of the search box to return to
     viewing all tables.
    * To use two or more joined tables to provide data, choose two tables
     and join them using the join pane. You must import data into
     Quick Sight if you choose to use joined tables. For more information
     about joining data using the Amazon Quick Sight interface, see [Joining data](../../../quicksight/latest/user/joining-data.md "../../../quicksight/latest/user/joining-data.md").
    * To use a custom SQL query to provide data in a new dataset, choose
     **Switch to Custom SQL** tool on the
     **Tables** pane. For more information, see [Using SQL to customize data](../../../quicksight/latest/user/adding-a-SQL-query.md "../../../quicksight/latest/user/adding-a-SQL-query.md").


    To change the SQL query in an existing dataset, choose **Edit
     SQL** on the **Fields** pane to open the
     SQL pane and edit the query.

4. Prepare the data by doing one or more of the following:
   - [Selecting fields](../../../quicksight/latest/user/selecting-fields.md "../../../quicksight/latest/user/selecting-fields.md")
   - [Editing field names and
     descriptions](../../../quicksight/latest/user/changing-a-field-name.md "../../../quicksight/latest/user/changing-a-field-name.md")
   - [Changing a field data type](../../../quicksight/latest/user/changing-a-field-data-type.md "../../../quicksight/latest/user/changing-a-field-data-type.md")
   - [Adding calculated fields](../../../quicksight/latest/user/adding-a-calculated-field-analysis.md "../../../quicksight/latest/user/adding-a-calculated-field-analysis.md")
   - [Filtering data in Quick Sight](../../../quicksight/latest/user/adding-a-filter.md "../../../quicksight/latest/user/adding-a-filter.md")

5. If you aren't joining tables, choose whether to query the database directly or
   to import the data into SPICE by selecting either the
   **Query** or **SPICE**
   radio button. We recommend using SPICE for enhanced performance.

If you want to use SPICE, check the SPICE
indicator to see if you have enough space to import the dataset. Importing
occurs when you choose either **Save & visualize** or
**Save**.

If you don't have enough space, you can remove fields from the dataset or
apply a filter to decrease its size.

###### Note

The SPICE indicator doesn't update to reflect the potential
savings of removing fields or filtering the data. It continues to reflect
the size of the dataset as retrieved from the data source. 6. Choose **Save** to save your work, or
**Cancel** to cancel it.

You might also see an option to **Save & visualize**.
This option appears based on the screen you started from. If this option isn't
there, you can create a new visualization by starting from the dataset screen.

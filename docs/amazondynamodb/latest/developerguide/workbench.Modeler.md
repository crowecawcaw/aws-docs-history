# Importing sample data from a CSV

file

If you have preexisting sample data in a CSV file, you can import it into NoSQL Workbench. This enables you to quickly populate your model with sample data without having to enter it line by line.

The column names in the CSV file must match the attribute names in your data model,
but they do not need to be in the same order. For example, if your data model has
attributes called `LoginAlias`, `FirstName`, and
`LastName`, your CSV columns could be `LastName`,
`FirstName`, and `LoginAlias`.

You can import up to 150 rows at a time from a CSV file.

###### To import data from a CSV file into NoSQL Workbench

1. To import CSV data to a **Table**, first click the table name in the resource panel, and then click the additional actions (three-dot icon) in the main content toolbar.
2. Select **Import sample data**.
3. Select your CSV file and choose **Open**. The CSV data appends to your table.

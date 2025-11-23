# Saving and applying converted schemas in AWS SCT

When the AWS Schema Conversion Tool generates converted schema
(as shown in ), it doesn't immediately apply
the converted schema to the target DB instance. Instead, converted schema are stored
locally in your project until you are ready to apply them to the target DB instance.
Using this functionality, you can work with schema items that can't be
converted automatically to your target DB engine.

For more information on items that can't be
converted automatically, see
[Using the assessment report in the AWS Schema Conversion Tool](CHAP_AssessmentReport.md "CHAP_AssessmentReport.md").

You can optionally have the tool save your converted schema to a file as a SQL script prior to
applying the schema to your target DB instance. You can also have the tool apply the converted schema
directly to your target DB instance.

## Saving your converted schema to a file

You can save your converted schema as SQL scripts in a text file. By using this approach, you can
modify the generated SQL scripts from AWS SCT to address items that the tool can't
convert automatically. You can then run your updated scripts on your target DB instance to
apply your converted schema to your target database.

###### To save your converted schema as SQL scripts

1. Choose your schema and open the context (right-click) menu.
2. Choose **Save as SQL**.
3. Enter the name of the file and choose **Save**.
4. Save your converted schema using one of the following options:
   - **Single file**
   - **Single file per stage**
   - **Single file per statement**

###### To choose the format of the SQL script

1. On the **Settings** menu, choose **Project
   settings**.
2. Choose **Save scripts**.
3. For **Vendor**, choose the database platform.
4. For **Save SQL scripts to**, choose how you want to save
   your database schema script.
5. Choose **OK** to save the settings.

## Applying your converted schema

When you are ready to apply your converted schema to your target Amazon RDS DB instance,
choose the schema element from the right panel of your project. Open the context
(right-click) menu for the schema element, and then choose **Apply to
database**, as shown following.

![Apply to database](images/write_to_database.png)

## The extension pack schema

The first time that you apply your converted schema to your target DB instance,
AWS SCT adds an additional schema to your target DB instance.
This schema implements system functions of the source database that are required when
writing your converted schema to your target DB instance.
The schema is called the extension pack schema.

Don't modify the extension pack schema,
or you might encounter unexpected results in the
converted schema that is written to your target DB instance.
When your schema is fully migrated to your target DB instance,
and you no longer need AWS SCT,
you can delete the extension pack schema.

The extension pack schema is named according to your source database as follows:

- IBM Db2 LUW: `aws_db2_ext`
- Microsoft SQL Server: `aws_sqlserver_ext`
- MySQL: `aws_mysql_ext`
- Oracle: `aws_oracle_ext`
- PostgreSQL: `aws_postgresql_ext`
- SAP ASE: `aws_sapase_ext`

For more information, see
[Using the AWS Lambda functions from the AWS SCT extension
pack](CHAP_ExtensionPack.md#CHAP_ExtensionPack.OLTP "CHAP_ExtensionPack.md#CHAP_ExtensionPack.OLTP") .



# Converting schemas using AWS SCT
<a name="CHAP_Converting.Convert"></a>

After you have connected your project to both your source database and your target Amazon RDS DB instance, your AWS Schema Conversion Tool project displays the schema from your source database in the left panel. The schema is presented in a tree-view format, and each node of the tree is lazy loaded. When you choose a node in the tree view, AWS SCT requests the schema information from your source database at that time. 

You can choose schema items from your source database and then convert the schema to equivalent schema for the DB engine of your target DB instance. You can choose any schema item from your source database to convert. If the schema item that you choose depends on a parent item, then AWS SCT also generates the schema for the parent item. For example, suppose that you choose a table to convert. If so, AWS SCT generates the schema for the table, and the database that the table is in. 

## Converting schema
<a name="CHAP_Converting.Convert.Procedure"></a>

To convert a schema from your source database, select the check box for the name of schema to convert. Next, choose this schema from the left panel of your project. AWS SCT highlights the schema name in blue. Open the context (right-click) menu for the schema, and choose **Convert schema**, as shown following.

![Convert schema](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/transform_schema.png)


After you have converted the schema from your source database, you can choose schema items from the left panel of your project and view the converted schema in the center panels of your project. The lower-center panel displays the properties of and the SQL command to create the converted schema, as shown following. 

![Choose source schema item](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/select_schema_item.png)


After you have converted your schema, you can save your project. The schema information from your source database is saved with your project. This functionality means that you can work offline without being connected to your source database. AWS SCT connects to your source database to update the schema in your project if you choose **Refresh from Database** for your source database. For more information, see [Updating and refreshing converted schemas in AWS SCT](CHAP_Converting.UpdateRefresh.md). 

You can create a database migration assessment report of the items that can't be converted automatically. The assessment report is useful for identifying and resolving schema items that can't be converted automatically. For more information, see [Using the assessment report in the AWS Schema Conversion Tool](CHAP_AssessmentReport.md). 

When AWS SCT generates a converted schema, it doesn't immediately apply it to the target DB instance. Instead, the converted schema is stored locally until you are ready to apply it to the target DB instance. For more information, see [Applying your converted schema](CHAP_Converting.SaveAndApply.md#CHAP_Converting.Applying). 

## Editing converted schema
<a name="CHAP_Converting.Edit"></a>

You can edit converted schema and save the changes as part of your project.

**To edit converted schema**

1. In the left panel that displays the schema from your source database, choose the schema item that you want to edit the converted schema for. 

1. In the lower-center panel that displays the converted schema for the selected item, choose the **SQL** tab. 

1. In the text displayed for the **SQL** tab, change the schema as needed. The schema is automatically saved with your project as you update it.   
![Refresh the schema from the target DB instance](http://docs.aws.amazon.com/SchemaConversionTool/latest/userguide/images/edit_converted_schema.png)

The changes that you make to converted schema are stored with your project as you make updates. If you newly convert a schema item from your source database, and you have made updates to previously converted schema for that item, those existing updates are replaced by the newly converted schema item based on your source database. 

## Clearing a converted schema
<a name="CHAP_Converting.Clear"></a>

Until you apply the schema to your target DB instance, AWS SCT only stores the converted schema locally in your project. You can clear the planned schema from your project by choosing the tree-view node for your DB instance, and then choosing **Refresh from Database**. Because no schema has been written to your target DB instance, refreshing from the database removes the planned schema elements in your AWS SCT project to match what exists in your source DB instance. 
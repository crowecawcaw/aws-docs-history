# Applying migration rules in AWS Schema Conversion Tool

Before you convert your schema with AWS SCT, you can set up migration rules.
_Migration rules_ in AWS SCT can do such transformations as change the data type of columns, move objects from one schema to another,
and change the names of objects. For example, suppose that you have a set of tables in
your source schema named `test_TABLE_NAME`. You can set up a rule that
changes the prefix `test_` to the prefix `demo_` in the target
schema.

###### Note

You can only create migration rules for different source and target database engines.

You can create migration rules that perform the following tasks:

- Add, remove, or replace a prefix
- Add, remove, or replace a suffix
- Change column collation
- Change data type
- Change the length of `char`, `varchar`,
  `nvarchar`, and `string` data types
- Move objects
- Rename objects
  You can create migration rules for the following objects:

- Database
- Schema
- Table
- Column

## Creating migration rules

You can create migration rules and save the rules as part of your project.
With your project open, use the following procedure to create migration rules.

###### To create migration rules

1. On the **View** menu, choose **Mapping
   view**.
2. In **Server mappings**, choose a pair of source and target servers.
3. Choose **New migration rule**.
   The **Transformation rules** dialog box appears.
4. Choose **Add new rule**.
   A new row is added to the list of rules.
5. Configure your rule:
   1. For **Name**, enter a name for your rule.
   2. For **For**,
      choose the type of object that the rule applies to.
   3. For **where**, enter a filter to apply to objects
      before applying the migration rule. The where clause is evaluated by
      using a like clause. You can enter an exact name to select one
      object, or you can enter a pattern to select multiple objects.

   The fields available for the **where** clause
   are different depending on the type of the object.
   For example, if the object type is schema
   there is only one field available, for the schema name. 4. For **Actions**, choose the type of migration
   rule that you want to create. 5. Depending on the rule type, enter one or two additional values.
   For example, to rename an object, enter the new name of the object.
   To replace a prefix, enter the old prefix and the new prefix.

   For char, varchar, nvarchar, and string data types, you can change
   the data type length using the multiplication operator. For example,
   the `%*4` value transforms the `varchar(10)`
   data type into `varchar(40)`.

6. After you have configured your migration rule,
   choose **Save** to save your rule.
   You can also choose **Cancel** to cancel your changes.

![The transformation rules dialog box](images/transformation-rules.png) 7. After you are done adding, editing, and deleting rules,
choose **Save All** to save all your changes. 8. Choose **Close**
to close the **Transformation rules** dialog box.

You can use the toggle icon
to turn off a migration rule without deleting it.
You can use the copy icon
to duplicate an existing migration rule.
You can use the pencil icon
to edit an existing migration rule.
You can use the delete icon
to delete an existing migration rule.
To save any changes
you make to your migration rules,
choose **Save All**.

## Exporting migration rules

If you use AWS DMS to migrate your data from your source database to your target
database, you can provide information about your migration rules to AWS DMS. For more
information about tasks, see [Working with
AWS Database Migration Service replication tasks](../../../dms/latest/userguide/CHAP_Tasks.md "../../../dms/latest/userguide/CHAP_Tasks.md").

###### To export migration rules

1. In the AWS Schema Conversion Tool, choose **Mapping View** on the
   **View** menu.
2. In **Migration rules**, choose a migration rule and then choose
   **Modify migration rule**.
3. Choose **Export script for AWS DMS**.
4. Browse to the location where you want to save your script,
   and then choose **Save**.
   Your migration rules are saved as a JSON script
   that can be consumed by AWS DMS.

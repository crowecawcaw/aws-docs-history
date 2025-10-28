# Virtual data provider

AWS Database Migration Service (DMS) offers Virtual Mode for data providers in schema
conversion. This feature allows you to perform schema conversion without connecting to a
target database, reducing infrastructure costs and providing flexibility for migration
planning. With Virtual Mode, you can start conversion work immediately to plan optimal
migration strategy before committing resources. You can evaluate compatibility, convert and
review schema code, and even test different target options. Then you can connect to a
database when you are ready. Virtual Mode supports all target databases compatible with
AWS DMS Schema Conversion, including MySQL, PostgreSQL, Amazon Redshift, and Amazon RDS
for Db2.

## Create virtual data provider

To create a virtual data provider, simply enable Virtual Mode in the form for creating the data provider. For more information, see [Configure your data providers for DMS Schema Conversion](getting-started-data-providers.md "getting-started-data-providers.md").

## Virtual data provider usage

To use a virtual data provider, create a new migration project or modify an existing
migration project. Then set the project's target data provider to the virtual data
provider you've created.

To use a virtual provider for the Secret and IAM role for reading that secret's
fields, use any secret that is granted to the IAM role to successfully setup the
migration project.

After target provider is set, choose the **Schema conversion** tab.
Then choose the **Launch schema conversion** button. Wait until the
project is started.

You can now use schema conversion with the virtual target data provider just as you
would with a real target data provider. Actions that require connection to a real target
database will be disabled, but **Save as SQL** will be available for
the target tree.

## Transition from a virtual

data provider to a real data provider

When you are ready to proceed with the actual migration, you can make the transition
to a real data provider .

###### To transition from a virtual data provider to a real data provider, follow these

steps.

1. Sign in to the AWS Management Console, and open the AWS DMS console.
2. In the navigation pane, choose **Data providers**. Then
   choose the data provider you wish to modify.
3. Go to the section **Associated migration projects** , to see
   all the migration projects using this virtual data provider.
4. Choose the first associated project.
5. Choose the **Schema conversion** tab.
6. Check the option **Details section** -
   **Status**.
7. If the status is **Open** and the button **Close
   schema conversion** is not greyed out, choose it and wait until the
   project is closed.
8. Repeat the previous steps for all remaining associated migration
   projects.
9. Confirm that there are no remaining open projects.
10. Return to the data provider and choose **Modify**.
11. Turn **Virtual Mode** off.
12. Fill the connection settings correctly. The connection parameters depend on
    your database engine. For more information, see [Creating data providers](data-providers-create.md "data-providers-create.md").
13. Choose **Save changes**.

###### Note

After changes have been saved, it won't be possible to turn Virtual Mode
back to on. 14. Return to the AWS DMS console. 15. In the navigation pane, choose **Migration Projects**. Then
choose the migration project you want to change the data provider for. 16. Choose **Modify**. 17. Fill the Secret to be used to connect to target data provider. Use the correct
secret, containing the credentials needed to connect to the database. 18. Fill the IAM role to use to read the target secret. Check that the IAM role
specified here is correct, is granted read on the connection credentials secret,
and is available to AWS DMS Schema Conversion service. 19. Choose **Save changes**. 20. Choose **Schema conversion** tab. 21. Choose **Launch schema conversion** button. 22. Wait until the project is started.

###### Important

Once you disable Virtual Mode and save this change the data provider, this action
cannot be undone. You will be required to provide actual database connection details
for the data provider, and working Secret and IAM role to access the Secret in the
associated migration project.

On the very first start of the project containing the transited data provider, you
will have conversion results. Only these actions will be available:

- **On node schemas** - Refresh from database.
- **On database objects** - Apply changes, then save as SQL.

The **Apply** action will apply converted objects to the real database.

The **Refresh from database** action loads database objects from the real database. Any unsaved conversion objects will be lost.

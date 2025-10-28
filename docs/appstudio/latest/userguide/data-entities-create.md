# Creating an entity in an App Studio app

There are four methods for creating an entity in an App Studio app. The following list contains each method, its benefits, and a link to the instructions for using
that method to create and then configure the entity.

- [Creating an entity from an existing data source](#data-entities-create-existing-data-source "#data-entities-create-existing-data-source"):
  Automatically create an entity and its fields from an existing data source table and map the fields to the data source table columns.
  This option is preferable if you have an existing data source that you want to use in your App Studio app.
- [Creating an entity with an App Studio managed data source](#data-entities-create-managed-data-source "#data-entities-create-managed-data-source"):
  Create an entity and a DynamoDB table that App Studio manages for you. The DynamoDB table is automatically updated as you update your entity.
  With this option, you don't have to manually create, manage, or connect a third-party data source, or designate mapping from entity fields to table columns. All of your
  app's data modeling and configuration is done in App Studio. This
  option is preferable if you don't want to manage your own data sources and a DynamoDB table and its functionality is sufficient for your app.
- [Creating an empty entity](#data-entities-create-empty "#data-entities-create-empty"): Create an empty entity entirely from scratch.
  This option is preferable if you don't have any existing data sources or connectors created by an admin, and you want to flexibly design your app's data model without
  being constrained by external data sources. You can connect the entity to a data source after creation.
- [Creating an entity with AI](#data-entities-create-with-ai "#data-entities-create-with-ai"): Generate an entity, fields, data actions,
  and sample data based on the specified entity name. This option is preferable if you have an idea of the data model
  for your app, but you want help translating it into an entity.

## Creating an entity from an existing data source

Use a table from a data source to automatically create an entity and its fields, and map
the entity fields to the columns of the table. This option is preferable if you have an existing data source that you want to use in your App Studio app.

1. If necessary, navigate to your application.
2. Choose the **Data** tab at the top of the canvas.
3. If there are no entities in your app, choose **+ Create entity**.
   Otherwise, in the left-side **Entities** menu, choose **+ Add**.
4. Select **Use a table from an existing data source**.
5. In **Connector**, select the connector that contains the table you want to use to create your entity.
6. In **Table**, choose the table you want to use to create your entity.
7. Select the **Create data actions** checkbox to create data actions.
8. Choose **Create entity**. Your entity is now created, and you can see it in the left-hand **Entities** panel.
9. Configure your new entity by following the procedures in [Configuring or editing an entity in an App Studio app](data-entities-edit.md "data-entities-edit.md"). Note that because your
   entity was created with an existing data source, some properties or resources have already been created, such as fields, the connected data source, and field mapping. Also, your
   entity will contain data actions if you selected the **Create data actions** checkbox during creation.

## Creating an entity with an App Studio managed data source

Create a managed entity and corresponding DynamoDB table that is managed by App Studio. While the DynamoDB table exists in the associated AWS account, when changes
are made to the entity in the App Studio app, the DynamoDB table is updated automatically. With this option, you don't have to manually create, manage, or connect a third-party data source, or designate mapping from entity fields to table columns. This
option is preferable if you don't want to manage your own data sources and a DynamoDB table and its functionality is sufficient for your app.
For more information about managed entities, see [Managed data entities in AWS App Studio](managed-data-entities.md "managed-data-entities.md").

You can use the same managed entities in multiple applications. For instructions, see
[Creating an entity from an existing data source](#data-entities-create-existing-data-source "#data-entities-create-existing-data-source").

1. If necessary, navigate to your application.
2. Choose the **Data** tab at the top of the canvas.
3. If there are no entities in your app, choose **+ Create entity**.
   Otherwise, in the left-side **Entities** menu, choose **+ Add**.
4. Select **Create App Studio managed entity**.
5. In **Entity name**, provide a name for your entity.
6. In **Primary key**, provide a name for the primary key of your entity. The primary key is the unique identifier of the entity and
   cannot be changed after the entity is created.
7. In **Primary key data type**, select the data type of primary key of your entity. The data type cannot be changed after the
   entity is created.
8. Choose **Create entity**. Your entity is now created, and you can see it in the left-hand **Entities** panel.
9. Configure your new entity by following the procedures in [Configuring or editing an entity in an App Studio app](data-entities-edit.md "data-entities-edit.md"). Note that because your
   entity was created with managed data, some properties or resources have already been created, such as the primary key field, and the connected data source.

## Creating an empty entity

Create an empty entity entirely from scratch. This option is preferable if you don't have any existing data sources or connectors created by an admin. Creating an empty
entity offers flexibility, as you can design your entity within your App Studio app without being constrained by external data sources. After you design your app's
data model, and configure the entity accordingly, you can still connect it to an external data source later.

1. If necessary, navigate to your application.
2. Choose the **Data** tab at the top of the canvas.
3. If there are no entities in your app, choose **+ Create entity**.
   Otherwise, in the left-side **Entities** menu, choose **+ Add**.
4. Select **Create an entity**.
5. Choose **Create entity**. Your entity is now created, and you can see it in the left-hand **Entities** panel.
6. Configure your new entity by following the procedures in [Configuring or editing an entity in an App Studio app](data-entities-edit.md "data-entities-edit.md").

## Creating an entity with AI

Generate an entity, fields, data actions, and sample data based on the specified entity name. This option is preferable if you have an idea of the data model
for your app, but you want help translating it into an entity.

1. If necessary, navigate to your application.
2. Choose the **Data** tab at the top of the canvas.
3. If there are no entities in your app, choose **+ Create entity**.
   Otherwise, in the left-side **Entities** menu, choose **+ Add**.
4. Select **Create an entity with AI**.
5. In **Entity name**, provide a name for your entity. This name is used to generate the fields, data actions, and sample data of your entity.
6. Select the **Create data actions** checkbox to create data actions.
7. Choose **Generate an entity**. Your entity is now created, and you can see it in the left-hand **Entities** panel.
8. Configure your new entity by following the procedures in [Configuring or editing an entity in an App Studio app](data-entities-edit.md "data-entities-edit.md"). Note that because your
   entity was created with AI, your entity will already contain generated fields. Also, your
   entity will contain data actions if you selected the **Create data actions** checkbox during creation.

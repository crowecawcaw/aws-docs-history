# Managed data entities in AWS App Studio

Typically, you configure an entity in App Studio with a connection to an external database table, and you must create and map each entity field with
a column in the connected database table. When you make a change to the data model, both the external database table and the entity must be updated, and the changed fields
must be remapped. While this method is flexible and enables the use of different types of data sources, it takes more up-front planning and
ongoing maintenance.

A _managed entity_ is a type of entity for which App Studio manages the entire data storage and configuration process for you. When you create a
managed entity, a corresponding DynamoDB table is created in the associated AWS account. This ensures secure and transparent data management within AWS. With a
managed entity, you configure the entity's schema in App Studio, and the corresponding DynamoDB table is automatically updated as well.

## Using managed entities in multiple applications

Once you create a managed entity in an App Studio app, that entity can be used in other App Studio apps. This is helpful for configuring data storage for apps
with identical data models and schemas by providing a single underlying resource to maintain.

When using a managed entity in multiple applications, all schema updates to the corresponding DynamoDB table must be made using the original application
in which the managed entity was created. Any schema changes made to the entity in other applications will not update the corresponding DynamoDB table.

## Managed entity limitations

**Primary key update restrictions**: You cannot change the entity's primary key name or type after
it is created, as this is a destructive change in DynamoDB, and would result in loss of existing data.

**Renaming columns**: When you rename a column in DynamoDB, you actually create a
new column while the original column remains with original data. The original data is not automatically copied to the
new column or deleted from the original column. You can rename managed entity fields, known as the _system name_, but you
will lose access to the original column and its data. There is no restriction with renaming the display name.

**Changing data type**: Though DynamoDB allows flexibility to
modify column data types after table creation, such changes can severely impact existing data as well as
query logic and accuracy. Data type changes require transforming all existing data to conform to the new
format, which is complex for large, active tables. Additionally, data actions may return unexpected results until
data migration is complete. You can switch data types of fields, but the existing data will not be migrated to the new data type.

**Sorting Column**: DynamoDB enables sorted data retrieval
through Sort Keys. Sort Keys must be defined as part of composite Primary Keys along with the Partition
Key. Limitations include mandatory Sort Key, sorting confined within one partition, and no global sorting
across partitions. Careful data modeling of Sort Keys is required to avoid hot partitions. We will not be
supporting Sorting for Preview milestone.

**Joins**: Joins are not supported in DynamoDB.
Tables are denormalized by design to avoid expensive join operations. To model one-to-many relationships,
the child table contains an attribute referencing the parent table's primary key. Multi-table data queries
involve looking up items from the parent table to retrieve details. We will not be supporting native Joins
for Managed entities as part of the Preview milestone. As a workaround, we will introduce an automation step
that can perform a data merge of 2 entities. This will be very similar to a one level look-up. We will not be
supporting Sorting for Preview milestone.

**Env Stage**: We will allow publishing to test but use
the same managed store across both environments

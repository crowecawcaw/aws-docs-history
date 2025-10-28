# Creating, editing, or deleting data actions

Data actions are used in applications to run actions
on an entity's data, such as fetching all records, or fetching a record by ID. Data actions can be used to locate and return data matching specified conditions to
be viewed in components such as tables or detail views.

###### Contents

- [Creating data actions](data-entities-edit-data-actions.md#data-entities-data-action-add "data-entities-edit-data-actions.md#data-entities-data-action-add")
- [Editing or configuring data actions](data-entities-edit-data-actions.md#data-entities-data-action-edit "data-entities-edit-data-actions.md#data-entities-data-action-edit")
- [Data action condition operators and examples](data-entities-edit-data-actions.md#data-entities-data-action-operators "data-entities-edit-data-actions.md#data-entities-data-action-operators")
  - [Condition operator support by database](data-entities-edit-data-actions.md#data-entities-data-action-operators-support "data-entities-edit-data-actions.md#data-entities-data-action-operators-support")
  - [Data action condition examples](data-entities-edit-data-actions.md#data-entities-data-action-operators-examples "data-entities-edit-data-actions.md#data-entities-data-action-operators-examples")

- [Deleting data actions](data-entities-edit-data-actions.md#data-entities-data-action-delete "data-entities-edit-data-actions.md#data-entities-data-action-delete")

## Creating data actions

###### Tip

You can press CTRL+Z to undo the most recent change to your entity.

1. If necessary, navigate to the entity for which you want to create data actions.
2. Choose the **Data actions** tab.
3. There are two methods for creating data actions:
   - (Recommended) To use AI to generate data actions for you, based on your entity name, fields, and connected data source,
     choose **Generate data actions**. The following actions will be generated:
     1. `getAll`: Retrieves all the records from an entity.
        This action is useful when you need to display a list of records or perform operations on multiple records at once.
     2. `getByID`: Retrieves a single record from an entity based on its unique identifier (ID or primary key).
        This action is useful when you need to display or perform operations on a specific record.

   - To add a single data action, choose **+ Add data action**.

4. To view or configure the new data action, see the following section,
   [Editing or configuring data actions](#data-entities-data-action-edit "#data-entities-data-action-edit").

## Editing or configuring data actions

1. If necessary, navigate to the entity for which you want to create data actions.
2. Choose the **Data actions** tab.
3. In **Fields** configure the fields to be returned by the query. By default, all
   of the configured fields in the entity are selected.

You can also add **Joins** to the data action
by performing the following steps:

    1. Choose  **+ Add Join** to open a dialog box.
    2. In **Related entity**, select the entity you want to join with the current entity.
    3. In **Alias**, optionally enter a temporary alias name for the related entity.
    4. In **Join type**, select the desired join type.
    5. Define the join clause by selecting the fields from each entity.
    6. Choose **Add** to create the join.

Once created, the join will be displayed in the **Joins** section, making additional fields
available in the **Fields to Return** dropdown. You can add multiple joins,
including chained joins across entities. You can also filter and sort by fields from joined entities.

To delete a join, choose the trash icon next to it. This will remove any fields from that join and break any dependent joins or constraints using those fields. 4. In **Conditions**, add, edit, or remove rules that filter the output of the
query. You can organize rules into groups, and you can chain together multiple rules with `AND` or
`OR` statements. For more information about the operators you can use, see
[Data action condition operators and examples](#data-entities-data-action-operators "#data-entities-data-action-operators"). 5. In **Sorting**, configure how the query results are sorted by choosing an
attribute and choosing ascending or descending order. You can remove the sorting configuration by choosing the trash icon next to the
sorting rule. 6. In **Transform results**, you can enter custom JavaScript to modify or format results
before they are displayed or sent to automations. 7. In **Output preview**, view a preview table of the query output based on the
configured fields, filters, sorting, and JavaScript.

## Data action condition operators and examples

You can use condition operators to compare a configured expression value with an entity column to return a subset of database
objects. The operators that you can use depend on on the data type of the column, and the type of database that the entity is connected to, such as Amazon Redshift, Amazon Aurora, or Amazon DynamoDB.

The following condition operators can be used with all database services:

- `=` and `!=`: Available for all data types (excluding primary key columns).
- `<=`, `>=`, `<`, and `>=`: Available only to numerical columns.
- `IS NULL` and `IS NOT NULL`: Used to match columns that
  have null or empty values. Null values are often interpreted differently in each database, however in App Studio,
  the `NULL` operator matches and returns records that have null values in the connected database table.

The following condition operators can only be used in entities that are connected to database services that support them:

- `LIKE` and `NOT LIKE`(Redshift, Aurora): Used for performing pattern-based queries in the connected database. The
  `LIKE` operator provides flexibility in search functionality because it finds and returns records that fit the specified patterns.
  You define the patterns using wildcard characters that match any character or sequence of characters within
  the pattern. Each database management system has a unique set of wildcard characters, but the two most popular are `%` to represent any number of
  characters (including 0), and `_` to represent a single character.
- `Contains` and `Not Contains` (DynamoDB): Used for performing a case-sensitive
  search to determine whether the given text is found within the column values.
- `Starts With` and `Not Starts With` (DynamoDB): Used for performing a case-sensitive
  search to determine whether the given text is found at the beginning of the column values.

### Condition operator support by database

The following table shows which data action condition operators are supported by each database that can
connect to App Studio.

|              | =, !=, <, >, <=, >= | LIKE, NOT LIKE | Contains, Not Contains | Starts With, Not Starts With | IS NULL, IS NOT NULL |
| ------------ | ------------------- | -------------- | ---------------------- | ---------------------------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **DynamoDB** | Yes                 | No             | Yes                    | Yes                          | Yes                  |
| **Aurora**   | Yes                 | Yes            | No                     | No                           | Yes                  |
| **Redshift** | Yes                 | Yes            | No                     | No                           | Yes                  | ### Data action condition examples Consider the following database table, which includes multiple items with `name`, `city`, and `hireDate` fields. |
| name         | city                | hireDate       |                        | ---                          | ---                  | ---                                                                                                                                                 |
| Adam         | Seattle             | 2025-03-01     |                        | Adrienne                     | Boston               | 2025-03-05                                                                                                                                          |
| Bob          | Albuquerque         | 2025-03-06     |                        | Carlos                       | Chicago              | 2025-03-10                                                                                                                                          |
| Caroline     | NULL                | 2025-03-12     |                        | Rita                         | Miami                | 2025-03-15                                                                                                                                          | Now, consider creating data actions in App Studio that return the `name` field for items that match specified conditions. The following list contains condition examples and the values that the table returns for each. ###### Note The examples are formatted as SQL examples– they may not appear as they do in App Studio, but are used to illustrate the behavior of the operators. <br>• `WHERE name LIKE 'Adam'`: Returns `Adam`. <br>• `WHERE name LIKE 'A%'`: Returns `Adam` and `Adrienne`. <br>• `WHERE name NOT LIKE 'B_B'`: Returns `Adam`, `Adrienne`, `Carlos`, `Caroline`, and `Rita`. <br>• `WHERE contains(name, 'ita')`: Returns `Rita`. <br>• `WHERE begins_with(name, 'Car')`: Returns `Carlos` and `Caroline`. <br>• `WHERE city IS NULL`: Returns `Caroline`. <br>• `WHERE hireDate < "2025-03-06"`: Returns `Adam` and `Adrienne`. <br>• `WHERE hireDate >= DateTime.now().toISODate()`: Note that `DateTime.now().toISODate()` returns the current date. In a scenario where the current date is 2025-03-10, the expression returns `Carlos`, `Caroline`, and `Rita`. ###### Tip For more information about comparing dates and times in expressions, see [Date and time](expressions.md#expressions-date-time "expressions.md#expressions-date-time"). ## Deleting data actions Use the following procedure to delete data actions from an App Studio entity. 1. If necessary, navigate to the entity for which you want to delete data actions. 2. Choose the **Data actions** tab. 3. For each data action you want to delete, choose the dropdown menu next to **Edit** and choose **Delete**. 4. Choose **Confirm** in the dialog box. |

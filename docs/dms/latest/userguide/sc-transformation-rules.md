# Transformation rules in DMS Schema Conversion

_Transformation rules_ let you customize how DMS Schema Conversion
converts your database objects, overriding default naming and data type
mappings. You can apply these rules to databases, schemas, tables, views,
columns, function return values, routine parameters, and local
variables.

For example, suppose that you have a set of tables in your source schema named
`test_TABLE_NAME`. You can set up a rule that changes the prefix
`test_` to the prefix `demo_` in the target
schema.

You can create transformation rules that perform the following tasks:

- Add, remove, or replace a prefix
- Add, remove, or replace a suffix
- Change the data type of a column, function return value, routine
  parameter, or local variable
- Convert the object name to lowercase or uppercase
- Rename an object

## Creating transformation rules

DMS Schema Conversion stores transformation rules as part of your migration project. To
define transformation rules, pass them as a JSON string that contains an object
with a `rules` array when you create or modify a migration project.
Each element in the array represents a separate rule object. A migration
project supports up to 512 transformation rules (128 KB maximum).

The structure of the array with transformation rules is as follows:

```
{
  "rules": [
    {
      `Rule object 1`
    },
    {
      `Rule object 2`
    },
    ...
    {
      `Rule object N`
    }
  ]
}
```

You can add multiple transformation rules in your project. DMS Schema Conversion applies
transformation rules during conversion in the same order as you added them.

If multiple rules target the same object, the behavior depends on the
action type. Rules with different action types all take effect. For example,
an `add-prefix` rule and an `add-suffix` rule both
apply. Rules with the same action type override each other, and only the last one
takes effect.

To create transformation rules, use one of the following methods.

AWS Management Console

###### To create transformation rules using the console

1. On the **Create migration project** page, choose
   **Add transformation rule**. For more information, see
   [Creating migration projects](migration-projects-create.md "migration-projects-create.md").
2. For **Rule target**, choose the type of database objects
   that this rule applies to. The console wizard supports
   `schema`, `table`, and
   `column` targets. To use other targets such as
   `database` or `view`, use the
   JSON editor in the console or the AWS CLI.
3. For **Source schema**, choose **Enter a
   schema**. Then, specify the source schemas, tables,
   and columns to which this rule applies. You can use an exact name to
   select one object, or use a pattern with the percent sign (%) as a
   wildcard to match any number of characters.
4. For **Action**, choose the task to perform.
5. Depending on the rule action, enter additional
   values:

   - `add-prefix` or `add-suffix` –
     Enter the text to add.
   - `remove-prefix` or `remove-suffix` –
     Enter the text to remove.
   - `replace-prefix` or `replace-suffix` –
     Enter the existing text and the replacement text.
   - `rename` – Enter the new name for the
     object.
   - `convert-uppercase` or
     `convert-lowercase` – No additional values
     required.
   - `change-data-type` – Enter the target data
     type name, and optionally the precision, scale, or
     length.

6. Choose **Add transformation rule** to add another
   transformation rule.

After you are done adding rules, choose **Create migration
project**.

AWS CLI
To add transformation rules using the AWS CLI, use the
`--transformation-rules` parameter with one of the
following commands:

- [create-migration-project](../../../cli/latest/reference/dms/create-migration-project.md "../../../cli/latest/reference/dms/create-migration-project.md") – When creating a new migration project.
- [modify-migration-project](../../../cli/latest/reference/dms/modify-migration-project.md "../../../cli/latest/reference/dms/modify-migration-project.md") – For an existing migration project.

The following example adds transformation rules to an existing
migration project:

```
aws dms modify-migration-project \
  --migration-project-identifier `migration_project_arn` \
  --transformation-rules '`json_rules`'
```

To run this command in a specific AWS Region, add the
`--region` parameter, for example
`--region us-west-2`.

To edit, duplicate, or remove existing transformation rules, see [Editing
transformation rules](#sc-transformation-rules-edit "#sc-transformation-rules-edit").

## Retrieving transformation rules

You can retrieve transformation rules from an existing DMS Schema Conversion migration
project using the AWS Management Console or the AWS CLI.

AWS Management Console
To view the transformation rules using the AWS Management Console, choose
**Modify** on an existing migration project and review the
list of existing rules in the **Transformation rules**
section.

AWS CLI
To retrieve transformation rules from an existing DMS Schema Conversion migration project,
use the [describe-migration-projects](../../../cli/latest/reference/dms/describe-migration-projects.md "../../../cli/latest/reference/dms/describe-migration-projects.md") command.
The response uses JSON format and includes the transformation rules
associated with the project.

The following AWS CLI example retrieves transformation rules from a migration
project:

```
aws dms describe-migration-projects \
  --filters Name=migration-project-identifier,Values=`migration_project_arn`
```

## Editing transformation rules

To edit, add, or remove transformation rules in your migration project, use
one of the following methods.

AWS Management Console

###### To edit transformation rules

1. Choose **Migration projects**, and then choose your
   migration project.
2. Choose **Modify**
   to edit your migration project settings.
3. For **Transformation rules**, choose one of the following
   actions:

   - Choose **Add transformation rule** to add a new
     transformation rule.
   - Choose **Duplicate** to duplicate an existing
     transformation rule and add it at the end of the list.
   - Choose **Remove** to remove an existing
     transformation rule.
   - Choose the existing transformation rule to edit it.

4. After you are done editing rules, choose **Save
   changes**.

AWS CLI
To update transformation rules using the AWS CLI, use the
[modify-migration-project](../../../cli/latest/reference/dms/modify-migration-project.md "../../../cli/latest/reference/dms/modify-migration-project.md") command with the
`--transformation-rules` parameter. Pass the complete
updated set of rules as a JSON string.

```
aws dms modify-migration-project \
  --migration-project-identifier `migration_project_arn` \
  --transformation-rules '`json_rules`'
```

## Transformation rule format

A transformation rule uses JSON object fields to define how to convert a source
object into its target equivalent. Each rule type uses a specific set of fields.
Include only the fields that apply to your task.

The following JSON object describes a DMS Schema Conversion transformation rule:

```
{
  "rule-type": "transformation",
  "rule-id": `rule_id`,
  "rule-name": "`rule_name`",
  "rule-action": "`rule_action`",
  "rule-target": "`rule_target`",
  "object-locator": {
    [ "database-name": "`database_name`", ]
    [ "schema-name": "`schema_name`", ]
    [ "table-name": "`table_name`", ]
    [ "view-name": "`view_name`", ]
    [ "column-name": "`column_name`", ]
    [ "parent": "`parent_name`", ]
    [ "function-name": "`function_name`", ]
    [ "procedure-name": "`procedure_name`", ]
    [ "parameter-name": "`parameter_name`", ]
    [ "local-variable-name": "`local_variable_name`", ]
    [ "type": "`source_data_type`", ]
    [ "precision": `source_precision`, ]
    [ "scale": `source_scale`, ]
    [ "length": `source_length` ]
  },
  [ "value": "`rule_value`", ]
  [ "old-value": "`rule_old_value`", ]
  [ "data-type": {
    "type": "`data_type_name`",
    [ "precision": `data_type_precision`, ]
    [ "scale": `data_type_scale`, ]
    [ "length": `data_type_length` ]
  } ]
}
```

The following table describes each parameter.

| Parameter        | Possible values                                                                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rule-type`      | `transformation`                                                                                                                                                                        | A value that applies the rule to each object specified<br>by the object locator.<br>For all transformation rules, set this to<br>`transformation`.<br>Required parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `rule-id`        | A numeric (integer) value.                                                                                                                                                              | A unique numeric value to identify the rule.<br>Required parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `rule-name`      | An alphanumeric value.                                                                                                                                                                  | A unique name to identify the rule.<br>Required parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| `rule-action`    | `add-prefix`, `remove-prefix`,<br>`replace-prefix`, `add-suffix`,<br>`remove-suffix`, `replace-suffix`,<br>`convert-uppercase`,<br>`convert-lowercase`, `rename`,<br>`change-data-type` | The transformation you want to apply to the object. All<br>transformation rule actions are case-sensitive.<br>Prefix operations:<br>• `add-prefix` – Add a specified text to<br>the beginning of a name.<br>• `remove-prefix` – Remove a specified<br>text from the beginning of a name.<br>• `replace-prefix` – Replace an existing<br>prefix with a new one.<br>Suffix operations:<br>• `add-suffix` – Add a specified text to<br>the end of a name.<br>• `remove-suffix` – Remove a specified<br>text from the end of a name.<br>• `replace-suffix` – Replace an existing<br>suffix with a new one.<br>Case conversion:<br>• `convert-uppercase` – Convert all<br>characters in a name to uppercase.<br>• `convert-lowercase` – Convert all<br>characters in a name to lowercase.<br>Direct modification:<br>• `rename` – Change the name to a<br>completely new specified value.<br>• `change-data-type` – Modify the data<br>type of a column or local variable to a different<br>data type.<br>Scope: prefix, suffix, rename, and case conversion<br>operations can be applied to schemas, tables, and<br>columns.<br>The `change-data-type` operation applies only<br>to columns, function return values, routine parameters,<br>and local variables.<br>Required parameter. |
| `rule-target`    | `database`, `schema`,<br>`table`, `view`,<br>`column`, `function result`,<br>`routine parameter`, `local<br>variable`                                                                   | The type of object to which the rule will be<br>applied.<br>• `database` – Database.<br>• `schema` – Database schema.<br>• `table` – Database table.<br>• `view` – Database view.<br>• `column` – Database table or view<br>column.<br>• `function result` – Function return<br>value.<br>• `routine parameter` – Stored procedure<br>or function parameter.<br>• `local variable` – Local variable<br>within stored procedure or function.<br>Required parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `object-locator` | A JSON object.                                                                                                                                                                          | An object that identifies which source<br>database objects the rule applies to. You can use<br>the percent sign (`%`) as a wildcard for all or<br>part of the value in each `object-locator` object<br>field.<br>The object contains the following string fields:<br>• `database-name`<br>• `schema-name`<br>• `table-name`<br>• `view-name`<br>• `column-name`<br>• `parent`<br>• `function-name`<br>• `procedure-name`<br>• `parameter-name`<br>• `local-variable-name`<br>• `type`<br>• `precision`<br>• `scale`<br>• `length`<br>All object names, such as table or column names, in<br>transformation rules are case-sensitive.<br>The following sections describe each object<br>field.<br>Required parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `object-locator  | database-name`                                                                                                                                                                          | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database.<br>This field applies only to Microsoft SQL Server and<br>SAP ASE source engines, where the database is the<br>top-level container above the schema.<br>Optional JSON object field.                                                                                                                                                      |
| `object-locator  | schema-name`                                                                                                                                                                            | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database schema.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                                    |
| `object-locator  | table-name`                                                                                                                                                                             | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database table.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                                     |
| `object-locator  | view-name`                                                                                                                                                                              | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database view. Use this<br>field to include views as objects in transformation<br>rules.<br>Optional JSON object field.                                                                                                                                                                                                                            |
| `object-locator  | column-name`                                                                                                                                                                            | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database table column.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                              |
| `object-locator  | parent`                                                                                                                                                                                 | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database object that is the<br>parent of the specified object, for example, for the<br>`function-name` or<br>`procedure-name`.<br>This field applies only to Oracle to PostgreSQL and<br>Aurora PostgreSQL conversion paths. Use this field to<br>specify the package name for packaged functions or<br>procedures.<br>Optional JSON object field. |
| `object-locator  | function-name`                                                                                                                                                                          | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database function.<br>This field applies only to Oracle to PostgreSQL and<br>Aurora PostgreSQL conversion paths.<br>Optional JSON object field.                                                                                                                                                                                                    |
| `object-locator  | procedure-name`                                                                                                                                                                         | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database procedure.<br>This field applies only to Oracle to PostgreSQL and<br>Aurora PostgreSQL conversion paths.<br>Optional JSON object field.                                                                                                                                                                                                   |
| `object-locator  | parameter-name`                                                                                                                                                                         | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of the source database function or procedure<br>parameter.<br>This field applies only to Oracle to PostgreSQL and<br>Aurora PostgreSQL conversion paths.<br>Optional JSON object field.                                                                                                                                                                          |
| `object-locator  | local-variable-name`                                                                                                                                                                    | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | The name of a local variable within the source database<br>function or procedure.<br>This field applies only to Oracle to PostgreSQL and<br>Aurora PostgreSQL conversion paths.<br>Optional JSON object field.                                                                                                                                                            |
| `object-locator  | type`                                                                                                                                                                                   | An alphanumeric value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The source data type name to match. Use this<br>field to apply the rule only to objects with a specific<br>data type.<br>Optional JSON object field.                                                                                                                                                                                                                      |
| `object-locator  | precision`                                                                                                                                                                              | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The precision of the source data type to match.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                            |
| `object-locator  | scale`                                                                                                                                                                                  | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The scale of the source data type to match.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                                |
| `object-locator  | length`                                                                                                                                                                                 | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The length of the source data type to match.<br>Optional JSON object field.                                                                                                                                                                                                                                                                                               |
| `value`          | An alphanumeric value that follows the naming rules for the<br>target database.                                                                                                         | The text value used by the transformation<br>action. For `add-prefix` and<br>`add-suffix`, specifies the text to add. For<br>`remove-prefix` and<br>`remove-suffix`, specifies the text to remove.<br>For `replace-prefix` and<br>`replace-suffix`, specifies the replacement<br>text. For `rename`, specifies the new<br>name.<br>Required for all actions except<br>`convert-uppercase`,<br>`convert-lowercase`, and<br>`change-data-type`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| `old-value`      | An alphanumeric value that follows the naming rules for the<br>source database.                                                                                                         | The existing value to find and replace in the<br>object name. Required for actions such as<br>`replace-prefix` and<br>`replace-suffix`.<br>Optional parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `data-type`      | A JSON object.                                                                                                                                                                          | An object describing replacement data type properties<br>when `rule-action` is<br>`change-data-type`.<br>The object contains the following fields:<br>• `type` : string<br>• `precision` : number<br>• `scale` : number<br>• `length` : number<br>The following sections describe each object<br>field.<br>Optional parameter.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| `data-type       | type`                                                                                                                                                                                   | An alphanumeric value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | The name of the replacement data type for the target<br>database column if the `rule-action` is<br>`change-data-type`. Must be a valid target<br>database data type.<br>Required JSON object field.                                                                                                                                                                       |
| `data-type       | precision`                                                                                                                                                                              | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The precision of the replacement data type for the<br>target database if the `rule-action` is<br>`change-data-type`.<br>Optional JSON object field.                                                                                                                                                                                                                       |
| `data-type       | scale`                                                                                                                                                                                  | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The scale of the replacement data type for the target<br>database if the `rule-action` is<br>`change-data-type`.<br>Optional JSON object field.                                                                                                                                                                                                                           |
| `data-type       | length`                                                                                                                                                                                 | A numeric (integer) value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | The length of the replacement data type for the target<br>database if the `rule-action` is<br>`change-data-type`.<br>Optional JSON object field.                                                                                                                                                                                                                          |

## Transformation rule examples

The following examples show the JSON value for the
`--transformation-rules` parameter for different rule types:

The following example performs these actions when converting from source to target
database:

- Add prefix `DW_` to schema
  `SALES`.
- Add prefix `FACT_` to table `ORDERS` in
  schema `SALES`.
- Add prefix `OLD_` to column
  `UNIT_PRICE` in table `PRODUCTS` in
  schema `SALES`.

```
{
  "rules": [
    {
      "rule-id": 5,
      "rule-type": "transformation",
      "rule-name": "add-prefix-schema-sales",
      "rule-action": "add-prefix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "SALES"
      },
      "value": "DW_"
    },
    {
      "rule-id": 12,
      "rule-type": "transformation",
      "rule-name": "add-prefix-table-orders",
      "rule-action": "add-prefix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "SALES",
        "table-name": "ORDERS"
      },
      "value": "FACT_"
    },
    {
      "rule-id": 27,
      "rule-type": "transformation",
      "rule-name": "add-prefix-column-unit-price",
      "rule-action": "add-prefix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "SALES",
        "table-name": "PRODUCTS",
        "column-name": "UNIT_PRICE"
      },
      "value": "OLD_"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Remove prefix `SRC_` from schema
  `SRC_FINANCE`.
- Remove prefix `TMP_` from table
  `TMP_INVOICES` in schema
  `SRC_FINANCE`.
- Remove prefix `PAID_` from column
  `PAID_AMOUNT` in table
  `TMP_PAYMENTS` in schema
  `SRC_FINANCE`.

```
{
  "rules": [
    {
      "rule-id": 3,
      "rule-type": "transformation",
      "rule-name": "remove-prefix-schema-src-finance",
      "rule-action": "remove-prefix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "SRC_FINANCE"
      },
      "value": "SRC_"
    },
    {
      "rule-id": 18,
      "rule-type": "transformation",
      "rule-name": "remove-prefix-table-tmp-invoices",
      "rule-action": "remove-prefix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "SRC_FINANCE",
        "table-name": "TMP_INVOICES"
      },
      "value": "TMP_"
    },
    {
      "rule-id": 41,
      "rule-type": "transformation",
      "rule-name": "remove-prefix-column-paid-amount",
      "rule-action": "remove-prefix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "SRC_FINANCE",
        "table-name": "TMP_PAYMENTS",
        "column-name": "PAID_AMOUNT"
      },
      "value": "PAID_"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Replace prefix `OLD_` with `NEW_` in
  schema `OLD_INVENTORY`.
- Replace prefix `STG_` with `INT_` in
  table `STG_WAREHOUSES` in schema
  `OLD_INVENTORY`.
- Replace prefix `SRC_` with `TGT_` in
  column `SRC_WAREHOUSE_CODE` in table
  `STG_WAREHOUSES` in schema
  `OLD_INVENTORY`.

```
{
  "rules": [
    {
      "rule-id": 7,
      "rule-type": "transformation",
      "rule-name": "replace-prefix-schema-old-inventory",
      "rule-action": "replace-prefix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "OLD_INVENTORY"
      },
      "value": "NEW_",
      "old-value": "OLD_"
    },
    {
      "rule-id": 22,
      "rule-type": "transformation",
      "rule-name": "replace-prefix-table-stg-warehouses",
      "rule-action": "replace-prefix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "OLD_INVENTORY",
        "table-name": "STG_WAREHOUSES"
      },
      "value": "INT_",
      "old-value": "STG_"
    },
    {
      "rule-id": 35,
      "rule-type": "transformation",
      "rule-name": "replace-prefix-column-src-warehouse-code",
      "rule-action": "replace-prefix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "OLD_INVENTORY",
        "table-name": "STG_WAREHOUSES",
        "column-name": "SRC_WAREHOUSE_CODE"
      },
      "value": "TGT_",
      "old-value": "SRC_"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Add suffix `_HIST` to schema
  `HR_ARCHIVE`.
- Add suffix `_HIST` to table
  `JOB_CHANGES` in schema
  `HR_ARCHIVE`.
- Add suffix `_TS` to column
  `CREATED_AT` in table
  `EMPLOYEE_SALARIES` in schema
  `HR_ARCHIVE`.

```
{
  "rules": [
    {
      "rule-id": 9,
      "rule-type": "transformation",
      "rule-name": "add-suffix-schema-hr-archive",
      "rule-action": "add-suffix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "HR_ARCHIVE"
      },
      "value": "_HIST"
    },
    {
      "rule-id": 16,
      "rule-type": "transformation",
      "rule-name": "add-suffix-table-job-changes",
      "rule-action": "add-suffix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "HR_ARCHIVE",
        "table-name": "JOB_CHANGES"
      },
      "value": "_HIST"
    },
    {
      "rule-id": 44,
      "rule-type": "transformation",
      "rule-name": "add-suffix-column-created-at",
      "rule-action": "add-suffix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "HR_ARCHIVE",
        "table-name": "EMPLOYEE_SALARIES",
        "column-name": "CREATED_AT"
      },
      "value": "_TS"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Remove suffix `_FILES` from schema
  `LEGAL_FILES`.
- Remove suffix `_V1` from table
  `CLAUSES_V1` in schema
  `LEGAL_FILES`.
- Remove suffix `_CODE` from column
  `COUNTRY_CODE` in table
  `CONTRACTS_V1` in schema
  `LEGAL_FILES`.

```
{
  "rules": [
    {
      "rule-id": 6,
      "rule-type": "transformation",
      "rule-name": "remove-suffix-schema-legal-files",
      "rule-action": "remove-suffix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "LEGAL_FILES"
      },
      "value": "_FILES"
    },
    {
      "rule-id": 14,
      "rule-type": "transformation",
      "rule-name": "remove-suffix-table-clauses-v1",
      "rule-action": "remove-suffix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "LEGAL_FILES",
        "table-name": "CLAUSES_V1"
      },
      "value": "_V1"
    },
    {
      "rule-id": 31,
      "rule-type": "transformation",
      "rule-name": "remove-suffix-column-country-code",
      "rule-action": "remove-suffix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "LEGAL_FILES",
        "table-name": "CONTRACTS_V1",
        "column-name": "COUNTRY_CODE"
      },
      "value": "_CODE"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Replace suffix `_DEV` with `_PROD` in
  schema `REPORTING_DEV`.
- Replace suffix `_RPT` with `_REPORT`
  in table `MONTHLY_RPT` in schema
  `REPORTING_DEV`.
- Replace suffix `_ID` with `_KEY` in
  column `CUSTOMER_ID` in table
  `MONTHLY_RPT` in schema
  `REPORTING_DEV`.

```
{
  "rules": [
    {
      "rule-id": 8,
      "rule-type": "transformation",
      "rule-name": "replace-suffix-schema-reporting-dev",
      "rule-action": "replace-suffix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "REPORTING_DEV"
      },
      "value": "_PROD",
      "old-value": "_DEV"
    },
    {
      "rule-id": 23,
      "rule-type": "transformation",
      "rule-name": "replace-suffix-table-monthly-rpt",
      "rule-action": "replace-suffix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "REPORTING_DEV",
        "table-name": "MONTHLY_RPT"
      },
      "value": "_REPORT",
      "old-value": "_RPT"
    },
    {
      "rule-id": 47,
      "rule-type": "transformation",
      "rule-name": "replace-suffix-column-customer-id",
      "rule-action": "replace-suffix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "REPORTING_DEV",
        "table-name": "MONTHLY_RPT",
        "column-name": "CUSTOMER_ID"
      },
      "value": "_KEY",
      "old-value": "_ID"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Convert all characters in the name of schema
  `CRM_LEGACY` to uppercase.
- Convert all characters in the name of table
  `CUSTOMER_ACCOUNTS` in schema
  `CRM_LEGACY` to uppercase.
- Convert all characters in the name of column
  `FIRST_NAME` in table
  `CUSTOMER_ACCOUNTS` in schema
  `CRM_LEGACY` to uppercase.

```
{
  "rules": [
    {
      "rule-id": 4,
      "rule-type": "transformation",
      "rule-name": "convert-uppercase-schema-crm-legacy",
      "rule-action": "convert-uppercase",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "CRM_LEGACY"
      }
    },
    {
      "rule-id": 19,
      "rule-type": "transformation",
      "rule-name": "convert-uppercase-table-customer-accounts",
      "rule-action": "convert-uppercase",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "CRM_LEGACY",
        "table-name": "CUSTOMER_ACCOUNTS"
      }
    },
    {
      "rule-id": 36,
      "rule-type": "transformation",
      "rule-name": "convert-uppercase-column-first-name",
      "rule-action": "convert-uppercase",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "CRM_LEGACY",
        "table-name": "CUSTOMER_ACCOUNTS",
        "column-name": "FIRST_NAME"
      }
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Convert all characters in the name of schema
  `LOGISTICS` to lowercase.
- Convert all characters in the name of table
  `SHIPMENT_ORDERS` in schema
  `LOGISTICS` to lowercase.
- Convert all characters in the name of column
  `DESTINATION_CITY` in table
  `SHIPMENT_ORDERS` in schema
  `LOGISTICS` to lowercase.

```
{
  "rules": [
    {
      "rule-id": 11,
      "rule-type": "transformation",
      "rule-name": "convert-lowercase-schema-logistics",
      "rule-action": "convert-lowercase",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "LOGISTICS"
      }
    },
    {
      "rule-id": 25,
      "rule-type": "transformation",
      "rule-name": "convert-lowercase-table-shipment-orders",
      "rule-action": "convert-lowercase",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "LOGISTICS",
        "table-name": "SHIPMENT_ORDERS"
      }
    },
    {
      "rule-id": 52,
      "rule-type": "transformation",
      "rule-name": "convert-lowercase-column-destination-city",
      "rule-action": "convert-lowercase",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "LOGISTICS",
        "table-name": "SHIPMENT_ORDERS",
        "column-name": "DESTINATION_CITY"
      }
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Rename schema `TEST_SCHEMA` to
  `TEST_NEW_SCHEMA`.
- Rename table `REGIONS` in schema `HR`
  to `ORG_REGIONS`.
- Rename column `CITY` in table
  `LOCATIONS` in schema `HR` to
  `ORG_CITY_NAME`.

```
{
  "rules": [
    {
      "rule-id": 2,
      "rule-type": "transformation",
      "rule-name": "rename-schema-test-schema",
      "rule-action": "rename",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "TEST_SCHEMA"
      },
      "value": "TEST_NEW_SCHEMA"
    },
    {
      "rule-id": 15,
      "rule-type": "transformation",
      "rule-name": "rename-table-hr-regions",
      "rule-action": "rename",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "HR",
        "table-name": "REGIONS"
      },
      "value": "ORG_REGIONS"
    },
    {
      "rule-id": 38,
      "rule-type": "transformation",
      "rule-name": "rename-column-hr-locations-city",
      "rule-action": "rename",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "HR",
        "table-name": "LOCATIONS",
        "column-name": "CITY"
      },
      "value": "ORG_CITY_NAME"
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Change the data type of column `SALARY` in table
  `EMPLOYEES` in schema `PAYROLL` from
  `NUMBER` to `DECIMAL` with precision
  18 and scale 4.
- Change the data type of column `NOTES` in table
  `EMPLOYEES` in schema `PAYROLL` from
  `VARCHAR2` to `VARCHAR` with length

350.

- Change the data type of column `HIRE_DATE` in table
  `EMPLOYEES` in schema `PAYROLL` from
  `DATE` to `TIMESTAMP WITH TIME ZONE`
  with precision 3.

```
{
  "rules": [
    {
      "rule-id": 10,
      "rule-type": "transformation",
      "rule-name": "change-datatype-column-salary",
      "rule-action": "change-data-type",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "PAYROLL",
        "table-name": "EMPLOYEES",
        "column-name": "SALARY"
      },
      "data-type": {
        "type": "DECIMAL",
        "precision": 18,
        "scale": 4
      }
    },
    {
      "rule-id": 29,
      "rule-type": "transformation",
      "rule-name": "change-datatype-column-notes",
      "rule-action": "change-data-type",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "PAYROLL",
        "table-name": "EMPLOYEES",
        "column-name": "NOTES"
      },
      "data-type": {
        "type": "VARCHAR",
        "length": 350
      }
    },
    {
      "rule-id": 56,
      "rule-type": "transformation",
      "rule-name": "change-datatype-column-hire-date",
      "rule-action": "change-data-type",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "PAYROLL",
        "table-name": "EMPLOYEES",
        "column-name": "HIRE_DATE"
      },
      "data-type": {
        "type": "TIMESTAMP WITH TIME ZONE",
        "precision": 3
      }
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Change the data type of parameter `P_AMOUNT` in
  stored procedure `PROCESS_PAYMENT` in schema
  `FINANCE` to `NUMERIC`.
- Change the data type of local variable
  `V_TAX_RATE` in stored procedure
  `PROCESS_PAYMENT` in schema
  `FINANCE` to `NUMERIC` with precision
  10 and scale 6.
- Change the data type of local variable
  `V_DESCRIPTION` in standalone function
  `CALC_DISCOUNT` in schema
  `FINANCE` to `CHARACTER` with length

150.

```
{
  "rules": [
    {
      "rule-id": 7,
      "rule-type": "transformation",
      "rule-name": "change-datatype-param-p-amount",
      "rule-action": "change-data-type",
      "rule-target": "routine parameter",
      "object-locator": {
        "schema-name": "FINANCE",
        "procedure-name": "PROCESS_PAYMENT",
        "parameter-name": "P_AMOUNT"
      },
      "data-type": {
        "type": "NUMERIC"
      }
    },
    {
      "rule-id": 21,
      "rule-type": "transformation",
      "rule-name": "change-datatype-localvar-v-tax-rate",
      "rule-action": "change-data-type",
      "rule-target": "local variable",
      "object-locator": {
        "schema-name": "FINANCE",
        "procedure-name": "PROCESS_PAYMENT",
        "local-variable-name": "V_TAX_RATE"
      },
      "data-type": {
        "type": "NUMERIC",
        "precision": 10,
        "scale": 6
      }
    },
    {
      "rule-id": 43,
      "rule-type": "transformation",
      "rule-name": "change-datatype-localvar-v-description",
      "rule-action": "change-data-type",
      "rule-target": "local variable",
      "object-locator": {
        "schema-name": "FINANCE",
        "function-name": "CALC_DISCOUNT",
        "local-variable-name": "V_DESCRIPTION"
      },
      "data-type": {
        "type": "CHARACTER",
        "length": 150
      }
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Change the return data type of standalone function
  `GET_PRODUCT_PRICE` in schema
  `FNG_COMPANY` to `BIGINT`.
- Change the return data type of standalone function
  `CALC_DISCOUNTED_PRICE` in schema
  `FNG_COMPANY` to `DECIMAL`.
- Change the return data type of packaged function
  `CALCULATE_TAX` within package
  `TAX_UTILS` in schema
  `FNG_COMPANY` to `REAL`.

```
{
  "rules": [
    {
      "rule-id": 13,
      "rule-type": "transformation",
      "rule-name": "change-result-type-get-product-price",
      "rule-action": "change-data-type",
      "rule-target": "function result",
      "object-locator": {
        "schema-name": "FNG_COMPANY",
        "function-name": "GET_PRODUCT_PRICE"
      },
      "data-type": {
        "type": "BIGINT"
      }
    },
    {
      "rule-id": 28,
      "rule-type": "transformation",
      "rule-name": "change-result-calc-discounted-price",
      "rule-action": "change-data-type",
      "rule-target": "function result",
      "object-locator": {
        "schema-name": "FNG_COMPANY",
        "function-name": "CALC_DISCOUNTED_PRICE"
      },
      "data-type": {
        "type": "DECIMAL"
      }
    },
    {
      "rule-id": 61,
      "rule-type": "transformation",
      "rule-name": "change-result-type-calculate-tax",
      "rule-action": "change-data-type",
      "rule-target": "function result",
      "object-locator": {
        "schema-name": "FNG_COMPANY",
        "parent": "TAX_UTILS",
        "function-name": "CALCULATE_TAX"
      },
      "data-type": {
        "type": "REAL"
      }
    }
  ]
}
```

The following example performs these actions when converting from source to target
database:

- Add prefix `MIGR_` to all schemas whose names start
  with `STG_`.
- Add prefix `MIGR_` to all tables in all schemas
  whose names start with `STG_`.
- Add suffix `_NEW` to all columns whose names start
  with `SRC_` in all tables across all schemas whose
  names start with `STG_`.

```
{
  "rules": [
    {
      "rule-id": 8,
      "rule-type": "transformation",
      "rule-name": "add-prefix-schemas-starting-with-stg",
      "rule-action": "add-prefix",
      "rule-target": "schema",
      "object-locator": {
        "schema-name": "STG_%"
      },
      "value": "MIGR_"
    },
    {
      "rule-id": 33,
      "rule-type": "transformation",
      "rule-name": "add-prefix-all-tables-in-stg-schemas",
      "rule-action": "add-prefix",
      "rule-target": "table",
      "object-locator": {
        "schema-name": "STG_%",
        "table-name": "%"
      },
      "value": "MIGR_"
    },
    {
      "rule-id": 57,
      "rule-type": "transformation",
      "rule-name": "add-suffix-columns-starting-with-src",
      "rule-action": "add-suffix",
      "rule-target": "column",
      "object-locator": {
        "schema-name": "STG_%",
        "table-name": "%",
        "column-name": "SRC_%"
      },
      "value": "_NEW"
    }
  ]
}
```

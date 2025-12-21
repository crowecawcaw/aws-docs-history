# Transformation rules and actions

You use the transformation actions to specify any transformations you want to
apply to the selected schema, table, or view. Transformation rules are optional.

## Limitations

- You cannot apply more than one transformation rule action against the same object (schema,
  table, column, table-tablespace, or index-tablespace). You can apply several
  transformation rule actions on any level as long as each transformation
  action is applied against a different object. However, this restriction is
  not applicable when using data masking transformation rules where you can
  have another transformation like `ADD-COLUMN` or
  `CHANGE-DATA-TYPE` for the same column.
- Table names and column names in transformation rules are case-sensitive. For example, you must
  provide table names and column names for an Oracle or Db2 database in
  upper-case.
- Transformations are not supported for column names with Right-to-Left languages.
- Transformations cannot be performed on columns that contain special characters
  (e.g. #, \, /, -) in their name.
- The only supported transformation for columns that are mapped to BLOB/CLOB data types is to
  drop the column on the target.
- AWS DMS doesn't support replicating two source tables to a single target table. AWS DMS replicates
  records from table to table, and from column to column, according to the
  replication task’s transformation rules. The object names must be unique to
  prevent overlapping.

For example, a source table has a column named `ID` and the corresponding target table
has a pre-existing column called `id`. If a rule uses an `ADD-COLUMN` statement
to add a new column called `id`, and a SQLite statement to populate the column with custom
values, this creates a duplicate, ambiguous object named `id` and is not supported.

- When creating a transformation rule, we recommend using the `data-type` parameter only when
  the selection rules specify multiple columns, for instance, when you set
  `column-name` to `%`. We don't recommend using `data-type`
  for selecting a single column.
- AWS DMS does not support transformation rules where source and target
  objects (tables) are on the same database/schema. Using the same table as
  both source and target in a transformation rule can lead to unexpected and
  potentially harmful results, including but not limited to unintended
  alterations to the table data, modification of table structures or even
  tables getting dropped.

## Values

For table-mapping rules that use the transformation rule type, you can apply the
following values.

| Parameter          | Possible values                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `rule-type`        | `transformation`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | A value that applies the rule to each object<br>specified by the selection rule. Use `transformation`<br>unless otherwise noted.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `rule-id`          | A numeric value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | A unique numeric value to identify the<br>rule. If you specify multiple transformation rules for the same object<br>(schema, table, column, inter-table space, or index table space), AWS DMS applies the transformation<br>rule with the lower rule-id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `rule-name`        | An alphanumeric value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | A unique name to identify the rule.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| `object-locator`   | An object with the following parameters:<br>• `schema-name` – The name of the<br>schema. For MongoDB and Amazon DocumentDB endpoints, this is the<br>name of the database holding a set of<br>collections.<br>• `table-name` – The name of the<br>table, view, or collection.<br>• `table-tablespace-name` – The name<br>of an existing table tablespace.<br>• `index-tablespace-name` – The name<br>of an existing index tablespace.<br>• `column-name` – The name of an<br>existing column.<br>• `data-type` – The name of an<br>existing column data type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | The name of each schema, table or view, table tablespace,<br>index tablespace, and column to which the rule applies. You can<br>use the "%" percent sign as a wildcard for all or part<br>of the value of each `object-locator` parameter,<br>except `data-type`. Thus, you can match these<br>items:<br>• A single table or view in a single schema<br>• A single table or view in some or all schemas<br>• Some or all tables and views in a single schema<br>• Some or all tables and views in some or all<br>schemas<br>• One or more columns in the specified table or tables,<br>view or views, and schema or schemas.<br>• We recommend using the `data-type` parameter only when<br>the selection rules specify multiple columns, for instance, when you set<br>`column-name` to `%`. We don't recommend using this parameter<br>for a single column.<br>Also, the `table-tablespace-name` or<br>`index-tablespace-name` parameter is only<br>available to match an Oracle source endpoint. You can specify<br>either `table-tablespace-name` or<br>`index-tablespace-name` in a single rule, but not<br>both. Thus, you can match \*either<br>• of the<br>following items:<br>• One, some, or all table tablespaces<br>• One, some, or all index tablespaces                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| `rule-action`      | `add-column`, `include-column`,<br>`remove-column`<br>`rename`<br>`convert-lowercase`,<br>`convert-uppercase`<br>`add-prefix`, `remove-prefix`,<br>`replace-prefix`<br>`add-suffix`, `remove-suffix`,<br>`replace-suffix`<br>`define-primary-key`<br>`change-data-type`<br>`add-before-image-columns`<br>`data-masking-digits-mask`<br>`data-masking-digits-randomize`<br>`data-masking-hash-mask`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | The transformation you want to apply to the object. All<br>transformation rule actions are case-sensitive.<br>The `add-column` value of the<br>`rule-action` parameter adds a column to a table.<br>But you can't add a new column with the same name as an existing<br>column of the same table.<br>When used with the `expression` and<br>`data-type` parameters, `add-column`<br>specifies the value of new column data.<br>The `change-data-type` value for<br>`rule-action` is only available for<br>`column` rule targets.<br>The `include-column` value of the `rule-action`<br>parameter changes the mode of the table to *drop all columns by<br>default<br>• and *include the columns specified\*.<br>Multiple columns are included in the target by invoking the `include-column`<br>rule multiple times.<br>You can't use a `define-primary-key` rule when the rule has a wildcard (`%`) in<br>a schema or table name.<br>For an existing task, transformation rule actions which alter the target table schema such as<br>`remove-column`, `rename`, or `add-prefix` will not take effect<br>until you restart the task. If you resume the task after adding the transformation rule,<br>you may see unexpected behavior for the altered column, which might include missing column data.<br>A task restart is required to ensure the transformation rule works properly.<br>The `data-masking-digits-mask`, `data-masking-digits-randomize`, and `data-masking-hash-mask`<br>are for masking sensitive information contained in one or more columns of the table when loading to target.<br>These transformations are only available for column rule targets. For more details, see<br>[Using data masking to hide sensitive information](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md") |
| `rule-target`      | `schema`, `table`,<br>`column`, `table-tablespace`,<br>`index-tablespace`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | The type of object that you're<br>transforming.The `table-tablespace` and<br>`index-tablespace` values are only available for<br>an Oracle target endpoint. Make sure to specify a<br>value for the parameter that you specify as part of the<br>`object-locator`:<br>`table-tablespace-name` or<br>`index-tablespace-name` name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `value`            | An alphanumeric value that follows the naming<br>rules for the target type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The new value for actions that require input, such<br>as `rename`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `old-value`        | An alphanumeric value that follows the naming<br>rules for the target type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | The old value for actions that require<br>replacement, such as `replace-prefix`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| `data-type`        | `type` – The data type to use if the<br>`rule-action` is `add-column` or the<br>replacement data type if the`rule-action` is<br>`change-data-type`.<br>Or, the name of the replacement data type when<br>`rule-action` is `change-data-type`,<br>the value of `column-name` is `"%"`, and<br>an additional `data-type` parameter to identify the<br>existing data type is included in the<br>`object-locator`.<br>AWS DMS supports column data type transformations for the<br>following DMS data types: `"bytes", "date", "time",<br>"datetime", "int1", "int2", "int4", "int8", "numeric",<br>"real4", "real8", "string", "uint1", "uint2", "uint4",<br>"uint8", "wstring", "blob", "nclob", "clob", "boolean",<br>"set", "list" "map", "tuple"`<br>NoteAWS DMS can apply transformations from one type to another<br>ONLY in supported formats. E.g. DATE should be represented<br>in `YYYY:MM:DD/YYYY-MM-DD.` DATETIME should be<br>represented in `YYYY:MM:DD HH:MM:SS/YYYY-MM-DD<br>HH:MM:SS`. TIME should be represented in<br>`HH:MM:SS`.<br>`precision` – If the added column or<br>replacement data type has a precision, an integer value to<br>specify the precision.<br>`scale` – If the added column or<br>replacement data type has a scale, an integer value or date<br>time value to specify the scale.<br>`length` – The length of new column data<br>(when used with `add-column`) | The following is an example of a `data-type`<br>parameter to specify the existing data type to be replaced.<br>`<br>{<br>"rules": [{<br>"rule-type": "selection",<br>"rule-id": "1",<br>"rule-name": "1",<br>"object-locator": {<br>"schema-name": "%",<br>"table-name": "%"<br>},<br>"rule-action": "include"<br>},<br>{<br>"rule-type": "transformation",<br>"rule-id": "2",<br>"rule-name": "2",<br>"rule-target": "column",<br>"object-locator": {<br>"schema-name": "test",<br>"table-name": "table_t",<br>"column-name": "col10"<br>},<br>"rule-action": "change-data-type",<br>"data-type": {<br>"type": "string",<br>"length": "4092",<br>"scale": ""<br>}<br>}<br>]<br>}<br>`<br>Here, the `col10` column of the `table_t` table<br>is changed to the `string` data type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| `expression`       | An alphanumeric value that follows SQLite syntax.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | When used with the `rule-action` set to<br>`rename-schema`, the `expression`<br>parameter specifies a new schema. When used with the<br>`rule-action` set to `rename-table`,<br>`expression` specifies a new table. When used<br>with the `rule-action` set to<br>`rename-column`, `expression`<br>specifies a new column name value.<br>When used with the `rule-action` set to<br>`add-column`, `expression` specifies<br>data that makes up a new column.<br>Note that only expressions are supported for this parameter. Operators and commands<br>are not supported.<br>For more information about using expressions for<br>transformation rules, see [Using transformation rule expressions to define column content](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md").<br>For more information about SQLite expressions, see [Using SQLite functions to build expressions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions-SQLite "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions-SQLite").                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `primary-key-def`  | An object with the following parameters:<br>• `name` – The name of a new primary<br>key or unique index for the table or view.<br>• (Optional) `origin` – The type of<br>unique key to define: `primary-key` (the<br>default) or `unique-index`.<br>• `columns` – An array of strings<br>listing the names of columns in the order they appear in<br>the primary key or unique index.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | This parameter can define the name, type, and<br>content of a unique key on the transformed table or view. It does so<br>when the `rule-action` is set to<br>`define-primary-key` and the `rule-target`<br>is set to `table`. By default, the unique key is defined<br>as a primary key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| `before-image-def` | An object with the following parameters:<br>• `column-prefix` – A value prepended<br>to a column name. The default value is<br>`BI_`.<br>• `column-suffix` – A value appended<br>to the column name. The default is empty.<br>• `column-filter` – Requires one of<br>the following values: `pk-only` (default),<br>`non-lob` (optional) and `all`<br>(optional).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | This parameter defines a naming convention to identify the<br>before-image columns and specifies a filter to identify which<br>source columns can have before-image columns created for them on<br>the target. You can specify this parameter when the<br>`rule-action` is set to<br>`add-before-image-columns` and the<br>`rule-target` is set to<br>`column`.<br>Don't set both `column-prefix` and<br>`column-suffix` to empty strings.<br>For `column-filter`, select:<br>• `pk-only` – To add only columns that<br>are part of table primary keys.<br>• `non-lob` – To add only columns that<br>are not of LOB type.<br>• `all` – To add any column that has a<br>before-image value.<br>NoteThe `before-image-def` parameter does not<br>support large binary object (LOB) data types such as CLOB<br>and BLOB. If the data type is set as LOB, a void column is<br>created in the table.<br>For more information about before-image support for AWS DMS<br>target endpoints, see:<br>• [Using a before image to view<br>original values of CDC rows for a Kinesis data stream as a target](CHAP_Target.md#CHAP_Target.Kinesis.BeforeImage "CHAP_Target.md#CHAP_Target.Kinesis.BeforeImage")<br>• [Using a before image to view<br>original values of CDC rows for Apache Kafka as a target](CHAP_Target.md#CHAP_Target.Kafka.BeforeImage "CHAP_Target.md#CHAP_Target.Kafka.BeforeImage")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## Examples

###### Example Rename a schema

The following example renames a schema from `Test` in your source
to `Test1` in your target.

```
{

    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "rename",
            "rule-target": "schema",
            "object-locator": {
                "schema-name": "Test"
            },
            "value": "Test1"
        }
    ]
}
```

###### Example Rename a table

The following example renames a table from `Actor` in your
source to `Actor1` in your target.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "rename",
            "rule-target": "table",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "Actor"
            },
            "value": "Actor1"
        }
    ]
}
```

###### Example Rename a column

The following example renames a column in table `Actor` from
`first_name` in your source to `fname` in your
target.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
         {
            "rule-type": "transformation",
            "rule-id": "4",
            "rule-name": "4",
            "rule-action": "rename",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "test",
                "table-name": "Actor",
                "column-name" : "first_name"
            },
            "value": "fname"
        }
    ]
}
```

###### Example Rename an Oracle table tablespace

The following example renames the table tablespace named
`SetSpace` for a table named `Actor` in your
Oracle source to `SceneTblSpace` in your Oracle target
endpoint.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "Play",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "rename",
            "rule-target": "table-tablespace",
            "object-locator": {
                "schema-name": "Play",
                "table-name": "Actor",
                "table-tablespace-name": "SetSpace"
            },
            "value": "SceneTblSpace"
        }
    ]
}
```

###### Example Rename an Oracle index tablespace

The following example renames the index tablespace named
`SetISpace` for a table named `Actor` in your
Oracle source to `SceneIdxSpace` in your Oracle target
endpoint.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "Play",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "rename",
            "rule-target": "table-tablespace",
            "object-locator": {
                "schema-name": "Play",
                "table-name": "Actor",
                "table-tablespace-name": "SetISpace"
            },
            "value": "SceneIdxSpace"
        }
    ]
}
```

###### Example Add a column

The following example adds a `datetime` column to the table
`Actor` in schema `test`.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "add-column",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "test",
                "table-name": "actor"
            },
            "value": "last_updated",
            "data-type": {
                "type": "datetime",
                "precision": 6
            }
        }
    ]
}
```

###### Example Remove a column

The following example transforms the table named `Actor` in
your source to remove all columns starting with the characters
`col` from it in your target.

```
{
 	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "remove-column",
		"rule-target": "column",
		"object-locator": {
			"schema-name": "test",
			"table-name": "Actor",
			"column-name": "col%"
		}
	}]
 }
```

###### Example Convert to lowercase

The following example converts a table name from `ACTOR` in
your source to `actor` in your target.

```
{
	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "convert-lowercase",
		"rule-target": "table",
		"object-locator": {
			"schema-name": "test",
			"table-name": "ACTOR"
		}
	}]
}
```

###### Example Convert to uppercase

The following example converts all columns in all tables and all schemas
from lowercase in your source to uppercase in your target.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "convert-uppercase",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "%",
                "table-name": "%",
                "column-name": "%"
            }
        }
    ]
}
```

###### Example Add a prefix

The following example transforms all tables in your source to add the
prefix `DMS_` to them in your target.

```
{
 	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "add-prefix",
		"rule-target": "table",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"value": "DMS_"
	}]

}
```

###### Example Replace a prefix

The following example transforms all columns containing the prefix
`Pre_` in your source to replace the prefix with
`NewPre_` in your target.

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "test",
                "table-name": "%"
            },
            "rule-action": "include"
        },
        {
            "rule-type": "transformation",
            "rule-id": "2",
            "rule-name": "2",
            "rule-action": "replace-prefix",
            "rule-target": "column",
            "object-locator": {
                "schema-name": "%",
                "table-name": "%",
                "column-name": "%"
            },
            "value": "NewPre_",
            "old-value": "Pre_"
        }
    ]
}
```

###### Example Remove a suffix

The following example transforms all tables in your source to remove the
suffix `_DMS` from them in your target.

```
{
	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "remove-suffix",
		"rule-target": "table",
		"object-locator": {
			"schema-name": "test",
			"table-name": "%"
		},
		"value": "_DMS"
	}]
}
```

###### Example Define a primary key

The following example defines a primary key named
`ITEM-primary-key` on three columns of the `ITEM`
table migrated to your target endpoint.

```
{
	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "inventory",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "define-primary-key",
		"rule-target": "table",
		"object-locator": {
			"schema-name": "inventory",
			"table-name": "ITEM"
		},
		"primary-key-def": {
			"name": "ITEM-primary-key",
			"columns": [
				"ITEM-NAME",
				"BOM-MODEL-NUM",
				"BOM-PART-NUM"
			]
              }
	}]
}
```

###### Example Define a unique index

The following example defines a unique index named
`ITEM-unique-idx` on three columns of the `ITEM`
table migrated to your target endpoint.

```
{
	"rules": [{
		"rule-type": "selection",
		"rule-id": "1",
		"rule-name": "1",
		"object-locator": {
			"schema-name": "inventory",
			"table-name": "%"
		},
		"rule-action": "include"
	}, {
		"rule-type": "transformation",
		"rule-id": "2",
		"rule-name": "2",
		"rule-action": "define-primary-key",
		"rule-target": "table",
		"object-locator": {
			"schema-name": "inventory",
			"table-name": "ITEM"
		},
		"primary-key-def": {
			"name": "ITEM-unique-idx",
			"origin": "unique-index",
			"columns": [
				"ITEM-NAME",
				"BOM-MODEL-NUM",
				"BOM-PART-NUM"
			]
              }
	}]
}
```

###### Example Change data type of target column

The following example changes the data type of a target column named
`SALE_AMOUNT` from an existing data type to
`int8`.

```
{
    "rule-type": "transformation",
    "rule-id": "1",
    "rule-name": "RuleName 1",
    "rule-action": "change-data-type",
    "rule-target": "column",
    "object-locator": {
        "schema-name": "dbo",
        "table-name": "dms",
        "column-name": "SALE_AMOUNT"
    },
    "data-type": {
        "type": "int8"
    }
}
```

###### Example Add a before image column

For a source column named `emp_no`, the transformation rule in
the example following adds a new column named `BI_emp_no` in the
target.

```
{
	"rules": [{
			"rule-type": "selection",
			"rule-id": "1",
			"rule-name": "1",
			"object-locator": {
				"schema-name": "%",
				"table-name": "%"
			},
			"rule-action": "include"
		},
		{
			"rule-type": "transformation",
			"rule-id": "2",
			"rule-name": "2",
			"rule-target": "column",
			"object-locator": {
				"schema-name": "%",
				"table-name": "employees"
			},
			"rule-action": "add-before-image-columns",
			"before-image-def": {
				"column-prefix": "BI_",
				"column-suffix": "",
				"column-filter": "pk-only"
			}
		}
	]
}
```

Here, the following statement populates a `BI_emp_no` column in the
corresponding row with 1.

```
UPDATE employees SET emp_no = 3 WHERE BI_emp_no = 1;
```

When writing CDC updates to supported AWS DMS targets, the
`BI_emp_no` column makes it possible to tell which rows have
updated values in the `emp_no` column.

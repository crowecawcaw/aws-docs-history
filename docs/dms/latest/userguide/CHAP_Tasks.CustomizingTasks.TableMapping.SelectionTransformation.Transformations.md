

# Transformation rules and actions
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations"></a>

You use the transformation actions to specify any transformations you want to apply to the selected schema, table, or view. Transformation rules are optional. 

## Limitations
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.Limitations"></a>
+ You cannot apply more than one transformation rule action against the same object (schema, table, column, table-tablespace, or index-tablespace). You can apply several transformation rule actions on any level as long as each transformation action is applied against a different object. However, this restriction is not applicable when using data masking transformation rules where you can have another transformation like `ADD-COLUMN` or `CHANGE-DATA-TYPE` for the same column.
+ Table names and column names in transformation rules are case-sensitive. For example, you must provide table names and column names for an Oracle or Db2 database in upper-case.
+ Transformations are not supported for column names with Right-to-Left languages.
+ Transformations cannot be performed on columns that contain special characters (e.g. \#, \\, /, -) in their name.
+ The only supported transformation for columns that are mapped to BLOB/CLOB data types is to drop the column on the target.
+ AWS DMS doesn't support replicating two source tables to a single target table. AWS DMS replicates records from table to table, and from column to column, according to the replication task’s transformation rules. The object names must be unique to prevent overlapping.

  For example, a source table has a column named `ID` and the corresponding target table has a pre-existing column called `id`. If a rule uses an `ADD-COLUMN` statement to add a new column called `id`, and a SQLite statement to populate the column with custom values, this creates a duplicate, ambiguous object named `id` and is not supported. 
+ When creating a transformation rule, we recommend using the `data-type` parameter only when the selection rules specify multiple columns, for instance, when you set `column-name` to `%`. We don't recommend using `data-type` for selecting a single column.
+ AWS DMS does not support transformation rules where source and target objects (tables) are on the same database/schema. Using the same table as both source and target in a transformation rule can lead to unexpected and potentially harmful results, including but not limited to unintended alterations to the table data, modification of table structures or even tables getting dropped.

## Values
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.Values"></a>

For table-mapping rules that use the transformation rule type, you can apply the following values. 


| Parameter | Possible values | Description | 
| --- | --- | --- | 
| rule-type | transformation | A value that applies the rule to each object specified by the selection rule. Use transformation unless otherwise noted. | 
| rule-id | A numeric value. | A unique numeric value to identify the rule. If you specify multiple transformation rules for the same object (schema, table, column, inter-table space, or index table space), AWS DMS applies the transformation rule with the lower rule-id. | 
| rule-name | An alphanumeric value. | A unique name to identify the rule. | 
| object-locator | An object with the following parameters:+  `schema-name` – The name of the schema. For MongoDB and Amazon DocumentDB endpoints, this is the name of the database holding a set of collections. <br />+  `table-name` – The name of the table, view, or collection. <br />+  `table-tablespace-name` – The name of an existing table tablespace. <br />+  `index-tablespace-name` – The name of an existing index tablespace. <br />+  `column-name` – The name of an existing column. <br />+  `data-type` – The name of an existing column data type.  | The name of each schema, table or view, table tablespace, index tablespace, and column to which the rule applies. You can use the "%" percent sign as a wildcard for all or part of the value of each `object-locator` parameter, except `data-type`. Thus, you can match these items:+  A single table or view in a single schema <br />+  A single table or view in some or all schemas <br />+  Some or all tables and views in a single schema <br />+  Some or all tables and views in some or all schemas <br />+  One or more columns in the specified table or tables, view or views, and schema or schemas. <br />+ We recommend using the `data-type` parameter only when the selection rules specify multiple columns, for instance, when you set `column-name` to `%`. We don't recommend using this parameter for a single column.<br />Also, the `table-tablespace-name` or `index-tablespace-name` parameter is only available to match an Oracle source endpoint. You can specify either `table-tablespace-name` or `index-tablespace-name` in a single rule, but not both. Thus, you can match *either* of the following items:+  One, some, or all table tablespaces <br />+  One, some, or all index tablespaces  | 
| rule-action | `add-column`, `include-column`, `remove-column`<br />`rename`<br />`convert-lowercase`, `convert-uppercase`<br />`add-prefix`, `remove-prefix`, `replace-prefix`<br />`add-suffix`, `remove-suffix`, `replace-suffix`<br />`define-primary-key`<br />`change-data-type`<br />`add-before-image-columns`<br />`data-masking-digits-mask`<br />`data-masking-digits-randomize`<br />`data-masking-hash-mask` | The transformation you want to apply to the object. All transformation rule actions are case-sensitive.<br />The `add-column` value of the `rule-action` parameter adds a column to a table. But you can't add a new column with the same name as an existing column of the same table.<br />When used with the `expression` and `data-type` parameters, `add-column` specifies the value of new column data. <br />The `change-data-type` value for `rule-action` is only available for `column` rule targets.<br />The `include-column` value of the `rule-action` parameter changes the mode of the table to *drop all columns by default* and *include the columns specified*. Multiple columns are included in the target by invoking the `include-column` rule multiple times.<br />You can't use a `define-primary-key` rule when the rule has a wildcard (`%`) in a schema or table name. <br />For an existing task, transformation rule actions which alter the target table schema such as `remove-column`, `rename`, or `add-prefix` will not take effect until you restart the task. If you resume the task after adding the transformation rule, you may see unexpected behavior for the altered column, which might include missing column data. A task restart is required to ensure the transformation rule works properly.<br />The `data-masking-digits-mask`, `data-masking-digits-randomize`, and `data-masking-hash-mask` are for masking sensitive information contained in one or more columns of the table when loading to target. These transformations are only available for column rule targets. For more details, see [Using data masking to hide sensitive information](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Masking.md)  | 
| rule-target | schema, table, column, table-tablespace, index-tablespace | The type of object that you're transforming.The `table-tablespace` and `index-tablespace` values are only available for an Oracle target endpoint. <br />Make sure to specify a value for the parameter that you specify as part of the `object-locator`: `table-tablespace-name` or `index-tablespace-name` name. | 
| value | An alphanumeric value that follows the naming rules for the target type. | The new value for actions that require input, such as rename. | 
| old-value | An alphanumeric value that follows the naming rules for the target type. | The old value for actions that require replacement, such as replace-prefix. | 
| data-type | `type` – The data type to use if the `rule-action` is `add-column` or the replacement data type if the`rule-action` is `change-data-type`.<br />Or, the name of the replacement data type when `rule-action` is `change-data-type`, the value of `column-name` is `"%"`, and an additional `data-type` parameter to identify the existing data type is included in the `object-locator`.<br />AWS DMS supports column data type transformations for the following DMS data types: `"bytes", "date", "time", "datetime", "int1", "int2", "int4", "int8", "numeric", "real4", "real8", "string", "uint1", "uint2", "uint4", "uint8", "wstring", "blob", "nclob", "clob", "boolean", "set", "list" "map", "tuple"` AWS DMS can apply transformations from one type to another ONLY in supported formats. E.g. DATE should be represented in `YYYY:MM:DD/YYYY-MM-DD.` DATETIME should be represented in `YYYY:MM:DD HH:MM:SS/YYYY-MM-DD HH:MM:SS`. TIME should be represented in `HH:MM:SS`. <br />`precision` – If the added column or replacement data type has a precision, an integer value to specify the precision.<br />`scale` – If the added column or replacement data type has a scale, an integer value or date time value to specify the scale.<br />`length` – The length of new column data (when used with `add-column`)  | The following is an example of a `data-type` parameter to specify the existing data type to be replaced. <pre>{<br />	"rules": [{<br />			"rule-type": "selection",<br />			"rule-id": "1",<br />			"rule-name": "1",<br />			"object-locator": {<br />				"schema-name": "%",<br />				"table-name": "%"<br />			},<br />			"rule-action": "include"<br />		},<br />		{<br />			"rule-type": "transformation",<br />			"rule-id": "2",<br />			"rule-name": "2",<br />			"rule-target": "column",<br />			"object-locator": {<br />				"schema-name": "test",<br />				"table-name": "table_t",<br />				"column-name": "col10"<br />			},<br />			"rule-action": "change-data-type",<br />			"data-type": {<br />				"type": "string",<br />				"length": "4092",<br />				"scale": ""<br />			}<br />		}<br />	]<br />}</pre><br />Here, the `col10` column of the `table_t` table is changed to the `string` data type. | 
| expression | An alphanumeric value that follows SQLite syntax.  | When used with the `rule-action` set to `rename-schema`, the `expression` parameter specifies a new schema. When used with the `rule-action` set to `rename-table`, `expression` specifies a new table. When used with the `rule-action` set to `rename-column`, `expression` specifies a new column name value.<br />When used with the `rule-action` set to `add-column`, `expression` specifies data that makes up a new column.<br />Note that only expressions are supported for this parameter. Operators and commands are not supported.<br />For more information about using expressions for transformation rules, see [Using transformation rule expressions to define column content](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions.md).<br />For more information about SQLite expressions, see [Using SQLite functions to build expressions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions.md#CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Expressions-SQLite). | 
| primary-key-def | An object with the following parameters:+  `name` – The name of a new primary key or unique index for the table or view. <br />+  (Optional) `origin` – The type of unique key to define: `primary-key` (the default) or `unique-index`. <br />+  `columns` – An array of strings listing the names of columns in the order they appear in the primary key or unique index.  | This parameter can define the name, type, and content of a unique key on the transformed table or view. It does so when the rule-action is set to define-primary-key and the rule-target is set to table. By default, the unique key is defined as a primary key. | 
| before-image-def | An object with the following parameters:+  `column-prefix` – A value prepended to a column name. The default value is `BI_`. <br />+  `column-suffix` – A value appended to the column name. The default is empty. <br />+  `column-filter` – Requires one of the following values: `pk-only` (default), `non-lob` (optional) and `all` (optional).  | This parameter defines a naming convention to identify the before-image columns and specifies a filter to identify which source columns can have before-image columns created for them on the target. You can specify this parameter when the `rule-action` is set to `add-before-image-columns` and the `rule-target` is set to `column`.<br />Don't set both `column-prefix` and `column-suffix` to empty strings.<br />For `column-filter`, select:+  `pk-only` – To add only columns that are part of table primary keys. <br />+  `non-lob` – To add only columns that are not of LOB type. <br />+  `all` – To add any column that has a before-image value.   The `before-image-def` parameter does not support large binary object (LOB) data types such as CLOB and BLOB. If the data type is set as LOB, a void column is created in the table. <br />For more information about before-image support for AWS DMS target endpoints, see:+  [Using a before image to view original values of CDC rows for a Kinesis data stream as a target](CHAP_Target.Kinesis.md#CHAP_Target.Kinesis.BeforeImage) <br />+  [Using a before image to view original values of CDC rows for Apache Kafka as a target](CHAP_Target.Kafka.md#CHAP_Target.Kafka.BeforeImage)  | 

## Examples
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Transformations.Examples"></a>

**Example Rename a schema**  
The following example renames a schema from `Test` in your source to `Test1` in your target.  

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

**Example Rename a table**  
The following example renames a table from `Actor` in your source to `Actor1` in your target.  

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

**Example Rename a column**  
The following example renames a column in table `Actor` from `first_name` in your source to `fname` in your target.  

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

**Example Rename an Oracle table tablespace**  
The following example renames the table tablespace named `SetSpace` for a table named `Actor` in your Oracle source to `SceneTblSpace` in your Oracle target endpoint.  

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

**Example Rename an Oracle index tablespace**  
The following example renames the index tablespace named `SetISpace` for a table named `Actor` in your Oracle source to `SceneIdxSpace` in your Oracle target endpoint.  

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

**Example Add a column**  
The following example adds a `datetime` column to the table `Actor` in schema `test`.  

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

**Example Remove a column**  
The following example transforms the table named `Actor` in your source to remove all columns starting with the characters `col` from it in your target.  

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

**Example Convert to lowercase**  
The following example converts a table name from `ACTOR` in your source to `actor` in your target.  

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

**Example Convert to uppercase**  
The following example converts all columns in all tables and all schemas from lowercase in your source to uppercase in your target.  

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

**Example Add a prefix**  
The following example transforms all tables in your source to add the prefix `DMS_` to them in your target.  

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

**Example Replace a prefix**  
The following example transforms all columns containing the prefix `Pre_` in your source to replace the prefix with `NewPre_` in your target.  

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

**Example Remove a suffix**  
The following example transforms all tables in your source to remove the suffix `_DMS` from them in your target.  

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

**Example Define a primary key**  
The following example defines a primary key named `ITEM-primary-key` on three columns of the `ITEM` table migrated to your target endpoint.  

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

**Example Define a unique index**  
The following example defines a unique index named `ITEM-unique-idx` on three columns of the `ITEM` table migrated to your target endpoint.  

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

**Example Change data type of target column**  
The following example changes the data type of a target column named `SALE_AMOUNT` from an existing data type to `int8`.  

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

**Example Add a before image column**  
For a source column named `emp_no`, the transformation rule in the example following adds a new column named `BI_emp_no` in the target.  

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
Here, the following statement populates a `BI_emp_no` column in the corresponding row with 1.  

```
UPDATE employees SET emp_no = 3 WHERE BI_emp_no = 1;
```
When writing CDC updates to supported AWS DMS targets, the `BI_emp_no` column makes it possible to tell which rows have updated values in the `emp_no` column.
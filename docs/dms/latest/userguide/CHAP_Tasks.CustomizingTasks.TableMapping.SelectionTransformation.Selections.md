

# Selection rules and actions
<a name="CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Selections"></a>

Using table mapping, you can specify what tables, views, and schemas you want to work with by using selection rules and actions. For table-mapping rules that use the selection rule type, you can apply the following values. 

**Warning**  
Do not to include any sensitive data within these rules.


| Parameter | Possible values | Description | 
| --- | --- | --- | 
| rule-type | selection | A selection rule. Define at least one selection rule when specifying a table mapping. | 
| rule-id | A numeric value. | A unique numeric value to identify the rule. If you create the rule using the console, the console creates this value for you. | 
| rule-name | An alphanumeric value. | A unique name to identify the rule. If you create the rule using the console, the console creates this value for you. | 
| rule-action | include, exclude, explicit | A value that includes or excludes the object or objects selected by the rule. If explicit is specified, you can select and include only one object that corresponds to an explicitly specified table and schema. | 
| object-locator | An object with the following parameters:+  `schema-name` – The name of the schema. <br />+  `table-name` – The name of the table. <br />+  (Optional) `table-type` – `table \| view \| all`, to indicate if `table-name` refers only to tables, views, or both tables and views. The default is `table`. <br />AWS DMS loads views only in a full-load task. If you have only full-load and change data capture (CDC) tasks, configure at least one full-load-only task to load your views. <br />Not all target endpoints accept views as a source of replication, even in full load (e.g. Amazon OpenSearch Service). Check the limitations of your target endpoint.  DMS selection rules are case-sensitive. However, the selection result also depends on the source endpoint database configuration. If the source endpoint is configured as case-insensitive, the case of the object locator value does not matter. Ensure that correct object identifiers are used in DMS selection rules on a case-insensitive endpoint.  | The name of each schema and table or view to which the rule applies. You can also specify if a rule includes only tables, only views, or both tables and views. If the `rule-action` is either `include` or `exclude`, you can use the "%" percent sign as a wildcard for all or part of the value for the `schema-name` and `table-name` parameter. For information about other wildcards you can use, see [Wildcards in table mapping](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.Wildcards.md). Thus, you can match these items:+  A single table, view, or collection in a single schema <br />+  A single table, view, or collection in some or all schemas <br />+  Some or all tables and views in a single schema, or collections in a single database <br />+  Some or all tables and views in some or all schemas, or collections in some or all databases <br />If the `rule-action` is `explicit`, you can only specify the exact name of a single table or view and its schema (with no wildcards).<br />The supported sources for views include:+  Oracle <br />+  Microsoft SQL Server <br />+  PostgreSQL <br />+  IBM Db2 LUW <br />+  IBM Db2 z/OS <br />+  SAP Adaptive Server Enterprise (ASE) <br />+  MySQL <br />+  AURORA MySQL <br />+  MariaDB  AWS DMS never loads a source view to a target view. A source view is loaded to an equivalent table on the target with the same name as the view on the source. <br />The supported sources for databases containing collections include:+  MongoDB <br />+  Amazon DocumentDB  | 
| load-order | A positive integer. The maximum value is 2,147,483,647.  | The priority for loading tables and views. Tables and views with higher values are loaded first.  | 
| filters | An array of objects. | One or more objects for filtering the source. You specify object parameters to filter on a single column in the source. You specify multiple objects to filter on multiple columns. For more information, see [Using source filters](CHAP_Tasks.CustomizingTasks.Filters.md). | 

**Example Migrate all tables in a schema**  
The following example migrates all tables from a schema named `Test` in your source to your target endpoint.  

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
        }
    ]
}
```

**Example Migrate some tables in a schema**  
The following example migrates all tables except those starting with `DMS` from a schema named `Test` in your source to your target endpoint.  

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
            "rule-type": "selection",
            "rule-id": "2",
            "rule-name": "2",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "DMS%"
            },
            "rule-action": "exclude"
        }
    ]
}
```

**Example Migrate a specified single table in single schema**  
The following example migrates the `Customer` table from the `NewCust` schema in your source to your target endpoint.  

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "NewCust",
                "table-name": "Customer"
            },
            "rule-action": "explicit"
        }
    ]
}
```
You can explicitly select on multiple tables and schemas by specifying multiple selection rules.

**Example Migrate tables in a set order**  
Tables and views are migrated according to their load-order values, with higher values receiving priority in the migration sequence. The following example migrates two tables, `loadfirst` with a priority value of 2 and `loadsecond` with a priority value of 1, the migration task would first process the `loadfirst` table before proceeding to the `loadsecond` table. This prioritization mechanism ensures that dependencies between database objects are respected during the migration process.  

```
{
    "rules": [
        {
            "rule-type": "selection",
            "rule-id": "1",
            "rule-name": "1",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "loadsecond"
            },
            "rule-action": "include",
            "load-order": "1"
        },
        {
            "rule-type": "selection",
            "rule-id": "2",
            "rule-name": "2",
            "object-locator": {
                "schema-name": "Test",
                "table-name": "loadfirst"
            },
            "rule-action": "include",
            "load-order": "2"
        }
    ]
}
```

**Note**  
`load-order` is applicable for table initialization. The load of a successive table won't wait for a previous table load to complete if `MaxFullLoadSubTasks` is greater than 1.

**Example Migrate some views in a schema**  
The following example migrates some views from a schema named `Test` in your source to equivalent tables in your target.  

```
{
   "rules": [
        {
           "rule-type": "selection",
           "rule-id": "2",
           "rule-name": "2",
           "object-locator": {
               "schema-name": "Test",
               "table-name": "view_DMS%",
               "table-type": "view"
            },
           "rule-action": "include"
        }
    ]
}
```

**Example Migrate all tables and views in a schema**  
The following example migrates all tables and views from a schema named `report` in your source to equivalent tables in your target.  

```
{
   "rules": [
        {
           "rule-type": "selection",
           "rule-id": "3",
           "rule-name": "3",
           "object-locator": {
               "schema-name": "report",
               "table-name": "%",
               "table-type": "all"
            },
           "rule-action": "include"
        }
    ]
}
```
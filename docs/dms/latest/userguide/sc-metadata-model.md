# Metadata model in DMS Schema Conversion

When you work with DMS Schema Conversion, the service represents your database schemas as a
hierarchical tree. This tree is called the _metadata tree_, and it
applies to both source and target schemas. Each element in the tree, including the root
element ("Servers"), is a metadata model.

The metadata tree contains two kinds of elements:

- **Objects** — Represent actual database objects
  such as tables, functions, views, sequences, and indexes. You can retrieve
  the SQL definition of an object using the [DescribeMetadataModel](../APIReference/API_DescribeMetadataModel.md "../APIReference/API_DescribeMetadataModel.md")
  request.
- **Categories** — Virtual grouping containers
  such as "Schemas", "Tables", "Functions", and
  "Indexes". Categories organize objects in the tree for navigation but do
  not have SQL definitions themselves.
  The metadata tree loads data only when you request it. This approach is called
  on-demand loading (also known as lazy loading), which means DMS Schema Conversion retrieves data
  from your database only as needed. You use the import operation to load metadata —
  either by refreshing a specific metadata model or importing an entire subtree at once.
  Operations such as assessment and conversion also load the metadata tree
  automatically.

## How the metadata model works

The metadata model in DMS Schema Conversion follows a lifecycle of operations.
Operations that modify the metadata tree (such as import and convert) are asynchronous.
You start a request for these operations, and it runs in the background. Call the
corresponding describe API to check the request status. Operations that read the
tree (such as describing children or definitions) are synchronous.

###### Note

In DMS Schema Conversion, the terms _operation_ and _request_ are used interchangeably.

The typical workflow includes the following steps:

1. **Import** — Load metadata from your source
   or target database into the metadata tree. You can either load the initial
   metadata model or reload an existing model from the database. For more
   information, see [Navigate the
   tree](#sc-metadata-model-navigating "#sc-metadata-model-navigating"). For the API
   reference, see [StartMetadataModelImport](../APIReference/API_StartMetadataModelImport.md "../APIReference/API_StartMetadataModelImport.md").
2. **Assess** — Analyze the selected source
   metadata models to identify conversion complexity and potential issues. For more
   information, see [Creating database migration assessment reports with DMS Schema Conversion](assessment-reports.md "assessment-reports.md").
3. **Convert** — Convert the selected source
   metadata models to a target-compatible format. The converted definitions are
   stored as part of the target metadata tree. For more information, see [Converting database schemas in DMS Schema Conversion: step-by-step guide](schema-conversion-convert.md "schema-conversion-convert.md").
4. **Export** — Save metadata definitions.
   You can export both source and target metadata as SQL scripts to your Amazon S3
   bucket. For non-virtual targets, you can also apply converted objects
   directly to your target database. For more information about virtual
   targets, see [Virtual mode for offline source and virtual target](virtual-data-provider.md "virtual-data-provider.md"). For more information
   about applying converted objects, see [Applying your converted code](schema-conversion-save-apply.md#schema-conversion-apply "schema-conversion-save-apply.md#schema-conversion-apply").

After you assess or convert source metadata models, you can generate an assessment
report to review the results. For more information, see [Creating database migration assessment reports with DMS Schema Conversion](assessment-reports.md "assessment-reports.md").

For supported migration pairs, you can also create custom statement metadata models
from SQL definitions using [StartMetadataModelCreation](../APIReference/API_StartMetadataModelCreation.md "../APIReference/API_StartMetadataModelCreation.md"). For more information, see [Create statement
models](#sc-metadata-model-creation "#sc-metadata-model-creation").

## Navigate the metadata model tree

You can navigate the metadata tree using the following API requests:

- [DescribeMetadataModelChildren](../APIReference/API_DescribeMetadataModelChildren.md "../APIReference/API_DescribeMetadataModelChildren.md") — Returns the
  children of a given metadata model. Each child includes selection rules
  (filters that identify specific metadata models) that you can pass to
  the next call to drill deeper.
- [DescribeMetadataModel](../APIReference/API_DescribeMetadataModel.md "../APIReference/API_DescribeMetadataModel.md") — Returns the name,
  type, and SQL definition of a specific metadata model.

Both requests require the `Origin` parameter (`SOURCE` or
`TARGET`) and use selection rules to identify the metadata model.
The navigation pattern is the same for both source and target trees. For more information
about the selection rules format, see [Selection rules in DMS Schema Conversion](sc-selection-rules.md "sc-selection-rules.md").

Choose your preferred interface to view navigation instructions.

AWS Management Console
After you open your schema conversion project, you can browse both
source and target metadata trees. For more information about opening a
project, see [Converting database schemas in DMS Schema Conversion: step-by-step guide](schema-conversion-convert.md "schema-conversion-convert.md").

The console displays two tree panels: the source tree on the left and
the target tree on the right. Each panel consists of a header that shows
the database engine, an Actions menu, and the metadata tree itself.

The Actions menu is context-dependent. Not every metadata model has all
actions available. Source and target trees have different action
lists.

To view the SQL definition and properties of a metadata model, choose
it in the tree. The center panel displays the Source SQL and Target SQL
tabs with the definition, and a Properties tab with metadata attributes.
Additional tabs might appear depending on the metadata model type
— for example, Columns for tables and views, or Parameters for
routines.

To expand the children of a metadata model, choose the expand icon
(black triangle) next to it. Choose either the expand icon or
the metadata model name to load its children automatically.

When you choose a source metadata model that has been converted, the
corresponding target metadata model is selected automatically in the
target tree panel.

###### Browse the metadata tree

The following walkthrough shows how to browse the metadata tree
and view a metadata model definition.

1. In the tree panel, choose the expand icon next to your
   server to display the top-level categories, such as
   **Databases** or
   **Schemas** depending on the
   database engine.
2. Continue expanding categories to navigate to the metadata
   model you want to explore. For example, expand
   **Databases**, then a specific
   database, then **Schemas**, then a
   schema name, then a category such as
   **Tables**,
   **Views**, or
   **Procedures**. Some database
   engines don't have the **Databases**
   level — in that case, expand
   **Schemas** directly.
3. Choose a metadata model to view its SQL definition in the
   center panel. The **Source SQL**
   tab shows the source definition, and the
   **Target SQL** tab shows the
   converted definition if the metadata model has been
   converted.

AWS CLI

###### Browse the metadata

tree

To browse the metadata tree, you follow a repeating pattern: import metadata
at a level, then describe the children at that level. Repeat this process to
drill deeper into the tree.

Start by calling [start-metadata-model-import](../../../cli/latest/reference/dms/start-metadata-model-import.md "../../../cli/latest/reference/dms/start-metadata-model-import.md") with a selection rule that identifies the
top-level metadata model. Include the `server-name` and a top-level
`category-name` (either `Databases` or
`Schemas`, depending on the database engine) in the
`object-locator`. For more information about the selection rules
structure, see [Selection rules in DMS Schema Conversion](sc-selection-rules.md "sc-selection-rules.md").

```
aws dms start-metadata-model-import \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --refresh \
    --selection-rules '{"rules":[{"rule-type":"selection","rule-id":"1",
      "rule-name":"1","object-locator":{"server-name":"`my-server`","category-name":"`top-level-category`"},"rule-action":"explicit"}]}'
```

Import requests are asynchronous. Use [describe-metadata-model-imports](../../../cli/latest/reference/dms/describe-metadata-model-imports.md "../../../cli/latest/reference/dms/describe-metadata-model-imports.md") to check the status before
browsing. Use the `request-id` filter with the
`RequestIdentifier` value returned by
`start-metadata-model-import` to find a specific import:

```
aws dms describe-metadata-model-imports \
    --migration-project-identifier "`my-migration-project`" \
    --filters Name=request-id,Values=`request-identifier`
```

After the import completes, call
[describe-metadata-model-children](../../../cli/latest/reference/dms/describe-metadata-model-children.md "../../../cli/latest/reference/dms/describe-metadata-model-children.md") to retrieve the children at
that level:

```
aws dms describe-metadata-model-children \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --selection-rules '{"rules":[{"rule-type":"selection","rule-id":"1",
      "rule-name":"1","object-locator":{"server-name":"`my-server`"},
      "rule-action":"explicit"}]}'
```

Each child in the response includes a `SelectionRules` field. Pass
these selection rules to the next import and describe calls to drill
deeper:

```
{
    "MetadataModelChildren": [
        {
            "MetadataModelName": "Schemas",
            "SelectionRules": "{\"rules\":[{\"rule-type\":\"selection\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"object-locator\":{\"server-name\":\"src-database-server\",\"category-name\":\"Schemas\"},\"rule-action\":\"explicit\"}]}"
        }
    ]
}
```

To drill into the next level, import at that level using the selection rules
returned from the previous `describe-metadata-model-children` call, and
then describe its children:

```
aws dms start-metadata-model-import \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --refresh \
    --selection-rules '`selection-rules-from-previous-response`'
```

Before describing children, ensure the import has completed by checking its
status with `describe-metadata-model-imports`. Then call
`describe-metadata-model-children`:

```
aws dms describe-metadata-model-children \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --selection-rules '`selection-rules-from-previous-response`'
```

The response returns the children at that level, each with their own
selection rules. Pass these selection rules to the next import and describe
calls to continue drilling deeper into the tree.

```
{
    "MetadataModelChildren": [
        {
            "MetadataModelName": "`child-name`",
            "SelectionRules": "`selection-rules-JSON-string`"
        }
    ]
}
```

**Using --refresh compared to full import**

Use `--refresh` to reload a specific metadata model from the
database. This also loads the names of its direct children. You can list these
children using `describe-metadata-model-children`, but to describe or
browse them further, you must run another import at the child level.

To load an entire subtree (for example, all objects in a schema, a database,
or a specific category such as Tables or Procedures), omit the
`--refresh` flag and change `rule-action` to
`include` in the selection rules:

```
aws dms start-metadata-model-import \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --selection-rules '{"rules":[{"rule-type":"selection","rule-id":"1",
      "rule-name":"1","object-locator":{`...`},
      "rule-action":"include"}]}'
```

Loading a full subtree can take minutes or hours for large schemas and places
load on your database. For interactive exploration, use `--refresh`
and drill into specific branches as needed.

###### Get the definition of

a metadata model

To retrieve the SQL definition of a metadata model, use
[describe-metadata-model](../../../cli/latest/reference/dms/describe-metadata-model.md "../../../cli/latest/reference/dms/describe-metadata-model.md"). Pass the selection rules that identify
the specific metadata model from a previous
`describe-metadata-model-children` response:

```
aws dms describe-metadata-model \
    --migration-project-identifier "`my-migration-project`" \
    --origin `SOURCE` \
    --selection-rules '`selection-rules-for-target-object`'
```

The response includes the metadata model name, type, and SQL definition:

```
{
    "MetadataModelName": "employees",
    "MetadataModelType": "table",
    "Definition": "CREATE TABLE hr.employees(\n    id integer NOT NULL,\n    name varchar(100),\n    department_id integer\n);"
}
```

###### Note

The `Definition` field might not be populated for some metadata
models, such as schemas and categories.

###### View converted

definitions

After you convert source metadata models, the converted definitions are available
on the target tree. There are three ways to retrieve them.

**Using target selection rules from the source
response**

When you describe a source metadata model after conversion, the response
includes a `TargetMetadataModels` field with the target
selection rules:

```
{
    "MetadataModelName": "employees",
    "MetadataModelType": "table",
    "TargetMetadataModels": [
        {
            "MetadataModelName": "employees",
            "SelectionRules": "{\"rules\":[{\"rule-type\":\"selection\",\"rule-id\":\"1\",\"rule-name\":\"1\",\"object-locator\":{\"server-name\":\"tgt-database-server\",\"schema-name\":\"hr\",\"table-name\":\"employees\",\"table-type\":\"table\"},\"rule-action\":\"explicit\"}]}"
        }
    ],
    "Definition": "CREATE TABLE hr.employees(\n    id integer NOT NULL,\n    name varchar(100),\n    department_id integer\n);"
}
```

Pass the selection rules from `TargetMetadataModels` to
`describe-metadata-model` with `--origin TARGET`:

```
aws dms describe-metadata-model \
    --migration-project-identifier "`my-migration-project`" \
    --origin TARGET \
    --selection-rules '`selection-rules-from-TargetMetadataModels`'
```

The response contains the converted SQL definition in the target engine
syntax:

```
{
    "MetadataModelName": "employees",
    "MetadataModelType": "table",
    "Definition": "CREATE TABLE hr.employees (\nid INT NOT NULL,\nname VARCHAR(100) DEFAULT NULL,\ndepartment_id INT DEFAULT NULL,\nPRIMARY KEY (id)\n);"
}
```

**Using get-target-selection-rules**

You can use [get-target-selection-rules](../../../cli/latest/reference/dms/get-target-selection-rules.md "../../../cli/latest/reference/dms/get-target-selection-rules.md") to convert source selection rules into
their target counterparts directly, without first calling
`describe-metadata-model` on the source:

```
aws dms get-target-selection-rules \
    --migration-project-identifier "`my-migration-project`" \
    --selection-rules '`source-selection-rules`'
```

**Navigating the target tree directly**

You can also browse the target tree the same way as the source tree, using
`--origin TARGET`. This is useful when you want to explore all
converted objects without starting from the source.

## Create statement metadata models

###### Note

Statement creation currently supports only the following directions: from SQL Server to Aurora PostgreSQL, or from SQL Server to Amazon RDS for PostgreSQL.

You can create statement metadata models from SQL definitions using [StartMetadataModelCreation](../APIReference/API_StartMetadataModelCreation.md "../APIReference/API_StartMetadataModelCreation.md"). This is useful when you want to convert SQL
statements that do not exist as objects in your source database — for example,
application queries or ad-hoc SQL code.

AWS Management Console
Creating statement metadata models is not available in the AWS
Management Console. Use the AWS CLI or an AWS SDK instead.

AWS CLI
To create a statement metadata model, use [start-metadata-model-creation](../../../cli/latest/reference/dms/start-metadata-model-creation.md "../../../cli/latest/reference/dms/start-metadata-model-creation.md"). The selection rules must
specify a schema that exists in your source database. The created metadata
model appears under the `Statements` category within that
schema.

```
aws dms start-metadata-model-creation \
    --migration-project-identifier "`my-migration-project`" \
    --metadata-model-name "`GetAllEmployees`" \
    --selection-rules '{"rules":[{"rule-type":"selection","rule-id":"1",
      "rule-name":"1","object-locator":{"server-name":"`my-server`",
      "database-name":"`my_database`","schema-name":"`dbo`"},
      "rule-action":"explicit"}]}' \
    --properties '{"StatementProperties":{"Definition":"SELECT * FROM dbo.Employees;"}}'
```

After creation, you can find the metadata model in the tree under the
`Statements` category and describe it:

```
{
    "MetadataModelName": "GetAllEmployees",
    "MetadataModelType": "statement",
    "Definition": "SELECT * FROM dbo.Employees;"
}
```

After creation, you can run any supported operation on the statement
metadata model, such as assessment, conversion, or export.

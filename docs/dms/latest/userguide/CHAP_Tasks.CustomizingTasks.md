# Using table mapping to

specify task settings

Table mapping uses several types of rules to specify the data source, source schema,
data, and any transformations that should occur during the task. You can use table
mapping to specify individual tables in a database to migrate and the schema to use for
the migration.

When working with table mapping, you can use filters to specify data that you want
replicated from table columns. In addition, you can use transformations to modify
selected schemas, tables, or views before they are written to the target
database.

###### Topics

- [Specifying table
  selection and transformations rules from the console](CHAP_Tasks.CustomizingTasks.TableMapping.md "CHAP_Tasks.CustomizingTasks.TableMapping.md")
- [Specifying table selection and transformations rules using
  JSON](CHAP_Tasks.CustomizingTasks.TableMapping.md "CHAP_Tasks.CustomizingTasks.TableMapping.md")
- [Selection rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")
- [Wildcards in table mapping](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")
- [Transformation rules and actions](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")
- [Using transformation rule expressions to define column content](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")
- [Table and collection settings rules and operations](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")
- [Using data masking to hide sensitive information](CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md "CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.md")

###### Note

When working with table mapping for a MongoDB source endpoint, you can use filters to specify
data that you want replicated, and specify a database name in place of the
`schema_name`. Or, you can use the default
`"%"`.

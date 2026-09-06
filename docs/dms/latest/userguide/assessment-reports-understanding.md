

# Understanding conversion assessment report metrics
<a name="assessment-reports-understanding"></a>

The conversion assessment report analyzes incompatibilities between your source and target database engines. It identifies which database objects DMS Schema Conversion can convert automatically, and which database objects require manual action to complete the conversion to your target database engine.

The report reflects the current state of your migration project. After you run an assessment, the report shows all of the action items that DMS Schema Conversion identified and the database objects that are candidates for conversion using generative AI. After you run a conversion, the report shows the action items that still require manual resolution, and marks the database objects that DMS Schema Conversion converted using generative AI so that you can verify the generated code.

Running an assessment is recommended, but it is optional. The same conversion statistics, action items, and complexity categories that an assessment provides are also available after you run a conversion operation. You do not need to run an assessment before you convert your schema.

## Complexity categories
<a name="assessment-reports-understanding-complexity"></a>

DMS Schema Conversion classifies every database object into one of four complexity categories, based on how much manual effort is required to convert the object to your target database engine. The **Summary** tab and the Summary CSV file report the number of database objects in each category, for every object type (such as tables, views, procedures, triggers, indexes, constraints, and sequences).


**Complexity categories**  

| Category | Description | 
| --- | --- | 
| Automatically converted | DMS Schema Conversion converts the database object to your target database engine without any manual action. These database objects have no associated action items. | 
| Simple actions | The database object has one or more action items that require manual action, but resolving them requires relatively little effort. | 
| Medium-complexity actions | The database object has an action item that requires a moderate amount of manual effort to resolve, such as rewriting part of the object's logic for compatibility with your target database engine. | 
| Complex actions | The database object has an action item that requires significant manual effort to resolve, such as redesigning the object's logic to work with your target database engine. | 

DMS Schema Conversion determines a database object's category from the action items that apply to it. A database object with no action items is automatically converted. A database object with one or more action items is classified by the highest complexity among those action items — for example, a database object with both a simple action item and a medium-complexity action item is classified as medium-complexity. Note that a database object with many simple action items can also be classified as complex if the sum of the effort values for those simple action items exceeds the effort threshold for a complex action item.

The Summary CSV file that you can export from the report (see [Saving assessment reports](assessment-reports.md#assessment-reports-save)) reports these categories using the following column headers, with one row for each object type: `Category`, `Number of objects`, `Objects automatically converted`, `Objects with simple actions`, `Objects with medium-complexity actions`, `Objects with complex actions`, and `Total lines of code`.

## Effort estimates
<a name="assessment-reports-understanding-effort"></a>

For each action item, the conversion assessment report provides two effort estimates that together indicate how much manual work is required to convert the affected database objects:
+ **Learning curve effort** — The one-time cost to design a conversion approach for a given action item type. You incur this effort once per action item type, regardless of how many database objects are affected by that type of issue.
+ **Effort to convert an occurrence** — The cost to convert each individual occurrence of the action item, following the conversion approach that you designed. You incur this effort once for every database object affected by the action item.

DMS Schema Conversion reports both effort values in the `Action_Items_Summary` CSV file, along with the schema, action item, number of occurrences, action item description, and recommended action for each action item type. For more information about this file, see [Saving your conversion assessment report for DMS Schema Conversion](assessment-reports.md#assessment-reports-save).

Effort values use a weighted scale that ranges from low (least effort) to high (most effort). Use these values, together with the number of occurrences, to estimate the total effort required to resolve each action item type. For more information about calculating total effort, see [Using the conversion assessment report for migration planning](assessment-reports-planning.md).

## Action item codes
<a name="assessment-reports-understanding-codes"></a>

Each action item in your conversion assessment report has an **action item code** — a numeric identifier that categorizes the specific type of conversion issue. DMS Schema Conversion assigns the same code to every occurrence of the same issue type, so you can use the code to group and track related action items across your database objects.

The following table shows three action item codes from a sample conversion assessment report, illustrating how codes span different complexity levels.


**Example action item codes**  

| Code | Description | Complexity | Recommended action | 
| --- | --- | --- | --- | 
| 5075 | PostgreSQL does not support the WITH READ ONLY clause for views | Simple actions | Revise your code to use views without the subquery restriction clause. | 
| 5201 | PostgreSQL does not support this partition type | Medium-complexity actions | Convert your source code manually. | 
| 5340 | DMS SC cannot convert functions | Complex actions | Revise your code to use another function or create a user-defined function. | 

Action item codes do not follow a numbering scheme that corresponds to a specific complexity category or database object type. To find the complexity category, effort estimates, and recommended action for a specific code, see the `Action_Items_Summary` CSV file or the **Action items** tab in the AWS DMS console.

## Conversion statistics and SQL metrics
<a name="assessment-reports-understanding-statistics"></a>

In addition to reporting complexity categories for each object type, the **Summary** tab and the Summary CSV file (see [Saving assessment reports](assessment-reports.md#assessment-reports-save)) report the following aggregate statistics for your entire source schema:
+ **Storage objects count** — The total number of database storage objects in your schema, such as tables, indexes, constraints, and sequences, and how many of them DMS Schema Conversion converted automatically.
+ **Code objects count** — The total number of database code objects in your schema, such as procedures, functions, views, and triggers, and how many of them DMS Schema Conversion converted automatically.
+ **Total lines of code** — The number of lines of source code in the database objects of each object type. DMS Schema Conversion reports this value per object type in the Summary CSV file, so that you can gauge the relative size of each type of object in your schema.
+ **SQL syntax elements number** — The total number of SQL syntax constructs that DMS Schema Conversion parsed across all of your database objects, and how many of those constructs it converted automatically. A single database object can contain many SQL syntax elements, so this value is typically much larger than the storage and code object counts. Use it as a more granular measure of conversion coverage across your schema.

The Summary CSV file reports the storage objects count, code objects count, and SQL syntax elements number as their own rows, alongside a row for every database object type in your schema. For example, a report might show a `Storage_objects_count` of 747, with 663 objects automatically converted; a `Code_objects_count` of 253, with 213 objects automatically converted; and an `SQL_syntax_elements_number` of 178091, with 176745 elements automatically converted. The specific numbers in your report depend on the size and complexity of your source schema.

For every object type — such as tables, views, procedures, triggers, indexes, constraints, and sequences — the summary reports the number of objects of that type and how those objects are distributed across the four complexity categories: automatically converted, simple actions, medium-complexity actions, and complex actions. For example, a report might show 474 tables in total, with 379 automatically converted, 29 with simple actions, 6 with medium-complexity actions, and 60 with complex actions. Comparing the distribution across object types can help you identify which types of objects in your schema need the most manual conversion effort. For more information about the complexity categories, see [Complexity categories](#assessment-reports-understanding-complexity).

To use these statistics to estimate the overall scope of your migration, see [Using the conversion assessment report for migration planning](assessment-reports-planning.md).
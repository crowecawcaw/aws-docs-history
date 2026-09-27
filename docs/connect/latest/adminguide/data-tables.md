

# Create and configure data tables
<a name="data-tables"></a>

## What are data tables?
<a name="understanding-data-tables"></a>

With data tables, you can store and manage data that affects your configurations within Connect Customer. You define their structure as attributes (columns) and values (rows), with validation rules that enforce data integrity. Other resources, such as flows and views, reference that data at runtime. For example, a flow can read a value to decide how to route a contact, and a view can display a value to an agent. The data lives in the table rather than in the resources that use it, so you can change a value directly, and the update takes effect immediately.

Data tables support use cases that range from simple routing rules to complex, time-based configurations, all editable in real time. Unlike [predefined attributes](predefined-attributes.md), which store a named list of values, a data table can have multiple columns, a range of data types, and references between tables.

For example, a data table can map each store location to its business hours and support queue. A flow can look up the caller's location in the table and route the contact based on whether that store is open. You update the table directly, so you can change hours or queues without editing the flow, and without granting access to sensitive flow resources.

In addition to entering a value directly, you can calculate it with an expression. For example, an expression can return a morning or afternoon greeting based on the current time, or look up a value in another data table. Expressions are evaluated when the value is read, so the result stays current. For more information, see [Data table expressions](#data-tables-expressions).

A data table consists of:
+ Table metadata (structure and validation rules)
+ Table values (the actual data)

Table metadata includes:
+ Attributes (columns) with defined data types
+ Primary keys to identify unique records
+ Optional validation rules for data integrity

Table values are stored in records (rows) that contain values for each attribute (column).

## Sample use case
<a name="data-tables-sample-use-case"></a>

The following example builds a simple translations table that stores a prompt for each language.

1. Create a data table with a primary attribute named `Language`. The primary attribute is the key used to look up a record in the table.

1. Add an attribute for each message type, such as `Greeting`. To support a large number of message types, use the advanced example that follows, which adds primary attributes instead of a separate column for each message type.

1. Add a record for each language.

The table looks like this:


| Language (primary attribute) | Greeting | 
| --- | --- | 
| English | Hello | 
| Spanish | Hola | 

To look up a value along more than one dimension, add more primary attributes. For example, a `Department` primary attribute lets each greeting vary by both language and department.


| Language (primary attribute) | Department (primary attribute) | Greeting | 
| --- | --- | --- | 
| English | Sales | Hello. This is sales. | 
| Spanish | Sales | Hola. Soy del departamento de ventas. | 
| English | Marketing | Hi. You've reached marketing. | 

Add a third primary attribute, `Message type`, to identify each message precisely.


| Language (primary attribute) | Department (primary attribute) | Message type (primary attribute) | Message | 
| --- | --- | --- | --- | 
| English | Sales | Greeting | Hello. This is sales. | 
| Spanish | Sales | Greeting | Hola. Soy del departamento de ventas. | 
| English | Marketing | Greeting | Hi. You've reached marketing. | 
| English | Marketing | Farewell | Thanks for contacting marketing. | 

## Create data tables
<a name="create-data-tables"></a>

1. Go to the Routing menu and choose **Data tables**.

1. Choose **Add new data table**.

   1. Provide a **Name**.

   1. (Optional) Provide a **Description**.

   1. Indicate a **Time zone** to support time-based use cases.

   1. Define a **Lock level**. Locking prevents multiple editors from overwriting changes at the data table, record (row), attribute (column), or value (cell) level.

1. After saving, choose **Add attribute** to define the first column of the table.
**Note**  
Primary attributes appear first, followed by the other attributes. Within each group, attributes are sorted alphabetically by name.

   1. Provide a **Name**.

   1. Choose a **Type**:

      1. **Single** text, number, or boolean (yes/no) attribute

      1. **List** of text or numbers

   1. (Optional) Choose **Use as primary attribute**.

      1. Primary keys help identify and reference specific records. They also enable granular access control to table data. One or more attributes can be designated as primary, and become the first column(s) of the table. If no primary attribute is defined, the table can contain only one record.
**Note**  
Primary attributes cannot be added or removed if the table contains data. For example, if a table's primary attributes are first name, last name, and middle initial, you cannot add SSN as another primary attribute or remove middle initial without first deleting all records. However, you can edit the values in a primary attribute, for example a last name can be changed. You can also add non-primary attributes after a table is populated with data.

   1. (Optional) Provide **Basic validation** if the type is text or numeric (for example, max length).

   1. (Optional) Update **Collection validation** if the type is text or numeric, to provide a choice of predefined values for this attribute, and even restrict to those values.

   1. Upon saving, your table displays its first attribute (column).

   1. Repeat as needed.

![Data table management page.](https://docs.aws.amazon.com/connect/latest/adminguide/images/data-table-management.png)


## Add records to data tables
<a name="add-records-to-data-tables"></a>

A record is a row of values in a data table. How you add a record depends on whether the table has primary attributes. When you add or edit a record, Connect Customer enforces the required fields, data types, length limits, and other validation rules specified in the table definition.

For data tables with primary attributes, each record is uniquely identified by its primary values. To add a record, choose **Add record**, and then enter the primary values along with the value for each attribute. These tables also have a [default record](#data-tables-default-values), which provides the values that are returned when a lookup does not match a record. To set the default record, choose the actions menu (the ellipsis icon) on the first (default) record, and then choose **Edit default record**.

Data tables without primary attributes can contain only one record, which is the default record. Choose **Add record** to set the values of the default record.

When you add the first record, you must confirm that the table's primary attributes can no longer be changed once it contains data. Connect Customer sorts records by their primary values; for example, when the first primary attribute is text, records are ordered alphabetically.

For more information about default records and the values that Connect Customer returns when a lookup does not match a record, see [Default values](#data-tables-default-values).

## Edit data tables and their records
<a name="edit-data-tables-and-their-records"></a>

You can edit a data table's records at any time, and you can change most of its structure. After a data table contains data, you cannot add or remove primary attributes, but you can rename them and add non-primary attributes. When you save a change, Connect Customer validates it against the table definition, enforcing the same required fields, data types, and length limits that apply when you add a record. To keep multiple editors from overwriting each other's changes, you can lock edits. For more information, see [Prevent conflicting edits with lock levels](#data-tables-lock-levels).

To edit a single value, choose its cell in the table and enter the new value. To add a whole record, choose **Add record**. To edit the table's default record, choose the actions menu (the ellipsis icon), and then choose **Edit default record**.

Changes take effect almost immediately. An update applies to later flow runs and API calls, and flows do not cache table data, so no refresh is required after a change.

**Note**  
While changes propagate rapidly, in rare cases, there might be a brief delay, typically just milliseconds, before all system components reflect the change. When feasible, plan updates during operational windows to minimize impact.

**Note**  
Always test configurations that impact flows before impacting production workloads, and monitor system behavior immediately after significant changes.

## Default values
<a name="data-tables-default-values"></a>

A data table always returns a value that conforms to the attribute's type, so resources that reference the table, such as flows and views, always receive a usable value. Connect Customer provides this guarantee through two levels of defaults: a default record that supplies fallback values when a lookup does not match a record, and a built-in default for each value type. When a value is requested, Connect Customer resolves it in the following order:

1. If the requested record contains a value for the attribute, that value is returned.

1. If the requested primary values do not match a record, the value from the default record is returned.

1. If the default record does not define the attribute, or the data table has no default record, the default for the attribute's value type is returned.

The following table lists the default for each value type.


| Value type | Default value | 
| --- | --- | 
| Text | Empty string (`""`) | 
| Number | `0` | 
| Boolean | `false` | 
| Text list | Empty list (`[]`) | 
| Number list | Empty list (`[]`) | 

For example, consider a data table with a `Language` primary attribute and a `Greeting` attribute.


| Language (primary attribute) | Greeting | 
| --- | --- | 
| (Default) | Hello | 
| Spanish | Hola | 

A lookup for `Spanish` returns `Hola`. A lookup for a language that has no record, such as `French`, returns the default record's value, `Hello`. If the data table had no default record, the same lookup would return an empty string, which is the default for the text value type.

The default record supplies the fallback value for each attribute. To set these values, choose the actions menu (the ellipsis icon), and then choose **Edit default record**. If a data table has no primary attributes, it contains only the default record; choose **Add record** to set its values. For more information, see [Add records to data tables](#add-records-to-data-tables).

As a result, a data table never returns a null value. Every attribute always resolves to a value of its declared type.

## Prevent conflicting edits with lock levels
<a name="data-tables-lock-levels"></a>

Data table values can be updated at any time by multiple people and automated processes, including flows and API calls. To prevent one editor from unintentionally overwriting another editor's changes, each data table has a **lock level**. You set the lock level when you create a data table, and you can change it at any time.

Locking is optimistic. Reading values is never blocked. An update is applied only if no conflicting change was made within the locked scope since the values were last read. If a conflicting change occurred, the update is rejected, and the editor must refresh to load the latest values before trying again. The lock level determines the scope at which a concurrent change blocks an update.


| Lock level | Behavior | 
| --- | --- | 
| Data table | An update is rejected if any value in the table changed since the values were last read. This is the most restrictive lock level, and effectively allows only one editor to change the table at a time. | 
| Record (row) | An update is rejected if any value in the same record changed. Edits to different records can proceed at the same time. If the table has no primary attributes, it contains a single record, so this lock level behaves like the data table lock level. | 
| Attribute (column) | An update is rejected if any value for the same attribute changed. Edits to different attributes can proceed at the same time. | 
| Value (cell) | An update is rejected only if that same value changed. Edits to any other value can proceed at the same time. This is the least restrictive lock level that still prevents overwrites. | 
| None | Updates are not locked. Concurrent updates are allowed, and the most recent update overwrites earlier ones. This is the default. | 

You set a data table's lock level when you create it, and you can change the lock level at any time.

## Import and export data table values
<a name="import-and-export-data-table-values"></a>

You can import and export a data table's values to and from a CSV file, for making bulk edits, migrating data from another system, or capturing a point-in-time backup before a major change. Both operations act on values only (rows), not on the table's attributes (columns) and validation rules.

To export values, open the data table and choose **Export to CSV**. Connect Customer downloads the table's values as a CSV file, with one column for each attribute.

To import values from a CSV file:

1. Choose the arrow next to **Export to CSV**, then choose **Import using CSV**.

1. On the **Upload file** step, choose **Choose file**, select a file, then choose **Next**.

1. On the **Map attributes** step, map the CSV columns to data table attributes if necessary. Columns are mapped automatically when the column name matches an attribute name. The table's primary attributes must be mapped to a unique column or set of columns.

1. For **Existing value handling**, choose **Create new values only** or **Create and overwrite mapped values**, then choose **Next**.
**Note**  
Importing never deletes values from a data table. **Create new values only** leaves existing values unchanged, and **Create and overwrite mapped values** updates matching values, but neither option removes values.

1. On the **Review and import** step, choose **Import values**.

## Data table expressions
<a name="data-tables-expressions"></a>

Instead of entering a value directly, you can compute it with an expression, similar to a formula in a spreadsheet. An expression begins with an equals sign (`=`) and combines functions and operators to reference values in the same table or other tables, apply conditional logic, format values, and perform calculations. Expressions are supported for the text, number, and boolean value types. They are not supported for list value types or for primary attributes.

Editing expression values requires the **Data tables - Edit expressions** permission. For more information, see [Security profiles for Connect Customer and Contact Control Panel (CCP) access](connect-security-profiles.md).

Expressions are evaluated at the time a value is requested. If an expression cannot be evaluated, the attribute's default value is returned. For more information, see [Default values](#data-tables-default-values).

The following functions are available in expressions. In the function signatures, arguments shown in square brackets are optional.


| Function | Description | 
| --- | --- | 
| `LOOKUP(attribute, [primaryAttribute, value]...)` | Returns the value of an attribute from a record in the current table, identified by one or more primary attribute and value pairs. | 
| `XLOOKUP(tableIdOrArn, attribute, [primaryAttribute, value]...)` | Returns the value of an attribute from a record in another table, identified by one or more primary attribute and value pairs. | 
| `ALOOKUP(tableIdOrArn, attribute, valueOnError, valueOnInvalid, valueOnNotFound, [primaryAttribute, value]...)` | Works like `XLOOKUP`, but returns the fallback value that you specify when the lookup returns an error, returns an invalid value, or does not find a record. | 
| `IF(condition, valueIfTrue, valueIfFalse)` | Returns one value when the condition is true and another when it is false. | 
| `AND(boolean, ...)` | Returns true when all arguments are true. | 
| `OR(boolean, ...)` | Returns true when at least one argument is true. | 
| `NOT(boolean)` | Returns the opposite of the boolean argument. | 
| `EQ(value1, value2)` | Returns true when the two values are equal. | 
| `COALESCE(value, ...)` | Returns the first argument that is not empty. | 
| `GT(number1, number2)` | Returns true when the first number is greater than the second. | 
| `GTE(number1, number2)` | Returns true when the first number is greater than or equal to the second. | 
| `LT(number1, number2)` | Returns true when the first number is less than the second. | 
| `LTE(number1, number2)` | Returns true when the first number is less than or equal to the second. | 
| `ADD(number, ...)` | Returns the sum of the numbers. Also available as `SUM`. | 
| `SUBTRACT(number1, number2)` | Returns the first number minus the second. | 
| `MULTIPLY(number, ...)` | Returns the product of the numbers. | 
| `DIVIDE(dividend, divisor)` | Returns the dividend divided by the divisor. | 
| `CEILING(number, [factor])` | Rounds a number up, optionally to the nearest multiple of a factor. | 
| `FLOOR(number, [factor])` | Rounds a number down, optionally to the nearest multiple of a factor. | 
| `ROUND(number, [places])` | Rounds a number to the nearest value, optionally to a number of decimal places. | 
| `ROUNDUP(number, [places])` | Rounds a number up, optionally to a number of decimal places. | 
| `ROUNDDOWN(number, [places])` | Rounds a number down, optionally to a number of decimal places. | 
| `CONCAT(value, ...)` | Combines values into a single text string. | 
| `JOIN(delimiter, value, ...)` | Combines values into a single text string separated by the delimiter. | 
| `TEXT(number, [format])` | Converts a number to text, optionally applying a number format. | 
| `NUMBER(text)` | Converts text to a number. | 
| `BOOLEAN(text)` | Converts text to a boolean. | 
| `NOW()` | Returns the current date and time in ISO 8601 format. | 
| `HOUR([datetime])` | Returns the hour, from 0 to 23. If no argument is provided, the current date and time is used. | 
| `MINUTE([datetime])` | Returns the minute, from 0 to 59. If no argument is provided, the current date and time is used. | 
| `SECOND([datetime])` | Returns the second, from 0 to 59. If no argument is provided, the current date and time is used. | 
| `DAY([datetime])` | Returns the day of the month. If no argument is provided, the current date and time is used. | 
| `MONTH([datetime])` | Returns the month of the year. If no argument is provided, the current date and time is used. | 
| `YEAR([datetime])` | Returns the year. If no argument is provided, the current date and time is used. | 
| `WEEKDAY([datetime])` | Returns the day of the week as a number. If no argument is provided, the current date and time is used. | 
| `INDEX(list, position)` | Returns the item at the specified position in a list. | 
| `IFERROR(expression, fallback)` | Returns the result of the expression, or the fallback value when the expression produces an error. | 
| `HOOP(hoursOfOperationIdOrArn, valueIfOpen, valueIfClosed, [timeShift])` | Returns one value when the specified hours of operation are currently open and another when they are closed. | 

The following example looks up a message in a separate messages table. It returns the value of the `Message` attribute for the record where the `Language` primary attribute is `English` and the `Department` primary attribute is `Sales`:

```
=XLOOKUP("{{messages-table-arn}}", "Message", "Language", "English", "Department", "Sales")
```

The following example returns a different greeting depending on the current hour. Called with no argument, `HOUR` uses the current time and returns the hour in the data table's configured time zone:

```
=IF(HOUR() < 12, "Good morning", "Good afternoon")
```

## Using data tables for dynamic lookups in flows
<a name="data-tables-dynamic-lookups-in-flows"></a>

Flows can read and write values from data tables. For more information, see [Flow block in Connect Customer: Data Table](data-table-block.md).

After a data table query runs in your flow, you can reference the retrieved values in subsequent blocks using the following namespace format:

```
$.DataTables.{{QueryName}}.{{AttributeName}}
```

For attribute names that contain spaces or special characters, use bracket notation:

```
$.DataTables.{{QueryName}}['{{attribute name}}']
```

For example, if you have a query named `TranslationLookup` that retrieves a `Greeting` attribute, reference it as `$.DataTables.TranslationLookup.Greeting`.

**Note**  
When you use the **Data tables** namespace dropdown in the block configuration UI, the `$.DataTables.` prefix must be omitted. The UI adds it automatically.

## Use data tables to build custom user interfaces
<a name="data-tables-custom-user-interfaces"></a>

Data tables let business users make routine operational adjustments without direct access to the underlying Connect Customer configuration. Using the UI builder, you build custom interfaces from data tables and assign them to workspaces, where your operations team uses them to respond to changing conditions without engaging IT. A single table can bring together values from several resources, so business users can act on those values without holding permissions to each underlying resource, such as flows, prompts, and queues.

Purpose-built interfaces can allow authorized business users to control scenarios such as:
+ Managing queue assignments, operating hours, skill mappings, and escalation rules
+ Modifying routing by language, location, or VIP status
+ Activating emergency protocols

For more information about building custom interfaces, see the [UI builder](no-code-ui-builder.md).

## Access control and security for data tables
<a name="data-tables-access-control-and-security"></a>

You can control access to data tables so that business users can view and modify only the data that relates to their responsibilities. Connect Customer provides three access control mechanisms, which you can combine:
+ Security profile permissions provide view, edit, create, and delete choices for managing the data table resource.
+ Tag-based access control (TBAC) provides table-level restrictions. It controls which data tables a user can access, based on the tags assigned to each table. TBAC does not restrict access to individual records within a table. For more information, see [Apply tag-based access control in Connect Customer](tag-based-access-control.md).
+ Record-based access control restricts a user to specific records (rows) within a table, based on primary attribute values. You configure it on a [security profile](connect-security-profiles.md) by specifying primary attributes and the values that a user can access. Any data table that contains a primary attribute with a matching name is then restricted to the records that have those primary values. Use record-based access control when multiple teams need to access different subsets of data within large, multi-purpose tables. For more information, see [Apply record-based access control in Connect Customer](record-based-access-control.md).
**Note**  
Record-based access control relies on the primary attributes of a table. For more information about primary attributes, see the description of **Use as primary attribute** in the steps to create a data table earlier in this topic.

## Service quotas for data tables
<a name="service-quotas-for-data-tables"></a>

Connect Customer applies the following default quotas to data tables:
+ Tables: 100 total for each instance
+ Attributes (columns): 100 for each table
+ Values (cells): 1,000 for each table
+ Lists: 100 items for text and number list values
+ Characters: 5,000 for non-primary text values, 1,000 for TEXT\_LIST items and primary text values

To learn more about service quotas and how to manage them, see [Connect Customer service quotas](amazon-connect-service-limits.md).

## Track changes to data tables
<a name="track-changes-to-data-tables"></a>

The on-screen audit history shows recent changes to a data table, along with the before and after values. It covers changes to the table's structure, such as attributes, primary keys, and default values, as well as records that are added or changed.

To view the audit history, choose **View historical changes** at the bottom of the **Data table management** page.

**Note**  
AWS CloudTrail tracks the history of all resource changes. For more information, see [Log Connect Customer API calls with AWS CloudTrail](logging-using-cloudtrail.md).
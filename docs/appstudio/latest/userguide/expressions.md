# Using JavaScript to write expressions in App Studio

In AWS App Studio, you can use JavaScript expressions to dynamically control
the behavior and appearance of your applications. Single-line JavaScript expressions are written
within double curly braces, `{{ }}`, and can be used in various contexts such as automations, UI components,
and data queries. These expressions are evaluated at runtime and can be used to perform calculations,
manipulate data, and control application logic.

App Studio provides native support for three JavaScript open source
libraries: Luxon, UUID, Lodash as well as SDK integrations to detect JavaScript syntax and type-checking errors within your app's configurations.

###### Important

App Studio does not support using third-party or custom JavaScript libraries.

## Basic syntax

JavaScript expressions can include variables, literals, operators, and function calls.
Expressions are commonly used to perform calculations or evaluate conditions.

See the following examples:

- `{{ 2 + 3 }}` will evaluate to 5.
- `{{ "Hello, " + "World!" }}` will evaluate to "Hello, World!".
- `{{ Math.max(5, 10) }}` will evaluate to 10.
- `{{ Math.random() * 10 }}` returns a random number (with decimals) between [0-10).

## Interpolation

You can also use JavaScript to interpolate dynamic values within static text.
This is achieved by enclosing the JavaScript expression within double curly braces, like the following example:

```
Hello {{ currentUser.firstName }}, welcome to App Studio!
```

In this example, `currentUser.firstName` is a JavaScript expression that retrieves the first name of the current user,
which is then dynamically inserted into the greeting message.

## Concatenation

You can concatenate strings and variables using the `+` operator in JavaScript, as in the following example.

```
{{ currentRow.FirstName + " " + currentRow.LastName }}
```

This expression combines the values of `currentRow.FirstName` and `currentRow.LastName` with a space in between,
resulting in the full name of the current row. For example, if `currentRow.FirstName` is `John`, and `currentRow.LastName` is
`Doe`, then the expression would resolve to `John Doe`.

## Date and time

JavaScript provides various functions and objects for working with dates and times. For example:

- `{{ new Date().toLocaleDateString() }}`: Returns the current date in a localized format.
- `{{ DateTime.now().toISODate() }}`: Returns the current date in YYYY-MM-DD format, for use in the Date component.

### Date and time comparison

Use operators such as `=`, `>`, `<`, `>=`, or `<=` to compare date or time values. For example:

- `{{ui.`timeInput`.value > "10:00 AM"}}`: Checks if the time is after 10:00 AM.
- `{{ui.`timeInput`.value <= "5:00 PM"}}`: Checks if the time is at or before 5:00 PM.
- `{{ui.`timeInput`.value > DateTime.now().toISOTime()}}`: Checks if the time is after the current time.
- `{{ui.`dateInput`.value > DateTime.now().toISODate()}}`: Checks if the date is before the current date.
- `{{ DateTime.fromISO(ui.`dateInput`.value).diff(DateTime.now(), "days").days >= 5 }}`:
  Checks if the date is at least 5 days from the current date.

## Code blocks

In addition to expressions, you can also write multi-line JavaScript code blocks.
Unlike expressions, code blocks do not require curly braces. Instead, you can write your
JavaScript code directly within the code block editor.

###### Note

While expressions are evaluated and their values are displayed, code blocks are run, and their output (if any) is displayed.

## Global variables and functions

App Studio provides access to certain global variables and functions that can be used within your
JavaScript expressions and code blocks. For example, `currentUser` is a global variable that represents the
currently logged-in user, and you can access properties like `currentUser.role` to retrieve the user's role.

## Referencing or updating UI component values

You can use expressions in components and automation actions to both reference and update UI component values.
By programmatically referencing and updating component values, you can create dynamic and interactive user
interfaces that respond to user input and data changes.

### Referencing UI component values

You can create interactive and data-driven applications by implementing dynamic behavior by accessing values from UI components.

You can access values and properties of UI components on the same page by using the `ui` namespace in expressions.
By referencing a component's name, you can retrieve its value or perform operations based on its state.

###### Note

The `ui` namespace will only show components on the current page, as components are scoped to their respective pages.

The basic syntax for referring to components in an App Studio app is: `{{ui.`componentName`}}`.

The following list contains examples for using the `ui` namespace to access UI component values:

- `{{ui.`textInputName`.value}}`: Represents the value of a text input component named `textInputName`.
- `{{ui.`formName`.isValid}}`: Check if all fields in the form named `formName` are valid based on your provided
  validation criteria.
- `{{ui.`tableName`.currentRow.`columnName`}}`: Represents the value of a specific column in the current row of a table
  component named `tableName`.
- `{{ui.`tableName`.selectedRowData.`fieldName`}}`: Represents the value of the specified field from the
  selected row in a table component named `tableName`. You can then append
  a field name such as `ID`
  (`{{ui.`tableName`.selectedRowData.`ID`}}`) to
  reference the value of that field from the selected row.

The following list contains more specific examples of referencing component values:

- `{{ui.`inputText1`.value.trim().length > 0}}`: Check if the value of the
  `inputText1` component, after trimming any leading or trailing whitespace, has a non-empty string.
  This can be useful for validating user input or enabling/disabling other components based on the input text field's value.
- `{{ui.`multiSelect1`.value.join(", ")}}`: For a multi-select component named `multiSelect1`,
  this expression converts the array of selected option values into a comma-separated string. This can be helpful for
  displaying the selected options in a user-friendly format or passing the selections to another component or automation.
- `{{ui.`multiSelect1`.value.includes("`option1`")}}`:
  This expression checks if the value `option1` is included in the array of selected options for the
  `multiSelect1` component. It returns true if `option1` is selected, and false otherwise.
  This can be useful for conditionally rendering components or taking actions based on specific option selections.
- `{{ui.`s3Upload1`.files.length > 0}}`: For an Amazon S3 file upload component named `s3Upload1`,
  this expression checks if any files have been uploaded by checking the length of the files array. It can be useful for
  enabling/disabling other components or actions based on whether files have been uploaded.
- `{{ui.`s3Upload1`.files.filter(file => file.type === "`image/png`").length}}`: This
  expression filters the list of uploaded files in the `s3Upload1` component to only include PNG image files,
  and returns the count of those files. This can be helpful for validating or displaying information about the types of files uploaded.

### Updating UI component values

To update or manipulate the value of a component, use
the `RunComponentAction` within an automation. Here's an example of the syntax you can use to update the value of a
text input component named `myInput` using the `RunComponentAction` action:

```
RunComponentAction(ui.`myInput`, "setValue", "`New Value`")
```

In this example, the `RunComponentAction` step calls the `setValue` action on the `myInput`
component, passing in the new value, `New Value`.

## Working with table data

You can access table data and values to perform operations. You can use the following expressions to access table data:

- `currentRow`: Used to access table data from the current row within the table. For example, setting a table action's name, sending a value from the
  row to an automation that is started from an action, or using values from existing columns in a table to create a new column.
- `ui.`tableName`.selectedRow` and `ui.`tableName`.selectedRowData`
  are both used to access table data from other components on the page. For example, setting
  a button's name outside of the table based on the selected row. The values returned are the same, but the differences between
  `selectedRow` and `selectedRowData` are as follows:
  - `selectedRow`: This namespace includes the name shown in the column header for each field. You should use `selectedRow` when
    referencing a value from a visible column in the table. For example, if you have a custom or computed column in your table that doesn't exist as a field in the entity.
  - `selectedRowData`: This namespace includes the fields in the entity used as a source for the table. You should use `selectedRowData`
    to reference a value from the entity that isn't visible in the table, but is useful for other components or automations in your app.

The following list contains examples of accessing table data in expressions:

- `{{ui.`tableName`.selectedRow.`columnNameWithNoSpace`}}`: Returns the value of the
  `columnNameWithNoSpace` column from the selected row in the table.
- `{{ui.`tableName`.selectedRow.['`Column Name With Space`']}}`: Returns the value of the
  `Column Name With Space` column from the selected row in the table.
- `{{ui.`tableName`.selectedRowData.`fieldName`}}`: Returns the value of the
  `fieldName` entity field from the selected row in the table.
- `{{ui.`tableName`.selectedRows[0].`columnMappingName`}}`:
  Reference the selected row's column name from other components or expressions on the same page.
- `{{currentRow.`firstName` + ' ' + currentRow.`lastNamecolumnMapping`}}`: Concatenate values from
  multiple columns to create a new column in a table.
- `{{ { "Blocked": "🔴", "Delayed": "🟡", "On track": "🟢" }[currentRow.`statuscolumnMapping`] + " " + 
currentRow.`statuscolumnMapping`}}`:
  Customize the display value of a field within a table based on the stored status value.
- `{{currentRow.`colName`}}`, `{{currentRow["`First Name`"]}}`, `{{currentRow}}`,
  or `{{ui.`tableName`.selectedRows[0]}}`: Pass the referenced row's context within a row action.

## Accessing automations

You can use automations to run server-side logic and operations in App Studio. Within automation actions, you can use
expressions to process data, generate dynamic values, and incorporate results from previous actions.

### Accessing automation parameters

You can pass dynamic values from UI components and other automations into automations, making them reusable and flexible.
This is done using automation parameters with the `params` namespace as follows:

`{{params.`parameterName`}}`: Reference a value passed into the automation from a UI component or
other source. For example, `{{params.`ID`}}` would reference a parameter named `ID`.

#### Manipulating automation parameters

You can use JavaScript to manipulate automation parameters. See the following examples:

- `{{params.`firstName`}} {{params.`lastName`}}`: Concatenate values passed as parameters.
- `{{params.`numberParam1` + params.`numberParam2`}}`: Add two number parameters.
- `{{params.`valueProvided`?.length > 0 ? params.`valueProvided` : '`Default`'}}`: Check if a parameter is
  not null or undefined, and has a non-zero length. If true, use the provided value; otherwise, set a default value.
- `{{params.`rootCause` || "`No root cause provided`"}}`:
  If the `params.`rootCause`` parameter is false (null, undefined, or an empty string), use the provided default value.
- `{{Math.min(params.`numberOfProducts`, `100`)}}`: Restrict the value of a parameter to a
  maximum value (in this case, `100`).
- `{{ DateTime.fromISO(params.`startDate`).plus({ days: 7 }).toISO() }}`: If the
  `params.`startDate``parameter is`"2023-06-15T10:30:00.000Z"`, this 
expression will evaluate to `"2023-06-22T10:30:00.000Z"`, which is the date one week after the start date.

### Accessing automation results from a previous action

Automations allow application to run server-side logic and operations, such as querying databases, interacting with APIs, or
performing data transformations. The `results` namespace provides access to the outputs and data returned by previous actions within the same automation. Note the following points about accessing automation results:

1. You can only access results of previous automation steps within the same automation.
2. If you have actions named `action1` and `action2` in that order,
   `action1` cannot reference any results, and `action2` can only access
   `results.`action1``.
3. This also works in client-side actions. For example, if you have a button that triggers an automation using the
   `InvokeAutomation` action. You can then have a navigation step with a `Run If` condition like
   `results.`myInvokeAutomation1`.fileType === "pdf"` to navigate to a page with a
   PDF viewer if the automation indicates the file is a PDF.

The following list contains the syntax for accessing automation results from a previous action using the `results` namespace.

- `{{results.`stepName`.data}}`: Retrieve the data array from an automation step named `stepName`.
- `{{results.`stepName`.output}}`: Retrieve the output of an automation step named `stepName`.

The way you access the results of an automation step depends on the type of action and the data it
returns. Different actions may return different properties or data structures. Here are some common examples:

- For a data action, you can access the returned data array using `results.`stepName`.data`.
- For an API call action, you may access the response body using `results.`stepName`.body`.
- For an Amazon S3 action, you may access the file content using `results.`stepName`.Body.transformToWebStream()`.

See the documentation for the specific action types you're using to understand the shape of the data they return and how to
access it within the `results` namespace. The following list contains some examples

- `{{results.`getDataStep`.data.filter(row => row.status === "pending").length}}`:
  Assuming the `getDataStep`
  is an `Invoke Data Action` automation action that returns an array of data rows, this expression filters the data array to
  include only rows where the status field is equal to `pending`, and returns the length (count) of the filtered array.
  This can be useful for querying or processing data based on specific conditions.
- `{{params.`email`.split("@")[0]}}`: If the
  `params.`email`` parameter contains an email address,
  this expression splits the string at the @ symbol and returns the part before the @ symbol, effectively extracting the
  username portion of the email address.
- `{{new Date(params.`timestamp` * 1000)}}`: This expression takes a Unix timestamp parameter
  (`params.`timestamp``) and converts it to a JavaScript Date object. It assumes that the 
timestamp is in seconds, so it 
multiplies it by 1000 to convert it to milliseconds, which is the format expected by the `Date` constructor. This can
  be useful for working with date and time values in automations.
- `{{results.`stepName`.Body}}`: For an `Amazon S3 GetObject` automation action
  named `stepName`, this
  expression retrieves the file content, which can be consumed by UI components like **Image** or **PDF Viewer** for
  displaying the retrieved file. Note that this expression would need to be configured in the **Automation output** of
  the automation to use in components.

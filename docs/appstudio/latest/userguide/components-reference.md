# Components reference

This topic details each of App Studio's components, their properties, and includes configuration examples.

## Common component properties

This section outlines the general properties and features that are shared across multiple
components in the application studio. The specific implementation details and use cases for each
property type may vary depending on the component, but the general concept of these properties
remains consistent across App Studio.

### Name

A default name is generated for each component; however, you can edit to change to a unique
name to each component. You will use this name to reference the component and its data from
other components or expressions within the same page. Limitation: Do not include spaces in the
component name; it can only have have letters, numbers, underscores and dollar signs. Examples:
`userNameInput`, `ordersTable`, `metricCard1`.

### Primary value, Secondary value, and Value

Many components in the application studio provide fields for specifying values or
expressions that determine the content or data displayed within the component. These fields are
often labeled as `Primary value`, `Secondary value`, or simply `Value`, depending on the component
type and purpose.

The `Primary value` field is typically used to define the main value, data point, or content
that should be prominently displayed within the component.

The `Secondary value` field, when available, is used to display an additional or supporting
value or information alongside the primary value.

The `Value` field allows you to specify the value or expression that should be displayed in
the component.

These fields support both static text input and dynamic expressions. By using expressions,
you can reference data from other components, data sources, or variables within your
application, enabling dynamic and data-driven content display.

#### Syntax for expressions

The syntax for entering expressions in these fields follows a consistent pattern:

```
{{`expression`}}
```

Where `expression` is a valid expression that evaluates to the desired value or
data you want to display.

##### Example: Static text

- Primary value: you can enter a static number or value directly, such as
  `"123"` or `"$1,999.99"`.
- Secondary value: you can enter a static text label, such as
  `"Goal"` or `"Projected Revenue"`.
- Value: you can enter a static string, such as `"since last
month"` or `"Total Quantity"`.

##### Examples: Expressions

- `Hello, {{currentUser.firstName}}`: Displays a greeting with the first name
  of the currently logged-in user.
- `{{currentUser.role === 'Admin' ? 'Admin Dashboard' : 'User Dashboard'}}`:
  Conditionally displays a different dashboard title based on the user's role.
- `{{ui.componentName.data?.[0]?.fieldName}}`: Retrieves the value of the
  `fieldName` field from the first item in the data of the component with the ID
  `componentName`.
- `{{ui.componentName.value * 100}}`: Performs a calculation on the value of
  the component with the ID `componentName`.
- `{{ui.componentName.value + ' items'}}`: Concatenates the value of the
  component with the ID `componentName` and the string `'
items'`.
- `{{ui.ordersTable.data?.[0]?.orderNumber}}`: Retrieves the order number
  from the first row of data in the `ordersTable` component.
- `{{ui.salesMetrics.data?.[0]?.totalRevenue * 1.15}}`: Calculates the
  projected revenue by increasing the total revenue from the first row of data in the
  `salesMetrics` component by 15%.
- `{{ui.customerProfile.data?.[0]?.firstName + ' ' +
ui.customerProfile.data?.lastName}}`: Concatenates the first and last name from the
  data in the `customerProfile` component.
- `{{new Date(ui.orderDetails.data?.orderDate).toLocaleDateString()}}`:
  Formats the order date from the `orderDetails` component to a more readable date
  string.
- `{{ui.productList.data?.length}}`: Displays the total number of products in
  the data connected to the `productList` component.
- `{{ui.discountPercentage.value * ui.orderTotal.value}}`: Calculates the
  discount amount based on the discount percentage and the order total.
- `{{ui.cartItemCount.value + ' items in cart'}}`: Displays the number of
  items in the shopping cart, along with the label `items in cart`.

By using these expression fields, you can create dynamic and data-driven content within
your application, allowing you to display information that is tailored to the user's context
or the state of your application. This enables more personalized and interactive user
experiences.

### Label

The **Label** property allows you to specify a caption or title for the component. This label
is typically displayed alongside or above the component, helping users understand its
purpose.

You can use both static text and expressions to define the label.

#### Example: Static text

If you enter the text "First Name" in the Label field, the component will display "First
Name" as its label.

#### Example: Expressions

##### Example: Retail store

The following example personalizes the label for each user, making the interface feel more tailored to the individual:

```
{{currentUser.firstName}} {{currentUser.lastName}}'s Account
```

##### Example: SaaS project management

The following example pulls data from the selected project to
provide context-specific labels, helping users stay oriented within the application:

```
Project {{ui.projectsTable.selectedRow.id}} - {{ui.projectsTable.selectedRow.name}}
```

##### Example: Healthcare clinic

The following example references the
current user's profile and the doctor's information, providing a more personalized experience for patients.

```
Dr. {{ui.doctorProfileTable.data.firstName}}
       {{ui.doctorProfileTable.data.lastName}}
```

### Placeholder

The Placeholder property allows you to specify hint or guidance text that is displayed
within the component when it is empty. This can help users understand the expected input format
or provide additional context.

You can use both static text and expressions to define the placeholder.

#### Example: Static text

If you enter the text `Enter your name` in the **Placeholder** field, the component will
display `Enter your name` as the placeholder text.

#### Example: Expressions

##### Example: Financial services

`Enter the amount you'd like to deposit into your `{{ui.accountsTable.selectedRow.balance}}` account` These examples pull data from the selected account to display
relevant prompts, making the interface intuitive for banking customers.

##### Example: E-commerce

`Enter the coupon code for `{{ui.cartTable.data.currency}}` total`
The placeholder here dynamically updates based on the user's cart contents, providing a
seamless checkout experience.

##### Example: Healthcare clinic

`Enter your `{{ui.patientProfile.data.age}}`-year-old patient's symptoms` By using an
expression that references the patient's age, the application can create a more personalized
and helpful placeholder.

### Source

The **Source** property allows you to select the data source for a component. Upon selection,
you can choose from the following data source types: `entity`, `expression`, or `automation`.

#### Entity

Selecting **Entity** as the data source allows you to connect the component to an existing
data entity or model in your application. This is useful when you have a well-defined data
structure or schema that you want to leverage throughout your application.

When to use the entity data source:

- When you have a data model or entity that contains the information you want to display
  in the component (e.g., a "Products" entity with fields like "Name", "Description",
  "Price").
- When you need to dynamically fetch data from a database, API, or other external data
  source and present it in the component.
- When you want to take advantage of the relationships and associations defined in your
  application's data model.

##### Selecting a query on an entity

Sometimes, you may want to connect a component to a specific query that retrieves data
from an entity, rather than the entire entity. In the Entity data source, you have the option
to choose from existing queries or create a new one.

By selecting a query, you can:

- Filter the data displayed in the component based on specific criteria.
- Pass parameters to the query to dynamically filter or sort the data.
- Leverage complex joins, aggregations, or other data manipulation techniques defined in
  the query.

For example, if you have a `Customers` entity in your application with fields like
`Name`, `Email`, and `PhoneNumber`. You can connect a table component to this entity and
choose a pre-defined `ActiveCustomers` data action that filters the customers based on their status.
This allows you to display only the active customers in the table, rather than the entire
customer database.

##### Adding parameters to an entity data source

When using an entity as the data source, you can also add parameters to the component.
These parameters can be used to filter, sort, or transform the data displayed in the
component.

For example, if you have a `Products` entity with fields like `Name`, `Description`, `Price`, and
`Category`. You can add a parameter named `category` to a table component that displays the
product list. When users select a category from a dropdown, the table will automatically
update to show only the products belonging to the selected category, using the
`{{params.category}}` expression in the data action.

#### Expression

Select **Expression** as the data source to enter custom expressions or
calculations to generate the data for the component dynamically. This is useful when you need
to perform transformations, combine data from multiple sources, or generate data based on
specific business logic.

When to use the **Expression** data source:

- When you need to calculate or derive data that is not directly available in your data
  model (e.g., calculating the total order value based on quantity and price).
- When you want to combine data from multiple entities or data sources to create a
  composite view (e.g., displaying a customer's order history along with their contact
  information).
- When you need to generate data based on specific rules or conditions (e.g., displaying a
  "Recommended Products" list based on the user's browsing history).

For example, if you have a `Metrics` component that needs to display the total revenue for the
current month, you can use an expression like the following to calculate and display the monthly revenue:

```
{{ui.table1.orders.concat(ui.table1.orderDetails).filter(o => o.orderDate.getMonth() === new Date().getMonth()).reduce((a, b) => a + (b.quantity * b.unitPrice), 0)}}
```

##### Automation

Select **Automation** as the data source to connect the component to an
existing automation or workflow in your application. This is useful when the data or
functionality for the component is generated or updated as part of a specific process or
workflow.

When to use the **Automation** data source:

- When the data displayed in the component is the result of a specific automation or
  workflow (e.g., a "Pending Approvals" table that is updated as part of an approval
  process).
- When you want to trigger actions or updates to the component based on events or
  conditions within an automation (e.g., updating a Metrics with the latest sales figures
  for a SKU).
- When you need to integrate the component with other services or systems in your
  application through an automation (e.g., fetching data from a third-party API and displaying
  it in a table).

For example, if you have a stepflow component that guides users through a job application process. The
stepflow component can be connected to an automation that handles the job application submission,
background checks, and offer generation. As the automation progresses through these steps, the
stepflow component can dynamically update to reflect the current status of the
application.

By carefully selecting the appropriate data source for each component, you can ensure
that your application's user interface is powered by the right data and logic, providing a
seamless and engaging experience for your users.

### Visible if

Use the **Visible if** property to show or hide components or elements based on specific
conditions or data values. This is useful when you want to dynamically control the visibility of
certain parts of your application's user interface.

The **Visible if** property uses the following syntax:

```
{{`expression` ? true : false}}
```

or

```
{{`expression`}}
```

Where `expression` is a boolean expression that evaluates to either
`true` or `false`.

If the expression evaluates to `true`, the component will be visible. If the
expression evaluates to `false`, the component will be hidden. The expression can
reference values from other components, data sources, or variables within your
application.

#### Visible if expression examples

##### Example: Showing or hiding a password input field based on an email input

Imagine you have a login form with an email input field and a password input field. You
want to show the password input field only if the user has entered an email address. You can
use the following Visible if expression:

```
{{ui.emailInput.value !== ""}}
```

This expression checks if the value of the `emailInput` component is not an
empty string. If the user has entered an email address, the expression evaluates to
`true`, and the password input field will be visible. If the email field is empty,
the expression evaluates to `false`, and the password input field will be
hidden.

##### Example: Displaying additional form fields based on a dropdown selection

Let's say you have a form where users can select a category from a dropdown list.
Depending on the category selected, you want to show or hide additional form fields to gather
more specific information.

For example, if the user selects the `Products` category, you can use the following
expression to show an additional `Product Details` field:

```
{{ui.categoryDropdown.value === "`Products`"}}
```

If the user selects the `Services` or `Consulting` categories, you can use this expression
to show a different set of additional fields:

```
{{ui.categoryDropdown.value === "`Services`" || ui.categoryDropdown.value === "`Consulting`"}}
```

##### Examples: Other

To make the component visible if the `textInput1` component's value is not an
empty string:

```
{{ui.textInput1.value === "" ? false : true}}
```

To make the component always visible:

```
{{true}}
```

To make the component visible if the `emailInput` component's value is not an
empty string:

```
{{ui.emailInput.value !== ""}}
```

### Disabled if

The **Disabled if** feature allows you to conditionally enable or disable a component based on
specific conditions or data values. This is achieved by using the **Disabled if** property, which
accepts a boolean expression that determines whether the component should be enabled or
disabled.

The **Disabled if** property uses the following syntax:

```
{{expression ? true : false}}
```

or

```
{{expression}}
```

#### Disabled if expression examples

##### Example: Disabling a submit button based on form validation

If you have a form with multiple input fields, and you want to disable the submit
button until all required fields are filled out correctly, you can use the following **Disabled
If** expression:

```
{{ui.nameInput.value === "" || ui.emailInput.value === "" || ui.passwordInput.value === ""}}
```

This expression checks if any of the required input fields (`nameInput`, `emailInput`,
`passwordInput`) are empty. If any of the fields are empty, the expression evaluates to `true`, and
the submit button will be disabled. Once all the required fields are filled out, the expression
evaluates to `false`, and the submit button will be enabled.

By using these types of conditional expressions in the **Visible if** and **Disabled ff**
properties, you can create dynamic and responsive user interfaces that adapt to user input,
providing a more streamlined and relevant experience for your application's users.

Where `expression` is a boolean expression that evaluates to
either true or false.

Example:

```
{{ui.textInput1.value === "" ? true : false}}: The component will be Disabled if the textInput1 component's value is an empty string.
{{!ui.nameInput.isValid || !ui.emailInput.isValid || !ui.passwordInput.isValid}}: The component will be Disabled if any of the named input fields are invalid.
```

#### Container layouts

The layout properties determine how the content or elements within a component are
arranged and positioned. Several layout options are available, each represented by an
icon:

- **Column Layout**: This layout arranges the content or elements
  vertically, in a single column.
- **Two column layout**: This layout divides the component into two
  equal-width columns, allowing you to position content or elements side by side.
- **Row layout**: This layout arranges the content or elements
  horizontally, in a single row.

##### Orientation

- **Horizontal**: This layout arranges the content or elements
  horizontally, in a single row.
- **Vertical**: This layout arranges the content or elements vertically,
  in a single column.
- **Inline wrapped**: This layout arranges the content or elements
  horizontally, but wraps to the next line if the elements exceed the available width.

##### Alignment

- **Left**: Aligns the content or elements to the left side of the
  component.
- **Center**: Centers the content or elements horizontally within the
  component.
- **Right**: Aligns the content or elements to the right side of the
  component.

##### Width

The **Width** property specifies the horizontal size of the component. You can
enter a percentage value between 0% and 100%, representing the component's width relative to
its parent container or the available space.

##### Height

The **Height** property specifies the vertical size of the component. The "auto"
value adjusts the component's height automatically based on its content or the available
space.

##### Space between

The **Space between** property determines the spacing or gap between the content or elements
within the component. You can select a value from 0px (no spacing) to 64px, with increments of
4px (e.g., 4px, 8px, 12px, etc.).

##### Padding

The **Padding** property controls the space between the content or elements and the edges of
the component. You can select a value from 0px (no padding) to 64px, with increments of 4px
(e.g., 4px, 8px, 12px, etc.).

##### Background

The **Background** enables or disables a background color or style for the
component.

These layout properties provide flexibility in arranging and positioning the content
within a component, as well as controlling the size, spacing, and visual appearance of the
component itself.

## Data components

This section covers the various data components available in the application studio,
including the **Table**, **Detail**, **Metric**, **Form**, and **Repeater** components.
These components are used to display, gather, and manipulate data within your application.

### Table

The **Table** component displays data in a tabular format, with rows and columns. It is used
to present structured data, such as lists of items or records from a database, in an organized
and easy-to-read manner.

#### Table properties

The **Table** component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

In addition to the common properties, the **Table** component has specific properties and
configuration options, including `Columns`, `Search and export`, and `Expressions`.

##### Columns

In this section, you can define the columns to be displayed in the table. Each column
can be configured with the following properties:

- **Format**: The data type of the field, for example: text, number, date.
- **Column label**: The header text for the column.
- **Value**: The field from the data source that should be displayed in
  this column.

This field allows you to specify the value or expression that should be displayed in
the column cells. You can use expressions to reference data from the connected source or
other components.

Example: `{{currentRow.`title`}}` - This expression will display the value of
the `title` field from the current row in the column cells.

- **Enable sorting**: This toggle allows you to enable or disable
  sorting functionality for the specific column. When enabled, users can sort the table data
  based on the values in this column.

##### Search and export

The **Table** component provides the following toggles to enable or disable search and
export functionality:

- **Show search** When enabled, this toggle adds a search input field
  to the table, allowing users to search and filter the displayed data.
- **Show export** When enabled, this toggle adds an export option to
  the table, allowing users to download the table data in various formats, for example: CSV.

###### Note

By default, the search functionality is limited to the data that has been loaded into
the table. To use search exhaustively, you will need to load all pages of data.

##### Rows per page

You can specify the number of rows to be displayed per page in the table. Users can
then navigate between pages to view the full dataset.

##### Pre-fetch limit

Specify the maximum number of records to pre-fetch in each query request. The maximum is 3000.

##### Actions

In the **Actions** section, configure the following properties:

- **Action location**: When **Pin to right** is enabled, any added actions will
  always show on the right of the table, regardless of user scrolling.
- **Actions**: Add action buttons to the table. You can configure these buttons to do specified
  actions when clicked by a user, such as:
  - Run a component action
  - Navigate to a different page
  - Invoke a data action
  - Run custom JavaScript
  - Invoke an automation

##### Expressions

The **Table** component provides several areas to use expressions and row-level action
capabilities that allow you to customize and enhance the table's functionality and
interactivity. They allow you to dynamically reference and display data within the table. By
leveraging these expression fields, you can create dynamic columns, pass data to row-level
actions, and reference table data from other components or expressions within your
application.

##### Examples: Referencing row values

`{{currentRow.`columnName`}}` or `{{currentRow["`Column Name`"]}}`
These expressions allow you to reference the value of a specific column for the current row
being rendered. Replace `columnName` or `Column Name` with the actual name of the column you
want to reference.

Examples:

- `{{currentRow.productName}}` Displays the product name for the current
  row.
- `{{currentRow["`Supplier Name`"]}}` Displays the supplier name for the
  current row, where the column header is `Supplier Name`.
- `{{currentRow.orderDate}}` Displays the order date for the current
  row.

##### Examples: Referencing selected row

`{{ui.`table1`.selectedRow["columnName"]}}` This expression allows you to
reference the value of a specific column for the currently selected row in the table with
the ID `table1`. Replace `table1` with the actual ID of your table component, and
`columnName` with the name of the column you want to reference.

Examples:

- `{{ui.`ordersTable`.selectedRow["totalAmount"]}}` Displays the total amount
  for the currently selected row in the table with the ID `ordersTable`.
- `{{ui.`customersTable`.selectedRow["email"]}}` Displays the email address
  for the currently selected row in the table with the ID `customersTable`.
- `{{ui.`employeesTable`.selectedRow["department"]}}` Displays the department
  for the currently selected row in the table with the ID `employeesTable`.

##### Examples: Creating custom columns

You can add custom columns to a table based on data returned from the underlying data action,
automation, or expression. You can use existing column values and JavaScript expressions to
create new columns.

Examples:

- `{{currentRow.quantity * currentRow.unitPrice}}` Creates a new column
  displaying the total price by multiplying the quantity and unit price columns.
- `{{new Date(currentRow.orderDate).toLocaleDateString()}}` Creates a new
  column displaying the order date in a more readable format.
- `{{currentRow.firstName + ' ' + currentRow.lastName + ' (' + currentRow.email +
')' }}` Creates a new column displaying the full name and email address for each
  row.

##### Examples: Customizing column display values:

You can customize the display value of a field within a table column by setting the
`Value` field of the column mapping. This allows you to apply custom formatting or
transformations to the displayed data.

Examples:

- `{{ currentRow.rating >= 4 ? '⭐️'.repeat(currentRow.rating) : currentRow.rating
}}` Displays star emojis based on the rating value for each row.
- `{{ currentRow.category.toLowerCase().replace(/\b\w/g, c => c.toUpperCase())
}}` Displays the category value with each word capitalized for each row.
- `{{ currentRow.status === 'Active' ? '🟢 Active' : '🔴 Inactive' }}`:
  Displays a colored circle emoji and text based on the status value for each row.

##### Row-level button actions

`{{currentRow.columnName}}` or `{{currentRow["Column Name"]}}`
You can use these expressions to pass the referenced row's context within a row-level
action, such as navigating to another page with the selected row's data or triggering an
automation with the row's data.

Examples:

- If you have an edit button in the row action column, you can pass
  `{{currentRow.orderId}}` as a parameter to navigate to an order editing page
  with the selected order's ID.
- If you have a delete button in the row action column, you can pass
  `{{currentRow.customerName}}` to an automation that sends a confirmation email
  to the customer before deleting their order.
- If you have a view details button in the row action column, you can pass
  `{{currentRow.employeeId}}` to an automation that logs the employee who viewed
  the order details.

By leveraging these expression fields and row-level action capabilities, you can create
highly customized and interactive tables that display and manipulate data based on your
specific requirements. Additionally, you can connect row-level actions with other components
or automations within your application, enabling seamless data flow and
functionality.

### Detail

The **Detail** component is designed to display detailed information about a specific record
or item. It provides a dedicated space for presenting comprehensive data related to a single
entity or row, making it ideal for showcasing in-depth details or facilitating data entry and
editing tasks.

#### Detail properties

The **Detail** component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

The **Detail** component also has specific properties and configuration options, including
`Fields`, `Layout`, and `Expressions`.

#### Layout

The **Layout** section allows you to customize the arrangement and presentation of the fields
within the **Detail** component. You can configure options such as:

- **Number of columns**: Specify the number of columns to display the
  fields in.
- **Field ordering**: Drag and drop fields to reorder their
  appearance.
- **Spacing and alignment**: Adjust the spacing and alignment of fields
  within the component.

#### Expressions and examples

The **Detail** component provides various expression fields that allow you to reference and
display data within the component dynamically. These expressions enable you to create
customized and interactive **Detail** components that seamlessly connect with your application's
data and logic.

##### Example: Referencing data

`{{ui.details.data[0]?.["colName"]}}`: This expression allows you to
reference the value of the column named "colName" for the first item (index 0) in the data
array connected to the **Detail** component with the ID "details". Replace "colName" with the
actual name of the column you want to reference. For example, the following expression will display the value of the "customerName" column for the first item in the data array
connected to the "details" component:

```
{{ui.details.data[0]?.["customerName"]}}
```

###### Note

This expression is useful when the **Detail** component is on the same page as the table
being referenced, and you want to display data from the first row of the table in the **Detail**
component.

##### Example: Conditional rendering

`{{ui.`table1`.selectedRow["`colName`"]}}`: This expression returns true if the
selected row in the table with the ID `table1` has data for the column named `colName`. It
can be used to conditionally show or hide the **Detail** component based on whether the table's
selected row is empty or not.

Example:

You can use this expression in the `Visible if` property of the **Detail** component to
conditionally show or hide it based on the selected row in the table.

```
{{ui.table1.selectedRow["customerName"]}}
```

If this expression evaluates to true (the selected row in the `table1` component
has a value for the `customerName` column), the **Detail** component will be visible. If the
expression evaluates to false (i.e., the selected row is empty or does not have a value for
"customerName"), the **Detail** component will be hidden.

##### Example: Conditional display

`{{(ui.Component.value === "green" ? "🟢" : ui.Component.value === "yellow" ? "🟡"
 : ui.detail1.data?.[0]?.CustomerStatus)}}`: This expression conditionally displays an
emoji based on the value of a component or data field.

Breakdown:

- `ui.`Component`.value`: References the value of a component with the ID
  `Component`.
- `=== "green"`: Checks if the component's value is equal to the string
  "green".
- `? "🟢"`: If the condition is true, displays the green circle emoji.
- `: ui.Component.value === "yellow" ? "🟡"`: If the first condition is
  false, checks if the component's value is equal to the string "yellow".
- `? "🟡"`: If the second condition is true, displays the yellow square
  emoji.
- `: ui.detail1.data?.[0]?.CustomerStatus`: If both conditions are false, it
  references the "CustomerStatus" value of the first item in the data array connected to the
  Detail component with the ID "detail1".

This expression can be used to display an emoji or a specific value based on the value
of a component or data field within the **Detail** component.

### Metrics

The **Metrics** component is a visual element that displays key metrics or data points in
a card-like format. It is designed to provide a concise and visually appealing way to present
important information or performance indicators.

#### Metrics properties

The **Metrics** component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

#### Trend

The Metrics's trend feature allows you to display a visual indicator of the
performance or change over time for the metric being displayed.

##### Trend value

This field allows you to specify the value or expression that should be used to
determine the trend direction and magnitude. Typically, this would be a value that represents
the change or performance over a specific time period.

Example:

```
{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue}}
```

This expression retrieves the month-over-month revenue value from the first item in the
data connected to the "salesMetrics" Metrics.

##### Positive trend

This field allows you to enter an expression that defines the condition for a positive
trend. The expression should evaluate to true or false.

Example:

```
{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue > 0}}
```

This expression checks if the month-over-month revenue value is greater than 0,
indicating a positive trend.

##### Negative trend

This field allows you to enter an expression that defines the condition for a negative
trend. The expression should evaluate to true or false.

Example:

```
{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue < 0}}
```

This expression checks if the month-over-month revenue value is less than 0, indicating
a negative trend.

##### Color bar

This toggle allows you to enable or disable the display of a colored bar to visually
indicate the trend status.

##### Color Bar examples:

##### Example: Sales metrics trend

- **Trend value**:
  `{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue}}`
- **Positive trend**:
  `{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue > 0}}`
- **Negative trend**:
  `{{ui.salesMetrics.data?.[0]?.monthOverMonthRevenue < 0}}`
- **Color bar**: Enabled

##### Example: inventory metrics trend

- **Trend value**:
  `{{ui.inventoryMetrics.data?.[0]?.currentInventory -
ui.inventoryMetrics.data?.[1]?.currentInventory}}`
- **Positive trend**:
  `{{ui.inventoryMetrics.data?.[0]?.currentInventory >
ui.inventoryMetrics.data?.[1]?.currentInventory}}`
- **Negative trend**:
  `{{ui.inventoryMetrics.data?.[0]?.currentInventory <
ui.inventoryMetrics.data?.[1]?.currentInventory}}`
- **Color Bbar**: Enabled

##### Example: Customer satisfaction trend

- **Trend value**:
  `{{ui.customerSatisfactionMetrics.data?.[0]?.npsScore}}`
- **Positive trend**:
  `{{ui.customerSatisfactionMetrics.data?.[0]?.npsScore >= 8}}`
- **Negative trend**:
  `{{ui.customerSatisfactionMetrics.data?.[0]?.npsScore < 7}}`
- **Color bar**: Enabled

By configuring these trend-related properties, you can create **Metrics** components that provide a
visual representation of the performance or change over time for the metric being
displayed.

By leveraging these expressions, you can create highly customized and interactive metrics
components that reference and display data dynamically, allowing you to showcase key metrics,
performance indicators, and data-driven visualizations within your application.

#### Metrics expression examples

In the properties panel, you can enter expressions to display the title, primary value,
secondary value, and value caption to dynamically display a value.

##### Example: Referencing primary value

`{{ui.`metric1`.primaryValue}}`: This expression allows you to reference the
primary value of the **Metrics** component with the ID `metric1` from other components or
expressions within the same page.

Example: `{{ui.`salesMetrics`.primaryValue}}` will display the primary value of
the `salesMetrics` **Metrics** component.

##### Example: Referencing secondary value

`{{ui.`metric1`.secondaryValue}}`: This expression allows you to reference the
secondary value of the **Metrics** component with the ID `metric1` from other components or
expressions within the same page.

Example: `{{ui.`revenueMetrics`.secondaryValue}}` will display the secondary
value of the `revenueMetrics` **Metrics** component.

##### Example: Referencing data

`{{ui.`metric1`.data}}`: This expression allows you to reference the data of
the **Metrics** component with the ID `metric1` from other components or expressions within the
same page.

Example: `{{ui.`kpiMetrics`.data}}` will reference the data connected to the
`kpiMetrics` **Metrics** component.

##### Example: Displaying specific data values:

`{{ui.`metric1`.data?.[0]?.`id`}}`: This expression is an example of how to
display a specific piece of information from the data connected to the **Metrics** component with
the ID `metric1`. It is useful when you want to display a specific property of the first item
in the data.

Breakdown:

- `ui.`metric1``: References the **Metrics** component with the ID
`metric1`.
- `data`: Refers to the information or data set connected to that
  component.
- `?.[0]`: Means the first item or entry in that data set.
- `?.id`: Displays the `id` value or identifier of that first item or
  entry.

Example: `{{ui.`orderMetrics`.data?.[0]?.`orderId`}}` will display the `orderId`
value of the first item in the data connected to the `orderMetrics` **Metrics** component.

##### Example: Displaying data length

`{{ui.`metric1`.data?.length}}`: This expression demonstrates how to display
the length (number of items) in the data connected to the **Metrics** component with the ID
`metric1`. It is useful when you want to display the number of items in the data.

Breakdown:

- `ui.`metric1`.data`: References the data set connected to the
  component.
- `?.length`: Accesses the total count or number of items or entries in that
  data set.

Example: `{{ui.`productMetrics`.data?.length}}` will display the number of
items in the data connected to the `productMetrics` **Metrics** component.

### Repeater

The **Repeater** component is a dynamic component that allows you to generate and display a
collection of elements based on a provided data source. It is designed to facilitate the
creation of lists, grids, or repeating patterns within your application's user interface. A few
example use cases include:

- Displaying a card for each user in an account
- Showing a list of products that include images and a button to add it to the cart
- Showing a list of files the user can access

The **Repeater** component differentiates itself from the **Table** component with rich content. A
**Table** component has a strict row and column format. The **Repeater** can display your data more flexibly.

#### Repeater properties

The **Repeater** component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

In addition to the common properties, the **Repeater** component has the following additional properties and
configuration options.

#### Item template

The **Item template** is a container where you can define the structure and components that
will be repeated for each item in the data source. You can drag and drop other components into
this container, such as **Text**, **Image**, **Button**, or any other component you need to represent each
item.

Within the **Item template**, you can reference properties or values from the current item
using expressions in the format `{{currentItem.propertyName}}`.

For example, if your data source contains an `itemName` property, you can use
`{{currentItem.itemName}}` to display the item name(s) of the current item.

#### Layout

The **Layout** section allows you to configure the arrangement of the repeated elements
within the Repeater Component.

##### Orientation

- **List**: Arranges the repeated elements vertically in a single
  column.
- **Grid**: Arranges the repeated elements in a grid layout with
  multiple columns.

##### Rows per page

Specify the number of rows to display per page in the list layout. Pagination is
provided for items that overflow the specified number of rows.

##### Columns and Rows per Page (Grid)

- **Columns**: Specify the number of columns in the grid layout.
- **Rows per Page**: Specify the number of rows to display per page in
  the grid layout. Pagination is provided for items that overflow the specified grid
  dimensions.

#### Expressions and examples

The **Repeater** component provides various expression fields that allow you to reference and
display data within the component dynamically. These expressions enable you to create
customized and interactive **Repeater** components that seamlessly connect with your application's
data and logic.

##### Example: Referencing items

- `{{currentItem.propertyName}}`: Reference properties or values from the
  current item within the **Item Template**.
- `{{ui.repeaterID[index]}}`: Reference a specific item in the Repeater
  Component by its index.

##### Example: Rendering a list of products

- **Source**: Select the `Products` entity as the data source.
- **Item Template**: Add a **Container** component with a **Text** component
  inside to display the product name (`{{currentItem.productName}}`) and an **Image**
  component to display the product image
  (`{{currentItem.productImageUrl}}`).
- **Layout**: Set the `Orientation` to `List` and adjust the `Rows per Page`
  as desired.

##### Example: Generating a grid of user avatars

- **Source**: Use an expression to generate an array of user data
  (e.g., `[{name: 'John', avatarUrl: '...'}, {...}, {...}]`).
- **Item Template**: Add an **Image** component and set its `Source` property
  to `{{currentItem.avatarUrl}}`.
- **Layout**: Set the `Orientation` to `Grid`, specify the number of
  `Columns` and `Rows per Page`, and adjust the `Space Between` and `Padding` as needed.

By using the `Repeater` component, you can create dynamic and data-driven user
interfaces, streamlining the process of rendering collections of elements and reducing the need
for manual repetition or hard-coding.

### Form

The Form component is designed to capture user input and facilitate data entry tasks within
your application. It provides a structured layout for displaying input fields, dropdowns,
checkboxes, and other form controls, allowing users to input or modify data seamlessly. You can
nest other components inside of a form component, such as a table.

#### Form properties

The **Form** component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

#### Generate Form

The **Generate Form** feature makes it easy to quickly create form fields by automatically
populating them based on a selected data source. This can save time and effort when building
forms that need to display a large number of fields.

###### To use the **Generate Form** feature:

1. In the **Form** component's properties, locate the **Generate Form** section.
2. Select the data source you want to use to generate the form fields. This can be an
   entity, workflow, or any other data source available in your application.
3. The form fields will be automatically generated based on the selected data source,
   including the field labels, types, and data mappings.
4. Review the generated fields and make any necessary customizations, such as adding
   validation rules or changing the field order.
5. Once you're satisfied with the form configuration, choose **Submit** to apply the generated
   fields to your **Form** component.

The **Generate Form** feature is particularly useful when you have a well-defined data model
or set of entities in your application that you need to capture user input for. By
automatically generating the form fields, you can save time and ensure consistency across your
application's forms.

After using the **Generate Form** feature, you can further customize the layout, actions,
and expressions for the **Form** component to fit your specific requirements.

#### Expressions and examples

Like other components, you can use expressions to reference and display data within the
**Form** component. For example:

- `{{ui.userForm.data.email}}`: References the value of the `email` field from
  the data source connected to the **Form** component with the ID `userForm`.

###### Note

See [Common component properties](#common-properties "#common-properties") for more expression examples of the common properties.

By configuring these properties and leveraging expressions, you can create customized and
interactive Form components that seamlessly integrate with your application's data sources and
logic. These components can be used to capture user input, display pre-populated data, and
trigger actions based on the form submissions or user interactions.

### Stepflow

The **Stepflow** component is designed to guide users through multi-step processes or workflows
within your application. It provides a structured and intuitive interface for presenting a
sequence of steps, each with its own set of inputs, validations, and actions.

The Stepflow component shares several common properties with other components, such as
`Name`, `Source`, and `Actions`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

The **Stepflow** component has additional properties and configuration options, such as `Step
 Navigation`, `Validation`, and `Expressions`.

## AI components

### Gen AI

The **Gen AI** component is a grouping container that is used to group components and their
accompanying logic to easily edit them with AI using chat within the application studio. When you use the chat to create
components, they will be grouped into a **Gen AI** container. For information about editing or using this component, see
[Building or editing your app](generative-ai.md#generative-ai-build-app "generative-ai.md#generative-ai-build-app").

## Text & number components

### Text input

The **Text input** component allows users to enter and submit text data within your
application. It provides a simple and intuitive way to capture user input, such as names,
addresses, or any other textual information.

- `{{ui.`inputTextID`.value}}`: Returns the provided value in the input
  field.
- `{{ui.`inputTextID`.isValid}}`: Returns the validity of the provided value in
  the input field.

### Text

The **Text** component is used to display textual information within your application. It can
be used to show static text, dynamic values, or content generated from expressions.

### Text area

The **Text area** component is designed to capture multi-line text input from users. It
provides a larger input field area for users to enter longer text entries, such as
descriptions, notes, or comments.

- `{{ui.`textAreaID`.value}}`: Returns the provided value in the text
  area.
- `{{ui.`textAreaID`.isValid}}`: Returns the validity of the provided value in
  the text area.

### Email

The **Email** component is a specialized input field designed to capture email addresses from
users. It can enforce specific validation rules to ensure the entered value adheres to the
correct email format.

- `{{ui.`emailID`.value}}`: Returns the provided value in the email input
  field.
- `{{ui.`emailID`.isValid}}`: Returns the validity of the provided value in the
  email input field.

### Password

The **Password** component is an input field specifically designed for users to enter
sensitive information, such as passwords or PIN codes. It masks the entered characters to
maintain privacy and security.

- `{{ui.`passwordID`.value}}`: Returns the provided value in the password input
  field.
- `{{ui.`passwordID`.isValid}}`: Returns the validity of the provided value in
  the password input field.

### Search

The **Search** component provides users with a dedicated input field for performing search
queries or entering search terms within the populated data within the application.

- `{{ui.`searchID`.value}}`: Returns the provided value in the search
  field.

### Phone

The **Phone** component is an input field tailored for capturing phone numbers or other
contact information from users. It can include specific validation rules and formatting options
to ensure the entered value adheres to the correct phone number format.

- `{{ui.`phoneID`.value}}`: Returns the provided value in the phone input
  field.
- `{{ui.`phoneID`.isValid}}`: Returns the validity of the provided value in the
  phone input field.

### Number

The **Number** component is an input field designed specifically for users to enter numerical
values. It can enforce validation rules to ensure the entered value is a valid number within a
specified range or format.

- `{{ui.`numberID`.value}}`: Returns the provided value in the number input
  field.
- `{{ui.`numberID`.isValid}}`: Returns the validity of the provided value in the
  number input field.

### Currency

The **Currency** component is a specialized input field for capturing monetary values or
amounts. It can include formatting options to display currency symbols, decimal separators, and
enforce validation rules specific to currency inputs.

- `{{ui.`currencyID`.value}}`: Returns the provided value in the currency input
  field.
- `{{ui.`currencyID`.isValid}}`: Returns the validity of the provided value in
  the currency input field.

### Detail pair

The **Detail pair** component is used to display key-value pairs or pairs of related
information in a structured and readable format. It is commonly used to present details or
metadata associated with a specific item or entity.

## Selection components

### Switch

The **Switch** component is a user interface control that allows users to toggle between two
states or options, such as on/off, true/false, or enabled/disabled. It provides a visual
representation of the current state and allows users to change it with a single click or
tap.

### Switch group

The **Switch group** component is a collection of individual switch controls that allow users
to select one or more options from a predefined set. It provides a visual representation of the
selected and unselected options, making it easier for users to understand and interact with the
available choices.

#### Switch group expression fields

- `{{ui.switchGroupID.value}}`: Returns an array of strings containing the
  value of each switch that is enabled by the app user.

### Checkbox group

The **Checkbox group** component presents users with a group of checkboxes, allowing them to
select multiple options simultaneously. It is useful when you want to provide users with the
ability to choose one or more items from a list of options.

#### Checkbox group expression fields

- `{{ui.checkboxGroupID.value}}`: Returns an array of strings containing the
  value of each checkbox that is selected by the app user.

### Radio group

The **Radio group** component is a set of radio buttons that allow users to select a single
option from multiple mutually exclusive choices. It ensures that only one option can be
selected at a time, providing a clear and unambiguous way for users to make a selection.

#### Radio group expression fields

The following fields can be used in expressions.

- `{{ui.radioGroupID.value}}`: Returns the value of the radio button that is
  selected by the app user.

### Single select

The **Single select** component presents users with a list of options, from which they can
select a single item. It is commonly used in scenarios where users need to make a choice from a
predefined set of options, such as selecting a category, a location, or a preference.

#### Single select expression fields

- `{{ui.singleSelectID.value}}`: Returns the value of the list item that is
  selected by the app user.

### Multi select

The **Multi select** component is similar to the **Single select** component but allows users to
select multiple options simultaneously from a list of choices. It is useful when users need to
make multiple selections from a predefined set of options, such as selecting multiple tags,
interests, or preferences.

#### Multi select expression fields

- `{{ui.multiSelectID.value}}`: Returns an array of strings containing the
  value of each list item that is selected by the app user.

## Buttons & navigation components

The application studio provides a variety of button and navigation components to allow
users to trigger actions and navigate within your application.

### Button components

The available button components are:

- Button
- Outlined button
- Icon button
- Text button

These button components share the following common properties:

#### Content

- **Button label**: The text to be displayed on the button.

#### Type

- **Button**: A standard button.
- **Outlined**: A button with an outlined style.
- **Icon**: A button with an icon.
- **Text**: A text-only button.

#### Size

The size of the button. Possible values are `Small`, `Medium`, and `Large`.

#### Icon

You can select from a variety of icons to be displayed on the button, including:

- Envelope Closed
- Bell
- Person
- Hamburger Menu
- Search
- Info Circled
- Gear
- Chevron Left
- Chevron Right
- Dots Horizontal
- Trash
- Edit
- Check
- Close
- Home
- Plus

#### Triggers

When the button is clicked, you can configure one or more actions to be triggered. The
available action types are:

- **Basic**
  - Run component action: Executes a specific action within a component.
  - Navigate: Navigates to another page or view.
  - Invoke Data Action: Triggers a data-related action, such as creating, updating, or
    deleting a record.

- **Advanced**
  - JavaScript: Runs custom JavaScript code.
  - Invoke Automation: Starts an existing automation or workflow.

#### JavaScript action button properties

Select the `JavaScript` action type to run custom JavaScript code when the
button is clicked.

##### Source code

In the `Source code` field, you can enter your JavaScript expression or function. For
example:

```
return "Hello World";
```

This will simply return the string `Hello World` when the button is clicked.

##### Condition: Run if

You can also provide a boolean expression that determines whether the JavaScript action
should be executed or not. This uses the following syntax:

```
{{ui.textinput1.value !== ""}}
```

In this example, the JavaScript action will only run if the value of the `textinput1`
component is not an empty string.

By using these advanced trigger options, you can create highly customized button
behaviors that integrate directly with your application's logic and data. This allows you to
extend the built-in functionality of the buttons and tailor the user experience to your
specific requirements.

###### Note

Always thoroughly test your JavaScript actions to ensure they are functioning as expected.

### Hyperlink

The **Hyperlink** component provides a clickable link for navigating to external URLs or
internal application routes.

#### Hyperlink properties

##### Content

- **Hyperlink label**: The text to be displayed as the hyperlink
  label.

##### URL

The destination URL for the hyperlink, which can be an external website or an internal
application route.

##### Triggers

When the hyperlink is clicked, you can configure one or more actions to be triggered.
The available action types are the same as those for the button components.

## Date & time components

### Date

The **Date** component allows users to select and input dates.

The **Date** component shares several common properties with other components, such as
`Name`, `Source`, and `Validation`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

In addition to the common properties, the **Date** component has the following specific
properties:

#### Date properties

##### Format

- **YYYY/MM/DD**, **DD/MM/YYYY**,
  **YYYY/MM/DD**, **YYYY/DD/MM**,
  **MM/DD**, **DD/MM**: The format in which the date
  should be displayed.

##### Value

- **YYYY-MM-DD**: The format in which the date value is stored
  internally.

##### Min date

- **YYYY-MM-DD**: The minimum date that can be selected.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### Max date

- **YYYY-MM-DD**: The maximum date that can be selected.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### Calendar type

- **1 Month**, **2 Months**: The type of calendar UI
  to display.

##### Disabled dates

- **Source**: The data source for the dates that should be disabled. For example: None, Expression.
- **Disabled dates**: An expression that determines which dates should
  be disabled, such as:
  - `{{currentRow.column}}`: Disables dates that match what this expression evaluates to.
  - `{{new Date(currentRow.dateColumn) < new Date("2023-01-01")}}`: Disables dates before January 1, 2023
  - `{{new Date(currentRow.dateColumn).getDay() === 0 || new Date(currentRow.dateColumn).getDay() === 6}}`:
    Disables weekends.

##### Behavior

- **Visible if**: An expression that determines the visibility of the
  **Date** component.
- **Disable if**: An expression that determines whether the **Date**
  component should be disabled.

#### Validation

The **Validation** section allows you to define additional rules and constraints for the date
input. By configuring these validation rules, you can ensure that the date values entered by
users meet the specific requirements of your application. You can add the following types of
validations:

- **Required**: This toggle ensures that the user must enter a date
  value before submitting the form.
- **Custom**: You can create custom validation rules using JavaScript
  expressions. For example:

```
{{new Date(ui.dateInput.value) < new Date("2023-01-01")}}
```

This expression checks if the entered date is before January 1, 2023. If the condition
is true, the validation will fail.

You can also provide a custom validation message to be displayed when the validation is
not met:

```
"Validation not met. The date must be on or after January 1, 2023."
```

By configuring these validation rules, you can ensure that the date values entered by
users meet the specific requirements of your application.

#### Expressions and examples

The **Date** component provides the following expression field:

- `{{ui.dateID.value}}`: Returns the date value entered by the user in the
  format `YYYY-MM-DD`.

### Time

The **Time** component allows users to select and input time values. By configuring the
various properties of the **Time** component, you can create time input fields that meet the
specific requirements of your application, such as restricting the selectable time range,
disabling certain times, and controlling the component's visibility and interactivity.

#### Time properties

The **Time** component shares several common properties with other components, such as
`Name`, `Source`, and `Validation`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

In addition to the common properties, the **Time** component has the following specific
properties:

##### Time intervals

- **5 minutes**, **10 minutes**, **15
  minutes**, **20 minutes**, **25 minutes**,
  **30 minutes**, **60 minutes**: The intervals available
  for selecting the time.

##### Value

- **HH:MM AA**: The format in which the time value is stored
  internally.

###### Note

This value must match the format of `HH:MM AA`.

##### Placeholder

- **Calendar settings**: The placeholder text displayed when the time
  field is empty.

##### Min time

- **HH:MM AA**: The minimum time that can be selected.

###### Note

This value must match the format of `HH:MM AA`.

##### Max time

- **HH:MM AA**: The maximum time that can be selected.

###### Note

This value must match the format of `HH:MM AA`.

##### Disabled times

- **Source**: The data source for the times that should be disabled
  (e.g., None, Expression).
- **Disabled times**: An expression that determines which times should
  be disabled, such as `{{currentRow.column}}`.

##### Disabled times configuration

You can use the **Disabled Times** section to specify which time values should be
unavailable for selection.

##### Source

- **None**: No times are disabled.
- **Expression**: You can use a JavaScript expression to determine
  which times should be disabled, such as `{{currentRow.column}}`.

##### Example expression:

```
{{currentRow.column === "Lunch Break"}}
```

This expression would disable any times where the "Lunch Break" column is true for the
current row.

By configuring these validation rules and disabled time expressions, you can ensure that
the time values entered by users meet the specific requirements of your application.

##### Behavior

- **Visible if**: An expression that determines the visibility of the
  Time component.
- **Disable if**: An expression that determines whether the Time
  component should be disabled.

##### Validation

- **Required**: A toggle that ensures the user must enter a time value
  before submitting the form.
- **Custom**: Allows you to create custom validation rules using
  JavaScript expressions.

**Custom Validation Message**: The message to be displayed when the
custom validation is not met.

For example:

```
{{ui.timeInput.value === "09:00 AM" || ui.timeInput.value === "09:30 AM"}}
```

This expression checks if the entered time is 9:00 AM or 9:30 AM. If the
condition is true, the validation will fail.

You can also provide a custom validation message to be displayed when the validation
is not met:

```
Validation not met. The time must be 9:00 AM or 9:30 AM.
```

#### Expressions and examples

The Time component provides the following expression field:

- `{{ui.timeID.value}}`: Returns the time value entered by the user in the
  format HH:MM AA.

##### Example: Time value

- `{{ui.timeID.value}}`: Returns the time value entered by the user in the
  format `HH:MM AA`.

##### Example: Time comparison

- `{{ui.timeInput.value > "10:00 AM"}}`: Checks if the time value is greater
  than 10:00 AM.
- `{{ui.timeInput.value < "05:00 pM"}}`: Checks if the time value is less
  than 05:00 PM.

### Date range

The **Date range** component allows users to select and input a range of dates. By configuring
the various properties of the Date Range component, you can create date range input fields that
meet the specific requirements of your application, such as restricting the selectable date
range, disabling certain dates, and controlling the component's visibility and
interactivity.

#### Date range properties

The **Date Range** component shares several common properties with other components, such as
`Name`, `Source`, and `Validation`. For more information on these properties, see
[Common component properties](#common-properties "#common-properties").

In addition to the common properties, the **Date Range** component has the following specific
properties:

##### Format

- **MM/DD/YYYY**: The format in which the date range should be
  displayed.

##### Start date

- **YYYY-MM-DD**: The minimum date that can be selected as the start of
  the range.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### End date

- **YYYY-MM-DD**: The maximum date that can be selected as the end of
  the range.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### Placeholder

- **Calendar settings**: The placeholder text displayed when the date
  range field is empty.

##### Min date

- **YYYY-MM-DD**: The minimum date that can be selected.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### Max date

- **YYYY-MM-DD**: The maximum date that can be selected.

###### Note

This value must match the format of `YYYY-MM-DD`.

##### Calendar type

- **1 Month**: The type of calendar UI to display. For example, single
  month.
- **2 Month**: The type of calendar UI to display. For example, two
  months.

##### Mandatory days selected

- **0**: The number of mandatory days that must be selected within the
  date range.

##### Disabled dates

- **Source**: The data source for the dates that should be disabled
  (e.g., None, Expression, Entity, or Automation).
- **Disabled dates**: An expression that determines which dates should
  be disabled, such as `{{currentRow.column}}`.

##### Validation

The **Validation** section allows you to define additional rules and constraints for the
date range input.

#### Expressions and examples

The **Date Range** component provides the following expression fields:

- `{{ui.dateRangeID.startDate}}`: Returns the start date of the selected range
  in the format `YYYY-MM-DD`.
- `{{ui.dateRangeID.endDate}}`: Returns the end date of the selected range in
  the format `YYYY-MM-DD`.

##### Example: Calculating date difference

- `{(new Date(ui.dateRangeID.endDate) - new Date(ui.dateRangeID.startDate)) / (1000
- 60 _ 60 _ 24)}}` Calculates the number of days between the start and end
  dates.

##### Example: Conditional visibility based on date range

- `{{new Date(ui.dateRangeID.startDate) < new Date("2023-01-01") || new
Date(ui.dateRangeID.endDate) > new Date("2023-12-31")}}` Checks if the selected date
  range is outside of the year 2023.

##### Example: Disabled dates based on current row data

- `{{currentRow.isHoliday}}` Disables dates where the "isHoliday" column in
  the current row is true.
- `{{new Date(currentRow.dateColumn) < new Date("2023-01-01")}}` Disables
  dates before January 1, 2023 based on the "dateColumn" in the current row.
- `{{new Date(currentRow.dateColumn).getDay() === 0 || new
Date(currentRow.dateColumn).getDay() === 6}}` Disables weekends based on the
  "dateColumn" in the current row.

##### Custom validation

- `{{new Date(ui.dateRangeID.startDate) > new Date(ui.dateRangeID.endDate)}}`
  Checks if the start date is later than the end date, which would fail the custom
  validation.

## Media components

The application studio provides several components for embedding and displaying various
media types within your application.

### iFrame embed

The **iFrame embed** component allows you to embed external web content or applications within
your application using an iFrame.

#### iFrame embed properties

##### URL

###### Note

The source of the media displayed in this component must be allowed in your application's content security settings. For more information,
see [Viewing or updating your app's content security settings](app-content-security-settings-csp.md "app-content-security-settings-csp.md").

The URL of the external content or application you want to embed.

##### Layout

- **Width**: The width of the iFrame, specified as a percentage (%) or
  a fixed pixel value (e.g., 300px).
- **Height**: The height of the iFrame, specified as a percentage (%)
  or a fixed pixel value.

### S3 upload

The **S3 upload** component allows users to upload files to an Amazon S3 bucket. By
configuring the **S3 Upload** component, you can enable users to easily upload files to your
application's Amazon S3 storage, and then leverage the uploaded file information within your
application's logic and user interface.

###### Note

Remember to ensure that the necessary permissions and Amazon S3 bucket configurations are in
place to support the file uploads and storage requirements of your application.

#### S3 upload properties

##### S3 Configuration

- **Connector**: Select the pre-configured Amazon S3 connector to use for the
  file uploads.
- **Bucket**: The Amazon S3 bucket where the files will be uploaded.
- **Folder**: The folder within the Amazon S3 bucket where the files will be
  stored.
- **File name**: The naming convention for the uploaded files.

##### File upload configuration

- **Label**: The label or instructions displayed above the file upload
  area.
- **Description**: Additional instructions or information about the
  file upload.
- **File type**: The type of files that are allowed to be uploaded. For example: image, document, or video.
- **Size**: The maximum size of the individual files that can be
  uploaded.
- **Button label**: The text displayed on the file selection
  button.
- **Button style**: The style of the file selection button. For example, outlined or filled.
- **Button size**: The size of the file selection button.

##### Validation

- **Max number of files**: The maximum number of files that can be
  uploaded at once.
- **Max file size**: The maximum size allowed for each individual
  file.

##### Triggers

- **On success**: Actions to be triggered when a file upload is
  successful.
- **On failure**: Actions to be triggered when a file upload
  fails.

#### S3 upload expression fields

The **S3 upload** component provides the following expression fields:

- `{{ui.s3uploadID.files}}`: Returns an array of the files that have been
  uploaded.
- `{{ui.s3uploadID.files[0]?.size}}`: Returns the size of the file at the
  designated index.
- `{{ui.s3uploadID.files[0]?.type}}`: Returns the type of the file at the
  designated index.
- `{{ui.s3uploadID.files[0]?.nameOnly}}`: Returns the name of the file, with
  no extension suffix, at the designated index.
- `{{ui.s3uploadID.files[0]?.nameWithExtension}}`: Returns the name of the
  file with its extension suffix at the designated index.

#### Expressions and examples

##### Example: Accessing uploaded files

- `{{ui.s3uploadID.files.length}}`: Returns the number of files that have
  been uploaded.
- `{{ui.s3uploadID.files.map(f => f.name).join(', ')}}`: Returns a
  comma-separated list of the file names that have been uploaded.
- `{{ui.s3uploadID.files.filter(f => f.type.startsWith('image/'))}}`: Returns
  an array of only the image files that have been uploaded.

##### Example: Validating file uploads

- `{{ui.s3uploadID.files.some(f => f.size > 5 * 1024 * 1024)}}`: Checks if
  any of the uploaded files exceed 5 MB in size.
- `{{ui.s3uploadID.files.every(f => f.type === 'image/png')}}`: Checks if all
  the uploaded files are PNG images.
- `{{ui.s3uploadID.files.length > 3}}`: Checks if more than 3 files have been
  uploaded.

##### Example: Triggering actions

- `{{ui.`s3uploadID`.files.length > 0 ? 'Upload Successful' : 'No files
uploaded'}}`: Displays a success message if at least one file has been
  uploaded.
- `{{ui.`s3uploadID`.files.some(f => f.type.startsWith('video/')) ?
triggerVideoProcessing() : null}}`: Triggers a video processing automation if any
  video files have been uploaded.
- `{{ui.`s3uploadID`.files.map(f => f.url)}}`: Retrieves the URLs of the
  uploaded files, which can be used to display or further process the files.

These expressions allow you to access the uploaded files, validate the file uploads, and
trigger actions based on the file upload results. By utilizing these expressions, you can
create more dynamic and intelligent behavior within your application's file upload
functionality.

###### Note

Replace `s3uploadID` with the ID of your **S3 upload** component.

### PDF viewer component

The **PDF viewer** component allows users to view and interact with PDF documents within your
application. App Studio supports these different input types for the PDF Source, the **PDF viewer**
component provides flexibility in how you can integrate PDF documents into your application,
whether it's from a static URL, an inline data URI, or dynamically generated content.

#### PDF viewer properties

##### Source

###### Note

The source of the media displayed in this component must be allowed in your application's content security settings. For more information,
see [Viewing or updating your app's content security settings](app-content-security-settings-csp.md "app-content-security-settings-csp.md").

The source of the PDF document, which can be an expression, entity, URL, or
automation.

##### Expression

Use an expression to dynamically generate the PDF source.

##### Entity

Connect the **PDF viewer** component to a data entity that contains the PDF document.

##### URL

Specify the URL of the PDF document.

##### URL

You can enter a URL that points to the PDF document you want to display. This could be
a public web URL or a URL within your own application.

Example: `https://example.com/document.pdf`

##### Data URI

A **Data URI** is a compact way to include small data files (like images or PDFs) inline
within your application. The PDF document is encoded as a base64 string and included
directly in the component's configuration.

##### Blob or ArrayBuffer

You can also provide the PDF document as a Blob or ArrayBuffer object, which allows
you to dynamically generate or retrieve the PDF data from various sources within your
application.

##### Automation

Connect the **PDF viewer** component to an automation that provides the PDF document.

##### Actions

- **Download**: Adds a button or link that allows users to download the
  PDF document.

##### Layout

- **Width**: The width of the PDF Viewer, specified as a percentage (%)
  or a fixed pixel value (e.g., 600px).
- **Height**: The height of the PDF Viewer, specified as a fixed pixel
  value.

### Image viewer

The **Image viewer** component allows users to view and interact with image files within your
application.

#### Image viewer properties

##### Source

###### Note

The source of the media displayed in this component must be allowed in your application's content security settings. For more information,
see [Viewing or updating your app's content security settings](app-content-security-settings-csp.md "app-content-security-settings-csp.md").

- **Entity**: Connect the **Image viewer** component to a data entity that contains
  the image file.
- **URL**: Specify the URL of the image file.
- **Expression**: Use an expression to dynamically generate the image
  source.
- **Automation**: Connect the **Image viewer** component to an automation that
  provides the image file.

##### Alt text

The alternative text description of the image, which is used for accessibility
purposes.

##### Layout

- **Image fit**: Determines how the image should be resized and
  displayed within the component. For example: `Contain`, `Cover`, or `Fill`.
- **Width**: The width of the **Image viewer** component, specified as a percentage
  (%) or a fixed pixel value (e.g., 300px).
- **Height**: The height of the **Image viewer** component, specified as a fixed
  pixel value.
- **Background**: Allows you to set a background color or image for the
  **Image viewer** component.

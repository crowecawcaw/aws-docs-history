# Work with cells

## Overview

Notebooks support a variety of languages such as Python, SQL, and Markdown. Each cell is
associated with a language, and the editor in the cell supports functionality such as auto code
complete, formatting, and linting.

All the code in the notebook is executed on the notebook kernel, which is built on IPython.
The notebook kernel runs on SageMaker notebook compute, which has a configurable form factor
that includes different types of instances. When cells are executed, they may produce output
that is shown below each cell. Notebooks support rich rendering of data frames (pandas or
Spark), where the output is rendered in an interactive data table and charts.

## Procedure

To create and run Python code:

1. Choose **Python** to add a new Python cell.
2. Enter your Python code in the cell editor.
3. Choose the play icon or press **Shift+Enter** to run the cell.
4. View the results displayed below the cell.

All notebook code is executed in the notebook kernel, which runs on SageMaker compute. You
can configure the form factor of this compute. The notebook runs an IPython kernel that can
execute Python code. For larger scale data processing, the notebook's Python environment comes
with Spark without requiring you to configure or manage any infrastructure. You can start
writing Spark code to run interactive analytics and exploration on serverless, autoscalable
Athena Spark.

To create and run SQL code:

1. Choose **SQL** to add a new SQL cell.
2. Select your data connection from the dropdown if prompted.
3. Enter your SQL query in the cell editor.
4. Choose the play icon or press **Shift+Enter** to run the cell.
5. View the query results in the interactive table below the cell.

SQL cells can query your existing Python data frames using DuckDB, or run SQL against
Athena (SQL), Athena Spark, or any other connection to first-party and third-party engines
like Amazon Redshift, Snowflake, and BigQuery. Add a connection from the [available connections that are supported](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md").

### Run multiple SQL statements in a single cell

You can write and run multiple SQL statements in a single SQL cell by separating each
statement with a semicolon (`;`). When you run a cell that contains multiple
statements, the notebook executes them sequentially and displays the results in a tabbed
interface.

To run multiple SQL statements:

1. In a SQL cell, enter two or more SQL statements separated by semicolons. For
   example:

```
SELECT COUNT(*) FROM customers WHERE region = 'US';
SELECT COUNT(*) FROM customers WHERE region = 'EU';
SELECT COUNT(*) FROM customers WHERE region = 'ASIA';
```

2. Choose the play icon or press **Shift+Enter** to run the cell.
3. The output area displays a row of tabs labeled **Result 1**,
   **Result 2**, **Result 3**,
   and so on — one tab for each statement.
4. Choose a tab to view the results for that statement.

Each tab displays a status indicator:

- A success indicator (✓) when the statement completed successfully.
- An error indicator (⚠) when the statement encountered an error. Choose the tab to
  view the error details.

### Reference multi-statement SQL results in Python

When you run multiple SQL statements in a single cell, the notebook creates a separate
data frame variable for each statement result. The variables follow this naming
convention:

- `dataframe_name` — A list containing all results.
- ``dataframe_name`\_0` — The result of the first statement.
- ``dataframe_name`\_1` — The result of the second statement.
- ``dataframe_name`\_2` — The result of the third statement, and so on.

For example, if the cell's data frame variable is `df_cell_1`, the following
variables are created:

| Variable      | Description                                   |
| ------------- | --------------------------------------------- |
| `df_cell_1`   | A list containing all statement results       |
| `df_cell_1_0` | Result of the first statement (Result 1 tab)  |
| `df_cell_1_1` | Result of the second statement (Result 2 tab) |
| `df_cell_1_2` | Result of the third statement (Result 3 tab)  |

You can reference these variables in subsequent Python cells:

```
# Access the first statement's result
print(df_cell_1_0.head())

# Access by index from the list
print(df_cell_1[1].head())
```

You can rename the base data frame variable using the variable name editor in the cell's
symbol bar. When you rename the base variable, all indexed variables update automatically.
For example, renaming `df_cell_1` to `sales_data` updates the indexed
variables to `sales_data_0`, `sales_data_1`, and so on.

###### Note

Individual indexed variables (such as `sales_data_0`) cannot be renamed
independently. Only the base data frame name can be changed.

### Visualize multi-statement results

Each result tab supports the full set of visualization options independently. You
can:

- Switch between table and chart views for each result tab separately.
- Apply column filters, sorting, and pinning per result tab.
- Create different chart types for different statement results.

Visualization settings for the first result tab are saved with the notebook. Settings
for additional result tabs are maintained during your current session but reset when you
reopen the notebook.

### Rename cells

You can assign custom names to cells to make them easier to identify and navigate,
especially in large notebooks. By default, cells are labeled with sequential numbers (1, 2,
3, and so on).

To rename a cell:

1. Choose the cell number in the cell header. The number becomes an editable text
   field.
2. Enter a custom name for the cell.
3. Press **Enter** or choose outside the text field to
   save the name.

The custom name replaces the default number in the cell header. This is useful
for:

- Identifying the purpose of specific cells at a glance (for example, "Data cleanup"
  or "Model training").
- Navigating large notebooks more efficiently.
- Making notebooks easier for collaborators to understand.

### Keyboard shortcuts

Amazon SageMaker Unified Studio notebooks provide keyboard shortcuts that enable you to
perform common actions and navigate within your notebooks. These shortcuts are familiar to
developers who have used other Python or SQL notebook editors.

To view all available shortcuts, press **⌘+Shift+/** (Mac)
or **Ctrl+Shift+/** (Windows/Linux).

Notebooks support two modes for keyboard shortcuts: edit mode and command mode. Shortcuts
without modifier keys are generally used in command mode.

#### Edit mode

Edit mode is active when you are editing the content of a cell. In this mode, keyboard
shortcuts require modifier keys to avoid interfering with normal text input.

| Action                        | Mac         | Windows/Linux |
| ----------------------------- | ----------- | ------------- |
| Run the current cell          | ⌘+Enter     | Ctrl+Enter    |
| Run cell and select next cell | Shift+Enter | Shift+Enter   |
| Toggle Gen AI prompting       | Option+A    | Alt+A         |

#### Command mode

To enter command mode, press **Esc**. A blue ring appears
around the selected cell to indicate that command mode is active.

In command mode, the following actions are available in addition to the edit mode
shortcuts:

**Navigation**

| Action            | Shortcut |
| ----------------- | -------- |
| Select above cell | Up       |
| Select below cell | Down     |
| Edit cell content | Enter    |

**Cell creation**

| Action            | Shortcut |
| ----------------- | -------- |
| Add cell above    | A        |
| Add cell below    | B        |
| Add Python cell   | P        |
| Add SQL cell      | Q        |
| Add Markdown cell | M        |
| Add table cell    | T        |
| Add charts cell   | C        |

**Cell operations**

| Action                         | Mac          | Windows/Linux |
| ------------------------------ | ------------ | ------------- |
| Copy cell                      | ⌘+C          | Ctrl+C        |
| Paste cell                     | ⌘+V          | Ctrl+V        |
| Duplicate cell                 | ⌘+D          | Ctrl+D        |
| Run cell and insert cell below | Option+Enter | Alt+Enter     |
| Save notebook                  | ⌘+S          | Ctrl+S        |

###### Tip

When the intercell menu is open, you can use the typed cell shortcuts
(**P**, **Q**,
**M**, **T**,
**C**) to add a cell of a specific type.

To add documentation:

1. Choose **Markdown** to add a Markdown cell.
2. Enter your documentation using Markdown syntax.
3. Choose the play icon or press **Shift+Enter** to render
   the formatted text.

To reference data between cells: Python variables created in one cell are available in
subsequent cells. SQL query results can be referenced by variable name in Python cells. You
can also use the variable explorer in the left navigation to see all available variables and
their schemas.

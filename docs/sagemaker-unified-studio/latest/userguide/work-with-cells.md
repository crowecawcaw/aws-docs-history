# Work with cells

## Overview

Notebooks support a variety of languages such as Python, SQL and Markdown. Each cell is
associated with a language and the editor in the cell supports functionality such as auto code
complete, formatting, linting etc.

All the code in the notebook is executed on the notebook kernel which is built on ipython.
The notebook kernel runs on the sagemaker notebook compute which has a configurable form
factor which includes different types of instances. When cells are executed, they may produce
output which is shown below each cell. Notebooks support rich rendering of data frames (pandas
or spark) where the output is rendered in an interactive data table and charts.

## Procedure

To create and run Python code:

1. Click the Python button to add a new Python cell.
2. Enter your Python code in the cell editor.
3. Click the play icon or press Shft+Enter to run the cell.
4. View the results displayed below the cell.

All notebook code is executed in the notebook kernel which runs on SageMaker compute. The
user can configure the form factor of this compute. The notebook runs an ipython kernel which
can execute Python code. For larger scale data processing, the notebook's python environment
comes with Spark without the user needing to configure or manage any infrastructure. User can
simply start writing Spark code to run interactive analytics and exploration on serverless,
autoscalable Athena Spark.

To create and run SQL code:

1. Click the SQL button to add a new SQL cell.
2. Select your data connection from the dropdown if prompted.
3. Enter your SQL query in the cell editor.
4. Click the play icon or press Shft+Enter to run the cell.
5. View the query results in the interactive table below the cell.

SQL cells can query your existing Python data frames using DuckDB or run SQL against
Athena (SQL), Athena Spark or any other connection to 1st and 3rd party engines like Redshift,
Snowflake, Big Query etc. Add a connection from the [available connections that are supported](../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md "../../../sagemaker-lakehouse-architecture/latest/userguide/lakehouse-data-connection.md").

To add documentation:

1. Click the Markdown button to add a markdown cell.
2. Enter your documentation using markdown syntax.
3. Click the play icon or press Shft+Enter to render the formatted text.

To reference data between cells: - Python variables created in one cell are available in
subsequent cells. SQL query results can be referenced by variable name in Python cells. You
can also use the variable explorer on the left navigation to see all available variables and
their schemas.

# Visualize and explore data

## Overview

Amazon SageMaker Unified Studio notebooks provide rich data visualization and exploration capabilities. Data frames automatically render as interactive tables, and you can create dedicated chart cells for custom visualizations.

On the left navigation, the data explorer provides access to your data catalog for discovering and accessing datasets. The variable explorer shows all active variables in your notebook session, including their data types and schemas.

## Procedure

To view data in interactive tables:

1. Execute a Python or SQL cell that returns a data frame – compatible types include pandas, pyarrow, pyspark. Note: There is a limit of 20,000 rows for loading on the interactive tables and charts.
2. The results automatically display as an interactive table below the cell.
3. Use the table controls to filter, sort, and explore the data.
4. Click column headers to see data distribution visualizations.

To create custom charts:

1. Click the Charts button to add a chart cell.
2. Select the data frame you want to visualize from the dropdown.
3. Choose your chart type and configure the axes.
4. The chart renders automatically based on your selections.

To explore variables:

1. Open the variable explorer panel in the notebook interface.
2. View all active variables, their types, and memory usage.
3. Click on data frame variables to expand and see their schema.
4. Use variable names to reference data in new cells.

To access the data catalog:

1. Open the data explorer panel.
2. Navigate through your available data catalogs and databases.
3. Use the actions menu to read data directly into your notebook.
4. Generate code to access specific tables or datasets.

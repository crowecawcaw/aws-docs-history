# Using pivot tables

Use pivot tables to show measure values for the intersection of two dimensions.

Heat maps and pivot tables display data in a similar tabular fashion. Use a heat map
if you want to identify trends and outliers, because the use of color makes these easier
to spot. Use a pivot table if you want to analyze data on the visual.

To create a pivot table, choose at least one field of any data type, and choose the
pivot table icon. Amazon Quick Suite creates the table and populates the cell values with the
count of the column value for the intersecting row value. Typically, you choose a
measure and two dimensions measurable by that measure.

Pivot tables support scroll down and right. You can add up to 20 fields as rows and 20
fields as columns. Up to 500,000 records are supported.

Using a pivot table, you can do the following:

- Specify multiple measures to populate the cell values of the table, so that
  you can see a range of data
- Cluster pivot table columns and rows to show values for subcategories grouped
  by related dimension
- Sort values in pivot table rows or columns
- Apply statistical functions
- Add totals and subtotals to rows and columns
- Use infinite scroll
- Transpose fields used by rows and columns
- Create custom total aggregations
  To easily transpose the fields used by the rows and columns of the pivot table, choose
  the orientation icon (
  ![](../images/pivot-orientation.png)
  ) near the top right of the visual. To see options for showing and
  hiding totals and subtotals, formatting the visual, or exporting data to a CSV file,
  choose the Menu items icon at top right.

As with all visual types, you can add and remove fields. You can also change the field
associated with a visual element, change field aggregation, and change date field
granularity. In addition, you can focus on or exclude rows or columns. For more
information about how to make these changes to a pivot table, see [Changing fields used by a visual in
Amazon Quick Suite](changing-visual-fields.md "changing-visual-fields.md").

For information on formatting pivot tables, see [Formatting in Amazon Quick Suite](formatting-a-visual.md "formatting-a-visual.md").

For information on custom total aggregations for pivot tables, see [Custom total values](tables-pivot-tables-custom-totals.md "tables-pivot-tables-custom-totals.md").

###### Topics

- [Pivot table features](#pivot-table-features "#pivot-table-features")
- [Creating a pivot table](create-pivot-table.md "create-pivot-table.md")
- [Orienting pivot table values](pivot-table-value-orientation.md "pivot-table-value-orientation.md")
- [Expanding and collapsing pivot
  table clusters](expanding-and-collapsing-clusters.md "expanding-and-collapsing-clusters.md")
- [Showing and hiding pivot table columns
  in Quick Suite](hiding-pivot-table-columns.md "hiding-pivot-table-columns.md")
- [Sorting pivot tables in
  Quick Suite](sorting-pivot-tables.md "sorting-pivot-tables.md")
- [Using table calculations in pivot
  tables](working-with-calculations.md "working-with-calculations.md")
- [Pivot table limitations](pivot-table-limitations.md "pivot-table-limitations.md")
- [Pivot table best practices](pivot-table-best-practices.md "pivot-table-best-practices.md")

## Pivot table features

Pivot tables don't display a legend.

To understand the features supported by pivot tables, use the following
table.

| Feature                                 | Supported?           | Comments                                                                                                                                                                                                                                                                                                                                                                           | For more information                                                                                                                                                                    |
| --------------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| Changing the legend display             | No                   |                                                                                                                                                                                                                                                                                                                                                                                    | [Legends on visual types in Quick Suite](customizing-visual-legend.md "customizing-visual-legend.md")                                                                                   |
| Changing the title display              | Yes                  |                                                                                                                                                                                                                                                                                                                                                                                    | [Titles and subtitles on visual types in Quick Suite](customizing-a-visual-title.md "customizing-a-visual-title.md")                                                                    |
| Changing the axis range                 | Not applicable       |                                                                                                                                                                                                                                                                                                                                                                                    | [Range and scale on visual types in Quick Suite](changing-visual-scale-axis-range.md "changing-visual-scale-axis-range.md")                                                             |
| Changing the visual colors              | No                   |                                                                                                                                                                                                                                                                                                                                                                                    | [Colors in visual types in Quick Suite](changing-visual-colors.md "changing-visual-colors.md")                                                                                          |
| Focusing on or excluding elements       | Yes, with exceptions | You can focus on or exclude any column or row, except when you are using a date field as one of the dimensions. In that case, you can only focus on the column or row that uses the date dimension, not exclude it.                                                                                                                                                                | [Focusing on visual elements](focusing-on-visual-elements.md "focusing-on-visual-elements.md") [Excluding visual elements](excluding-visual-elements.md "excluding-visual-elements.md") |
| Sorting                                 | Yes                  | You can sort fields in the **Rows** or **Columns** field wells alphabetically or by a metric in ascending or descending order.                                                                                                                                                                                                                                                     | [Sorting visual data in Amazon Quick Suite](sorting-visual-data.md "sorting-visual-data.md") [Sorting pivot tables in Quick Suite](sorting-pivot-tables.md "sorting-pivot-tables.md")   |
| Performing field aggregation            | Yes                  | You must apply aggregation to the field or fields you choose for the value. You can't apply aggregation to the fields that you choose for the rows or columns. If you choose to create a multi-measure pivot table, you can apply different types of aggregation to the different measures. For example, you can show the sum of the sales amount and the maximum discount amount. | [Changing field aggregation](changing-field-aggregation.md "changing-field-aggregation.md")                                                                                             |
| Adding drill-downs                      | No                   |                                                                                                                                                                                                                                                                                                                                                                                    | [Adding drill-downs to visual data in Quick Sight](adding-drill-downs.md "adding-drill-downs.md")                                                                                       |
| Showing and hiding totals and subtotals | Yes                  | You can show or hide totals and subtotals for rows and columns. Metrics automatically roll up to show subtotals when you collapse a row or column. If you use a table calculation, use aggregates to display roll-ups.                                                                                                                                                             |                                                                                                                                                                                         |
| Exporting or copying data               | Yes                  | You can export all of the data to a CSV file. You can select and copy the content of the cells.                                                                                                                                                                                                                                                                                    | [Exporting data from visuals](exporting-data.md "exporting-data.md")                                                                                                                    |
| Conditional formatting                  | Yes                  | You can add conditional formatting for values, subtotals and totals.                                                                                                                                                                                                                                                                                                               | [Conditional formatting on visual types in Quick Suite](conditional-formatting-for-visuals.md "conditional-formatting-for-visuals.md")                                                  | ###### Topics |

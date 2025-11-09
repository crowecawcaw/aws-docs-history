# Using heat maps

Use heat maps to show a measure for the intersection of two dimensions, with
color-coding to easily differentiate where values fall in the range. Heat maps can also
be used to show the count of values for the intersection of the two dimensions.

Each rectangle on a heat map represents the value for the specified measure for the
intersection of the selected dimensions. Rectangle color represents where the value
falls in the range for the measure, with darker colors indicating higher values and
lighter colors indicating lower ones.

Heat maps and pivot tables display data in a similar tabular fashion. Use a heat map
if you want to identify trends and outliers, because the use of color makes these easier
to spot. Use a pivot table if you want to further analyze data on the visual, for
example by changing column sort order or applying aggregate functions across rows or
columns.

To create a heat map, choose at least two fields of any data type. Amazon Quick Suite
populates the rectangle values with the count of the x-axis value for the intersecting
y-axis value. Typically, you choose a measure and two dimensions.

Heat maps show up to 50 data points for rows and up to 50 data points for columns. For
more information about how Amazon Quick Suite handles data that falls outside display limits,
see [Display limits](working-with-visual-types.md#display-limits "working-with-visual-types.md#display-limits").

## Heat map features

To understand the features supported by heat maps, use the following table.

| Feature                           | Supported?           | Comments                                                                                                                                                                                    | For more information                                                                                                                                                                          |
| --------------------------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Changing the legend display       | Yes                  |                                                                                                                                                                                             | [Legends on visual types in<br>Quick Suite](customizing-visual-legend.md "customizing-visual-legend.md")                                                                                      |
| Changing the title display        | Yes                  |                                                                                                                                                                                             | [Titles and subtitles on visual types in<br>Quick Suite](customizing-a-visual-title.md "customizing-a-visual-title.md")                                                                       |
| Changing the axis range           | Not applicable       |                                                                                                                                                                                             | [Range and scale on visual types in<br>Quick Suite](changing-visual-scale-axis-range.md "changing-visual-scale-axis-range.md")                                                                |
| Changing the visual colors        | No                   |                                                                                                                                                                                             | [Colors in visual types in<br>Quick Suite](changing-visual-colors.md "changing-visual-colors.md")                                                                                             |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude a rectangle in a heat map, except<br>when you are using a date field as the rows dimension. In that case,<br>you can only focus on a rectangle, not exclude it. | [Focusing on visual<br>elements](focusing-on-visual-elements.md "focusing-on-visual-elements.md")<br>[Excluding visual elements](excluding-visual-elements.md "excluding-visual-elements.md") |
| Sorting                           | Yes                  | You can sort by the fields you choose for the columns and the<br>values.                                                                                                                    | [Sorting visual data in Amazon Quick Suite](sorting-visual-data.md "sorting-visual-data.md")                                                                                                  |
| Performing field aggregation      | Yes                  | You must apply aggregation to the fields you choose for the<br>value, and can't apply aggregation to the fields you choose for<br>the rows or columns.                                      | [Changing field aggregation](changing-field-aggregation.md "changing-field-aggregation.md")                                                                                                   |
| Adding drill-downs                | Yes                  | You can add drill-down levels to the **Rows**<br>and \*_Columns_<br>• field wells.                                                                                                          | [Adding drill-downs to visual data in<br>Quick Sight](adding-drill-downs.md "adding-drill-downs.md")                                                                                          |
| Conditional formatting            | No                   |                                                                                                                                                                                             | [Conditional formatting on visual<br>types in Quick Suite](conditional-formatting-for-visuals.md "conditional-formatting-for-visuals.md")                                                     |

## Creating a heat map

Use the following procedure to create a heat map.

###### To create a heat map

1. On the analysis page, choose **Visualize** on the tool
   bar.
2. Choose **Add** on the application bar, and then choose
   **Add visual**.
3. On the **Visual types** pane, choose the heat map
   icon.
4. From the **Fields list** pane, drag the fields that you
   want to use to the appropriate field wells. Typically, you want to use
   dimension or measure fields as indicated by the target field well. If you
   choose to use a dimension field as a measure, the **Count**
   aggregate function is automatically applied to it to create a numeric
   value.

To create a heat map, drag a dimension to the **Rows**
field well, a dimension to the **Columns** field well, and
a measure to the **Values** field well. 5. (Optional) Add drill-down layers by dragging one or more additional fields
to the **Rows** or **Columns** field
wells. For more information about adding drill-downs, see [Adding drill-downs to visual data in
Quick Sight](adding-drill-downs.md "adding-drill-downs.md").

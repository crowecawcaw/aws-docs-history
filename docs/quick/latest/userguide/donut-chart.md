# Using donut charts

Use donut charts to compare values for items in a dimension. The best use for this
type of chart is to show a percentage of a total amount.

Each wedge in a donut chart represents one value in a dimension. The size of the wedge
represents the proportion of the value for the selected measure that the item represents
compared to the whole for the dimension. Donut charts are best when precision isn't
important and there are few items in the dimension.

To learn how to use donut charts in Amazon Quick, you can
watch this video:

To create a donut chart, use one dimension in the **Group/Color**
field well. With only one field, the chart displays the division of values by row count.
To display the division of dimension values by a metric value, you can add a metric
field to the **Value** field well.

Donut charts show up to 20 data points for group or color. For more information about
how Amazon Quick handles data that falls outside display limits, see [Display limits](working-with-visual-types.md#display-limits "working-with-visual-types.md#display-limits").

## Donut chart features

To understand the features supported by donut charts, use the following
table.

| Feature                           | Supported?           | Comments                                                                                                                                                                                                         | For more information                                                                                                                                                                          |
| --------------------------------- | -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Changing the legend display       | Yes                  |                                                                                                                                                                                                                  | [Legends on visual types in<br>Quick](customizing-visual-legend.md "customizing-visual-legend.md")                                                                                            |
| Changing the title display        | Yes                  |                                                                                                                                                                                                                  | [Titles and subtitles on visual types in<br>Quick](customizing-a-visual-title.md "customizing-a-visual-title.md")                                                                             |
| Changing the axis range           | Not applicable       |                                                                                                                                                                                                                  | [Range and scale on visual types in<br>Quick](changing-visual-scale-axis-range.md "changing-visual-scale-axis-range.md")                                                                      |
| Changing the visual colors        | Yes                  |                                                                                                                                                                                                                  | [Colors in visual types in<br>Quick](changing-visual-colors.md "changing-visual-colors.md")                                                                                                   |
| Focusing on or excluding elements | Yes, with exceptions | You can focus on or exclude a wedge in a donut chart, except when<br>you are using a date field as a dimension. In that case, you can<br>only focus on a wedge, not exclude it.                                  | [Focusing on visual<br>elements](focusing-on-visual-elements.md "focusing-on-visual-elements.md")<br>[Excluding visual elements](excluding-visual-elements.md "excluding-visual-elements.md") |
| Sorting                           | Yes                  | You can sort on the field that you choose for the value or the<br>group or color.                                                                                                                                | [Sorting visual data in Amazon Quick](sorting-visual-data.md "sorting-visual-data.md")                                                                                                        |
| Performing field aggregation      | Yes                  | You must apply aggregation to the field that you choose for the<br>value, and can't apply aggregation to the field that you choose<br>for group or color.                                                        | [Changing field aggregation](changing-field-aggregation.md "changing-field-aggregation.md")                                                                                                   |
| Adding drill-downs                | Yes                  | You can add drill-down levels to the<br>\*_Group/Color_<br>• field well.                                                                                                                                         | [Adding drill-downs to visual data in<br>Quick Sight](adding-drill-downs.md "adding-drill-downs.md")                                                                                          |
| Choosing size                     | Yes                  | You can choose how thick the donut chart is: small, medium, and<br>large.                                                                                                                                        | [Formatting in Amazon Quick](formatting-a-visual.md "formatting-a-visual.md")                                                                                                                 |
| Showing totals                    | Yes                  | You can choose to display or hide the aggregate of the<br>**Value\*<br>• field. By default, this displays the<br>total count of the **Group/Color*<br>• field, or the<br>total sum of the \*\*Value*<br>• field. | [Formatting in Amazon Quick](formatting-a-visual.md "formatting-a-visual.md")                                                                                                                 |

## Creating a donut chart

Use the following procedure to create a donut chart.

###### To create a donut chart

1. On the analysis page, choose **Visualize** on the tool
   bar.
2. Choose **Add** on the application bar, and then choose
   **Add visual**.
3. On the **Visual types** pane, choose the donut chart
   icon.
4. From the **Fields list** pane, drag the fields that you
   want to use to the appropriate field wells. Typically, you want to use
   dimension or measure fields as indicated by the target field well. If you
   choose to use a dimension field as a measure, the **Count**
   aggregate function is automatically applied to it to create a numeric
   value.

To create a donut chart, drag a dimension to the
**Group/Color** field well. Optionally, drag a measure
to the **Value** field well. 5. (Optional) Add drill-down layers by dragging one or more additional fields
to the **Group/Color** field well. For more information
about adding drill-downs, see [Adding drill-downs to visual data in
Quick Sight](adding-drill-downs.md "adding-drill-downs.md").

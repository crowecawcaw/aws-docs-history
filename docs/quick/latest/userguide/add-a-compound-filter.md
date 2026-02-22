# Adding filter conditions (group filters) with

AND and OR operators

In analyses, when you add multiple filters to a visual, Quick uses the AND
operator to combine them. You can also add filter conditions to a single filter with the
OR operator. This is called a compound filter, or filter group.

To add multiple filters using the OR operator, create a filter group. Filter grouping
is available for all types of filters in analyses.

When you filter on multiple measures (green fields marked with #), you can apply
the filter conditions to an aggregate of that field. Filters
in a group can contain either aggregated or nonaggregated fields, but not both.

###### To create a filter group

1. Create a new filter in an analysis. For more information about creating
   filters, see [Adding filters](add-a-filter-data-prep.md "add-a-filter-data-prep.md").
2. In the **Filters** pane, choose the new filter to expand
   it.
3. In the expanded filter, choose **Add filter condition** at
   bottom, and then choose a field to filter on.
4. Choose the conditions to filter on.

The data type of the field that you selected determines the options available
here. For example, if you chose a numeric field, you can specify the
aggregation, filter condition, and values. If you chose a text field, you can
chose the filter type, filter condition, and values. And if you chose a date
field, you can specify the filter type, condition, and time granularity. For
more information about these options, see [Filter types in Amazon Quick](filtering-types.md "filtering-types.md"). 5. (Optional) You can add additional filter conditions to the filter group by
choosing **Add filter condition** again at bottom. 6. (Optional) To remove a filter from the filter group, choose the trash-can
icon near the field name. 7. When finished, choose **Apply**.

The filters appear as a group in the **Filters** pane.

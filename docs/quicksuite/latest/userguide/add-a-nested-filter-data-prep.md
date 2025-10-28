# Adding nested filters

Nested filters are advanced filters that can be added to a Quick Suite analysis.
A Nested filter filters a field using a subset of data defined by another field in that
same dataset. This allows authors to show additional contextual data without the need to
filter data out if the data point doesn't meet an initial condition.

Nested filters function similarly to a correlated subquery in SQL or a market basket
analysis. For example, say you want to perform a market basket analysis on your sales
data. You can use nested filters to find the sales quantity by product for customers who
have or have not purchased a specific product. You can also use nested filters to
identify groups of customers that did not purchase a selected product or who only
purchased a specific list of products.

Nested filters can only be added at the analysis level. You can't add a nested
filter to a dataset.

Use the procedure below to add a nested filter to a Quick Suite analysis.

1. Open the [Quick Suite console](https://quicksight.aws.amazon.com/ "https://quicksight.aws.amazon.com/").
2. Choose **Analyses**, and then choose the analysis that you
   want to add a nested filter to.
3. Create a new filter on the text field that you want to filter on. For more
   information about creating a filter, see [Adding filters in analyses](add-a-filter-data-prep.md#add-a-filter-data-prep-analyses "add-a-filter-data-prep.md#add-a-filter-data-prep-analyses").
4. After you create the new filter, locate the new filter in the
   **Filters** pane. Choose the ellipsis (three dots) next to
   the new filter, and then choose **Edit filter**. Alternatively,
   choose the filter entity in the **Filters** pane to open the
   **Edit filter** pane.
5. The **Edit filter** pane opens. Open the **Filter
   type** dropdown menu, navigate to the **Avanced
   filter** section, and then choose **Nested
   filter**.
6. For **Qualifying condition**, choose
   **Include** or **Exclude**. The
   _qualifying condition_ allows you to run a not in the set
   query on the data in your analysis. In our sales example above, the qualifying
   condition determines if the filter returns a list of customers who did buy the
   specifc product or a list of customers who did not buy the product.
7. For **Nested field**, choose the text field that you want to
   filter data with. The nested field cannot be the same as the primary field
   selected in step 3. Category fields are the only supported field type for the
   inner filter.
8. For **Nested filter type**, choose the filter type that you
   want. The filter type that you choose determines the final configuration steps
   for the nested filter. Available filter types and information about their
   configuration can be found in the list below.
   - [Filter
     list](text-filter-list.md "text-filter-list.md")
   - [Custom filter list](add-text-custom-filter-list-data-prep.md "add-text-custom-filter-list-data-prep.md")
   - [Custom filter](add-text-filter-custom-list-data-prep.md "add-text-filter-custom-list-data-prep.md")

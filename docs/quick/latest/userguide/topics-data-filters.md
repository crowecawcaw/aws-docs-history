# Adding filters to a Amazon Quick Sight topic

dataset

Sometimes your business users (readers) might ask questions that contain terms
that map to multiple cells of values in the data. For example, let's say one of
your readers asks, "Show me weekly sales trend in the west."
_West_ in this instance refers to both the
`Northwest` and `Southwest` values in the
`Region` field, and requires the data to be filtered to generate an
answer. You can add filters to a topic to support requests like these.

###### To add a filter to a topic

1.  Open the topic that you want to add a filter to.
2.  In the topic, choose the **Data** tab.
3.  For **Actions**, choose **Add
    filter**.
4.  In the **Filter configuration** page that opens, do the
    following:
    1. For **Name**, enter a friendly name for the
       filter.
    2. For **Dataset**, choose a dataset that you want
       to apply the filter to.
    3. For **Field**, choose the field that you want to
       filter.

    Depending on the type of field you choose, you're offered
    different filtering options.

        * If you chose a text field (for example,
         `Region`), do the following:




        	1. For **Filter type**, choose the
        	 type of filter that you want.


        	For more information about filter text fields, see
        	 [Adding text filters](add-a-text-filter-data-prep.md "add-a-text-filter-data-prep.md").
        	2. For **Rule**, choose a
        	 rule.
        	3. For **Value**, enter one or more
        	 values.
        * If you chose a date field (for example,
         `Date`), do the following:




        	1. For **Filter type**, choose the
        	 type of filter that you want, and then enter the
        	 date or dates that you want to apply the filter
        	 to.


        	For more information about filtering dates, see
        	 [Adding date filters](add-a-date-filter2.md "add-a-date-filter2.md").
        * If you chose a numeric field (for example,
         `Compensation`), do the following:




        	1. For **Aggregation**, choose how
        	 you want to aggregate the filtered values.
        	2. For **Rule**, choose a rule for
        	 the filter, and then enter a value for that
        	 rule.
        For more information about filtering numeric fields, see
         [Adding numeric filters](add-a-numeric-filter-data-prep.md "add-a-numeric-filter-data-prep.md").

    4. (Optional) To specify when the filter is applied, choose
       **Apply the filter anytime the dataset is
       used**, and then choose one of the following:
       - **Apply always** – When you choose
         this option, the filter is applied whenever any column from
         the dataset you specified is linked to a question.
       - **Apply always, unless a question results in an
         explicit filter from the dataset** –
         When you choose this option, the filter is applied whenever
         any column from the dataset you specified is linked to a
         question. However, if the question mentions an explicit
         filter on the same field, the filter isn't applied.

    5. When finished, choose **Save**.

    The filter is added to the list of fields in the topic. You can
    edit the description for it or adjust when the filter is
    applied.

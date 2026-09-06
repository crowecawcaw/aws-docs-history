

# Tutorial: Create a prepared Amazon Quick Sight dataset
<a name="example-prepared-data-set"></a>

Use the following procedure to prepare the Marketing dataset and create an analysis. If you don't see the Web and Social Media Analytics sample data already in Amazon Quick Sight, you can download it: [web-and-social-analytics.csv.zip](samples/web-and-social-analytics.csv.zip).

**To prepare the Marketing dataset and create an analysis**

1. From the Amazon Quick homepage, choose **Data** in the navigation pane.

1. In the **Datasets** tab, choose **New** then **Dataset**.

1. From the existing data sources, choose the **Web and Social Media Analytics** Amazon S3 data source. Choose your table and then choose **Edit/Preview data**.

   Amazon Quick opens the data preparation page.

1. For **Dataset Name**, enter **Marketing Sample** to replace *Web and Social Media Analytics* for the dataset name.

1. Exclude some fields from the dataset.

   In the **Fields** pane, choose the three-dot menu for the **Twitter followers cumulative** and **Mailing list cumulative** fields, and then choose **Exclude field**. To select more than one field at a time, press the Ctrl key while you select (Command key on Mac).

1. Rename a field.

   In the **Dataset** preview pane, scroll to the **Website Pageviews** field and choose the pencil icon to edit.

   In the **Edit field** page that opens, for **Name**, enter **Website page views**, and then choose **Apply**.

1. Add a calculated field that substitutes a text string for any 0-length string value in the **Events** field:

   1. On the data preparation page, scroll to the top of the **Fields** pane, and then choose **Add calculated field**.

   1. In the **Add calculated field** page that opens, for **Add name**, enter **populated\_event**.

   1. In the **Functions** pane at right, double-click the **ifelse** function from the list of functions. This adds the function to the calculated field formula.

   1. Expand the **Field list** pane by choosing the drop-down arrow, and then double-click the **Events** field. This adds the field to the calculated field formula.

   1. In formula editor, enter the following additional functions and parameters required, in bold in the following: ifelse(**strlen(**{Events}**)=0, 'Unknown', {Events}**).

      The final formula should be as follows: `ifelse(strlen({Events})=0, 'Unknown', {Events})`.

   1. Choose **Save**.

      The new calculated field is created, and appears at the top of the **Fields** pane.

1. Choose **Save**.

## Next steps
<a name="example-next-step-data-set"></a>

Create an analysis by using the procedure in [Tutorial: Create an Amazon Quick Sight analysis](example-create-an-analysis.md).
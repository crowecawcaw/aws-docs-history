# Using Union to combine rows

You use the Union transform node when you want to combine rows from more than one data
source that have the same schema.

There are to types of Union transformations:

1. ALL – when applying ALL, the resulting union does not remove duplicate rows.
2. DISTINCT – when applying DISTINCT, the resulting union removes duplicate rows.

**Unions vs. Joins**

You use Union to combine rows. You use Join to combine columns.

###### Using the Union transform in the Visual ETL canvas

1. Add more than one data source to perform a union transform. To add a data source, open the Resource Panel, then choose
   the data source from the Sources tab. Before using the Union transformation,
   you must ensure that all data sources involved in the union have the same schema and structure.
2. When you have at least two data sources that you want to combine using the Union transform, create the Union transform by adding it to the canvas.
   Open the Resource Panel on the canvas and search for 'Union'. You can also choose the Transforms tab in the Resource Panel and
   scroll down until you find the Union transform, then choose **Union**.
3. Select the Union node on the job canvas. In the Node properties window, choose the parent nodes to connect to the Union transform.
4. AWS Glue checks for compatibility to make sure that the Union transform can be applied to all data sources.
   If the schema for the data sources are the same, the operation will be allowed. If the data sources do not have the same schema,
   an invalid error message is displayed: “The input schemas of this union are not the same. Consider using ApplyMapping to match the schemas.”
   To fix this, choose Use **ApplyMapping**.
5. Choose the Union type.
   1. All – By default, the All Union type is selected; this will result in duplicate rows if there are any in the data combination.
   2. Distinct – Choose Distinct if you want duplicate rows to be removed from the resulting data combination.

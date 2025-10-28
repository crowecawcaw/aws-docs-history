# Explode array or map into rows transform

You can use the Explode transform to extract values from a nested structure into
individual rows that are easier to manipulate. In the case of an array, the transform will
generate a row for each value of the array, replicating the values for the other columns in
the row. In the case of a map, the transform will generate a row for each entry with the key
and value as columns plus any other columns in the row.

For example, if we have this dataset which has a “category” array column with multiple
values.

| product_id | category                     |
| ---------- | ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1          | [sports, winter]             |
| 2          | [garden, tools]              |
| 3          | [videos]                     |
| 4          | [games, electronics, social] |
| 5          | []                           | If you explode the 'category' column into a column with the same name, you will override the column. You can select that you want NULLs included to get the following (ordered for illustration purposes):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| 1          | sports                       |
| ---        | ---                          |
| 1          | winter                       |
| 2          | garden                       |
| 2          | tools                        |
| 3          | videos                       |
| 4          | games                        |
| 4          | electronics                  |
| 4          | social                       |
| 5          |                              | ###### To add an Explode Array Or Map Into Rows transform: 1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio. 2. Choose the plus icon to open the **Add nodes** menu. 3. Under **Transforms**, choose **Explode Array or Map Into Rows**. 4. Select the diagram to add the node to your visual ETL job. 5. Select the node on the diagram to view details about the transform. 6. Under **Column to explode**, enter the name of an existing column that will be exploded. 7. Under **New column name**, enter the name of a new column that will be generated. 8. (Optional) Under **Values column**, if you are exploding a dictionary, specify a name for a column to contain the values. 9. Use the toggle to indicate whether or not to include null values. By default, if the column to explode is NULL or has an empty structure, it will be omitted on the exploded dataset. |

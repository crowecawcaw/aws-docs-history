# Extract JSON path transform

Use this transform to extract new columns from a string column with JSON data.

###### To add an Extract JSON path transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Extract JSON
   Path**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **JSON column**, select a column from the data source.
8. Under **JSON paths**, enter a JSON path or multiple paths separated
   by commas to specify the location to extract the data from.
9. Under **Output columns**, enter the names of the columns to create
   from each of the JSON paths.
10. (Optional) If desired, use the toggle to drop the JSON column.

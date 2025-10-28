# Parse JSON column transform

Use this transform to parse a string column that contains JSON data.

###### To add a Parse JSON Column transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Parse JSON
   Column**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **JSON column**, choose the column that contains JSON
   data
8. Enter a number to use as a ratio of samples to use for inferring schema. This must
   be a value between 0.1 and 1, with 1 meaning all samples are used. If your JSON strings
   are consistent, you can use a lower value to speed up the inference.
9. (Optional) Enter a name for the new column.

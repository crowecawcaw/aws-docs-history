# Add current timestamp transform

The Add Current Timestamp transform allows you to mark the rows with the time on which
the data was processed. This is useful for auditing purposes or to track latency in the data
pipeline. You can add this new column as a timestamp data type or a formatted string.

###### To add an Add Current Timestamp transform:

1. Navigate to your Visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Add Current
   Timestamp**.
4. Select the diagram to add the node to your Visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Timestamp column name**, enter a custom name for the new
   column.
7. (Optional) under **Timestamp format**, enter a format if you would
   prefer the column to be a formatted date string.

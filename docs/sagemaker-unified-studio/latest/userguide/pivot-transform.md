# Pivot rows into columns transform

Use this transform to aggregate the values of a numeric column into categories by using
the values of the columns configured.

###### To add a Pivot Rows Into Columns transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Pivot Rows Into
   Columns**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **Aggregation column**, select a numeric column to
   use.
8. Under **Aggregation**, select a Spark function to apply to the
   aggregation column.
9. Under **Columns to convert**, select columns whose values will
   become new columns.

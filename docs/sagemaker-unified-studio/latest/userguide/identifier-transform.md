# Identifier transform

Use this transform to assign a numeric identifier for each row in the dataset.

###### To add an Identifier transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose
   **Identifier**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **Column name**, enter a name for the new column. This column
   is named id by default.
8. (Optional) If you want to make the ID unique among the job runs, switch the toggle
   to on to include a timestamp and extend the column type from long to decimal.

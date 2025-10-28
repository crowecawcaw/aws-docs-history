# Unpivot columns into rows transform

Use this transform to convert column names into values of a new column and generate one
row for each column in the original row.

###### To add an Unpivot Columns Into Rows transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Unpivot Columns Into
   Rows**.
4. Select the diagram to add the node to your visual ETL job.
5. Connect the transform node to a data source node.
6. Select the node on the diagram to view details about the transform.
7. Under **Unpivot names column**, enter a column to create out of the
   source column names.
8. Under **Unpivot values column**, enter a column to create out of
   the source column values.
9. Under **Columns to unpivot into the new value column**, select the
   column or columns whose names will become the values of the new column.

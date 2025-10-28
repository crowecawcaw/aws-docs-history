# Autobalance processing transform

Use this transform to repartition data to optimize future cluster resource usage. This
transform is particularly useful for uneven datasets.

###### To add an Autobalance Processing transform:

1. Navigate to your visual ETL job in Amazon SageMaker Unified Studio.
2. Choose the plus icon to open the **Add nodes** menu.
3. Under **Transforms**, choose **Autobalance
   Processing**.
4. Select the diagram to add the node to your visual ETL job.
5. Select the node on the diagram to view details about the transform.
6. Under **Number of partitions**, input a number of partitions to
   randomly distribute the data into. Or, switch the toggle to off to use the number of
   cores as the partition number.
7. (Optional) Under **Repartition columns**, identify columns that you
   want data of the same value to be assigned to the same partition in.

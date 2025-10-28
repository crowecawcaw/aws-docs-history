# Terminating and removing an Amazon EMR on EC2 cluster

###### Warning

A terminated EMR Cluster is irrecoverable. Ensure that the resource and any data on HDFS or jupyter notebooks is no longer required prior to removal.

When you no longer need an Amazon EMR on EC2 cluster, the cluster can be terminated and removed.

To remove a cluster:

1. Login to the Amazon SageMaker Unified Studio and navigate to the **Data processing** tab of the Compute section.
   Select the name of the compute instance you would like to remove.
2. On the compute details page, select the **Terminate and remove** option.
3. A dialog box will appear asking you to confirm that you want to terminate and remove the
   instance of compute, which in this case is your Amazon EMR on EC2 cluster. Confirm that you want to remove the compute, by typing "confirm" in the text box.
4. Choose **Terminate and remove compute** to begin termination and removal.
5. After a few minutes, your cluster should have been removed.

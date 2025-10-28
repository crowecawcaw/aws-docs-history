# Add destination nodes

A destination node in SageMaker Canvas specifies where to store your processed and transformed data.
When you choose to export your transformed data to Amazon S3, Canvas uses the specified
destination node location, applying all the transformations you've configured in your data
flow. For more information about export jobs to Amazon S3, see the preceding section [Export to Amazon S3](canvas-export-data.md#canvas-export-data-s3 "canvas-export-data.md#canvas-export-data-s3").

By default, choosing to export your data to Amazon S3 adds a destination node to your data
flow. However, you can add multiple destination nodes to your flow, allowing you to
simultaneously export different sets of transformations or variations of your data to
different Amazon S3 locations. For example, you can create one destination node that exports the
data after applying all transformations, and another destination node that exports the data
after only certain initial transformations, such as a join operation. This flexibility
enables you to export and store different versions or subsets of your transformed data in
separate S3 locations for various use cases.

Use the following procedure to add a destination node to your data flow.

###### To add a destination node

1. Navigate to your data flow.
2. Choose the ellipsis icon next to the node where you want to place the destination
   node.
3. In the context menu, hover over **Export**, and then select
   **Add destination**.
4. In the **Export destination** side panel, enter a
   **Dataset name** to name the output.
5. For **Amazon S3 location**, enter the Amazon S3 location to which you want
   to export the output. You can enter the S3 URI, alias, or ARN of the S3 location or
   S3 access point. For more information access points, see [Managing data access with
   Amazon S3 access points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md") in the _Amazon S3 User
   Guide_.
6. For **Export settings**, specify the following fields:
   1. **File type** – The file format of the exported
      data.
   2. **Delimiter** – The delimiter used to separate
      values in the file.
   3. **Compression** – The compression method used to
      reduce the file size.

7. For **Partitioning**, specify the following fields:
   1. **Number of partitions** – The number of dataset
      files that SageMaker Canvas writes as the output of the job.
   2. **Choose columns** – You can choose a subset of
      columns from the data to include in the partitions.

8. Choose **Add** if you want to simply add a destination node to
   your data flow, or choose **Add** and then choose
   **Export** if you want to add the node and initiate an export
   job.
   You should now see a new destination node in your flow.

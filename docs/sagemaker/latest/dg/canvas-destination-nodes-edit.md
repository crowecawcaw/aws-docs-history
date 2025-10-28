# Edit a destination node

A _destination node_ in a Amazon SageMaker Canvas data flow specifies
the Amazon S3 location where your processed and transformed data is stored, applying all the
configured transformations in your data flow. You can edit the configuration of an existing
destination node and then choose to re-run the job to overwrite the data in the specified
Amazon S3 location. For more information about adding a new destination node, see [Add destination nodes](canvas-destination-nodes-add.md "canvas-destination-nodes-add.md").

Use the following procedure to edit a destination node in your data flow and initiate an
export job.

###### To edit a destination node

1. Navigate to your data flow.
2. Choose the ellipsis icon next to the destination node that you want to
   edit.
3. In the context menu, choose **Edit**.
4. The **Edit destination** side panel opens. From this panel, you
   can edit details such as the dataset name, the Amazon S3 location, and the export and
   partitioning settings.
5. (Optional) In **Additional nodes to export**, you can select more
   destination nodes to process when you run the export job.
6. Leave the **Process entire dataset** option selected if you want
   Canvas to apply your data flow transforms to your entire dataset and export the
   result. If you deselect this option, Canvas only applies the transforms to the
   sample of your dataset used in the interactive Data Wrangler data flow.
7. Leave the **Auto job configuration** option selected if you want
   Canvas to automatically determine whether to run the job using Canvas
   application memory or an EMR Serverless job. If you deselect this option and
   manually configure your job, then you can choose to use either an EMR Serverless or
   a SageMaker Processing job. For instructions on how to configure an EMR Serverless or a
   SageMaker Processing job, see the preceding section [Export to Amazon S3](canvas-export-data.md#canvas-export-data-s3 "canvas-export-data.md#canvas-export-data-s3").
8. When you're done making changes, choose **Update**.
   Saving changes to your destination node configuration doesn't automatically re-run a job
   or overwrite data that has already been processed and exported. Export your data again to
   run a job with the new configuration. If you decide to export your data again with a job,
   Canvas uses the updated destination node configuration to transform and output the data
   to the specified location, overwriting any existing data.

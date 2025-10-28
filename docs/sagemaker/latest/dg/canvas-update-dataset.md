# Update a dataset

After importing your initial dataset into Amazon SageMaker Canvas, you might have
additional data that you want to add to your dataset. For example, you might get
inventory data at the end of every week that you want to add to your dataset.
Instead of importing your data multiple times, you can update your existing dataset
and add or remove files from it.

###### Note

You can only update datasets that
you have imported through local upload or Amazon S3.

You can
update your dataset either manually or automatically. For more information
about automatic dataset updates, see [Configure automatic updates for a
dataset](canvas-update-dataset-auto.md "canvas-update-dataset-auto.md").

Every time you update your dataset, Canvas creates a
new version of your dataset. You can only use the latest version of your
dataset to build a model or generate predictions. For more information about
viewing the version history of your dataset, see [View your dataset details](canvas-import-dataset.md#canvas-view-dataset-details "canvas-import-dataset.md#canvas-view-dataset-details").

You can also use dataset updates
with automated batch predictions, which starts a
batch prediction job whenever you update your dataset. For more information, see
[Batch predictions in SageMaker Canvas](canvas-make-predictions-batch.md "canvas-make-predictions-batch.md").

The following section describes how to do manual updates to your
dataset.

## Manually update a dataset

To do a manual update, do the following:

1. Open the SageMaker Canvas application.
2. In the left navigation pane, choose **Datasets**.
3. From the list of datasets, choose the dataset you want to update.
4. Choose the **Update dataset** dropdown menu and choose
   **Manual update**. You are taken to the import data
   workflow.
5. From the **Data source** dropdown menu,
   choose either **Local upload** or **Amazon S3**.
6. The page shows you a preview of your data. From here, you can add or
   remove files from the dataset. If you’re importing tabular data, the schema
   of the new files (column names and data types) must match the schema of the
   existing files. Additionally, your new files must not exceed the maximum
   dataset size or file size. For more information about these limitations,
   see [Import a dataset](canvas-import-dataset.md "canvas-import-dataset.md").

###### Note

If you add a file with the same name as an existing file in your
dataset, the new file overwrites the old version of the file. 7. When you’re ready to save your changes, choose **Update dataset**.

You should now have a new version of your dataset.

On the **Datasets** page, you can choose the
**Version history** tab to see all of the versions of your
dataset and the history of both manual and automatic updates you’ve made.

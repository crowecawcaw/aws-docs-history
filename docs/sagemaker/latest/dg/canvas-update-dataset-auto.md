# Configure automatic updates for a

dataset

After importing your initial dataset into Amazon SageMaker Canvas, you might have additional data that
you want to add to your dataset. For example, you might get inventory data at the end of
every week that you want to add to your dataset. Instead of importing your data multiple
times, you can update your existing dataset and add or remove files from it.

###### Note

You can only update datasets that you have imported through local upload or
Amazon S3.

With automatic dataset updates, you
specify a location where Canvas checks for files at a frequency you specify. If you
import new files during the update, the schema of the files must match the existing dataset
exactly.

Every time you update your dataset, Canvas creates a new version of your dataset. You
can only use the latest version of your dataset to build a model or generate predictions.
For more information about viewing the version history of your dataset, see [View your dataset details](canvas-import-dataset.md#canvas-view-dataset-details "canvas-import-dataset.md#canvas-view-dataset-details").

You can also use dataset updates with automated batch predictions, which starts a batch
prediction job whenever you update your dataset. For more information, see [Batch predictions in SageMaker Canvas](canvas-make-predictions-batch.md "canvas-make-predictions-batch.md").

The following section describes how to do automatic updates to your
dataset.

An automatic update is when you set up a configuration for Canvas to update your
dataset at a given frequency. We recommend that you use this option if you regularly receive
new files of data that you want to add to your dataset.

When you set up the auto update configuration, you specify an Amazon S3 location where you
upload your files and a frequency at which Canvas checks the location and imports files.
Each instance of Canvas updating your dataset is referred to as a _job_. For each job, Canvas imports all of the files in the
Amazon S3 location. If you have new files with the same names as existing files in your dataset,
Canvas overwrites the old files with the new files.

For automatic dataset updates, Canvas doesn’t perform schema validation. If the schema
of files imported during an automatic update don’t match the schema of the existing files or
exceed the size limitations (see [Import a dataset](canvas-import-dataset.md "canvas-import-dataset.md") for a
table of file size limitations), then you get errors when your jobs run.

###### Note

You can only set up a maximum of 20 automatic configurations in your Canvas
application. Additionally, Canvas only does automatic updates while you’re logged in
to your Canvas application. If you log out of your Canvas application, automatic
updates pause until you log back in.

To configure automatic updates for your dataset, do the following:

1. Open the SageMaker Canvas application.
2. In the left navigation pane, choose **Datasets**.
3. From the list of datasets, choose the dataset you want to update.
4. Choose the **Update dataset** dropdown menu and choose
   **Automatic update**. You are taken to the **Auto
   updates**tab for the dataset.
5. Turn on the **Auto update enabled** toggle.
6. For **Specify a data source**, enter the Amazon S3 path to a folder
   where you plan to regularly upload files.
7. For **Choose a frequency**, select **Hourly**,
   **Weekly**, or **Daily**.
8. For **Specify a starting time**, use the calendar and time picker
   to select when you want the first auto update job to start.
9. When you’re ready to create the auto update configuration, choose
   **Save**.
   Canvas begins the first job of your auto update cadence at the specified starting
   time.

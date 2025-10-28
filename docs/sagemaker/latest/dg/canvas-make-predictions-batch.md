# Batch predictions in SageMaker Canvas

Make batch predictions when you have an entire dataset for which you’d like to
generate predictions. Amazon SageMaker Canvas supports batch predictions for datasets up to PBs in
size.

There are two types of batch predictions you can make:

- [Manual batch predictions](canvas-make-predictions-batch-manual.md "canvas-make-predictions-batch-manual.md") are when you
  have a dataset for which you want to make one-time predictions.
- [Automatic batch predictions](canvas-make-predictions-batch-auto.md "canvas-make-predictions-batch-auto.md") are when
  you set up a configuration that runs whenever a specific dataset is updated. For
  example, if you’ve configured weekly updates to a SageMaker Canvas dataset of inventory
  data, you can set up automatic batch predictions that run whenever you update
  the dataset. After setting up an automated batch predictions workflow, see [How to manage automations](canvas-manage-automations.md "canvas-manage-automations.md") for more information about
  viewing and editing the details of your configuration. For more information
  about setting up automatic dataset updates, see [Configure automatic updates for a
  dataset](canvas-update-dataset-auto.md "canvas-update-dataset-auto.md").

###### Note

Time series forecasting models don't support automatic batch predictions.

You can only set up automatic batch predictions for datasets imported through local upload or
Amazon S3. Additionally, automatic batch predictions can only run while you’re logged in
to the Canvas application. If you log out of Canvas, the automatic batch
prediction job resumes when you log back in.

To get started, review the [Batch prediction dataset requirements](canvas-make-predictions-batch-preqreqs.md "canvas-make-predictions-batch-preqreqs.md"), and then choose one of the
following manual or automatic batch prediction workflows.

###### Topics

- [Batch prediction dataset requirements](canvas-make-predictions-batch-preqreqs.md "canvas-make-predictions-batch-preqreqs.md")
- [Make manual batch predictions](canvas-make-predictions-batch-manual.md "canvas-make-predictions-batch-manual.md")
- [Make automatic batch predictions](canvas-make-predictions-batch-auto.md "canvas-make-predictions-batch-auto.md")
- [Edit your automatic batch prediction configuration](canvas-make-predictions-batch-auto-edit.md "canvas-make-predictions-batch-auto-edit.md")
- [Delete your automatic batch prediction configuration](canvas-make-predictions-batch-auto-delete.md "canvas-make-predictions-batch-auto-delete.md")
- [View your batch prediction jobs](canvas-make-predictions-batch-auto-view.md "canvas-make-predictions-batch-auto-view.md")

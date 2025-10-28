# How data processing works in Data Wrangler

While working with data interactively in an Amazon SageMaker Data Wrangler data flow, Amazon SageMaker Canvas only applies the
transformations to a sample dataset for you to preview. After finishing your data flow in
SageMaker Canvas, you can process all of your data and save it in a location that is suitable for your
machine learning workflows.

There are several options for how to proceed after you've finished transforming your data
in Data Wrangler:

- [Create a model](canvas-processing-export-model.md "canvas-processing-export-model.md"). You can create a Canvas model, where you
  directly start creating a model with your prepared data. You can create a model
  either after processing your entire dataset, or by exporting just the sample data
  you worked with in Data Wrangler. Canvas saves your processed data (either the entire
  dataset or the sample data) as a Canvas dataset.

We recommend that you use your sample data for quick iterations, but that you use
your entire data when you want to train your final model. When building tabular
models, datasets larger than 5 GB are automatically downsampled to 5 GB, and for
time series forecasting models, datasets larger than 30 GB are downsampled to 30
GB.

To learn more about creating a model, see [How custom models work](canvas-build-model.md "canvas-build-model.md").

- [Export the data](canvas-export-data.md "canvas-export-data.md"). You can export your data for use in machine
  learning workflows. When you choose to export your data, you have several
  options:
  - You can save your data in the Canvas application as a dataset. For
    more information about the supported file types for Canvas datasets and
    additional requirements when importing data into Canvas, see [Create a dataset](canvas-import-dataset.md "canvas-import-dataset.md").
  - You can save your data to Amazon S3. Depending on the Canvas memory
    availability, your data is processed in the application and then
    exported to Amazon S3. If the size of your dataset exceeds what Canvas can
    process, then by default, Canvas uses an EMR Serverless job to scale to
    multiple compute instances, process your full dataset, and export it to
    Amazon S3. You can also manually configure a SageMaker Processing job to have more
    granular control over the compute resources used to process your
    data.

- [Export a data flow](canvas-export-data-flow.md "canvas-export-data-flow.md"). You might want to save the code for your
  data flow so that you can modify or run your transformations outside of Canvas.
  Canvas provides you with the option to save your data flow transformations as
  Python code in a Jupyter notebook, which you can then export to Amazon S3 for use elsewhere
  in your machine learning workflows.
  When you export your data from a data flow and save it either as a Canvas dataset or
  to Amazon S3, Canvas creates a new destination node in your data flow, which is a final node
  that shows you where your processed data is stored. You can add additional destination nodes
  to your flow if you'd like to perform multiple export operations. For example, you can
  export the data from different points in your data flow to only apply some of the
  transformations, or you can export transformed data to different Amazon S3 locations. For more
  information about how to add or edit a destination node, see
  [Add destination nodes](canvas-destination-nodes-add.md "canvas-destination-nodes-add.md")
  and [Edit a destination node](canvas-destination-nodes-edit.md "canvas-destination-nodes-edit.md").

For more information about setting up a schedule with Amazon EventBridge to automatically
process and export your data on a schedule, see [Create a schedule to automatically
process new data](canvas-data-export-schedule-job.md "canvas-data-export-schedule-job.md").

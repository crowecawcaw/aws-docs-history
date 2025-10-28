# Batch prediction dataset requirements

For batch predictions, make sure that your datasets meet the requirements outlined in
[Create a dataset](canvas-import-dataset.md "canvas-import-dataset.md").
If your dataset is larger than 5 GB, then Canvas uses Amazon EMR Serverless to process
your data and split it into smaller batches. After your data has been split, Canvas uses
SageMaker AI Batch Transform to make predictions. You may see charges from both of these
services after running batch predictions. For more information, see
[Canvas pricing](https://aws.amazon.com/sagemaker/canvas/pricing/ "https://aws.amazon.com/sagemaker/canvas/pricing/").

You might not be able to make predictions on some datasets if they have incompatible
_schemas_. A _schema_ is an organizational structure. For a tabular dataset, the schema
is the names of the columns and the data type of the data in the columns. An
incompatible schema might happen for one of the following reasons:

- The dataset that you're using to make predictions has fewer columns than the
  dataset that you're using to build the model.
- The data types in the columns you used to build the dataset might be different
  from the data types in dataset that you're using to make predictions.
- The dataset that you're using to make predictions and the dataset that you've used
  to build the model have column names that don't match. The column names are case
  sensitive. `Column1` is not the same as `column1`.
  To ensure that you can successfully generate batch predictions, match the schema of your
  batch predictions dataset to the dataset you used to train the model.

###### Note

For batch predictions, if you dropped any columns when building your model, Canvas
adds the dropped columns back to the prediction results. However, Canvas does not
add the dropped columns to your batch predictions for time series models.

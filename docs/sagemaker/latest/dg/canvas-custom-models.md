# Custom models

In Amazon SageMaker Canvas, you can train custom machine learning models tailored to your specific data
and use case. By training a custom model on your data, you are able to capture characteristics and trends that are specific
and most representative of your data. For example, you might want to create a custom time series
forecasting model that you train on inventory data from your warehouse to manage
your logistics operations.

Canvas supports training a range of model types. After training a custom model,
you can evaluate the model's performance and accuracy. Once satisfied with a model, you can make predictions
on new data, and you also have the option to share the custom model with
data scientists for further analysis or to deploy it to a SageMaker AI hosted endpoint for real-time inference, all
from within the Canvas application.

You can train a Canvas custom model on the following types of datasets:

- Tabular (including numeric, categorical, timeseries, and text data)
- Image
  The following table shows the types of custom models that you can build in Canvas, along
  with their supported data types and data sources.

| Model type                     | Example use case                                                                                                       | Supported data types                                        | Supported data sources                   |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------------------------------- |
| Numeric prediction             | Predicting house prices based on features like square footage                                                          | Numeric                                                     | Local upload, Amazon S3, SaaS connectors |
| 2 category prediction          | Predicting whether or not a customer is likely to churn                                                                | Binary or categorical                                       | Local upload, Amazon S3, SaaS connectors |
| 3+ category prediction         | Predicting patient outcomes after being discharged from the<br>hospital                                                | Categorical                                                 | Local upload, Amazon S3, SaaS connectors |
| Time series forecasting        | Predicting your inventory for the next quarter                                                                         | Timeseries                                                  | Local upload, Amazon S3, SaaS connectors |
| Single-label image prediction  | Predicting types of manufacturing defects in images                                                                    | Image (JPG, PNG)                                            | Local upload, Amazon S3                  |
| Multi-category text prediction | Predicting categories of products, such as clothing, electronics, or household<br>goods, based on product descriptions | Source column: text<br>Target column: binary or categorical | Local upload, Amazon S3                  |

**Get started**

To get started with building and generating predictions from a custom model, do the
following:

- Determine your use case and type of model that you want to build. For more information
  about the custom model types, see [How custom models work](canvas-build-model.md "canvas-build-model.md"). For more information about the data types and sources
  supported for custom models, see [Data import](canvas-importing-data.md "canvas-importing-data.md").
- [Import
  your data](canvas-importing-data.md "canvas-importing-data.md") into Canvas. You can build a custom model with any tabular or image
  dataset that meets the input requirements. For more information about the input requirements,
  see [Create a dataset](canvas-import-dataset.md "canvas-import-dataset.md").

To learn more about sample datasets provided by SageMaker AI with which you can experiment, see
[Sample datasets in Canvas](canvas-sample-datasets.md "canvas-sample-datasets.md").

- [Build](canvas-build-model.md "canvas-build-model.md")
  your custom model. You can do a **Quick build** to get your model and start
  making predictions more quickly, or you can do a **Standard build** for greater
  accuracy.

For numeric, categorical, and time series forecasting model types, you can clean and
prepare your data with the [Data Wrangler feature](canvas-data-prep.md "canvas-data-prep.md").
In Data Wrangler, you can create a data flow and use various
data preparation techniques, such as applying advanced transforms or joining datasets. For
image prediction models, you can [Edit an image dataset](canvas-edit-image.md "canvas-edit-image.md") to update your labels or add and delete images. Note that
you can't use these features for multi-category text prediction models.

- [Evaluate
  your model's performance](canvas-evaluate-model.md "canvas-evaluate-model.md") and determine how well it might perform on real-world
  data.
- [Make
  single or batch predictions](canvas-make-predictions.md "canvas-make-predictions.md") with your model.

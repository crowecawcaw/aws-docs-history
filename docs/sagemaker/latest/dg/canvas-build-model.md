# How custom models work

Use Amazon SageMaker Canvas to build a custom model on the dataset that you've imported. Use the model that
you've built to make predictions on new data. SageMaker Canvas uses the information in the dataset to build
up to 250 models and choose the one that performs the best.

When you begin building a model, Canvas automatically recommends one or more _model types_. Model types fall into one of the following
categories:

- **Numeric prediction** – This is known as _regression_ in machine learning. Use the numeric prediction model type
  when you want to make predictions for numeric data. For example, you might want to predict the
  price of houses based on features such as the house’s square footage.
- **Categorical prediction** – This is known as _classification_ in machine learning. When you want to categorize data
  into groups, use the categorical prediction model types:
  - **2 category prediction** – Use the 2 category
    prediction model type (also known as _binary classification_
    in machine learning) when you have two categories that you want to predict for your data. For
    example, you might want to determine whether a customer is likely to churn.
  - **3+ category prediction** – Use the 3+ category
    prediction model type (also known as _multi-class
    classification_ in machine learning) when you have three or more categories that
    you want to predict for your data. For example, you might want to predict a customer's loan
    status based on features such as previous payments.

- **Time series forecasting** – Use time series forecasts
  when you want to make predictions over a period of time. For example, you might want to predict
  the number of items you’ll sell in the next quarter. For information about time series
  forecasts, see [Time Series Forecasts in Amazon SageMaker Canvas](canvas-time-series.md "canvas-time-series.md").
- **Image prediction** – Use the single-label image
  prediction model type (also known as _single-label image
  classification_ in machine learning) when you want to assign labels to images. For
  example, you might want to classify different types of manufacturing defects in images of your
  product.
- **Text prediction** – Use the multi-category text
  prediction model type (also known as _multi-class text
  classification_ in machine learning) when you want to assign labels to passages of
  text. For example, you might have a dataset of customer reviews for a product, and you want to
  determine whether customers liked or disliked the product. You might have your model predict
  whether a given passage of text is `Positive`, `Negative`, or
  `Neutral`.
  For a table of the supported input data types for each model type, see [Custom models](canvas-custom-models.md "canvas-custom-models.md").

For each tabular data model that you build (which includes numeric, categorical, time series
forecasting, and text prediction models), you choose the **Target column**. The
**Target column** is the column that contains the information that you want to
predict. For example, if you're building a model to predict whether people have cancelled their
subscriptions, the **Target column** contains data points that are either a
`yes` or a `no` about someone's cancellation status.

For image prediction models, you build the model with a dataset of images that have been
assigned labels. For the unlabeled images that you provide, the model predicts a label. For
example, if you’re building a model to predict whether an image is a cat or a dog, you provide
images labeled as cats or dogs when building the model. Then, the model can accept unlabeled
images and predict them as either cats or dogs.

**What happens when you build a model**

To build your model, you can choose either a **Quick build** or a
**Standard build**. The **Quick build** has a shorter build
time, but the **Standard build** generally has a higher accuracy.

For tabular and time series forecasting models, Canvas uses _downsampling_
to reduce the size of datasets larger than 5 GB or 30 GB, respectively. Canvas downsamples
with the stratified sampling method. The
table below lists the size of the downsample by model type. To control the sampling process, you
can use Data Wrangler in Canvas to sample using your preferred sampling technique. For time series
data, you can resample to aggregate data points. For more information about sampling, see [Sampling](canvas-transform.md#canvas-transform-sampling "canvas-transform.md#canvas-transform-sampling"). For more
information about resampling time series data, see [Resample Time Series
Data](canvas-transform.md#canvas-resample-time-series "canvas-transform.md#canvas-resample-time-series").

If you choose to do a **Quick build** on a dataset with more than 50,000
rows, then Canvas samples your data down to 50,000 rows for a shorter model training
time.

The following table summarizes key characteristics of the model building process, including
average build times for each model and build type, the size of the downsample when building models
with large datasets, and the minimum and maximum number of data points you should have for each
build type.

| Limit                                                                          | Numeric and categorical prediction                          | Time series forecasting | Image prediction | Text prediction |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------- | ----------------------- | ---------------- | --------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Quick build** time                                                           | 2‐20 minutes                                                | 2‐20 minutes            | 15‐30 minutes    | 15‐30 minutes   |
| **Standard build** time                                                        | 2‐4 hours                                                   | 2‐4 hours               | 2‐5 hours        | 2‐5 hours       |
| Downsample size (the reduced size of a large dataset after Canvas downsamples) | 5 GB                                                        | 30 GB                   | N/A              | N/A             |
| Minimum number of entries (rows) for **Quick builds**                          | 2 category: 500 rows 3+ category, numeric, time series: N/A | N/A                     | N/A              | N/A             |
| Minimum number of entries (rows, images, or documents) for **Standard builds** | 250                                                         | 50                      | 50               | N/A             |
| Maximum number of entries (rows, images, or documents) for **Quick builds**    | N/A                                                         | N/A                     | 5000             | 7500            |
| Maximum number of entries (rows, images, or documents) for **Standard builds** | N/A                                                         | 150,000                 | 180,000          | N/A             |
| Maximum number of columns                                                      | 1,000                                                       | 1,000                   | N/A              | N/A             | Canvas predicts values by using the information in the rest of the dataset, depending on the model type: <br>• For categorical prediction, Canvas puts each row into one of the categories listed in the **Target column**. <br>• For numeric prediction, Canvas uses the information in the dataset to predict the numeric values in the **Target column**. <br>• For time series forecasting, Canvas uses historical data to predict values for the **Target column** in the future. <br>• For image prediction, Canvas uses images that have been assigned labels to predict labels for unlabeled images. <br>• For text prediction, Canvas analyzes text data that has been assigned labels to predict labels for passages of unlabeled text. **Additional features to help you build your model** Before building your model, you can use Data Wrangler in Canvas to prepare your data using 300+ built-in transforms and operators. Data Wrangler supports transforms for both tabular and image datasets. Additionally, you can connect to data sources outside of Canvas, create jobs to apply transforms to your entire dataset, and export your fully prepared and cleaned data for use in ML workflows outside of Canvas. For more information, see [Data preparation](canvas-data-prep.md "canvas-data-prep.md"). To see visualizations and analytics to explore your data and determine which features to include in your model, you can use Data Wrangler’s built-in analyses. You can also access a **Data Quality and Insights Report** that highlights potential issues with your dataset and provides recommendations for how to fix them. For more information, see [Perform exploratory data analysis (EDA)](canvas-analyses.md "canvas-analyses.md"). In addition to the more advanced data preparation and exploration functionality provided through Data Wrangler, Canvas provides some basic features that you can use: <br>• To filter your data and access a set of basic data transforms, see [Prepare data for model building](canvas-prepare-data.md "canvas-prepare-data.md"). <br>• To access simple visualizations and analytics for feature exploration, see [Data exploration and analysis](canvas-explore-data.md "canvas-explore-data.md"). <br>• To learn more about additional features such as previewing your model, validating your dataset, and changing the size of the random sample used to build your model, see [Preview your model](canvas-preview-model.md "canvas-preview-model.md"). For tabular datasets with multiple columns (such as datasets for building categorical, numeric, or time series forecasting model types), you might have rows with missing data points. While Canvas builds the model, it automatically adds missing values. Canvas uses the values in your dataset to perform a mathematical approximation for the missing values. For the highest model accuracy, we recommend adding in the missing data if you can find it. Note that the missing data feature is not supported for text prediction or image prediction models. **Get started** To get started with building a custom model, see [Build a model](canvas-build-model-how-to.md "canvas-build-model-how-to.md") and follow the procedure for the type of model that you want to build. |

Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Getting Started (Python Notebooks)

###### Note

For a complete list of tutorials using Python notebooks, see the Amazon Forecast [Github
Samples](https://github.com/aws-samples/amazon-forecast-samples/tree/master/notebooks "https://github.com/aws-samples/amazon-forecast-samples/tree/master/notebooks") page.

To get started using Amazon Forecast APIs with Python notebooks, see the [Getting Started Tutorial](https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/basic/Getting_Started/Amazon_Forecast_Quick_Start_Guide.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/basic/Getting_Started/Amazon_Forecast_Quick_Start_Guide.ipynb"). The tutorial guides you through the core steps of
Forecast from start to finish.

For basic tutorials for specific processes, refer to the following Python
notebooks:

1. [Preparing data](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/1.Importing_Your_Data.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/1.Importing_Your_Data.ipynb") - Prepare a dataset, create a dataset group, define the schema,
   and import the dataset group.
2. [Building your predictor](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/2.Building_Your_Predictor.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/2.Building_Your_Predictor.ipynb") - Train a predictor on the data you imported into your Forecast dataset.
3. [Evaluating predictors](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/3.Evaluating_Your_Predictor.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/3.Evaluating_Your_Predictor.ipynb") - Obtain predictions, visualize predictions, and compare
   results.
4. [Retraining predictors](https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/advanced/Retraining_AutoPredictor/Retraining.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/advanced/Retraining_AutoPredictor/Retraining.ipynb") - Retrain an existing predictor with updated data.
5. [Upgrade to AutoPredictor](https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/basic/Upgrading_to_AutoPredictor/UpgradeToAutoPredictor.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/basic/Upgrading_to_AutoPredictor/UpgradeToAutoPredictor.ipynb") - Upgrade legacy predictors to AutoPredictor.
6. [Clean Up](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/4.Cleanup.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/basic/Tutorial/4.Cleanup.ipynb") - Delete the dataset groups, predictors, forecasts created during the
   tutorials.
   To repeat the Getting Started tutorial with AutoML, see [Getting Started with AutoML](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Getting_started_with_AutoML/Getting_started_with_AutoML.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Getting_started_with_AutoML/Getting_started_with_AutoML.ipynb").

## Advanced Tutorials

For more advanced tutorials, refer to the following Python notebooks:

- [Item-level Explainability](https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/advanced/Item_Level_Explainability/Item_Level_Explanability.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/main/notebooks/advanced/Item_Level_Explainability/Item_Level_Explanability.ipynb") - Understand how dataset attributes impact
  forecasts for specific time series and time points.
- [Comparing multiple models](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Compare_Multiple_Models/Compare_Multiple_Models.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Compare_Multiple_Models/Compare_Multiple_Models.ipynb") - Create predictors using Prophet, ETS, and DeepAR+, and compare their
  performances by visualizing the results.
- [Cold start forecasting](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Forecast%20with%20Cold%20Start%20Items/Forecast%20with%20Cold%20Start%20Items.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Forecast%20with%20Cold%20Start%20Items/Forecast%20with%20Cold%20Start%20Items.ipynb") - Use item metadata and the DeepAR+ algorithm to
  forecast for cold-start scenarios (when there is little to no historical data).
- [Incorporating related time-series datasets](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Incorporating_Related_Time_Series_dataset_to_your_Predictor/Incorporating_Related_Time_Series_dataset_to_your_Predictor.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Incorporating_Related_Time_Series_dataset_to_your_Predictor/Incorporating_Related_Time_Series_dataset_to_your_Predictor.ipynb") - Use related time-series datasets
  to improve the accuracy of your model.
- [Incorporating item metadata](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Incorporating_Item_Metadata_Dataset_to_your_Predictor/Incorporating_Item_Metadata_Dataset_to_your_Predictor.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Incorporating_Item_Metadata_Dataset_to_your_Predictor/Incorporating_Item_Metadata_Dataset_to_your_Predictor.ipynb") - Use item metadata to improve the accuracy of
  your model.
- [Using the Weather Index](https://github.com/aws-samples/amazon-forecast-samples/tree/master/notebooks/advanced/Weather_index "https://github.com/aws-samples/amazon-forecast-samples/tree/master/notebooks/advanced/Weather_index") - Use the Weather Index to incorporate historical and
  projected weather information when training your predictors.
- [Performing What-if analysis](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/WhatIf_Analysis/WhatIf_Analysis.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/WhatIf_Analysis/WhatIf_Analysis.ipynb") - Explore different pricing scenarios and
  evaluate how it impacts demand.
- [Evaluate item-level accuracy](https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Item_Level_Accuracy/Item_Level_Accuracy_Using_Bike_Example.ipynb "https://github.com/aws-samples/amazon-forecast-samples/blob/master/notebooks/advanced/Item_Level_Accuracy/Item_Level_Accuracy_Using_Bike_Example.ipynb") - Export backtest metrics and forecasts, and
  evaluate the item-level performance of your predictor.

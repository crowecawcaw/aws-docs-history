

# Tutorial: Build an end-to-end machine learning workflow in SageMaker Canvas
<a name="canvas-end-to-end-machine-learning-workflow"></a>

This tutorial guides you through an end-to-end machine learning (ML) workflow using Amazon SageMaker Canvas. SageMaker Canvas is a visual no-code interface that you can use to prepare data and to train and deploy ML models. For the tutorial, you use a NYC taxi dataset to train a model that predicts the fare amount for a given trip. You get hands-on experience with key ML tasks such as assessing data quality and addressing data issues, splitting data into training and test sets, model training and evaluation, making predictions, and deploying your trained model–all within the SageMaker Canvas application.

**Important**  
This tutorial assumes that you or your administrator have created an AWS account. For information about creating an AWS account, see [Getting started: Are you a first time AWS User?](https://docs.aws.amazon.com/accounts/latest/reference/welcome-first-time-user.html)

## Setting up
<a name="canvas-tutorial-setting-up"></a>

An Amazon SageMaker AI domain is a centralized place to manage all your Amazon SageMaker AI environments and resources. A domain acts as a virtual boundary for your work in SageMaker AI, providing isolation and access control for your machine learning (ML) resources. 

To get started with Amazon SageMaker Canvas, you or your administrator must navigate to the SageMaker AI console and create a Amazon SageMaker AI domain. A domain has the storage and compute resources needed for you to run SageMaker Canvas. Within the domain, you configure SageMaker Canvas to access your Amazon S3 buckets and deploy models. Use the following procedure to set up a quick domain and create a SageMaker Canvas application.

**To set up SageMaker Canvas**

1. Navigate to the [SageMaker AI console](https://console.aws.amazon.com/sagemaker).

1. On the left-hand navigation, choose SageMaker Canvas.

1. Choose **Create a SageMaker AI domain**.

1. Choose **Set up**. The domain can take a few minutes to set up.

The preceding procedure used a quick domain set up. You can perform an advanced set up to control all aspects of the account configuration, including permissions, integrations, and encryption. For more information about a custom set up, see [Use custom setup for Amazon SageMaker AI](onboard-custom.md).

By default, doing the quick domain set up provides you with permissions to deploy models. If you have custom permissions set up through a standard domain and you need manually grant model deployment permissions, see [Permissions management](canvas-deploy-model.md#canvas-deploy-model-prereqs).

## Flow creation
<a name="canvas-tutorial-flow-creation"></a>

Amazon SageMaker Canvas is a machine learning platform that enables users to build, train, and deploy machine learning models without extensive coding or machine learning expertise. One of the powerful features of Amazon SageMaker Canvas is the ability to import and work with large datasets from various sources, such as Amazon S3.

For this tutorial, we're using the NYC taxi dataset to predict the fare amount for each trip using a Amazon SageMaker Canvas Data Wrangler data flow. The following procedure outlines the steps for importing a modified version of the NYC taxi dataset into a data flow.

**Note**  
For improved processing, SageMaker Canvas imports a sample of your data. By default, it randomly samples 50,000 rows.

**To import the NYC taxi dataset**

1. From the SageMaker Canvas home page, choose **Data Wrangler**.

1. Choose **Import data**.

1. Select **Tabular**.

1. Choose the toolbox next to data source.

1. Select **Amazon S3** from the dropdown.

1. For **Input S3 endpoint**, specify `s3://{{amazon-sagemaker-data-wrangler-documentation-artifacts}}/{{canvas-single-file-nyc-taxi-dataset}}.csv`

1. Choose **Go**.

1. Select the checkbox next to the dataset.

1. Choose **Preview data**.

1. Choose **Save**.

## Data Quality and Insights Report 1 (sample)
<a name="canvas-tutorial-data-quality-insights-report-1"></a>

After importing a dataset into Amazon SageMaker Canvas, you can generate a Data Quality and Insights report on a sample of the data. Use it to provide valuable insights into the dataset. The report does the following:
+ Assesses the dataset's completeness
+ Identifies missing values and outliers

It can identify other potential issues that may impact model performance. It also evaluates the predictive power of each feature concerning the target variable, allowing you to identify the most relevant features for problem you're trying to solve.

We can use the insights from the report to predict the fare amount. By specifying the **Fare amount** column as the target variable and selecting **Regression** as the problem type, the report will analyze the dataset's suitability for predicting continuous values like fare prices. The report should reveal that features like **year** and **hour\_of\_day** have low predictive power for the chosen target variable, providing you with valuable insights.

Use the following procedure to get a Data Quality and Insights report on a 50,000 row sample from the dataset.

**To get a report on a sample**

1. Choose **Get data insights** from the pop up window next to the **Data types** node.

1. For **Analysis name**, specify a name for the report.

1. For **Problem type**, choose **Regression**.

1. For **Target column**, choose **Fare amount**.

1. Choose **Create**.

You can review the Data Quality and Insights report on a sample of your data. The report indicates that the **year** and **hour\_of\_day** features are not predictive of the target variable, **Fare amount**.

At the top of the navigation, choose the name of the data flow to navigate back to it.

## Drop year and hour of day
<a name="canvas-tutorial-drop-year-and-hour-of-day"></a>

We're using insights from the report to drop the **year** and **hour\_of\_day** columns to streamline the feature space and potentially improve model performance.

Amazon SageMaker Canvas provides a user-friendly interface and tools to perform such data transformations.

Use the following procedure to drop the **year** and **hour\_of\_day** columns from the NYC taxi dataset using the Data Wrangler tool in Amazon SageMaker Canvas.

1. Choose the icon next to **Data types**.

1. Choose **Add step**.

1. In the search bar, write **Drop column**.

1. Choose **Manage columns**.

1. Choose **Drop column**.

1. For **Columns to drop**, select the **year** and **hour\_of\_day** columns.

1. Choose **Preview** to view how your transform changes your data.

1. Choose **Add**.

You can use the preceding procedure as the basis to add all of the other transforms in SageMaker Canvas.

## Data Quality and Insights Report 2 (full dataset)
<a name="canvas-tutorial-data-quality-insights-report-2"></a>

For the previous insights report, we used a sample of the NYC taxi dataset. For our second report, we're running a comprehensive analysis on the entire dataset to identify potential issues impacting model performance.

Use the following procedure to create a Data Quality and Insights report on an entire dataset.

**To get a report on the entire dataset**

1. Choose the icon next to the **Drop columns** node.

1. Choose **Get data insights**.

1. For **Analysis name**, specify a name for the report.

1. For **Problem type**, choose **Regression**.

1. For **Target column**, choose **Fare amount**.

1. For **Data size**, choose **Full dataset**.

1. Choose **Create**.

The following is an image from the insights report:

![Duplicate rows, Skewed target, and Very low quick model score are listed as the insights.](http://docs.aws.amazon.com/sagemaker/latest/dg/images/canvas-tutorial-dqi-insights.png)


It shows the following issues:
+ Duplicate rows
+ Skewed target

Duplicate rows can lead to data leakage, where the model is exposed to the same data during training and testing. They can lead to overly optimistic performance metrics. Removing duplicate rows ensures that the model is trained on unique instances, reducing the risk of data leakage and improving the model's ability to generalize.

A skewed target variable distribution, in this case, the **Fare amount** column, can cause imbalanced classes, where the model may become biased towards the majority class. This can lead to poor performance on minority classes, which is particularly problematic in scenarios where accurately predicting rare or underrepresented instances is important.

## Addressing data quality issues
<a name="canvas-tutorial-addressing-data-quality-issues"></a>

To address these issues and prepare the dataset for modeling, you can search for the following transformations and apply them:

1. Drop duplicates using the **Manage rows** transform.

1. **Handle outliers** in the **Fare amount** column using the **Robust standard deviation numeric outliers**.

1. **Handle outliers** in the **Trip distance** and **Trip duration** columns using the **Standard deviation numeric outliers**.

1. Use the **Encode categorical** to encode the **Rate code id**, **Payment type**, **Extra flag**, and **Toll flag** columns as floats.

If you're not sure about how to apply a transform, see [Drop year and hour of day](#canvas-tutorial-drop-year-and-hour-of-day)

By addressing these data quality issues and applying appropriate transformations, you can improve the dataset's suitability for modeling.

## Verifying data quality and quick model accuracy
<a name="canvas-tutorial-verifying-data-quality-and-quick-model-accuracy"></a>

After applying the transforms to address data quality issues, such as removing duplicate rows, we create our final Data Quality and Insights report. This report helps verify that the applied transformations resolved the issues and that the dataset is now in a suitable state for modeling.

When reviewing the final Data Quality and Insights report, you should expect to see no major data quality issues flagged. The report should indicate that:
+ The target variable is no longer skewed
+ There are no outliers or duplicate rows

Additionally, the report should provide a quick model score based on a baseline model trained on the transformed dataset. This score serves as an initial indicator of the model's potential accuracy and performance.

Use the following procedure to create the Data Quality and Insights report.

**To create the Data Quality and Insights report**

1. Choose the icon next to the **Drop columns** node.

1. Choose **Get data insights**.

1. For **Analysis name**, specify a name for the report.

1. For **Problem type**, choose **Regression**.

1. For **Target column**, choose **Fare amount**.

1. For **Data size**, choose **Full dataset**.

1. Choose **Create**.

## Split the data into training and test sets
<a name="canvas-tutorial-split-data"></a>

To train a model and evaluate its performance, we use the **Split data** transform to split the data into training and test sets.

By default, SageMaker Canvas uses a Randomized split, but you can also use the following types of splits:
+ Ordered
+ Stratified
+ Split by key

You can change the **Split percentage** or add splits.

For this tutorial, use all of the default settings in the split. You need to double click on the dataset to view its name. The training dataset has the name **Dataset (Train)**.

Next to the **Ordinal encode** node apply the **Split data** transform.

## Train model
<a name="canvas-tutorial-train-model"></a>

After you split your data, you can train a model. This model learns from patterns in your data. You can use it to make predictions or uncover insights.

SageMaker Canvas has both quick builds and standard builds. Use a standard build to train best performing model on your data.

Before you start training a model, you must first export the training dataset as a SageMaker Canvas dataset.

**To export your dataset**

1. Next to the node for the training dataset, choose the icon and select **Export**.

1. Select **SageMaker Canvas dataset**.

1. Choose **Export** to export the dataset.

After you've created a dataset, you can train a model on the SageMaker Canvas dataset that you've created. For information about training a model, see [Build a custom numeric or categorical prediction model](canvas-build-model-how-to.md#canvas-build-model-numeric-categorical).

## Evaluate model and make predictions
<a name="canvas-tutorial-evaluate-model-and-make-predictions"></a>

After training your machine learning model, it's crucial to evaluate its performance to ensure it meets your requirements and performs well on unseen data. Amazon SageMaker Canvas provides a user-friendly interface to assess your model's accuracy, review its predictions, and gain insights into its strengths and weaknesses. You can use the insights to make informed decisions about its deployment and potential areas for improvement.

Use the following procedure to evaluate a model before you deploy it.

**To evaluate a model**

1. Choose **My Models**.

1. Choose the model you've created.

1. Under **Versions**, select the version corresponding to the model.

You can now view the model evaluation metrics.

After you evaluate the model, you can make predictions on new data. We're using the test dataset that we've created.

To use the test dataset for predictions we need to convert it into a SageMaker Canvas dataset. The SageMaker Canvas dataset is in a format that the model can interpret.

Use the following procedure to create a SageMaker Canvas dataset from the test dataset.

**To create a SageMaker Canvas dataset**

1. Next to the **Dataset (Test)** dataset, choose the radio icon.

1. Select **Export**.

1. Select **SageMaker Canvas dataset**.

1. For **Dataset name**, specify a name for the dataset.

1. Choose **Export**.

Use the following procedure to make predictions. It assumes that you're still on the **Analyze** page.

**To make predictions on test dataset**

1. Choose **Predict**.

1. Choose **Manual**.

1. Select the dataset that you've exported.

1. Choose **Generate predictions**.

1. When SageMaker Canvas has finished generating predictions, select the icon to the right of the dataset.

1. Choose **Preview** to view the predictions.

## Deploy a model
<a name="canvas-tutorial-deploy-a-model"></a>

After you've evaluated your model, you can deploy it to an endpoint. You can submit requests to the endpoint to get predictions.

Use the following procedure to deploy a model. It assumes that you're still on the **Predict** page.

**To deploy a model**

1. Choose **Deploy**.

1. Choose **Create deployment**.

1. Choose **Deploy**.

## Cleaning up
<a name="canvas-tutorial-cleaning-up"></a>

You've successfully completed the tutorial. To avoid incurring additional charges, delete the resources that you're not using.

Use the following procedure to delete the endpoint that you created. It assumes that you're still on the **Deploy** page.

**To delete an endpoint**

1. Choose the radio button to the right of your deployment.

1. Select **Delete deployment**.

1. Choose **Delete**.

After deleting the deployment, delete the datasets that you've created within SageMaker Canvas. Use the following procedure to delete the datasets.

**To delete the datasets**

1. Choose **Datasets** on the left-hand navigation.

1. Select the dataset that you've analyzed and the synthetic dataset used for predictions.

1. Choose **Delete**.

To avoid incurring additional charges, you must log out of SageMaker Canvas. For more information, see [Logging out of Amazon SageMaker Canvas](canvas-log-out.md).
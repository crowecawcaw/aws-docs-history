Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Generating Forecasts

After you create an Amazon Forecast predictor, you are ready to create a forecast. By default, a forecast includes
predictions for every item (`item_id`) in the dataset group that was used to train the predictor.
However, you can specify a subset of items that are used to generate a forecast.

After you create a forecast, you can export it to your Amazon Simple Storage Service
(Amazon S3) bucket.

###### Topics

- [Creating a forecast](#exporting-forecast "#exporting-forecast")
- [Specifying time series](#forecast-time-series "#forecast-time-series")
- [Exporting a forecast](#export-forecast "#export-forecast")
- [Querying a forecast](#query-forecast "#query-forecast")
- [Coldstart Forecasts](#coldstart-forecast "#coldstart-forecast")

## Creating a forecast

You can create a forecast with the Forecast console, AWS CLI, or AWS SDKs. The status of your predictor must be
**Active** before you can generate a forecast.

Console

###### To create a forecast

1. Sign in to the AWS Management Console and open the Amazon Forecast console at [https://console.aws.amazon.com/forecast/](https://console.aws.amazon.com/forecast/ "https://console.aws.amazon.com/forecast/").
2. From **Dataset groups**, choose your dataset group.
3. On your dataset group's **Dashboard**, under **Generate
   forecasts**, choose **Create a forecast**. The **Create a
   forecast** page appears.
4. On the **Create a forecast** page, for **Forecast
   details**, provide a name for your forecast and choose the predictor you want to use
   to create forecasts.
5. For **Forecast quantiles**, optionally specify the quantiles at which probabilistic forecasts are generated.
   The default quantiles are the quantiles you specified during predictor creation.
6. Optionally, choose the radio button for **Selected Items** to specify a subset of
   time series that are used for forecast generation.
7. Optionally, add any tags for the forecast. For more information see [Tagging Amazon Forecast Resources](tagging-forecast-resources.md "tagging-forecast-resources.md").
8. Choose **Start**. The **Forecasts** page appears.

The **Status** column lists the status of your forecast. Wait for Amazon Forecast to finish creating the forecast. The process can
take several minutes or longer. When your forecast has been created, the status transitions to **Active**.

Now that your forecast has been created, you can export the
forecast. See [Exporting a forecast](#export-forecast "#export-forecast").

CLI
To create a forecast with the AWS CLI, use the `create-forecast` command.
Provide a name for the forecast and the Amazon Resource Name (ARN) of your predictor. For `forecast-types`,
optionally specify the quantiles at which probabilistic forecasts are generated.
The default values are the quantiles you specified when you created the predictor.
Optionally add any tags for the forecast. For more information see [Tagging Amazon Forecast Resources](tagging-forecast-resources.md "tagging-forecast-resources.md").

For information on
required and optional parameters see [CreateForecast](API_CreateForecast.md "API_CreateForecast.md").

```
aws forecast create-forecast \
--forecast-name `forecast_name` \
--forecast-types 0.1 0.5 0.9 \
--predictor-arn arn:aws:forecast:`region`:`account_number`:predictor/`predictorName` \
--tags Key=`key1`,Value=`value1` Key=`key2`,Value=`value2`
```

Python
To create a forecast with the SDK for Python (Boto3), use the `create_forecast` method.
Provide a name for the forecast and the Amazon Resource Name (ARN) of your predictor. For `ForecastTypes`,
optionally specify the quantiles at which probabilistic forecasts are generated.
The default values are the quantiles you specified when you created the predictor.
Optionally add any tags for the forecast. For more information see [Tagging Amazon Forecast Resources](tagging-forecast-resources.md "tagging-forecast-resources.md").

For information on
required and optional parameters see [CreateForecast](API_CreateForecast.md "API_CreateForecast.md").

```
import boto3

forecast = boto3.client('forecast')

create_forecast_response = forecast.create_forecast(
   ForecastName = "`Forecast_Name`",
   ForecastTypes = ["0.1", "0.5", "0.9"],        # optional, the default types/quantiles are what you specified for the predictor
   PredictorArn = "arn:aws:forecast:`region`:`accountNumber`:predictor/`predictorName`",
   Tags = [
      {
         "Key": "`key1`",
         "Value": "`value1`"
      },
      {
         "Key": "`key2`",
         "Value": "`value2`"
      }
   ]
)
forecast_arn = create_forecast_response['ForecastArn']
print(forecast_arn)
```

## Specifying time series

###### Note

A time series is a combination of the item (item_id) and all dimensions in your datasets.

To specify a list of time series, upload a CSV file identifying the time series by
their item_id and dimension values to an S3 bucket. You must also define the attributes and attribute types of the time series
in a schema.

For example, a retailer may want to know how an advertising campaign impacts sales for a
specific item (`item_id`) at a specific store location
(`store_location`). In this use case, you would specify the time
series that is the combination of item_id and store_location.

The following CSV file selects the following five time series:

1. Item_id: 001, store_location: Seattle
2. Item_id: 001, store_location: New York
3. Item_id: 002, store_location: Seattle
4. Item_id: 002, store_location: New York
5. Item_id: 003, store_location: Denver

```
001, Seattle
001, New York
002, Seattle
002, New York
003, Denver
```

The schema defines the first column as `item_id` and the second column
as `store_location`.

Forecast creation is skipped for any time series that you specify that are not in the input dataset. The
forecast export file will not contain these time series or their forecasted values.

## Exporting a forecast

After you create a forecast, you can export it to an Amazon S3 bucket. Exporting a forecast copies the forecast
to your Amazon S3 bucket as a CSV file (by default), and the exported data includes all attributes of any item metadata
dataset in addition to item predictions. You can specify the Parquet file format when you export a
forecast.

The granularity of the exported forecasts (such as hourly, daily, or weekly) is the forecast frequency that you
specified when you created the predictor.
You can optionally specify an AWS Key Management Service key to encrypt the data before it's written to the bucket.

###### Note

Export files can directly return information from the Dataset Import. This makes
the files vulnerable to CSV injection if the imported data contains formulas or
commands. For this reason, exported files can prompt security warnings. To avoid
malicious activity, disable links and macros when reading exported files.

Console

###### To export a forecast

1. In the navigation pane, under your dataset group, choose
   **Forecasts**.
2. Choose the radio button for your forecast and choose **Create forecast export**. The **Create forecast
   export** page is displayed.
3. On the **Create forecast export** page, for **Export
   details**, provide the following information.
   - **Export name** – Enter a name for your forecast export
     job.
   - **Generated forecast** – From the drop-down menu, choose
     the forecast that you created in `Step 3: Create a Forecast`.
   - **IAM role** – Either keep the default **Enter a custom
     IAM role ARN** or choose **Create a new role** to have Amazon Forecast create the role for you.
   - **Custom IAM role ARN** – If you are entering a custom IAM role, enter the Amazon Resource Name
     (ARN) of the IAM role that you created in [Create an IAM Role for
     Amazon Forecast (IAM Console)](aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console "aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console").
   - **KMS key ARN** – If you use AWS Key Management Service for bucket encryption, provide the Amazon Resource Name (ARN) of the AWS KMS key.
   - **S3 forecast export location** – Use the following
     format to enter the location of your Amazon Simple Storage Service (Amazon S3) bucket or folder in the
     bucket:

   `s3://<name of your S3 bucket>/<folder
 path>/`

4. Choose **Create forecast export**. The
   **my_forecast** page is displayed.

Wait for Amazon Forecast to finish exporting the forecast. The process can take several minutes or
longer. When your forecast has been exported, the status transitions to
**Active** and you can find the forecast files in your Amazon S3
bucket.

CLI
To export a forecast with the AWS CLI you use the `export-forecast-job` command. Give the
forecast export job a name, specify the ARN of the forecast to export, and optionally add any tags.
For the `destination`, specify the path to your output Amazon S3 bucket, the ARN of the IAM role that you created in [Create an IAM Role for
Amazon Forecast (IAM Console)](aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console "aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console"), and if you use a AWS KMS key for bucket encryption, the ARN for your key.

For more information about required and optional parameters, see
[CreateForecastExportJob](API_CreateForecastExportJob.md "API_CreateForecastExportJob.md")
operation.

```
forecast create-forecast-export-job \
--forecast-export-job-name `exportJobName` \
--forecast-arn arn:aws:forecast:`region`:`acctNumber`:forecast/`forecastName` \
--destination S3Config="{Path='s3://`bucket`/`folderName`',RoleArn='arn:aws:iam::`acctNumber`:role/`Role`, KMSKeyArn='arn:aws:kms:`region`:`accountNumber`:key/`keyID`'}"
--tags Key=`key1`,Value=`value1` Key=`key2`,Value=`value2`
```

Python
To export a forecast with the SDK for Python (Boto3) you use the `export_forecast_job` method. Give the
forecast export job a name, specify the ARN of the forecast to export, and optionally add any tags.
For the `Destination`, specify the path to your output Amazon S3 bucket, the ARN of the IAM role that you created in [Create an IAM Role for
Amazon Forecast (IAM Console)](aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console "aws-forecast-iam-roles.md#aws-forecast-create-iam-role-with-console"), and if you use a AWS KMS key for bucket encryption, the ARN for your key.

For more information about required and optional parameters, see
[CreateForecastExportJob](API_CreateForecastExportJob.md "API_CreateForecastExportJob.md")
operation.

```
import boto3

forecast = boto3.client('forecast')

export_forecast_response = forecast.create_forecast_export_job(
   Destination = {
      "S3Config": {
         "Path": "s3://`bucketName`/`folderName`/",
         "RoleArn": "arn:aws:iam::`accountNumber`:role/`roleName`",
         "KMSKeyArn": "arn:aws:kms:`region`:`accountNumber`:key/`keyID`"
      }
   },
   ForecastArn = "arn:aws:forecast:`region`:`accountNumber`:forecast/`forecastName`",
   ForecastExportJobName = "`export_job_name`",
   Tags = [
      {
         "Key": "`key1`",
         "Value": "`value1`"
      },
      {
         "Key": "`key2`",
         "Value": "`value2`"
      }
   ]
)
forecast_export_job_arn = export_forecast_response["ForecastExportJobArn"]
print(forecast_export_job_arn)
```

## Querying a forecast

You can query a forecast using the
[QueryForecast](API_forecastquery_QueryForecast.md "API_forecastquery_QueryForecast.md")
operation. By default, the complete range of the forecast is returned.
You can request a specific date range within the complete forecast.

When you query a forecast you must specify filtering criteria. A filter is a key-value
pair. The key is one of the schema attribute names (including forecast dimensions)
from one of the datasets used to create the
forecast. The _value_ is a valid values for the specified key. You can
specify multiple key-value pairs. The returned forecast will only contain items that satisfy
all the criteria.

## Coldstart Forecasts

A common challenge faced by customers in industries such as retail, manufacturing, or consumer packaged goods is to generate forecasts for items with no historical data. This scenario is known as coldstart forecasting and is typically encountered when businesses introduce new products to market, on-board brands or catalogues, or cross-sell products in new regions.

Amazon Forecast requires item metadata to perform coldstart forecasting. Leveraging item characteristics found in the item metadata, Forecast explicitly identifies items in the item metadata that are similar to the item with no historical data. Forecast uses the demand characteristics of the existing items to generate a coldstart forecast for the new item.

Amazon Forecast identifies coldstart items as those items that are included in the item metadata file but are not included in the target time series file. To correctly identify a coldstart item, ensure that the item ID of the coldstart item is entered as a row in the item metadata file and that it is not entered in the target time series file. For multiple coldstart items, enter each item ID as a separate row in the item metadata file. If the coldstart item does not have an item ID, you can use any alphanumeric combination less than 64 characters and not already used by another item in dataset.

Coldstart forecasting requires both an item metadata dataset and an AutoPredictor.

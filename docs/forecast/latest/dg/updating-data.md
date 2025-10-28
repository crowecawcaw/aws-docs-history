Amazon Forecast is no longer available to new customers. Existing customers of
Amazon Forecast can continue to use the service as normal.
[Learn more"](https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/ "https://aws.amazon.com/blogs/machine-learning/transition-your-amazon-forecast-usage-to-amazon-sagemaker-canvas/")

# Updating Data

As you collect new data, you will want to import that data into Forecast. To do so, you have two options, replacement and incremental updates. A replacement dataset import job will overwrite all existing data with the newly imported data. An incremental update will append the newly imported data to the dataset.

After importing your new data, you can use an existing predictor to generate a forecast for that data.

###### Topics

- [Import modes](#idsi "#idsi")
- [Updating existing datasets](#idsi-console "#idsi-console")
- [Updating forecasts](#update-data-new-forecasts "#update-data-new-forecasts")

## Import modes

To configure how Amazon Forecast adds new data to existing dataset, you specify the import
mode for your dataset import job. The default import mode is `FULL`. You can
only configure the import mode by using the Amazon Forecast API.

- To overwrite all existing data in your dataset, specify `FULL` in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") API operation.
- To append the records to the existing data in your dataset, specify `INCREMENTAL`
  in the [CreateDatasetImportJob](API_CreateDatasetImportJob.md "API_CreateDatasetImportJob.md") API operation. If an existing
  record and an imported record have the same timeseries ID (item ID, dimension,
  and timestamp), then the existing record is replaced with the newly imported
  record. Amazon Forecast always uses the record with the most recent timestamp.

If you have not imported a dataset, the incremental option is not available. The default import mode is a full replacement.

### Incremental import mode guidelines

When you perform an incremental dataset import, you cannot change the timestamp format, data format, or geolocation data. To change any of these items, you need to perform a full data dataset import.

## Updating existing datasets

###### Important

By default, a dataset import job replaces any existing data in the dataset that you imported into. You can change this by specifying the dataset import job's [Import modes](#idsi "#idsi").

To update a dataset, create a dataset import job for the dataset and specify the import mode.

CLI
To update a dataset, use the `create-dataset-import-job` command. For the `import-mode`, specify `FULL`, to replace existing data or `INCREMENTAL` to add to it. For more information, see [Import modes](#idsi "#idsi").

The following code shows how to create a dataset import job that incrementally imports new data into a dataset.

```
aws forecast create-dataset-import-job \
                        --dataset-import-job-name `dataset import job name` \
                        --dataset-arn `dataset arn` \
                        --data-source "S3Config":{"KMSKeyArn":"`string`", "Path":"`string`", "RoleArn":"`string`"} \
                        --import-mode `INCREMENTAL`
```

Python
To update a dataset, use the `create_dataset_import_job` method. For the `import-mode`, specify `FULL`, to replace existing data or `INCREMENTAL` to add to it. For more information, see [Import modes](#idsi "#idsi").

```
import boto3

forecast = boto3.client('forecast')

response = forecast.create_dataset_import_job(
    datasetImportJobName = '`YourImportJob`',
    datasetArn = '`dataset_arn`',
    dataSource = {"S3Config":{"KMSKeyArn":"`string`", "Path":"`string`", "RoleArn":"`string`"}},
    importMode = '`INCREMENTAL`'
)
```

## Updating forecasts

As you collect new data, you might want to use it to generate new forecasts. Forecast
does not automatically retrain a predictor when you import an updated dataset, but you
can manually retrain a predictor to generate a new forecast with the updated data. For
instance, if you collect daily sales data and want to include new data points in your
forecast, you could import the updated data and use it to generate a forecast without
training a new predictor. For newly imported data to have an impact on your forecasts,
you must retrain the predictor.

###### To generate a forecast from the new data:

1. Upload the new data to an Amazon S3 bucket. Your new data should contain only the data added since your last data set import.
2. Create an **Incremental** dataset import job with the new
   data. The new data is appended to the existing data and the forecast is
   generated from the updated data. If your new data file contains both
   previously-imported data and new data, create a **Full**
   dataset import job.
3. Create a new forecast using the existing predictor.
4. Retrieve the forecast as usual.

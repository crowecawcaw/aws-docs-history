End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Creating a dataset

You retrieve data from a data store by creating a SQL dataset or a container dataset. AWS IoT Analytics can query the data to answer analytical questions.
Although a data store is not a database, you use SQL expressions to query the data and produce results that are stored in a dataset.

###### Topics

- [Querying data](#query-data "#query-data")
- [Accessing the queried data](#access-queried-data "#access-queried-data")

## Querying data

To query the data, you create a dataset. A dataset contains the SQL that you use to query the data store
along with an optional schedule that repeats the query at a day and time you choose. You create the optional schedules
using expressions similar to [Amazon CloudWatch schedule expressions](../../../AmazonCloudWatch/latest/events/ScheduledEvents.md "../../../AmazonCloudWatch/latest/events/ScheduledEvents.md").

Run the following command to create a dataset.

```
aws iotanalytics create-dataset --cli-input-json file://mydataset.json
```

Where the `mydataset.json` file contains the following content.

```
{
    "datasetName": "mydataset",
    "actions": [
        {
            "actionName":"myaction",
            "queryAction": {
                "sqlQuery": "select * from mydatastore"
            }
        }
    ]
}
```

Run the following command to create the dataset content by executing the query.

```
aws iotanalytics create-dataset-content --dataset-name mydataset
```

Wait a few minutes for the dataset content to be created before you continue.

## Accessing the queried data

The result of the query is your dataset content, stored as a file, in CSV format.
The file is made available to you through Amazon S3. The following example shows how you can check that
your results are ready and download the file.

Run the following `get-dataset-content` command.

```
aws iotanalytics get-dataset-content --dataset-name mydataset
```

If your dataset contains any data, then the output from `get-dataset-content`,
has `"state": "SUCCEEDED"` in the `status` field, like this
the following example.

```
{
    "timestamp": 1508189965.746,
    "entries": [
        {
          "entryName": "someEntry",
          "dataURI": "https://aws-iot-analytics-datasets-f7253800-859a-472c-aa33-e23998b31261.s3.amazonaws.com/results/f881f855-c873-49ce-abd9-b50e9611b71f.csv?X-Amz-"

        }
    ],
    "status": {
      "state": "SUCCEEDED",
      "reason": "A useful comment."
    }
}
```

`dataURI` is a signed URL to the output results. It is valid for a short period of time (a few hours).
Depending on your workflow, you might want to always call `get-dataset-content` before you access the content
because calling this command generates a new signed URL.

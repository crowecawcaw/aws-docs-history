End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Create a dataset with AWS IoT SiteWise data (AWS CLI)

Run the following AWS CLI commands to get started querying your AWS IoT SiteWise data.

The examples shown here use the AWS Command Line Interface (AWS CLI). For more information on the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). For more information about the CLI commands available
for AWS IoT Analytics, see [iotanalytics](../../../cli/latest/reference/iotanalytics/index.md "../../../cli/latest/reference/iotanalytics/index.md") in the _AWS Command Line Interface Reference_.

###### To create a dataset

1. Run the following `create-dataset` command to create a dataset.

```
aws iotanalytics create-dataset --cli-input-json file://my_dataset.json
```

Where the `my_dataset.json` file contains the following content.

```
{
    "datasetName": "my_dataset",
    "actions": [
        {
            "actionName":"my_action",
            "queryAction": {
                "sqlQuery": "SELECT * FROM my_iotsitewise_datastore.asset_metadata LIMIT 5"
            }
        }
    ]
}
```

For more information about supported SQL functionality in AWS IoT Analytics, see [SQL expressions in AWS IoT Analytics](sql-support.md "sql-support.md"). Or, see
[Tutorial: Query AWS IoT SiteWise data in AWS IoT Analytics](tutorial-query-mls.md "tutorial-query-mls.md") for examples of statistical queries that can provide insight to your data. 2. Run the following `create-dataset-content` command to create your dataset content by running your query.

```
aws iotanalytics create-dataset-content --dataset-name my_dataset
```

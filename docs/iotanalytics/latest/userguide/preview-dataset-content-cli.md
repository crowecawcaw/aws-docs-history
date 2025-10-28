End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# Access dataset content in AWS IoT Analytics (AWS CLI)

If your dataset contains any data, you can preview and download your SQL query results.

The examples shown here use the AWS Command Line Interface (AWS CLI). For more information on the AWS CLI, see the
[AWS Command Line Interface User Guide](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). For more information about the CLI commands available
for AWS IoT Analytics, see [iotanalytics](../../../cli/latest/reference/iotanalytics/index.md "../../../cli/latest/reference/iotanalytics/index.md") in the _AWS Command Line Interface Reference_.

###### To access your AWS IoT Analytics dataset results (AWS CLI)

1. Run the following `get-dataset-content` command to view the result of your query.

```
aws iotanalytics get-dataset-content --dataset-name my_iotsitewise_dataset
```

2. If your dataset contains any data, then the output from `get-dataset-content`,
   has `"state": "SUCCEEDED"` in the `status` field, such as in the following example.

```
{
    "timestamp": 1508189965.746,
    "entries": [
        {
          "entryName": "my_entry_name",
          "dataURI": "https://aws-iot-analytics-datasets-f7253800-859a-472c-aa33-e23998b31261.s3.amazonaws.com/results/f881f855-c873-49ce-abd9-b50e9611b71f.csv?X-Amz-"

        }
    ],
    "status": {
      "state": "SUCCEEDED",
      "reason": "A useful comment."
    }
}
```

3. The output from `get-dataset-content` includes a `dataURI`, which is a signed URL to the output results. It is valid for a short period of time (a few hours). Visit the `dataURI` URL to access your SQL query results.

###### Note

Depending on your workflow, you might want to always call `get-dataset-content` before you access the content
because calling this command generates a new signed URL.

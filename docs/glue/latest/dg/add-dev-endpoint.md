# Adding a development endpoint

Use development endpoints to iteratively develop and test your extract, transform, and load
(ETL) scripts in AWS Glue. Working with development endpoints is only available through the AWS Command Line Interface.

1. In a command line window, enter a command similar to the following.

```
aws glue create-dev-endpoint --endpoint-name "endpoint1" --role-arn "arn:aws:iam::`account-id`:role/`role-name`" --number-of-nodes "3" --glue-version "1.0" --arguments '{"GLUE_PYTHON_VERSION": "3"}' --region "`region-name`"
```

This command specifies AWS Glue version 1.0. Because this version supports both Python 2 and
Python 3, you can use the `arguments` parameter to indicate the desired Python
version. If the `glue-version` parameter is omitted, AWS Glue version 0.9 is assumed.
For more information about AWS Glue versions, see the [Glue version job property](add-job.md#glue-version-table "add-job.md#glue-version-table").

For information about additional command line parameters, see [create-dev-endpoint](../../../cli/latest/reference/glue/create-dev-endpoint.md "../../../cli/latest/reference/glue/create-dev-endpoint.md") in the _AWS CLI Command Reference_. 2. (Optional) Enter the following command to check the development endpoint status. When the
status changes to `READY`, the development endpoint is ready to use.

```
aws glue get-dev-endpoint --endpoint-name "endpoint1"
```

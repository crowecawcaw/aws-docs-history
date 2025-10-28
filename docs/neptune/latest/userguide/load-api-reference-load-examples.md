# Neptune Loader Examples

This example demonstrates how to use the Neptune loader to load data into a Neptune graph database using the
Gremlin CSV format. The request is sent as an HTTP POST request to the Neptune loader endpoint, and the request
body contains the necessary parameters to specify the data source, format, IAM role, and other configuration options.
The response includes the load ID, which can be used to track the progress of the data loading process.

###### Example Request

The following is a request sent via HTTP POST using the `curl` command.
It loads a file in the Neptune CSV format. For more information, see [Gremlin load data format](bulk-load-tutorial-format-gremlin.md "bulk-load-tutorial-format-gremlin.md").

```
curl -X POST \
    -H 'Content-Type: application/json' \
    https://`your-neptune-endpoint`:`port`/loader -d '
    {
      "source" : "s3://`bucket-name`/`object-key-name`",
      "format" : "csv",
      "iamRoleArn" : "`ARN for the IAM role you are using`",
      "region" : "`region`",
      "failOnError" : "`FALSE`",
      "parallelism" : "`MEDIUM`",
      "updateSingleCardinalityProperties" : "`FALSE`",
      "queueRequest" : "`FALSE`"
    }'
```

###### Example Response

```
{
    "status" : "200 OK",
    "payload" : {
        "loadId" : "`ef478d76-d9da-4d94-8ff1-08d9d4863aa5`"
    }
}
```
